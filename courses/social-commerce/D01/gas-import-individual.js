
function importStudentsWithIDAsPassword() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName("students");
  if (!sheet) {
    sheet = ss.insertSheet("students");
  }
  
  const headers = ["student_id", "email", "full_name", "password_hash", "role", "must_change_password", "created_at"];
  
  const data = [
    ["admin", "dangph@hub.edu.vn", "ThS. Phó Hải Đăng", "$2a$10$rHGDml6/7WvO.PqoUWMk.uk7LFAhcQqOHhMJe7Fmn2tvEeYcll/ha", "admin", "false", "2026-05-15T16:49:05.503Z"],
    ["030239230015", "030239230015@st.hub.edu.vn", "Võ Thị Vân Anh", "$2a$10$6UfeMyZgLR2643K4Tb3MvecqpEJFv99B1rQp95KGH8n1Zi2hlkgsC", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230016", "030239230016@st.hub.edu.vn", "Vũ Trúc Lan Anh", "$2a$10$FQ3veTBYpXH4zEcQEU6BeuF38g08qauxT.SQAwMJaHiv1GHp09oxO", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230017", "030239230017@st.hub.edu.vn", "Lý Tố Ánh", "$2a$10$y6l17cO4MvcDLjA9MBW8n.nT5l7A9tCTpgi7K5v5LeKe78jVCwUjW", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230025", "030239230025@st.hub.edu.vn", "Tô Nhật Chương", "$2a$10$gVs6Ccae331IG9.wogiFPe9FfqcC/fuyTOGSIChj3l5UwQ/M3ZVjq", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230033", "030239230033@st.hub.edu.vn", "Dương Thị Phương Dung", "$2a$10$3LJp4rIy44Di9hUqKWJWp.zLo5iK6pgk4LNxciwUtEHUaV742gbaS", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230034", "030239230034@st.hub.edu.vn", "Phạm Thị Thùy Dung", "$2a$10$yPQVvii7.lqq5LpLTLTAv.O8w/J4Sl8aUB4Y/1RcEWLShjwXBk6IS", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230029", "030239230029@st.hub.edu.vn", "Đoàn Quốc Đại", "$2a$10$ngIEzFwnxWodw0lZ1OYv8eDIDvVe3b4.l4B/H2x.A/l2YIUxb34gW", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230041", "030239230041@st.hub.edu.vn", "Nguyễn Quỳnh Giang", "$2a$10$Tb.sqaJ.VhehIiUm.Vt6LexTLwKe2FqJOA7T7sjJldjaieToF6tVS", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230045", "030239230045@st.hub.edu.vn", "Trần Thị Hà", "$2a$10$LHI4ptYcpe.ALUKjHCqmw.j5MopYNCzHIvd7Z.jEkWgniu3pdXlim", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230048", "030239230048@st.hub.edu.vn", "Trần Thanh Hải", "$2a$10$Xo2x3Ye5gmEAIVOmSRqXrOZyPx7K/cUAqlNGArqfaKurry4AYtt3i", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230050", "030239230050@st.hub.edu.vn", "Lê Gia Hân", "$2a$10$ETZhYBj5mC7QzW.lnE1UQeCZYo5Y8xu1fUNLjKOU.3XuFSdvCUIzW", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230054", "030239230054@st.hub.edu.vn", "Nguyễn Trung Hiền", "$2a$10$ctFSk9e6HoyhVqdy7aW1WOpcJXZbklyp1ow9ezwwB0p1V2OpcNt76", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230055", "030239230055@st.hub.edu.vn", "Trần Thị Thanh Hiền", "$2a$10$jTyjvVusvaKiUQazyfpYV.MqA4dWjvjukte9k6jwf.NWsidJ4g3gK", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230059", "030239230059@st.hub.edu.vn", "Nguyễn Văn Hoàng", "$2a$10$l8D9Pqb3/yWYaoYCxRogl.7XcjYRcRzrop/pJi23yAz0uom4tmK5O", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230071", "030239230071@st.hub.edu.vn", "Đoàn Trung Nhật Huy", "$2a$10$QQb7NMwp1J6dxjzwLaY7RO9Vt1rpHOmYdko2TIKhbrJP7uEet8ET6", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230072", "030239230072@st.hub.edu.vn", "Huỳnh Đức Huy", "$2a$10$zw11EV92tj3geD3wn6I2LudPWCW/vwPa.s5EEMArTmR1xc524MWCe", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230074", "030239230074@st.hub.edu.vn", "Tôn Thất Gia Huy", "$2a$10$wxpnWs9MB/JCn9u0Mab8wO8S08XOnQX9iUQu0vdTFq/dXQv76nucS", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230078", "030239230078@st.hub.edu.vn", "Nguyễn Thị Huyền", "$2a$10$Sod8sJ7OM8k/wNPr881wXeYd/PlG620aH8Tv0ZjgtXsBk3wOnZj7K", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230081", "030239230081@st.hub.edu.vn", "Vũ Trần Khánh Huyền", "$2a$10$gjFiftT6db.uZ1SU2MRuweCjYuXsFScAS0rgj.rMCo3rVZx1Y2aIq", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230083", "030239230083@st.hub.edu.vn", "Cao Như Huỳnh", "$2a$10$R1f2fXwCWD13TkJ2K9k/p.UBCgSLKeCIsoEanu3Inql9lLEO8cg36", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230064", "030239230064@st.hub.edu.vn", "Lê Đình Tuấn Hưng", "$2a$10$vfIG.bhJ8HDaVOY2Vpj3SeHkQ105dUv8uCiyBUdrjmQ3c6B2tRYTS", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230067", "030239230067@st.hub.edu.vn", "Hoàng Xuân Hương", "$2a$10$qiIr77UnUjUDG70.6LtMP.rbL4LMJR5URDkIrlqkiEdaZDlBmVSku", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230089", "030239230089@st.hub.edu.vn", "Nguyễn Thị Khánh", "$2a$10$CH7RHylDsUnJWwhGAyoEfe0z/Oz7dMMMiO05Kp/WLyh4AzTHL/OkS", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230094", "030239230094@st.hub.edu.vn", "Phạm Hà Nhân Kiệt", "$2a$10$2cXtsKRRVTKpF243ac04Qu2pyZQC9gM7uXWLAONOW9JPL0mFdCHoq", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230097", "030239230097@st.hub.edu.vn", "Nguyễn Thị Hồng Kim", "$2a$10$cWqQ2tdlwWNMaMypi4Fwyus5cRvBaw1ei.oVeHtGxEYqCIefvHos.", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230098", "030239230098@st.hub.edu.vn", "Nguyễn Thị Thiên Kim", "$2a$10$dH2BNS6D65GLOYrNqi98eODSjJbno70BoHbBi3JnRK3XY0iQSii8K", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230099", "030239230099@st.hub.edu.vn", "Nguyễn Thị Diệu Lam", "$2a$10$DxHtT9MTKegdEh5UUMSvZ.72U2AsZTGAcgDnb8E9xHsKBeTujxONe", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230105", "030239230105@st.hub.edu.vn", "Hồ Tống Khánh Linh", "$2a$10$65ZQQgDAz4pOKHKmUgAAzu2DwP56RutSzsH/vAXctrKNo06KMk.2a", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230108", "030239230108@st.hub.edu.vn", "Nguyễn Hiện Hiển Linh", "$2a$10$iy9RDYWVV.EOYZ.trKxpeutmeOdRh6et20193N7Fxm74Df8pZ3qQW", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230104", "030239230104@st.hub.edu.vn", "Tô Thanh Lịch", "$2a$10$scVReMbP/RIkQ23olBRMeOSoLSsfwXHsVB4EVxqcQFNobByQDaD26", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230123", "030239230123@st.hub.edu.vn", "Nguyễn Thị Xuân Mai", "$2a$10$xIzc3SsnGfgXFtgapS087u0xZ4kjlK6L77gd9lYAyH6xPng5sidWq", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230124", "030239230124@st.hub.edu.vn", "Nguyễn Văn Mẫn", "$2a$10$oIQ/Z7HeDZFNgW.w1Xo1meTDISUiWL9HicH8qVpTqHeUSqiGrXQQ6", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230136", "030239230136@st.hub.edu.vn", "Huỳnh Hiếu Ngân", "$2a$10$U3KlhnPP5iqNvvnt3LGDY.34biMaywxv0g1jgWOxNsgQY7ac39VMO", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230140", "030239230140@st.hub.edu.vn", "Nguyễn Thu Ngân", "$2a$10$lgfbHTHyb4bsU2pOuJuM1ubCN1qCvcwHtBylCrwNgDjjRka8muc8a", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230141", "030239230141@st.hub.edu.vn", "Thiều Thị Thúy Ngân", "$2a$10$fLUKNj5/PaayWTRzG0n7Aum2ToZ8ZEMDtE5Juy2InPT9/Olct7Ftu", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230143", "030239230143@st.hub.edu.vn", "Đoàn Yến Nghi", "$2a$10$NkPdTHg1DiZWedorZDP68OSQ.BzCKXTr9IFQ2jTbICWx4gjxXRojG", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230147", "030239230147@st.hub.edu.vn", "Dương Yến Ngọc", "$2a$10$3/1bthalBaPWOy3gDgRKnOHg1kK2OoB0quJ4M6SVO0A7x1zBBHtHG", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030238220150", "030238220150@st.hub.edu.vn", "Nguyễn Thị Vân Ngọc", "$2a$10$xnPOp3BjQJqiKeeXOQ6Nu.n7C6SSbu0J2i.ZojNXDO8i8vyyhFY2a", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230154", "030239230154@st.hub.edu.vn", "Trịnh Thái Minh Nguyên", "$2a$10$xmp7BzZDBptmxmbu3BI0Wu.8rrm6ZWNjF41ouiY7mZK07c4YVo65G", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230157", "030239230157@st.hub.edu.vn", "Nguyễn Đức Nhật", "$2a$10$xGwIMxy4ZUK4DYmGNhij/OaPJ.hL2htQV9U7xLe2NMoYS3MZz7QoC", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230164", "030239230164@st.hub.edu.vn", "Nguyễn Võ Yến Nhi", "$2a$10$nvTFQZqziTD5H.H3H9ixG.H.MvHOjjq0v5YiWKMU5vJg3wt9q1MKm", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230175", "030239230175@st.hub.edu.vn", "Trình Nguyễn Quỳnh Như", "$2a$10$hgr2J6ZPUKi3oljE2Y40MugSe6eGEAO7.Ij9EP0ZLJVhhJejcRNk2", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230178", "030239230178@st.hub.edu.vn", "Nguyễn Đào Ánh Ni", "$2a$10$3.vWWDvZ.R5OPg1W65cSx.ROQ2FmggfisxmYxiObb6fzhbpu/8eHu", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230193", "030239230193@st.hub.edu.vn", "Đoàn Nữ Anh Phương", "$2a$10$qWkgiO.5px7HMG9Cq2CwBOkUKjzoJjdyL9b3uW/wpfIlpNBXCwZf2", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230195", "030239230195@st.hub.edu.vn", "Phạm Thị Thanh Phương", "$2a$10$csMRmPnHRddWE9fzE64P/.VduqqfnlaZCENWNZLy5La4tvymeNuzO", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230197", "030239230197@st.hub.edu.vn", "Nguyễn Thị Ngọc Quế", "$2a$10$cqHNa/u7CeZrT8ZXnhp.5.A24UjoqHx/8qf8TdVFM6Qb6CTz.qCv6", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230200", "030239230200@st.hub.edu.vn", "Lê Nguyễn Tú Quyên", "$2a$10$hc5UwMjWi4Fs50uPSRTU0eJro4dAFoZjTwHBkjlAdOtw96bYU84kO", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030238220208", "030238220208@st.hub.edu.vn", "Bùi Thị Như Quỳnh", "$2a$10$jjbGDDulcPjv8eGsRwdJuOQgbc7bRpmn49mbw77duj5KRn4m.ykDi", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230214", "030239230214@st.hub.edu.vn", "Biện Hà Thành", "$2a$10$osV5CEcxZTEEh4pxw3sL8OziXY208rABqJB9Naa2ZCBWP6Pc.HNsS", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230216", "030239230216@st.hub.edu.vn", "Dương Thị Thu Thảo", "$2a$10$AWuBHVvT4g7yUmTY3jggae0SN.O6kB0V7NYju88TcWsRmS7wGh31a", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230217", "030239230217@st.hub.edu.vn", "Nguyễn Thị Thanh Thảo", "$2a$10$Hg8RslwXfsuXgBxMOVj2l.4Eo1Wk0dissOURBoGE9GiuBtBr6E26m", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230211", "030239230211@st.hub.edu.vn", "Trần Quốc Thái", "$2a$10$jNN0wuvYDD2FMweXHub7A.WrnMM5lD.7K81XBFWLkBs6tzQCrQinu", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230226", "030239230226@st.hub.edu.vn", "Đặng Lộc Thiên", "$2a$10$I/SSWTZmSfWjzqrtNVcCDemKzFp1.l32jrIkeY2LI//HwOYnOl7lK", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230238", "030239230238@st.hub.edu.vn", "Đỗ Hiền Thục", "$2a$10$8IrnhWcQrmcaFLUeSBGGiekk9ucvVzLK4lE/MTOr3a4lfMkWKC4QC", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230232", "030239230232@st.hub.edu.vn", "Phạm Đình Anh Thư", "$2a$10$BGWgDxiPKWGWgsyrqS3oTunZwwyGD3DNBULnNxqdplQHITUaC0WFy", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230234", "030239230234@st.hub.edu.vn", "Trần Thị Minh Thư", "$2a$10$vYtQN3jpPct0/cVo42bBNu1hsjyz8Xs1USUosIbpD7tmZiWVIebKq", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230242", "030239230242@st.hub.edu.vn", "Phan Thị Kiều Thy", "$2a$10$fUDdqmC4dxoRPKcQcFrmbu86RGF2kx1Jug2y1DtzkQjJdnV3a9Ef.", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230246", "030239230246@st.hub.edu.vn", "Đỗ Đoàn Quốc Tín", "$2a$10$rv1EyafgkCXkTXJFHTLViOPP5WPgJvQXuZI/XGF8H1/7bq4nzWcnq", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230260", "030239230260@st.hub.edu.vn", "Ngô Thảo Trang", "$2a$10$lT72LCNB/PJnM4M5lPuh3e/E5TUqzseSEfgtECOrnX3O.aGJzgd02", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230263", "030239230263@st.hub.edu.vn", "Phạm Thị Thùy Trang", "$2a$10$qtk/v1UTRQSA6auCJ1HrturmgXBK31xrhz0ulIZ19wnfW8OJDidC.", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030238220271", "030238220271@st.hub.edu.vn", "Võ Ngọc Thùy Trang", "$2a$10$KhFP4VsefcWsBTbkpLoPO.GZs4jYimzVQLWxFwD.sH2bgDK//Qfem", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230251", "030239230251@st.hub.edu.vn", "Lê Huỳnh Mai Trâm", "$2a$10$s3dSI0APjMnCFvTQ0r/gxO6kHbB/VlrCpPWZd0QvXTaPc0hwkHKji", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230252", "030239230252@st.hub.edu.vn", "Lê Thị Bích Trâm", "$2a$10$N/djmmO6gQcJ.R4yQ5Q7AeEYcnHZ9GLjqbsthvl8t2nj3o1gsuRna", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230253", "030239230253@st.hub.edu.vn", "Nguyễn Ngọc Bích Trâm", "$2a$10$mvkHEJAhYyl413.S6y0ffufYZQTgc.djXJifH4I6OIaT8viVC2WMy", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230255", "030239230255@st.hub.edu.vn", "Nguyễn Thị Ngọc Trâm", "$2a$10$nXXjxMpjN6z7o1ioKUK6m.DlxJOqgEC/16ZV.rkFswQMvBYKM8KFa", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230272", "030239230272@st.hub.edu.vn", "Võ Thanh Trúc", "$2a$10$.MNnU4aB6eQYI8zpsrxqau/yL26ygXJnEXM7WtJHkvXkhm4WBqj.C", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230277", "030239230277@st.hub.edu.vn", "Hoàng Nguyễn Trúc Uyên", "$2a$10$mbK.SpEaYtU0N53iXGNEHu8S0OpCHKiBVcx4bFrIqIMzj7K6/dvx2", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230280", "030239230280@st.hub.edu.vn", "Phạm Thị Thục Uyên", "$2a$10$971bOs.rqvJ7Ml2wbHToceAl609pbYhSW5kcbuBZoCsuKSfaEV23G", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230283", "030239230283@st.hub.edu.vn", "Lê Thị Hồng Vân", "$2a$10$cmJnP.k1XADJufF4y0J.ReJxjiACvEDNbw0Y3R3XzRLjLhsaV4Evq", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230285", "030239230285@st.hub.edu.vn", "Nguyễn Thị Tường Vân", "$2a$10$gD2M6/zMTrnMwY8i4BbN0uky4VrWTMJHWYPPeRlWqsYPxpK5lcnTe", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230286", "030239230286@st.hub.edu.vn", "Nguyễn Thùy Vân", "$2a$10$fQUFlcExhVcsnkTSisLuWeQcuPHAprqp8ewGm/YA3lDs11/VMgcnS", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230295", "030239230295@st.hub.edu.vn", "Nguyễn Thị Thúy Vy", "$2a$10$ZNndvXjffp1lV6CyqrZhb.bFJbV8XCbIILq8VEyt/rYkCF0bnx4Da", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230303", "030239230303@st.hub.edu.vn", "Nguyễn Hoàng Yến", "$2a$10$wKg6S8bUZPSXQ8pUCYRI3egvj2/UyNLL1aWQoLjNMrVGcQlINfphe", "student", "true", "2026-05-15T16:49:05.503Z"],
    ["030239230299", "030239230299@st.hub.edu.vn", "Trần Lê Như Ý", "$2a$10$ZIoKXHUoYGhdRB4xey/xK.lHNU0idhcRdOHPRTNY.lLpFpT8nkvnm", "student", "true", "2026-05-15T16:49:05.503Z"]
  ];
  
  sheet.clear();
  sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
  sheet.getRange(2, 1, data.length, headers.length).setValues(data);
  
  SpreadsheetApp.getUi().alert("Đã import thành công " + data.length + " người dùng! Mật khẩu là MSSV.");
}
