/**
 * Google Apps Script để import danh sách lớp SEO D01 (ITS340)
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
  
  const headers = ["student_id", "email", "full_name", "password", "role", "must_change_password", "created_at", "password_hash"];
  
  const data = [
    ["admin", "dangph@hub.edu.vn", "ThS. Phó Hải Đăng", "$2a$10$cMPFDO9DCGQwbbnBMxDhL.ql.5guZUoZzDIHh3YFuxr3jHHAElt7u", "admin", "false", "2026-05-20T01:06:03.393Z", "$2a$10$cMPFDO9DCGQwbbnBMxDhL.ql.5guZUoZzDIHh3YFuxr3jHHAElt7u"],
    ["030239230016", "030239230016@st.hub.edu.vn", "Vũ Trúc Lan Anh", "$2a$10$w/WIhHbvzg4iZ1hMBj4pVeYtNjxeRUya3FWWuJ3F9Me9IGDqNvj9m", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$w/WIhHbvzg4iZ1hMBj4pVeYtNjxeRUya3FWWuJ3F9Me9IGDqNvj9m"],
    ["030239230017", "030239230017@st.hub.edu.vn", "Lý Tố Ánh", "$2a$10$vRO4ylQaCfkPJb5oTjNxb.IFIwyJMU60ekfAZIrYvR3YiUx1rc73u", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$vRO4ylQaCfkPJb5oTjNxb.IFIwyJMU60ekfAZIrYvR3YiUx1rc73u"],
    ["030239230021", "030239230021@st.hub.edu.vn", "Đồng Quảng Bình", "$2a$10$SBIAzB.3m/CDAPNIz/1dm.iy89wbOIcB22WWE7Wrpv9FIDZs5GOAW", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$SBIAzB.3m/CDAPNIz/1dm.iy89wbOIcB22WWE7Wrpv9FIDZs5GOAW"],
    ["030239230023", "030239230023@st.hub.edu.vn", "Nguyễn Ngọc Kim Chi", "$2a$10$LykJNYhZJ0xYKVRWpetTpOSDM.0xzWvhtUa2e.uUlwrpX8u5iS40W", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$LykJNYhZJ0xYKVRWpetTpOSDM.0xzWvhtUa2e.uUlwrpX8u5iS40W"],
    ["030239230024", "030239230024@st.hub.edu.vn", "Trần Văn Chiến", "$2a$10$GtA4ESseOuWZSy50wZvwUugNXWOGKcyOnwiNGb1k4q0G2f.zKQtDO", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$GtA4ESseOuWZSy50wZvwUugNXWOGKcyOnwiNGb1k4q0G2f.zKQtDO"],
    ["030239230025", "030239230025@st.hub.edu.vn", "Tô Nhật Chương", "$2a$10$8D0T6oxpe95KCiqiW7eKQu4ylbO8UUQClIWIWrAIgrjgNTr2JU1jy", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$8D0T6oxpe95KCiqiW7eKQu4ylbO8UUQClIWIWrAIgrjgNTr2JU1jy"],
    ["030239230033", "030239230033@st.hub.edu.vn", "Dương Thị Phương Dung", "$2a$10$QtWW2MRRafbX5ldQ2ii1TeX61E/vuu9YfNAMuaOy9IWw4uBiZO.yC", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$QtWW2MRRafbX5ldQ2ii1TeX61E/vuu9YfNAMuaOy9IWw4uBiZO.yC"],
    ["030239230034", "030239230034@st.hub.edu.vn", "Phạm Thị Thùy Dung", "$2a$10$UdO68DXnFj673olH05IDQOLJ45xUTpbsN/MTMwb5SpQ40/3EGdYRC", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$UdO68DXnFj673olH05IDQOLJ45xUTpbsN/MTMwb5SpQ40/3EGdYRC"],
    ["030239230041", "030239230041@st.hub.edu.vn", "Nguyễn Quỳnh Giang", "$2a$10$9P0L0NNIhuLCEH9AIftBXurDfS9Rwen6Vk.xXNP06uebERWjBGrHO", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$9P0L0NNIhuLCEH9AIftBXurDfS9Rwen6Vk.xXNP06uebERWjBGrHO"],
    ["030239230045", "030239230045@st.hub.edu.vn", "Trần Thị Hà", "$2a$10$EfCfpqW5JWQkkX.GzhM8Z.71PviAmbxCLA0rVbyV3wrikA5URTGtu", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$EfCfpqW5JWQkkX.GzhM8Z.71PviAmbxCLA0rVbyV3wrikA5URTGtu"],
    ["030239230046", "030239230046@st.hub.edu.vn", "Trần Thị Thu Hà", "$2a$10$W5PAbGxfgRn9wSbWniqvyun30ODjZA1szbyqwgaVWB7e9Xq2cLYsm", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$W5PAbGxfgRn9wSbWniqvyun30ODjZA1szbyqwgaVWB7e9Xq2cLYsm"],
    ["030239230047", "030239230047@st.hub.edu.vn", "Trần Ngọc Như Hải", "$2a$10$P.8ofieTbEnGCWy9cEkZl.LdlJ7TeDrBugNE6c14KWK9XlntS0h/m", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$P.8ofieTbEnGCWy9cEkZl.LdlJ7TeDrBugNE6c14KWK9XlntS0h/m"],
    ["030239230048", "030239230048@st.hub.edu.vn", "Trần Thanh Hải", "$2a$10$u9nHm8T7m54G7he.4B2OD.ZUdEpYHHJX9aX0Do3LdMtV7X8TSm.Ca", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$u9nHm8T7m54G7he.4B2OD.ZUdEpYHHJX9aX0Do3LdMtV7X8TSm.Ca"],
    ["030239230055", "030239230055@st.hub.edu.vn", "Trần Thị Thanh Hiền", "$2a$10$Sg6FS3Wl7UY0H4g5oYwcdukH4VmCCkfna1yy/AQrJqRFa295L46sy", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$Sg6FS3Wl7UY0H4g5oYwcdukH4VmCCkfna1yy/AQrJqRFa295L46sy"],
    ["030239230059", "030239230059@st.hub.edu.vn", "Nguyễn Văn Hoàng", "$2a$10$VnLzzpWbMK5b4jB8ZRNjBO9uP0pXz3VmyJ5yfaTM/oOFNgPMqhixG", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$VnLzzpWbMK5b4jB8ZRNjBO9uP0pXz3VmyJ5yfaTM/oOFNgPMqhixG"],
    ["030239230071", "030239230071@st.hub.edu.vn", "Đoàn Trung Nhật Huy", "$2a$10$riWeTIYkibtztStn0XjFU.VqeetsWW6R5yHR3JJUdvUh/33ZxR8/e", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$riWeTIYkibtztStn0XjFU.VqeetsWW6R5yHR3JJUdvUh/33ZxR8/e"],
    ["030239230067", "030239230067@st.hub.edu.vn", "Hoàng Xuân Hương", "$2a$10$u.wMy7XjUojdq9dIFW2ciuii6E5luNH/l7JroOssj18IiqWQDDlk6", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$u.wMy7XjUojdq9dIFW2ciuii6E5luNH/l7JroOssj18IiqWQDDlk6"],
    ["030239230085", "030239230085@st.hub.edu.vn", "Huỳnh Gia Khang", "$2a$10$9QS50jl.ZZQiMN1FjUOlfuND0ejw1CEgNTuW7NgVx9vTpZ8Hh3Rs6", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$9QS50jl.ZZQiMN1FjUOlfuND0ejw1CEgNTuW7NgVx9vTpZ8Hh3Rs6"],
    ["030239230089", "030239230089@st.hub.edu.vn", "Nguyễn Thị Khánh", "$2a$10$Rz6zb5EG8bs4PvPQV5vYb.HuJkcG3DW9mbTxW.XzatL.Z18bnoWOG", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$Rz6zb5EG8bs4PvPQV5vYb.HuJkcG3DW9mbTxW.XzatL.Z18bnoWOG"],
    ["030239230108", "030239230108@st.hub.edu.vn", "Nguyễn Hiện Hiển Linh", "$2a$10$I2GRxERHrLNnGTmkCiPuj.ZEL3gw86Lhl2EdgVggRSkaknufVvg3G", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$I2GRxERHrLNnGTmkCiPuj.ZEL3gw86Lhl2EdgVggRSkaknufVvg3G"],
    ["030239230104", "030239230104@st.hub.edu.vn", "Tô Thanh Lịch", "$2a$10$mBYNgGqO4aCtlpFiwXHEsOTzRdAV4iBM/rwzw.XG9BkjUG3Crgqey", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$mBYNgGqO4aCtlpFiwXHEsOTzRdAV4iBM/rwzw.XG9BkjUG3Crgqey"],
    ["030239230123", "030239230123@st.hub.edu.vn", "Nguyễn Thị Xuân Mai", "$2a$10$/wWau7Sns01pxwyz6z5obOJUADtlz6wPwHHDFy7SA3oxmF3sWNDS.", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$/wWau7Sns01pxwyz6z5obOJUADtlz6wPwHHDFy7SA3oxmF3sWNDS."],
    ["030239230136", "030239230136@st.hub.edu.vn", "Huỳnh Hiếu Ngân", "$2a$10$MtsJBHU4HhgG13Jvq6kRR.dzCmGfrSOkR2fJ5g98maLMyFUq7rLWi", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$MtsJBHU4HhgG13Jvq6kRR.dzCmGfrSOkR2fJ5g98maLMyFUq7rLWi"],
    ["030239230141", "030239230141@st.hub.edu.vn", "Thiều Thị Thúy Ngân", "$2a$10$upKOu8t4aAh0ivGvHQSb7ujX4xqTG0n.DuLfIAJ6hgrs0aYqp7IGC", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$upKOu8t4aAh0ivGvHQSb7ujX4xqTG0n.DuLfIAJ6hgrs0aYqp7IGC"],
    ["030239230154", "030239230154@st.hub.edu.vn", "Trịnh Thái Minh Nguyên", "$2a$10$/9GuPbChFSV.wNJTS7gFcuH7wYtLnti43XVier5x4YZdBVoTI.uoe", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$/9GuPbChFSV.wNJTS7gFcuH7wYtLnti43XVier5x4YZdBVoTI.uoe"],
    ["030239230164", "030239230164@st.hub.edu.vn", "Nguyễn Võ Yến Nhi", "$2a$10$AAj6Q86o1lXdve3WvtRiA.xHYMby7zV7m8dwfXY3tjzvjCs8GwOFa", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$AAj6Q86o1lXdve3WvtRiA.xHYMby7zV7m8dwfXY3tjzvjCs8GwOFa"],
    ["030235190102", "030235190102@st.hub.edu.vn", "Phan Nguyễn Yến Nhi", "$2a$10$xwZ9fzeFfqKEDdd1Ck3qGe2I4dRuJXlzra0k/KoMFgXergjBJ1rRi", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$xwZ9fzeFfqKEDdd1Ck3qGe2I4dRuJXlzra0k/KoMFgXergjBJ1rRi"],
    ["030239230177", "030239230177@st.hub.edu.vn", "Võ Tuyết Nhung", "$2a$10$0KsGWNKGyQE8xvQu8eM0vOu/7v45AtEGjA3ljZ5Jyq6Fj1FAx3cSW", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$0KsGWNKGyQE8xvQu8eM0vOu/7v45AtEGjA3ljZ5Jyq6Fj1FAx3cSW"],
    ["030239230175", "030239230175@st.hub.edu.vn", "Trình Nguyễn Quỳnh Như", "$2a$10$Vo/3o616Zxlc7WM4dWagAOzO.O0Bw4P3hIBQwqv1colWs7AcFmJYS", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$Vo/3o616Zxlc7WM4dWagAOzO.O0Bw4P3hIBQwqv1colWs7AcFmJYS"],
    ["030239230182", "030239230182@st.hub.edu.vn", "Trần Thị Mai Oanh", "$2a$10$uqJF/oFW7VnRvJsnqshkceiSVZ/8wrAqgvDnkxBu3R6/.apFdbSX2", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$uqJF/oFW7VnRvJsnqshkceiSVZ/8wrAqgvDnkxBu3R6/.apFdbSX2"],
    ["030239230197", "030239230197@st.hub.edu.vn", "Nguyễn Thị Ngọc Quế", "$2a$10$csr7PxLE65EsHcbsfVq84O6oW4J9teCacSHqK3KKuV/YIjxuY5auK", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$csr7PxLE65EsHcbsfVq84O6oW4J9teCacSHqK3KKuV/YIjxuY5auK"],
    ["030239230200", "030239230200@st.hub.edu.vn", "Lê Nguyễn Tú Quyên", "$2a$10$8AO2WjXooNP0pRgHaq6KXO5uex/I9ltden5Q.2lxdiPM.MtBOHrcO", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$8AO2WjXooNP0pRgHaq6KXO5uex/I9ltden5Q.2lxdiPM.MtBOHrcO"],
    ["030239230203", "030239230203@st.hub.edu.vn", "Nguyễn Đặng Như Quỳnh", "$2a$10$J57ziG4BN.b72JMCZnWnn.ZUsmMdPMHc3EEqT5LS/H0YjFZcA9Khu", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$J57ziG4BN.b72JMCZnWnn.ZUsmMdPMHc3EEqT5LS/H0YjFZcA9Khu"],
    ["030239230206", "030239230206@st.hub.edu.vn", "Trịnh Diễm Quỳnh", "$2a$10$16RFpzNqwLbXURLsCSm5UOgH5CX/p85zNKl46ejKvAvyppqzYSr/.", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$16RFpzNqwLbXURLsCSm5UOgH5CX/p85zNKl46ejKvAvyppqzYSr/."],
    ["030239230209", "030239230209@st.hub.edu.vn", "Phan Thị Sáng", "$2a$10$iGl6gH4u4LIjuFSrCTHVq.pWd0z0.QEehueho3R85J2HhETiL0Wwe", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$iGl6gH4u4LIjuFSrCTHVq.pWd0z0.QEehueho3R85J2HhETiL0Wwe"],
    ["030239230216", "030239230216@st.hub.edu.vn", "Dương Thị Thu Thảo", "$2a$10$XfF.N9uP7d/hMxVztqthXug32v3LcSseno4UcXEZV5dIlL9wscWmK", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$XfF.N9uP7d/hMxVztqthXug32v3LcSseno4UcXEZV5dIlL9wscWmK"],
    ["030239230217", "030239230217@st.hub.edu.vn", "Nguyễn Thị Thanh Thảo", "$2a$10$4.2b7pVVta4waSrcPJ90c.T.bO8yaP5GL/.ceC9Iwp.b3plcPCHYG", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$4.2b7pVVta4waSrcPJ90c.T.bO8yaP5GL/.ceC9Iwp.b3plcPCHYG"],
    ["030239230225", "030239230225@st.hub.edu.vn", "Nguyễn Ngọc Phương Thi", "$2a$10$1sINygpjwy/T0ZTTn0LwmeaGLlpgF4xa34iLEe8b6.3vmTn.OO6Fy", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$1sINygpjwy/T0ZTTn0LwmeaGLlpgF4xa34iLEe8b6.3vmTn.OO6Fy"],
    ["030239230237", "030239230237@st.hub.edu.vn", "Vương Minh Thuận", "$2a$10$WB4o59B6SuYO3vxR8mNGgO39/fyUgkC6Gky7WG5RDpM26uawYRwPC", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$WB4o59B6SuYO3vxR8mNGgO39/fyUgkC6Gky7WG5RDpM26uawYRwPC"],
    ["030239230238", "030239230238@st.hub.edu.vn", "Đỗ Hiền Thục", "$2a$10$6AdNawvqKn8TSzEpL3DYZe6MaHs43Pjdcpz4oEHzySwTE0Y2UAUHi", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$6AdNawvqKn8TSzEpL3DYZe6MaHs43Pjdcpz4oEHzySwTE0Y2UAUHi"],
    ["030239230233", "030239230233@st.hub.edu.vn", "Phan Thị Anh Thư", "$2a$10$rEKLnJ9dQf.gR7.0a4h1weFMgyUKgP7F7OJeX4NXAAm/llayM77ga", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$rEKLnJ9dQf.gR7.0a4h1weFMgyUKgP7F7OJeX4NXAAm/llayM77ga"],
    ["030239230234", "030239230234@st.hub.edu.vn", "Trần Thị Minh Thư", "$2a$10$eK/bOFnj7Bg9yXCc5tDf8up3lPokUPXDuxRzqU0SjPI3C5miCxrFq", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$eK/bOFnj7Bg9yXCc5tDf8up3lPokUPXDuxRzqU0SjPI3C5miCxrFq"],
    ["030239230262", "030239230262@st.hub.edu.vn", "Nguyễn Thùy Trang", "$2a$10$xtnGAJiOEYt.KsuIi1hPQOCc1BPdfw0njHXQp4gqPhg7C33tc7lJy", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$xtnGAJiOEYt.KsuIi1hPQOCc1BPdfw0njHXQp4gqPhg7C33tc7lJy"],
    ["030239230263", "030239230263@st.hub.edu.vn", "Phạm Thị Thùy Trang", "$2a$10$v2M3u8MsLTv09/jyv58ZjO0p9oJODFIyG0LruazAZ5I0w4K4LAtTC", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$v2M3u8MsLTv09/jyv58ZjO0p9oJODFIyG0LruazAZ5I0w4K4LAtTC"],
    ["030239230252", "030239230252@st.hub.edu.vn", "Lê Thị Bích Trâm", "$2a$10$gx1FTngEJOfEPDelUXoXFO89ot.kYF0oDiATB3cKg6PqFch9qt6qO", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$gx1FTngEJOfEPDelUXoXFO89ot.kYF0oDiATB3cKg6PqFch9qt6qO"],
    ["030239230253", "030239230253@st.hub.edu.vn", "Nguyễn Ngọc Bích Trâm", "$2a$10$yTj7LUk0pu7pkRFNI9vXu.Dd/ymi8nr34GhFLVtNT58czChCdPz/K", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$yTj7LUk0pu7pkRFNI9vXu.Dd/ymi8nr34GhFLVtNT58czChCdPz/K"],
    ["030239230255", "030239230255@st.hub.edu.vn", "Nguyễn Thị Ngọc Trâm", "$2a$10$/heL0nKvsE2dmEOflUOGIeUyLCUIUG1Tpvm4iH07gIRHjUbP8.QsC", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$/heL0nKvsE2dmEOflUOGIeUyLCUIUG1Tpvm4iH07gIRHjUbP8.QsC"],
    ["030239230268", "030239230268@st.hub.edu.vn", "Nguyễn Vũ Thùy Trinh", "$2a$10$wbzbPdRcvVMnghB.qba7yuj2ORIQNUPbK0zxf/lt6CZ5z6kRUWMxG", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$wbzbPdRcvVMnghB.qba7yuj2ORIQNUPbK0zxf/lt6CZ5z6kRUWMxG"],
    ["030239230269", "030239230269@st.hub.edu.vn", "Võ Hoàng Phương Trinh", "$2a$10$EAwhNS2qSvjoOxbuT1IRles3fZYd8XLxmGKhpNEmyfaMJwD7/QgXG", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$EAwhNS2qSvjoOxbuT1IRles3fZYd8XLxmGKhpNEmyfaMJwD7/QgXG"],
    ["030239230277", "030239230277@st.hub.edu.vn", "Hoàng Nguyễn Trúc Uyên", "$2a$10$tREMY9hehexD51F0EO4qbe3lRAsS8J/PsQlkncmkomEs8iqpx8t56", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$tREMY9hehexD51F0EO4qbe3lRAsS8J/PsQlkncmkomEs8iqpx8t56"],
    ["030239230280", "030239230280@st.hub.edu.vn", "Phạm Thị Thục Uyên", "$2a$10$1BmGHVZ0Nn9ulYYotH2.retWNgQS5q8ppQhu0rlmvyjsyhcVTqUF2", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$1BmGHVZ0Nn9ulYYotH2.retWNgQS5q8ppQhu0rlmvyjsyhcVTqUF2"],
    ["030239230283", "030239230283@st.hub.edu.vn", "Lê Thị Hồng Vân", "$2a$10$eMxFwP4dtEtyUXCGNBnExOVLRurdAADkw2A3Lc.5aOrkUst8A5gOe", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$eMxFwP4dtEtyUXCGNBnExOVLRurdAADkw2A3Lc.5aOrkUst8A5gOe"],
    ["030239230285", "030239230285@st.hub.edu.vn", "Nguyễn Thị Tường Vân", "$2a$10$AXk1KHDWrpgHR1K42cDKW.nN2K2iCXNlfGHMHqbThlyRAN9geUPe2", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$AXk1KHDWrpgHR1K42cDKW.nN2K2iCXNlfGHMHqbThlyRAN9geUPe2"],
    ["030239230289", "030239230289@st.hub.edu.vn", "Nguyễn Phạm Thảo Vi", "$2a$10$q8w9nVZWjl5XZBHDa4w7VOhVK1YfRq5twwqBvsQDIfwpJyPzmh1Sy", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$q8w9nVZWjl5XZBHDa4w7VOhVK1YfRq5twwqBvsQDIfwpJyPzmh1Sy"],
    ["030239230295", "030239230295@st.hub.edu.vn", "Nguyễn Thị Thúy Vy", "$2a$10$ASHmBzm2cZQkp06T1QbGfuFixLcBgKc7aweYhEwWfR0fW4TS4z0.i", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$ASHmBzm2cZQkp06T1QbGfuFixLcBgKc7aweYhEwWfR0fW4TS4z0.i"],
    ["030239230300", "030239230300@st.hub.edu.vn", "Đặng Phi Yên", "$2a$10$WGFmdpmcxBh6iHx2iSGA0.wes3wlO7Iej6X4ZuZYMumn.QlQEaUIq", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$WGFmdpmcxBh6iHx2iSGA0.wes3wlO7Iej6X4ZuZYMumn.QlQEaUIq"],
    ["030239230299", "030239230299@st.hub.edu.vn", "Trần Lê Như Ý", "$2a$10$2M26rRVgk.G0VmwUEI2dSO1JxFFbS/rpsxiJ8DBr/mokckYYRkwuC", "student", "true", "2026-05-20T01:06:03.393Z", "$2a$10$2M26rRVgk.G0VmwUEI2dSO1JxFFbS/rpsxiJ8DBr/mokckYYRkwuC"]
  ];
  
  sheet.clear();
  // Set headers ở dòng 1
  sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
  // Set dữ liệu bắt đầu từ dòng 2
  sheet.getRange(2, 1, data.length, headers.length).setValues(data);
  
  // Định dạng cột student_id và email thành dạng TEXT để tránh mất số 0 ở đầu
  sheet.getRange(2, 1, data.length, 1).setNumberFormat("@");
  sheet.getRange(2, 2, data.length, 1).setNumberFormat("@");
  
  SpreadsheetApp.getUi().alert("🎉 Đã import thành công " + data.length + " tài khoản (1 Admin + 57 Sinh viên) vào bảng 'students'!");
}
