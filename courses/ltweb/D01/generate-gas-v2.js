import { readFileSync, writeFileSync } from 'fs';
import bcrypt from 'bcryptjs';

function decodeEntities(str) {
  return str.replace(/&#(\d+);/g, (match, dec) => String.fromCharCode(dec)).trim();
}

async function generate() {
  console.log('📖 Reading student list...');
  const content = readFileSync('d:/ITS717_252_1_D01.md', 'utf-8');
  const rowRegex = /<tr>\s*<td[^>]*>\d+<\/td>\s*<td[^>]*>(\d+)<\/td>\s*<td[^>]*>[^<]*<\/td>\s*<td>([^<]*)<\/td>\s*<td>([^<]*)<\/td>/g;

  const students = [];
  let match;
  while ((match = rowRegex.exec(content)) !== null) {
    const id = match[1];
    const hoLot = decodeEntities(match[2]);
    const ten = decodeEntities(match[3]);
    const fullName = `${hoLot} ${ten}`.replace(/\s+/g, ' ').trim();
    students.push({ id, name: fullName });
  }

  console.log(`🔒 Hashing passwords for ${students.length} students (using ID as password)...`);
  const adminHash = await bcrypt.hash('Admin@2026', 10);
  const now = new Date().toISOString();

  // Map each student to a data row with their individual hash
  const studentData = [];
  for (const s of students) {
    const hash = await bcrypt.hash(s.id, 10); // Password = Student ID
    studentData.push(`["${s.id}", "${s.id}@st.hub.edu.vn", "${s.name}", "${hash}", "student", "true", "${now}"]`);
    if (studentData.length % 10 === 0) console.log(`...hashed ${studentData.length} students`);
  }

  const gasScript = `
function importStudentsWithIDAsPassword() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName("students");
  if (!sheet) {
    sheet = ss.insertSheet("students");
  }
  
  const headers = ["student_id", "email", "full_name", "password_hash", "role", "must_change_password", "created_at"];
  
  const data = [
    ["admin", "dangph@hub.edu.vn", "ThS. Phó Hải Đăng", "${adminHash}", "admin", "false", "${now}"],
    ${studentData.join(',\n    ')}
  ];
  
  sheet.clear();
  sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
  sheet.getRange(2, 1, data.length, headers.length).setValues(data);
  
  SpreadsheetApp.getUi().alert("Đã import thành công " + data.length + " người dùng! Mật khẩu là MSSV.");
}
`;

  writeFileSync('gas-import-individual.js', gasScript);
  console.log('✅ GAS script with individual hashes generated!');
}

generate();
