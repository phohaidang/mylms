/**
 * seed-d01.js — Seed admin + 74 sinh viên lớp D01 môn TMXH
 * 
 * Usage: node courses/social-commerce/D01/seed-d01.js
 */
import { config } from 'dotenv';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import bcrypt from 'bcryptjs';
import { google } from 'googleapis';

const __dirname = dirname(fileURLToPath(import.meta.url));
config({ path: join(__dirname, '.env') });

// ── Google Sheets Setup ──
// Node 24+ uses OpenSSL 3.x which may reject old key formats
// Convert key to proper PKCS#8 PEM format
import crypto from 'crypto';

let privateKey = process.env.GOOGLE_PRIVATE_KEY
  ? process.env.GOOGLE_PRIVATE_KEY.replace(/\\n/g, '\n').replace(/"/g, '')
  : undefined;

// Fix for Node 24+ OpenSSL 3.x: re-export key to PKCS#8
if (privateKey) {
  try {
    const keyObj = crypto.createPrivateKey(privateKey);
    privateKey = keyObj.export({ type: 'pkcs8', format: 'pem' });
  } catch (e) {
    console.warn('⚠️  Key conversion failed, using raw key:', e.message);
  }
}

const auth = new google.auth.GoogleAuth({
  credentials: {
    client_email: process.env.GOOGLE_SERVICE_ACCOUNT_EMAIL,
    private_key: privateKey,
  },
  scopes: ['https://www.googleapis.com/auth/spreadsheets'],
});

const sheets = google.sheets({ version: 'v4', auth });
const SPREADSHEET_ID = process.env.GOOGLE_SHEETS_ID;

async function appendRows(sheetName, rows) {
  await sheets.spreadsheets.values.append({
    spreadsheetId: SPREADSHEET_ID,
    range: `${sheetName}!A:Z`,
    valueInputOption: 'RAW',
    requestBody: { values: rows },
  });
}

// ── Danh sách 74 sinh viên lớp D01 ──
const students = [
  { id: '030239230015', name: 'Võ Thị Vân Anh' },
  { id: '030239230016', name: 'Vũ Trúc Lan Anh' },
  { id: '030239230017', name: 'Lý Tố Ánh' },
  { id: '030239230025', name: 'Tô Nhật Chương' },
  { id: '030239230033', name: 'Dương Thị Phương Dung' },
  { id: '030239230034', name: 'Phạm Thị Thùy Dung' },
  { id: '030239230029', name: 'Đoàn Quốc Đại' },
  { id: '030239230041', name: 'Nguyễn Quỳnh Giang' },
  { id: '030239230045', name: 'Trần Thị Hà' },
  { id: '030239230048', name: 'Trần Thanh Hải' },
  { id: '030239230050', name: 'Lê Gia Hân' },
  { id: '030239230054', name: 'Nguyễn Trung Hiền' },
  { id: '030239230055', name: 'Trần Thị Thanh Hiền' },
  { id: '030239230059', name: 'Nguyễn Văn Hoàng' },
  { id: '030239230071', name: 'Đoàn Trung Nhật Huy' },
  { id: '030239230072', name: 'Huỳnh Đức Huy' },
  { id: '030239230074', name: 'Tôn Thất Gia Huy' },
  { id: '030239230078', name: 'Nguyễn Thị Huyền' },
  { id: '030239230081', name: 'Vũ Trần Khánh Huyền' },
  { id: '030239230083', name: 'Cao Như Huỳnh' },
  { id: '030239230064', name: 'Lê Đình Tuấn Hưng' },
  { id: '030239230067', name: 'Hoàng Xuân Hương' },
  { id: '030239230089', name: 'Nguyễn Thị Khánh' },
  { id: '030239230094', name: 'Phạm Hà Nhân Kiệt' },
  { id: '030239230097', name: 'Nguyễn Thị Hồng Kim' },
  { id: '030239230098', name: 'Nguyễn Thị Thiên Kim' },
  { id: '030239230099', name: 'Nguyễn Thị Diệu Lam' },
  { id: '030239230105', name: 'Hồ Tống Khánh Linh' },
  { id: '030239230108', name: 'Nguyễn Hiện Hiển Linh' },
  { id: '030239230104', name: 'Tô Thanh Lịch' },
  { id: '030239230123', name: 'Nguyễn Thị Xuân Mai' },
  { id: '030239230124', name: 'Nguyễn Văn Mẫn' },
  { id: '030239230136', name: 'Huỳnh Hiếu Ngân' },
  { id: '030239230140', name: 'Nguyễn Thu Ngân' },
  { id: '030239230141', name: 'Thiều Thị Thúy Ngân' },
  { id: '030239230143', name: 'Đoàn Yến Nghi' },
  { id: '030239230147', name: 'Dương Yến Ngọc' },
  { id: '030238220150', name: 'Nguyễn Thị Vân Ngọc' },
  { id: '030239230154', name: 'Trịnh Thái Minh Nguyên' },
  { id: '030239230157', name: 'Nguyễn Đức Nhật' },
  { id: '030239230164', name: 'Nguyễn Võ Yến Nhi' },
  { id: '030239230175', name: 'Trình Nguyễn Quỳnh Như' },
  { id: '030239230178', name: 'Nguyễn Đào Ánh Ni' },
  { id: '030239230193', name: 'Đoàn Nữ Anh Phương' },
  { id: '030239230195', name: 'Phạm Thị Thanh Phương' },
  { id: '030239230197', name: 'Nguyễn Thị Ngọc Quế' },
  { id: '030239230200', name: 'Lê Nguyễn Tú Quyên' },
  { id: '030238220208', name: 'Bùi Thị Như Quỳnh' },
  { id: '030239230214', name: 'Biện Hà Thành' },
  { id: '030239230216', name: 'Dương Thị Thu Thảo' },
  { id: '030239230217', name: 'Nguyễn Thị Thanh Thảo' },
  { id: '030239230211', name: 'Trần Quốc Thái' },
  { id: '030239230226', name: 'Đặng Lộc Thiên' },
  { id: '030239230238', name: 'Đỗ Hiền Thục' },
  { id: '030239230232', name: 'Phạm Đình Anh Thư' },
  { id: '030239230234', name: 'Trần Thị Minh Thư' },
  { id: '030239230242', name: 'Phan Thị Kiều Thy' },
  { id: '030239230246', name: 'Đỗ Đoàn Quốc Tín' },
  { id: '030239230260', name: 'Ngô Thảo Trang' },
  { id: '030239230263', name: 'Phạm Thị Thùy Trang' },
  { id: '030238220271', name: 'Võ Ngọc Thùy Trang' },
  { id: '030239230251', name: 'Lê Huỳnh Mai Trâm' },
  { id: '030239230252', name: 'Lê Thị Bích Trâm' },
  { id: '030239230253', name: 'Nguyễn Ngọc Bích Trâm' },
  { id: '030239230255', name: 'Nguyễn Thị Ngọc Trâm' },
  { id: '030239230272', name: 'Võ Thanh Trúc' },
  { id: '030239230277', name: 'Hoàng Nguyễn Trúc Uyên' },
  { id: '030239230280', name: 'Phạm Thị Thục Uyên' },
  { id: '030239230283', name: 'Lê Thị Hồng Vân' },
  { id: '030239230285', name: 'Nguyễn Thị Tường Vân' },
  { id: '030239230286', name: 'Nguyễn Thùy Vân' },
  { id: '030239230295', name: 'Nguyễn Thị Thúy Vy' },
  { id: '030239230303', name: 'Nguyễn Hoàng Yến' },
  { id: '030239230299', name: 'Trần Lê Như Ý' },
];

async function main() {
  console.log('\n🎓 Seed lớp D01 — ITS717 Thương mại Xã hội');
  console.log(`📊 Sheet ID: ${SPREADSHEET_ID}`);
  console.log(`👥 Tổng sinh viên: ${students.length}\n`);

  const now = new Date().toISOString();
  const defaultPassword = await bcrypt.hash('hub2026', 10);

  // 1. Seed Admin
  console.log('  ⏳ Tạo tài khoản admin...');
  const adminPassword = await bcrypt.hash(process.env.ADMIN_PASSWORD || 'admin2026', 10);
  await appendRows('students', [[
    'admin',
    process.env.ADMIN_EMAIL,
    process.env.ADMIN_NAME,
    adminPassword,
    'admin',
    'false',
    now
  ]]);
  console.log(`  ✅ Admin: ${process.env.ADMIN_EMAIL}`);

  // 2. Seed Students
  console.log(`  ⏳ Import ${students.length} sinh viên...`);
  const studentRows = students.map(s => [
    s.id,
    `${s.id}@st.hub.edu.vn`,
    s.name,
    defaultPassword,
    'student',
    'true',       // must_change_password
    now
  ]);

  // Batch 20 at a time to avoid API limits
  for (let i = 0; i < studentRows.length; i += 20) {
    const batch = studentRows.slice(i, i + 20);
    await appendRows('students', batch);
    console.log(`  ✅ Đã import ${Math.min(i + 20, studentRows.length)}/${studentRows.length}`);
  }

  console.log(`\n  ✅ Hoàn tất! ${students.length} sinh viên + 1 admin`);
  console.log(`  🔑 Mật khẩu mặc định sinh viên: hub2026`);
  console.log(`  🔑 Mật khẩu admin: ${process.env.ADMIN_PASSWORD}\n`);
}

main().catch(err => {
  console.error('❌ Lỗi:', err.message);
  process.exit(1);
});
