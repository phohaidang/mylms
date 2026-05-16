import { readFileSync, writeFileSync } from 'fs';

function decodeEntities(str) {
  return str.replace(/&#(\d+);/g, (match, dec) => String.fromCharCode(dec)).trim();
}

const content = readFileSync('d:/ITS717_252_1_D01.md', 'utf-8');
const rowRegex = /<tr>\s*<td[^>]*>\d+<\/td>\s*<td[^>]*>(\d+)<\/td>\s*<td[^>]*>[^<]*<\/td>\s*<td>([^<]*)<\/td>\s*<td>([^<]*)<\/td>/g;

const students = [];
let match;
while ((match = rowRegex.exec(content)) !== null) {
  const id = match[1];
  const fullName = `${decodeEntities(match[2])} ${decodeEntities(match[3])}`.replace(/\s+/g, ' ').trim();
  students.push({ id, name: fullName });
}

const studentHash = '$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S';
const adminHash = '$2a$10$swofHPBwGxh7KS3Xx799AezkwjtZGgPsiI3CV7Td1fRnmumxg46W6';
const now = new Date().toISOString();

const gasScript = `
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
  sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
  sheet.getRange(2, 1, data.length, headers.length).setValues(data);
  
  SpreadsheetApp.getUi().alert("Đã import thành công " + data.length + " người dùng!");
}
`;

writeFileSync('gas-import.js', gasScript);
console.log('GAS script generated!');
