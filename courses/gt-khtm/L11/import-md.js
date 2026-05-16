/**
 * IMPORT SCRIPT — Import sinh viên từ file .md (HTML Table) vào Google Sheets
 */

import 'dotenv/config';
import { google } from 'googleapis';
import bcrypt from 'bcryptjs';
import { readFileSync } from 'fs';
import { dirname } from 'path';
import { fileURLToPath } from 'url';

const SPREADSHEET_ID = process.env.GOOGLE_SHEETS_ID;
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
    const fullName = `${hoLot} ${ten}`.replace(/\s+/g, ' ').trim();
    const email = `${id}@st.hub.edu.vn`;
    students.push([id, email, fullName]);
  }
  return students;
}

async function run() {
  console.log(`📂 Đang đọc file: ${MD_FILE_PATH}`);
  const students = parseStudentFile(MD_FILE_PATH);
  console.log(`✅ Đã tìm thấy ${students.length} sinh viên.\n`);

  // LÀM SẠCH KEY BẰNG CÁCH TRÍCH XUẤT TRỰC TIẾP CHUỖI BASE64
  let rawKey = process.env.GOOGLE_PRIVATE_KEY || '';
  
  // Tìm chuỗi bắt đầu bằng MII (header của PKCS#8 RSA)
  const base64Match = rawKey.match(/MII[A-Za-z0-9+/=\s\\n\r]+/);
  if (!base64Match) {
    console.error('❌ Không tìm thấy chuỗi Base64 hợp lệ trong GOOGLE_PRIVATE_KEY!');
    process.exit(1);
  }

  // Làm sạch triệt để: xóa \n literal, xóa space, xóa xuống dòng thực
  const coreBase64 = base64Match[0].replace(/\\n/g, '').replace(/[\s\r\n]/g, '');
  const privateKey = `-----BEGIN PRIVATE KEY-----\n${coreBase64}\n-----END PRIVATE KEY-----\n`;

  const auth = new google.auth.GoogleAuth({
    credentials: {
      client_email: process.env.GOOGLE_SERVICE_ACCOUNT_EMAIL,
      private_key: privateKey,
    },
    scopes: ['https://www.googleapis.com/auth/spreadsheets']
  });

  const sheets = google.sheets({ version: 'v4', auth });

  console.log('🔒 Đang tạo mật khẩu hash...');
  const adminHash = await bcrypt.hash(process.env.ADMIN_PASSWORD || 'Admin@2026', 10);
  const studentHash = await bcrypt.hash('hub2026', 10);

  const now = new Date().toISOString();
  const headers = ['student_id', 'email', 'full_name', 'password_hash', 'role', 'must_change_password', 'created_at'];
  
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
    console.log(`🧹 Xóa dữ liệu cũ trong sheet "${SHEET_NAME}"...`);
    await sheets.spreadsheets.values.clear({
      spreadsheetId: SPREADSHEET_ID,
      range: `${SHEET_NAME}!A:G`
    });

    console.log('📝 Ghi dữ liệu mới...');
    await sheets.spreadsheets.values.update({
      spreadsheetId: SPREADSHEET_ID,
      range: `${SHEET_NAME}!A1`,
      valueInputOption: 'RAW',
      requestBody: { values: allRows }
    });

    console.log('\n✅ IMPORT HOÀN TẤT!');
    console.log(`   👨‍🏫 Admin: ${adminRow[1]}`);
    console.log(`   👨‍🎓 ${students.length} sinh viên đã được nhập.\n`);
  } catch (err) {
    console.error('❌ Lỗi:', err.message);
    if (err.response) console.error(JSON.stringify(err.response.data, null, 2));
    process.exit(1);
  }
}

run();
