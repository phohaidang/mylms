/**
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
    ["admin", "dangph@hub.edu.vn", "ThS. Phó Hải Đăng", "$2a$10$0x6U7O489A6glaEw3N6X4ubvaHWrjKKSRBzf9KIofpAjo0ycVP6JO", "admin", "false", "2026-05-17T07:37:16.154Z"],
    ["110322230009", "110322230009@st.hub.edu.vn", "Hoàng Mỹ Anh", "$2a$10$mXJB.RCbBKiY9zyvjuXC.e/Gf.SYPbxLW3efuSEr3bKC9hw.yAdNS", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110323240018", "110323240018@st.hub.edu.vn", "Lê Hoàng Minh Anh", "$2a$10$lRF2qPTNuU3hireRHsQlOObz/UXEKxm6.1EQQdOnLksGIr4X6CWFG", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110323240022", "110323240022@st.hub.edu.vn", "Nguyễn Lê Vân Anh", "$2a$10$k4Lg5Qb7IhSudZZWHOZxM.U6KZ9FPmfMDvZggLCFsVsFxcUlN48wu", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110323240028", "110323240028@st.hub.edu.vn", "Trương Thanh Anh", "$2a$10$GJ/6Tj/M9Daf7z4ePtFJhenAEFK76vSa0T62gtmhIbEf4J6Mddca6", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110324250152", "110324250152@st.hub.edu.vn", "TRƯƠNG GIA BÌNH", "$2a$10$a/xqLlBrIoiSOF0bZlCineDA7CohiUUwmRNFMZtWuNiBeUsTetX1e", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110322230002", "110322230002@st.hub.edu.vn", "Nguyễn Thành Danh", "$2a$10$PUX.jvsVg63FbCKwA2Xzzur52lRBve4Nzjf5v1g8qnCDT2i78fs5C", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110124250051", "110124250051@st.hub.edu.vn", "MAI ĐÌNH ĐÌNH", "$2a$10$qvqPOR7y8S08wO4TnWUI7O94eUmh0zwu7s5PrKomHvy55jwyShBX6", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110124250003", "110124250003@st.hub.edu.vn", "VÕ TẤN ĐỨC", "$2a$10$pHL.ihkruQza9MmUcuC8nuR2Edt.Jxd891izn1MuPvpQkrkDL4WrS", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110323240056", "110323240056@st.hub.edu.vn", "Dương Vũ Gia Hân", "$2a$10$f7QIPzvgVRtMq.sqTkVxt.LzrLegt/HMtG39wNsUdUvuCklRT.sbu", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110124250046", "110124250046@st.hub.edu.vn", "LÊ GIA HÂN", "$2a$10$3XcSDMnqmn1ck.mkcUN/J.lzzB7ImKAKEx8jzEozho/nb2dfqXqWm", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110324250047", "110324250047@st.hub.edu.vn", "TRẦN QUỐC HIẾU", "$2a$10$jkK40BcUSUdZ9leE8M7fY.Cn4I.ZSmJQll6S1Py2VpG5A5pUSthim", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110323240064", "110323240064@st.hub.edu.vn", "Nguyễn Phương Nhật Hoàng", "$2a$10$eFcLbx/uK7DHwgtJ/slzGebCi/Wrecl7DuLylgNf.9MHwQwrdK4e6", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110323240075", "110323240075@st.hub.edu.vn", "Trần Tuấn Huy", "$2a$10$rkAPssOnHkjwzAdOhUxmFeMM78YB3BpjS1ILyDQHJ7fkYAdVWG8QG", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110323240070", "110323240070@st.hub.edu.vn", "Phạm Tuấn Hùng", "$2a$10$KEQ1RLtmNDMjWZ/HgSG9ouYUkpzrWCyiCLwlg/lBr4rT7io3b1vv6", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110322230092", "110322230092@st.hub.edu.vn", "Mai Thị Xuân Hương", "$2a$10$UyYMIf0JdQsl7EpbJMBfKOJybARo75R3UfAEyVmfRKL04.Y2rn0MC", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110324250059", "110324250059@st.hub.edu.vn", "ĐINH GIA KHIÊM", "$2a$10$TJk7m02M3hkqEZacbvTUOO7fuhf5hIDRNR/IvKpIMwe9FD.J7vHZW", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110324250128", "110324250128@st.hub.edu.vn", "VŨ ĐĂNG KHOA", "$2a$10$v1eKLs/PVQL8cEbOGlhygu7LDqJC7hDzNPAmfbVQ.H0Amneat4mtu", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110324250068", "110324250068@st.hub.edu.vn", "TRẦN QUANG MINH", "$2a$10$0Q6ME3z58oZ3mLxrsIWTn.t.pwtvLOVx/5u4.s41GI6WLNhADRvuC", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110323240116", "110323240116@st.hub.edu.vn", "Đỗ Ngọc Kim Ngân", "$2a$10$u11SrcD/orVziiziOyC7BOB5qFud.AZtmY8elXtHCsiTc7yCKNdu6", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110324250133", "110324250133@st.hub.edu.vn", "VŨ BÙI THANH NGÂN", "$2a$10$3NR7KSG2tixWlPNEFuFczumZwilU6v52BpDiwn12XFX9M3qGn1uXC", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110324250072", "110324250072@st.hub.edu.vn", "NGUYỄN GIA NGHI", "$2a$10$NJ.JjZdzK8jW7tsc2YMpHegGhBDsvmzXQ2zeVhHAmbJgV.kmRYmgK", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110322230154", "110322230154@st.hub.edu.vn", "Nguyễn Thị Yến Nhi", "$2a$10$bKu020YRreAlz9xyFtTM9u3cQubD7wtAkbn8PPVcubM8E21qtW5FC", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110324250087", "110324250087@st.hub.edu.vn", "LỘC HUỲNH ÁNH NHƯ", "$2a$10$hVp3LlDq.bwk.l3sULo2eOMgd2qRjpic7t4YJA1T2ZjXtS6LN49Vi", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110322230159", "110322230159@st.hub.edu.vn", "Thạch Thị Huỳnh Như", "$2a$10$s1wqbELfNuX.Sr3yO6EmxuJ9T.0vZ.VU/fmDaQaQBGEBYLPpEHtR6", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110124250028", "110124250028@st.hub.edu.vn", "NGUYỄN NGỌC MỸ PHƯƠNG", "$2a$10$NIjJ.4yMklIqOqRXEyRe5OQCzs7Poh8xakXErapQx7GKEJ6Eqywzq", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110324250153", "110324250153@st.hub.edu.vn", "ĐỖ THỊ MỸ QUYÊN", "$2a$10$PryXICC3i2HggThe9eLU5uH7ttzMEeap2gDStl7kNYVtYTMnepq4a", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110323240174", "110323240174@st.hub.edu.vn", "Nguyễn Thị Chi Tâm", "$2a$10$o7jyBMW2lQ1JNorFvgk75OEnaYigEAGeoNRkjgLfI9elGCbKHBMU.", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110324250147", "110324250147@st.hub.edu.vn", "LÊ NGỌC ANH THƠ", "$2a$10$d4.94m8qGdUf1hxRwqRfAOarYwtMoNiBvmWwCaF6SCRbTA915/Xl6", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110324250098", "110324250098@st.hub.edu.vn", "PHAN THỊ ANH THƯ", "$2a$10$PVRlxxFyca4kygHlA3B7teWwChNnTfffhrDbB31VYsqnwrqXmg.US", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110124250035", "110124250035@st.hub.edu.vn", "ĐOÀN HÀ NHẬT TIÊN", "$2a$10$kY7YwuLf36MQNWLsyV4njOtFEo8UEskRq9ZF5kbT7sKmrcPbXlpum", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110124250044", "110124250044@st.hub.edu.vn", "LÃ MINH TRANG", "$2a$10$XuWpU6.7rjsuUU5.LAB.lu0sb96m/Y8PSPELqXQEsL94JuDFbAOVy", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110324250108", "110324250108@st.hub.edu.vn", "NGUYỄN THỊ HUYỀN TRANG", "$2a$10$vc01MVbdKAIoZT6TN8nfW.MFaXqBvCK7fXZLo4Hu4DgCg0feUu3dC", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110124250036", "110124250036@st.hub.edu.vn", "NGUYỄN THỊ YẾN TRANG", "$2a$10$FBgQ2FjR5HHyzJEUR4BXvu1YmHjVByj/UgE04IB7o9JZGHVPC3uUy", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110124250037", "110124250037@st.hub.edu.vn", "PHẠM DƯƠNG PHƯƠNG TRANG", "$2a$10$/B0uraLFN.hcHIyDqThS0.r5dTD0A6YovK0ymlabiDW0oj0etpS6G", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110324250110", "110324250110@st.hub.edu.vn", "HỒ THANH TRÚC", "$2a$10$mMfgnkZ7.MBA/NJuzRMdoel1u74QufDcDAWQeU8YRebHXdq9PHon6", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110124250050", "110124250050@st.hub.edu.vn", "NGUYỄN HOÀNG THANH TRÚC", "$2a$10$u5l5i2o/Nmmkng9pv7tBWOlB9eOXMgfgJG7b7jWcSg4WeOUWfSyuC", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110323240218", "110323240218@st.hub.edu.vn", "Nguyễn Thanh Trúc", "$2a$10$PlllbyY3rIK8xNPSJl/Ws.tY1qYOj5GuTP5hyIiMjBWs6wpkdmO1.", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110324250114", "110324250114@st.hub.edu.vn", "HỒ NGỌC CÁT TƯỜNG", "$2a$10$j1OwzXq4gTvnfxTzfRz.ROBQbQojzN2Iy/fwmpZv0Gaqx84csvaf.", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110324250115", "110324250115@st.hub.edu.vn", "CAO PHƯƠNG UYÊN", "$2a$10$17JoIE0N.fHLGxmLw1n80ON81FoMrmuOIlpJ6AqHtSdMUXh5YrV36", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110324250117", "110324250117@st.hub.edu.vn", "ĐINH NGUYỄN KHÁNH VÂN", "$2a$10$VBSDTO7z3.HqwBxZiQP0HuykH/49ok7vB8rrM1DupCFzlSNDP7S7O", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110323240227", "110323240227@st.hub.edu.vn", "Nguyễn Hải Vân", "$2a$10$ZeG/qTVzHypBJGvnZy.fwO7d6KuJQa/dIpHTzUyAS7SoiqFO.190e", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110124250040", "110124250040@st.hub.edu.vn", "ĐỖ ANH VŨ", "$2a$10$ARRNbZfgUDNKd7ySGnDn3ectuwiXCi.PnPyIBxVW7mkXt2tu9/d/e", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110324250129", "110324250129@st.hub.edu.vn", "BÙI NGỌC PHƯƠNG VY", "$2a$10$752OcF6SGKGE2N2o3jk1K.XLzzlbA5oYKHAaw/iotmsQs5akXsDGa", "student", "true", "2026-05-17T07:37:16.154Z"],
    ["110324250145", "110324250145@st.hub.edu.vn", "NGUYỄN ĐOÀN HẢI YẾN", "$2a$10$RLVy46pUBQVNcassUea72ej7uxic5D0O0waNDUThNbdKpb4S/J/h6", "student", "true", "2026-05-17T07:37:16.154Z"]
  ];
  
  sheet.clear();
  // Set headers ở dòng 1
  sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
  // Set dữ liệu bắt đầu từ dòng 2
  sheet.getRange(2, 1, data.length, headers.length).setValues(data);
  
  // Định dạng cột student_id thành dạng TEXT để tránh mất số 0 ở đầu
  sheet.getRange(2, 1, data.length, 1).setNumberFormat("@");
  sheet.getRange(2, 2, data.length, 1).setNumberFormat("@");
  
  SpreadsheetApp.getUi().alert("🎉 Đã import thành công " + data.length + " tài khoản (1 Admin + 44 Sinh viên) vào bảng 'students'!");
}
