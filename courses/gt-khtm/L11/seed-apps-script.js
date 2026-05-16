/**
 * SEED SCRIPT cho Google Apps Script
 * ITS717 — TMXH — Lop D01
 * 
 * Chay function: seedAllStudents
 */

function seedAllStudents() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName('students');
  
  if (!sheet) {
    sheet = ss.insertSheet('students');
  }
  
  sheet.clear();
  
  var now = new Date().toISOString();
  
  // Bcrypt hashes (da tao bang Node.js)
  var ADMIN_HASH = '$2a$10$ryXu.c52eOybBGATaaU7R.ux6HLjr8GawCD1s2/Pgj/zup5wCIR.u';
  var STUDENT_HASH = '$2a$10$K6EX51nKz3EfR5YMwRCdduKazVwkb8a/gQs0VFCOvn83MFAUA4uz.';
  
  var headers = ['student_id', 'email', 'full_name', 'password', 'role', 'must_change_password', 'created_at'];
  
  var admin = ['admin', 'dangph@hub.edu.vn', 'ThS. Pho Hai Dang', ADMIN_HASH, 'admin', 'false', now];
  
  var students = [
    ['030239230015', '030239230015@st.hub.edu.vn', 'Vo Thi Van Anh'],
    ['030239230016', '030239230016@st.hub.edu.vn', 'Vu Truc Lan Anh'],
    ['030239230017', '030239230017@st.hub.edu.vn', 'Ly To Anh'],
    ['030239230025', '030239230025@st.hub.edu.vn', 'To Nhat Chuong'],
    ['030239230033', '030239230033@st.hub.edu.vn', 'Duong Thi Phuong Dung'],
    ['030239230034', '030239230034@st.hub.edu.vn', 'Pham Thi Thuy Dung'],
    ['030239230029', '030239230029@st.hub.edu.vn', 'Doan Quoc Dai'],
    ['030239230041', '030239230041@st.hub.edu.vn', 'Nguyen Quynh Giang'],
    ['030239230045', '030239230045@st.hub.edu.vn', 'Tran Thi Ha'],
    ['030239230048', '030239230048@st.hub.edu.vn', 'Tran Thanh Hai'],
    ['030239230050', '030239230050@st.hub.edu.vn', 'Le Gia Han'],
    ['030239230054', '030239230054@st.hub.edu.vn', 'Nguyen Trung Hien'],
    ['030239230055', '030239230055@st.hub.edu.vn', 'Tran Thi Thanh Hien'],
    ['030239230059', '030239230059@st.hub.edu.vn', 'Nguyen Van Hoang'],
    ['030239230071', '030239230071@st.hub.edu.vn', 'Doan Trung Nhat Huy'],
    ['030239230072', '030239230072@st.hub.edu.vn', 'Huynh Duc Huy'],
    ['030239230074', '030239230074@st.hub.edu.vn', 'Ton That Gia Huy'],
    ['030239230078', '030239230078@st.hub.edu.vn', 'Nguyen Thi Huyen'],
    ['030239230081', '030239230081@st.hub.edu.vn', 'Vu Tran Khanh Huyen'],
    ['030239230083', '030239230083@st.hub.edu.vn', 'Cao Nhu Huynh'],
    ['030239230064', '030239230064@st.hub.edu.vn', 'Le Dinh Tuan Hung'],
    ['030239230067', '030239230067@st.hub.edu.vn', 'Hoang Xuan Huong'],
    ['030239230089', '030239230089@st.hub.edu.vn', 'Nguyen Thi Khanh'],
    ['030239230094', '030239230094@st.hub.edu.vn', 'Pham Ha Nhan Kiet'],
    ['030239230097', '030239230097@st.hub.edu.vn', 'Nguyen Thi Hong Kim'],
    ['030239230098', '030239230098@st.hub.edu.vn', 'Nguyen Thi Thien Kim'],
    ['030239230099', '030239230099@st.hub.edu.vn', 'Nguyen Thi Dieu Lam'],
    ['030239230105', '030239230105@st.hub.edu.vn', 'Ho Tong Khanh Linh'],
    ['030239230108', '030239230108@st.hub.edu.vn', 'Nguyen Hien Hien Linh'],
    ['030239230104', '030239230104@st.hub.edu.vn', 'To Thanh Lich'],
    ['030239230123', '030239230123@st.hub.edu.vn', 'Nguyen Thi Xuan Mai'],
    ['030239230124', '030239230124@st.hub.edu.vn', 'Nguyen Van Man'],
    ['030239230136', '030239230136@st.hub.edu.vn', 'Huynh Hieu Ngan'],
    ['030239230140', '030239230140@st.hub.edu.vn', 'Nguyen Thu Ngan'],
    ['030239230141', '030239230141@st.hub.edu.vn', 'Thieu Thi Thuy Ngan'],
    ['030239230143', '030239230143@st.hub.edu.vn', 'Doan Yen Nghi'],
    ['030239230147', '030239230147@st.hub.edu.vn', 'Duong Yen Ngoc'],
    ['030238220150', '030238220150@st.hub.edu.vn', 'Nguyen Thi Van Ngoc'],
    ['030239230154', '030239230154@st.hub.edu.vn', 'Trinh Thai Minh Nguyen'],
    ['030239230157', '030239230157@st.hub.edu.vn', 'Nguyen Duc Nhat'],
    ['030239230164', '030239230164@st.hub.edu.vn', 'Nguyen Vo Yen Nhi'],
    ['030239230175', '030239230175@st.hub.edu.vn', 'Trinh Nguyen Quynh Nhu'],
    ['030239230178', '030239230178@st.hub.edu.vn', 'Nguyen Dao Anh Ni'],
    ['030239230193', '030239230193@st.hub.edu.vn', 'Doan Nu Anh Phuong'],
    ['030239230195', '030239230195@st.hub.edu.vn', 'Pham Thi Thanh Phuong'],
    ['030239230197', '030239230197@st.hub.edu.vn', 'Nguyen Thi Ngoc Que'],
    ['030239230200', '030239230200@st.hub.edu.vn', 'Le Nguyen Tu Quyen'],
    ['030238220208', '030238220208@st.hub.edu.vn', 'Bui Thi Nhu Quynh'],
    ['030239230214', '030239230214@st.hub.edu.vn', 'Bien Ha Thanh'],
    ['030239230216', '030239230216@st.hub.edu.vn', 'Duong Thi Thu Thao'],
    ['030239230217', '030239230217@st.hub.edu.vn', 'Nguyen Thi Thanh Thao'],
    ['030239230211', '030239230211@st.hub.edu.vn', 'Tran Quoc Thai'],
    ['030239230226', '030239230226@st.hub.edu.vn', 'Dang Loc Thien'],
    ['030239230238', '030239230238@st.hub.edu.vn', 'Do Hien Thuc'],
    ['030239230232', '030239230232@st.hub.edu.vn', 'Pham Dinh Anh Thu'],
    ['030239230234', '030239230234@st.hub.edu.vn', 'Tran Thi Minh Thu'],
    ['030239230242', '030239230242@st.hub.edu.vn', 'Phan Thi Kieu Thy'],
    ['030239230246', '030239230246@st.hub.edu.vn', 'Do Doan Quoc Tin'],
    ['030239230260', '030239230260@st.hub.edu.vn', 'Ngo Thao Trang'],
    ['030239230263', '030239230263@st.hub.edu.vn', 'Pham Thi Thuy Trang'],
    ['030238220271', '030238220271@st.hub.edu.vn', 'Vo Ngoc Thuy Trang'],
    ['030239230251', '030239230251@st.hub.edu.vn', 'Le Huynh Mai Tram'],
    ['030239230252', '030239230252@st.hub.edu.vn', 'Le Thi Bich Tram'],
    ['030239230253', '030239230253@st.hub.edu.vn', 'Nguyen Ngoc Bich Tram'],
    ['030239230255', '030239230255@st.hub.edu.vn', 'Nguyen Thi Ngoc Tram'],
    ['030239230272', '030239230272@st.hub.edu.vn', 'Vo Thanh Truc'],
    ['030239230277', '030239230277@st.hub.edu.vn', 'Hoang Nguyen Truc Uyen'],
    ['030239230280', '030239230280@st.hub.edu.vn', 'Pham Thi Thuc Uyen'],
    ['030239230283', '030239230283@st.hub.edu.vn', 'Le Thi Hong Van'],
    ['030239230285', '030239230285@st.hub.edu.vn', 'Nguyen Thi Tuong Van'],
    ['030239230286', '030239230286@st.hub.edu.vn', 'Nguyen Thuy Van'],
    ['030239230295', '030239230295@st.hub.edu.vn', 'Nguyen Thi Thuy Vy'],
    ['030239230303', '030239230303@st.hub.edu.vn', 'Nguyen Hoang Yen'],
    ['030239230299', '030239230299@st.hub.edu.vn', 'Tran Le Nhu Y']
  ];
  
  var allRows = [headers, admin];
  for (var i = 0; i < students.length; i++) {
    var s = students[i];
    allRows.push([s[0], s[1], s[2], STUDENT_HASH, 'student', 'true', now]);
  }
  
  sheet.getRange(1, 1, allRows.length, headers.length).setValues(allRows);
  
  Logger.log('SEED DONE: 1 admin + ' + students.length + ' students');
  SpreadsheetApp.getUi().alert('SEED HOAN TAT!\n\nAdmin: dangph@hub.edu.vn / Admin@2026\nSinh vien: ' + students.length + ' tai khoan / Mat khau: hub2026');
}
