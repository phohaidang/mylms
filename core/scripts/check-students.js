// Quick check: read first 5 students from SEO D01 Google Sheet
import dotenv from 'dotenv';
import { google } from 'googleapis';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
dotenv.config({ path: join(__dirname, '..', 'courses', 'seo', 'D01', '.env') });

const auth = new google.auth.GoogleAuth({
  credentials: {
    client_email: process.env.GOOGLE_SERVICE_ACCOUNT_EMAIL,
    private_key: process.env.GOOGLE_PRIVATE_KEY?.replace(/\\n/g, '\n').replace(/"/g, '')
  },
  scopes: ['https://www.googleapis.com/auth/spreadsheets.readonly']
});

const sheets = google.sheets({ version: 'v4', auth });

async function check() {
  try {
    const res = await sheets.spreadsheets.values.get({
      spreadsheetId: process.env.GOOGLE_SHEETS_ID,
      range: 'students!A:E'
    });
    
    const rows = res.data.values;
    if (!rows || rows.length === 0) {
      console.log('No data found');
      return;
    }
    
    console.log('Headers:', rows[0]);
    console.log('\nFirst 5 students:');
    for (let i = 1; i <= Math.min(5, rows.length - 1); i++) {
      console.log(`  ${i}. student_id="${rows[i][0]}" | email="${rows[i][1]}" | name="${rows[i][2]}"`);
    }
    console.log(`\nTotal students: ${rows.length - 1}`);
    
    // Search for the specific student
    const target = rows.find(r => r[0]?.includes('030239230123') || r[1]?.includes('030239230123'));
    if (target) {
      console.log('\n🔍 Found target student:', target);
    } else {
      console.log('\n❌ Student 030239230123 NOT found in sheet');
      // Show all student_ids for comparison
      console.log('\nAll student_ids:');
      rows.slice(1).forEach(r => console.log(`  "${r[0]}"`));
    }
  } catch (err) {
    console.error('Error:', err.message);
  }
}

check();
