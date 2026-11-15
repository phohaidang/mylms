# 📘 SOP: QUY CHUẨN CẤU TRÚC VÀ BIÊN SOẠN HỌC LIỆU LMS HUB
> **Dành cho AI Assistant / Autonomous Agent / Đội ngũ Giảng dạy**  
> *Phiên bản:* 2.0 (Chuẩn hóa Multi-Course Shared-Core Architecture)  
> *Mục đích:* Hướng dẫn toàn diện cho công cụ AI hiểu rõ cấu trúc hệ thống LMS, phân loại học liệu, phương pháp biên soạn chuẩn sư phạm và schema kỹ thuật bắt buộc để tự động tạo học liệu không xảy ra lỗi.

---

## 🎯 1. NGUYÊN TẮC CỐT LÕI (CORE PRINCIPLES)

1. **Đề Cương Chi Tiết (`de_cuong.md`) là Hiến Pháp (Single Source of Truth):**
   - Mọi học liệu (Ebook, Lesson HTML, Quiz, Exam, Slide, Exercise) đều phải bắt nguồn từ Đề cương môn học.
   - Tuyệt đối tuân thủ: Chuẩn đầu ra (CLO), Tỷ lệ cấp độ nhận thức theo Bloom's Taxonomy, Ma trận đề thi, Thời lượng phân bổ từng buổi.
2. **Kiến trúc 3 Tầng (Shared Core Architecture):**
   - **Tầng 1 - `core/`**: Mã nguồn dùng chung (Server Express API, Frontend SPA Vanilla JS, Sync Scripts). *AI không sửa đổi khi chỉ thêm môn học.*
   - **Tầng 2 - `courses/{course-slug}/`**: Định nghĩa môn học và kho học liệu chuẩn (`content/`). *Đây là không gian làm việc chính của quy trình này.*
   - **Tầng 3 - `courses/{course-slug}/{class-id}/`**: Triển khai theo lớp thực tế (Database Google Sheets, Danh sách sinh viên `roster.md`, Vercel deployment).
3. **Phân tách Học liệu (Student vs. Teacher View):**
   - Sinh viên học tương tác qua Ebook SCQA, Mục tiêu buổi học, Lab thực hành và Quiz online.
   - Kịch bản giảng dạy chi tiết theo timeline, bảng câu hỏi dẫn dắt và đáp án tuyệt đối chỉ hiển thị cho Giảng viên (Admin).

---

## 🗺️ 2. BẢN ĐỒ THƯ MỤC HỌC LIỆU MÔN HỌC (DIRECTORY MAP)

Tất cả học liệu của một môn học nằm trọn vẹn trong thư mục `courses/{course-slug}/`:

```text
05-Projects/lms-hub/courses/{course-slug}/
├── course-config.json              # [BẮT BUỘC] Trục xương sống: metadata và danh sách buổi học
├── syllabus.md                     # Đề cương chi tiết định dạng Markdown
├── build_ebook_json.py             # Script tự động parse Markdown sang chapter-N.json
├── build_question_bank.py          # Script tự động parse test_bank.md sang bank.json & session-N.json
└── content/                        # [BẮT BUỘC] Thư mục chứa toàn bộ dữ liệu runtime của LMS
    ├── ebook/                      # Ebook SCQA 3 cấp độ tương tác
    │   ├── chapter-1.json
    │   ├── chapter-2.json
    │   └── ...
    ├── questions/                  # Ngân hàng trắc nghiệm & Quiz từng buổi
    │   ├── bank.json               # Toàn bộ câu hỏi môn học
    │   ├── session-1.json          # Quiz 10-15 câu cho Buổi 1
    │   ├── session-2.json          # Quiz 10-15 câu cho Buổi 2
    │   └── ...
    ├── lessons/                    # Giáo án HTML hiển thị trên web
    │   ├── Buoi_01.html            # Đánh số 2 chữ số: Buoi_01, Buoi_02...
    │   ├── Buoi_02.html
    │   └── ...
    ├── exams/                      # Đề thi chính thức (Strict Mode, 4 mã đề)
    │   ├── midterm-1.json          # Bài kiểm tra quá trình / giữa kỳ
    │   └── final.json              # Đề thi kết thúc môn (nếu có)
    ├── slides/                     # Slide bài giảng định dạng PDF
    │   ├── Buoi_01.pdf
    │   └── ...
    └── images/                     # Hình ảnh, sơ đồ minh họa đính kèm
```

---

## 📋 3. DANH MỤC HỌC LIỆU & SCHEMA KỸ THUẬT CHUẨN

---

### 3.1. Trục Xương Sống: `course-config.json`
- **Đường dẫn**: `courses/{course-slug}/course-config.json`
- **Mục đích**: Backend nạp vào `app.locals.courseConfig` để điều phối toàn bộ routes (`/api/courses/sessions`, `/api/ebook/chapters`,...).
- **Quy tắc kỹ thuật**:
  - `sessions[].id`: Số nguyên liên tục từ `1` đến `N`.
  - `sessions[].chapter`: Bắt buộc theo định dạng `"Ch.1"`, `"Ch.2"`,... (Frontend dùng Regex `session.chapter.match(/Ch\.(\d+)/i)` để liên kết với Ebook Chapter tương ứng).
  - Nếu buổi học có kỳ thi: thêm `"hasExam": true, "examId": "midterm-1"`.

```json
{
  "meta": {
    "code": "ITS708",
    "name": "Lập trình Web",
    "total_sessions": 9,
    "chapters": 5,
    "university": "ĐH Ngân Hàng TP.HCM",
    "textbook": "PHP and MySQL: server – side web development — Jon Duckett"
  },
  "sessions": [
    {
      "id": 1,
      "chapter": "Ch.1",
      "title": "Bức tranh toàn cảnh & Giao diện tĩnh",
      "topics": "Mô hình Client-Server, Web tĩnh/động, HTML, CSS",
      "clo": "CLO1",
      "textbook": "Ch.1 Duckett",
      "duration": "5 tiết (250 phút)"
    },
    {
      "id": 9,
      "chapter": "Ch.5",
      "title": "Kết nối CSDL & Thực hành tổng hợp",
      "topics": "Kết nối PHP & MySQL, lấy dữ liệu động",
      "clo": "CLO1, CLO2",
      "textbook": "Ch.9,12,13 Duckett",
      "duration": "5 tiết (250 phút)",
      "hasExam": true,
      "examId": "midterm-1"
    }
  ]
}
```

---

### 3.2. Ebook Tương Tác SCQA: `content/ebook/chapter-{N}.json`
- **Đường dẫn**: `courses/{course-slug}/content/ebook/chapter-1.json`, `chapter-2.json`,...
- **Mục đích**: Cung cấp tài liệu đọc tương tác theo từng Khái niệm (`concepts`), hỗ trợ sinh viên tự kiểm tra năng lực qua **Vòng Test 3 cấp bậc (Bloom's Levels)**.
- **Phương pháp biên soạn nội dung**:
  1. **Khung tư duy SCQA**:
     - `situation` (Thực trạng quen thuộc với SV): Neo vào kinh nghiệm đời thực.
     - `complication` (Biến cố/Nghịch lý): Gây tò mò, nhận thức khoảng trống tri thức.
     - `question` (Câu hỏi tự nhiên): Câu hỏi SV tự bật ra trong đầu.
     - `answer` (Hook mở đầu): 1 câu trả lời ngắn gọn, toàn bộ chương học sẽ chứng minh câu này.
  2. **Khái niệm (`concepts`)**:
     - Chia nhỏ kiến thức thành từng đơn vị (Atomic).
     - Định nghĩa ngắn gọn, chuẩn xác.
     - `key_points`: 2-5 điểm then chốt (cho phép chèn thẻ HTML: `<strong>`, `<code>`, `<pre>`, `<table>`).
  3. **Vòng Test 3 Cấp Bậc (`tests`)**:
     - **Level 1 (Nhớ - Remember)**: 4-5 câu trắc nghiệm kiểm tra định nghĩa, thuật ngữ cốt lõi.
     - **Level 2 (Hiểu - Understand)**: 4-5 câu trắc nghiệm phân biệt, so sánh cơ chế hoạt động.
     - **Level 3 (Vận dụng - Apply)**: 3-4 câu trắc nghiệm tình huống/code + 1 câu tự luận (`essay`) có kèm barem/rubric chấm điểm chi tiết.

```json
{
  "chapter": 1,
  "title": "Tổng quan về lập trình web",
  "sessions": [1],
  "scqa": {
    "situation": "Mỗi ngày bạn mở Shopee, Facebook hay Google hàng chục lần — chỉ cần chạm vào màn hình là trang web hiện ra.",
    "complication": "Phía sau cú chạm đó là cả một chuỗi trao đổi dữ liệu phức tạp. Nếu không hiểu cơ chế này, bạn chỉ là người dùng, không thể tạo ra hệ thống.",
    "question": "Trang web thực sự hoạt động như thế nào và lập trình viên cần làm những gì?",
    "answer": "Website hoạt động theo mô hình Client - Server qua HTTP/HTTPS, kết hợp giao diện HTML/CSS và xử lý back-end."
  },
  "concepts": [
    {
      "id": "c1-mo-hinh-client-server",
      "term": "Mô hình khách – chủ (Client – Server)",
      "definition": "Mô hình mạng phân tán trong đó các máy khách (Client) gửi yêu cầu và máy chủ (Server) tiếp nhận, xử lý rồi phản hồi kết quả.",
      "key_points": [
        "Quy trình 4 bước: Request -> Processing -> DB Query -> Response.",
        "Giao thức vận hành chính: <strong>HTTP / HTTPS</strong>.",
        "Web browser là một Web Client, không phải Web Server."
      ],
      "case_study": null,
      "related_concepts": ["c1-web-client", "c1-web-server"]
    }
  ],
  "tests": {
    "level_1": {
      "name": "🎯 Level 1: Khái niệm cốt lõi",
      "description": "Nhận biết kiến thức nền tảng của chương.",
      "bloom_level": "Remember",
      "questions": [
        {
          "id": "L1-c1-q1",
          "type": "mc",
          "concept_ref": "c1-mo-hinh-client-server",
          "question": "Trong mô hình Client-Server, thiết bị nào đóng vai trò gửi yêu cầu?",
          "options": ["A. Web Server", "B. Web Browser (Client)", "C. Database Server", "D. Switch mạng"],
          "correct": "B"
        }
      ]
    },
    "level_2": {
      "name": "📝 Level 2: Hiểu và giải thích",
      "description": "Phân biệt và so sánh các khái niệm.",
      "bloom_level": "Understand",
      "questions": [
        {
          "id": "L2-c1-q1",
          "type": "mc",
          "concept_ref": "c1-mo-hinh-client-server",
          "question": "Điểm khác biệt căn bản giữa Website tĩnh và Website động là gì?",
          "options": [
            "A. Website tĩnh không có hình ảnh",
            "B. Website động tạo nội dung theo thời gian thực nhờ xử lý máy chủ và CSDL",
            "C. Website tĩnh bắt buộc phải dùng PHP",
            "D. Website động chạy nhanh hơn website tĩnh"
          ],
          "correct": "B"
        }
      ]
    },
    "level_3": {
      "name": "🚀 Level 3: Vận dụng",
      "description": "Áp dụng kiến thức vào bài toán thực tế.",
      "bloom_level": "Apply",
      "questions": [
        {
          "id": "L3-c1-q1",
          "type": "mc",
          "concept_ref": "c1-mo-hinh-client-server",
          "question": "Khi người dùng gõ URL sai và nhận mã lỗi 404, tầng nào đã phát sinh phản hồi này?",
          "options": ["A. Trình duyệt client tự sinh", "B. Web Server phản hồi tài nguyên không tồn tại", "C. Nhà mạng viễn thông chặn", "D. Hệ điều hành máy tính"],
          "correct": "B"
        },
        {
          "id": "L3-c1-essay1",
          "type": "essay",
          "concept_ref": "c1-mo-hinh-client-server",
          "question": "Vẽ và giải thích quy trình 4 bước khi một sinh viên truy cập xem kết quả học tập trên website nhà trường.",
          "rubric": "Vẽ đúng sơ đồ luồng (30%) · Nêu đúng vai trò Client/Server (30%) · Đề cập truy vấn DB (20%) · Trình bày logic (20%)",
          "max_words": 300
        }
      ]
    }
  }
}
```

---

### 3.3. Câu Hỏi Trắc Nghiệm & Quiz Buổi: `content/questions/`
- **Đường dẫn**:
  - `content/questions/bank.json`: Toàn bộ ngân hàng câu hỏi.
  - `content/questions/session-{id}.json`: Đề trắc nghiệm 10 câu cho từng buổi học (`session-1.json`, `session-2.json`,...).
- **Quy tắc phân bổ câu hỏi Quiz Buổi**:
  - Số lượng: **10 câu** trắc nghiệm 4 lựa chọn (A, B, C, D).
  - Thời gian làm bài: `time_limit_minutes: 15`.
  - Cơ cấu Bloom: **4 câu Mức 1 (Nhớ)** : **4 câu Mức 2 (Hiểu)** : **2 câu Mức 3 (Vận dụng)**.
  - Backend tự động xáo trộn ngẫu nhiên thứ tự lựa chọn khi trả về cho sinh viên (anti-cheat).
- **Schema `session-{id}.json`**:

```json
{
  "session": 1,
  "chapter": "Ch.1",
  "title": "Bức tranh toàn cảnh & Giao diện tĩnh",
  "time_limit_minutes": 15,
  "questions": [
    {
      "id": "ltweb-q004",
      "type": "mc",
      "question": "Trong cấu trúc URL đầy đủ, thành phần host dùng để xác định nội dung nào?",
      "options": [
        "A. Máy chủ lưu trữ tài nguyên cần truy cập",
        "B. Giao thức truyền dữ liệu trên Internet",
        "C. Chuỗi tham số truy vấn gửi kèm",
        "D. Đường dẫn vị trí tệp tin trên đĩa cứng máy chủ"
      ],
      "correct": "A"
    }
  ]
}
```

- **Schema `bank.json`**:
```json
[
  {
    "id": "ltweb-q001",
    "chapter": 1,
    "level": 1,
    "session": 1,
    "type": "mc",
    "question": "URL là viết tắt của cụm từ nào?",
    "options": [
      "A. Universal Real Location",
      "B. Uniform Resource Locator",
      "C. Unique Resource Link",
      "D. Unified Reference Locator"
    ],
    "correct": "B"
  }
]
```

---

### 3.4. Giáo Án Buổi Học HTML: `content/lessons/Buoi_{XX}.html`
- **Đường dẫn**: `courses/{course-slug}/content/lessons/Buoi_01.html` (chú ý: số thứ tự buổi phải đệm số 0 thành 2 chữ số: `01`, `02`,...).
- **CƠ CHẾ PARSING QUAN TRỌNG CỦA LMS HUB (Phải tuân thủ 100%)**:
  Khi sinh viên truy cập xem bài giảng trên LMS (`core/client/src/pages/lesson.js`):
  1. Frontend thực hiện `fetch('/lessons/Buoi_01.html')` và dùng `DOMParser` để bóc tách:
     - Thẻ tiêu đề (`h1, h2, h3, h4, .section-label`) chứa từ khóa **`Mục tiêu`** → Trích xuất toàn bộ nội dung con đưa vào ô **🎯 Mục tiêu buổi học**.
     - Thẻ tiêu đề chứa từ khóa **`SCQA`** → Trích xuất đưa vào ô **Khung SCQA Buổi Học**.
     - Thẻ tiêu đề chứa từ khóa **`Bài tập về nhà`** hoặc **`BTVN`** → Trích xuất đưa vào ô **📝 Bài tập về nhà & Lab**.
     - Tự động ẩn toàn bộ Kịch bản chi tiết và Bảng câu hỏi của giảng viên.
  2. Khi Giảng viên truy cập: Hệ thống nhúng toàn bộ file HTML vào iframe để giảng viên theo dõi tiến trình và speaker notes.
- **Cấu trúc 8 phần chuẩn của tài liệu HTML**:

```html
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Buổi 1 — Tổng quan Lập trình Web</title>
  <style>
    /* CSS nhúng cục bộ: Serif/Academic styling, biến CSS, responsive layout */
    body { font-family: 'Source Serif 4', Georgia, serif; line-height: 1.7; color: #1b1714; background: #fdfaf6; }
    .container { max-width: 900px; margin: 0 auto; padding: 40px 20px; }
    .section-title { color: #8b2500; border-bottom: 2px solid #e0d7cb; padding-bottom: 8px; margin-top: 32px; }
    .timeline-table { width: 100%; border-collapse: collapse; margin: 16px 0; }
    .timeline-table th, .timeline-table td { border: 1px solid #d5cbbd; padding: 10px; text-align: left; }
    .timeline-table th { background: #f0e8dc; }
    .badge { display: inline-block; padding: 3px 8px; border-radius: 4px; font-size: 0.85rem; background: #e0d7cb; }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <span class="badge">Môn học: Lập trình Web</span>
      <h1>Buổi 1: Bức tranh toàn cảnh & Giao diện tĩnh</h1>
    </header>

    <!-- PHẦN I: BẮT BUỘC CHỨA TỪ KHÓA 'Mục tiêu' ĐỂ LMS EXTRACT CHO SV -->
    <h2 class="section-title">I. Mục tiêu buổi học</h2>
    <ul>
      <li>Hiểu rõ mô hình trao đổi dữ liệu Client - Server (CLO1).</li>
      <li>Phân tích được các thành phần cấu tạo URL (CLO1).</li>
      <li>Dựng được trang web HTML tĩnh đầu tiên có áp dụng CSS (CLO2).</li>
    </ul>

    <!-- PHẦN II: BẮT BUỘC CHỨA TỪ KHÓA 'SCQA' ĐỂ LMS EXTRACT CHO SV -->
    <h2 class="section-title">II. Khung SCQA của buổi</h2>
    <p><strong>Situation:</strong> Hàng ngày chúng ta truy cập hàng chục website tin tức, mua sắm.</p>
    <p><strong>Complication:</strong> Dữ liệu được gửi và nhận qua cơ chế nào mà hàng triệu người không bị nhầm lẫn giỏ hàng của nhau?</p>
    <p><strong>Question:</strong> Làm thế nào để máy chủ nhận diện và trả kết quả chính xác cho từng người?</p>
    <p><strong>Answer-preview:</strong> Thông qua giao thức HTTP/HTTPS và định danh URL chuẩn xác.</p>

    <!-- PHẦN III & IV: KỊCH BẢN DẠY (CHỈ DÀNH CHO GIẢNG VIÊN - LMS TỰ ẨN VỚI SV) -->
    <h2 class="section-title">III. Khởi động từ Cái Biết của SV (15 phút)</h2>
    <p>Đặt câu hỏi gợi mở về trải nghiệm đặt hàng Shopee...</p>

    <h2 class="section-title">IV. Kịch bản chi tiết theo timeline</h2>
    <table class="timeline-table">
      <thead>
        <tr><th>Thời gian</th><th>Hoạt động Giảng viên</th><th>Hoạt động Sinh viên</th><th>Học liệu</th></tr>
      </thead>
      <tbody>
        <tr><td>00 - 45'</td><td>Thuyết giảng Client-Server & HTTP</td><td>Lắng nghe, ghi chú, trả lời câu hỏi</td><td>Slide 1-15</td></tr>
        <tr><td>46 - 90'</td><td>Demo dựng trang HTML & Live Server</td><td>Code-along theo giảng viên</td><td>VS Code, index.html</td></tr>
      </tbody>
    </table>

    <h2 class="section-title">V. Bảng câu hỏi thảo luận</h2>
    <ol>
      <li>Nếu máy chủ tắt dịch vụ Apache thì trình duyệt báo lỗi gì?</li>
      <li>Tại sao cổng 80 và 443 không cần gõ trên thanh địa chỉ URL?</li>
    </ol>

    <!-- PHẦN VI: BẮT BUỘC CHỨA TỪ KHÓA 'Bài tập về nhà' ĐỂ LMS EXTRACT CHO SV -->
    <h2 class="section-title">VI. Bài tập về nhà & Lab thực hành</h2>
    <div class="homework-box">
      <h3>Lab 1: Trang Profile Cá Nhân (Bắt buộc)</h3>
      <p>Tạo file <code>index.html</code> giới thiệu bản thân có đủ ảnh đại diện, danh sách sở thích và bảng thông tin học tập có định dạng CSS.</p>
    </div>

    <h2 class="section-title">VII. Câu hỏi ôn tập củng cố cuối buổi</h2>
    <p>(3-5 câu trắc nghiệm nhanh kiểm tra mức độ tiếp thu)</p>

    <h2 class="section-title">VIII. Lưu ý và Tình huống dự phòng cho Giảng viên</h2>
    <ul>
      <li>Nếu mạng phòng lab chập chờn: Yêu cầu SV sử dụng Live Server cục bộ trên VS Code.</li>
    </ul>
  </div>
</body>
</html>
```

---

### 3.5. Đề Thi Chính Thức: `content/exams/{examId}.json`
- **Đường dẫn**: `courses/{course-slug}/content/exams/midterm-1.json`
- **Tính năng trên LMS**:
  - `strict_mode: true`: Giám sát toàn màn hình, chống chuyển tab, cảnh báo gian lận.
  - Phân chia `variants` (Mã đề 1, 2, 3, 4): Hệ thống phát ngẫu nhiên mã đề cho từng sinh viên, tự động xáo trộn câu hỏi và đáp án bằng giải thuật Fisher-Yates.
  - Hỗ trợ Giảng viên xuất đề thi và Answer Key ra file Word `.docx` chỉ bằng 1 click.
- **Schema `midterm-1.json`**:

```json
{
  "exam_id": "midterm-1",
  "title": "Kiểm tra Quá trình 1 — Trắc nghiệm",
  "scope": "Chương 1 đến Chương 3 (Buổi 1–5)",
  "session": 6,
  "weight": "20%",
  "time_limit_minutes": 30,
  "instructions": "Trắc nghiệm khách quan, cá nhân, không sử dụng tài liệu. Mỗi câu chỉ có 1 đáp án đúng duy nhất.",
  "strict_mode": true,
  "variants": [
    {
      "variant_id": 1,
      "questions": [
        {
          "id": "mt1-q1",
          "type": "mc",
          "question": "Thành phần nào sau đây tiếp nhận và phản hồi HTTP Request của người dùng?",
          "options": ["A. Web Browser", "B. Web Server", "C. Router", "D. Switch"],
          "correct": "B"
        }
      ]
    },
    {
      "variant_id": 2,
      "questions": [
        {
          "id": "mt1-q1",
          "type": "mc",
          "question": "Giao thức nào truyền tải siêu văn bản có mã hóa an toàn trên Internet?",
          "options": ["A. HTTP", "B. FTP", "C. HTTPS", "D. SMTP"],
          "correct": "C"
        }
      ]
    }
  ]
}
```

---

### 3.6. Slide Bài Giảng: `content/slides/Buoi_{XX}.pdf`
- **Đường dẫn**: `courses/{course-slug}/content/slides/Buoi_01.pdf`
- **Cơ chế**:
  - Được bảo mật qua endpoint `/api/courses/sessions/:id/slide` (yêu cầu JWT Token).
  - Phía sinh viên có cơ chế Gating: Sinh viên cần hoàn thành khảo sát phản hồi buổi học (Session Feedback) thì hệ thống mới kích hoạt nút tải Slide.

---

## ⚙️ 4. PIPELINE TỰ ĐỘNG HÓA VÀ SCRIPTS HỖ TRỢ (AUTOMATION PIPELINE)

Để chuyển đổi nhanh từ nội dung thô dạng Markdown (`04-output/teaching/{Course}/`) sang dữ liệu JSON chuẩn của LMS, AI hãy sử dụng hoặc tạo 2 script Python tiêu chuẩn đặt ngay tại thư mục môn học:

### 4.1. Script `build_question_bank.py`
Tự động chuyển bảng Markdown `test_bank.md` (9 cột) thành `bank.json` và phân bổ thành `session-1.json`, `session-2.json`:
- Đọc bảng: `| STT | Câu hỏi | Lựa chọn 1 | Lựa chọn 2 | Lựa chọn 3 | Lựa chọn 4 | Đáp án đúng | Mức độ | Chương |`
- Lọc theo buổi/chương, bốc thăm đúng tỷ lệ 4 Nhớ : 4 Hiểu : 2 Vận dụng cho mỗi buổi.

### 4.2. Script `build_ebook_json.py`
Tự động bóc tách các file Markdown chương (`chuong_1_*.md`...):
- Bóc tách block SCQA: `**Situation**: ...`, `**Complication**: ...`
- Bóc tách từng Section `## 1.1...` thành các `concepts` (`id`, `term`, `definition`, `key_points`).
- Tự động nhặt câu hỏi từ `bank.json` theo độ tương đồng ngữ nghĩa (keyword matching) đưa vào 3 Level Test tương ứng.
- Xuất thành `courses/{course}/content/ebook/chapter-N.json`.

---

## 🔄 5. QUY TRÌNH TRIỂN KHAI VÀ ĐỒNG BỘ (SYNC & DEPLOY WORKFLOW)

Sau khi AI tạo đầy đủ học liệu trong thư mục `courses/{course-slug}/content/`, quy trình đồng bộ bắt buộc như sau:

```bash
# Bước 1: Đứng tại thư mục gốc lms-hub
cd d:/PARA/Projects/second-brain/05-Projects/lms-hub

# Bước 2: Đồng bộ học liệu từ course sang các lớp học cụ thể
# Cú pháp: npm run sync -- <course-slug> <class-id>
npm run sync -- ltweb D01

# (Hoặc đồng bộ toàn bộ tất cả các môn/lớp trong hệ thống)
npm run sync:all

# Bước 3: Kiểm tra thử nghiệm tại Local
cd courses/ltweb/D01
# Chạy Terminal 1: npm run server (Backend port 3010)
# Chạy Terminal 2: npm run client (Vite Dev port 5173)

# Bước 4: Đẩy lên GitHub để Vercel tự động build & deploy
git add .
git commit -m "feat: complete LMS course content for ltweb"
git push origin main
```

---

## ✅ 6. CHECKLIST KIỂM ĐỊNH CHẤT LƯỢNG CHO AI (QUALITY ASSURANCE CHECKLIST)

Trước khi xác nhận hoàn tất việc khởi tạo hoặc cập nhật học liệu, AI phải tự kiểm tra các tiêu chí sau:

- [ ] **Encoding**: Tất cả file JSON, HTML, Markdown đều lưu ở định dạng **UTF-8 không BOM**.
- [ ] **Tính hợp lệ JSON**: Mọi file `.json` đều parse được qua `JSON.parse()`, không có dấu phẩy thừa ở cuối (trailing commas), không có ký tự điều khiển unescaped.
- [ ] **Quy chuẩn đặt tên (Naming Conventions)**:
  - File buổi học: Bắt buộc đệm 2 chữ số: `Buoi_01.html`, `Buoi_01.pdf`.
  - File quiz: `session-1.json`, `session-2.json` (không đệm số 0).
  - File ebook: `chapter-1.json`, `chapter-2.json`.
- [ ] **Liên kết Session - Chapter**: Giá trị `chapter` trong `course-config.json` (vd: `"Ch.1"`) khớp chính xác với số thứ tự trong file `chapter-1.json`.
- [ ] **Từ khóa trích xuất trong HTML**: Trong file `Buoi_XX.html` bắt buộc phải có ít nhất 3 tiêu đề chứa các từ khóa:
  - `Mục tiêu` (cho phần mục tiêu buổi học)
  - `SCQA` (cho phần tình huống dẫn nhập)
  - `Bài tập về nhà` hoặc `BTVN` (cho phần bài tập)
- [ ] **Chất lượng đề trắc nghiệm**:
  - Mỗi câu hỏi luôn có đủ 4 lựa chọn bắt đầu bằng `A. `, `B. `, `C. `, `D. `.
  - Đáp án đúng `correct` chỉ là một chữ cái in hoa: `"A"`, `"B"`, `"C"` hoặc `"D"`.
  - Không để lộ đáp án trong phần văn bản câu hỏi.
- [ ] **An toàn mã nguồn**: Không sửa đổi mã trong thư mục `_sync/` (thư mục này được sinh tự động bởi script `sync-deploy.js`). Mọi điều chỉnh học liệu chỉ thực hiện tại `courses/{course-slug}/content/`.
