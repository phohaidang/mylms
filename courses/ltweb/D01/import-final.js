import { readFileSync } from 'fs';
import { google } from 'googleapis';
import bcrypt from 'bcryptjs';

// Parse .env manually to be absolutely sure about the key
function getEnv() {
  const content = readFileSync('.env', 'utf-8');
  const env = {};
  
  // Regex to find GOOGLE_PRIVATE_KEY="content" spanning multiple lines
  const keyMatch = content.match(/GOOGLE_PRIVATE_KEY="([\s\S]+?)"/);
  if (keyMatch) {
    env.GOOGLE_PRIVATE_KEY = keyMatch[1];
  }
  
  // Other vars
  const otherVars = ['GOOGLE_SHEETS_ID', 'GOOGLE_SERVICE_ACCOUNT_EMAIL', 'ADMIN_EMAIL', 'ADMIN_PASSWORD', 'ADMIN_NAME'];
  otherVars.forEach(v => {
    const m = content.match(new RegExp(`${v}=(.+)`));
    if (m) env[v] = m[1].trim();
  });
  
  return env;
}

const env = getEnv();
const SHEET_NAME = 'students';
const MD_FILE_PATH = 'd:/ITS717_252_1_D01.md';

function decodeEntities(str) {
  return str.replace(/&#(\d+);/g, (match, dec) => String.fromCharCode(dec)).trim();
}

function parseStudentFile(path) {
  const content = readFileSync(path, 'utf-8');
  const students = [];
  const rowRegex = /<tr>\s*<td[^>]*>\d+<\/td>\s*<td[^>]*>(\d+)<\/td>\s*<td[^>]*>[^<]*<\/td>\s*<td>([^<]*)<\/td>\s*<td>([^<]*)<\/td>/g;
  let match;
  while ((match = rowRegex.exec(content)) !== null) {
    const id = match[1];
    const hoLot = decodeEntities(match[2]);
    const ten = decodeEntities(match[3]);
    students.push([id, `${id}@st.hub.edu.vn`, `${hoLot} ${ten}`.replace(/\s+/g, ' ').trim()]);
  }
  return students;
}

async function run() {
  const students = parseStudentFile(MD_FILE_PATH);
  console.log(`✅ Đã tìm thấy ${students.length} sinh viên.`);

  let key = env.GOOGLE_PRIVATE_KEY;
  // Clean: remove literal \n and real newlines
  key = key.replace(/\\n/g, '\n').replace(/\r/g, '');
  
  const auth = new google.auth.GoogleAuth({
    credentials: {
      client_email: env.GOOGLE_SERVICE_ACCOUNT_EMAIL,
      private_key: key,
    },
    scopes: ['https://www.googleapis.com/auth/spreadsheets']
  });

  const sheets = google.sheets({ version: 'v4', auth });

  console.log('🔒 Hashing...');
  const adminHash = await bcrypt.hash(env.ADMIN_PASSWORD || 'Admin@2026', 10);
  const studentHash = await bcrypt.hash('hub2026', 10);

  const now = new Date().toISOString();
  const rows = [
    ['student_id', 'email', 'full_name', 'password_hash', 'role', 'must_change_password', 'created_at'],
    ['admin', env.ADMIN_EMAIL, env.ADMIN_NAME, adminHash, 'admin', 'false', now],
    ...students.map(s => [s[0], s[1], s[2], studentHash, 'student', 'true', now])
  ];

  try {
    console.log('🧹 Clearing...');
    await sheets.spreadsheets.values.clear({ spreadsheetId: env.GOOGLE_SHEETS_ID, range: `${SHEET_NAME}!A:G` });
    console.log('📝 Updating...');
    await sheets.spreadsheets.values.update({
      spreadsheetId: env.GOOGLE_SHEETS_ID,
      range: `${SHEET_NAME}!A1`,
      valueInputOption: 'RAW',
      requestBody: { values: rows }
    });
    console.log('✅ DONE!');
  } catch (err) {
    console.error('❌ Error:', err.message);
  }
}

run();
