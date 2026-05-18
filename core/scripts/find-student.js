import dotenv from 'dotenv';
import { google } from 'googleapis';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
// Load the specific class .env
dotenv.config({ path: join(__dirname, '..', '..', 'courses', 'seo', 'D01', '.env') });

const pkey = process.env.GOOGLE_PRIVATE_KEY.replace(/\\n/g, '\n').replace(/"/g, '');

const auth = new google.auth.GoogleAuth({
  credentials: {
    client_email: process.env.GOOGLE_SERVICE_ACCOUNT_EMAIL,
    private_key: pkey
  },
  scopes: ['https://www.googleapis.com/auth/spreadsheets']
});

const sheets = google.sheets({ version: 'v4', auth });

async function run() {
  try {
    const res = await sheets.spreadsheets.values.get({
      spreadsheetId: process.env.GOOGLE_SHEETS_ID,
      range: 'students!A:E'
    });
    const rows = res.data.values || [];
    console.log('Headers:', rows[0]);
    console.log('Total students:', rows.length - 1);
    
    // Check if the student with ID 030239230123 exists
    const searchId = '030239230123';
    const match = rows.find(r => r[0] === searchId || r[1]?.includes(searchId));
    if (match) {
      console.log('FOUND MATCH IN SHEET:', match);
      console.log({
        student_id: match[0],
        email: match[1],
        full_name: match[2],
        role: match[3],
        password_hash: match[4]
      });
    } else {
      console.log(`Student ${searchId} NOT FOUND in Sheet!`);
      console.log('Sample of first 10 students:');
      rows.slice(1, 11).forEach(r => console.log(`ID: "${r[0]}", Email: "${r[1]}", Name: "${r[2]}"`));
    }
  } catch (err) {
    console.error('Error fetching sheet:', err);
  }
}

run();
