/**
 * Seed Guest Account cho LMS Demo
 * Chạy: node seed-guest.js
 */
import bcrypt from 'bcryptjs';
import { GoogleSpreadsheet } from 'google-spreadsheet';
import { JWT } from 'google-auth-library';
import dotenv from 'dotenv';

dotenv.config();

const GUEST_ACCOUNT = {
  student_id: 'GUEST001',
  email: 'guest@demo.lms',
  full_name: 'Khách Trải Nghiệm',
  password: 'demo2026',
  role: 'student',
  must_change_password: false
};

async function seedGuest() {
  console.log('🔐 Hashing password...');
  const password_hash = await bcrypt.hash(GUEST_ACCOUNT.password, 10);
  console.log('✅ Hash:', password_hash);

  console.log('📊 Connecting to Google Sheet...');
  const auth = new JWT({
    email: process.env.GOOGLE_SERVICE_ACCOUNT_EMAIL,
    key: process.env.GOOGLE_PRIVATE_KEY.replace(/\\n/g, '\n'),
    scopes: ['https://www.googleapis.com/auth/spreadsheets'],
  });

  const doc = new GoogleSpreadsheet(process.env.GOOGLE_SHEETS_ID, auth);
  await doc.loadInfo();
  console.log('✅ Connected to:', doc.title);

  // Find students sheet
  const sheet = doc.sheetsByTitle['students'];
  if (!sheet) {
    console.log('❌ Sheet "students" not found! Available sheets:', Object.keys(doc.sheetsByTitle).join(', '));
    return;
  }

  // Check if guest already exists
  const rows = await sheet.getRows();
  const existing = rows.find(r => r.get('email') === GUEST_ACCOUNT.email);
  if (existing) {
    console.log('⚠️ Guest account already exists, updating password...');
    existing.set('password_hash', password_hash);
    existing.set('must_change_password', 'false');
    await existing.save();
    console.log('✅ Password updated!');
  } else {
    console.log('➕ Adding guest account...');
    await sheet.addRow({
      student_id: GUEST_ACCOUNT.student_id,
      email: GUEST_ACCOUNT.email,
      full_name: GUEST_ACCOUNT.full_name,
      password_hash: password_hash,
      role: GUEST_ACCOUNT.role,
      must_change_password: 'false',
      created_at: new Date().toISOString(),
      last_login: ''
    });
    console.log('✅ Guest account created!');
  }

  console.log('\n🎉 Done! Guest credentials:');
  console.log(`   Email: ${GUEST_ACCOUNT.email}`);
  console.log(`   Password: ${GUEST_ACCOUNT.password}`);
}

seedGuest().catch(err => {
  console.error('❌ Error:', err.message);
  process.exit(1);
});
