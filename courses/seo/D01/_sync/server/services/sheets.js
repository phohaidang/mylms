/**
 * Google Sheets Service — Database wrapper
 * 
 * In dev mode (no GOOGLE_SHEETS_ID): uses in-memory JSON store
 * In production: uses Google Sheets API v4
 */

import { google } from 'googleapis';
import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { Readable } from 'stream';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const DATA_DIR = join(__dirname, '..', '..', 'data');
const MOCK_DB_PATH = join(DATA_DIR, '_mock_db.json');

const IS_MOCK = !process.env.GOOGLE_SHEETS_ID;
const IS_VERCEL = !!process.env.VERCEL;

// Ensure data directory exists (ONLY when NOT on Vercel)
if (!IS_VERCEL && !existsSync(DATA_DIR)) {
  mkdirSync(DATA_DIR, { recursive: true });
}

// ============ MOCK MODE (in-memory + file persist) ============
let mockData = {
  students: [],
  quiz_attempts: [],
  exam_attempts: [],
  manual_grades: [],
  ebook_progress: [],
  course_config: [],
  session_feedback: [],
  attendance_log: []
};

if (IS_MOCK && existsSync(MOCK_DB_PATH)) {
  try {
    mockData = JSON.parse(readFileSync(MOCK_DB_PATH, 'utf-8'));
  } catch (e) {
    console.warn('Could not load mock DB, starting fresh');
  }
}

function saveMockDB() {
  if (IS_VERCEL) return; // Cannot write to disk on Vercel
  writeFileSync(MOCK_DB_PATH, JSON.stringify(mockData, null, 2));
}

// ============ GOOGLE SHEETS MODE ============
let sheets = null;
let drive = null;
const SPREADSHEET_ID = process.env.GOOGLE_SHEETS_ID;

try {
  if (!IS_MOCK) {
    const auth = new google.auth.GoogleAuth({
      credentials: {
        client_email: process.env.GOOGLE_SERVICE_ACCOUNT_EMAIL,
        private_key: process.env.GOOGLE_PRIVATE_KEY 
          ? process.env.GOOGLE_PRIVATE_KEY.replace(/\\n/g, '\n').replace(/"/g, '') 
          : undefined
      },
      scopes: ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file']
    });
    sheets = google.sheets({ version: 'v4', auth });
    drive = google.drive({ version: 'v3', auth });
  }
} catch (err) {
  console.error('❌ Google API Init Error:', err);
}


// ============ UNIFIED API ============

/**
 * Get all rows from a sheet/table
 */
export async function getAll(sheetName) {
  if (IS_MOCK || !sheets) {
    return mockData[sheetName] || [];
  }
  
  try {
    const res = await sheets.spreadsheets.values.get({
      spreadsheetId: SPREADSHEET_ID,
      range: `${sheetName}!A:Z`
    });
    
    const rows = res.data.values;
    if (!rows || rows.length < 2) return [];
    
    const headers = rows[0].map(h => String(h || '').trim().toLowerCase());
    return rows.slice(1).map(row => {
      const obj = {};
      headers.forEach((h, i) => { 
        if (h) obj[h] = row[i] || ''; 
      });
      return obj;
    });
  } catch (err) {
    // If sheet not found (400) or other sheet errors, return empty array
    if (err.response && (err.response.status === 400 || err.response.status === 404)) {
      console.warn(`Sheet "${sheetName}" not found or empty. Returning [].`);
      return [];
    }
    throw err;
  }
}

/**
 * Find rows matching a condition
 */
export async function find(sheetName, predicate) {
  const all = await getAll(sheetName);
  return all.filter(predicate);
}

/**
 * Find one row matching a condition
 */
export async function findOne(sheetName, predicate) {
  const all = await getAll(sheetName);
  return all.find(predicate);
}

/**
 * Count rows matching a condition
 */
export async function count(sheetName, predicate) {
  const all = await getAll(sheetName);
  return all.filter(predicate).length;
}


async function ensureSheetExists(sheetName) {
  try {
    const ss = await sheets.spreadsheets.get({ spreadsheetId: SPREADSHEET_ID });
    const sheetExists = ss.data.sheets.some(s => s.properties.title === sheetName);
    if (!sheetExists) {
      await sheets.spreadsheets.batchUpdate({
        spreadsheetId: SPREADSHEET_ID,
        requestBody: {
          requests: [{ addSheet: { properties: { title: sheetName } } }]
        }
      });
      console.log(`📝 Auto-created sheet: ${sheetName}`);
    }
  } catch (err) {
    console.error(`Error ensuring sheet ${sheetName} exists:`, err);
  }
}

/**
 * Append a row to a sheet
 */
export async function append(sheetName, data) {
  if (IS_MOCK || !sheets) {
    if (!mockData[sheetName]) mockData[sheetName] = [];
    mockData[sheetName].push(data);
    saveMockDB();
    return data;
  }
  
  await ensureSheetExists(sheetName);
  
  const all = await getAll(sheetName);
  const headers = all.length > 0
    ? Object.keys(all[0])
    : Object.keys(data);
  
  // If sheet is totally empty (no headers), write headers first
  if (all.length === 0) {
    await sheets.spreadsheets.values.update({
      spreadsheetId: SPREADSHEET_ID,
      range: `${sheetName}!A1`,
      valueInputOption: 'RAW',
      requestBody: { values: [headers] }
    });
  }
  
  const row = headers.map(h => {
    const val = data[h];
    return typeof val === 'object' ? JSON.stringify(val) : String(val ?? '');
  });
  
  await sheets.spreadsheets.values.append({
    spreadsheetId: SPREADSHEET_ID,
    range: `${sheetName}!A:Z`,
    valueInputOption: 'RAW',
    requestBody: { values: [row] }
  });
  
  return data;
}

/**
 * Update a row matching a condition
 */
export async function update(sheetName, predicate, newData) {
  if (IS_MOCK || !sheets) {
    const arr = mockData[sheetName] || [];
    const idx = arr.findIndex(predicate);
    if (idx >= 0) {
      mockData[sheetName][idx] = { ...arr[idx], ...newData };
      saveMockDB();
      return mockData[sheetName][idx];
    }
    return null;
  }
  
  await ensureSheetExists(sheetName);
  
  // For Google Sheets: read all, find row index, update
  const res = await sheets.spreadsheets.values.get({
    spreadsheetId: SPREADSHEET_ID,
    range: `${sheetName}!A:Z`
  });
  
  const rows = res.data.values;
  if (!rows || rows.length < 2) return null;
  
  const headers = rows[0].map(h => String(h || '').trim().toLowerCase());
  
  // Check if we need to add new columns
  const newDataKeys = Object.keys(newData).map(k => k.toLowerCase());
  const missingHeaders = newDataKeys.filter(k => !headers.includes(k));
  
  if (missingHeaders.length > 0) {
    const updatedHeaders = [...rows[0], ...missingHeaders];
    await sheets.spreadsheets.values.update({
      spreadsheetId: SPREADSHEET_ID,
      range: `${sheetName}!A1`,
      valueInputOption: 'RAW',
      requestBody: { values: [updatedHeaders] }
    });
    // Refresh headers for current operation
    missingHeaders.forEach(h => headers.push(h));
  }

  for (let i = 1; i < rows.length; i++) {
    const obj = {};
    headers.forEach((h, j) => { 
      if (h) obj[h] = rows[i][j] || ''; 
    });
    
    if (predicate(obj)) {
      const merged = { ...obj, ...newData };
      const updatedRow = headers.map((h, j) => {
        const val = merged[h];
        return typeof val === 'object' ? JSON.stringify(val) : String(val ?? '');
      });
      
      await sheets.spreadsheets.values.update({
        spreadsheetId: SPREADSHEET_ID,
        range: `${sheetName}!A${i + 1}:Z${i + 1}`,
        valueInputOption: 'RAW',
        requestBody: { values: [updatedRow] }
      });
      return merged;
    }
  }
  return null;
}

/**
 * Count rows matching a condition
 */
export async function count(sheetName, predicate) {
  const all = await getAll(sheetName);
  return predicate ? all.filter(predicate).length : all.length;
}

/**
 * Upload a file buffer to Google Drive
 */
export async function uploadToDrive(fileName, mimeType, buffer) {
  if (IS_MOCK || !drive) {
     console.warn('DRIVE MOCK: Skipped uploading', fileName, 'to Drive.');
     return `http://mock-drive-link/${fileName}`;
  }

  const folderId = process.env.GOOGLE_DRIVE_FOLDER_ID;
  const fileMetadata = {
    name: fileName,
    parents: folderId ? [folderId] : []
  };

  const stream = new Readable();
  stream.push(buffer);
  stream.push(null);

  const media = {
    mimeType: mimeType,
    body: stream
  };

  try {
    const file = await drive.files.create({
      resource: fileMetadata,
      media: media,
      fields: 'id, webViewLink'
    });
    return file.data.webViewLink;
  } catch (err) {
    console.error('Google Drive Upload error:', err);
    throw err;
  }
}

/**
 * Create a backup of the spreadsheet on Google Drive
 */
export async function createBackup() {
  if (IS_MOCK || !drive || !sheets) return { message: 'Mock mode or API Error: no backup created' };
  
  try {
    const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
    const ss = await sheets.spreadsheets.get({ spreadsheetId: SPREADSHEET_ID });
    const originalTitle = ss.data.properties.title;
    
    const response = await drive.files.copy({
      fileId: SPREADSHEET_ID,
      requestBody: {
        name: `[BACKUP] ${originalTitle} (${timestamp})`,
      }
    });
    
    return {
      success: true,
      backup_id: response.data.id,
      name: response.data.name
    };
  } catch (err) {
    console.error('Backup error:', err);
    throw err;
  }
}

/**
 * Export all data from all known sheets as a single JSON object
 */
export async function exportAllData() {
  if (IS_MOCK || !sheets) return mockData;
  
  try {
    const ss = await sheets.spreadsheets.get({ spreadsheetId: SPREADSHEET_ID });
    const sheetNames = ss.data.sheets.map(s => s.properties.title);
    
    const allData = {};
    for (const name of sheetNames) {
      allData[name] = await getAll(name);
    }
    return allData;
  } catch (err) {
    console.error('Export error:', err);
    throw err;
  }
}

export default { getAll, find, findOne, append, update, count, uploadToDrive, createBackup, exportAllData };

if (IS_MOCK) {
  console.log('📋 Database: Mock mode (in-memory + file persist)');
} else {
  console.log('📋 Database: Google Sheets connected');
}
