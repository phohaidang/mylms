/**
 * SEED SCRIPT - Lớp AI26.D7.01 (Kỹ năng ứng dụng AI trong học tập và nghiên cứu)
 * Tự động đọc danh sách từ roster-AI26.D7.01.md và import vào Google Sheets
 * 
 * Chạy: node courses/ky-nang-ai-hub/AI26.D7.01/seed-ai26.js
 */

import dotenv from 'dotenv';
import { google } from 'googleapis';
import bcrypt from 'bcryptjs';
import { readFileSync, writeFileSync, unlinkSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));

// Nạp file .env từ đúng thư mục lớp (courses/ky-nang-ai-hub/AI26.D7.01/.env)
dotenv.config({ path: join(__dirname, '.env') });

const SPREADSHEET_ID = process.env.GOOGLE_SHEETS_ID;
const SHEET_NAME = 'students';
const ROSTER_PATH = join(__dirname, '..', 'roster-AI26.D7.01.md');

// Hàm đọc và trích xuất sinh viên từ file Markdown
function loadStudentsFromMarkdown(path) {
  if (!existsSync(path)) {
    throw new Error(`Không tìm thấy file roster tại: ${path}`);
  }
  const content = readFileSync(path, 'utf-8');
  const lines = content.split('\n');
  const students = [];

  for (const line of lines) {
    // Tìm các dòng chứa dữ liệu bảng: | STT | MSSV | Họ và Tên | Email Đăng Nhập |
    const match = line.match(/^\|\s*(\d+)\s*\|\s*(\w+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|/);
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
  console.log('🚀 Bắt đầu seed tài khoản sinh viên lớp AI26.D7.01 vào Google Sheets...\n');
  
  if (!SPREADSHEET_ID) {
    console.error('❌ Lỗi: GOOGLE_SHEETS_ID chưa được thiết lập trong .env');
    console.error('   Vui lòng mở file courses/ky-nang-ai-hub/AI26.D7.01/.env và điền GOOGLE_SHEETS_ID trước khi chạy seed.');
    process.exit(1);
  }

  const students = loadStudentsFromMarkdown(ROSTER_PATH);
  console.log(`📋 Nguồn: ${ROSTER_PATH}`);
  console.log(`📋 Spreadsheet ID: ${SPREADSHEET_ID}`);
  console.log(`📋 Sheet name: ${SHEET_NAME}`);
  console.log(`👤 Tổng số sinh viên: ${students.length} sinh viên (+ 1 admin + 1 trợ lý)\n`);

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
  const adminPassword = process.env.ADMIN_PASSWORD || 'admin2026';
  const studentDefaultPassword = 'hub' + new Date().getFullYear(); // e.g. hub2026
  const adminHash = await bcrypt.hash(adminPassword, 10);
  const studentHash = await bcrypt.hash(studentDefaultPassword, 10);
  const trolyHash = await bcrypt.hash('demo2026', 10);
  console.log(`   ✅ Admin password: ${adminPassword}`);
  console.log(`   ✅ Student default password: ${studentDefaultPassword}\n`);

  const now = new Date().toISOString();
  const headers = ['student_id', 'email', 'full_name', 'password', 'role', 'must_change_password', 'created_at', 'password_hash'];
  
  const adminRow = [
    'ADMIN',
    process.env.ADMIN_EMAIL || 'dangph@hub.edu.vn',
    process.env.ADMIN_NAME || 'ThS. Phó Hải Đăng',
    '',
    'admin',
    'false',
    now,
    adminHash
  ];

  const trolyRow = [
    'TROLY-01',
    'troly@st.hub.edu.vn',
    'Trợ Lý Nghiên Cứu',
    '',
    'student',
    'false',
    now,
    trolyHash
  ];
  
  const studentRows = students.map(([id, email, name]) => [
    id, email, name, '', 'student', 'false', now, studentHash
  ]);

  const allRows = [headers, adminRow, trolyRow, ...studentRows];

  try {
    // 1. Kiểm tra sheet 'students' đã tồn tại chưa
    const spreadsheet = await sheets.spreadsheets.get({ spreadsheetId: SPREADSHEET_ID });
    const existingSheet = spreadsheet.data.sheets?.find(s => s.properties?.title === SHEET_NAME);

    if (!existingSheet) {
      console.log(`📄 Đang tạo sheet mới "${SHEET_NAME}"...`);
      await sheets.spreadsheets.batchUpdate({
        spreadsheetId: SPREADSHEET_ID,
        requestBody: {
          requests: [
            {
              addSheet: {
                properties: {
                  title: SHEET_NAME,
                  gridProperties: { rowCount: allRows.length + 50, columnCount: 10 }
                }
              }
            }
          ]
        }
      });
      console.log(`   ✅ Đã tạo sheet "${SHEET_NAME}"`);
    } else {
      console.log(`⚠️ Sheet "${SHEET_NAME}" đã tồn tại. Đang xóa dữ liệu cũ để ghi mới...`);
      await sheets.spreadsheets.values.clear({
        spreadsheetId: SPREADSHEET_ID,
        range: `${SHEET_NAME}!A:Z`
      });
    }

    // 2. Ghi toàn bộ dữ liệu
    console.log(`📤 Đang ghi ${allRows.length} dòng dữ liệu...`);
    await sheets.spreadsheets.values.update({
      spreadsheetId: SPREADSHEET_ID,
      range: `${SHEET_NAME}!A1`,
      valueInputOption: 'RAW',
      requestBody: { values: allRows }
    });

    console.log('\n🎉 Hoàn thành! Đã seed thành công tài khoản lớp AI26.D7.01 vào Google Sheets.');
  } catch (err) {
    console.error('❌ Lỗi khi thao tác Google Sheets:', err.message);
    if (err.message.includes('permission') || err.message.includes('403')) {
      console.error('\n⚠️ Nhớ CHIA SẺ Google Sheet với email Service Account (quyền Editor):');
      console.error(`   👉 ${process.env.GOOGLE_SERVICE_ACCOUNT_EMAIL}`);
    }
  } finally {
    // Dọn dẹp key tạm
    if (existsSync(tmpKeyPath)) {
      unlinkSync(tmpKeyPath);
    }
  }
}

seed();
