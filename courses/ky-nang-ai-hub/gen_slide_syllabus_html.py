# -*- coding: utf-8 -*-
"""
Tạo bản HTML Slide Deck tương tác (18 slides, điều hướng bằng phím mũi tên Trái/Phải, Phím Space, Fullscreen F)
cho Slide 00: Giới thiệu Đề cương, Lộ trình 11 buổi & Chiến lược Đánh giá Cuối khóa (100%)
"""
import os

html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Slide 00: Đề cương, Lộ trình 11 Buổi & Chiến lược Đánh giá — HUB</title>
  <style>
    :root {
      --navy: #1B2558;
      --dark-navy: #111A40;
      --white: #FFFFFF;
      --off-white: #F5F6FA;
      --red: #C62828;
      --light-red: #FFEBEE;
      --accent: #1565C0;
      --light-accent: #E3F2FD;
      --gold: #F9A825;
      --green: #2E7D32;
      --light-green: #E8F5E9;
      --orange: #E65100;
      --light-orange: #FFF3E0;
      --text-dark: #212121;
      --text-mid: #424242;
      --text-light: #757575;
      --border: #E0E0E0;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: #0d122a;
      font-family: 'Calibri', 'Segoe UI', sans-serif;
      color: var(--text-dark);
      height: 100vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }
    .deck-viewport {
      width: 1280px;
      height: 720px;
      position: relative;
      background: var(--white);
      box-shadow: 0 20px 60px rgba(0,0,0,0.6);
      border-radius: 6px;
      overflow: hidden;
      transform-origin: center center;
    }
    .slide {
      width: 1280px;
      height: 720px;
      position: absolute;
      top: 0;
      left: 0;
      display: none;
      flex-direction: column;
      background: var(--white);
    }
    .slide.active { display: flex; }
    .slide.navy-bg {
      background: var(--navy);
      color: var(--white);
    }
    .gold-top-bar {
      width: 100%;
      height: 9px;
      background: var(--gold);
      flex-shrink: 0;
    }
    .header-bar {
      width: 100%;
      height: 68px;
      background: var(--navy);
      color: var(--white);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 56px;
      font-family: Georgia, serif;
      font-size: 16px;
      font-weight: 700;
      letter-spacing: 2px;
      text-transform: uppercase;
      flex-shrink: 0;
    }
    .footer-bar {
      width: 100%;
      height: 44px;
      background: var(--navy);
      color: #D0D5E8;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 56px;
      font-size: 13px;
      margin-top: auto;
      flex-shrink: 0;
    }
    .footer-bar .page-num {
      color: var(--gold);
      font-weight: 700;
      font-size: 14px;
    }
    .slide-body {
      padding: 22px 56px 18px;
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }
    h1.page-title {
      font-family: Georgia, serif;
      font-size: 27px;
      color: var(--red);
      font-weight: 700;
      margin-bottom: 14px;
      line-height: 1.25;
    }
    .grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      flex: 1;
    }
    .grid-3 {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 20px;
      flex: 1;
    }
    .grid-4 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      flex: 1;
    }
    .card {
      background: var(--off-white);
      border: 1px solid var(--border);
      border-radius: 6px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 3px 8px rgba(0,0,0,0.06);
    }
    .card-header {
      padding: 10px 16px;
      color: var(--white);
      font-weight: 700;
      font-size: 15px;
      text-align: center;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .card-content {
      padding: 14px 18px;
      font-size: 14.5px;
      line-height: 1.5;
      flex: 1;
    }
    .card-content ul {
      padding-left: 18px;
    }
    .card-content li {
      margin-bottom: 8px;
    }
    .left-card {
      background: var(--off-white);
      border: 1px solid var(--border);
      border-left: 8px solid var(--navy);
      border-radius: 4px;
      padding: 12px 16px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }
    .left-card h3 {
      font-size: 15.5px;
      margin-bottom: 6px;
      text-transform: uppercase;
    }
    .left-card ul {
      padding-left: 18px;
      font-size: 14px;
      line-height: 1.45;
    }
    .left-card li { margin-bottom: 5px; }
    .banner {
      padding: 12px 20px;
      border-radius: 6px;
      margin-bottom: 14px;
      font-size: 14.5px;
      line-height: 1.45;
      text-align: center;
      font-weight: 600;
    }
    table.acad-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13.5px;
    }
    table.acad-table th {
      background: var(--navy);
      color: var(--white);
      padding: 9px 12px;
      text-align: left;
      font-weight: 700;
    }
    table.acad-table td {
      padding: 8px 12px;
      border: 1px solid var(--border);
      vertical-align: middle;
      line-height: 1.4;
    }
    table.acad-table tr:nth-child(even) { background: var(--off-white); }
    .controls-bar {
      margin-top: 12px;
      display: flex;
      align-items: center;
      gap: 14px;
      color: #cbd5e1;
      font-size: 13px;
    }
    .controls-bar button {
      background: #1e293b;
      color: #f8fafc;
      border: 1px solid #475569;
      padding: 6px 14px;
      border-radius: 4px;
      cursor: pointer;
      font-weight: 600;
    }
    .controls-bar button:hover { background: #334155; }
  </style>
</head>
<body>

<div class="deck-viewport" id="viewport">

  <!-- SLIDE 1: TRANG BÌA -->
  <section class="slide navy-bg active">
    <div class="gold-top-bar"></div>
    <div style="padding: 48px 70px; text-align: center; flex: 1; display: flex; flex-direction: column; justify-content: center;">
      <div style="color: var(--gold); font-size: 18px; font-weight: 700; letter-spacing: 3px; margin-bottom: 8px;">
        TRƯỜNG ĐẠI HỌC NGÂN HÀNG TP. HỒ CHÍ MINH (HUB)
      </div>
      <div style="color: #CBD5E1; font-size: 15px; letter-spacing: 2px; margin-bottom: 22px;">
        CHƯƠNG TRÌNH ĐÀO TẠO CHỨNG CHỈ CHUẨN ĐẦU RA BẮT BUỘC ĐỂ TỐT NGHIỆP
      </div>
      <div style="width: 420px; height: 3px; background: var(--gold); margin: 0 auto 28px;"></div>
      <h1 style="font-family: Georgia, serif; font-size: 36px; line-height: 1.35; color: var(--white); margin-bottom: 18px;">
        ĐỀ CƯƠNG, LỘ TRÌNH &amp; CHIẾN LƯỢC ĐÁNH GIÁ<br>
        KỸ NĂNG ỨNG DỤNG AI TRONG HỌC TẬP VÀ NGHIÊN CỨU
      </h1>
      <div style="color: var(--gold); font-size: 19px; font-style: italic; margin-bottom: 36px;">
        Triết lý đào tạo: Tư duy &rarr; Kỹ năng &rarr; Công cụ &nbsp;|&nbsp; Phương pháp: Giảng dạy chứng nghiệm
      </div>
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; max-width: 960px; margin: 0 auto;">
        <div style="background: var(--dark-navy); border: 1.5px solid var(--gold); padding: 16px; border-radius: 6px;">
          <div style="color: var(--gold); font-weight: 700; font-size: 18px;">11 BUỔI (44 TIẾT)</div>
          <div style="font-size: 14px; color: #E2E8F0; margin-top: 4px;">4 tiết &times; 50 phút / buổi (200 phút)</div>
        </div>
        <div style="background: var(--dark-navy); border: 1.5px solid var(--gold); padding: 16px; border-radius: 6px;">
          <div style="color: var(--gold); font-weight: 700; font-size: 18px;">35% DEMO &ndash; 65% STUDIO</div>
          <div style="font-size: 14px; color: #E2E8F0; margin-top: 4px;">Thực hành va chạm &amp; Xây dựng Đề án</div>
        </div>
        <div style="background: var(--dark-navy); border: 1.5px solid var(--gold); padding: 16px; border-radius: 6px;">
          <div style="color: var(--gold); font-weight: 700; font-size: 18px;">100% ĐIỂM CUỐI KHÓA</div>
          <div style="font-size: 14px; color: #E2E8F0; margin-top: 4px;">Đề án 4 Mảnh ghép &amp; Kiểm toán chéo</div>
        </div>
      </div>
    </div>
    <div style="background: var(--dark-navy); padding: 18px 60px; text-align: center; font-size: 15px; color: #E2E8F0; border-top: 1px solid #2D3A7B;">
      <strong>Giảng viên biên soạn &amp; giảng dạy: ThS. Phó Hải Đăng</strong> &nbsp;|&nbsp; Khoa Hệ thống thông tin quản lý &nbsp;|&nbsp; Email: dangph@hub.edu.vn
    </div>
  </section>

  <!-- SLIDE 2: MỤC LỤC 5 PHẦN -->
  <section class="slide">
    <div class="header-bar"><span>TỔNG QUAN HỌC PHẦN</span><span>HUB_AI_CERT</span></div>
    <div class="slide-body">
      <h1 class="page-title">5 NỘI DUNG TRỌNG TÂM SINH VIÊN CẦN NẮM RÕ NGAY BUỔI 1</h1>
      <div style="display: flex; flex-direction: column; gap: 14px; flex: 1; justify-content: center;">
        <div style="display: flex; align-items: center; gap: 18px; background: var(--off-white); padding: 14px 20px; border-radius: 6px; border: 1px solid var(--border);">
          <div style="width: 48px; height: 48px; border-radius: 50%; background: var(--red); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 18px; flex-shrink: 0;">01</div>
          <div>
            <div style="font-size: 17px; font-weight: 700; color: var(--navy);">Tại sao cần môn học này &amp; Triết lý: Tư duy &rarr; Kỹ năng &rarr; Công cụ</div>
            <div style="font-size: 14px; color: var(--text-light);">Bằng chứng thực nghiệm về Hallucination (1/277 bài PubMed), hai cái bẫy nhận thức và 4 trụ cột năng lực</div>
          </div>
        </div>
        <div style="display: flex; align-items: center; gap: 18px; background: var(--off-white); padding: 14px 20px; border-radius: 6px; border: 1px solid var(--border);">
          <div style="width: 48px; height: 48px; border-radius: 50%; background: var(--navy); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 18px; flex-shrink: 0;">02</div>
          <div>
            <div style="font-size: 17px; font-weight: 700; color: var(--navy);">Chuẩn đầu ra (CLO1 &ndash; CLO5) &amp; Lộ trình 11 Buổi (44 Tiết) qua 4 Module</div>
            <div style="font-size: 14px; color: var(--text-light);">Bản đồ tiến trình từ Prompt-Context-Harness &rarr; Second Brain &rarr; NCKH &amp; Kiểm chứng &rarr; Đạo đức &amp; Pháp lý</div>
          </div>
        </div>
        <div style="display: flex; align-items: center; gap: 18px; background: var(--light-red); padding: 14px 20px; border-radius: 6px; border: 1.5px solid var(--red);">
          <div style="width: 48px; height: 48px; border-radius: 50%; background: var(--red); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 18px; flex-shrink: 0;">03</div>
          <div>
            <div style="font-size: 17px; font-weight: 700; color: var(--red);">Chiến lược Đánh giá Cuối khóa (100% Điểm): Mô hình 3 Cấu phần (40% &ndash; 30% &ndash; 30%)</div>
            <div style="font-size: 14px; color: var(--text-dark);">Không chấm điểm quá trình rời rạc: 40% Hồ sơ Đề án nhóm + 30% Cá nhân Second Brain + 30% Bảo vệ &amp; Kiểm toán chéo</div>
          </div>
        </div>
        <div style="display: flex; align-items: center; gap: 18px; background: var(--off-white); padding: 14px 20px; border-radius: 6px; border: 1px solid var(--border);">
          <div style="width: 48px; height: 48px; border-radius: 50%; background: var(--navy); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 18px; flex-shrink: 0;">04</div>
          <div>
            <div style="font-size: 17px; font-weight: 700; color: var(--navy);">Giải phẫu 4 Mảnh ghép Đề án, Kiểm toán chéo (Peer Audit) &amp; Điểm liệt Liêm chính</div>
            <div style="font-size: 14px; color: var(--text-light);">Cách tích lũy sản phẩm ngay tại lớp từ Buổi 1 đến Buổi 10, Rubric 7 tiêu chí và quy tắc loại bỏ 100% trích dẫn bịa</div>
          </div>
        </div>
        <div style="display: flex; align-items: center; gap: 18px; background: var(--off-white); padding: 14px 20px; border-radius: 6px; border: 1px solid var(--border);">
          <div style="width: 48px; height: 48px; border-radius: 50%; background: var(--navy); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 18px; flex-shrink: 0;">05</div>
          <div>
            <div style="font-size: 17px; font-weight: 700; color: var(--navy);">Quy tắc Vận hành Lớp học trên LMS Hub &amp; Điều kiện Bảo vệ Cuối khóa</div>
            <div style="font-size: 14px; color: var(--text-light);">Nhịp học 200 phút, điểm danh qua Feedback tải bài giảng, Quiz Active Recall 5 lượt &amp; Bộ 5 Biểu mẫu thực hành</div>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bar"><span>Trường ĐH Ngân hàng TP.HCM (HUB) | Kỹ năng ứng dụng AI trong học tập và nghiên cứu | ThS. Phó Hải Đăng</span><span class="page-num">2 / 18</span></div>
  </section>

  <!-- SLIDE 3: BỐI CẢNH & CÚ SỐC THỰC NGHIỆM -->
  <section class="slide">
    <div class="header-bar"><span>01. BỐI CẢNH &amp; TRIẾT LÝ ĐÀO TẠO</span><span>TẠI SAO KHÔNG DẠY "BẤM NÚT"?</span></div>
    <div class="slide-body">
      <h1 class="page-title">KHOẢNG CÁCH NGUY HIỂM KHI DÙNG AI MÀ THIẾU PHƯƠNG PHÁP</h1>
      <div class="grid-2">
        <div class="card" style="background: var(--light-red); border-color: var(--red);">
          <div class="card-header" style="background: var(--red);">BẰNG CHỨNG KHOA HỌC BÁO ĐỘNG (2025 &ndash; 2026)</div>
          <div class="card-content">
            <div style="font-family: Georgia, serif; font-size: 26px; font-weight: 700; color: var(--red); text-align: center; margin: 6px 0 14px;">
              1 / 277 bài báo trên PubMed dính trích dẫn bịa!
            </div>
            <ul>
              <li><strong>Topaz và cs. (The Lancet, 5/2026):</strong> Kiểm tra 2,5 triệu bài báo (97 triệu trích dẫn), tỷ lệ bài có tài liệu tham khảo bịa tăng gấp 10 lần từ <strong>1/2.828 (2023)</strong> lên <strong>1/277 (đầu 2026)</strong>.</li>
              <li><strong>Linardon và cs. (JMIR Ment Health, 2025):</strong> GPT-4o bịa hoàn toàn <strong>19,9%</strong> trích dẫn; tính cả sai thông tin thư mục là <strong>56,3% (99/176)</strong>.</li>
              <li><strong>Bịa nhiều nhất ở đề tài chuyên sâu:</strong> Tỷ lệ bịa vọt từ 6% lên <strong>28% &ndash; 29%</strong> ở các đề tài ít được nghiên cứu (đúng chỗ SV làm khóa luận cần nhất!).</li>
              <li><strong>Vụ GS. Jeff Hancock (ĐH Stanford, 1/2025):</strong> Bị tòa án bác bỏ toàn bộ bản khai chuyên gia vì lọt 2 trích dẫn do GPT-4o bịa.</li>
            </ul>
          </div>
        </div>
        <div class="card">
          <div class="card-header" style="background: var(--navy);">BA RỦI RO LỚN ĐỐI VỚI SINH VIÊN ĐẠI HỌC</div>
          <div class="card-content">
            <ul>
              <li><strong>1. Ảo tưởng trôi chảy (Fluency Illusion):</strong> Thấy AI xuất bài tiểu luận 1.500 chữ trong 30 giây rất mượt mà nên tưởng mình đã hiểu. Thực chất não bộ không có <em>ma sát nhận thức</em> nên quên 80% sau 24 giờ và đứng hình khi giảng viên hỏi vặn.</li>
              <li><strong>2. Lệ thuộc nhận thức (Cognitive Offloading):</strong> Giao phó toàn bộ việc lập dàn ý, suy luận và viết kết luận cho máy làm teo dần năng lực tư duy cấu trúc độc lập.</li>
              <li><strong>3. Rủi ro Pháp lý &amp; Bảo mật dữ liệu Ngân hàng:</strong>
                <br>&bull; <strong>Thông tư 49/2026/TT-BGDĐT (Điều 10):</strong> Giấu hoặc không công bố đầy đủ việc dùng AI là hành vi vi phạm liêm chính học thuật.
                <br>&bull; <strong>Luật Bảo vệ dữ liệu cá nhân 2025:</strong> Tải dữ liệu khách hàng thật lên AI công cộng nước ngoài là vi phạm pháp luật.
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bar"><span>Trường ĐH Ngân hàng TP.HCM (HUB) | Kỹ năng ứng dụng AI trong học tập và nghiên cứu | ThS. Phó Hải Đăng</span><span class="page-num">3 / 18</span></div>
  </section>

  <!-- SLIDE 4: TRIẾT LÝ & 4 TRỤ CỘT -->
  <section class="slide">
    <div class="header-bar"><span>01. BỐI CẢNH &amp; TRIẾT LÝ ĐÀO TẠO</span><span>KIẾN TRÚC NĂNG LỰC</span></div>
    <div class="slide-body">
      <h1 class="page-title">TRIẾT LÝ: TƯ DUY &rarr; KỸ NĂNG &rarr; CÔNG CỤ &amp; 4 TRỤ CỘT CỐT LÕI</h1>
      <div class="banner" style="background: var(--light-accent); border: 1.5px solid var(--accent); color: var(--navy);">
        VỊ THẾ NGƯỜI LÀM CHỦ: &nbsp; <strong>AI ĐỀ XUẤT &mdash; BẠN QUYẾT ĐỊNH &mdash; BẠN CHỊU TRÁCH NHIỆM</strong><br>
        <em>Phép thử vàng: "Nếu AI làm sai ở bước này, mình có đủ kiến thức và công cụ để phát hiện ra không? Nếu không &rarr; Tuyệt đối đừng giao!"</em>
      </div>
      <div class="grid-2" style="gap: 16px;">
        <div class="left-card" style="border-left-color: var(--red);">
          <h3 style="color: var(--red);">TRỤ CỘT 1: BẢN CHẤT AI, PROMPT, CONTEXT &amp; HARNESS (Buổi 1&ndash;3)</h3>
          <ul>
            <li><strong>Hiểu bản chất xác suất:</strong> AI là máy đoán chữ tiếp theo, không phải kho sự thật.</li>
            <li><strong>Từ Prompt đến Context:</strong> Khung CRISP, 5 kỹ thuật nâng cao &amp; chốt chặn <em>"Không suy đoán"</em>.</li>
            <li><strong>Kiến trúc Harness:</strong> Xây "bộ dây cương" có cổng dừng <strong>GATE (🔒)</strong> &amp; xử lý thiếu dữ liệu <strong>FALLBACK (❓)</strong>.</li>
          </ul>
        </div>
        <div class="left-card" style="border-left-color: var(--accent);">
          <h3 style="color: var(--accent);">TRỤ CỘT 2: SECOND BRAIN &amp; PHÁT TRIỂN SỰ HỌC (Buổi 4&ndash;5)</h3>
          <ul>
            <li><strong>Kiến trúc PARA &amp; CODE:</strong> Ngoại hóa tri thức, chống "nghĩa địa file số".</li>
            <li><strong>Ghi chú nguyên tử (Atomic Notes):</strong> 1 ghi chú = 1 luận điểm bằng ngôn từ riêng + Phản tư 4F.</li>
            <li><strong>Tích hợp RAG (Gemini Notebook):</strong> Biến AI thành "Thư ký trung thành" trích dẫn tận dòng.</li>
          </ul>
        </div>
        <div class="left-card" style="border-left-color: var(--green);">
          <h3 style="color: var(--green);">TRỤ CỘT 3: AI TRONG NCKH &amp; KIỂM CHỨNG 5 BƯỚC (Buổi 6&ndash;8)</h3>
          <ul>
            <li><strong>Quy trình 4 bước:</strong> Tìm &rarr; Đọc &rarr; Tổng hợp &rarr; Viết (Kiểm chứng đi xuyên suốt).</li>
            <li><strong>Kỹ năng "Soi 3 phút":</strong> Đối chiếu số liệu, truy chỗ AI tự bịa thêm (case Hemani 2026).</li>
            <li><strong>Màng lọc 3 lớp:</strong> Checklist 5 bước + Công cụ Tomaca + Khóa chốt Zotero 8.</li>
          </ul>
        </div>
        <div class="left-card" style="border-left-color: var(--orange);">
          <h3 style="color: var(--orange);">TRỤ CỘT 4: ĐẠO ĐỨC, PHÁP LÝ &amp; BẢO MẬT DỮ LIỆU (Buổi 9&ndash;11)</h3>
          <ul>
            <li><strong>Pháp lý Việt Nam &amp; Quốc tế:</strong> Thông tư 49/2026 (Điều 10), Luật AI 134/2025, COPE/ICMJE.</li>
            <li><strong>Đèn giao thông &amp; Khai báo:</strong> Phân vùng Xanh &ndash; Vàng &ndash; Đỏ &amp; Mẫu câu khai báo AI chuẩn.</li>
            <li><strong>Bảo mật dữ liệu Ngân hàng:</strong> Khử định danh &amp; chỉ gửi Schema trước khi phân tích.</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="footer-bar"><span>Trường ĐH Ngân hàng TP.HCM (HUB) | Kỹ năng ứng dụng AI trong học tập và nghiên cứu | ThS. Phó Hải Đăng</span><span class="page-num">4 / 18</span></div>
  </section>

  <!-- SLIDE 5: CHUẨN ĐẦU RA CLO1 - CLO5 -->
  <section class="slide">
    <div class="header-bar"><span>02. CHUẨN ĐẦU RA &amp; LỘ TRÌNH 11 BUỔI</span><span>COURSE LEARNING OUTCOMES</span></div>
    <div class="slide-body">
      <h1 class="page-title">5 CHUẨN ĐẦU RA (CLO) Ở MỨC VẬN DỤNG, ĐÁNH GIÁ &amp; SÁNG TẠO</h1>
      <table class="acad-table">
        <thead>
          <tr>
            <th style="width: 11%;">Mã CLO</th>
            <th style="width: 15%;">Thang Bloom</th>
            <th style="width: 48%;">Năng lực Sinh viên đạt được sau khóa học</th>
            <th style="width: 26%;">Cấu phần Đánh giá Cuối khóa</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>CLO1</strong></td>
            <td>Phân tích (Mức 4)</td>
            <td>Giải thích cơ chế xác suất LLM, nguyên nhân Hallucination, Cognitive Offloading và lập bảng phân vai <em>"Việc nào giao &ndash; Việc nào giữ"</em>.</td>
            <td>Hồ sơ Đề án (Phần 1) &amp; Vấn đáp bảo vệ</td>
          </tr>
          <tr>
            <td><strong>CLO2</strong></td>
            <td>Sáng tạo (Mức 5&ndash;6)</td>
            <td>Viết câu lệnh chuẩn CRISP + kỹ thuật nâng cao, làm sạch Context và đóng gói bộ khung điều phối AI (<strong>Harness</strong>) có cổng <strong>GATE &amp; FALLBACK</strong>.</td>
            <td>Hồ sơ Đề án (Mảnh ghép 1) &amp; Live Demo</td>
          </tr>
          <tr>
            <td><strong>CLO3</strong></td>
            <td>Vận dụng (Mức 3)</td>
            <td>Tổ chức tri thức theo PARA/CODE, tự viết hệ thống <strong>Atomic Notes</strong> + phản tư 4F và kết nối với công cụ <strong>RAG (Gemini Notebook)</strong>.</td>
            <td><strong>Hồ sơ Cá nhân (30% điểm)</strong>: &ge; 6 Atomic Notes &amp; Nhật ký LMS</td>
          </tr>
          <tr>
            <td><strong>CLO4</strong></td>
            <td>Đánh giá (Mức 5)</td>
            <td>Thực hiện quy trình NCKH 4 bước; thực thi kỹ năng <em>"Soi 3 phút"</em>, <strong>Checklist 5 bước</strong>, công cụ <strong>Tomaca</strong> và quản lý trích dẫn bằng <strong>Zotero 8</strong>.</td>
            <td>Hồ sơ Đề án (Mảnh ghép 3) &amp; Kiểm toán chéo (Peer Audit)</td>
          </tr>
          <tr>
            <td><strong>CLO5</strong></td>
            <td>Đánh giá (Mức 5)</td>
            <td>Phân loại rủi ro theo Đèn giao thông (Xanh&ndash;Vàng&ndash;Đỏ), khử định danh dữ liệu ngân hàng và viết <strong>Bản khai báo AI</strong> đúng Điều 10 <strong>Thông tư 49/2026</strong>.</td>
            <td>Hồ sơ Đề án (Mảnh ghép 4) &amp; Kiểm toán chéo (Peer Audit)</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="footer-bar"><span>Trường ĐH Ngân hàng TP.HCM (HUB) | Kỹ năng ứng dụng AI trong học tập và nghiên cứu | ThS. Phó Hải Đăng</span><span class="page-num">5 / 18</span></div>
  </section>

  <!-- SLIDE 6: BẢN ĐỒ TỔNG THỂ 11 BUỔI & 4 MẢNH GHÉP -->
  <section class="slide">
    <div class="header-bar"><span>02. CHUẨN ĐẦU RA &amp; LỘ TRÌNH 11 BUỔI</span><span>ROADMAP 44 TIẾT</span></div>
    <div class="slide-body">
      <h1 class="page-title">BẢN ĐỒ TỔNG THỂ 11 BUỔI (44 TIẾT) GẮN VỚI 4 MẢNH GHÉP ĐỀ ÁN</h1>
      <div class="grid-4">
        <div class="card" style="border-color: var(--red);">
          <div class="card-header" style="background: var(--red);">MODULE 1 (Buổi 1 &ndash; 3)<br>12 Tiết</div>
          <div class="card-content" style="font-size: 13.5px;">
            <div style="font-weight: 700; color: var(--red); text-align: center; margin-bottom: 8px;">BẢN CHẤT AI, PROMPT, CONTEXT &amp; HARNESS</div>
            <ul>
              <li><strong>Buổi 1:</strong> Bản chất xác suất LLM, Hallucination (1/277) &amp; Phân vai.</li>
              <li><strong>Buổi 2:</strong> Khung CRISP, 5 kỹ thuật nâng cao &amp; Context Engineering.</li>
              <li><strong>Buổi 3:</strong> Kiến trúc Harness (GATE &amp; FALLBACK) + Gia sư Socrates.</li>
            </ul>
            <div style="background: var(--light-red); border: 1px solid var(--red); padding: 8px; border-radius: 4px; margin-top: 10px; font-weight: 700; color: var(--red); text-align: center; font-size: 12.5px;">
              CHỐT MẢNH GHÉP 1 (Buổi 3):<br>Bộ Harness Nghiệp vụ vượt 3 kịch bản test
            </div>
          </div>
        </div>
        <div class="card" style="border-color: var(--accent);">
          <div class="card-header" style="background: var(--accent);">MODULE 2 (Buổi 4 &ndash; 5)<br>8 Tiết</div>
          <div class="card-content" style="font-size: 13.5px;">
            <div style="font-weight: 700; color: var(--accent); text-align: center; margin-bottom: 8px;">SECOND BRAIN &amp; KHO TRI THỨC RAG</div>
            <ul>
              <li><strong>Buổi 4:</strong> Kiến trúc PARA, luồng CODE, viết Atomic Notes &amp; phản tư 4F.</li>
              <li><strong>Buổi 5:</strong> Bản chất RAG (Thư ký trung thành), Gemini Notebook &amp; truy vấn chéo đa nguồn.</li>
            </ul>
            <div style="background: var(--light-accent); border: 1px solid var(--accent); padding: 8px; border-radius: 4px; margin-top: 10px; font-weight: 700; color: var(--accent); text-align: center; font-size: 12.5px;">
              CHỐT MẢNH GHÉP 2 (Buổi 5):<br>Kho Second Brain + RAG &amp; Tiến độ Atomic Notes
            </div>
          </div>
        </div>
        <div class="card" style="border-color: var(--green);">
          <div class="card-header" style="background: var(--green);">MODULE 3 (Buổi 6 &ndash; 8)<br>12 Tiết</div>
          <div class="card-content" style="font-size: 13.5px;">
            <div style="font-weight: 700; color: var(--green); text-align: center; margin-bottom: 8px;">AI TRONG NCKH &amp; KIỂM CHỨNG 5 BƯỚC</div>
            <ul>
              <li><strong>Buổi 6:</strong> Tìm nguồn thật (Semantic/Elicit/Consensus) &amp; "Soi 3 phút".</li>
              <li><strong>Buổi 7:</strong> Quy luật Linardon, Checklist 5 bước, Tomaca &amp; Zotero 8.</li>
              <li><strong>Buổi 8:</strong> Ma trận tổng hợp (Synthesis), Viết 4 nhịp &amp; Làm slide 4 lớp.</li>
            </ul>
            <div style="background: var(--light-green); border: 1px solid var(--green); padding: 8px; border-radius: 4px; margin-top: 10px; font-weight: 700; color: var(--green); text-align: center; font-size: 12.5px;">
              CHỐT MẢNH GHÉP 3 (Buổi 8):<br>Báo cáo NCKH/Nghiệp vụ + 100% nguồn Zotero
            </div>
          </div>
        </div>
        <div class="card" style="border-color: var(--orange);">
          <div class="card-header" style="background: var(--orange);">MODULE 4 (Buổi 9 &ndash; 11)<br>12 Tiết</div>
          <div class="card-content" style="font-size: 13.5px;">
            <div style="font-weight: 700; color: var(--orange); text-align: center; margin-bottom: 8px;">ĐẠO ĐỨC, PHÁP LÝ, KIỂM TOÁN &amp; BẢO VỆ</div>
            <ul>
              <li><strong>Buổi 9:</strong> Thông tư 49/2026 (Điều 10), COPE, Bảo mật &amp; Khai báo AI.</li>
              <li><strong>Buổi 10:</strong> Studio Kiểm toán chéo 3 vòng giữa các nhóm (Peer Audit).</li>
              <li><strong>Buổi 11:</strong> Bảo vệ Đề án, Vấn đáp cá nhân &amp; Tổng kết hành trình.</li>
            </ul>
            <div style="background: var(--light-orange); border: 1px solid var(--orange); padding: 8px; border-radius: 4px; margin-top: 10px; font-weight: 700; color: var(--orange); text-align: center; font-size: 12.5px;">
              CHỐT MẢNH GHÉP 4 &amp; BẢO VỆ:<br>Khai báo Thông tư 49 + Kiểm toán chéo (100% điểm)
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bar"><span>Trường ĐH Ngân hàng TP.HCM (HUB) | Kỹ năng ứng dụng AI trong học tập và nghiên cứu | ThS. Phó Hải Đăng</span><span class="page-num">6 / 18</span></div>
  </section>

  <!-- SLIDE 7: CHI TIẾT BUỔI 1 - 5 -->
  <section class="slide">
    <div class="header-bar"><span>02. CHUẨN ĐẦU RA &amp; LỘ TRÌNH 11 BUỔI</span><span>CHI TIẾT MODULE 1 &amp; 2</span></div>
    <div class="slide-body">
      <h1 class="page-title">LỘ TRÌNH CHI TIẾT BUỔI 1 &ndash; 5: TỪ PROMPT-HARNESS ĐẾN SECOND BRAIN</h1>
      <table class="acad-table">
        <thead>
          <tr>
            <th style="width: 10%;">Buổi</th>
            <th style="width: 28%;">Chủ đề Buổi học (4 tiết = 200 phút)</th>
            <th style="width: 37%;">Trọng tâm Tư duy &amp; Kỹ năng cốt lõi</th>
            <th style="width: 25%;">Sản phẩm trên LMS &amp; Đề án</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Buổi 1</strong></td>
            <td><strong>Bản chất AI &amp; Tư duy người làm chủ:</strong> "AI là Trợ lý, Bạn là Chủ"</td>
            <td>Cơ chế xác suất LLM; Hallucination (Topaz 1/277); Cognitive Offloading &amp; Fluency Illusion; Bảng phân vai Người &ndash; AI.</td>
            <td>Khởi tạo LMS Hub; lập nhóm 3&ndash;4 SV; viết Atomic Note &amp; phản tư 4F số 1.</td>
          </tr>
          <tr>
            <td><strong>Buổi 2</strong></td>
            <td><strong>Từ Prompt đến Context Engineering:</strong> Giao diện của Tư duy</td>
            <td>Khung CRISP 5 thành tố; 5 kỹ thuật nâng cao (CoT, Role, Few-shot, Iterative, Negative + <em>"Không suy đoán"</em>); Thiết kế gói Context sạch.</td>
            <td>Chốt đề tài Đề án nhóm; thiết kế 3 cụm Prompt CRISP + danh mục Context.</td>
          </tr>
          <tr>
            <td><strong>Buổi 3</strong></td>
            <td><strong>Kiến trúc Harness:</strong> Xây dựng "Bộ dây cương" điều phối AI</td>
            <td>Phân biệt Prompt &ndash; Context &ndash; Harness; Thiết kế cổng dừng <strong>GATE (🔒)</strong> &amp; <strong>FALLBACK (❓)</strong>; Gia sư Socrates với 4 kỹ thuật học sâu.</td>
            <td style="background: var(--light-green); font-weight: 700; color: var(--green);">HOÀN THÀNH MẢNH GHÉP 1: Đóng gói &amp; test 3 kịch bản Bộ Harness Đề án.</td>
          </tr>
          <tr>
            <td><strong>Buổi 4</strong></td>
            <td><strong>Kiến trúc Second Brain (PARA &amp; CODE)</strong> &amp; Ghi chú nguyên tử</td>
            <td>Ngoại hóa tri thức; Tổ chức theo hành động PARA; Luồng CODE; Kỹ thuật viết Atomic Note (100% ngôn từ riêng, tiêu đề khẳng định) &amp; 4F.</td>
            <td>Dựng không gian Second Brain; viết 3 Atomic Notes đầu tiên; mở kho nhóm.</td>
          </tr>
          <tr>
            <td><strong>Buổi 5</strong></td>
            <td><strong>Tích hợp Second Brain với Công nghệ RAG</strong> (Gemini Notebook)</td>
            <td>Bản chất RAG (Thư ký trung thành có trích dẫn) vs LLM thuần; Truy vấn chéo đa tài liệu; Vòng lặp Second Brain &harr; RAG; Cảnh báo Grounded Garbage.</td>
            <td style="background: var(--light-green); font-weight: 700; color: var(--green);">HOÀN THÀNH MẢNH GHÉP 2: Dựng kho RAG Đề án &amp; Rà soát giữa khóa.</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="footer-bar"><span>Trường ĐH Ngân hàng TP.HCM (HUB) | Kỹ năng ứng dụng AI trong học tập và nghiên cứu | ThS. Phó Hải Đăng</span><span class="page-num">7 / 18</span></div>
  </section>

  <!-- SLIDE 8: CHI TIẾT BUỔI 6 - 11 -->
  <section class="slide">
    <div class="header-bar"><span>02. CHUẨN ĐẦU RA &amp; LỘ TRÌNH 11 BUỔI</span><span>CHI TIẾT MODULE 3 &amp; 4</span></div>
    <div class="slide-body">
      <h1 class="page-title">LỘ TRÌNH CHI TIẾT BUỔI 6 &ndash; 11: NCKH, KIỂM CHỨNG, ĐẠO ĐỨC &amp; BẢO VỆ</h1>
      <table class="acad-table" style="font-size: 12.8px;">
        <thead>
          <tr>
            <th style="width: 10%;">Buổi</th>
            <th style="width: 28%;">Chủ đề Buổi học (4 tiết = 200 phút)</th>
            <th style="width: 37%;">Trọng tâm Tư duy &amp; Kỹ năng cốt lõi</th>
            <th style="width: 25%;">Sản phẩm trên LMS &amp; Đề án</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Buổi 6</strong></td>
            <td><strong>NCKH với AI (Bước 1 &amp; 2):</strong> Tìm nguồn thật &amp; "Soi 3 phút"</td>
            <td>Quy tắc <em>"Nguồn thật trước, AI sau"</em>; Phễu câu hỏi; Semantic Scholar, Elicit, Consensus; Prompt 7 mục &amp; "Soi 3 phút" (Case Hemani 2026).</td>
            <td>Mỗi SV tìm 3 bài thật, chạy tóm tắt 7 mục &amp; lập Biên bản Soi 3 phút.</td>
          </tr>
          <tr>
            <td><strong>Buổi 7</strong></td>
            <td><strong>Trích dẫn bịa, Checklist 5 bước, Tomaca &amp; Zotero 8</strong></td>
            <td>Quy tắc <em>"Chưa kiểm chứng, chưa vào bài"</em>; Quy luật Linardon (19,9% / 29%); Checklist 5 bước; Thực hành Tomaca (Máy soát người quyết) &amp; Zotero 8.</td>
            <td>Kiểm chứng đủ 9&ndash;12 nguồn của Đề án qua 5 bước + Tomaca &amp; nạp Zotero.</td>
          </tr>
          <tr>
            <td><strong>Buổi 8</strong></td>
            <td><strong>NCKH với AI (Bước 3 &amp; 4):</strong> Tổng hợp, Viết &amp; Trình bày</td>
            <td>Phân biệt Summary vs Synthesis; Lập Ma trận Tổng hợp tìm Research Gap; Viết học thuật 4 nhịp chèn Zotero; Làm slide 4 lớp.</td>
            <td style="background: var(--light-green); font-weight: 700; color: var(--green);">HOÀN THÀNH MẢNH GHÉP 3: Bản thảo Báo cáo có Ma trận tổng hợp &amp; Zotero.</td>
          </tr>
          <tr>
            <td><strong>Buổi 9</strong></td>
            <td><strong>Đạo đức, Pháp lý (Thông tư 49/2026) &amp; An toàn dữ liệu</strong></td>
            <td>Thông tư 49/2026/TT-BGDĐT (Điều 10); Luật AI 134/2025; COPE/ICMJE; Vụ GS Hancock; Đèn giao thông (Xanh&ndash;Vàng&ndash;Đỏ); Khử định danh &amp; Mẫu khai báo.</td>
            <td style="background: var(--light-green); font-weight: 700; color: var(--green);">HOÀN THÀNH MẢNH GHÉP 4: Bảng bảo mật dữ liệu &amp; Bản khai báo Thông tư 49.</td>
          </tr>
          <tr>
            <td><strong>Buổi 10</strong></td>
            <td><strong>Project Clinic &amp; Studio Kiểm toán chéo (Peer Audit)</strong></td>
            <td>Kỹ năng Kiểm toán học thuật (Red-Teaming) 3 vòng: Stress-test bộ Harness nhóm bạn, quét Tomaca &amp; mở PDF gốc kiểm tra Checklist 5 bước.</td>
            <td>Nộp trọn bộ Hồ sơ Đề án 4 mảnh ghép &amp; Biên bản Kiểm toán chéo (15% điểm).</td>
          </tr>
          <tr>
            <td><strong>Buổi 11</strong></td>
            <td><strong>Bảo vệ Đề án Cuối khóa (Showcase), Phản biện &amp; Tổng kết</strong></td>
            <td>Thuyết trình &amp; Live Demo bộ Harness; Tranh biện cùng Hội đồng Kiểm toán chéo; Vấn đáp chỉ định từng cá nhân trên Second Brain.</td>
            <td style="background: var(--light-red); font-weight: 700; color: var(--red);">CHẤM TỔNG KẾT CUỐI KHÓA (100% ĐIỂM) &amp; Cam kết Người làm chủ AI.</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="footer-bar"><span>Trường ĐH Ngân hàng TP.HCM (HUB) | Kỹ năng ứng dụng AI trong học tập và nghiên cứu | ThS. Phó Hải Đăng</span><span class="page-num">8 / 18</span></div>
  </section>

  <!-- SLIDE 9: SECTION DIVIDER ĐÁNH GIÁ -->
  <section class="slide navy-bg">
    <div class="gold-top-bar"></div>
    <div style="flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 60px; text-align: center;">
      <div style="color: var(--gold); font-size: 18px; font-weight: 700; letter-spacing: 4px; margin-bottom: 14px;">PHẦN TRỌNG TÂM</div>
      <h1 style="font-family: Georgia, serif; font-size: 40px; color: var(--white); margin-bottom: 24px;">
        CHIẾN LƯỢC ĐÁNH GIÁ HỌC PHẦN (100% CUỐI KHÓA)
      </h1>
      <div style="width: 360px; height: 3px; background: var(--gold); margin-bottom: 28px;"></div>
      <p style="font-size: 19px; line-height: 1.6; color: #E2E8F0; max-width: 920px;">
        Đặc thù lớp Chứng chỉ chuẩn đầu ra bắt buộc để tốt nghiệp tại HUB:<br>
        &bull; Không chia điểm quá trình và điểm thi trắc nghiệm rời rạc như môn chính quy.<br>
        &bull; Đánh giá 100% qua <strong>ĐỀ ÁN TÍCH HỢP LŨY TIẾN (CAPSTONE PORTFOLIO)</strong><br>
        kết hợp <strong>THUYẾT TRÌNH, VẤN ĐÁP CÁ NHÂN &amp; KIỂM TOÁN CHÉO GIỮA CÁC NHÓM</strong>.
      </p>
    </div>
  </section>

  <!-- SLIDE 10: CƠ CẤU 100% ĐIỂM (40% - 30% - 30%) -->
  <section class="slide">
    <div class="header-bar"><span>03. CHIẾN LƯỢC ĐÁNH GIÁ CUỐI KHÓA (100%)</span><span>MÔ HÌNH 3 CẤU PHẦN</span></div>
    <div class="slide-body">
      <h1 class="page-title">CƠ CẤU 100% ĐIỂM HẾT MÔN: KẾT HỢP KẾT QUẢ NHÓM &amp; NĂNG LỰC CÁ NHÂN</h1>
      <div class="grid-3">
        <div class="card" style="border-color: var(--navy);">
          <div class="card-header" style="background: var(--navy);">CẤU PHẦN 1: HỒ SƠ ĐỀ ÁN NHÓM</div>
          <div class="card-content">
            <div style="font-family: Georgia, serif; font-size: 36px; font-weight: 700; color: var(--navy); text-align: center;">40% <span style="font-size: 16px; color: var(--text-mid);">(4,0 điểm)</span></div>
            <hr style="margin: 10px 0; border: none; border-top: 2px solid var(--navy);">
            <ul>
              <li><strong>Hình thức:</strong> Chấm chung theo nhóm (3 &ndash; 4 SV cùng chuyên ngành).</li>
              <li><strong>Sản phẩm nộp (Buổi 10):</strong> Bộ Hồ sơ Đề án Ứng dụng AI gồm 4 Mảnh ghép lũy tiến từ Buổi 1 đến Buổi 9.</li>
              <li><strong>Trọng tâm chấm:</strong>
                <br>&bull; Thiết kế Prompt-Context &amp; Bộ Harness (15%)
                <br>&bull; Báo cáo nghiên cứu/nghiệp vụ có 9&ndash;12 nguồn Zotero đã kiểm chứng 5 bước + Tomaca (15%)
                <br>&bull; Bảo mật dữ liệu &amp; Khai báo AI theo Thông tư 49/2026 (10%).
              </li>
            </ul>
          </div>
        </div>
        <div class="card" style="background: var(--light-red); border-color: var(--red);">
          <div class="card-header" style="background: var(--red);">CẤU PHẦN 2: DẤU ẤN CÁ NHÂN</div>
          <div class="card-content">
            <div style="font-family: Georgia, serif; font-size: 36px; font-weight: 700; color: var(--red); text-align: center;">30% <span style="font-size: 16px; color: var(--text-mid);">(3,0 điểm)</span></div>
            <hr style="margin: 10px 0; border: none; border-top: 2px solid var(--red);">
            <ul>
              <li><strong>Hình thức:</strong> Chấm RIÊNG từng thành viên (Chống triệt để "ăn theo nhóm"!).</li>
              <li><strong>Kho Second Brain (15%):</strong> Mỗi cá nhân phải tự tay đóng góp <strong>&ge; 06 Atomic Notes</strong> (viết bằng ngôn từ riêng) vào Đề án &amp; hoàn thành &ge; 80% Nhật ký 4F + Quiz trên LMS.</li>
              <li><strong>Vấn đáp chỉ định (15%):</strong> Tại Buổi 11, Giảng viên chỉ định ngẫu nhiên <strong>BẤT KỲ thành viên nào</strong> giải thích bản chất hoặc thao tác live trên Harness/Zotero.</li>
            </ul>
          </div>
        </div>
        <div class="card" style="background: var(--light-green); border-color: var(--green);">
          <div class="card-header" style="background: var(--green);">CẤU PHẦN 3: BẢO VỆ &amp; KIỂM TOÁN</div>
          <div class="card-content">
            <div style="font-family: Georgia, serif; font-size: 36px; font-weight: 700; color: var(--green); text-align: center;">30% <span style="font-size: 16px; color: var(--text-mid);">(3,0 điểm)</span></div>
            <hr style="margin: 10px 0; border: none; border-top: 2px solid var(--green);">
            <ul>
              <li><strong>Hình thức:</strong> Thực hiện tại Studio Buổi 10 và Hội đồng Buổi 11.</li>
              <li><strong>Thuyết trình &amp; Demo (15%):</strong> Nhóm trình bày giải pháp (8&ndash;10 phút), Live Demo bộ Harness dừng đúng cổng GATE và trả lời phản biện.</li>
              <li><strong>Kiểm toán chéo nhóm bạn (15%):</strong> Đóng vai "Hội đồng Kiểm toán" dùng Stress-test, Tomaca &amp; Checklist 5 bước đi "soi" đề án của nhóm đối tác.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bar"><span>Trường ĐH Ngân hàng TP.HCM (HUB) | Kỹ năng ứng dụng AI trong học tập và nghiên cứu | ThS. Phó Hải Đăng</span><span class="page-num">10 / 18</span></div>
  </section>

  <!-- SLIDE 11: GIẢI PHẪU 4 MẢNH GHÉP LŨY TIẾN -->
  <section class="slide">
    <div class="header-bar"><span>04. GIẢI PHẪU ĐỀ ÁN &amp; KIỂM TOÁN CHÉO</span><span>CAPSTONE PORTFOLIO</span></div>
    <div class="slide-body">
      <h1 class="page-title">4 MẢNH GHÉP LŨY TIẾN CỦA ĐỀ ÁN: LÀM TỚI ĐÂU, XONG TỚI ĐÓ!</h1>
      <div class="grid-2" style="gap: 18px;">
        <div class="left-card" style="border-left-color: var(--red);">
          <h3 style="color: var(--red);">MẢNH GHÉP 1 (Chốt ở Buổi 3): KIẾN TRÚC PROMPT &ndash; CONTEXT &ndash; HARNESS</h3>
          <ul>
            <li><strong>Bảng phân vai Người &ndash; AI:</strong> Phân rã bài toán nghiệp vụ (Tài chính, Ngân hàng, Kế toán, Marketing...) theo nguyên tắc kiểm soát lỗi.</li>
            <li><strong>Bộ 3 cụm Prompt CRISP &amp; Context:</strong> Tích hợp CoT, Few-shot, Iterative và chốt chặn <em>"Không suy đoán"</em>.</li>
            <li><strong>Đóng gói Bộ Harness sống:</strong> Cài đặt trên Claude Project / Gemini Gem có cổng dừng <strong>GATE (🔒) &amp; FALLBACK (❓)</strong>, vượt 3 kịch bản test.</li>
          </ul>
        </div>
        <div class="left-card" style="border-left-color: var(--accent);">
          <h3 style="color: var(--accent);">MẢNH GHÉP 2 (Chốt ở Buổi 5): HỆ THỐNG SECOND BRAIN &amp; KHO RAG</h3>
          <ul>
            <li><strong>Kiến trúc PARA &amp; CODE:</strong> Tổ chức cây thư mục tri thức của đề án trên Obsidian / Notion / Google Docs.</li>
            <li><strong>Đóng góp cá nhân bắt buộc:</strong> Mỗi thành viên tự viết tối thiểu <strong>06 Atomic Notes</strong> (tiêu đề khẳng định, ngôn từ riêng, có liên kết <code>[[...]]</code>).</li>
            <li><strong>Tích hợp Kho RAG:</strong> Nạp tài liệu thật + Atomic Notes vào Gemini Notebook để truy vấn chéo có trích dẫn tận dòng.</li>
          </ul>
        </div>
        <div class="left-card" style="border-left-color: var(--green);">
          <h3 style="color: var(--green);">MẢNH GHÉP 3 (Chốt ở Buổi 8): BÁO CÁO NGHIÊN CỨU &amp; KIỂM CHỨNG ZOTERO</h3>
          <ul>
            <li><strong>Ma trận Tổng hợp (Synthesis Matrix):</strong> Đối sánh <strong>09 &ndash; 12 nguồn tài liệu thật</strong> (mỗi SV phụ trách &ge; 3 nguồn) tìm từ Semantic Scholar/Elicit/Consensus.</li>
            <li><strong>Hồ sơ Kiểm chứng:</strong> Ít nhất 02 Biên bản "Soi 3 phút" + Bảng Checklist kiểm chứng 5 bước + Báo cáo quét trên công cụ <strong>Tomaca</strong>.</li>
            <li><strong>Khóa chốt Zotero 8:</strong> Báo cáo dài 2.500 &ndash; 4.000 chữ chèn trích dẫn tự động từ Zotero (gửi kèm file thư viện <code>.bib</code> / <code>.ris</code>).</li>
          </ul>
        </div>
        <div class="left-card" style="border-left-color: var(--orange);">
          <h3 style="color: var(--orange);">MẢNH GHÉP 4 (Chốt ở Buổi 9): AN TOÀN DỮ LIỆU &amp; KHAI BÁO THÔNG TƯ 49</h3>
          <ul>
            <li><strong>Ma trận Đèn giao thông (Xanh&ndash;Vàng&ndash;Đỏ):</strong> Phân loại rủi ro dữ liệu của đề án theo Checklist 3 câu hỏi an toàn dữ liệu.</li>
            <li><strong>Minh chứng Khử định danh:</strong> Đảm bảo 100% dữ liệu mẫu đưa vào AI đã xóa sạch thông tin định danh cá nhân (PII) / bí mật ngân hàng.</li>
            <li><strong>Bản Khai báo Sử dụng AI:</strong> Viết đúng chuẩn Điều 10 <strong>Thông tư 49/2026/TT-BGDĐT</strong> và chuẩn quốc tế COPE / ICMJE.</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="footer-bar"><span>Trường ĐH Ngân hàng TP.HCM (HUB) | Kỹ năng ứng dụng AI trong học tập và nghiên cứu | ThS. Phó Hải Đăng</span><span class="page-num">11 / 18</span></div>
  </section>

  <!-- SLIDE 12: CẤU PHẦN 2 (30% CÁ NHÂN) -->
  <section class="slide">
    <div class="header-bar"><span>04. GIẢI PHẪU ĐỀ ÁN &amp; KIỂM TOÁN CHÉO</span><span>CHỐNG FREE-RIDER</span></div>
    <div class="slide-body">
      <h1 class="page-title">CẤU PHẦN 2 (30% ĐIỂM CÁ NHÂN): TRIỆT TIÊU TÌNH TRẠNG "ĂN THEO NHÓM"</h1>
      <div class="grid-2">
        <div class="card" style="background: var(--light-red); border-color: var(--red);">
          <div class="card-header" style="background: var(--red);">15% HỒ SƠ SECOND BRAIN CÁ NHÂN TRÊN LMS</div>
          <div class="card-content">
            <ul>
              <li><strong>Mục tiêu:</strong> Đảm bảo không một sinh viên nào có thể nhận Chứng chỉ chuẩn đầu ra nếu chỉ đứng tên trong nhóm mà không tự thực hành.</li>
              <li><strong>06 Atomic Notes chuyên môn:</strong> Mỗi thành viên phải đứng tên tác giả ít nhất 06 Ghi chú nguyên tử trong kho Second Brain của Đề án (mã hóa theo MSSV: <code>AN-2026-MSSV-01</code>...).</li>
              <li><strong>Tiêu chuẩn Atomic Note:</strong> Tiêu đề là 1 câu khẳng định sắc bén; nội dung 100&ndash;200 chữ viết bằng ngôn từ riêng (cấm copy-paste AI); có nguồn đã qua 5 bước kiểm chứng và có liên kết <code>[[...]]</code>.</li>
              <li><strong>Nhật ký Phản tư 4F &amp; Quiz:</strong> Hoàn thành đều đặn Nhật ký 4F (Fact &ndash; Feelings &ndash; Findings &ndash; Future) và Quiz Active Recall sau mỗi buổi học trên LMS Hub.</li>
            </ul>
          </div>
        </div>
        <div class="card">
          <div class="card-header" style="background: var(--navy);">15% VẤN ĐÁP CHỈ ĐỊNH TRỰC TIẾP TẠI BUỔI 11</div>
          <div class="card-content">
            <ul>
              <li><strong>Quy tắc "Chỉ định bất kỳ":</strong> Khi nhóm lên bảo vệ ở Buổi 11, Giảng viên và Hội đồng Kiểm toán có quyền chỉ định <strong>BẤT KỲ thành viên nào</strong> trả lời hoặc thao tác máy tính (kể cả phần của bạn khác trong nhóm).</li>
              <li><strong>Ba Thử thách Vấn đáp nhanh tại bục giảng:</strong>
                <br><br>1. <em>"Mở 1 Atomic Note của em và giải thích tại sao em kết nối nó với mục 2 của báo cáo?"</em>
                <br><br>2. <em>"Mở thư viện Zotero của nhóm, bấm vào trích dẫn số X và thực hiện thao tác 'Soi 3 phút' ngay trên file PDF gốc."</em>
                <br><br>3. <em>"Nhập một dữ liệu thiếu vào Bộ Harness của nhóm và giải thích cách cổng GATE / FALLBACK hoạt động."</em>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bar"><span>Trường ĐH Ngân hàng TP.HCM (HUB) | Kỹ năng ứng dụng AI trong học tập và nghiên cứu | ThS. Phó Hải Đăng</span><span class="page-num">12 / 18</span></div>
  </section>

  <!-- SLIDE 13: CẤU PHẦN 3 (30%) KIỂM TOÁN CHÉO -->
  <section class="slide">
    <div class="header-bar"><span>04. GIẢI PHẪU ĐỀ ÁN &amp; KIỂM TOÁN CHÉO</span><span>PEER AUDIT &amp; RED-TEAMING</span></div>
    <div class="slide-body">
      <h1 class="page-title">CẤU PHẦN 3 (30%): BIẾN LỚP HỌC THÀNH HỘI ĐỒNG KIỂM TOÁN HỌC THUẬT</h1>
      <div class="banner" style="background: var(--light-green); border: 1.5px solid var(--green); color: var(--green);">
        Thay vì "nhận xét chéo xã giao" (khen nhau cho vui), mỗi nhóm được phân công làm <strong>HỘI ĐỒNG KIỂM TOÁN (AUDITOR)</strong> cho 1 nhóm khác ở Buổi 10.<br>
        Điểm của Nhóm Kiểm toán (15%) phụ thuộc vào độ sắc bén và bằng chứng trang gốc khi "soi" bài của nhóm bạn!
      </div>
      <div class="grid-3">
        <div class="card" style="border-color: var(--red);">
          <div class="card-header" style="background: var(--red);">VÒNG 1: KIỂM TOÁN HARNESS &amp; SECOND BRAIN</div>
          <div class="card-content">
            <ul>
              <li><strong>Stress-test 3 kịch bản:</strong> Nhập dữ liệu chuẩn, dữ liệu thiếu (test FALLBACK ❓) và ra lệnh ép vượt rào (test GATE 🔒) trên bộ Harness của nhóm bạn.</li>
              <li><strong>Thẩm định Atomic Notes:</strong> Kiểm tra số lượng (&ge; 6 notes/người) và phát hiện xem có ghi chú nào là bản copy-paste thô từ AI không.</li>
            </ul>
          </div>
        </div>
        <div class="card" style="border-color: var(--accent);">
          <div class="card-header" style="background: var(--accent);">VÒNG 2: KIỂM TOÁN NGUỒN (TOMACA + 5 BƯỚC)</div>
          <div class="card-content">
            <ul>
              <li><strong>Quét tự động trên Tomaca:</strong> Đưa toàn bộ 9&ndash;12 tài liệu tham khảo của nhóm bạn lên Tomaca để tìm DOI giả hoặc <code>metadata-mismatch</code>.</li>
              <li><strong>Soi PDF gốc 3 trích dẫn:</strong> Bốc ngẫu nhiên 3 trích dẫn trọng yếu, mở bài báo gốc kiểm tra Bước 3 (bài có nói đúng ý đó không?) &amp; Bước 4 (khớp số liệu bảng/hình không?).</li>
            </ul>
          </div>
        </div>
        <div class="card" style="border-color: var(--orange);">
          <div class="card-header" style="background: var(--orange);">VÒNG 3: KIỂM TOÁN BẢO MẬT &amp; THÔNG TƯ 49</div>
          <div class="card-content">
            <ul>
              <li><strong>Rà soát An toàn dữ liệu:</strong> Kiểm tra xem hồ sơ và prompt của nhóm bạn có làm lộ dữ liệu cá nhân/ngân hàng chưa khử định danh không.</li>
              <li><strong>Đối chiếu Thông tư 49/2026:</strong> Kiểm tra Bản khai báo AI đã nêu đủ công cụ, phiên bản, thời gian, mục đích và cam kết trách nhiệm chưa.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bar"><span>Trường ĐH Ngân hàng TP.HCM (HUB) | Kỹ năng ứng dụng AI trong học tập và nghiên cứu | ThS. Phó Hải Đăng</span><span class="page-num">13 / 18</span></div>
  </section>

  <!-- SLIDE 14: ĐIỂM LIỆT LIÊM CHÍNH & ĐÈN GIAO THÔNG -->
  <section class="slide">
    <div class="header-bar"><span>04. GIẢI PHẪU ĐỀ ÁN &amp; KIỂM TOÁN CHÉO</span><span>ZERO-TOLERANCE RULE</span></div>
    <div class="slide-body">
      <h1 class="page-title">QUY TẮC "ĐIỂM LIỆT LIÊM CHÍNH" &amp; KHUNG ĐÈN GIAO THÔNG SỬ DỤNG AI</h1>
      <div class="banner" style="background: var(--light-red); border: 2px solid var(--red); color: var(--red);">
        QUY TẮC ĐIỂM LIỆT LIÊM CHÍNH (ZERO-TOLERANCE INTEGRITY RULE):<br>
        Nếu trong Hồ sơ Đề án chính thức nộp ở Buổi 10 bị phát hiện có <strong>BẤT KỲ 01 TÀI LIỆU THAM KHẢO NÀO LÀ BỊA (Fabricated Citation)</strong><br>
        hoặc <strong>KHÔNG KHAI BÁO VIỆC DÙNG AI theo Điều 10 Thông tư 49/2026/TT-BGDĐT</strong> &rarr; <strong>TRỪ THẲNG 50% ĐIỂM HỒ SƠ &amp; BẮT BUỘC LÀM LẠI!</strong>
      </div>
      <div class="grid-3">
        <div class="card" style="background: var(--light-green); border-color: var(--green);">
          <div class="card-header" style="background: var(--green);">VÙNG XANH &mdash; KHUYẾN KHÍCH DÙNG</div>
          <div class="card-content">
            <ul>
              <li>Gợi ý từ khóa và hướng tìm kiếm ban đầu.</li>
              <li>Giải thích khái niệm, thuật ngữ khó để tự học (Gia sư Socrates).</li>
              <li>Phản biện dàn ý do chính bạn tự lập từ Second Brain.</li>
              <li>Rà soát lỗi chính tả, ngữ pháp tiếng Việt / tiếng Anh.</li>
            </ul>
          </div>
        </div>
        <div class="card" style="background: var(--light-orange); border-color: var(--orange);">
          <div class="card-header" style="background: var(--orange);">VÙNG VÀNG &mdash; DÙNG CÓ ĐIỀU KIỆN</div>
          <div class="card-content">
            <ul>
              <li>Dịch tài liệu học thuật &rarr; Phải đối chiếu lại bản PDF gốc.</li>
              <li>Tóm tắt bài báo bằng Prompt 7 mục &rarr; Phải "Soi 3 phút".</li>
              <li>Hỗ trợ viết code R/Python/Excel &rarr; Chỉ gửi Schema, tự chạy lại trên máy.</li>
              <li><strong>BẮT BUỘC:</strong> Kiểm chứng 5 bước, tự viết lại &amp; Khai báo AI.</li>
            </ul>
          </div>
        </div>
        <div class="card" style="background: var(--light-red); border-color: var(--red);">
          <div class="card-header" style="background: var(--red);">VÙNG ĐỎ &mdash; CẤM TUYỆT ĐỐI</div>
          <div class="card-content">
            <ul>
              <li>Để AI viết hộ phần Kết quả, Thảo luận, Kết luận.</li>
              <li>Đưa trích dẫn chưa qua 5 bước kiểm chứng &amp; Zotero vào bài.</li>
              <li>Nộp bài do AI sinh ra mà không khai báo (Vi phạm Thông tư 49).</li>
              <li>Tải dữ liệu mật / thông tin định danh khách hàng thật lên AI công cộng.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bar"><span>Trường ĐH Ngân hàng TP.HCM (HUB) | Kỹ năng ứng dụng AI trong học tập và nghiên cứu | ThS. Phó Hải Đăng</span><span class="page-num">14 / 18</span></div>
  </section>

  <!-- SLIDE 15: RUBRIC 7 TIÊU CHÍ -->
  <section class="slide">
    <div class="header-bar"><span>04. GIẢI PHẪU ĐỀ ÁN &amp; KIỂM TOÁN CHÉO</span><span>RUBRIC CHẤM ĐIỂM</span></div>
    <div class="slide-body">
      <h1 class="page-title">MA TRẬN RUBRIC CHẤM ĐIỂM CHI TIẾT 7 TIÊU CHÍ (100% ĐIỂM CUỐI KHÓA)</h1>
      <table class="acad-table" style="font-size: 12.6px;">
        <thead>
          <tr>
            <th style="width: 30%;">Tiêu chí Đánh giá</th>
            <th style="width: 9%; text-align: center;">CLO</th>
            <th style="width: 10%; text-align: center;">Trọng số</th>
            <th style="width: 51%;">Chuẩn Đạt Mức Tốt &ndash; Xuất Sắc (8,0 &ndash; 10 điểm)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>1.1. Thiết kế Prompt, Context &amp; Bộ Harness nghiệp vụ</strong></td>
            <td style="text-align: center;">CLO1, 2</td>
            <td style="text-align: center; font-weight: 700;">15%</td>
            <td>Phân vai sắc bén; đủ khung CRISP + kỹ thuật nâng cao; Bộ Harness (Gem/Project) có cổng GATE &amp; FALLBACK chạy mượt, vượt 3 kịch bản test.</td>
          </tr>
          <tr>
            <td><strong>1.2. Chất lượng Nghiên cứu, Tổng hợp &amp; Kiểm chứng Zotero</strong></td>
            <td style="text-align: center;">CLO4</td>
            <td style="text-align: center; font-weight: 700;">15%</td>
            <td>100% nguồn (9&ndash;12 nguồn) là nguồn thật quản lý bằng Zotero 8; có Ma trận tổng hợp, Biên bản Soi 3 phút, Checklist 5 bước &amp; báo cáo Tomaca.</td>
          </tr>
          <tr>
            <td><strong>1.3. Hồ sơ An toàn dữ liệu &amp; Bản khai báo Thông tư 49/2026</strong></td>
            <td style="text-align: center;">CLO5</td>
            <td style="text-align: center; font-weight: 700;">10%</td>
            <td>Phân loại rủi ro dữ liệu theo Đèn giao thông; khử định danh dữ liệu mẫu; Bản khai báo AI chi tiết, đúng Điều 10 Thông tư 49/2026 &amp; COPE.</td>
          </tr>
          <tr style="background: var(--light-red);">
            <td><strong>2.1. Kho Second Brain &amp; Atomic Notes cá nhân trên LMS</strong></td>
            <td style="text-align: center;">CLO3</td>
            <td style="text-align: center; font-weight: 700; color: var(--red);">15%</td>
            <td><strong>[Chấm cá nhân]</strong> Hoàn thành &ge; 80% Quiz &amp; phản tư 4F trên LMS; đóng góp &ge; 06 Atomic Notes chất lượng cao, ngôn từ riêng, có liên kết <code>[[...]]</code>.</td>
          </tr>
          <tr style="background: var(--light-red);">
            <td><strong>2.2. Năng lực làm chủ khi Vấn đáp chỉ định tại Hội đồng</strong></td>
            <td style="text-align: center;">CLO1&ndash;4</td>
            <td style="text-align: center; font-weight: 700; color: var(--red);">15%</td>
            <td><strong>[Chấm cá nhân]</strong> Trả lời lưu loát câu hỏi bất kỳ của GV/Hội đồng; giải thích được Atomic Note và thao tác live trên Harness/Zotero ngay tại bục.</td>
          </tr>
          <tr>
            <td><strong>3.1. Thuyết trình Bảo vệ &amp; Live Demo Đề án của Nhóm</strong></td>
            <td style="text-align: center;">CLO2, 4</td>
            <td style="text-align: center; font-weight: 700;">15%</td>
            <td>Slide thiết kế chuẩn 4 lớp ("AI làm draft, người làm final"); trình bày đúng giờ (8&ndash;10 phút); Live Demo bộ Harness &amp; minh chứng kiểm chứng thuyết phục.</td>
          </tr>
          <tr>
            <td><strong>3.2. Phản biện &amp; Báo cáo Kiểm toán chéo nhóm bạn</strong></td>
            <td style="text-align: center;">CLO4, 5</td>
            <td style="text-align: center; font-weight: 700;">15%</td>
            <td>Thực hiện nghiêm túc 3 vòng Kiểm toán chéo nhóm đối tác; phát hiện chính xác điểm mạnh/lỗ hổng kèm bằng chứng trang gốc; đặt 2 câu hỏi sắc bén.</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="footer-bar"><span>Trường ĐH Ngân hàng TP.HCM (HUB) | Kỹ năng ứng dụng AI trong học tập và nghiên cứu | ThS. Phó Hải Đăng</span><span class="page-num">15 / 18</span></div>
  </section>

  <!-- SLIDE 16: QUY TẮC VẬN HÀNH LMS HUB & GATEKEEPING -->
  <section class="slide">
    <div class="header-bar"><span>05. QUY TẮC VẬN HÀNH TRÊN LMS HUB</span><span>NHỊP HỌC &amp; ĐIỂM DANH</span></div>
    <div class="slide-body">
      <h1 class="page-title">NHỊP HỌC 200 PHÚT &amp; 3 ĐIỀU KIỆN GÁC CỔNG TRÊN HỆ THỐNG LMS HUB</h1>
      <div class="grid-2">
        <div class="card">
          <div class="card-header" style="background: var(--navy);">CẤU TRÚC 1 BUỔI HỌC 4 TIẾT (200 PHÚT)</div>
          <div class="card-content">
            <ul>
              <li><strong>Trước buổi học (Prep-work trên LMS):</strong> Đọc trước eBook SCQA của chương và làm thử Vòng Test Level 1.</li>
              <li><strong>Nhịp 1 &ndash; Hook &amp; Cái Biết (20 phút):</strong> Theo dõi hành trình nhân vật Minh tại HUB &amp; khảo sát trải nghiệm thực tế.</li>
              <li><strong>Nhịp 2 &ndash; Va chạm &amp; Khái niệm lõi (50 phút):</strong> Trực tiếp trải nghiệm tình huống AI sai/bịa, sau đó đúc kết nguyên lý &amp; xem Live Demo.</li>
              <li><strong>Nhịp 3 &ndash; Thực hành &amp; Studio Đề án (100 phút):</strong> Thực hành có hướng dẫn trên máy tính cá nhân; giải quyết trực tiếp từng mảnh ghép của Đề án nhóm ngay tại lớp.</li>
              <li><strong>Nhịp 4 &ndash; Phản tư 4F &amp; Khóa chốt LMS (30 phút):</strong> Viết Nhật ký Atomic Note 4F, làm Quiz 5 lượt và gửi Feedback tải bài giảng.</li>
            </ul>
          </div>
        </div>
        <div class="card" style="background: var(--light-red); border-color: var(--red);">
          <div class="card-header" style="background: var(--red);">3 ĐIỀU KIỆN BẮT BUỘC ĐỂ ĐƯỢC BẢO VỆ ĐỀ ÁN</div>
          <div class="card-content">
            <ul>
              <li><strong>Điều kiện 1 &ndash; Hiện diện trên lớp (&ge; 80%):</strong> Tham dự tối thiểu 09 / 11 buổi học trực tiếp và tham gia đầy đủ hoạt động thảo luận, thực hành nhóm.</li>
              <li><strong>Điều kiện 2 &ndash; Cơ chế Điểm danh LMS Hub:</strong> Ở mỗi buổi học, một sinh viên chỉ được hệ thống LMS ghi nhận hoàn thành khi thực hiện đủ 2 thao tác:
                <br>&bull; <em>(a) Gửi đánh giá Feedback buổi học CÓ KÈM NHẬN XÉT để mở khóa tải Slide/Bài giảng;</em>
                <br>&bull; <em>(b) Hoàn thành Quiz ôn tập (đạt 10/10 hoặc nỗ lực làm đủ 5 lượt Active Recall để mở khóa lời giải).</em>
              </li>
              <li><strong>Điều kiện 3 &ndash; Lịch sử Tích lũy Tri thức:</strong> Có đầy đủ nhật ký Atomic Notes &amp; phản tư 4F tích lũy đều đặn qua từng tuần.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bar"><span>Trường ĐH Ngân hàng TP.HCM (HUB) | Kỹ năng ứng dụng AI trong học tập và nghiên cứu | ThS. Phó Hải Đăng</span><span class="page-num">16 / 18</span></div>
  </section>

  <!-- SLIDE 17: BỘ 5 TOOLKITS & NHIỆM VỤ BUỔI 1 -->
  <section class="slide">
    <div class="header-bar"><span>05. QUY TẮC VẬN HÀNH TRÊN LMS HUB</span><span>TOOLKITS &amp; HÀNH ĐỘNG</span></div>
    <div class="slide-body">
      <h1 class="page-title">BỘ 5 BIỂU MẪU THỰC HÀNH (TOOLKITS) &amp; NHIỆM VỤ NGAY HÔM NAY</h1>
      <div class="grid-2">
        <div class="card" style="background: var(--light-accent); border-color: var(--accent);">
          <div class="card-header" style="background: var(--accent);">5 BIỂU MẪU GIẢNG VIÊN CUNG CẤP SẴN TRÊN LMS</div>
          <div class="card-content">
            <ul>
              <li><strong>Toolkit 1 (Mảnh ghép 1):</strong> Bảng phân vai Người &ndash; AI, Cheatsheet CRISP &amp; Template System Instructions 4 khối cho Bộ Harness.</li>
              <li><strong>Toolkit 2 (Mảnh ghép 2):</strong> Template Ghi chú nguyên tử (Atomic Note) chuẩn &amp; Mẫu Nhật ký Phản tư 4F.</li>
              <li><strong>Toolkit 3 (Mảnh ghép 3a):</strong> Prompt Tóm tắt bài báo khoa học 7 mục &amp; Biên bản "Soi bản tóm tắt trong 3 phút".</li>
              <li><strong>Toolkit 4 (Mảnh ghép 3b):</strong> Bảng Checklist Kiểm chứng Trích dẫn 5 bước, Hướng dẫn đọc Tomaca &amp; Quy trình Zotero 8.</li>
              <li><strong>Toolkit 5 (Mảnh ghép 4 &amp; Kiểm toán):</strong> Mẫu Bản Công bố Sử dụng AI theo Điều 10 Thông tư 49/2026/TT-BGDĐT &amp; Biên bản Kiểm toán chéo 3 vòng.</li>
            </ul>
          </div>
        </div>
        <div class="card" style="background: var(--light-green); border-color: var(--green);">
          <div class="card-header" style="background: var(--green);">4 VIỆC CẦN LÀM NGAY TRONG BUỔI 1 HÔM NAY</div>
          <div class="card-content">
            <ul>
              <li><strong>Bước 1 &ndash; Đăng nhập LMS Hub &amp; Đổi mật khẩu:</strong> Truy cập đường link LMS của lớp, đăng nhập bằng MSSV và thiết lập Mục tiêu cam kết học tập cá nhân.</li>
              <li><strong>Bước 2 &ndash; Lập nhóm Đề án (3 &ndash; 4 SV cùng ngành):</strong> Chọn những người đồng đội cam kết kỷ luật; thảo luận 3 bài toán nghiệp vụ/nghiên cứu tiềm năng của ngành mình.</li>
              <li><strong>Bước 3 &ndash; Thực hành Bảng phân vai đầu tiên:</strong> Áp dụng ngay bài học Buổi 1 để phân định "Việc nào giao AI &ndash; Việc nào giữ" cho bài toán của nhóm.</li>
              <li><strong>Bước 4 &ndash; Khóa chốt Buổi 1 trên LMS:</strong> Viết Nhật ký 4F số 1, làm Quiz Buổi 1 và gửi Feedback kèm nhận xét để tải tài liệu bài giảng.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bar"><span>Trường ĐH Ngân hàng TP.HCM (HUB) | Kỹ năng ứng dụng AI trong học tập và nghiên cứu | ThS. Phó Hải Đăng</span><span class="page-num">17 / 18</span></div>
  </section>

  <!-- SLIDE 18: SLIDE KẾT -->
  <section class="slide navy-bg">
    <div class="gold-top-bar"></div>
    <div style="padding: 44px 64px; text-align: center; flex: 1; display: flex; flex-direction: column; justify-content: center;">
      <h1 style="font-family: Georgia, serif; font-size: 30px; line-height: 1.35; color: var(--white); margin-bottom: 18px;">
        "AI CÓ THỂ LÀM NHANH HƠN, NHƯNG KHÔNG THỂ<br>
        CHỊU TRÁCH NHIỆM THAY CHO DANH DỰ VÀ TƯƠNG LAI CỦA BẠN."
      </h1>
      <div style="width: 380px; height: 3px; background: var(--gold); margin: 0 auto 28px;"></div>
      <div class="grid-3" style="max-height: 240px; margin-bottom: 28px;">
        <div style="background: var(--dark-navy); border: 1.5px solid var(--gold); border-radius: 6px; padding: 18px;">
          <div style="color: var(--gold); font-weight: 700; font-size: 16px; margin-bottom: 10px;">1. TƯ DUY &rarr; KỸ NĂNG &rarr; CÔNG CỤ</div>
          <div style="font-size: 14px; color: #E2E8F0; line-height: 1.5;">Công cụ thay đổi mỗi ngày, nhưng tư duy điều phối (Prompt &ndash; Context &ndash; Harness) và Bộ Não Thứ Hai (Second Brain) sẽ đi theo bạn suốt đời.</div>
        </div>
        <div style="background: var(--dark-navy); border: 1.5px solid var(--gold); border-radius: 6px; padding: 18px;">
          <div style="color: var(--gold); font-weight: 700; font-size: 16px; margin-bottom: 10px;">2. NGUỒN THẬT &amp; KIỂM CHỨNG 5 BƯỚC</div>
          <div style="font-size: 14px; color: #E2E8F0; line-height: 1.5;">Nguồn thật trước, AI sau. Chưa qua 5 bước kiểm chứng và chưa vào thư viện Zotero 8 thì tuyệt đối chưa được vào báo cáo.</div>
        </div>
        <div style="background: var(--dark-navy); border: 1.5px solid var(--gold); border-radius: 6px; padding: 18px;">
          <div style="color: var(--gold); font-weight: 700; font-size: 16px; margin-bottom: 10px;">3. MINH BẠCH &amp; LÀM CHỦ (THÔNG TƯ 49)</div>
          <div style="font-size: 14px; color: #E2E8F0; line-height: 1.5;">Dùng AI thì khai báo đàng hoàng. Bảo mật tuyệt đối dữ liệu ngân hàng &ndash; khách hàng. AI là trợ lý, bạn là chủ!</div>
        </div>
      </div>
      <div style="color: var(--gold); font-size: 18px; font-style: italic; margin-bottom: 16px;">
        "Tôi đã chuẩn bị trọn vẹn hệ thống học liệu cho các bạn. Các bạn đã sẵn sàng cam kết cho hành trình 11 buổi này chưa?"
      </div>
      <div style="color: #CBD5E1; font-size: 15px;">
        ThS. Phó Hải Đăng &nbsp;|&nbsp; Khoa Hệ thống thông tin quản lý &ndash; Trường ĐH Ngân hàng TP.HCM (HUB) &nbsp;|&nbsp; Thảo luận &amp; Giải đáp (Q&amp;A)
      </div>
    </div>
  </section>

</div>

<div class="controls-bar">
  <button onclick="prevSlide()">&larr; Trang trước</button>
  <span id="slide-indicator">Slide 1 / 18</span>
  <button onclick="nextSlide()">Trang tiếp &rarr;</button>
  <button onclick="toggleFullScreen()">Toàn màn hình (F)</button>
</div>

<script>
  const slides = document.querySelectorAll('.slide');
  const indicator = document.getElementById('slide-indicator');
  const viewport = document.getElementById('viewport');
  let current = 0;

  function showSlide(idx) {
    if (idx < 0) idx = 0;
    if (idx >= slides.length) idx = slides.length - 1;
    slides.forEach((s, i) => s.classList.toggle('active', i === idx));
    current = idx;
    indicator.textContent = `Slide ${current + 1} / ${slides.length}`;
  }
  function nextSlide() { showSlide(current + 1); }
  function prevSlide() { showSlide(current - 1); }
  function toggleFullScreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen();
    } else {
      document.exitFullscreen();
    }
  }
  function fitViewport() {
    const scale = Math.min((window.innerWidth - 40) / 1280, (window.innerHeight - 70) / 720);
    viewport.style.transform = `scale(${Math.min(scale, 1.15)})`;
  }
  window.addEventListener('resize', fitViewport);
  window.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') { e.preventDefault(); nextSlide(); }
    if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); prevSlide(); }
    if (e.key === 'f' || e.key === 'F') { toggleFullScreen(); }
  });
  fitViewport();
</script>
</body>
</html>
"""

html_paths = [
    r"d:\PARA\Projects\second-brain\03-Domains\Teaching\ComputerScience\Ky Nang Ung Dung AI\Slide_00_Gioi_Thieu_De_Cuong_Va_Danh_Gia_HUB.html",
    r"d:\PARA\Projects\second-brain\05-Projects\lms-hub\courses\ky-nang-ai-hub\content\slides\Buoi_00_De_Cuong.html"
]

for p in html_paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Saved HTML deck: {p}")
