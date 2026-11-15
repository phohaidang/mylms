"""Sinh trọn bộ 9 file học liệu bài giảng Buoi_01.html .. Buoi_09.html cho LMS Hub môn Lập trình Web (ITS708).

Đảm bảo:
1. Tương thích 100% với bộ trích xuất DOM trong D01/pages/lesson.js (các thẻ <h2> Mục tiêu, SCQA, Lộ trình buổi học, Bài tập về nhà).
2. Tích hợp đầy đủ:
   - Mục tiêu chuẩn đầu ra (CLO1, CLO2) & Trọng tâm ôn thi trắc nghiệm cuối kỳ.
   - Khung tư duy SCQA & Tình huống thực chiến kỹ sư web.
   - Lộ trình 250 phút theo Khế ước 30/70 (30% Lý thuyết cốt lõi Đề cương + 70% Thực chiến Self-hosting, Vibe Code có kiến trúc, Bảo mật & Gỡ lỗi).
   - Toàn bộ câu hỏi ôn tập lý thuyết và Bài tập thực hành 3 cấp độ (Cơ bản - Nâng cao - Thử thách đồ án TMĐT) từ giáo trình.
3. Không sử dụng dấu em-dash.
"""
import json, sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

COURSE_DIR = Path(r"d:/PARA/Projects/second-brain/05-Projects/lms-hub/courses/ltweb")
LESSONS_DIR = COURSE_DIR / "content/lessons"
LESSONS_DIR.mkdir(parents=True, exist_ok=True)

SESSIONS_DATA = [
    {
        "id": 1,
        "chapter": "Chương 1",
        "title": "Bức tranh toàn cảnh & Giao diện tĩnh (HTML/CSS)",
        "clo": "CLO1 - Hiểu nguyên tắc vận hành website, phân biệt Client-Server, Web tĩnh/động và dựng giao diện HTML/CSS nền tảng.",
        "exam_weight": "8/40 câu đề thi cuối kỳ (4 câu Mức 1 Nhận biết + 4 câu Mức 2 Thông hiểu) · 26 câu trong Ngân hàng câu hỏi.",
        "objectives": [
            "Giải thích chính xác mô hình <strong>Khách - Chủ (Client - Server)</strong> và 4 bước trao đổi dữ liệu qua giao thức <strong>HTTP/HTTPS</strong> cùng các mã trạng thái (200 OK, 404 Not Found, 500).",
            "Phân tích được 5 thành phần trong cấu trúc <strong>URL</strong>: <code>scheme</code>, <code>host</code>, <code>port</code> (mặc định 80/443), <code>path</code>, và <code>querystring</code>.",
            "Phân biệt rõ 4 loại <strong>Web Hosting</strong> (Shared, VPS, Dedicated, Cloud), <strong>Web tĩnh vs Web động</strong>, và <strong>Front-end vs Back-end</strong>.",
            "Sử dụng thành thạo cấu trúc trang <strong>HTML5</strong> và các thẻ định dạng văn bản, danh sách (<code>ul/ol/li</code>), bảng biểu (<code>table/tr/td</code>), liên kết (<code>a</code>), hình ảnh (<code>img</code>).",
            "Thực chiến tư duy <strong>First Principles</strong>: hiểu cách Internet vận hành từ bài toán CERN năm 1989 và định hình chuẩn đầu ra của kỹ sư web trong kỷ nguyên AI."
        ],
        "scqa": {
            "s": "Mỗi ngày bạn mở Shopee, Tiki hay Facebook hàng chục lần. Chỉ cần gõ địa chỉ hoặc chạm vào đường dẫn, giao diện cửa hàng hiện ra trong chưa đầy một giây.",
            "c": "Đằng sau cú chạm đó là cả một chuỗi sự kiện: trình duyệt phân giải tên miền, gửi gói tin HTTP Request, máy chủ xử lý và trả về mã HTML/CSS. Nếu chỉ biết bảo AI sinh code mà không hiểu luồng Client - Server, cấu trúc URL hay thẻ HTML, bạn sẽ hoàn toàn bất lực khi trang web lỗi hiển thị hoặc không tải được tài nguyên.",
            "q": "Trang web thực sự hoạt động theo cơ chế nào từ lúc gõ địa chỉ đến khi hiển thị, và làm sao để dựng bộ khung giao diện chuẩn mực cho cửa hàng thương mại điện tử?",
            "a": "Nắm vững mô hình Client - Server, giải phẫu cấu trúc URL & gói tin HTTP, phân biệt rõ vai trò của Front-end (HTML dựng khung, CSS làm đẹp, JS tương tác) với Back-end (PHP, MySQL), và tự tay xây dựng trang HTML chuẩn ngữ nghĩa."
        },
        "roadmap": [
            ("Phần 1 (30% Đề cương · 75 phút)", "Mô hình Client - Server, URL, Web Hosting, Web tĩnh vs Web động, Front-end vs Back-end, và hệ thống thẻ HTML5 cốt lõi (<code>!DOCTYPE html</code>, <code>head</code>, <code>body</code>, <code>h1-h6</code>, <code>p</code>, <code>a</code>, <code>img</code>, <code>ul/ol/li</code>, <code>table</code>)."),
            ("Phần 2 (70% Thực chiến · 120 phút)", "Tái hiện bài toán CERN 1989: Đóng vai Trình duyệt và Máy chủ gửi gói tin HTTP qua giấy -> Thiết kế lại ngôn ngữ đánh dấu HTML từ con số 0 -> Thảo luận góc nhìn kỹ sư kỷ nguyên AI (vì sao biết dùng AI sinh code chưa đủ mà phải hiểu kiến trúc và tự vận hành hệ thống)."),
            ("Phần 3 (Thực hành & Đồ án · 55 phút)", "Dựng khung HTML trang giới thiệu cá nhân & khung trang chủ cửa hàng TMĐT. Chia nhóm (3-5 SV/nhóm), nhận đề tài Đồ án nhóm (20% điểm quá trình) và thống nhất Khế ước học tập 30/70.")
        ],
        "homework": {
            "theory": [
                "1.1. Trình bày mô hình hoạt động của một trang web (Client - Request - Server - Response).",
                "1.2. Trình bày cấu trúc URL; chỉ rõ scheme, host, port, path, querystring trong <code>https://shop.vn:8080/sp?id=12&amp;c=book</code>.",
                "1.3. Nêu 4 loại web hosting (Shared, VPS, Dedicated, Cloud) và sự khác nhau về tài nguyên, chi phí, đối tượng phù hợp.",
                "1.4. So sánh trang web tĩnh và trang web động theo 5 tiêu chí (nội dung, công nghệ, xử lý tại server, CSDL, chi phí).",
                "1.5. So sánh lập trình Front-end và Back-end; nêu 3 công nghệ tiêu biểu cho mỗi bên."
            ],
            "labs": [
                "<strong>Mức Cơ bản (Bắt buộc):</strong> Tạo tập tin <code>index.html</code> giới thiệu bản thân gồm: tiêu đề <code>&lt;h1&gt;</code>, đoạn văn giới thiệu, 1 ảnh đại diện <code>&lt;img&gt;</code>, 1 danh sách <code>&lt;ul&gt;</code> sở thích, 1 bảng <code>&lt;table&gt;</code> thông tin môn học và 1 liên kết <code>&lt;a&gt;</code>.",
                "<strong>Mức Nâng cao:</strong> Bổ sung bảng thời khóa biểu học kỳ và biểu mẫu liên hệ cơ bản vào <code>index.html</code>, kiểm tra hiển thị tiếng Việt UTF-8 chuẩn.",
                "<strong>Mức Thử thách (Đồ án nhóm - 20%):</strong> Nhóm chốt tên cửa hàng TMĐT, ngành hàng, danh sách 5 chức năng chính và phác thảo sơ đồ trang chủ (Header, Menu, Banner, Lưới 6 sản phẩm, Footer). Hoàn thành đọc Ebook Chương 1 và làm Quiz Buổi 1 (26 câu) trên LMS."
            ]
        }
    },
    {
        "id": 2,
        "chapter": "Chương 2",
        "title": "Chuẩn bị môi trường, Máy chủ Web & Self-Hosting thực chiến",
        "clo": "CLO1 - Cài đặt, cấu hình thành thạo Web Server (XAMPP/WAMP), hiểu cơ chế biên dịch PHP, triển khai Self-hosting và kiến trúc Vibe Code.",
        "exam_weight": "6/40 câu đề thi cuối kỳ (2 câu Mức 1 + 2 câu Mức 2 + 2 câu Mức 3) · 18 câu trong Ngân hàng câu hỏi (+ ôn phần CSS của Chương 1).",
        "objectives": [
            "Vận dụng 3 bộ chọn CSS cơ bản (<code>tag</code>, <code>.class</code>, <code>#id</code>), 3 cách nhúng CSS (Inline, Internal, External), CSS Box Model (<code>padding</code>, <code>border</code>, <code>margin</code>) và thư viện CSS (Bootstrap, Tailwind).",
            "Giải thích được vì sao trình duyệt không hiểu trực tiếp mã <strong>PHP</strong> và vai trò của <strong>Web Server (Apache, Nginx, IIS)</strong> trong việc gọi PHP Engine biên dịch mã sang HTML.",
            "Phân biệt <strong>WAMP vs XAMPP vs MAMP</strong>, thư mục gốc <code>htdocs</code> (XAMPP) vs <code>www</code> (WAMP), và cơ chế tự động chạy tập tin mặc định <code>index.php</code> / <code>index.html</code>.",
            "Chỉnh sửa thành thạo 2 tập tin cấu hình cốt lõi: <strong><code>httpd.conf</code></strong> (đổi cổng <code>Listen 80</code> sang <code>8080/9999</code> khi xung đột cổng) và <strong><code>php.ini</code></strong> (bật <code>display_errors</code>, tăng <code>upload_max_filesize</code>).",
            "Thực chiến <strong>Self-Hosting trên Windows với Ngrok</strong> (đưa <code>localhost</code> ra Internet thật qua 4G) và áp dụng <strong>Kiến trúc 4 ngăn</strong> khi Vibe Code với AI."
        ],
        "scqa": {
            "s": "Bạn vừa tạo xong tập tin <code>shop.php</code> đầu tiên có lệnh <code>echo</code> tính giá khuyến mãi và hào hứng nhấp đúp chuột mở trên máy tính cá nhân, rồi gửi đường dẫn <code>http://localhost/shop/</code> qua Zalo cho bạn cùng bàn xem thử.",
            "c": "Hai cú sốc xảy ra liên tiếp: (1) Nhấp đúp trực tiếp khiến trình duyệt mở bằng giao thức <code>file:///</code> và phơi bày nguyên văn mã nguồn PHP chứ không tính toán; (2) Sau khi cài XAMPP chạy được <code>http://localhost/shop/</code> trên máy mình, bạn cùng bàn bấm vào link đó lại báo lỗi <em>This site can't be reached</em> vì <code>localhost</code> (127.0.0.1) là vòng lặp khép kín trên từng máy riêng biệt.",
            "q": "Làm thế nào để biến laptop cá nhân thành một Web Server thực thụ, cấu hình Apache/PHP không bị đụng cổng, phát sóng website ra Internet thật và tổ chức mã nguồn sạch sẽ khi dùng AI sinh code?",
            "a": "Cài đặt XAMPP, đặt mã nguồn vào <code>C:\\xampp\\htdocs\\</code>, làm chủ cặp bài trùng <code>httpd.conf</code> & <code>php.ini</code>, dùng đường hầm ngược <strong>Ngrok</strong> (<code>ngrok http 80</code>) để public <code>localhost</code> ra Internet, và ép AI tuân thủ kiến trúc tách file (<code>config.php</code>, <code>assets/style.css</code>, <code>includes/</code>, <code>index.php</code>)."
        },
        "roadmap": [
            ("Phần 1 (30% Đề cương · 75 phút)", "Ôn tập CSS cốt lõi (Selector <code>tag/.class/#id</code>, Inline/Internal/External CSS, Box Model) + Lý thuyết Web Server (Apache, Nginx, IIS), WAMP vs XAMPP, thư mục <code>htdocs</code> vs <code>www</code>, và cấu hình <code>httpd.conf</code> / <code>php.ini</code>."),
            ("Phần 2 (70% Thực chiến Self-Hosting · 80 phút)", "Giải phẫu mạng máy tính: <code>localhost (127.0.0.1)</code> vs LAN IP vs NAT/Firewall -> Thực hành mở đường hầm ngược với <code>ngrok http 80</code> (hoặc <code>ssh -R 80:localhost:80 nokey@localhost.run</code>) -> Bạn cùng bàn tắt Wi-Fi dùng 4G truy cập và kiểm tra gói tin HTTP trực tiếp trên cổng <code>127.0.0.1:4040</code>."),
            ("Phần 3 (70% Thực chiến Vibe Code · 95 phút)", "Bắt bệnh 'Vibe Code Mì Ý' (nhét 600 dòng HTML+CSS+PHP vào 1 file) -> Thiết kế kiến trúc 4 ngăn (<code>config.php</code>, <code>assets/style.css</code>, <code>includes/header-footer</code>, <code>index.php</code>) -> Bài test bảo trì chéo trong 60 giây & Giới thiệu đề bài nâng cao cho Đồ án nhóm (VPS Ubuntu + Tailscale + Coolify).")
        ],
        "homework": {
            "theory": [
                "2.1. Những phần mềm web server nào có thể chạy trang web viết bằng PHP? Nêu sự tương ứng giữa ngôn ngữ lập trình và web server.",
                "2.2. WAMP và XAMPP tích hợp sẵn những phần mềm nào? Điểm khác nhau giữa WAMP, MAMP và XAMPP là gì?",
                "2.3. Cổng (port) mặc định của Apache trong XAMPP là bao nhiêu? Trình bày các bước đổi sang cổng 8080 hoặc 9999 trong tập tin <code>httpd.conf</code>.",
                "2.4. Tập tin <code>php.ini</code> dùng để làm gì? Nêu ý nghĩa của thông số <code>display_errors</code> và <code>upload_max_filesize</code>.",
                "2.5. Nếu trong URL chỉ nhập tên thư mục mà không ghi tên tập tin, Apache sẽ tự động tìm tập tin nào? Điều gì xảy ra nếu thư mục đó không có tập tin mặc định?"
            ],
            "labs": [
                "<strong>Mức Cơ bản (Bắt buộc - Bài 2.7 Giáo trình):</strong> Cài đặt XAMPP/WAMP, khởi động Apache + MySQL xanh lá. Tạo <code>ltweb.php</code> trong <code>htdocs</code> in ra <code>Lập trình web PHP</code>, truy cập qua <code>http://localhost/ltweb.php</code> và chụp màn hình kết quả.",
                "<strong>Mức Nâng cao:</strong> Thực hành đổi cổng Apache trong <code>httpd.conf</code> (<code>Listen</code> và <code>ServerName</code>), bật <code>display_errors = On</code> trong <code>php.ini</code>. Tải giao diện cửa hàng tĩnh của buổi 1 vào <code>htdocs/my_shop/</code> và tách CSS ra tập tin <code>assets/style.css</code>.",
                "<strong>Mức Thử thách (Self-hosting & Kiến trúc):</strong> Dùng Ngrok phát sóng thư mục <code>my_shop</code> đã tách thành 4 phần (<code>config.php</code>, <code>includes/header.php</code>, <code>includes/footer.php</code>, <code>index.php</code>) lên Internet và chụp màn hình truy cập từ điện thoại 4G + giao diện <code>localhost:4040</code>. Hoàn thành Ebook Chương 2 & Quiz Buổi 2 (18 câu) trên LMS."
            ]
        }
    },
    {
        "id": 3,
        "chapter": "Chương 3 (Phần 1)",
        "title": "Nhập môn PHP (Phần 1): Biến, Kiểu dữ liệu, Toán tử & Cấu trúc điều kiện",
        "clo": "CLO1, CLO2 - Nắm vững cú pháp PHP nền tảng, quy tắc biến/hằng, 8 kiểu dữ liệu, độ ưu tiên toán tử và cấu trúc rẽ nhánh if/else, switch.",
        "exam_weight": "Phần trọng tâm của Chương 3 (12/40 câu đề thi cuối kỳ) · 64 câu trong Ngân hàng câu hỏi thuộc Buổi 3.",
        "objectives": [
            "Viết đúng cú pháp nhúng <strong>PHP</strong> (<code>&lt;?php ... ?&gt;</code> và thẻ rút gọn <code>&lt;?= ... ?&gt;</code>), câu lệnh xuất <code>echo</code> / <code>print</code>, và 3 cách viết chú thích (<code>//</code>, <code>#</code>, <code>/* */</code>).",
            "Áp dụng chính xác quy tắc đặt tên <strong>biến</strong> (bắt đầu bằng <code>$</code> + chữ cái hoặc <code>_</code>, phân biệt hoa/thường) và khai báo <strong>hằng</strong> bằng <code>define()</code> hoặc <code>const</code>.",
            "Phân biệt <strong>8 kiểu dữ liệu</strong> trong PHP (String, Integer, Float, Boolean, Array, Object, NULL, Resource), sự khác nhau giữa chuỗi nháy đơn <code>' '</code> và nháy kép <code>\" \"</code>, cùng cơ chế ép kiểu.",
            "Tính toán chính xác biểu thức có <strong>toán tử tiền tố/hậu tố</strong> (<code>++$x</code> vs <code>$x++</code>), so sánh bằng vs đồng nhất (<code>==</code> vs <code>===</code>), toán tử logic (<code>&amp;&amp;</code>, <code>||</code>, <code>!</code>, lưu ý độ ưu tiên của <code>=</code> so với <code>and/or</code>) và toán tử 3 ngôi (<code>? :</code>).",
            "Sử dụng thành thạo cấu trúc rẽ nhánh <code>if</code>, <code>if...else</code>, <code>if...elseif...else</code> và <code>switch...case</code> để xử lý logic tính chiết khấu, phí vận chuyển trong bài toán TMĐT."
        ],
        "scqa": {
            "s": "Giao diện cửa hàng của bạn đã chạy trên Web Server XAMPP, nhưng mọi con số (giá bán, tồn kho, phí vận chuyển) đều đang là chữ tĩnh cứng nhắc.",
            "c": "Trong thực tế thương mại điện tử, giá thanh toán phải tự động thay đổi theo số lượng mua, hạng thành viên, mã giảm giá và ngưỡng miễn phí vận chuyển. Đặc biệt, vì PHP là ngôn ngữ định kiểu động (dynamic typing), chỉ cần nhầm lẫn giữa phép gán <code>=</code>, so sánh lỏng <code>==</code> và so sánh nghiêm ngặt <code>===</code> (ví dụ <code>0 == 'abc'</code> hoặc <code>'50' === 50</code>), hệ thống có thể tính sai tiền hoặc mở toang lỗ hổng xác thực.",
            "q": "Làm sao để viết mã PHP tính toán biểu thức và điều khiển luồng rẽ nhánh chính xác tuyệt đối, đồng thời kiểm toán (audit) được các đoạn code logic do AI sinh ra?",
            "a": "Làm chủ biến, hằng, 8 kiểu dữ liệu, quy tắc nội suy chuỗi nháy kép, bảng độ ưu tiên toán tử (đặc biệt là <code>++$x</code>, <code>$x++</code>, <code>===</code>, <code>?:</code>) và cấu trúc điều kiện <code>if/elseif/switch</code>."
        },
        "roadmap": [
            ("Phần 1 (30% Đề cương · 80 phút)", "Cú pháp PHP cơ bản, Biến vs Hằng (<code>define</code> vs <code>const</code>), 8 kiểu dữ liệu & hàm gỡ lỗi <code>var_dump()</code>, sự khác biệt giữa nháy đơn <code>' '</code> và nháy kép <code>\" \"</code>, cách xử lý dấu nháy lồng nhau trong <code>echo</code>."),
            ("Phần 2 (Thực chiến Đọc code & Toán tử · 85 phút)", "Giải phẫu các bẫy toán tử hay gặp trong đề thi và thực tế: Tiền tố <code>++$x</code> vs Hậu tố <code>$x++</code>, <code>==</code> vs <code>===</code>, bẫy độ ưu tiên <code>$kq = $x and $y</code>, toán tử 3 ngôi <code>?:</code>. Thực hành 'Đấu trường Trace Code bằng tay' trước khi chạy máy."),
            ("Phần 3 (Thực chiến Logic TMĐT · 85 phút)", "Xây dựng bộ máy tính hóa đơn tự động bằng <code>if...elseif...else</code> và <code>switch...case</code> (tính giảm giá theo bậc, tính phí ship, đổi mệnh giá tiền) và kiểm toán đoạn code tính khuyến mãi bị lỗi logic do AI viết.")
        ],
        "homework": {
            "theory": [
                "3.1. Trình bày 5 đặc điểm cú pháp cơ bản của PHP. Cú pháp PHP gần giống nhất với ngôn ngữ nào?",
                "3.2. Nêu quy tắc đặt tên biến trong PHP. Trong các tên sau: <code>$2name</code>, <code>$_tong</code>, <code>$Ho-Ten</code>, <code>$ten_sv</code>, tên nào hợp lệ và tên nào sai?",
                "3.3. Phân biệt hằng và biến. So sánh sự khác nhau giữa khai báo hằng bằng <code>define()</code> và <code>const</code>.",
                "3.4. Giải thích sự khác nhau giữa <code>echo 'I love $txt!';</code> và <code>echo \"I love $txt!\";</code> khi <code>$txt = \"PHP\";</code>.",
                "3.5. Giải thích chi tiết từng bước giá trị của <code>$kq</code> trong 3 biểu thức: (a) <code>$a=4; $b=10; $c=15; $kq = ++$a + $c/$b;</code> (b) <code>$x=true; $y=false; $kq = $x and $y;</code> (c) <code>$a=4; $b=10; $c=15; $kq = ++$a * $b-- + $c / $a++ - --$b;</code>."
            ],
            "labs": [
                "<strong>Mức Cơ bản (Bắt buộc):</strong> (Bài 3.8 & 3.9) Viết trang PHP tìm số lớn nhất trong 3 số <code>$x=5, $y=9, $z=2</code> bằng <code>if/elseif</code>; viết chương trình in số ngày của một tháng <code>$thang</code> bằng cấu trúc <code>switch...case</code>.",
                "<strong>Mức Nâng cao (Bài 3.10):</strong> Viết chương trình nhập số tiền <code>$so_tien</code> (ví dụ <code>287000</code>) và đổi ra số tờ tiền mệnh giá 50.000, 20.000, 10.000, 5.000, 1.000 sao cho ưu tiên mệnh giá lớn nhất.",
                "<strong>Mức Thử thách (Nối đồ án TMĐT - Bài 3.11):</strong> Tích hợp logic tính hóa đơn tự động vào dự án cửa hàng: tính thành tiền, áp dụng chiết khấu bậc thang (từ 500k giảm 5%, từ 1 triệu giảm 10%), phí vận chuyển 30k (miễn phí nếu sau giảm từ 700k trở lên). Hoàn thành Quiz Buổi 3 (64 câu) trên LMS."
            ]
        }
    },
    {
        "id": 4,
        "chapter": "Chương 3 (Phần 2)",
        "title": "Nhập môn PHP (Phần 2): Vòng lặp, Mảng & Xử lý dữ liệu tập hợp",
        "clo": "CLO1, CLO2 - Sử dụng thành thạo vòng lặp (for, while, do-while, foreach), từ khóa break/continue và cấu trúc mảng 1 chiều, kết hợp, đa chiều.",
        "exam_weight": "Phần trọng tâm của Chương 3 (12/40 câu đề thi cuối kỳ) · 40 câu trong Ngân hàng câu hỏi thuộc Buổi 4.",
        "objectives": [
            "Phân biệt và sử dụng đúng 4 cấu trúc vòng lặp trong PHP: <strong><code>for</code></strong>, <strong><code>while</code></strong>, <strong><code>do...while</code></strong> (luôn chạy ít nhất 1 lần) và <strong><code>foreach</code></strong>.",
            "Vận dụng chính xác từ khóa <strong><code>break</code></strong> (thoát hẳn vòng lặp) và <strong><code>continue</code></strong> (bỏ qua lần lặp hiện tại để sang lần lặp kế tiếp).",
            "Khai báo và truy xuất thành thạo 3 loại mảng: <strong>Mảng chỉ số (Indexed Array)</strong>, <strong>Mảng kết hợp (Associative Array <code>key =&gt; value</code>)</strong> và <strong>Mảng đa chiều (Multidimensional Array)</strong>.",
            "Sử dụng vòng lặp <code>foreach</code> đơn và <code>foreach</code> lồng nhau để duyệt danh sách sản phẩm, giỏ hàng và xuất ra bảng/lưới giao diện HTML động."
        ],
        "scqa": {
            "s": "Ở buổi 3, bạn đã dùng biến <code>$ten_sp</code> và <code>$gia_sp</code> để hiển thị 1 sản phẩm. Nhưng một cửa hàng thương mại điện tử thực tế có hàng trăm đến hàng ngàn sản phẩm cùng lúc.",
            "c": "Bạn không thể khai báo <code>$sp1, $sp2, ..., $sp1000</code> hay copy-paste 1.000 khối thẻ HTML <code>&lt;div class='product-card'&gt;</code>. Cách làm thủ công đó khiến mã nguồn phình to, không thể tìm kiếm, lọc hay tính tổng giỏ hàng tự động.",
            "q": "Cấu trúc dữ liệu và công cụ điều khiển nào giúp lưu trữ cả danh sách sản phẩm trong một biến duy nhất và tự động sinh giao diện cho bất kỳ số lượng sản phẩm nào chỉ với vài dòng lệnh?",
            "a": "Sử dụng <strong>Mảng đa chiều kết hợp (Associative Multidimensional Array)</strong> để biểu diễn danh sách thực thể (sản phẩm, sinh viên, đơn hàng) và dùng vòng lặp <strong><code>foreach</code></strong> để tự động render giao diện HTML cũng như thống kê dữ liệu."
        },
        "roadmap": [
            ("Phần 1 (30% Đề cương · 75 phút)", "Bốn cấu trúc vòng lặp (<code>while</code>, <code>do...while</code>, <code>for</code>, <code>foreach</code>), điều kiện dừng tránh lặp vô hạn, từ khóa <code>break</code> vs <code>continue</code>; 3 loại mảng trong PHP (chỉ số, kết hợp, đa chiều) và cách thêm/truy xuất phần tử."),
            ("Phần 2 (70% Thực chiến Cấu trúc dữ liệu TMĐT · 95 phút)", "Biến đổi giao diện tĩnh thành giao diện động dữ liệu (Data-Driven UI): Tổ chức danh mục sản phẩm bằng mảng kết hợp 2 chiều -> Dùng <code>foreach</code> tự động sinh lưới sản phẩm, tự động gắn nhãn 'Hết hàng' khi <code>ton_kho == 0</code> và tính tổng giá trị giỏ hàng."),
            ("Phần 3 (Thực hành Trace Code & Lab · 80 phút)", "Giải nhanh chuỗi bài toán đọc code mảng & vòng lặp chuẩn đề thi cuối kỳ + Thực hành nhóm bài tập xử lý mảng số, mảng sinh viên và bảng cửu chương HTML.")
        ],
        "homework": {
            "theory": [
                "4.1. So sánh sự khác nhau cốt lõi giữa vòng lặp <code>while</code> và <code>do...while</code>. Khi nào vòng lặp <code>do...while</code> vẫn chạy thân vòng lặp dù điều kiện sai?",
                "4.2. Phân biệt 3 loại mảng trong PHP (mảng chỉ số, mảng kết hợp, mảng đa chiều) và viết cú pháp khai báo mẫu cho từng loại.",
                "4.3. Trình bày 2 cú pháp của vòng lặp <code>foreach</code> (chỉ lấy giá trị vs lấy cả khóa <code>$key =&gt; $value</code>).",
                "4.4. Phân biệt tác dụng của lệnh <code>break</code> và lệnh <code>continue</code> khi đặt bên trong vòng lặp."
            ],
            "labs": [
                "<strong>Mức Cơ bản (Bắt buộc - Bài 4.1 đến 4.5):</strong> Truy xuất phần tử từ mảng 1 chiều và mảng đa chiều; viết vòng lặp tìm giá trị lớn nhất, nhỏ nhất, in các số chẵn và tính tổng mảng 10 số.",
                "<strong>Mức Nâng cao (Bài 4.8 & 4.9):</strong> Cho chuỗi số <code>\"3,8,15,22,7\"</code>, tách thành mảng và in ra màn hình sao cho số chẵn tô màu đỏ, số lẻ tô màu xanh dương bằng CSS; in bảng cửu chương từ 1 đến 5 thành bảng <code>&lt;table&gt;</code> HTML.",
                "<strong>Mức Thử thách (Nối đồ án TMĐT - Bài 4.11):</strong> Đưa danh sách ít nhất 8 sản phẩm của nhóm (gồm mã, tên, giá, hình ảnh, tồn kho) vào mảng đa chiều trong <code>data.php</code>; dùng <code>foreach</code> hiển thị lên trang chủ, tự động hiện nhãn 'Hết hàng' nếu <code>ton_kho == 0</code>. Hoàn thành Quiz Buổi 4 (40 câu) trên LMS."
            ]
        }
    },
    {
        "id": 5,
        "chapter": "Chương 3 (Phần 3)",
        "title": "Nhập môn PHP (Phần 3): Xây dựng Hàm, Hàm dựng sẵn & Module hóa Code",
        "clo": "CLO1, CLO2 - Định nghĩa và gọi hàm, phân biệt truyền giá trị vs tham chiếu, sử dụng hàm dựng sẵn (chuỗi, mảng, số, ngày) và module hóa bằng include/require.",
        "exam_weight": "Hoàn tất trọn vẹn Chương 3 (148 câu trong Ngân hàng câu hỏi) · 44 câu thuộc Buổi 5.",
        "objectives": [
            "Định nghĩa và gọi <strong>Hàm tự xây dựng (User-defined function)</strong>, phân biệt tham số (parameter) vs đối số (argument), thiết lập giá trị tham số mặc định và trả về kết quả bằng <code>return</code>.",
            "Phân biệt rõ <strong>truyền tham số theo giá trị (pass by value)</strong> và <strong>truyền theo tham chiếu (pass by reference <code>&amp;$x</code>)</strong> qua bài toán hoán vị hai biến.",
            "Vận dụng thành thạo các <strong>Hàm dựng sẵn (Built-in functions)</strong> quan trọng: xử lý số (<code>abs</code>, <code>round</code>, <code>number_format</code>), thời gian (<code>date</code>), chuỗi (<code>strlen</code>, <code>substr</code>, <code>strtolower</code>, <code>strtoupper</code>, <code>explode</code>, <code>implode</code>) và mảng/biến (<code>count</code>, <code>is_array</code>, <code>array_key_exists</code>, <code>in_array</code>, <code>sort</code>, <code>asort</code>, <code>ksort</code>, <code>print_r</code>, <code>var_dump</code>, <code>isset</code>, <code>unset</code>).",
            "Tổ chức mã nguồn theo kiến trúc module hóa bằng <strong><code>include</code>, <code>include_once</code>, <code>require</code>, <code>require_once</code></strong> để tái sử dụng giao diện và thư viện hàm."
        ],
        "scqa": {
            "s": "Sau buổi 4, cửa hàng của bạn đã hiển thị được danh sách sản phẩm và tính hóa đơn, nhưng các đoạn code định dạng tiền tệ (<code>1.250.000đ</code>), tính giảm giá, kiểm tra chuỗi và hiển thị thẻ sản phẩm bị lặp đi lặp lại ở mọi trang.",
            "c": "Khi muốn đổi cách hiển thị tiền tệ hoặc sửa công thức giảm giá, bạn phải mở 10 tập tin khác nhau để sửa từng dòng. Ngoài ra, nếu không nắm rõ sự khác biệt giữa <code>sort()</code>, <code>asort()</code> và <code>ksort()</code>, khi sắp xếp mảng sản phẩm theo giá, toàn bộ mã sản phẩm (key) sẽ bị xóa sạch thành <code>0, 1, 2</code>!",
            "q": "Làm thế nào để đóng gói các đoạn logic dùng chung thành những khối LEGO tái sử dụng được ở mọi nơi, và chọn đúng hàm dựng sẵn của PHP cho từng bài toán xử lý dữ liệu?",
            "a": "Đóng gói logic vào các <strong>Hàm (Functions)</strong> đặt trong thư viện riêng (<code>helpers.php</code>), nạp vào các trang bằng <strong><code>require_once</code></strong>, và nắm vững bộ hàm dựng sẵn của PHP cho chuỗi, số, ngày tháng và mảng."
        },
        "roadmap": [
            ("Phần 1 (30% Đề cương · 80 phút)", "Định nghĩa & gọi hàm, tham số mặc định, truyền theo giá trị vs truyền tham chiếu (<code>&amp;$x</code>); tổng hợp các nhóm hàm dựng sẵn hay thi nhất (<code>date</code>, <code>number_format</code>, <code>explode/implode</code>, <code>sort/asort/ksort</code>, <code>array_key_exists</code>, <code>is_array</code>, <code>count</code>, <code>print_r</code>, <code>isset</code>, <code>unset</code>)."),
            ("Phần 2 (70% Thực chiến Refactoring & Module hóa · 90 phút)", "Phân biệt <code>include</code> vs <code>require</code> vs <code>require_once</code> (khi nào cảnh báo Warning, khi nào dừng chương trình Fatal Error) -> Thực hành Refactor dự án cửa hàng: tách <code>includes/functions.php</code>, <code>includes/header.php</code>, <code>includes/footer.php</code>."),
            ("Phần 3 (Thực hành tổng hợp Chương 3 · 80 phút)", "Hoàn thành bài thực hành Hóa đơn Mini kết hợp Mảng 2 chiều + Vòng lặp + Điều kiện + Hàm định dạng tiền + Sắp xếp sản phẩm. Tổng ôn toàn bộ Chương 3.")
        ],
        "homework": {
            "theory": [
                "5.1. Phân biệt truyền tham số theo giá trị (pass by value) và truyền theo tham chiếu (pass by reference <code>&amp;</code>). Tại sao hàm hoán vị <code>swap($a, $b)</code> bắt buộc phải dùng tham chiếu?",
                "5.2. So sánh 3 hàm sắp xếp mảng: <code>sort()</code>, <code>asort()</code> và <code>ksort()</code>. Hàm nào làm mất khóa (key) của mảng kết hợp?",
                "5.3. Phân biệt <code>explode()</code> và <code>implode()</code>; phân biệt <code>echo</code>, <code>print_r()</code> và <code>var_dump()</code>.",
                "5.4. So sánh 4 lệnh chèn tập tin: <code>include</code>, <code>include_once</code>, <code>require</code>, <code>require_once</code>. Vì sao với tập tin cấu hình quan trọng ta luôn ưu tiên <code>require_once</code>?"
            ],
            "labs": [
                "<strong>Mức Cơ bản (Bắt buộc - Bài 5.3 & 5.4):</strong> Viết hàm <code>giai_thua($n)</code> tính <code>n!</code> và hàm <code>trung_binh($mang)</code> tính giá trị trung bình của mảng số nguyên.",
                "<strong>Mức Nâng cao (Bài 4.7, 4.8 & 5.5):</strong> Viết hàm <code>hoan_vi(&amp;$a, &amp;$b)</code>; dùng <code>explode()</code> tách email <code>test@hub.edu.vn</code> thành tên email và tên miền; tách chuỗi danh sách sinh viên <code>\"0302000001-Nguyễn Văn A;0302000002-Nguyễn Văn B\"</code> và in từng dòng.",
                "<strong>Mức Thử thách (Nối đồ án TMĐT - Bài 5.7):</strong> Xây dựng tập tin <code>includes/helpers.php</code> chứa các hàm <code>dinh_dang_gia($so)</code>, <code>tinh_giam_gia($gia, $phan_tram)</code>, <code>render_san_pham($sp)</code> và dùng <code>require_once</code> ở cả trang chủ lẫn trang danh mục. Hoàn thành Ebook Chương 3 & Quiz Buổi 5 (44 câu) trên LMS."
            ]
        }
    },
    {
        "id": 6,
        "chapter": "Chương 4",
        "title": "Quản trị Cơ sở dữ liệu với MySQL & phpMyAdmin",
        "clo": "CLO1, CLO2 - Thiết kế bảng CSDL quan hệ, viết thành thạo các câu lệnh SQL (DDL & DML: CREATE, SELECT, INSERT, UPDATE, DELETE, JOIN, GROUP BY) và quản trị trên phpMyAdmin.",
        "exam_weight": "6/40 câu đề thi cuối kỳ (2 câu Mức 1 + 2 câu Mức 2 + 2 câu Mức 3) · 30 câu trong Ngân hàng câu hỏi.",
        "objectives": [
            "Hiểu rõ các khái niệm CSDL quan hệ (Bảng, Cột/Thuộc tính, Dòng/Bản ghi) và các ràng buộc toàn vẹn: <strong><code>PRIMARY KEY</code></strong>, <strong><code>FOREIGN KEY</code></strong>, <strong><code>UNIQUE</code></strong>, <strong><code>NOT NULL</code></strong>, <strong><code>AUTO_INCREMENT</code></strong>.",
            "Sử dụng nhóm lệnh <strong>DDL</strong> (<code>CREATE DATABASE</code>, <code>DROP DATABASE</code>, <code>CREATE TABLE</code>, <code>ALTER TABLE</code>, <code>DROP TABLE</code>) và chọn đúng kiểu dữ liệu MySQL (<code>varchar</code>, <code>text</code>, <code>int</code>, <code>float/double</code>, <code>date/datetime</code>).",
            "Viết chính xác câu lệnh truy vấn <strong><code>SELECT</code></strong> theo đúng thứ tự mệnh đề bắt buộc: <code>SELECT -&gt; FROM -&gt; WHERE -&gt; GROUP BY -&gt; HAVING -&gt; ORDER BY -&gt; LIMIT</code>.",
            "Phân biệt và vận dụng kết nối bảng <strong><code>INNER JOIN</code></strong>, <strong><code>LEFT JOIN</code></strong>, <strong><code>RIGHT JOIN</code></strong>, các hàm tổng hợp (<code>COUNT, SUM, AVG, MIN, MAX</code>) và các lệnh <strong><code>INSERT INTO</code></strong>, <strong><code>UPDATE ... SET ... WHERE</code></strong>, <strong><code>DELETE FROM ... WHERE</code></strong>.",
            "Sử dụng thành thạo công cụ <strong>phpMyAdmin</strong> để tạo CSDL (bảng mã <code>utf8mb4_unicode_ci</code>), quản lý bảng, chạy truy vấn SQL và sao lưu/phục hồi (<strong>Export / Import</strong> tập tin <code>.sql</code>)."
        ],
        "scqa": {
            "s": "Ở Chương 3, danh sách sản phẩm và giỏ hàng của bạn được lưu trong mảng PHP (<code>$products = [...]</code>).",
            "c": "Biến và mảng trong PHP chỉ sống tạm thời trong bộ nhớ RAM vài mili-giây khi trang web đang chạy. Ngay khi trang tải xong, mọi dữ liệu biến mất; khách hàng đăng ký tài khoản hay đặt hàng xong đều không thể lưu lại lâu dài. Hơn nữa, khi có hàng chục ngàn đơn hàng, việc lọc và thống kê bằng mảng PHP sẽ làm treo máy chủ.",
            "q": "Hệ thống nào giúp lưu trữ dữ liệu bền vững trên đĩa cứng, đảm bảo tính toàn vẹn giữa Khách hàng - Sản phẩm - Đơn hàng và truy xuất hàng vạn bản ghi trong chớp mắt?",
            "a": "Hệ quản trị cơ sở dữ liệu quan hệ <strong>MySQL</strong> kết hợp ngôn ngữ truy vấn <strong>SQL</strong> và công cụ quản trị trực quan <strong>phpMyAdmin</strong>."
        },
        "roadmap": [
            ("Phần 1 (30% Đề cương · 75 phút)", "Mô hình CSDL quan hệ, Khóa chính (Primary Key) vs Khóa ngoại (Foreign Key), các kiểu dữ liệu MySQL; nhóm lệnh DDL (<code>CREATE/ALTER/DROP</code>) và nhóm lệnh DML (<code>SELECT, INSERT, UPDATE, DELETE</code>), quy tắc vàng với mệnh đề <code>WHERE</code>."),
            ("Phần 2 (70% Thực chiến Truy vấn & Thiết kế CSDL TMĐT · 95 phút)", "Giải phẫu sự khác nhau giữa <code>WHERE</code> vs <code>HAVING</code>, <code>INNER JOIN</code> vs <code>LEFT JOIN</code> vs <code>RIGHT JOIN</code>, và phân trang với <code>LIMIT offset, count</code>. Thực hành Import CSDL <code>bike_stores.sql</code> trên phpMyAdmin và giải các bài toán truy vấn thống kê doanh thu thực tế."),
            ("Phần 3 (Thiết kế CSDL Đồ án nhóm · 80 phút)", "Thiết kế lược đồ CSDL cho Đồ án nhóm (tối thiểu 4 bảng: <code>users</code>, <code>categories</code>, <code>products</code>, <code>orders</code>, <code>order_items</code>), nhập dữ liệu mẫu tiếng Việt chuẩn UTF-8 và xuất (Export) tập tin <code>.sql</code>.")
        ],
        "homework": {
            "theory": [
                "6.1. Phân biệt ràng buộc <code>PRIMARY KEY</code> và <code>UNIQUE</code> trong MySQL. Vì sao phải tạo bảng chứa khóa chính trước bảng chứa khóa ngoại tham chiếu đến nó?",
                "6.2. Phân biệt mệnh đề <code>WHERE</code> và mệnh đề <code>HAVING</code> trong câu lệnh <code>SELECT</code>. Viết thứ tự chuẩn của 7 mệnh đề trong câu lệnh <code>SELECT</code>.",
                "6.3. So sánh kết quả trả về của <code>INNER JOIN</code>, <code>LEFT JOIN</code> và <code>RIGHT JOIN</code>. Khi một dòng ở bảng bên trái không có dòng khớp ở bảng bên phải thì <code>LEFT JOIN</code> trả về giá trị gì cho các cột của bảng phải?",
                "6.4. Phân biệt lệnh <code>DELETE FROM ten_bang;</code> và <code>DROP TABLE ten_bang;</code>. Điều gì xảy ra nếu chạy lệnh <code>UPDATE</code> hoặc <code>DELETE</code> mà quên viết mệnh đề <code>WHERE</code>?",
                "6.5. Nêu thông tin tài khoản đăng nhập mặc định của phpMyAdmin trên XAMPP/WAMP và cách sao lưu (Export) / phục hồi (Import) cơ sở dữ liệu."
            ],
            "labs": [
                "<strong>Mức Cơ bản (Bắt buộc):</strong> Tạo CSDL <code>QLSinhVien</code> gồm bảng <code>Lop</code> và <code>SinhVien</code> có khóa chính, khóa ngoại; thực hiện <code>INSERT</code> 5 sinh viên, truy vấn <code>SELECT ... WHERE ... ORDER BY</code> và <code>INNER JOIN</code>.",
                "<strong>Mức Nâng cao (Bài 6.3 trên CSDL <code>bike_stores</code>):</strong> Import <code>bike_stores.sql</code> vào phpMyAdmin; viết các truy vấn lọc sản phẩm theo thương hiệu/danh mục, thống kê số đơn hủy theo cửa hàng (<code>GROUP BY</code>), tìm khách hàng có tổng giá trị đơn > 3000 (<code>HAVING</code>) và tìm sản phẩm chưa từng được mua (<code>NOT IN</code>).",
                "<strong>Mức Thử thách (Nối đồ án TMĐT - Bài 6.5):</strong> Hoàn chỉnh CSDL cho đồ án nhóm trên phpMyAdmin (có đầy đủ khóa chính <code>AUTO_INCREMENT</code>, khóa ngoại và ít nhất 10 sản phẩm mẫu), Export ra tập tin <code>database.sql</code> lưu vào thư mục dự án. Hoàn thành Ebook Chương 4 & Quiz Buổi 6 (30 câu) trên LMS."
            ]
        }
    },
    {
        "id": 7,
        "chapter": "Chương 5 (Phần 1)",
        "title": "Lập trình Web động (Phần 1): Xử lý Web Form, GET/POST & Query String",
        "clo": "CLO1, CLO2 - Xây dựng biểu mẫu HTML Form đa dạng điều khiển, xử lý dữ liệu người dùng gửi lên bằng $_GET/$_POST, truyền tham số qua URL Query String và chống lỗi bảo mật XSS.",
        "exam_weight": "Phần trọng tâm của Chương 5 (8/40 câu đề thi cuối kỳ) · 43 câu trong Ngân hàng câu hỏi thuộc Buổi 7.",
        "objectives": [
            "Thiết kế biểu mẫu HTML <strong><code>&lt;form&gt;</code></strong> với đầy đủ các điều khiển: <code>text</code>, <code>password</code>, <code>radio</code> (cùng <code>name</code> để chọn 1), <code>checkbox</code> (<code>name=\"ten[]\"</code> để nhận mảng), <code>select/option</code>, <code>textarea</code>, <code>file</code> và <code>submit</code>.",
            "Nắm vững ý nghĩa của thuộc tính <strong><code>action</code></strong> (tập tin xử lý phía server; nếu bỏ trống sẽ gửi về chính trang hiện tại) và <strong><code>method</code></strong> (mặc định là <code>GET</code> nếu không khai báo).",
            "Phân biệt toàn diện hai phương thức <strong><code>GET</code> vs <code>POST</code></strong> (vị trí truyền dữ liệu trên URL Query String vs HTTP Request Body, tính bảo mật, giới hạn dung lượng, khả năng bookmark/lưu lịch sử).",
            "Sử dụng biến siêu toàn cục <strong><code>$_GET</code></strong> và <strong><code>$_POST</code></strong> (kiểu mảng kết hợp với khóa là thuộc tính <code>name</code> của thẻ input) kết hợp <code>isset()</code>, <code>empty()</code>, <code>htmlspecialchars()</code> để kiểm tra hợp lệ (validate) và giữ lại dữ liệu đã nhập khi form báo lỗi."
        ],
        "scqa": {
            "s": "Từ buổi 1 đến buổi 5, dữ liệu trong mã PHP của bạn đều do lập trình viên tự gõ sẵn trong code. Người dùng truy cập chỉ có thể xem chứ chưa thể gửi thông tin tìm kiếm, đăng ký hay đặt hàng lên máy chủ.",
            "c": "Khi người dùng nhập dữ liệu vào biểu mẫu (Web Form) và nhấn nút Gửi (Submit), dữ liệu đi từ trình duyệt (Client) lên máy chủ (Server). Nếu lập trình viên dùng nhầm phương thức <code>GET</code> cho form đổi mật khẩu, toàn bộ mật khẩu sẽ lộ rõ trên thanh địa chỉ URL, lịch sử trình duyệt và nhật ký máy chủ! Ngược lại, nếu không kiểm tra <code>isset()</code> hoặc không lọc dữ liệu đầu vào, website sẽ liên tục báo lỗi <em>Undefined array key</em> hoặc bị tấn công chèn mã độc XSS.",
            "q": "Cơ chế truyền dữ liệu từ Form HTML sang PHP hoạt động như thế nào, khi nào dùng GET hay POST, và làm sao để xử lý mọi loại ô nhập liệu một cách an toàn?",
            "a": "Hiểu rõ ánh xạ từ thuộc tính <code>name</code> của HTML sang khóa của mảng <code>$_GET</code> / <code>$_POST</code>, dùng <code>GET</code> cho tìm kiếm/lọc/phân trang qua Query String (<code>?key=val</code>), dùng <code>POST</code> cho đăng nhập/đăng ký/thay đổi dữ liệu, và luôn validate dữ liệu phía server."
        },
        "roadmap": [
            ("Phần 1 (30% Đề cương · 75 phút)", "Cấu trúc thẻ <code>&lt;form action='...' method='...'&gt;</code>, các điều khiển nhập liệu (textbox, password, radio, checkbox mảng <code>name='vehicle[]'</code>, select, textarea), so sánh chi tiết <code>GET</code> vs <code>POST</code> và cách truy xuất mảng <code>$_GET</code>, <code>$_POST</code>."),
            ("Phần 2 (70% Thực chiến Luồng dữ liệu & Bảo mật Form · 95 phút)", "Phân tích tình huống lộ mật khẩu qua URL khi dùng GET -> Kỹ thuật gộp Form và mã xử lý PHP vào cùng 1 tập tin -> Kỹ thuật giữ lại dữ liệu người dùng vừa nhập (Sticky Form: <code>value=\"&lt;?php echo $name; ?&gt;\"</code>) và chuyển hướng trang bằng <code>header(\"Location: ...\")</code> kèm Query String."),
            ("Phần 3 (Thực hành Lab Form 3 cấp độ · 80 phút)", "Thực hành xây dựng ứng dụng Máy tính 2 số bằng Radio, trang tìm kiếm sản phẩm bằng GET và Form Đăng ký thành viên có kiểm tra hợp lệ (Validate) bằng POST.")
        ],
        "homework": {
            "theory": [
                "7.1. So sánh phương thức <code>GET</code> và <code>POST</code> theo 5 tiêu chí: vị trí truyền dữ liệu, độ bảo mật, giới hạn dung lượng, khả năng đánh dấu trang (bookmark) và mục đích sử dụng.",
                "7.2. Trong thẻ <code>&lt;form&gt;</code>, điều gì xảy ra khi: (a) Không khai báo thuộc tính <code>method</code>? (b) Không khai báo thuộc tính <code>action</code>?",
                "7.3. Khóa (key) của mảng <code>$_GET</code> và <code>$_POST</code> được lấy từ thuộc tính nào của thẻ HTML? Vì sao các nút <code>radio</code> cùng nhóm phải đặt cùng thuộc tính <code>name</code>, và làm sao để nhận nhiều giá trị từ nhóm <code>checkbox</code>?",
                "7.4. Giải thích ý nghĩa của câu lệnh: <code>echo isset($_GET['name']) ? $_GET['name'] : 'Unknown';</code> và câu lệnh chuyển hướng <code>header('Location: signin.php?error=1');</code>."
            ],
            "labs": [
                "<strong>Mức Cơ bản (Bắt buộc - Bài 7.4):</strong> Tạo form nhập một chuỗi văn bản và nút Submit; khi gửi bằng POST, dùng PHP chuyển chuỗi thành chữ in hoa (<code>mb_strtoupper</code>) và hiển thị kết quả.",
                "<strong>Mức Nâng cao (Bài 7.5):</strong> Xây dựng trang <strong>Máy tính cá nhân 2 số</strong> gồm 2 ô nhập số, 4 nút radio chọn phép tính (<code>+, -, *, /</code>) và nút Tính. Kiểm tra lỗi nhập không phải số (<code>is_numeric</code>) và lỗi chia cho 0.",
                "<strong>Mức Thử thách (Nối đồ án TMĐT - Bài 7.6):</strong> Xây dựng trang <strong>Tìm kiếm & Lọc sản phẩm</strong> (dùng GET qua URL <code>?keyword=...&amp;cat=...</code>) và trang <strong>Đăng ký thành viên</strong> (dùng POST, giữ lại dữ liệu đã nhập khi báo lỗi, chống XSS bằng <code>htmlspecialchars</code>). Hoàn thành Quiz Buổi 7 (43 câu) trên LMS."
            ]
        }
    },
    {
        "id": 8,
        "chapter": "Chương 5 (Phần 2)",
        "title": "Lập trình Web động (Phần 2): Quản lý trạng thái với Session & Cookie",
        "clo": "CLO1, CLO2 - Giải quyết tính phi trạng thái (stateless) của HTTP bằng Session và Cookie để xây dựng chức năng Đăng nhập, Phân quyền, Đăng xuất và Giỏ hàng.",
        "exam_weight": "Phần trọng tâm của Chương 5 (8/40 câu đề thi cuối kỳ) · 16 câu trong Ngân hàng câu hỏi thuộc Buổi 8.",
        "objectives": [
            "Giải thích được vì sao giao thức <strong>HTTP là phi trạng thái (stateless)</strong> và tại sao biến thông thường trong PHP không thể giữ dữ liệu khi người dùng chuyển từ trang này sang trang khác.",
            "Nắm vững cơ chế hoạt động của <strong>Session</strong>: lưu dữ liệu trên <strong>Web Server</strong>, bắt buộc gọi <strong><code>session_start()</code></strong> ở đầu tập tin trước khi dùng mảng siêu toàn cục <strong><code>$_SESSION</code></strong>, xóa từng biến bằng <code>unset($_SESSION['key'])</code> và hủy toàn bộ phiên bằng <code>session_destroy()</code>.",
            "Nắm vững cơ chế hoạt động của <strong>Cookie</strong>: lưu dữ liệu trên <strong>Trình duyệt (Web Client)</strong>, thiết lập bằng <strong><code>setcookie(name, value, expire, path)</code></strong>, đọc bằng <strong><code>$_COOKIE['name']</code></strong> và xóa cookie bằng cách đặt thời gian hết hạn trong quá khứ (<code>time() - 3600</code>).",
            "Phân biệt chính xác khi nào dùng <strong>Session</strong> (lưu thông tin đăng nhập, quyền người dùng, giỏ hàng tạm thời) và khi nào dùng <strong>Cookie</strong> (ghi nhớ ngôn ngữ, giao diện sáng/tối, tự động đăng nhập 'Remember me')."
        ],
        "scqa": {
            "s": "Khách hàng vừa nhập đúng tài khoản và mật khẩu ở trang <code>login.php</code>, hoặc vừa bấm 'Thêm vào giỏ hàng' ở trang <code>product.php</code>.",
            "c": "Ngay khi khách bấm chuyển sang trang <code>checkout.php</code>, máy chủ web hoàn toàn 'mất trí nhớ' - không biết người này vừa đăng nhập hay đã chọn món hàng nào! Đó là vì mỗi yêu cầu HTTP là hoàn toàn độc lập (stateless). Nhưng nếu bạn lưu thẳng mật khẩu hay quyền Admin vào Cookie trên trình duyệt, kẻ tấn công chỉ cần mở F12 (DevTools) sửa Cookie là chiếm quyền điều khiển!",
            "q": "Làm thế nào để website ghi nhớ trạng thái đăng nhập và giỏ hàng của từng người dùng xuyên suốt nhiều trang một cách an toàn và đúng chuẩn kỹ thuật?",
            "a": "Kết hợp <strong>Session</strong> (lưu dữ liệu nhạy cảm như ID người dùng, vai trò, giỏ hàng trong phiên trên Server) và <strong>Cookie</strong> (lưu tùy chọn lâu dài trên trình duyệt với thời hạn xác định), đồng thời xóa sạch cả hai khi người dùng Đăng xuất."
        },
        "roadmap": [
            ("Phần 1 (30% Đề cương · 75 phút)", "Bản chất Stateless của HTTP; đối tượng Session (<code>session_start()</code>, <code>$_SESSION</code>, <code>unset()</code>, <code>session_destroy()</code>); đối tượng Cookie (<code>setcookie()</code>, <code>$_COOKIE</code>, cách tính thời gian sống <code>time() + số_giây</code> và cách xóa cookie); bảng so sánh Session vs Cookie."),
            ("Phần 2 (70% Thực chiến Xác thực & Bảo mật Phiên · 95 phút)", "Mở Chrome DevTools -> tab Application -> Cookies để quan sát trực tiếp <code>PHPSESSID</code> và các Cookie thực tế -> Xây dựng luồng Đăng nhập (<code>login.php</code>) - Trang quản trị có chốt chặn bảo vệ (<code>admin.php</code>) - Đăng xuất an toàn (<code>logout.php</code>)."),
            ("Phần 3 (Thực chiến Giỏ hàng TMĐT · 80 phút)", "Xây dựng module Giỏ hàng (Shopping Cart) bằng <code>$_SESSION['cart']</code>: thêm sản phẩm, tăng/giảm số lượng, xóa món hàng, tính tổng tiền thanh toán và tích hợp vào Đồ án nhóm.")
        ],
        "homework": {
            "theory": [
                "8.1. So sánh Session và Cookie theo 4 tiêu chí: vị trí lưu trữ, thời gian tồn tại mặc định, mức độ bảo mật và dung lượng lưu trữ.",
                "8.2. Trước khi truy xuất hoặc gán giá trị cho <code>$_SESSION</code>, ta bắt buộc phải gọi hàm nào? Để xóa riêng thông tin đăng nhập <code>$_SESSION['user']</code> mà vẫn giữ lại giỏ hàng <code>$_SESSION['cart']</code>, ta dùng lệnh nào?",
                "8.3. Giải thích ý nghĩa các tham số trong câu lệnh <code>setcookie('user_login', 'An', time() + 5 * 60, '/');</code> và câu lệnh <code>setcookie('user', '', time() - 3600, '/');</code>.",
                "8.4. Trong các tình huống sau, nên dùng Session hay Cookie: (a) Lưu thông tin định danh và vai trò người dùng đang đăng nhập; (b) Ghi nhớ ngôn ngữ hiển thị (Tiếng Việt / Tiếng Anh) sau khi đóng trình duyệt mở lại; (c) Lưu mật khẩu người dùng?"
            ],
            "labs": [
                "<strong>Mức Cơ bản (Bắt buộc - Bài 8.4 & 8.5):</strong> Tạo <code>page1.php</code> khởi tạo <code>$_SESSION['username']</code> và cookie sống 5 phút; tạo <code>page2.php</code> đọc và hiển thị giá trị Session/Cookie đó. Kiểm tra trong DevTools -> Application.",
                "<strong>Mức Nâng cao (Bài 8.6):</strong> Xây dựng hệ thống <strong>Đăng nhập - Bảo vệ trang - Đăng xuất</strong> hoàn chỉnh gồm <code>login.php</code>, <code>dashboard.php</code> (chưa đăng nhập tự động chuyển hướng về <code>login.php</code>) và <code>logout.php</code>.",
                "<strong>Mức Thử thách (Nối đồ án TMĐT - Bài 8.7):</strong> Xây dựng chức năng <strong>Giỏ hàng bằng Session</strong> (thêm vào giỏ, cập nhật số lượng, xóa sản phẩm, tính tổng đơn hàng) cho website TMĐT của nhóm. Hoàn thành Quiz Buổi 8 (16 câu) trên LMS."
            ]
        }
    },
    {
        "id": 9,
        "chapter": "Chương 5 (Phần 3)",
        "title": "Kết nối PHP & MySQL, Prepared Statements & Báo cáo Tổng hợp",
        "clo": "CLO1, CLO2 - Kết nối PHP với MySQL bằng thư viện MySQLi, thực thi truy vấn đọc/ghi dữ liệu động, phòng chống SQL Injection bằng Prepared Statements và hoàn thiện toàn bộ Website TMĐT.",
        "exam_weight": "Hoàn tất toàn bộ chương trình (40/40 câu đề thi cuối kỳ) · 18 câu thuộc Buổi 9 + Làm Đề thi thử 40 câu trên LMS.",
        "objectives": [
            "Thiết lập kết nối từ PHP đến MySQL bằng thư viện <strong>MySQLi</strong> (cả phong cách hướng đối tượng <code>new mysqli(...)</code> và hướng thủ tục <code>mysqli_connect(...)</code>), kiểm tra lỗi kết nối và thiết lập bảng mã <strong><code>set_charset('utf8')</code></strong>.",
            "Tổ chức mã kết nối CSDL chuẩn mực bằng cách tách riêng tập tin <strong><code>config.php</code></strong> và nạp bằng <strong><code>require_once</code></strong>.",
            "Thực hiện trọn vẹn quy trình 4 bước thao tác dữ liệu: kết nối -> thực thi câu lệnh SQL bằng <code>$conn-&gt;query($sql)</code> -> lấy mảng kết hợp bằng <strong><code>fetch_all(MYSQLI_ASSOC)</code></strong> / <code>fetch_assoc()</code> và duyệt hiển thị bằng <code>foreach</code> -> đóng kết nối <code>$conn-&gt;close()</code>.",
            "Sử dụng thành thạo <strong>Prepared Statements</strong> (<code>prepare()</code> -> <code>bind_param('ss', ...)</code> -> <code>execute()</code>) với ký tự giữ chỗ <code>?</code> để ngăn chặn triệt để lỗ hổng <strong>SQL Injection</strong> và xử lý tải tập tin (Upload ảnh sản phẩm) qua <code>$_FILES</code>.",
            "Hoàn thành Bài kiểm tra thực hành Giữa kỳ (20%), Báo cáo Đồ án nhóm Website TMĐT (20%) và luyện tập Đề thi thử Cuối kỳ (40 câu / 60 phút)."
        ],
        "scqa": {
            "s": "Bạn đã có giao diện HTML/CSS, bộ xử lý logic PHP (Form, Session, Cookie) và cơ sở dữ liệu MySQL chứa hàng trăm sản phẩm. Nhưng hiện tại PHP và MySQL vẫn đang đứng tách biệt nhau.",
            "c": "Nếu bạn nối chuỗi trực tiếp dữ liệu người dùng nhập từ Form vào câu lệnh SQL (ví dụ <code>SELECT * FROM users WHERE user = '$user'</code>), kẻ tấn công chỉ cần nhập <code>' OR '1'='1</code> là có thể đăng nhập không cần mật khẩu hoặc xóa trắng cơ sở dữ liệu (tấn công <strong>SQL Injection</strong>)!",
            "q": "Làm thế nào để kết nối PHP với MySQL một cách khoa học, dễ bảo trì và bảo vệ tuyệt đối cơ sở dữ liệu trước các cuộc tấn công SQL Injection?",
            "a": "Tách cấu hình kết nối ra <code>config.php</code> (đặt <code>set_charset('utf8')</code>), sử dụng phương thức hướng đối tượng của <strong>MySQLi</strong> để hiển thị dữ liệu động (<code>fetch_all(MYSQLI_ASSOC)</code>) và bắt buộc dùng <strong>Prepared Statements</strong> (<code>prepare</code> + <code>bind_param</code>) cho mọi truy vấn có tham số từ người dùng."
        },
        "roadmap": [
            ("Phần 1 (30% Đề cương · 60 phút)", "Kết nối PHP - MySQL với MySQLi (4 thông số: <code>servername</code>, <code>username</code>, <code>password</code>, <code>dbname</code>; thiết lập <code>utf8</code>; tách <code>config.php</code>), đọc dữ liệu với <code>query()</code> & <code>fetch_all(MYSQLI_ASSOC)</code>, thêm dữ liệu & upload ảnh với <code>$_FILES</code>, và cơ chế 3 bước của <strong>Prepared Statement</strong> (Chuẩn bị câu lệnh với dấu <code>?</code> -> Liên kết tham số <code>bind_param('ss', ...)</code> -> Thực thi <code>execute()</code>)."),
            ("Phần 2 (Kiểm tra Thực hành Giữa kỳ · 90 phút)", "Làm bài kiểm tra cá nhân trên máy tính (20% điểm học phần): Xây dựng ứng dụng web quản lý & tìm kiếm dữ liệu kết nối MySQL (hiển thị danh sách, tìm kiếm theo từ khóa/thể loại bằng GET, thêm mới bằng POST + Prepared Statement, phân quyền bằng Session)."),
            ("Phần 3 (Bảo vệ Đồ án nhóm & Tổng kết khóa học · 100 phút)", "Các nhóm thuyết trình và demo trực tiếp Website Thương mại điện tử chạy trên môi trường Internet (Ngrok hoặc VPS Ubuntu + Coolify), kiểm tra chéo khả năng bảo trì code và tổng kết hệ thống kiến thức ôn thi cuối kỳ (40 câu trắc nghiệm).")
        ],
        "homework": {
            "theory": [
                "9.1. Nêu 4 thông tin cần thiết để PHP thiết lập kết nối với MySQL. Vì sao cần gọi <code>$conn-&gt;set_charset('utf8')</code> ngay sau khi kết nối thành công và vì sao nên tách mã kết nối ra tập tin <code>config.php</code>?",
                "9.2. Giải thích ý nghĩa của hằng số <code>MYSQLI_ASSOC</code> trong lệnh <code>$result-&gt;fetch_all(MYSQLI_ASSOC)</code>.",
                "9.3. Prepared Statement là gì? Nêu đúng thứ tự 3 bước xử lý khi sử dụng Prepared Statement trong MySQLi.",
                "9.4. Trong câu lệnh <code>$stmt-&gt;bind_param('ssi', $ten, $tac_gia, $nam_xb);</code>, dấu <code>?</code> trong câu SQL và chuỗi định dạng <code>'ssi'</code> biểu thị điều gì? Ưu điểm bảo mật lớn nhất của Prepared Statement là gì?"
            ],
            "labs": [
                "<strong>Mức Cơ bản (Bắt buộc - Bài 9.1 & 9.2):</strong> Tạo <code>config.php</code> kết nối CSDL <code>bookdb</code> / <code>moviedb</code>; hiển thị danh sách 10 cuốn sách/bộ phim ra giao diện thẻ HTML và tạo Form tìm kiếm theo tên dùng <code>LIKE</code> + Prepared Statement.",
                "<strong>Mức Nâng cao (Bài 9.3 & 9.4):</strong> Tạo Form thêm sách mới (có tải ảnh bìa lên thư mục <code>uploads/</code> bằng <code>move_uploaded_file</code>) và làm chức năng phân trang 10 sản phẩm/trang bằng <code>LIMIT</code> & tham số <code>?page=</code>.",
                "<strong>Mức Thử thách (Hoàn thiện Đồ án & Luyện đề thi cuối kỳ):</strong> Hoàn tất 100% Ebook Chương 1-5, hoàn thành Quiz Buổi 9 (18 câu) và làm <strong>Đề kiểm tra tổng hợp / Thi thử cuối kỳ (40 câu - 60 phút)</strong> trên LMS."
            ]
        }
    }
]


def render_html(s):
    objs_html = "\n".join(f"      <li>{o}</li>" for o in s["objectives"])
    roadmap_html = "\n".join(
        f"""      <div class="timeline-item">
        <div class="time-badge">{part}</div>
        <div class="timeline-content">
          <p>{desc}</p>
        </div>
      </div>"""
        for part, desc in s["roadmap"]
    )
    theory_html = "\n".join(f"        <li>{q}</li>" for q in s["homework"]["theory"])
    labs_html = "\n".join(f"        <li>{l}</li>" for l in s["homework"]["labs"])

    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Buổi {s['id']} - {s['title']} | ITS708 Lập trình Web</title>
<style>
  :root {{
    --bg: #faf8f5;
    --surface: #ffffff;
    --ink: #1a1612;
    --ink-light: #4a453e;
    --accent: #b83b2b;
    --teal: #1a6b5c;
    --blue: #1e4d8c;
    --gold: #a67608;
    --border: #e5dfd6;
    --radius: 10px;
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    background: var(--bg);
    color: var(--ink);
    line-height: 1.7;
    font-size: 16px;
  }}
  .hero {{
    background: linear-gradient(135deg, #16213e 0%, #1a1a2e 60%, #0f3460 100%);
    color: #fff;
    padding: 2.8rem 2rem 2.4rem;
  }}
  .hero-inner {{ max-width: 900px; margin: 0 auto; }}
  .hero-badge {{
    display: inline-block;
    background: var(--accent);
    color: #fff;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 4px;
    margin-bottom: 1rem;
  }}
  .hero h1 {{ font-size: 2rem; font-weight: 800; line-height: 1.25; margin-bottom: 0.6rem; }}
  .hero-sub {{ font-size: 1rem; color: rgba(255,255,255,0.82); }}
  .container {{ max-width: 900px; margin: 0 auto; padding: 2rem 1.5rem 3.5rem; }}
  h2 {{
    font-size: 1.45rem;
    font-weight: 700;
    color: var(--ink);
    margin: 2rem 0 1rem;
    padding-bottom: 0.4rem;
    border-bottom: 2px solid var(--border);
  }}
  h3 {{ font-size: 1.15rem; font-weight: 700; color: var(--blue); margin: 1rem 0 0.5rem; }}
  .card {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.4rem 1.6rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  }}
  .card ul, .card ol {{ padding-left: 1.3rem; color: var(--ink-light); }}
  .card li {{ margin-bottom: 0.55rem; }}
  .meta-bar {{
    background: #eef4ff;
    border-left: 4px solid var(--blue);
    padding: 0.85rem 1.1rem;
    border-radius: 6px;
    margin-bottom: 1rem;
    font-size: 0.92rem;
  }}
  .scqa-grid {{ display: grid; gap: 0.8rem; }}
  .scqa-box {{
    padding: 0.9rem 1.1rem;
    border-radius: 8px;
    background: var(--surface);
    border-left: 4px solid var(--teal);
  }}
  .scqa-box.c {{ border-left-color: var(--accent); }}
  .scqa-box.q {{ border-left-color: var(--blue); }}
  .scqa-box.a {{ border-left-color: var(--gold); }}
  .timeline-item {{
    padding: 0.9rem 0;
    border-bottom: 1px dashed var(--border);
  }}
  .timeline-item:last-child {{ border-bottom: none; }}
  .time-badge {{
    display: inline-block;
    font-weight: 700;
    color: var(--accent);
    margin-bottom: 0.25rem;
  }}
  code {{
    background: #f1ece4;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: Consolas, monospace;
    font-size: 0.9em;
    color: #9a2a1a;
  }}
</style>
</head>
<body>
<header class="hero">
  <div class="hero-inner">
    <div class="hero-badge">ITS708 - {s['chapter']} · Buổi {s['id']}/9</div>
    <h1>Buổi {s['id']}: {s['title']}</h1>
    <p class="hero-sub">{s['clo']}</p>
  </div>
</header>

<div class="container">

  <h2>🎯 Mục tiêu buổi học</h2>
  <div class="card">
    <div class="meta-bar">
      <strong>📌 Trọng số Đề thi &amp; Ngân hàng câu hỏi:</strong> {s['exam_weight']}<br>
      <strong>🎓 Chuẩn đầu ra (CLO):</strong> {s['clo']}
    </div>
    <ol>
{objs_html}
    </ol>
  </div>

  <h2>💡 Khung tư duy SCQA &amp; Tình huống thực tế</h2>
  <div class="card">
    <div class="scqa-grid">
      <div class="scqa-box s"><strong>Situation (Bối cảnh):</strong> {s['scqa']['s']}</div>
      <div class="scqa-box c"><strong>Complication (Vấn đề thực tế):</strong> {s['scqa']['c']}</div>
      <div class="scqa-box q"><strong>Question (Câu hỏi trọng tâm):</strong> {s['scqa']['q']}</div>
      <div class="scqa-box a"><strong>Answer (Giải pháp kỹ thuật):</strong> {s['scqa']['a']}</div>
    </div>
  </div>

  <h2>🗺️ Lộ trình buổi học (Mô hình 30% Đề cương - 70% Thực chiến)</h2>
  <div class="card">
{roadmap_html}
  </div>

  <h2>🏠 Bài tập về nhà &amp; Thực hành</h2>
  <div class="card">
    <h3>Phần A - Câu hỏi ôn tập lý thuyết (Bám sát Giáo trình &amp; Đề cương)</h3>
    <ul>
{theory_html}
    </ul>
    <h3>Phần B - Bài tập thực hành Lab 3 mức độ (Cơ bản - Nâng cao - Đồ án TMĐT)</h3>
    <ul>
{labs_html}
    </ul>
  </div>

</div>
</body>
</html>
"""


def main():
    for s in SESSIONS_DATA:
        padded = f"{s['id']:02d}"
        out_file = LESSONS_DIR / f"Buoi_{padded}.html"
        html_str = render_html(s)
        assert "\u2014" not in html_str, f"Found em-dash in Buoi_{padded}.html"
        out_file.write_text(html_str, encoding="utf-8")
        print(f"Wrote {out_file.name} ({len(html_str)} chars)")


if __name__ == "__main__":
    main()
