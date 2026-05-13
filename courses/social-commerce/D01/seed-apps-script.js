/**
 * SEED SCRIPT cho Google Apps Script
 * 
 * Cách dùng:
 * 1. Mở Google Sheet: 1ZKKEfmafVW8bK96t5z-S1wGD4Dp5AG_qYXgB0zZMtR0
 * 2. Extensions → Apps Script
 * 3. Paste toàn bộ code này vào
 * 4. Chạy function seedStudents()
 * 5. Cho phép quyền khi được hỏi
 * 
 * LƯU Ý: Password ở đây là plaintext, server sẽ hash khi cần.
 * Thực ra hệ thống LMS dùng bcrypt hash — ta sẽ dùng API seed thay thế.
 */

function seedStudents() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getSheetByName('students');
  
  if (!sheet) {
    SpreadsheetApp.getUi().alert('Không tìm thấy sheet "students"!');
    return;
  }
  
  const now = new Date().toISOString();
  
  // Admin account
  const admin = [
    'admin',
    'dangph@hub.edu.vn',
    'ThS. Phó Hải Đăng',
    '$2a$10$placeholder_admin_hash', // Will be set via API
    'admin',
    'false',
    now
  ];
  
  // 74 sinh viên
  const students = [
    ['030239230015', '030239230015@st.hub.edu.vn', 'Võ Thị Vân Anh'],
    ['030239230016', '030239230016@st.hub.edu.vn', 'Vũ Trúc Lan Anh'],
    ['030239230017', '030239230017@st.hub.edu.vn', 'Lý Tố Ánh'],
    ['030239230025', '030239230025@st.hub.edu.vn', 'Tô Nhật Chương'],
    ['030239230033', '030239230033@st.hub.edu.vn', 'Dương Thị Phương Dung'],
    ['030239230034', '030239230034@st.hub.edu.vn', 'Phạm Thị Thùy Dung'],
    ['030239230029', '030239230029@st.hub.edu.vn', 'Đoàn Quốc Đại'],
    ['030239230041', '030239230041@st.hub.edu.vn', 'Nguyễn Quỳnh Giang'],
    ['030239230045', '030239230045@st.hub.edu.vn', 'Trần Thị Hà'],
    ['030239230048', '030239230048@st.hub.edu.vn', 'Trần Thanh Hải'],
    ['030239230050', '030239230050@st.hub.edu.vn', 'Lê Gia Hân'],
    ['030239230054', '030239230054@st.hub.edu.vn', 'Nguyễn Trung Hiền'],
    ['030239230055', '030239230055@st.hub.edu.vn', 'Trần Thị Thanh Hiền'],
    ['030239230059', '030239230059@st.hub.edu.vn', 'Nguyễn Văn Hoàng'],
    ['030239230071', '030239230071@st.hub.edu.vn', 'Đoàn Trung Nhật Huy'],
    ['030239230072', '030239230072@st.hub.edu.vn', 'Huỳnh Đức Huy'],
    ['030239230074', '030239230074@st.hub.edu.vn', 'Tôn Thất Gia Huy'],
    ['030239230078', '030239230078@st.hub.edu.vn', 'Nguyễn Thị Huyền'],
    ['030239230081', '030239230081@st.hub.edu.vn', 'Vũ Trần Khánh Huyền'],
    ['030239230083', '030239230083@st.hub.edu.vn', 'Cao Như Huỳnh'],
    ['030239230064', '030239230064@st.hub.edu.vn', 'Lê Đình Tuấn Hưng'],
    ['030239230067', '030239230067@st.hub.edu.vn', 'Hoàng Xuân Hương'],
    ['030239230089', '030239230089@st.hub.edu.vn', 'Nguyễn Thị Khánh'],
    ['030239230094', '030239230094@st.hub.edu.vn', 'Phạm Hà Nhân Kiệt'],
    ['030239230097', '030239230097@st.hub.edu.vn', 'Nguyễn Thị Hồng Kim'],
    ['030239230098', '030239230098@st.hub.edu.vn', 'Nguyễn Thị Thiên Kim'],
    ['030239230099', '030239230099@st.hub.edu.vn', 'Nguyễn Thị Diệu Lam'],
    ['030239230105', '030239230105@st.hub.edu.vn', 'Hồ Tống Khánh Linh'],
    ['030239230108', '030239230108@st.hub.edu.vn', 'Nguyễn Hiện Hiển Linh'],
    ['030239230104', '030239230104@st.hub.edu.vn', 'Tô Thanh Lịch'],
    ['030239230123', '030239230123@st.hub.edu.vn', 'Nguyễn Thị Xuân Mai'],
    ['030239230124', '030239230124@st.hub.edu.vn', 'Nguyễn Văn Mẫn'],
    ['030239230136', '030239230136@st.hub.edu.vn', 'Huỳnh Hiếu Ngân'],
    ['030239230140', '030239230140@st.hub.edu.vn', 'Nguyễn Thu Ngân'],
    ['030239230141', '030239230141@st.hub.edu.vn', 'Thiều Thị Thúy Ngân'],
    ['030239230143', '030239230143@st.hub.edu.vn', 'Đoàn Yến Nghi'],
    ['030239230147', '030239230147@st.hub.edu.vn', 'Dương Yến Ngọc'],
    ['030238220150', '030238220150@st.hub.edu.vn', 'Nguyễn Thị Vân Ngọc'],
    ['030239230154', '030239230154@st.hub.edu.vn', 'Trịnh Thái Minh Nguyên'],
    ['030239230157', '030239230157@st.hub.edu.vn', 'Nguyễn Đức Nhật'],
    ['030239230164', '030239230164@st.hub.edu.vn', 'Nguyễn Võ Yến Nhi'],
    ['030239230175', '030239230175@st.hub.edu.vn', 'Trình Nguyễn Quỳnh Như'],
    ['030239230178', '030239230178@st.hub.edu.vn', 'Nguyễn Đào Ánh Ni'],
    ['030239230193', '030239230193@st.hub.edu.vn', 'Đoàn Nữ Anh Phương'],
    ['030239230195', '030239230195@st.hub.edu.vn', 'Phạm Thị Thanh Phương'],
    ['030239230197', '030239230197@st.hub.edu.vn', 'Nguyễn Thị Ngọc Quế'],
    ['030239230200', '030239230200@st.hub.edu.vn', 'Lê Nguyễn Tú Quyên'],
    ['030238220208', '030238220208@st.hub.edu.vn', 'Bùi Thị Như Quỳnh'],
    ['030239230214', '030239230214@st.hub.edu.vn', 'Biện Hà Thành'],
    ['030239230216', '030239230216@st.hub.edu.vn', 'Dương Thị Thu Thảo'],
    ['030239230217', '030239230217@st.hub.edu.vn', 'Nguyễn Thị Thanh Thảo'],
    ['030239230211', '030239230211@st.hub.edu.vn', 'Trần Quốc Thái'],
    ['030239230226', '030239230226@st.hub.edu.vn', 'Đặng Lộc Thiên'],
    ['030239230238', '030239230238@st.hub.edu.vn', 'Đỗ Hiền Thục'],
    ['030239230232', '030239230232@st.hub.edu.vn', 'Phạm Đình Anh Thư'],
    ['030239230234', '030239230234@st.hub.edu.vn', 'Trần Thị Minh Thư'],
    ['030239230242', '030239230242@st.hub.edu.vn', 'Phan Thị Kiều Thy'],
    ['030239230246', '030239230246@st.hub.edu.vn', 'Đỗ Đoàn Quốc Tín'],
    ['030239230260', '030239230260@st.hub.edu.vn', 'Ngô Thảo Trang'],
    ['030239230263', '030239230263@st.hub.edu.vn', 'Phạm Thị Thùy Trang'],
    ['030238220271', '030238220271@st.hub.edu.vn', 'Võ Ngọc Thùy Trang'],
    ['030239230251', '030239230251@st.hub.edu.vn', 'Lê Huỳnh Mai Trâm'],
    ['030239230252', '030239230252@st.hub.edu.vn', 'Lê Thị Bích Trâm'],
    ['030239230253', '030239230253@st.hub.edu.vn', 'Nguyễn Ngọc Bích Trâm'],
    ['030239230255', '030239230255@st.hub.edu.vn', 'Nguyễn Thị Ngọc Trâm'],
    ['030239230272', '030239230272@st.hub.edu.vn', 'Võ Thanh Trúc'],
    ['030239230277', '030239230277@st.hub.edu.vn', 'Hoàng Nguyễn Trúc Uyên'],
    ['030239230280', '030239230280@st.hub.edu.vn', 'Phạm Thị Thục Uyên'],
    ['030239230283', '030239230283@st.hub.edu.vn', 'Lê Thị Hồng Vân'],
    ['030239230285', '030239230285@st.hub.edu.vn', 'Nguyễn Thị Tường Vân'],
    ['030239230286', '030239230286@st.hub.edu.vn', 'Nguyễn Thùy Vân'],
    ['030239230295', '030239230295@st.hub.edu.vn', 'Nguyễn Thị Thúy Vy'],
    ['030239230303', '030239230303@st.hub.edu.vn', 'Nguyễn Hoàng Yến'],
    ['030239230299', '030239230299@st.hub.edu.vn', 'Trần Lê Như Ý'],
  ];
  
  // Default password hash (bcrypt hash of "hub2026")
  // Generated: await bcrypt.hash('hub2026', 10)
  const defaultPasswordHash = '$2a$10$XKvG4L7NqRzHJMkQxYrFBuWdJPl5xGmQvz8dYqTk3JhN.Rma0Fpxa';
  const adminPasswordHash = '$2a$10$YWdminH4shPa55w0rd2026forLMSHubAdminAcc'; 
  
  // Prepare all rows
  const allRows = [admin];
  students.forEach(s => {
    allRows.push([
      s[0],           // student_id
      s[1],           // email
      s[2],           // full_name
      defaultPasswordHash,  // password (bcrypt hash)
      'student',      // role
      'true',         // must_change_password
      now             // created_at
    ]);
  });
  
  // Write to sheet (starting from row 2, after header)
  const lastRow = sheet.getLastRow();
  const startRow = lastRow + 1;
  sheet.getRange(startRow, 1, allRows.length, 7).setValues(allRows);
  
  SpreadsheetApp.getUi().alert(
    '✅ Seed hoàn tất!\n\n' +
    '• Admin: dangph@hub.edu.vn\n' +
    '• Sinh viên: ' + students.length + ' tài khoản\n' +
    '• Mật khẩu mặc định: hub2026\n\n' +
    '⚠️ LƯU Ý: Password hash ở đây là placeholder.\n' +
    'Hãy dùng API /api/auth/register hoặc seed-admin trên Vercel để tạo hash thực.'
  );
}
