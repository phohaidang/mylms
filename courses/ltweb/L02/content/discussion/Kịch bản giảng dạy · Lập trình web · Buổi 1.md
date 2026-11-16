# Kịch bản giảng dạy · Lập trình web · Buổi 1

Nov 13, 2026 · @Dasdragon

## Tổng quan buổi học

Buổi 1 dạy sinh viên nhìn Web như lời giải cho một vấn đề có thật ở CERN năm 1989, rồi mới xem máy chạy và tự viết trang HTML đầu tiên: 3 tiết giảng và 2 tiết nghe chuyên gia, 43 slide, 3 thử thách, 1 thử thách nhanh và 1 cuộc tranh biện. Lời giảng từng câu nằm sẵn trong deck (phím P); tài liệu này bổ sung phần deck không chứa được: thời gian, cách tổ chức hoạt động, đáp án gợi ý và cách xử lý tình huống.

**Mục tiêu.** Cuối buổi, mỗi sinh viên:

1. Kể lại được vấn đề gốc ở CERN: *thông tin có, đường nối không*, và vì sao ba phương án “nghe hợp lý” đều không dùng được.
2. Phân biệt Internet (đường sá chở dữ liệu) với Web (URL + HTTP + HTML + link chạy trên đường đó); nêu được 5 mốc 1989–1997.
3. Kể lại 4 việc xảy ra trong một giây khi bấm link một sản phẩm.
4. Tự viết và mở một trang sản phẩm bằng HTML thuần, giải thích được từng thẻ mình dùng.
5. Dùng được 3 câu hỏi của tư duy nguyên bản: vấn đề thật là gì, ràng buộc nào không bỏ được, giải pháp nhỏ nhất nào thoả hết.

| Bối cảnh lớp | Chi tiết |
| --- | --- |
| Đối tượng | Sinh viên chuyên ngành Thương mại điện tử, Trường ĐH Ngân hàng TP.HCM |
| Sĩ số | Trên 70: dùng thảo luận với bạn ngồi gần, giơ tay bình chọn, gọi ngẫu nhiên thay cho trình bày nhóm |
| Phòng | Phòng máy hoặc sinh viên mang laptop |
| Thời lượng | 3 tiết giảng (khoảng 145 phút, có 10 phút giải lao) + 2 tiết nghe TS. Phạm Hy Hiếu |

**Chuẩn bị trước giờ**

- [ ] Mở `lap-trinh-web-buoi-1-motion.html` bằng Chrome hoặc Edge; nhấn F để toàn màn hình, P để mở cửa sổ người giảng trên laptop.
- [ ] In 2 tờ cho trò chơi đóng vai (`trangchu.html`, `ao-thun.html`, nội dung ở Phần 4), bỏ vào phong bì ghi “hubshop.vn”. Không in `gio-hang.html`.
- [ ] 5–6 phiếu giấy A5 trống làm “phiếu xin”, bút dạ.
- [ ] Kiểm tra máy phòng lab có Notepad hoặc VS Code; bật hiện đuôi file nếu được.
- [ ] Viết sẵn ở góc bảng: 3 câu hỏi tư duy nguyên bản và 4 ô trống ① ② ③ ④.

Điều khiển deck: → hoặc Space sang câu tiếp, ← lùi, P cửa sổ người giảng, F toàn màn hình, E tự sửa vị trí và chữ. Đồng hồ trên slide: bấm để chạy hoặc dừng, giữ 1 giây để đặt lại. “hubshop.vn”, “Áo thun HUB” và giá 159.000đ là ví dụ minh hoạ, không phải cửa hàng thật.

## Tiến trình theo phút

Buổi học chạy khoảng 145 phút, trong đó khoảng 50 phút là sinh viên tự làm. Số trong cột Slide là số thứ tự slide; số trên băng keo đầu slide nhỏ hơn 1 (slide 8 mang băng keo “07”).

| Phút | Phần | Slide | Nội dung | Sinh viên làm gì |
| --- | --- | --- | --- | --- |
| 0–10 | 0 · Mở đầu | 1–4 | Bìa, cách học, “một giây”, câu hỏi lớn | Giơ tay bình chọn A/B/C |
| 10–24 | 1 · Bối cảnh | 5–8 | CERN, hai vấn đề, ENQUIRE | Trả lời nhanh: thông tin một khách hàng nằm ở mấy nơi |
| 24–44 | 2 · Thử thách 1 | 9–11 | Đề bài 6 ràng buộc, thảo luận 8 phút, đối chiếu 3 phương án | Nhóm 3–4 bạn ghi 3 quyết định, giơ tay theo phương án |
| 44–56 | 3 · Giải pháp | 12–14 | Điều Tim nhận ra, 5 câu trả lời, dòng thời gian | So giấy của nhóm với câu trả lời của Tim |
| 56–66 | Giải lao | 15 | Đồng hồ 10 phút | — |
| 66–101 | 4 · Vận hành | 16–23 | Internet và Web, đóng vai, máy khách – máy chủ, URL, HTTP, tĩnh/động, front-end/back-end | 3 bạn đóng vai, cả lớp chuyền phiếu; soi link sản phẩm trên điện thoại |
| 101–136 | 5 · HTML | 24–30 | Nhà in, bút đỏ → thẻ, thảo luận 3 phút, khung xương, giải phẫu thẻ, 6 thẻ, thử thách 3 | Viết `san-pham.html` trên máy (20 phút) |
| 136–145 | 6 · Chốt | 31–33 | Kể lại một giây, 3 câu hỏi, giới thiệu phần 2 | Kể lại 60 giây cho bạn bên cạnh |
| + 100 phút | 7 · Chuyên gia | 33–43 | Video 45 phút chia 7 đoạn, 5 lần dừng, tranh biện 12 phút | Phiếu nghe, giơ tay, tranh biện, bóc tách công việc, phiếu ra về |

Nếu mỗi tiết chỉ 45 phút: rút thử thách 3 còn 15 phút và lướt nhanh slide 23 (mặt tiền và nhà kho).

## Phần 0 · Mở đầu (phút 0–10, slide 1–4)

Mục đích của 10 phút đầu: tạo một câu hỏi mà sinh viên chưa trả lời được, và hẹn cuối buổi họ sẽ tự trả lời.

**Slide 1 · Bìa (1 phút).** Nói rõ hôm nay chưa code là có chủ ý: hiểu vì sao Web như vậy thì học code nhanh hơn và ít học vẹt.

**Slide 2 · Cách học (3 phút).** Giải thích “tư duy nguyên bản” bằng một ví dụ ngoài lập trình:

- Lối mòn: “Khách chê giao hàng chậm, mua thêm xe tải.”
- Nguyên bản: “Khách cần nhận nhanh, hay cần biết chính xác khi nào nhận? Ràng buộc thật là gì?” Câu trả lời có thể chỉ là một tin nhắn báo giờ giao.

Viết 3 câu hỏi của thẻ navy lên góc bảng; cả buổi sẽ quay lại chúng.

**Slide 3 · Một giây (3 phút).** Hỏi “Ai kể được một việc xảy ra trong một giây đó?”, gọi 1–2 bạn, ghi nguyên văn vào 4 ô trống trên bảng, không sửa. Câu hay gặp: “gửi qua wifi”, “Google tìm giúp”, “vào máy chủ của sàn”. Slide 31 sẽ so lại.

**Slide 4 · Câu hỏi lớn (3 phút).** Cho giơ tay A/B/C, ước lượng tỉ lệ và đọc to. Đáp án là C:

- A sai vì máy NeXT năm 1990 đã đủ mạnh để chạy cả máy chủ lẫn trình duyệt.
- B chưa đủ vì trình duyệt chỉ là phần mềm đọc tài liệu; về kỹ thuật không khó. Khó là biết cần đọc *loại* tài liệu gì, ở đâu, theo quy ước nào.
- Tim tự nói hầu hết các mảnh đã có sẵn; ông chỉ nối ý tưởng siêu văn bản vào ý tưởng TCP và DNS của Internet.

Nếu sinh viên hỏi ngay “Internet và Web khác gì?”: ghi câu hỏi lên bảng, hẹn slide 17.

## Phần 1 · Bối cảnh CERN 1989 (phút 10–24, slide 5–8)

Phần này dựng để sinh viên *cảm thấy* vấn đề trước khi ai nói ra giải pháp. Các tên máy (VAX, UNIX, Macintosh) chỉ là tên các dòng máy của những hãng khác nhau; không cần giải thích hay bắt nhớ.

**Slide 5 · CERN (3 phút).** CERN thành lập năm 1954; phần lớn nhà khoa học là khách. Câu trích trên giấy vàng là nguyên văn bản đề xuất 1989: *“When two years is a typical length of stay, information is constantly being lost.”*

**Slide 6 · Vấn đề thứ nhất (4 phút).** Thông điệp: mỗi nhóm một kiểu máy, file nhóm này máy nhóm kia không đọc được. Sau thẻ “Ngân hàng hôm nay”, hỏi 30 giây: “Chỗ bạn làm thêm hay thực tập, thông tin về một khách hàng nằm ở mấy nơi?” Câu trả lời hay gặp: phần mềm bán hàng, file Excel, nhóm Zalo, sổ tay, email.

**Slide 7 · Vấn đề thứ hai (3 phút).** Anna, Bruno, Chen, Dieter là nhân vật minh hoạ. Câu chốt cần sinh viên ghi lại: **thông tin có, đường nối không.** Đây là “vấn đề thật” trong câu hỏi 1 của tư duy nguyên bản.

**Slide 8 · ENQUIRE 1980 (4 phút).** Sơ đồ đã vẽ lại để đọc được từng lớp. Giảng theo thứ tự hiện hình:

1. Khung nét đứt = một chiếc máy, một chương trình của riêng Tim.
2. Bốn tấm thẻ = bốn “thứ”: một người, một tài liệu, một bảng số liệu, một dự án.
3. Mũi tên có nhãn đỏ = đường nối có nghĩa (viết, dùng số liệu, thuộc, làm cho). ENQUIRE thật có khoảng một chục kiểu quan hệ như vậy.
4. Máy UNIX và dấu × bên phải = không nối ra ngoài được.
5. Giấy đỏ = đường nối hai chiều, muốn nối tới đâu phải sửa được cả đầu bên kia.

Câu hỏi kiểm tra hiểu: “Bruno muốn nối tài liệu của mình vào thẻ Báo cáo hiệu chuẩn. Cậu ấy cần gì?” Đáp án: tài liệu phải nằm trong máy của Tim, và Bruno phải được sửa thẻ của Tim. Cả hai đều không thể có ở quy mô cả CERN.

Tư liệu: ENQUIRE viết bằng Pascal trên máy Norsk Data NORD-10 từ tháng 6/1980; mỗi thẻ mới phải nối từ một thẻ có sẵn; không cho nối ra cơ sở dữ liệu bên ngoài; mã nguồn đã mất ([ENQUIRE](https://en.wikipedia.org/wiki/ENQUIRE)). Chi tiết “Anna viết báo cáo…” là ví dụ minh hoạ, không phải dữ liệu thật trong ENQUIRE.

## Phần 2 · Thử thách 1: Nếu bạn là Tim (phút 24–44, slide 9–11)

Đây là phần quan trọng nhất của buổi: sinh viên phải tự thiết kế trước khi thấy đáp án, nên đừng rút ngắn 8 phút thảo luận.

**Slide 9 · Đề bài (3 phút).** Đọc to 6 ràng buộc. Nhấn ràng buộc 6 là *tài nguyên*, không phải rào cản: CERN mở kết nối Internet ra bên ngoài từ tháng 1/1989, hai tháng trước bản đề xuất.

**Slide 10 · Thảo luận (8 phút + 5 phút tổng hợp).** Cách chạy với lớp trên 70 bạn:

1. Phút 1: mỗi bạn tự nghĩ, không nói.
2. Phút 2–5: quay sang 2–3 bạn ngồi gần, bàn 5 câu gợi ý.
3. Phút 6–8: chốt 3 quyết định ra giấy, mỗi quyết định một câu.
4. Tổng hợp: kẻ 3 cột trên bảng (KHO CHUNG / ÉP CHUNG CHUẨN / ĐỂ NGUYÊN + CHỈ TỚI), cho giơ tay, ước lượng số tay mỗi cột. Gọi 2–3 nhóm có phương án khác nhau (đã chọn trước khi đi quanh lớp) đọc 3 quyết định. Chưa khen chê.

Khi nhóm bí, hỏi ngược một câu: “Trong phương án của em, ai sẽ là người phải thay đổi?”

**Slide 11 · Đối chiếu (5 phút).** Mỗi phương án vi phạm ràng buộc nào:

| Phương án | Vi phạm | Câu hỏi phản biện |
| --- | --- | --- |
| A · Một kho chung | 3, 4 (và 5 nếu có duyệt) | Ai ép mọi người nộp? Ai giữ kho khi người quản lý về nước? Ai duyệt kịp? |
| B · Ép chung một chuẩn | 1, 2, 3 | Ai gõ lại hàng nghìn tài liệu? Ai chịu bỏ máy của mình? |
| C · Gửi file cho nhau | Không giải quyết vấn đề gốc | Vẫn phải biết hỏi ai, xin file nào; đường nối vẫn nằm trong đầu người |

Tình huống hay gặp:

- Nhóm đề xuất “dùng Google Drive”: năm 1989 chưa có; và Drive là kho chung của một công ty, tức vẫn là phương án A.
- Nhóm đề xuất “AI tìm giúp”: hỏi lại AI tìm trong cái gì, đọc file bằng cách nào khi mỗi máy một kiểu? Vấn đề vẫn còn nguyên.
- Nhóm chọn đúng “để nguyên + chỉ tới”: khen, rồi hỏi tiếp “chỉ tới bằng gì?”. Chuyển sang slide 12.

## Phần 3 · Giải pháp của Tim và lịch sử WWW (phút 44–56, slide 12–14)

Web bỏ đúng hai giới hạn của ENQUIRE (chỉ một máy; nối hai chiều) và trả giá bằng link hỏng. Đó là mạch nối cần giữ khi giảng 3 slide này.

**Slide 12 · Điều Tim nhận ra (4 phút).** Bản đề xuất tháng 3/1989 viết: hệ thống mới phải nối được các hệ thống đang có *mà không cần trung tâm điều khiển*. Mike Sendall ghi lên bìa “Vague but exciting…”. Sau thẻ số 3, hỏi lớp: “Trên sàn TMĐT, khi nào bạn gặp trang 404?” (sản phẩm bị gỡ, shop đóng, link cũ trong nhóm chat). Nhấn: 404 là một quyết định thiết kế, không phải lỗi ngẫu nhiên.

**Slide 13 · Năm câu trả lời (4 phút).** Mỗi dòng có một cách hiểu đời thường gắn với TMĐT (quầy bán tại nhà, địa chỉ giao hàng, phiếu đặt hàng theo mẫu, bút đỏ biên tập, “xem thêm trang 45”). Sau slide, hỏi: “Nhóm nào có ít nhất 2 trong 5 câu giống Tim?”. Cho giơ tay, khen cụ thể một quyết định đúng của sinh viên.

**Slide 14 · Dòng thời gian (4 phút).** Slide chỉ hiện 5 mốc; bảng dưới đây đầy đủ hơn để trả lời khi sinh viên hỏi.

| Thời điểm | Sự kiện |
| --- | --- |
| 1969 | ARPANET, tiền thân của Internet, bắt đầu chạy |
| 1971 | Email và chuyển file xuất hiện trên mạng |
| 6/1980 | Tim viết ENQUIRE trong hợp đồng 6 tháng ở CERN |
| 1/1989 | CERN mở kết nối Internet ra bên ngoài |
| 3/1989 | Bản đề xuất “Information Management: A Proposal” |
| 11/1990 | Đề xuất chính thức cùng Robert Cailliau |
| Cuối 1990 | Máy chủ web và trình duyệt đầu tiên chạy trên máy NeXT; trang info.cern.ch |
| 8/1991 | Tim công bố phần mềm WWW trên các nhóm tin Internet |
| 1991 | Tài liệu “HTML Tags” mô tả 18 thẻ đầu tiên |
| 12/1991 | Máy chủ web đầu tiên ở Mỹ (SLAC) |
| Đầu 1993 | Trình duyệt Mosaic ra đời, có hình ảnh |
| 30/4/1993 | CERN cho dùng mã nguồn Web miễn phí bản quyền |
| 1994 | Tim rời CERN, lập tổ chức chuẩn W3C |
| 19/11/1997 | Việt Nam chính thức nối Internet toàn cầu |

Câu nên nhấn với sinh viên TMĐT: mốc 30/4/1993 là lý do hôm nay ai cũng mở được cửa hàng trên web mà không trả phí bản quyền cho ai. Tim nói nếu công nghệ này độc quyền trong tay ông, có lẽ nó đã không cất cánh.

Sau slide 14 là slide 15, giải lao 10 phút: bấm đồng hồ trên slide, dùng thời gian này để chuẩn bị phong bì cho trò đóng vai.

## Phần 4 · Web vận hành thế nào (phút 66–101, slide 16–23)

Trò đóng vai đi trước, các slide máy khách – máy chủ, URL, HTTP đi sau và chỉ “vẽ lại” điều sinh viên vừa tự làm bằng tay.

**Slide 16–17 · Internet và Web (5 phút).** Ẩn dụ: Internet là đường sá cộng bưu điện, chỉ lo chở gói dữ liệu tới đúng máy; Web là một loại hàng chạy trên đường đó. Email, Zalo, game online cũng chạy trên Internet nhưng không phải Web. Trả lời câu hỏi lớn đã ghi trên bảng từ slide 4.

**Slide 18 · Thử thách 2: gửi một trang web bằng giấy (10 phút).**

- Vai: 1 bạn ở bàn đầu làm trình duyệt; 1 bạn cuối lớp làm máy chủ hubshop.vn; các hàng ghế giữa là Internet. Khoảng cách xa là có chủ ý: phiếu phải đi qua nhiều tay.
- Đạo cụ: phong bì ghi “hubshop.vn” chứa 2 tờ in sẵn, vài phiếu xin trống.
- Luật quan trọng nhất: Internet chỉ chuyền theo chữ ghi bên ngoài, không mở ra đọc. Máy chủ chỉ trả lời đúng điều phiếu ghi.
- Khi trình duyệt nhận tờ HTML: nhờ bạn ấy đọc thẻ và vẽ lên bảng (h1 viết to, li gạch đầu dòng).

Tờ `ao-thun.html` (in cỡ chữ lớn):

```html
<h1>Áo thun HUB</h1>
<p>Giá: <b>159.000đ</b></p>
<ul><li>Vải cotton</li><li>Có 3 màu</li></ul>
<a href="trangchu.html">Về trang chủ</a>
```

Tờ `trangchu.html`:

```html
<h1>hubshop.vn</h1>
<p>Chào mừng bạn!</p>
<a href="ao-thun.html">Áo thun HUB</a>
```

Câu hỏi rút kinh nghiệm sau trò chơi:

| Câu hỏi | Đáp án gợi ý |
| --- | --- |
| Các bạn chuyền phiếu có cần hiểu bên trong viết gì không? | Không. Đó đúng là vai của Internet: chỉ cần địa chỉ bên ngoài |
| Vì sao máy chủ trả 404 cho gio-hang.html? | Trong phong bì không có tờ đó. 404 = không tìm thấy |
| Vì sao máy chủ hỏi “Bạn là ai?” | Mỗi phiếu là một lần mới, máy chủ không nhớ người hỏi. Sàn TMĐT cần cookie để giữ giỏ hàng |
| Nếu trình duyệt bấm “Về trang chủ” trên tờ HTML? | Một phiếu xin mới, một vòng xin – trả mới |

**Slide 19 · Máy khách – máy chủ (3 phút).** Vẽ lại trò chơi. Ẩn dụ quán ăn: khách gọi món, bếp nấu, phục vụ mang ra.

**Slide 20 · URL (5 phút, gồm thử thách nhanh 2 phút).** URL như địa chỉ giao hàng: cách gửi (https), tên cửa hàng (tên miền, tra bằng DNS), kệ nào (đường dẫn), ghi chú đơn (sau dấu ?). Sinh viên có thể gặp `:8080` hay `:443` trong link: đó là cổng, không ghi thì trình duyệt tự hiểu, không cần dạy sâu. Thử thách nhanh: chia sẻ link một sản phẩm trên sàn TMĐT, đọc to, cả lớp chỉ ra 4 phần. Link sàn thật thường rất dài; chỉ cần nhận ra tên miền, đường dẫn và phần sau dấu ?.

**Slide 21 · HTTP (4 phút).** Hai lượt: một lời xin, một lời đáp. Mã 200 có, 404 không thấy, 500 máy chủ lỗi. Cookie giải thích bằng vé gửi xe: máy chủ đưa vé, lần sau trình duyệt chìa vé ra để được nhận ra.

**Slide 22 · Web tĩnh và web động (5 phút).** Tĩnh như tờ rơi in sẵn, động như hoá đơn viết riêng. Hỏi lớp: “Trang nào ở trường mình gần với tĩnh, trang nào bắt buộc động?”. Gợi ý: trang giới thiệu khoa gần với tĩnh; cổng đăng ký học phần và xem điểm là động vì mỗi người thấy một khác.

**Slide 23 · Mặt tiền và nhà kho (3 phút).** Front-end là mặt tiền cửa hàng, back-end là kho và quầy thu ngân. Người làm TMĐT cần hiểu hai nửa nói chuyện thế nào để giao việc và kiểm tra kết quả, kể cả khi giao cho AI.

## Phần 5 · HTML và trang đầu tiên (phút 101–136, slide 24–30)

Phần này nối HTML với câu chuyện: thẻ chính là bút đỏ của biên tập viên, và “chữ thường” là lời giải cho ràng buộc 1 và 3. Bảng, biểu mẫu và video để dành buổi 2.

**Slide 24–25 · Nhà in và bút đỏ (6 phút).** Đánh dấu nói “đây là gì”, không nói “vẽ ra sao”. Khi demo, nhấn: xuống dòng trong file không có nghĩa, chỉ thẻ mới có nghĩa.

**Slide 26 · Thảo luận nhanh (3 phút + 2 phút chốt).** Cặp đôi với bạn ngồi cạnh. Gọi 3 cặp, mỗi cặp một lý do, rồi mới lật đáp án. Ngoài 4 lý do trên slide, sinh viên có thể nêu thêm:

- Máy tìm kiếm đọc được nội dung (đúng, và đây là nền của SEO sau này).
- Dễ thêm thẻ mới mà trang cũ vẫn chạy (đúng: 18 thẻ năm 1991 lên hơn 100 thẻ hôm nay).
- “Vì miễn phí” (chưa đủ: định dạng đẹp cũng có thể miễn phí; điểm mấu chốt là máy nào cũng đọc được).

**Slide 27 · Khung xương (3 phút).** Dòng `meta charset="utf-8"` là bắt buộc với trang tiếng Việt: thiếu nó, chữ có dấu dễ bị lỗi khi mở file.

**Slide 28–29 · Giải phẫu thẻ và 6 thẻ (5 phút).** Nhấn với thẻ img: trang không chứa ảnh, chỉ chứa địa chỉ của ảnh. Lại là nguyên tắc “trỏ tới, không gom vào” của Tim.

**Slide 30 · Thử thách 3: trang sản phẩm đầu tiên (20 phút).** Mẫu đầy đủ để đối chiếu khi đi kiểm tra (không chiếu trước):

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Áo thun HUB</title>
  </head>
  <body>
    <h1>Áo thun HUB</h1>
    <p>Giá: <b>159.000đ</b></p>
    <img src="ao-thun.jpg" width="200">
    <ul>
      <li>Vải cotton, mặc mát</li>
      <li>Có 3 màu: đen, trắng, xanh</li>
      <li>Size S đến XL</li>
    </ul>
    <a href="trangchu.html">Về trang chủ</a>
  </body>
</html>
```

| Tiêu chí | Đạt khi |
| --- | --- |
| Khung xương | Có DOCTYPE, html, head (có meta charset, title), body |
| Nội dung | h1 tên sản phẩm; p có b cho giá; ul có ít nhất 3 li |
| Ảnh và link | Ảnh hiện được; link a bấm được |
| Hiểu bài | Giải thích được một thẻ bất kỳ khi được hỏi, kể cả thẻ do AI viết |

Lỗi hay gặp trong phòng máy:

- File lưu thành `san-pham.html.txt`: bật hiện đuôi file, đổi tên.
- Chữ tiếng Việt lỗi dấu: thiếu `meta charset`, hoặc trình soạn thảo không lưu UTF-8.
- Ảnh không hiện: tên file ảnh sai, hoặc ảnh không nằm cùng thư mục với file HTML.
- Sửa rồi mà trang không đổi: chưa lưu file, hoặc chưa nhấn F5.

Lớp đông: cho phép hỏi bạn bên cạnh trước khi giơ tay. Đáp án thử thách “thử phá”: xoá `</b>` thì phần chữ phía sau bị in đậm lan ra, nhưng trang vẫn hiện. Trình duyệt “dễ tính”, đúng lý do 3 ở slide 26.

## Phần 6 · Chốt lại và cầu nối sang phần chuyên gia (phút 136–145, slide 31–33)

Sinh viên ra về với hai thứ: kể lại được một giây sau cú bấm, và ba câu hỏi để mang vào 2 tiết nghe chuyên gia.

**Slide 31 · Kể lại một giây (3 phút).** Đáp án đầy đủ cho 4 ô trống đã ghi ở đầu buổi:

&#91;embedded content: một giây sau cú bấm · 4 việc, lặp lại\]

Bước ① đến ③ đi qua Internet; bước ④ xảy ra ngay trên máy bạn. Khung tô màu là thứ sinh viên thấy; ba bước trước là phần máy làm mà buổi học vừa mở ra.

Cho 60 giây kể lại với bạn bên cạnh, rồi gọi một bạn kể to. So với câu trả lời ghi ở góc bảng lúc đầu: đây là khoảnh khắc sinh viên thấy mình đã tiến bộ.

**Slide 32 · Mang về (2 phút).** Đọc lại 3 câu hỏi của tư duy nguyên bản trên bảng, gắn mỗi câu với một đoạn của buổi: vấn đề thật (slide 7), ràng buộc (slide 9), giải pháp nhỏ nhất (slide 12–13).

**Slide 33 · Phần 2, nghe TS. Phạm Hy Hiếu (2 phút).** Phát phiếu nghe 4 câu, nghe xong nộp:

1. Diễn giả khuyên tránh hai suy nghĩ nào về AI? Bạn đang nghiêng về phía nào?
2. “Đã có vibe code, còn cần học không?” Ông trả lời bằng cách nghĩ nào?
3. Ông lập luận ra sao khi nói AI không lấy mất việc? Bạn đồng ý đến đâu?
4. Ba “vốn nghề” ông chọn là gì? Bạn đầu tư vào cái nào trước?

Kịch bản chi tiết cho 2 tiết này nằm ở Phần 7 ngay dưới.

**Bài về nhà (giao ở slide 43, cuối 2 tiết chuyên gia):**

- Thêm trang thứ hai và nối hai trang bằng link.
- Viết 3 dòng: chỗ bạn học hay làm thêm có chỗ nào “thông tin có, đường nối không”? Bạn sẽ “trỏ tới” thay vì “gom về” thế nào?
- Buổi sau: CSS, cách dặn “thợ in” về hình thức.

## Phần 7 · 2 tiết nghe TS. Phạm Hy Hiếu (100 phút, slide 33–43)

Trong 100 phút, sinh viên xem khoảng 45 phút của video 72 phút (7 đoạn). Video được dừng 5 lần, mỗi lần dừng có một hoạt động nối với buổi học. Video: [ĐGHCN 43 · 3 năng lực cốt lõi để làm chủ công nghệ Trí tuệ nhân tạo](https://www.youtube.com/watch?v=ZlEceN_TqsQ), podcast “Đơn giản hoá chuyện ngành”. Trong video, diễn giả được giới thiệu là giám đốc khối chuyển đổi trí tuệ nhân tạo tại Techcombank.

Mục tiêu riêng của 2 tiết: sinh viên nhìn AI như đồng nghiệp chứ không phải mối đe doạ; tự trả lời “có cần học khi đã có vibe code?” bằng tư duy nguyên bản; và phân biệt được quan điểm của một chuyên gia với dữ kiện đã kiểm chứng.

**Kế hoạch 100 phút**

| Phút | Mốc video | Slide | Hoạt động |
| --- | --- | --- | --- |
| 0–5 | — | 33 | Giới thiệu diễn giả, phát phiếu nghe 4 câu |
| 5–13 | 1:08–9:05 | — | Xem: chiếc laptop, STEM, vai trò của khoa học |
| 13–18 | — | 34 | Dừng 1: laptop là máy khách, cloud là máy chủ |
| 18–24 | 19:06–25:25 | — | Xem: ba trụ cột, chip – kernel – trình biên dịch, AI là đồng nghiệp |
| 24–29 | — | 35 | Dừng 2: giơ tay “hai thái cực” |
| 29–40 | 30:43–41:10 | — | Xem: gốc và ngọn, vibe coding, đục lỗ thẻ, first principles |
| 40–56 | — | 36–38 | Dừng 3: từ đục lỗ đến tiếng người, tranh biện 12 phút, câu trả lời của diễn giả |
| 56–62 | 41:12–47:15 | — | Xem: prompt, chọn công cụ, định nghĩa thành công |
| 62–67 | — | 39 | Dừng 4: viết 3 tiêu chí đo được cho trang sản phẩm |
| 67–71 | 47:17–51:05 | — | Xem: AI và việc làm |
| 71–80 | — | 40 | Dừng 5: bóc tách công việc vận hành gian hàng |
| 80–88 | 54:28–1:01:50 | — | Xem: chọn việc để học, ai cũng từ số 0, cú sốc phỏng vấn, áp lực nghề |
| 88–91 | 1:09:21–1:12:30 | — | Xem: ba vốn nghề |
| 91–97 | — | 41–42 | Phiếu ra về, nối hai phần |
| 97–100 | — | 43 | Bài về nhà, hỏi đáp, thu phiếu |

Các đoạn bỏ qua, có thể giao xem ở nhà: 9:06–19:05 (vì sao chọn ngành, hành trình Stanford → CMU → Google → xAI → OpenAI → về nước, nghiên cứu hay thực chiến); 25:25–30:43 (lĩnh vực nào thiếu người, chọn theo sở thích – sở trường – sở đoản); 51:08–54:27 (học AI cần toán gì); 1:01:50–1:09:20 (AI ở Việt Nam, làm chủ công nghệ là làm chủ chuỗi cung ứng, nếu được quay lại tuổi 18). Mốc thời gian lấy từ phụ đề tự động, có thể lệch vài giây.

**Câu hỏi và đáp án gợi ý tại 5 điểm dừng**

| Điểm dừng | Câu hỏi | Đáp án gợi ý (theo video) |
| --- | --- | --- |
| 1 · slide 34 | Laptop của kỹ sư AI đóng vai gì trong mô hình buổi trước? | Máy khách: chỉ để viết code; code chạy trên siêu máy tính trên cloud, tức máy chủ ở xa (3:40–5:00) |
| 1 · slide 34 | Máy tính chỉ biết cộng trừ nhân chia. Vậy AI “thông minh” từ đâu? | Theo diễn giả: ghép đúng rất nhiều phép tính thì mô phỏng được quá trình suy nghĩ; và bỏ bất kỳ chữ nào trong STEM cũng không có AI (5:04–7:30) |
| 2 · slide 35 | Hai suy nghĩ nào nên tránh? | “AI sẽ lấy mất việc của mình” và “AI dở lắm, chưa làm được gì”; thay bằng coi AI là bạn, đồng nghiệp (23:50–24:30) |
| 2 · slide 35 | AI chưa thắng người ở việc gì? | Diễn giả không dám chỉ ra việc nào chắc chắn; người giỏi nhất mỗi ngành có lẽ vẫn hơn, người trung bình thì có việc thua AI (24:29–25:20) |
| 3 · slide 36 | Vì sao ông chưa muốn mở lớp chuyên AI ở phổ thông? | AI đổi quá nhanh; thiếu gốc toán, lý, hoá, sinh, tin thì chạy theo ngọn, khổ khi AI rẽ hướng (31:07–33:00). Nối buổi học: nguyên tắc HTML giữ nguyên 35 năm chính là “gốc” |
| 3 · slide 37–38 | Đã có vibe code, còn cần học HTML? | Tuỳ mục đích: muốn vừa làm vừa học thì học bài bản; chỉ cần sản phẩm nhanh thì vibe code (39:11–41:10). Hôm nay vẫn cần hiểu bản chất để sửa lỗi vì AI chưa đủ đáng tin (36:00–37:30) |
| 4 · slide 39 | Viết 3 tiêu chí đo được cho trang sản phẩm | Tiếng Việt hiện đúng; ảnh hiện; khách thấy giá trong 3 giây; link về trang chủ bấm được; đọc được trên điện thoại. “Trang đẹp” chưa phải tiêu chí vì không đo được (46:00–47:15) |
| 5 · slide 40 | Việc nào trong vận hành gian hàng giao AI, việc nào người giữ? | AI: nháp mô tả, trả lời câu hỏi lặp lại, tổng hợp số liệu. Người: chọn sản phẩm, khiếu nại khó, quyết định giá, chịu trách nhiệm. Cả hai: AI nháp, người duyệt. Cách tách bước lấy từ lời khuyên của diễn giả (43:15–44:10) |

**Tranh biện “có cần học HTML?” (slide 37, 12 phút).** Chia phe theo chỗ ngồi, không cho tự chọn, để sinh viên tập bảo vệ cả quan điểm mình không thích. Lý lẽ gợi ý khi một phe bí:

- Phe cần học: sửa lỗi khi AI viết sai; kiểm tra AI làm đúng chưa; giao việc cho lập trình viên chính xác hơn; trả lời được khi đi phỏng vấn.
- Phe không cần: nếu mục đích chỉ là có trang bán hàng nhanh; công cụ kéo thả và AI đã đủ; thời gian dành cho kinh doanh có giá trị hơn; như đục lỗ thẻ, kỹ năng có thể lỗi thời.
- Chốt: phe nào gắn lý do với một mục đích cụ thể thì phe đó đang dùng tư duy nguyên bản. Mục đích của môn học là học, nên thử thách 3 cho dùng AI nhưng phải giải thích được từng thẻ.

**Lưu ý khi dẫn**

- **Quan điểm khác dữ kiện.** Các câu sau là phát biểu hoặc dự đoán của diễn giả, chưa kiểm chứng; khi nhắc lại nên nói “theo diễn giả”: lương khoảng 600.000 USD/năm cho kỹ sư AI trung cấp ở Anthropic; vốn đầu tư vào phần cứng AI “chục nghìn tỷ USD”; AI chỉ dựa trên khoảng 20 thuật toán; 6 tháng nữa viết prompt không còn quan trọng; AI rồi sẽ làm được mọi việc con người làm.
- **“AI không lấy việc” là một quan điểm**, phù hợp tinh thần buổi học nhưng còn tranh luận. Slide 40 để sinh viên tìm một chỗ đồng ý và một chỗ còn nghi ngờ. Một hướng phản biện để gợi mở: việc lặp lại dành cho người mới vào nghề thường là việc AI làm trước, nên sinh viên cần lên tay chuyên môn nhanh hơn. Điều này khớp với lời khuyên “hãy là người có ích”.
- **Phụ đề tự động có lỗi**: ghi sai tên thành “Phạm Huy Hiếu” và “vai coding”. Ở phút 29:29, diễn giả nhắc một công trình nổi tiếng của một nhà khoa học người Việt ở Đại học Princeton, nhưng phụ đề không ghi rõ tên công trình; nếu sinh viên hỏi, nên kiểm tra lại trước khi trả lời.
- **Câu nối hai phần (slide 42)**: Tim Berners-Lee bắt đầu từ vấn đề thật và ràng buộc; diễn giả bắt đầu từ mục đích và định nghĩa thành công. Hai cách diễn đạt của cùng một lối nghĩ.

## Phụ lục

**Câu hỏi kiểm tra nhanh** (dùng đầu buổi 2 hoặc làm phiếu ra về)

| Câu hỏi | Đáp án gợi ý |
| --- | --- |
| Vấn đề gốc ở CERN năm 1989 là gì? | Thông tin có, đường nối không; đường nối chỉ nằm trong trí nhớ người, mà người thì đi |
| Vì sao “một kho chung” không dùng được? | Không ai đủ quyền ép nộp; kho phụ thuộc người giữ; không duyệt kịp |
| Internet và Web khác nhau thế nào? | Internet chở dữ liệu giữa các máy; Web là một dịch vụ chạy trên đó, gồm URL, HTTP, HTML và link |
| Vì sao link trên Web là một chiều? | Để ai cũng nối tới trang người khác mà không phải xin phép hay sửa trang đó; cái giá là lỗi 404 |
| Trong `https://hubshop.vn/ao-thun?mau=den`, phần nào là tên miền, phần nào là dữ liệu gửi kèm? | `hubshop.vn` là tên miền; `mau=den` là dữ liệu gửi kèm |
| Mã 404 và 500 khác gì nhau? | 404: máy chủ không tìm thấy trang; 500: máy chủ bị lỗi khi xử lý |
| Vì sao sàn TMĐT cần cookie? | HTTP không nhớ người hỏi; cookie giúp máy chủ nhận ra bạn để giữ giỏ hàng, đăng nhập |
| Web động cần thêm gì so với web tĩnh? | Chương trình chạy trên máy chủ và kho dữ liệu, để viết trang HTML riêng cho từng lần hỏi |

**Xử lý tình huống**

| Tình huống | Cách xử lý |
| --- | --- |
| Lớp im lặng khi thảo luận | Đọc to câu gợi ý ① và cho 30 giây; gọi theo số thứ tự bàn thay vì xin xung phong |
| Không ai xung phong đóng vai | Chọn trình duyệt và máy chủ theo số bàn; bạn khác chỉ cần chuyền phiếu |
| Sinh viên hỏi “AI làm hết rồi, học HTML làm gì?” | Ghi lên bảng, hẹn mang câu hỏi vào phần chuyên gia; trả lời ngắn: phải hiểu thì mới giao việc và kiểm tra được AI |
| Thiếu thời gian | Bỏ thử thách nhanh soi link (slide 20), lướt slide 23; không cắt thử thách 1 |
| Máy phòng lab lỗi | Làm thử thách 3 theo cặp, chung một máy |

**Thuật ngữ nói đơn giản**

| Thuật ngữ | Nói đơn giản | Ví dụ TMĐT |
| --- | --- | --- |
| Máy khách (client) | Trình duyệt trên máy hoặc điện thoại của bạn | Chrome trên điện thoại người mua |
| Máy chủ (server) | Máy luôn bật, giữ tài liệu, ai hỏi thì trả | Máy chủ của một sàn |
| URL | Địa chỉ duy nhất của một trang | Link sản phẩm gửi qua tin nhắn |
| DNS | Danh bạ đổi tên miền ra địa chỉ số | Tên sàn → địa chỉ máy chủ |
| HTTP | Mẫu hỏi – đáp giữa trình duyệt và máy chủ | Mỗi lần bấm xem sản phẩm |
| HTML | Chữ thường cộng thẻ đánh dấu | Trang chi tiết sản phẩm |
| Cookie | Vé gửi xe máy chủ đưa cho trình duyệt | Giữ giỏ hàng, giữ đăng nhập |
| Front-end / back-end | Mặt tiền cửa hàng / nhà kho và quầy thu ngân | Trang sản phẩm / tính giá, trừ tồn kho |

**Đã đổi gì so với deck cũ**

| Chỗ đổi | Vì sao |
| --- | --- |
| ENQUIRE vẽ lại: 4 thẻ cụ thể, mũi tên có nhãn, khung “một máy”, máy bên ngoài bị chặn | Sơ đồ cũ chỉ có nút “Tiêu đề / loại · liên kết” trừu tượng, không thấy được giới hạn |
| Vấn đề thứ nhất: bỏ tên định dạng (WordPerfect, TeX, SGML), thêm thẻ “Ngân hàng hôm nay” | Giảm thuật ngữ, nối với ngành của sinh viên |
| Thêm slide “Một giây” (đầu) và “Kể lại một giây” (cuối) | Tạo câu hỏi mở và đóng vòng cho cả buổi |
| Thêm slide “Internet là đường sá, Web là một loại hàng” | Trả lời trực tiếp câu hỏi lớn |
| Thêm thử thách đóng vai và thử thách soi link | Sinh viên tự trải nghiệm HTTP trước khi học tên gọi |
| Bảng “Năm câu trả lời” có cột “hiểu kiểu đời thường” | Thay sơ đồ 4 mảnh ghép khó đọc |
| Gộp web tĩnh và web động vào một slide hai làn | So sánh trực tiếp, tiết kiệm thời gian |
| URL bỏ cổng (port), dùng ẩn dụ địa chỉ giao hàng | Giảm thuật ngữ |
| Phần HTML rút còn 6 thẻ; bảng, form, media để buổi 2; thêm meta charset | Vừa 3 tiết; tránh lỗi tiếng Việt khi thực hành |
| Thêm slide giải lao và slide cầu nối sang phần chuyên gia | Khớp lịch 3 + 2 tiết |
| Dùng cửa hàng minh hoạ hubshop.vn thay cho tên sàn thật | Tránh mô tả sai hệ thống của một công ty thật |

**Nguồn tư liệu** (đã mở và đối chiếu ngày 13/11/2026)

- [A short history of the Web](https://home.cern/science/computing/the-birth-of-the-web/short-history-web/) — CERN: các mốc 1989–1994.
- [Information Management: A Proposal](https://www.w3.org/History/1989/Proposal.html) — bản đề xuất 1989: “hai năm”, “không cần trung tâm”, “CERN là mô hình thu nhỏ của thế giới”.
- [First outline of the World Wide Web](https://timeline-upgrade.web.cern.ch/node/503) — CERN: lời ghi “Vague but exciting…” của Mike Sendall.
- [ENQUIRE](https://en.wikipedia.org/wiki/ENQUIRE) — cách ENQUIRE lưu thẻ, nối hai chiều, vì sao thất lạc.
- [Tim Berners-Lee (trang cho học sinh)](https://www.w3.org/People/Berners-Lee/Kids.html) — câu “đăng nhập từng máy”, “hỏi nhau lúc uống cà phê”, “các mảnh đã có sẵn”.
- [Tim Berners-Lee FAQ](https://www.w3.org/People/Berners-Lee/FAQ.html?i=c3a) — vì sao link một chiều, vì sao Web phải mở.
- [Internet prehistory at CERN](https://home.cern/internet-prehistory-cern/) — CERN mở kết nối Internet ra ngoài tháng 1/1989.
- [HTML Tags, 1991](https://wdm.olw.cz/web-design-history/tim-berners-lee-published-a-document-called-html-tags-1991) — 18 thẻ đầu tiên.
- [VNPT và hành trình 25 năm kết nối Internet toàn cầu](https://nhandan.vn/vnpt-va-hanh-trinh-25-nam-ket-noi-internet-toan-cau-post725715.html) — Nhân Dân: mốc 19/11/1997.

* [ĐGHCN 43 · 3 năng lực cốt lõi để làm chủ công nghệ Trí tuệ nhân tạo](https://www.youtube.com/watch?v=ZlEceN_TqsQ) — video phần 2; mốc thời gian và ý trích lấy từ bản phụ đề giảng viên cung cấp.
