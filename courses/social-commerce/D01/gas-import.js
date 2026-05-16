
function importStudents() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName("students");
  if (!sheet) {
    sheet = ss.insertSheet("students");
  }
  
  const headers = ["student_id", "email", "full_name", "password_hash", "role", "must_change_password", "created_at"];
  
  const data = [
    ["admin", "dangph@hub.edu.vn", "ThS. Phó Hải Đăng", "$2a$10$swofHPBwGxh7KS3Xx799AezkwjtZGgPsiI3CV7Td1fRnmumxg46W6", "admin", "false", "2026-05-15T16:36:52.865Z"],
    ["030239230015", "030239230015@st.hub.edu.vn", "Võ Thị Vân Anh", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230016", "030239230016@st.hub.edu.vn", "Vũ Trúc Lan Anh", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230017", "030239230017@st.hub.edu.vn", "Lý Tố Ánh", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230025", "030239230025@st.hub.edu.vn", "Tô Nhật Chương", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230033", "030239230033@st.hub.edu.vn", "Dương Thị Phương Dung", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230034", "030239230034@st.hub.edu.vn", "Phạm Thị Thùy Dung", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230029", "030239230029@st.hub.edu.vn", "Đoàn Quốc Đại", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230041", "030239230041@st.hub.edu.vn", "Nguyễn Quỳnh Giang", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230045", "030239230045@st.hub.edu.vn", "Trần Thị Hà", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230048", "030239230048@st.hub.edu.vn", "Trần Thanh Hải", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230050", "030239230050@st.hub.edu.vn", "Lê Gia Hân", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230054", "030239230054@st.hub.edu.vn", "Nguyễn Trung Hiền", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230055", "030239230055@st.hub.edu.vn", "Trần Thị Thanh Hiền", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230059", "030239230059@st.hub.edu.vn", "Nguyễn Văn Hoàng", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230071", "030239230071@st.hub.edu.vn", "Đoàn Trung Nhật Huy", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230072", "030239230072@st.hub.edu.vn", "Huỳnh Đức Huy", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230074", "030239230074@st.hub.edu.vn", "Tôn Thất Gia Huy", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230078", "030239230078@st.hub.edu.vn", "Nguyễn Thị Huyền", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230081", "030239230081@st.hub.edu.vn", "Vũ Trần Khánh Huyền", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230083", "030239230083@st.hub.edu.vn", "Cao Như Huỳnh", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230064", "030239230064@st.hub.edu.vn", "Lê Đình Tuấn Hưng", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230067", "030239230067@st.hub.edu.vn", "Hoàng Xuân Hương", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230089", "030239230089@st.hub.edu.vn", "Nguyễn Thị Khánh", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230094", "030239230094@st.hub.edu.vn", "Phạm Hà Nhân Kiệt", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230097", "030239230097@st.hub.edu.vn", "Nguyễn Thị Hồng Kim", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230098", "030239230098@st.hub.edu.vn", "Nguyễn Thị Thiên Kim", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230099", "030239230099@st.hub.edu.vn", "Nguyễn Thị Diệu Lam", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230105", "030239230105@st.hub.edu.vn", "Hồ Tống Khánh Linh", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230108", "030239230108@st.hub.edu.vn", "Nguyễn Hiện Hiển Linh", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230104", "030239230104@st.hub.edu.vn", "Tô Thanh Lịch", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230123", "030239230123@st.hub.edu.vn", "Nguyễn Thị Xuân Mai", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230124", "030239230124@st.hub.edu.vn", "Nguyễn Văn Mẫn", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230136", "030239230136@st.hub.edu.vn", "Huỳnh Hiếu Ngân", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230140", "030239230140@st.hub.edu.vn", "Nguyễn Thu Ngân", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230141", "030239230141@st.hub.edu.vn", "Thiều Thị Thúy Ngân", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230143", "030239230143@st.hub.edu.vn", "Đoàn Yến Nghi", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230147", "030239230147@st.hub.edu.vn", "Dương Yến Ngọc", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030238220150", "030238220150@st.hub.edu.vn", "Nguyễn Thị Vân Ngọc", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230154", "030239230154@st.hub.edu.vn", "Trịnh Thái Minh Nguyên", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230157", "030239230157@st.hub.edu.vn", "Nguyễn Đức Nhật", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230164", "030239230164@st.hub.edu.vn", "Nguyễn Võ Yến Nhi", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230175", "030239230175@st.hub.edu.vn", "Trình Nguyễn Quỳnh Như", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230178", "030239230178@st.hub.edu.vn", "Nguyễn Đào Ánh Ni", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230193", "030239230193@st.hub.edu.vn", "Đoàn Nữ Anh Phương", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230195", "030239230195@st.hub.edu.vn", "Phạm Thị Thanh Phương", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230197", "030239230197@st.hub.edu.vn", "Nguyễn Thị Ngọc Quế", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230200", "030239230200@st.hub.edu.vn", "Lê Nguyễn Tú Quyên", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030238220208", "030238220208@st.hub.edu.vn", "Bùi Thị Như Quỳnh", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230214", "030239230214@st.hub.edu.vn", "Biện Hà Thành", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230216", "030239230216@st.hub.edu.vn", "Dương Thị Thu Thảo", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230217", "030239230217@st.hub.edu.vn", "Nguyễn Thị Thanh Thảo", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230211", "030239230211@st.hub.edu.vn", "Trần Quốc Thái", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230226", "030239230226@st.hub.edu.vn", "Đặng Lộc Thiên", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230238", "030239230238@st.hub.edu.vn", "Đỗ Hiền Thục", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230232", "030239230232@st.hub.edu.vn", "Phạm Đình Anh Thư", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230234", "030239230234@st.hub.edu.vn", "Trần Thị Minh Thư", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230242", "030239230242@st.hub.edu.vn", "Phan Thị Kiều Thy", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230246", "030239230246@st.hub.edu.vn", "Đỗ Đoàn Quốc Tín", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230260", "030239230260@st.hub.edu.vn", "Ngô Thảo Trang", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230263", "030239230263@st.hub.edu.vn", "Phạm Thị Thùy Trang", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030238220271", "030238220271@st.hub.edu.vn", "Võ Ngọc Thùy Trang", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230251", "030239230251@st.hub.edu.vn", "Lê Huỳnh Mai Trâm", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230252", "030239230252@st.hub.edu.vn", "Lê Thị Bích Trâm", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230253", "030239230253@st.hub.edu.vn", "Nguyễn Ngọc Bích Trâm", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230255", "030239230255@st.hub.edu.vn", "Nguyễn Thị Ngọc Trâm", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230272", "030239230272@st.hub.edu.vn", "Võ Thanh Trúc", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230277", "030239230277@st.hub.edu.vn", "Hoàng Nguyễn Trúc Uyên", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230280", "030239230280@st.hub.edu.vn", "Phạm Thị Thục Uyên", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230283", "030239230283@st.hub.edu.vn", "Lê Thị Hồng Vân", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230285", "030239230285@st.hub.edu.vn", "Nguyễn Thị Tường Vân", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230286", "030239230286@st.hub.edu.vn", "Nguyễn Thùy Vân", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230295", "030239230295@st.hub.edu.vn", "Nguyễn Thị Thúy Vy", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230303", "030239230303@st.hub.edu.vn", "Nguyễn Hoàng Yến", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"],
    ["030239230299", "030239230299@st.hub.edu.vn", "Trần Lê Như Ý", "$2a$10$tymz1/JH8mnkeOK1ZEAORuJJlCvsZCzlHKtMqXqNvMz/nXPVKYU1S", "student", "true", "2026-05-15T16:36:52.865Z"]
  ];
  
  sheet.clear();
  sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
  sheet.getRange(2, 1, data.length, headers.length).setValues(data);
  
  SpreadsheetApp.getUi().alert("Đã import thành công " + data.length + " người dùng!");
}
