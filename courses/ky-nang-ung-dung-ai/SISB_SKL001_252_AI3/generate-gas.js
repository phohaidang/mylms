import { readFileSync, writeFileSync } from 'fs';

// Hàm giải mã HTML Entities (ví dụ: &#224; -> à, &#234; -> ê)
function decodeEntities(str) {
  return str.replace(/&#(\d+);/g, (match, dec) => String.fromCharCode(dec)).trim();
}

// Đọc file danh sách sinh viên
const content = readFileSync('d:/SISB_SKL001_252_AI3.md', 'utf-8');

// Regex khớp với từng dòng sinh viên trong bảng
// Cấu trúc dòng: <td>STT</td><td class="studyprogram_normal_dl">Mã SV</td><td>Lớp SV</td><td>Họ lót</td><td>Tên</td><td>Ngày sinh</td>
const rowRegex = /<tr>\s*<td[^>]*>(\d+)<\/td>\s*<td[^>]*class="studyprogram_normal_dl">(\d+)<\/td>\s*<td[^>]*>([^<]*)<\/td>\s*<td>([^<]*)<\/td>\s*<td>([^<]*)<\/td>/g;

const students = [];
let match;
while ((match = rowRegex.exec(content)) !== null) {
  const stt = match[1];
  const id = match[2];
  const className = match[3].trim();
  const hoLot = decodeEntities(match[4]);
  const ten = decodeEntities(match[5]);
  const fullName = `${hoLot} ${ten}`.replace(/\s+/g, ' ').trim();
  
  students.push({ stt, id, className, name: fullName });
}

// Hash mật khẩu mặc định cho sinh viên và admin
const studentHash = '$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S';
const adminHash = '$2a$10$swofHPBwGxh7KS3Xx799AezkwjtZGgPsiI3CV7Td1fRnmumxg46W6';
const now = new Date().toISOString();

const gasScript = `/**
 * Google Apps Script để import danh sách lớp SISB_SKL001_252_AI3
 * Hướng dẫn sử dụng:
 * 1. Mở Google Sheet liên kết với LMS
 * 2. Chọn Tiện ích mở rộng (Extensions) -> Apps Script
 * 3. Dán toàn bộ đoạn code này vào và nhấn Lưu (Save)
 * 4. Nhấn nút Run (Chạy) hàm importStudents
 */
function importStudents() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName("students");
  if (!sheet) {
    sheet = ss.insertSheet("students");
  }
  
  const headers = ["student_id", "email", "full_name", "password_hash", "role", "must_change_password", "created_at"];
  
  const data = [
    ["admin", "dangph@hub.edu.vn", "ThS. Phó Hải Đăng", "${adminHash}", "admin", "false", "${now}"],
    ${students.map(s => `["${s.id}", "${s.id}@st.hub.edu.vn", "${s.name}", "${studentHash}", "student", "true", "${now}"]`).join(',\n    ')}
  ];
  
  sheet.clear();
  // Set headers ở dòng 1
  sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
  // Set dữ liệu bắt đầu từ dòng 2
  sheet.getRange(2, 1, data.length, headers.length).setValues(data);
  
  // Định dạng cột student_id thành dạng TEXT để tránh mất số 0 ở đầu
  sheet.getRange(2, 1, data.length, 1).setNumberFormat("@");
  sheet.getRange(2, 2, data.length, 1).setNumberFormat("@");
  
  SpreadsheetApp.getUi().alert("🎉 Đã import thành công " + data.length + " tài khoản (1 Admin + ${students.length} Sinh viên) vào bảng 'students'!");
}
`;

// Ghi ra file gas-import.js
writeFileSync('courses/ky-nang-ung-dung-ai/SISB_SKL001_252_AI3/gas-import.js', gasScript);
console.log(`GAS script generated successfully! Parsed ${students.length} students.`);
