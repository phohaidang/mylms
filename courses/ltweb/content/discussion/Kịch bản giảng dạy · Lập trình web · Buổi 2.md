# Kịch bản giảng dạy · Lập trình web · Buổi 2

Nov 14, 2026 · @Dasdragon

## Tổng quan buổi học

Buổi 2 nối trực tiếp từ lời hẹn cuối Buổi 1 (*"CSS: dặn thợ in về hình thức"*) và mở ra bước nhảy quan trọng nhất từ giao diện tĩnh sang hệ thống thực chiến: biến chiếc laptop Windows của sinh viên thành một máy chủ web chạy PHP, dùng **Ngrok** mở đường hầm đưa cửa hàng `hubshop` ra Internet để bạn bè trong lớp đặt thử trên điện thoại, và dùng AI (**Vibe Code**) nâng cấp cửa hàng theo một kiến trúc ngăn nắp, có kiểm định.

Buổi học áp dụng công thức **30% Đề cương (CSS + XAMPP, Apache, PHP cấu hình) + 70% Tình huống Thực chiến (Bắt bệnh Server, Self-hosting với Ngrok, Vibe Code kiến trúc chuẩn, và đặt bài toán VPS Ubuntu/Coolify cho đồ án nhóm)**. Lời giảng từng câu nằm sẵn trong deck (phím P); tài liệu này bổ sung phần deck không chứa được: phân bổ thời gian, cách điều phối lớp đông, đáp án gợi ý và cách xử lý sự cố phòng máy.

**Mục tiêu.** Cuối buổi, mỗi sinh viên:

1. Kể được 3 nguyên tắc của Đề cương: phân biệt 3 cách đặt CSS (Inline, Internal, External) và quy tắc `.class` / `#id` / mô hình hộp (`padding` và `margin`); giải thích vì sao nhấp đúp `.php` không chạy được mà phải đi qua Apache trong `htdocs`.
2. Chỉ ra đúng nơi cần sửa khi gặp 4 sự cố kinh điển: đổi cổng trong `httpd.conf` khi đụng cổng 80, đổi dung lượng tải lên trong `php.ini`, bật `display_errors = On` khi code và tắt khi lên mạng thật.
3. Giải thích được bằng tư duy nguyên bản vì sao `localhost` và IP nội bộ không bán hàng qua mạng 4G được (rào cản NAT và tường lửa), và cách đường hầm **Ngrok** giải quyết rào cản đó.
4. Dùng AI (Vibe Code) tạo và chạy được trang cửa hàng `.php` có tách file `style.css` riêng, phát sóng qua Ngrok cho bạn bên cạnh truy cập trên điện thoại, và đọc hiểu được từng phần code do AI sinh ra.
5. Hiểu giới hạn "gấp laptop là sập tiệm" của Ngrok để sẵn sàng bước vào Đồ án Nhóm nâng cao (VPS Ubuntu + Tailscale + Coolify).

| Bối cảnh lớp | Chi tiết |
| --- | --- |
| Đối tượng | Sinh viên chuyên ngành Thương mại điện tử, Trường ĐH Ngân hàng TP.HCM |
| Sĩ số | Trên 70: thảo luận cặp đôi/nhóm bàn 3-4 bạn, giơ tay bình chọn, kiểm tra chéo qua điện thoại |
| Phòng | Phòng máy Windows hoặc sinh viên mang laptop cá nhân (khuyến khích dùng 4G trên điện thoại để test Ngrok) |
| Thời lượng | 5 tiết (khoảng 225 phút, chia làm 2 nửa: Phần 1 gồm 3 tiết Đề cương + Hạ tầng XAMPP/Ngrok; Phần 2 gồm 2 tiết Vibe Code Kiến trúc + Bắt bệnh + Đồ án Nhóm) |

**Chuẩn bị trước giờ**

- [ ] Mở `lap-trinh-web-buoi-2-motion.html` bằng Chrome hoặc Edge; nhấn F toàn màn hình, P để mở cửa sổ người giảng.
- [ ] Kiểm tra máy giảng viên đã cài sẵn **XAMPP** (hoặc WAMP) và file `ngrok.exe` (đã đăng nhập authtoken miễn phí tại dashboard.ngrok.com).
- [ ] Chuẩn bị sẵn thư mục mẫu `C:\xampp\htdocs\hubshop` có `index.php` và `style.css` để demo trong 30 giây khi cần.
- [ ] Viết sẵn lên góc bảng: **Thoả thuận 30 / 70** và **3 câu hỏi Tư duy nguyên bản** (Vấn đề thật - Ràng buộc - Giải pháp nhỏ nhất).

Điều khiển deck: → hoặc Space sang câu tiếp, ← lùi, P cửa sổ người giảng, F toàn màn hình, E tự sửa vị trí và chữ, C bật/tắt phụ đề. Đồng hồ trên slide: bấm để chạy hoặc dừng, giữ 1 giây để đặt lại.

## Tiến trình theo phút

Buổi học thiết kế cho 5 tiết (225 phút, có 2 lần giải lao ngắn), trong đó hơn 110 phút là sinh viên thảo luận tình huống, bắt bệnh và thực hành trực tiếp trên máy.

| Phút | Phần | Slide | Nội dung | Sinh viên làm gì |
| --- | --- | --- | --- | --- |
| 0–15 | 0 · Thoả thuận | 1–4 | Bìa, Thoả thuận 30/70, Mở vòng "Nhấp đúp file `.php`", Lộ trình 3 tầng | Nghe và xác nhận thoả thuận học tập; đoán vì sao file `.php` bị hiện mã nguồn |
| 15–50 | 1 · CSS (Đề cương) | 5–10 | Thợ in và CSS, Giải phẫu CSS (`.class` và `#id`), 3 cách đặt CSS, Mô hình hộp, Thử thách 1 (Bắt lỗi CSS của AI) | Thảo luận cặp đôi 5 phút bắt 3 lỗi giao diện và kiến trúc CSS |
| 50–90 | 2 · Web Server (Đề cương) | 11–17 | Vì sao trình duyệt mù PHP, Lịch sử & Chọn Server, WAMP/XAMPP và `htdocs`, `httpd.conf` vs `php.ini`, Thử thách 2 (Bắt bệnh phòng lab) | Nhóm 3-4 bạn thảo luận 10 phút giải 4 ca cấp cứu XAMPP trên Windows |
| 90–100 | Giải lao | 18 | Đồng hồ 10 phút | Chuẩn bị XAMPP và tải sẵn Ngrok nếu dùng laptop cá nhân |
| 100–145 | 3 · Self-hosting (Ngrok) | 19–24 | Cú sốc `localhost`, Ràng buộc NAT & Tường lửa, Giải pháp đường hầm Ngrok, Quan sát HTTP sống, Thử thách 3 (Phát sóng shop ra 4G) | Chạy `index.php` trên XAMPP, bật Ngrok, gửi link cho bạn khác bấm bằng 4G (15 phút) |
| 145–190 | 4 · Vibe Code Kiến trúc | 25–29 | Căn bệnh "Spaghetti 1 file", Khung kiến trúc 3 ngăn, Công thức Prompt cho kỹ sư, Thử thách 4 (Vibe Code & Kiểm định chéo) | Dùng AI tạo trang cửa hàng `hubshop` theo kiến trúc chuẩn, kiểm định chéo (25 phút) |
| 190–225 | 5 · Mở rộng & Chốt | 30–34 | Câu hỏi "11h đêm gấp máy", Bàn giao Đồ án Nhóm (VPS Ubuntu + Tailscale + Coolify), Tổng kết 1 giây có PHP, Bài về nhà & LMS | Lập nhóm đồ án, đối chiếu 3 câu hỏi nguyên bản, ghi nhận bài test trên LMS |

Nếu lớp chỉ học 3 tiết trên lớp và 2 tiết tự thực hành: chạy từ Slide 1 đến Slide 24 trong 3 tiết đầu (xong phần Đề cương + chạy thử XAMPP/Ngrok), giao Phần 4 và Phần 5 làm hoạt động thực hành có hướng dẫn trong 2 tiết sau.

---

## Phần 0 · Mở đầu & Thoả thuận học tập (phút 0–15, slide 1–4)

Mục đích: thiết lập rõ "luật chơi" của môn học ngay từ đầu để sinh viên yên tâm chuyện điểm số, thi cử và hào hứng bước vào phần thực chiến.

**Slide 1 · Bìa (2 phút).** Nhắc lại câu chốt Buổi 1: HTML chỉ là chữ thường đánh dấu ý nghĩa. Hôm nay ta làm hai việc lớn: mặc áo đẹp cho trang web (CSS), và dựng một máy chủ thật ngay trên chiếc laptop Windows của các bạn để người ngoài truy cập vào được.

**Slide 2 · Thoả thuận 30 / 70 (5 phút).** Giảng thật rõ và chậm rãi 2 cam kết trên slide:

- **100% kiến thức thi cuối kỳ** nằm trọn trong Ebook trên hệ thống LMS và bộ câu hỏi trắc nghiệm theo từng buổi. Sinh viên đọc Ebook và làm đủ bài test trên LMS là hoàn toàn yên tâm đi thi không sót bất kỳ câu hỏi nào.
- **Thời gian trên lớp chia 30 / 70:** 30% đầu buổi thầy cô chốt nhanh các nguyên lý cốt lõi nhất của đề cương; 70% thời gian còn lại lớp ta giải quyết các tình huống thực tế của kỹ sư thời AI: tự dựng máy chủ (Self-hosting) và chỉ huy AI viết code có kiến trúc dễ bảo trì (Vibe Coding).

Hỏi cả lớp: *"Ai đồng ý với thoả thuận này thì giơ tay?"* Tạo sự đồng thuận tập thể trước khi đi tiếp.

**Slide 3 · Cú sốc đầu tiên: Nhấp đúp vào `san-pham.php` (4 phút).** Nối từ bài về nhà Buổi 1:

- Buổi 1 lưu file `san-pham.html`, nhấp đúp chuột là Chrome mở ra trang áo thun rất đẹp.
- Hôm nay muốn trang web tự tính giá khuyến mãi 10%, ta đổi tên thành `san-pham.php` và viết thêm 1 dòng lệnh PHP. Nhưng khi nhấp đúp chuột vào file `.php`, trình duyệt lại chỉ hiện nguyên văn đoạn code hoặc tự tải file về máy!
- Đặt câu hỏi mở (ghi lên góc bảng): *"Vì sao trình duyệt hiểu `.html` ngay lập tức nhưng lại bó tay trước `.php`?"*

**Slide 4 · Lộ trình 3 chặng của buổi học (4 phút).** Giới thiệu 3 chặng:
1. **Trang điểm (CSS):** Dặn "thợ in" trình duyệt vẽ giao diện đẹp và ngăn nắp.
2. **Dựng bếp (XAMPP & Ngrok):** Biến laptop Windows thành máy chủ PHP và nối đường ống ra Internet.
3. **Chỉ huy AI (Vibe Code có kiến trúc):** Dùng AI dựng cửa hàng có cấu trúc dễ sửa, dễ bảo trì.

---

## Phần 1 · 30% Đề cương (Nửa 1): CSS - Dặn thợ in về hình thức (phút 15–50, slide 5–10)

Phần này phủ toàn bộ nội dung mục 1.2.6 trong Ebook Chương 1 (cú pháp CSS, Selector theo thẻ / `.class` / `#id`, 3 cách đặt CSS: Inline, Internal, External, thư viện Bootstrap/Tailwind, và mô hình hộp Box Model).

**Slide 5 · Thợ in và tờ hướng dẫn trang trí (4 phút).** Nối ẩn dụ nhà in từ Buổi 1:

- HTML là bản thảo có đánh dấu bút đỏ: chỉ nói *"đây là tiêu đề `h1`", "đây là đoạn văn `p`"*.
- Nếu không dặn gì thêm, trình duyệt dùng kiểu chữ mặc định trông như văn bản thập niên 1990.
- **CSS (Cascading Style Sheets)** chính là "tờ hướng dẫn trang trí" kẹp kèm bản thảo: dặn thợ in chỗ nào tô màu xanh `#1B2558`, chữ to bao nhiêu, bo góc mấy pixel.
- Câu hỏi tư duy nguyên bản: *"Vì sao không nhét luôn màu sắc, cỡ chữ vào chung thẻ HTML mà phải tách riêng ra CSS?"* (Đáp án: để khi muốn đổi màu thương hiệu của cả sàn TMĐT từ cam sang xanh, chỉ cần sửa 1 tờ hướng dẫn thay vì mở 1.000 trang sản phẩm ra sửa từng dòng).

**Slide 6 · Giải phẫu một lệnh CSS và 3 cách gọi tên (6 phút).** Chỉ vào cấu trúc `selector { thuộc-tính: giá-trị; }`. Giảng kỹ 3 loại Selector rất hay gặp trong đề thi và thực tế:

| Loại Selector | Ký hiệu trong CSS | Trong HTML | Khi nào dùng trong TMĐT? |
| --- | --- | --- | --- |
| **Theo tên thẻ** | `h1 { ... }` | `<h1>...</h1>` | Áp cho mọi thẻ cùng loại trên toàn trang |
| **Class selector** | `.nut-mua { ... }` (dấu chấm) | `class="nut-mua"` | Dùng **nhiều lần** cho các thành phần giống nhau (20 thẻ sản phẩm, các nút mua hàng) |
| **ID selector** | `#gio-hang-chinh { ... }` (dấu thăng) | `id="gio-hang-chinh"` | Dùng **duy nhất 1 lần** trên trang cho phần tử đặc biệt (khung đầu trang, giỏ hàng tổng) |

Mẹo nhớ nhanh cho sinh viên đi thi: **Class = Chấm (`.`) dùng Chung nhiều chỗ; ID = Thăng (`#`) như căn cước công dân, chỉ 1 người có.**

**Slide 7 · Ba nơi đặt CSS: Inline, Internal, External (6 phút).** So sánh 3 cách tích hợp CSS từ giáo trình:

1. **Inline CSS:** Viết thẳng `style="color:red;"` vào từng thẻ HTML. Nhanh cho 1 chỗ nhưng viết 50 sản phẩm thì thành thảm hoạ bảo trì.
2. **Internal CSS:** Đặt trong cặp thẻ `<style>...</style>` ở phần `<head>`. Chỉ có tác dụng trong đúng 1 file HTML đó.
3. **External CSS:** Tách hẳn ra một file `.css` riêng (ví dụ `style.css`), rồi nối vào trang bằng thẻ `<link rel="stylesheet" href="style.css">` trong `<head>`.
- **Góc nhìn Kiến trúc & Thư viện:** Nhấn mạnh các thư viện nổi tiếng như **Bootstrap** hay **Tailwind CSS** bản chất chính là một file External CSS khổng lồ người ta viết sẵn các `.class` (như `.btn`, `.btn-primary`), mình chỉ việc `<link>` vào rồi gọi tên class ra dùng.

**Slide 8 · Mô hình chiếc hộp (Box Model): `padding` khác gì `margin`? (6 phút).** Đây là câu hỏi kinh điển cả khi đi thi lẫn khi sửa giao diện bị dính chữ:

- Mọi thẻ HTML trên màn hình đều là một chiếc hộp chữ nhật.
- Có 3 lớp tính từ chữ ra ngoài:
  1. **Padding (Đệm trong):** Khoảng trống từ chữ đến đường viền hộp (`border`). Giống lớp xốp chống sốc **bên trong** thùng hàng Shopee.
  2. **Border (Viền hộp):** Đường khung bao quanh hộp (`border: 1px solid #000`, bo góc `border-radius`).
  3. **Margin (Lề ngoài):** Khoảng cách từ vỏ hộp này đẩy hộp bên cạnh ra xa. Giống khoảng cách giữa hai thùng hàng xếp trên kệ.

**Slide 9–10 · Thử thách 1: Bắt lỗi CSS do AI viết (8 phút thảo luận + 5 phút chữa).**

- **Tình huống trên slide:** Một bạn sinh viên nhờ AI tạo trang danh sách 100 sản phẩm cho `hubshop.vn`. AI trả về một file `san-pham.html` chạy được, nhưng có **3 vấn đề nghiêm trọng**:
  1. Ở mỗi thẻ sản phẩm đều lặp lại nguyên cụm `<div style="border:1px solid black; padding:0px; margin:0px;">` suốt 100 lần.
  2. Chữ tên áo và giá tiền dính sát rạt vào đường viền đen rất xấu, và 2 khung sản phẩm trên dưới dính liền vào nhau không có khe hở.
  3. Cả 100 sản phẩm đều được AI đặt trùng thuộc tính `id="san-pham"`.
- **Yêu cầu (Cặp đôi 5 phút):** Chỉ ra 3 lỗi trên vi phạm nguyên tắc nào và viết lại cách sửa đúng.
- **Đáp án chốt ở Slide 10:**
  1. **Lỗi bảo trì:** Dùng Inline CSS lặp 100 lần -> Phải tách ra file `style.css` (External CSS) và nối bằng thẻ `<link>`.
  2. **Lỗi dùng sai `#id`:** `id` chỉ được dùng 1 lần duy nhất -> Phải đổi sang `class="the-san-pham"` (trong CSS viết `.the-san-pham`).
  3. **Lỗi Box Model:** Chữ dính sát viền là do thiếu **`padding`** (sửa thành `padding: 16px;`); hai hộp dính nhau là do thiếu **`margin`** (sửa thành `margin-bottom: 20px;`).

---

## Phần 2 · 30% Đề cương (Nửa 2): Web Server, XAMPP và Cấu hình (phút 50–90, slide 11–17)

Phần này giải quyết câu hỏi mở ở đầu buổi và bao trọn toàn bộ nội dung Chương 2 trong Ebook (Lịch sử Web Server, chọn Web Server theo ngôn ngữ, Apache, WAMP/XAMPP/LAMP/MAMP, thư mục `htdocs`/`www`, cấu hình `httpd.conf` và `php.ini`).

**Slide 11 · Giải mã cú sốc: Vì sao trình duyệt "mù" PHP? (5 phút).**

- Trình duyệt (Chrome, Edge, Safari) ở máy khách chỉ biết đọc đúng 3 ngôn ngữ: **HTML, CSS và JavaScript**.
- Mã **PHP** chứa mật khẩu cơ sở dữ liệu, công thức tính giá, logic kiểm tra tồn kho. Nếu trình duyệt mà đọc trực tiếp được file `.php`, toàn bộ bí mật kinh doanh và mật khẩu kho hàng của sàn TMĐT sẽ lộ sạch cho khách xem!
- Vì vậy, file `.php` **bắt buộc phải được thực thi trên Máy chủ (Web Server)**: Phần mềm Web Server (Apache) nhận lời xin từ trình duyệt -> chuyển file `.php` cho **Bộ xử lý PHP** chạy ngầm -> lấy dữ liệu từ **MySQL** -> biến kết quả thành **HTML thuần** rồi mới gửi trả về trình duyệt. Trình duyệt không bao giờ nhìn thấy một dòng code PHP nào.

**Slide 12 · Lịch sử và Bản đồ chọn Web Server theo ngôn ngữ (5 phút).** Điểm nhanh các mốc chính trong Chương 2 để sinh viên nắm kiến thức thi:

- **12/1990:** Tim Berners-Lee viết Web Server đầu tiên (**CERN httpd**) trên máy NeXT.
- **1995:** **Apache HTTP Server** (mã nguồn mở) và **IIS** (của Microsoft) ra đời.
- **Từ 2000:** **Nginx** (đọc là *Engine-X*) và **Lighttpd** xuất hiện để tối ưu xử lý lượng truy cập cực lớn song song.
- **Bảng ghép cặp Ngôn ngữ & Web Server (Rất hay hỏi trong trắc nghiệm LMS):**
  - **PHP** -> **Apache**, **Nginx** (nhẹ, miễn phí, chạy WordPress/Joomla và các web TMĐT vừa và nhỏ).
  - **Java** -> **Apache Tomcat**, Jetty (chạy JSP/Servlet).
  - **C# (.NET)** -> **IIS** (trên Windows), Kestrel.
  - **Python** -> **Gunicorn**, uWSGI.
  - **JavaScript (Server)** -> **Node.js**.

**Slide 13 · Tại sao dùng XAMPP / WAMP trên máy cá nhân? (5 phút).**

- Muốn chạy thử web động trên laptop, ta cần cài đủ 3 mảnh: **Apache** (tiếp tân nhận yêu cầu) + **PHP** (đầu bếp chế biến) + **MySQL / MariaDB** (tủ kho chứa dữ liệu).
- Nếu tải rời từng phần mềm về tự cài: rất dễ lệch phiên bản và cực kỳ khó nối dây cấu hình cho người mới.
- Các gói tích hợp đóng sẵn 3 mảnh này vào 1 bộ cài duy nhất:
  - **WAMP** (*Windows, Apache, MySQL, PHP*): **Chỉ chạy trên Windows**, thư mục chứa web là `C:\wamp64\www\`.
  - **XAMPP** (*Cross-Platform, Apache, MySQL, PHP, Perl*): **Đa nền tảng** (chạy được trên Windows, Linux, macOS), thư mục chứa web là `C:\xampp\htdocs\`.
  - **LAMP** (chỉ cho Linux) và **MAMP** (cho macOS).

**Slide 14 · Quy tắc sống còn: Thư mục gốc (`htdocs`) và `index.php` (5 phút).**

- Nhiều bạn để file `san-pham.php` ngoài màn hình Desktop rồi mở Chrome gõ `C:\Users\...\Desktop\san-pham.php` -> Đó là mở trực tiếp từ ổ cứng (`file://`), **không đi qua tiếp tân Apache**, nên PHP không chạy!
- **Quy tắc bắt buộc:**
  1. Phải bật đèn xanh **Apache** trong XAMPP Control Panel (hoặc biểu tượng WAMP màu xanh lá).
  2. Phải đặt thư mục dự án (ví dụ `hubshop`) vào đúng `C:\xampp\htdocs\hubshop\` (hoặc `C:\wamp64\www\hubshop\`).
  3. Mở trình duyệt gõ: `http://localhost/hubshop/san-pham.php`.
- **Hỏi nhanh lớp:** *"Nếu thầy chỉ gõ `http://localhost/hubshop` mà không ghi tên file, Apache sẽ làm gì?"* -> Đáp án: Tự động tìm và chạy file **`index.php`** (hoặc `index.html`). Nếu trong thư mục không có file `index`, trình duyệt sẽ liệt kê danh sách toàn bộ các file đang có trong thư mục đó.

**Slide 15 · Hai bảng điều khiển của Kỹ sư: `httpd.conf` và `php.ini` (6 phút).** Sinh viên rất hay nhầm 2 file cấu hình này khi làm bài thi trắc nghiệm; dùng ẩn dụ để tách bạch:

| Tập tin | Quản lý ai? | Các tham số quan trọng (Theo Đề cương Chương 2) |
| --- | --- | --- |
| **`httpd.conf`** | **Apache** (Người tiếp tân gác cổng) | • `Listen 0.0.0.0:80` và `ServerName localhost:80`: Cổng mặc định là **80**. Nếu đổi sang `8080` hoặc `9999`, phải gõ `http://localhost:8080`.<br>• `LimitRequestBody`: Giới hạn kích thước gói tin gửi lên Apache (tính bằng byte).<br>• `LoadModule rewrite_module` (`mod_rewrite`): Bỏ dấu `#` ở đầu dòng để bật tính năng làm đẹp URL chuẩn SEO. |
| **`php.ini`** | **PHP** (Người đầu bếp xử lý code) | • `upload_max_filesize` và `post_max_size`: Giới hạn dung lượng file tải lên (ví dụ `50M`).<br>• `memory_limit`: Bộ nhớ tối đa cho 1 kịch bản PHP (`128M`).<br>• `max_execution_time`: Thời gian chạy tối đa (mặc định/ví dụ `300` giây), quá giờ tự ngắt để chống treo máy chủ.<br>• `display_errors`: Bật `On` khi đang lập trình để thấy dòng báo lỗi mà sửa; **bắt buộc tắt `Off`** khi đưa web ra thực tế để hacker không nhìn thấy cấu trúc hệ thống. |

*Lưu ý vàng:* Sửa bất kỳ thông số nào trong `httpd.conf` hay `php.ini` xong đều **phải Restart lại Apache** thì mới có tác dụng.

**Slide 16–17 · Thử thách 2: Bác sĩ cấp cứu phòng Lab (10 phút thảo luận + 4 phút giải đáp).**

- Chia nhóm 3–4 bạn ngồi gần. Trên slide hiện **4 ca cấp cứu thực tế**:
  - **Ca 1:** Bạn Nam bấm nút *Start Apache* trong XAMPP nhưng đèn nháy đỏ rồi tắt ngúm, báo lỗi: *"Port 80 in use by Unable to open process"*. Nam phải mở file nào, sửa dòng nào thành `8080`, và sau đó gõ địa chỉ gì trên trình duyệt?
  - **Ca 2:** Bạn Lan tải ảnh sản phẩm nặng `20MB` lên web PHP nhưng bị báo lỗi vượt quá giới hạn `2MB` mặc định của PHP. Lan cần mở file cấu hình nào và sửa tham số nào?
  - **Ca 3:** Bạn Minh gõ `http://localhost/hubshop` thì tự nhiên thấy hiện toàn bộ danh sách file code trong thư mục chứ không vào thẳng trang chủ. Vì sao và cách khắc phục?
  - **Ca 4:** Website `hubshop.vn` đã chạy thật cho khách hàng mua, nhưng khi khách nhập sai đường dẫn, màn hình hiện dòng lỗi: `Fatal error in C:\xampp\htdocs\hubshop\config_db.php on line 12`. Tại sao điều này cực kỳ nguy hiểm và phải tắt tham số nào?
- **Đáp án chốt ở Slide 17:**
  - **Ca 1:** Đụng cổng 80 (do IIS, Skype, VMware chiếm). Mở **`httpd.conf`**, sửa `Listen 80` và `ServerName localhost:80` thành `8080`, Restart Apache, truy cập `http://localhost:8080`.
  - **Ca 2:** Mở **`php.ini`**, tăng `upload_max_filesize = 50M` và `post_max_size = 50M`, rồi Restart Apache.
  - **Ca 3:** Do trong thư mục `hubshop` chưa có file tên là **`index.php`**. Chỉ cần đổi tên file trang chủ thành `index.php`.
  - **Ca 4:** Lộ đường dẫn hệ thống và tên file cấu hình cho kẻ tấn công. Phải mở **`php.ini`** đổi **`display_errors = Off`** khi chạy thực tế (Production).

---

## Giải lao 10 phút (phút 90–100, slide 18)

Bấm đồng hồ 10 phút trên Slide 18. Trong giờ giải lao, nhắc các bạn dùng laptop cá nhân bật sẵn Apache trên XAMPP và giải nén sẵn `ngrok.exe` (hoặc chuẩn bị điện thoại có 4G).

---

## Phần 3 · 70% Thực chiến (Phần A): Self-hosting trên Windows với Ngrok (phút 100–145, slide 19–24)

Đây là phần chuyển từ "kiến thức phòng thi" sang "tư duy hạ tầng của kỹ sư": dùng chính chiếc laptop Windows đang chạy XAMPP để phát sóng cửa hàng ra Internet thật.

**Slide 19 · Tình huống: Niềm vui ngắn chẳng tày gang với `localhost` (5 phút).**

- Bạn vừa dựng xong trang `http://localhost/hubshop/index.php` chạy mượt mà trên laptop.
- Bạn hào hứng copy nguyên đường link `http://localhost/hubshop/index.php` gửi qua Zalo cho bạn thân đang ngồi uống cà phê ở quận khác bấm vào xem.
- Kết quả: Điện thoại của bạn thân báo **"Không thể truy cập trang web này" (ERR_CONNECTION_REFUSED)**.
- Hỏi lớp 60 giây: *"Tại sao máy mình mở được mà điện thoại bạn mình bấm vào đúng cái link đó lại không mở được?"*
- Chốt bản chất: Từ khoá `localhost` (hay địa chỉ IP `127.0.0.1`) trong mạng máy tính có nghĩa là **"chính bản thân chiếc máy đang cầm trên tay"**. Khi điện thoại của bạn thân đọc chữ `localhost`, nó tự tìm bên trong chiếc điện thoại đó xem có web server nào không - chứ nó không hề gọi về chiếc laptop của bạn!

**Slide 20 · Tư duy nguyên bản: Ràng buộc thật sự của mạng cá nhân là gì? (7 phút).**

- Sinh viên hỏi tiếp: *"Vậy em không gửi chữ `localhost` nữa, em xem địa chỉ IP Wifi của laptop em (ví dụ `192.168.1.15`) rồi gửi `http://192.168.1.15/hubshop` cho bạn được không?"*
- Câu trả lời:
  - Nếu bạn ấy **bắt chung cục Wifi phòng máy** với em -> **Vào được!**
  - Nhưng nếu bạn ấy **tắt Wifi, bật 4G trên điện thoại** (hoặc ngồi ở nhà riêng) -> **Lập tức không vào được nữa!**
- Dùng sơ đồ trên slide để chỉ ra **2 ràng buộc vật lý không bỏ được**:
  1. **IP nội bộ (Private IP):** Địa chỉ `192.168.x.x` chỉ giống như "số phòng tầng 3 trong một khu chung cư". Có hàng triệu quán cà phê và hộ gia đình trên thế giới đều đánh số phòng là `192.168.1.15`. Bưu điện Internet ngoài đường lớn không biết phải giao thư đến chung cư nào.
  2. **NAT & Tường lửa (Router Wifi của trường/nhà):** Cục Router Wifi đóng vai bảo vệ toà nhà. Nó cho phép người từ trong phòng gọi ra ngoài Internet dễ dàng, nhưng **chặn đứng mọi người lạ từ ngoài Internet tự ý đẩy cửa xông vào phòng bạn** (để bảo vệ máy tính của bạn khỏi hacker). Bạn cũng không có quyền admin của cục Wifi trường Đại học Ngân hàng để mở cổng (Port Forwarding).

**Slide 21 · Giải pháp nhỏ nhất: Đường hầm Ngrok (Reverse Tunnel) (6 phút).**

- Áp dụng đúng câu hỏi số 3 của Tư duy nguyên bản: *"Người ngoài không tự đẩy cửa đi vào phòng mình được, nhưng mình từ trong phòng lại đi ra ngoài đường lớn được. Vậy giải pháp nhỏ nhất là gì?"*
- **Đáp án:** Ta cho một chương trình nhỏ trên laptop Windows (**Ngrok**) **chủ động nối một đường ống (Tunnel) từ cổng 80 của XAMPP đi ra một trạm trung chuyển công cộng ngoài mặt đường Internet** (ví dụ `https://hubshop-demo.ngrok-free.app`).
- Khi khách hàng dùng 4G bấm vào địa chỉ `ngrok-free.app` đó:
  1. Lời xin HTTP đến trạm trung chuyển Ngrok ngoài Internet.
  2. Trạm Ngrok tuồn lời xin đó qua "đường ống đã nối sẵn" về thẳng cổng 80 của Apache trên laptop Windows của bạn.
  3. Apache và PHP trên máy bạn xử lý xong, trả HTML ngược qua đường ống về điện thoại khách hàng!
- Chỉ cần đúng 1 dòng lệnh trên Windows Terminal / Command Prompt:
  ```bash
  ngrok http 80
  ```
  *(Lưu ý cho lớp: Nếu ở Phần 2 máy bạn nào đã đổi cổng Apache sang `8080`, thì gõ `ngrok http 8080`)*.

**Slide 22 · Khoảnh khắc "Aha!": Nhìn thấy HTTP sống dậy trên màn hình đen (5 phút).**

- Giảng viên bật trực tiếp cửa sổ đen của Ngrok lên màn hình máy chiếu (hoặc chiếu slide mô phỏng cửa sổ Ngrok).
- Giải thích 3 dòng thông tin cực kỳ trực quan trên màn hình Ngrok:
  - `Forwarding: https://a1b2-c3d4.ngrok-free.app -> http://localhost:80`: Địa chỉ công cộng trên Internet đã nối thẳng vào cổng 80 máy bạn. (Có sẵn luôn ổ khoá bảo mật `https://`!).
  - `Web Interface: http://127.0.0.1:4040`: Hộp đen giám sát (Ngrok Inspector) cho phép soi từng gói tin HTTP Request và Response.
  - `HTTP Requests`: Mỗi khi có một sinh viên dưới lớp lấy điện thoại bấm vào link, trên màn hình laptop của bạn nhảy ngay lập tức:
    - `GET /hubshop/index.php 200 OK`
    - `GET /hubshop/style.css 200 OK`
    - `GET /hubshop/gio-hang.php 404 Not Found`
- Nhấn mạnh: Mọi thứ học ở Buổi 1 (URL, DNS, HTTP GET, mã 200/404) và đầu Buổi 2 (cổng 80, Apache, `style.css`) giờ hiện ra sống động theo từng cú chạm tay trên điện thoại!

**Slide 23–24 · Thử thách 3: Phát sóng cửa hàng từ Laptop Windows ra mạng 4G (15 phút thực hành + 7 phút tổng kết).**

- **Cách tổ chức trong phòng máy:** Làm theo cặp hoặc nhóm bàn (1 máy bật XAMPP + Ngrok đóng vai **Máy chủ**, các điện thoại tắt Wifi bật **4G** đóng vai **Khách hàng từ xa**).
- **4 bước thực hiện trên Slide 23:**
  1. Tạo thư mục `C:\xampp\htdocs\hubshop`, đặt vào đó file `index.php` có 1 câu lệnh PHP động lấy giờ hệ thống:
     ```php
     <?php date_default_timezone_set('Asia/Ho_Chi_Minh'); ?>
     <!DOCTYPE html>
     <html>
     <head>
       <meta charset="utf-8">
       <title>HUB Shop Live</title>
       <link rel="stylesheet" href="style.css">
     </head>
     <body>
       <div class="card">
         <h1>Cửa hàng của [Tên Sinh Viên]</h1>
         <p>Giờ máy chủ hiện tại: <b><?php echo date('H:i:s - d/m/Y'); ?></b></p>
       </div>
     </body>
     </html>
     ```
  2. Mở `http://localhost/hubshop` trên máy mình để chắc chắn trang chạy đúng và giờ nhảy mỗi khi nhấn F5.
  3. Mở Command Prompt, gõ `ngrok http 80` (hoặc cổng Apache của máy), copy đường link `https://....ngrok-free.app/hubshop`.
  4. Gửi link cho bạn bàn bên cạnh mở bằng **4G trên điện thoại**. Quan sát cửa sổ Ngrok nhảy dòng `200 OK` và mở `http://127.0.0.1:4040` để xem điện thoại của bạn mình dùng trình duyệt gì (`User-Agent: iPhone / Android`)!
- **Câu hỏi phản biện sau khi làm xong (Slide 24):**
  - *"Khi bạn em nhấn F5 trên điện thoại, con số giây `H:i:s` thay đổi. Đồng hồ đó là đồng hồ của điện thoại bạn em hay đồng hồ của chiếc laptop Windows đang làm máy chủ?"* -> **Đáp án:** Đồng hồ của chiếc laptop làm máy chủ! Vì PHP chạy trên máy chủ, viết ra con số đó thành chữ HTML rồi mới gửi sang điện thoại.

---

## Phần 4 · 70% Thực chiến (Phần B): Vibe Code với Kiến trúc dễ bảo trì (phút 145–190, slide 25–29)

Phần này giải quyết trực tiếp yêu cầu cốt lõi của bạn: *"Với người có chuyên môn lập trình web thì vibe code phải tạo ra website với một kiến trúc dễ quản lý, bảo trì"*.

**Slide 25 · Căn bệnh "Vibe Code Mì Ý" (Spaghetti Code) (5 phút).**

- Chiếu 2 bức tranh đối lập khi dùng AI (ChatGPT, Claude, Cursor) viết code:
  - **Người không có chuyên môn gõ Prompt:** *"Hãy làm cho tôi một website bán quần áo thật đẹp"*.
  - **Hậu quả:** AI trả về **1 file duy nhất dài 800 dòng**, trong đó cấu hình cửa hàng, mã màu CSS, danh sách sản phẩm, công thức tính tiền và thẻ HTML trộn lẫn vào nhau như một bát mì ý rối tinh.
  - **Khi cần sửa thực tế:** Sếp bảo *"Đổi hotline ở chân trang trên cả 5 trang"* hoặc *"Đổi màu nút mua hàng"* -> Sửa chỗ này vỡ chỗ kia, AI càng sửa càng lỗi vì file quá dài.

**Slide 26 · Khung Kiến trúc "Chia để trị" (Separation of Concerns) từ Buổi 2 (6 phút).**

- Dạy sinh viên nguyên tắc vàng của kỹ sư phần mềm ngay từ những dòng PHP đầu tiên: **Mỗi file chỉ làm đúng 1 việc (Single Responsibility)**.
- Với một website TMĐT ở giai đoạn đầu, bắt buộc phải chia thư mục `htdocs/hubshop/` thành các ngăn rõ ràng:

```text
hubshop/
├── config.php        # Ngăn 1: Cấu hình chung (Tên shop, Hotline, % Khuyến mãi, sau này là kết nối DB)
├── assets/
│   └── style.css     # Ngăn 2: Toàn bộ giao diện CSS (External CSS - dùng chung mọi trang)
├── includes/
│   ├── header.php    # Ngăn 3: Đầu trang & Menu dùng chung
│   └── footer.php    # Ngăn 3: Chân trang & Bản quyền dùng chung
├── index.php         # Ngăn 4: Trang chủ cửa hàng
└── san-pham.php      # Ngăn 4: Trang chi tiết sản phẩm
```

- Chỉ cho sinh viên thấy lợi ích tức thì: Muốn đổi tên cửa hàng hoặc % giảm giá -> chỉ mở đúng `config.php` (10 dòng). Muốn đổi màu sắc -> chỉ mở `assets/style.css`. Giao cho AI sửa file nào thì chỉ đưa đúng file nhỏ đó, AI không bao giờ làm hỏng phần khác!

**Slide 27 · Công thức viết Prompt "Chuẩn Kỹ sư" (5 phút).**

Hướng dẫn sinh viên bộ khung 4 dòng khi ra lệnh cho AI viết code:
1. **Vai trò & Bối cảnh:** *"Tôi đang chạy PHP trên XAMPP (Windows), thư mục gốc `htdocs/hubshop`."*
2. **Ràng buộc Kiến trúc (Quan trọng nhất):** *"Bắt buộc tách code thành các file riêng biệt: `config.php` (chứa biến tên shop, hotline, phần trăm giảm giá), `assets/style.css` (External CSS dùng class, tuân thủ Box Model), và `index.php` (hiển thị trang sản phẩm)."*
3. **Yêu cầu Nghiệp vụ:** *"Trong `index.php`, dùng PHP lấy giá gốc trừ đi % giảm giá trong `config.php` để hiện giá khuyến mãi và giờ mở cửa hiện tại."*
4. **Tiêu chuẩn Nghiệm thu:** *"Code ngắn gọn, có chú thích tiếng Việt từng đoạn để tôi kiểm tra."*

**Slide 28–29 · Thử thách 4: Vibe Code cửa hàng `hubshop` & Kiểm định chéo (20 phút làm + 9 phút nghiệm thu).**

- **Nhiệm vụ (20 phút):**
  1. Dùng công thức Prompt trên để yêu cầu AI sinh bộ code `hubshop` gồm tối thiểu 3 file tách biệt (`config.php`, `assets/style.css`, `index.php`).
  2. Lưu vào `C:\xampp\htdocs\hubshop\`, kiểm tra trên `http://localhost/hubshop` và phát qua **Ngrok**.
- **Nghiệm thu chéo 3 bước (5 phút cuối thử thách - Slide 29):** Hai bạn ngồi cạnh đổi vai **Chủ đầu tư** và **Kỹ sư**:
  - **Bài test 1 (Kiểm tra tính dễ bảo trì):** Chủ đầu tư yêu cầu: *"Đổi tên cửa hàng và tăng khuyến mãi từ 10% lên 25%, đồng thời đổi màu nút Mua hàng sang màu đỏ trong vòng 60 giây!"* -> Nếu kỹ sư chỉ cần mở `config.php` và `style.css` sửa trong 30 giây mà không đụng vào HTML trong `index.php` là **ĐẠT chuẩn kiến trúc**.
  - **Bài test 2 (Kiểm tra hiểu bài Đề cương):** Chủ đầu tư chỉ ngẫu nhiên vào 1 class trong `style.css` (hỏi `padding`/`margin` làm gì) và 1 dòng `<?php ... ?>` trong `index.php` -> Kỹ sư giải thích đúng.
  - **Bài test 3 (Kiểm tra Self-hosting):** Chủ đầu tư dùng điện thoại bấm vào link Ngrok của Kỹ sư, thấy giao diện cập nhật ngay lập tức.

---

## Phần 5 · Đặt bài toán Đồ án Nhóm (VPS Ubuntu) & Chốt buổi (phút 190–225, slide 30–34)

**Slide 30 · Câu hỏi phản biện: "11 giờ đêm bạn gấp laptop đi ngủ..." (7 phút).**

- Khi cả lớp đang hào hứng vì cửa hàng chạy được trên điện thoại qua Ngrok, đặt câu hỏi thực tế:
  - *"Giả sử tối nay bạn đăng link Ngrok này lên TikTok, khách đang vào xem hàng ầm ầm. Đúng 11 giờ đêm, bạn gấp màn hình laptop Windows lại đi ngủ (hoặc mang laptop ra quán cà phê bị đổi Wifi). Chuyện gì xảy ra với khách hàng?"*
- Cho sinh viên tự liệt kê **4 giới hạn không thể vượt qua của Laptop cá nhân + Ngrok miễn phí**:
  1. **Tắt máy / Ngủ máy = Sập tiệm** (Web thương mại điện tử phải thức 24/7).
  2. **Đổi link mỗi lần bật lại:** Bản Ngrok miễn phí sẽ sinh một tên miền ngẫu nhiên mới mỗi khi tắt đi bật lại -> Link in trên bao bì hay gửi cho khách hôm qua hôm nay thành rác.
  3. **Giới hạn băng thông & kết nối:** Ngrok miễn phí chỉ cho vài chục lượt bấm mỗi phút.
  4. **Chung tài nguyên cá nhân:** Laptop vừa chạy XAMPP vừa mở 20 tab Chrome hay chơi game sẽ làm web của khách treo cứng.

**Slide 31 · Thử thách Kỹ sư Thực chiến (Bài tập Nhóm mở rộng): VPS Ubuntu + Tailscale + Coolify (10 phút).**

- Từ 4 giới hạn trên, giới thiệu **Kiến trúc Self-hosting chuyên nghiệp** dành cho **Bài tập Nhóm (5–7 sinh viên/nhóm)**:
  - Thay vì để máy chủ nằm trên chiếc laptop Windows hay phải tắt mở, cả nhóm đầu tư chung **1 máy chủ ảo trên mây (VPS)** cài hệ điều hành **Ubuntu Linux** chạy 24/7 (chi phí chỉ khoảng 80.000đ – 120.000đ/tháng, chia cho 6 bạn chỉ bằng **1 ly trà sữa 15.000đ/người**).
  - Giải thích vai trò của bộ 3 công cụ hiện đại bằng ngôn ngữ đời thường:
    1. **VPS Ubuntu:** Một chiếc máy tính không màn hình đặt ở trung tâm dữ liệu, bật 24/24, không bao giờ đi ngủ.
    2. **Tailscale:** Mạng riêng ảo (VPN) tạo một "hành lang nội bộ có khoá từ" nối thẳng máy tính của các thành viên trong nhóm vào quản trị VPS Ubuntu mà không sợ hacker ngoài Internet dò mật khẩu.
    3. **Coolify:** "Người quản gia tự động" cài trên Ubuntu. Thay vì phải gõ hàng trăm lệnh cấu hình Apache, PHP, MySQL, chứng chỉ HTTPS bằng tay, nhóm chỉ cần đẩy code lên **GitHub**, Coolify tự động kéo về đóng gói và phát sóng ra tên miền cố định 24/7!
- Nhấn mạnh sự công bằng:
  - Trên lớp mỗi buổi: 100% sinh viên dùng **Windows + XAMPP + Ngrok** để học và thực hành.
  - Đồ án Nhóm (nộp và trình diễn ở Buổi 8–9): Các nhóm triển khai hệ thống của nhóm lên **VPS Ubuntu + Tailscale + Coolify** để nhận điểm thưởng thực chiến tối đa.

**Slide 32 · Nhìn lại "Một giây sau cú bấm" khi có Web Server & PHP (6 phút).**

- Nâng cấp sơ đồ 4 bước của Buổi 1 thành **5 bước của Web động**:
  - ① Trình duyệt đọc URL, đi qua Internet (hoặc đường hầm Ngrok) tới cổng 80 của máy chủ.
  - ② **Apache** nhận lời xin `GET /index.php`, thấy đuôi `.php` nên gọi **Bộ xử lý PHP** dậy.
  - ③ **PHP** đọc `config.php`, tính toán giá khuyến mãi, lắp ghép thành **HTML thuần** trả cho Apache.
  - ④ Apache đóng gói `200 OK` gửi HTML về trình duyệt.
  - ⑤ Trình duyệt đọc HTML, thấy thẻ `<link href="style.css">` liền xin tiếp file CSS về để tô màu, kẻ khung (`padding`, `margin`) và vẽ lên màn hình điện thoại!

**Slide 33–34 · Bài tập về nhà trên LMS & Chuẩn bị Buổi 3 (12 phút).**

- **Cam kết 30% Đề cương (Trên hệ thống LMS):**
  - Đọc kỹ **Chương 1 (mục 1.2.6 CSS)** và toàn bộ **Chương 2 (Cài đặt & cấu hình Web Server)** trên Ebook LMS.
  - Hoàn thành **Vòng Test 3 cấp bậc của Chương 2** và **Quiz Buổi 2** trên LMS (hệ thống tự chấm điểm và lưu tiến độ).
- **Bài thực hành về nhà (Bắt buộc cá nhân):**
  - Hoàn thiện bộ khung `hubshop` trên XAMPP (`config.php`, `assets/style.css`, `index.php`, `san-pham.php`), chụp ảnh màn hình truy cập thành công qua link **Ngrok** trên điện thoại kèm cửa sổ log `200 OK` của Ngrok.
- **Nhiệm vụ Nhóm (Chuẩn bị cho Đồ án):**
  - Chốt danh sách nhóm 5–7 thành viên, bầu nhóm trưởng kỹ thuật, đăng ký tên cửa hàng TMĐT của nhóm.
- **Hẹn Buổi 3:** Bước vào **Chương 3 (Ngôn ngữ PHP - Phần 1)**: Biến, kiểu dữ liệu, toán tử và cấu trúc rẽ nhánh `if/else`, `switch/case` -> Thực chiến dùng PHP tính hoá đơn luỹ tiến, mã giảm giá, phí vận chuyển và bắt lỗi logic do AI viết!

---

## Phụ lục cho Giảng viên

**Bảng câu hỏi kiểm tra nhanh đầu Buổi 3 (khớp 100% Đề cương & Thực chiến)**

| Câu hỏi | Đáp án gợi ý |
| --- | --- |
| Muốn dùng chung một kiểu định dạng cho nhiều thẻ HTML, dùng `.class` hay `#id`? | Dùng `.class` (ký hiệu dấu chấm). `#id` chỉ dùng cho 1 phần tử duy nhất |
| Khoảng cách từ chữ bên trong nút bấm ra tới viền nút gọi là `padding` hay `margin`? | `padding` (đệm trong). Còn `margin` là khoảng cách đẩy các nút khác ở bên ngoài ra xa |
| Vì sao mở file `.php` bằng đường dẫn ổ cứng `C:\...` thì code PHP không chạy? | Vì trình duyệt không hiểu PHP; file `.php` phải được gọi qua Web Server (`http://localhost/...`) để Apache chuyển cho bộ xử lý PHP thực thi |
| Thư mục chứa mã nguồn web mặc định của XAMPP và WAMP tên là gì? | XAMPP là `htdocs` (`C:\xampp\htdocs\`); WAMP là `www` (`C:\wamp64\www\`) |
| Muốn đổi cổng mặc định 80 của Apache sang 8080 thì sửa ở file nào? | Sửa `Listen` và `ServerName` trong file **`httpd.conf`** của Apache, sau đó restart Apache |
| Muốn tăng dung lượng file tải lên tối đa từ 2MB lên 50MB trong PHP thì sửa file nào? | Sửa `upload_max_filesize` và `post_max_size` trong file **`php.ini`** |
| Vì sao khi đưa website lên chạy thật trên Internet phải đặt `display_errors = Off`? | Để khi có lỗi không bị lộ đường dẫn thư mục, tên bảng CSDL hay cấu trúc code cho tin tặc thấy |
| Ngrok giúp giải quyết rào cản nào khi chạy web trên laptop cá nhân? | Vượt qua rào cản NAT/Tường lửa của cục Wifi bằng cách chủ động nối một đường hầm (tunnel) từ cổng 80 trên laptop ra một địa chỉ công cộng trên Internet |

**Xử lý tình huống tại phòng máy**

| Tình huống | Cách xử lý nhanh |
| --- | --- |
| Máy phòng lab chặn tải hoặc chặn chạy `ngrok.exe` | Dùng ngay công cụ thay thế không cần cài đặt: `ssh -R 80:localhost:80 nokey@localhost.run` ngay trong Command Prompt của Windows 10/11 (có sẵn OpenSSH, không cần cài gì thêm, ra ngay link `https://...lhr.life`!) |
| Điện thoại mở link Ngrok hiện trang cảnh báo màu xanh *"You are about to visit..."* | Giải thích luôn cho lớp: Đây là màn hình chống lừa đảo của Ngrok bản miễn phí. Chỉ cần bấm nút **"Visit Site"** là vào thẳng cửa hàng |
| Sinh viên sửa `style.css` nhưng nhấn F5 trên điện thoại/trình duyệt không thấy đổi màu | Trình duyệt đang lưu bộ nhớ đệm (Cache) file CSS cũ. Hướng dẫn bấm **Ctrl + F5** (hoặc thêm `?v=2` vào sau `style.css?v=2` trong thẻ `<link>`) |
| Sinh viên nhầm cổng khi gõ lệnh Ngrok (Apache chạy cổng `8080` nhưng gõ `ngrok http 80`) | Ngrok sẽ báo lỗi `502 Bad Gateway` (Trạm trung chuyển Ngrok gọi về cổng 80 trên máy bạn nhưng không có ai nghe máy). Chỉ cần tắt Ngrok và gõ đúng cổng Apache đang chạy: `ngrok http 8080` |
