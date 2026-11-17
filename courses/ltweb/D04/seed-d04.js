/**
 * SEED SCRIPT - Lớp ITS708_261_1_D04 (Lập trình Web)
 * Tự động đọc danh sách từ roster-ITS708-D04.md và import vào Google Sheets
 */

import dotenv from 'dotenv';
import { google } from 'googleapis';
import bcrypt from 'bcryptjs';
import { readFileSync, writeFileSync, unlinkSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));

// Nạp file .env từ đúng thư mục lớp (courses/ltweb/D04/.env)
dotenv.config({ path: join(__dirname, '.env') });

const SPREADSHEET_ID = process.env.GOOGLE_SHEETS_ID;
const SHEET_NAME = 'students';
const ROSTER_PATH = join(__dirname, '..', 'roster-ITS708-D04.md');

// Hàm đọc và trích xuất sinh viên từ file Markdown
function loadStudentsFromMarkdown(path) {
  if (!existsSync(path)) {
    throw new Error(`Không tìm thấy file roster tại: ${path}`);
  }
  const content = readFileSync(path, 'utf-8');
  const lines = content.split('\n');
  const students = [];

  for (const line of lines) {
    // Tìm các dòng chứa dữ liệu bảng: | STT | MSSV | Họ Tên | Email | SĐT | Lớp |
    const match = line.match(/^\|\s*(\d+)\s*\|\s*(\d{12})\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]*)\s*\|\s*([^|]+)\s*\|/);
    if (match) {
      const mssv = match[2].trim();
      const fullName = match[3].trim();
      const email = match[4].trim();
      students.push([mssv, email, fullName]);
    }
  }
  return students;
}

async function seed() {
  console.log('🚀 Bắt đầu seed tài khoản sinh viên lớp D04 vào Google Sheets...\n');
  
  if (!SPREADSHEET_ID) {
    console.error('❌ Lỗi: GOOGLE_SHEETS_ID chưa được thiết lập trong .env');
    console.error('   Vui lòng mở file courses/ltweb/D04/.env và điền GOOGLE_SHEETS_ID trước khi chạy seed.');
    process.exit(1);
  }

  const students = loadStudentsFromMarkdown(ROSTER_PATH);
  console.log(`📋 Nguồn: ${ROSTER_PATH}`);
  console.log(`📋 Spreadsheet ID: ${SPREADSHEET_ID}`);
  console.log(`📋 Sheet name: ${SHEET_NAME}`);
  console.log(`👤 Tổng số sinh viên: ${students.length} sinh viên (+ 1 admin)\n`);

  // Tạo JSON key file tạm từ env vars
  const keyData = {
    type: 'service_account',
    client_email: process.env.GOOGLE_SERVICE_ACCOUNT_EMAIL,
    private_key: process.env.GOOGLE_PRIVATE_KEY?.replace(/\\n/g, '\n').replace(/^"|"$/g, ''),
    token_uri: 'https://oauth2.googleapis.com/token'
  };

  const tmpKeyPath = join(__dirname, '_tmp_key.json');
  writeFileSync(tmpKeyPath, JSON.stringify(keyData));

  const auth = new google.auth.GoogleAuth({
    keyFile: tmpKeyPath,
    scopes: ['https://www.googleapis.com/auth/spreadsheets']
  });

  const sheets = google.sheets({ version: 'v4', auth });

  // Hash passwords
  console.log('🔒 Đang tạo mật khẩu bcrypt hash...');
  const adminPassword = process.env.ADMIN_PASSWORD || 'Admin@2026';
  const studentDefaultPassword = 'hub' + new Date().getFullYear(); // e.g. hub2026
  const adminHash = await bcrypt.hash(adminPassword, 10);
  const studentHash = await bcrypt.hash(studentDefaultPassword, 10);
  console.log(`   ✅ Admin password: ${adminPassword}`);
  console.log(`   ✅ Student default password: ${studentDefaultPassword}\n`);

  const now = new Date().toISOString();
  const headers = ['student_id', 'email', 'full_name', 'password', 'role', 'must_change_password', 'created_at'];
  const adminRow = [
    'admin',
    process.env.ADMIN_EMAIL || 'dangph@hub.edu.vn',
    process.env.ADMIN_NAME || 'ThS. Phó Hải Đăng',
    adminHash,
    'admin',
    'false',
    now
  ];
  
  const studentRows = students.map(([id, email, name]) => [
    id, email, name, studentHash, 'student', 'true', now
  ]);
  const allRows = [headers, adminRow, ...studentRows];

  try {
    console.log('🧹 Xóa dữ liệu cũ trên sheet students...');
    await sheets.spreadsheets.values.clear({
      spreadsheetId: SPREADSHEET_ID,
      range: `${SHEET_NAME}!A:G`
    });

    console.log('📝 Ghi dữ liệu tài khoản mới...');
    await sheets.spreadsheets.values.update({
      spreadsheetId: SPREADSHEET_ID,
      range: `${SHEET_NAME}!A1`,
      valueInputOption: 'RAW',
      requestBody: { values: allRows }
    });

    console.log('\n=============================================');
    console.log('✅ SEED TÀI KHOẢN D04 THÀNH CÔNG!');
    console.log('=============================================');
    console.log(`   👨‍🏫 Admin: ${adminRow[1]} / ${adminPassword}`);
    console.log(`   👨‍🎓 ${students.length} sinh viên / Mật khẩu mặc định: ${studentDefaultPassword}`);
    console.log('=============================================\n');
  } catch (err) {
    console.error('❌ Lỗi seed:', err.message);
    if (err.response) console.error('   Response:', JSON.stringify(err.response.data, null, 2));
    process.exit(1);
  } finally {
    try { unlinkSync(tmpKeyPath); } catch {}
  }
}

seed();
