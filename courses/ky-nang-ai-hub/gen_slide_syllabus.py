# -*- coding: utf-8 -*-
"""
Script tạo bộ Slide Giới thiệu Đề cương, Lộ trình 11 buổi & Chiến lược Đánh giá Cuối khóa (100%)
Môn: Kỹ năng ứng dụng AI trong học tập và nghiên cứu (Trường ĐH Ngân hàng TP.HCM - HUB)
Theo chuẩn Design System: academic-presentation-vn (Navy / Red / Gold, Georgia & Calibri, Card-based 16:9)
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ---------------------------------------------------------------------------
# DESIGN SYSTEM CONSTANTS (academic-presentation-vn)
# ---------------------------------------------------------------------------
C_NAVY = RGBColor(0x1B, 0x25, 0x58)
C_DARK_NAVY = RGBColor(0x11, 0x1A, 0x40)
C_WHITE = RGBColor(0xFF, 0xFF, 0xFF)
C_OFF_WHITE = RGBColor(0xF5, 0xF6, 0xFA)
C_RED = RGBColor(0xC6, 0x28, 0x28)
C_LIGHT_RED = RGBColor(0xFF, 0xEB, 0xEE)
C_ACCENT = RGBColor(0x15, 0x65, 0xC0)
C_LIGHT_ACCENT = RGBColor(0xE3, 0xF2, 0xFD)
C_GOLD = RGBColor(0xF9, 0xA8, 0x25)
C_GREEN = RGBColor(0x2E, 0x7D, 0x32)
C_LIGHT_GREEN = RGBColor(0xE8, 0xF5, 0xE9)
C_ORANGE = RGBColor(0xE6, 0x51, 0x00)
C_LIGHT_ORANGE = RGBColor(0xFF, 0xF3, 0xE0)
C_GRAY = RGBColor(0x66, 0x66, 0x66)
C_LIGHT_GRAY = RGBColor(0xE0, 0xE0, 0xE0)
C_TEXT_DARK = RGBColor(0x21, 0x21, 0x21)
C_TEXT_MID = RGBColor(0x42, 0x42, 0x42)
C_TEXT_LIGHT = RGBColor(0x75, 0x75, 0x75)

FONT_TITLE = "Georgia"
FONT_BODY = "Calibri"

prs = Presentation()
prs.slide_width = Inches(10.0)
prs.slide_height = Inches(5.625)
blank_layout = prs.slide_layouts[6]


def set_slide_bg(slide, color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_rect(slide, x, y, w, h, fill_color, border_color=None, border_pt=1):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    if border_color:
        shape.line.color.rgb = border_color
        shape.line.width = Pt(border_pt)
    else:
        shape.line.fill.background()
    return shape


def add_oval(slide, x, y, w, h, fill_color, text="", font_size=14, text_color=C_WHITE):
    shape = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(y), Inches(w), Inches(h))
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.fill.background()
    if text:
        tf = shape.text_frame
        tf.word_wrap = False
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.text = text
        p.alignment = PP_ALIGN.CENTER
        p.font.name = FONT_BODY
        p.font.size = Pt(font_size)
        p.font.bold = True
        p.font.color.rgb = text_color
    return shape


def add_text_box(slide, x, y, w, h, text, font_name=FONT_BODY, font_size=11,
                 color=C_TEXT_DARK, bold=False, italic=False, align=PP_ALIGN.LEFT,
                 valign=MSO_ANCHOR.TOP, line_spacing=1.15):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = valign
    tf.margin_left = Inches(0.05)
    tf.margin_right = Inches(0.05)
    tf.margin_top = Inches(0.03)
    tf.margin_bottom = Inches(0.03)

    lines = text.split("\n")
    for idx, line in enumerate(lines):
        p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        p.text = line
        p.alignment = align
        p.line_spacing = line_spacing
        p.space_after = Pt(3)
        p.font.name = font_name
        p.font.size = Pt(font_size)
        p.font.bold = bold
        p.font.italic = italic
        p.font.color.rgb = color
    return tb


def add_bullets_box(slide, x, y, w, h, items, font_size=10.5, color=C_TEXT_DARK, space_after=4):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.06)
    tf.margin_right = Inches(0.06)
    tf.margin_top = Inches(0.04)
    tf.margin_bottom = Inches(0.04)

    for idx, item in enumerate(items):
        p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.line_spacing = 1.15
        p.space_after = Pt(space_after)
        if isinstance(item, tuple):
            lead, rest = item
            r1 = p.add_run()
            r1.text = "• " + lead + " "
            r1.font.name = FONT_BODY
            r1.font.size = Pt(font_size)
            r1.font.bold = True
            r1.font.color.rgb = C_NAVY
            r2 = p.add_run()
            r2.text = rest
            r2.font.name = FONT_BODY
            r2.font.size = Pt(font_size)
            r2.font.bold = False
            r2.font.color.rgb = color
        else:
            p.text = "• " + item
            p.font.name = FONT_BODY
            p.font.size = Pt(font_size)
            p.font.color.rgb = color
    return tb


def add_content_frame(slide, section_title, page_title, slide_num):
    set_slide_bg(slide, C_WHITE)
    # Header bar
    add_rect(slide, 0, 0, 10.0, 0.58, C_NAVY)
    add_text_box(slide, 0.5, 0.08, 8.8, 0.42, section_title.upper(),
                 font_name=FONT_TITLE, font_size=12.5, color=C_WHITE, bold=True,
                 valign=MSO_ANCHOR.MIDDLE)
    # Page title (Red)
    add_text_box(slide, 0.5, 0.68, 9.0, 0.48, page_title,
                 font_name=FONT_TITLE, font_size=20, color=C_RED, bold=True,
                 valign=MSO_ANCHOR.MIDDLE)
    # Footer bar
    add_rect(slide, 0, 5.25, 10.0, 0.375, C_NAVY)
    add_text_box(slide, 0.5, 5.27, 7.5, 0.32,
                 "Trường ĐH Ngân hàng TP.HCM (HUB)  |  Kỹ năng ứng dụng AI trong học tập và nghiên cứu  |  ThS. Phó Hải Đăng",
                 font_name=FONT_BODY, font_size=9, color=C_LIGHT_GRAY, valign=MSO_ANCHOR.MIDDLE)
    add_text_box(slide, 8.8, 5.27, 0.7, 0.32, f"{slide_num} / 18",
                 font_name=FONT_BODY, font_size=9.5, color=C_GOLD, bold=True,
                 align=PP_ALIGN.RIGHT, valign=MSO_ANCHOR.MIDDLE)


def add_card_with_header(slide, x, y, w, h, header_color, header_text, bg_color=C_OFF_WHITE, border_color=C_LIGHT_GRAY):
    add_rect(slide, x, y, w, h, bg_color, border_color, 1)
    add_rect(slide, x, y, w, 0.42, header_color)
    add_text_box(slide, x + 0.08, y + 0.03, w - 0.16, 0.36, header_text,
                 font_name=FONT_BODY, font_size=11.5, color=C_WHITE, bold=True,
                 align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)


def add_left_border_card(slide, x, y, w, h, accent_color, bg_color, title_text, body_items, title_color=None):
    add_rect(slide, x, y, w, h, bg_color, C_LIGHT_GRAY, 0.75)
    add_rect(slide, x, y, 0.08, h, accent_color)
    t_col = title_color if title_color else accent_color
    add_text_box(slide, x + 0.16, y + 0.06, w - 0.24, 0.32, title_text,
                 font_name=FONT_BODY, font_size=12, color=t_col, bold=True)
    add_bullets_box(slide, x + 0.14, y + 0.36, w - 0.22, h - 0.42, body_items, font_size=10)


# ===========================================================================
# SLIDE 1: TRANG BÌA (TITLE SLIDE - NAVY SANDWICH)
# ===========================================================================
s1 = prs.slides.add_slide(blank_layout)
set_slide_bg(s1, C_NAVY)
add_rect(s1, 0, 0, 10.0, 0.07, C_GOLD)
add_text_box(s1, 0.5, 0.55, 9.0, 0.35, "TRƯỜNG ĐẠI HỌC NGÂN HÀNG TP. HỒ CHÍ MINH (HUB)",
             font_name=FONT_BODY, font_size=13, color=C_GOLD, bold=True, align=PP_ALIGN.CENTER)
add_text_box(s1, 0.5, 0.9, 9.0, 0.3, "CHƯƠNG TRÌNH ĐÀO TẠO CHỨNG CHỈ CHUẨN ĐẦU RA BẮT BUỘC",
             font_name=FONT_BODY, font_size=11, color=C_LIGHT_GRAY, align=PP_ALIGN.CENTER)
add_rect(s1, 3.0, 1.32, 4.0, 0.03, C_GOLD)

add_text_box(s1, 0.6, 1.55, 8.8, 1.3,
             "ĐỀ CƯƠNG, LỘ TRÌNH & CHIẾN LƯỢC ĐÁNH GIÁ\nKỸ NĂNG ỨNG DỤNG AI TRONG HỌC TẬP VÀ NGHIÊN CỨU",
             font_name=FONT_TITLE, font_size=24, color=C_WHITE, bold=True,
             align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE, line_spacing=1.25)

add_text_box(s1, 1.0, 2.95, 8.0, 0.4,
             "Triết lý đào tạo: Tư duy  ->  Kỹ năng  ->  Công cụ  |  Giảng dạy chứng nghiệm",
             font_name=FONT_BODY, font_size=13, color=C_GOLD, italic=True, align=PP_ALIGN.CENTER)

# Info badges on cover
add_rect(s1, 1.3, 3.55, 2.3, 0.75, C_DARK_NAVY, C_GOLD, 1)
add_text_box(s1, 1.3, 3.6, 2.3, 0.65, "11 BUỔI (44 TIẾT)\n4 tiết x 50 phút / buổi",
             font_name=FONT_BODY, font_size=11, color=C_WHITE, bold=True, align=PP_ALIGN.CENTER)

add_rect(s1, 3.85, 3.55, 2.3, 0.75, C_DARK_NAVY, C_GOLD, 1)
add_text_box(s1, 3.85, 3.6, 2.3, 0.65, "35% LÝ THUYẾT & DEMO\n65% THỰC HÀNH STUDIO",
             font_name=FONT_BODY, font_size=11, color=C_WHITE, bold=True, align=PP_ALIGN.CENTER)

add_rect(s1, 6.4, 3.55, 2.3, 0.75, C_DARK_NAVY, C_GOLD, 1)
add_text_box(s1, 6.4, 3.6, 2.3, 0.65, "100% ĐÁNH GIÁ CUỐI KHÓA\nĐề án 4 Mảnh ghép & Kiểm toán",
             font_name=FONT_BODY, font_size=11, color=C_WHITE, bold=True, align=PP_ALIGN.CENTER)

add_rect(s1, 0, 4.65, 10.0, 0.975, C_DARK_NAVY)
add_text_box(s1, 0.5, 4.75, 9.0, 0.75,
             "Giảng viên biên soạn & giảng dạy: ThS. Phó Hải Đăng\nKhoa Hệ thống thông tin quản lý  |  Email: dangph@hub.edu.vn  |  Hệ thống học tập: LMS Hub",
             font_name=FONT_BODY, font_size=11, color=C_WHITE, align=PP_ALIGN.CENTER)


# ===========================================================================
# SLIDE 2: BẢN ĐỒ ĐỊNH HƯỚNG BUỔI ĐẦU TIÊN (MỤC LỤC 5 PHẦN)
# ===========================================================================
s2 = prs.slides.add_slide(blank_layout)
add_content_frame(s2, "Tổng quan học phần", "5 NỘI DUNG TRỌNG TÂM SINH VIÊN CẦN NẮM RÕ NGAY BUỔI 1", 2)

toc_items = [
    ("01", "Tại sao cần môn học này & Triết lý: Tư duy -> Kỹ năng -> Công cụ",
     "Cảnh báo thực nghiệm về Hallucination (1/277 bài PubMed), Lệ thuộc nhận thức và 4 trụ cột năng lực", C_RED),
    ("02", "Chuẩn đầu ra (CLO1 - CLO5) & Lộ trình 11 Buổi (44 Tiết) qua 4 Module",
     "Bản đồ tiến trình từ Prompt-Context-Harness -> Second Brain -> NCKH & Kiểm chứng -> Đạo đức & Pháp lý", C_NAVY),
    ("03", "Chiến lược Đánh giá Cuối khóa (100% Điểm): Mô hình 3 Cấu phần",
     "Không chấm điểm quá trình rời rạc: 40% Hồ sơ Đề án nhóm + 30% Cá nhân Second Brain + 30% Bảo vệ & Kiểm toán chéo", C_RED),
    ("04", "Giải phẫu 4 Mảnh ghép Đề án, Kiểm toán chéo (Peer Audit) & Điểm liệt Liêm chính",
     "Cách tích lũy sản phẩm ngay tại lớp từ Buổi 1 đến Buổi 10 và quy tắc loại bỏ 100% trích dẫn bịa", C_NAVY),
    ("05", "Quy tắc Vận hành Lớp học trên LMS Hub & Điều kiện Bảo vệ Cuối khóa",
     "Nhịp học 200 phút, cơ chế điểm danh qua Feedback tải bài giảng, Quiz Active Recall 5 lượt & Nhật ký 4F", C_NAVY),
]

for idx, (num, title, desc, col) in enumerate(toc_items):
    yy = 1.25 + idx * 0.76
    add_rect(s2, 0.6, yy, 8.8, 0.66, C_OFF_WHITE, C_LIGHT_GRAY, 0.75)
    add_oval(s2, 0.75, yy + 0.08, 0.5, 0.5, col, num, 13)
    add_text_box(s2, 1.4, yy + 0.04, 7.8, 0.3, title, font_name=FONT_BODY, font_size=12.5, color=C_NAVY, bold=True)
    add_text_box(s2, 1.4, yy + 0.33, 7.8, 0.28, desc, font_name=FONT_BODY, font_size=10, color=C_TEXT_LIGHT)


# ===========================================================================
# SLIDE 3: BỐI CẢNH & CÚ SỐc THỰC NGHIỆM (TẠI SAO KHÔNG DẠY "BẤM NÚT"?)
# ===========================================================================
s3 = prs.slides.add_slide(blank_layout)
add_content_frame(s3, "01. Bối cảnh & Triết lý đào tạo", "KHOẢNG CÁCH NGUY HIỂM KHI DÙNG AI MÀ THIẾU PHƯƠNG PHÁP", 3)

# Left card: Empirical data
add_card_with_header(s3, 0.5, 1.25, 4.35, 3.75, C_RED, "BẰNG CHỨNG KHOA HỌC BÁO ĐỘNG (2025 - 2026)", C_LIGHT_RED, C_RED)
add_text_box(s3, 0.65, 1.75, 4.05, 0.55, "1 / 277 bài báo trên PubMed",
             font_name=FONT_TITLE, font_size=20, color=C_RED, bold=True, align=PP_ALIGN.CENTER)
add_bullets_box(s3, 0.65, 2.3, 4.05, 2.6, [
    ("Topaz và cs. (The Lancet, 5/2026):", "Kiểm tra 2,5 triệu bài báo (97 triệu trích dẫn), tỷ lệ bài dính trích dẫn bịa tăng gấp 10 lần từ 1/2.828 (2023) lên 1/277 (đầu 2026)."),
    ("Linardon và cs. (JMIR Ment Health, 2025):", "GPT-4o bịa hoàn toàn 19,9% trích dẫn; tính cả sai thông tin thư mục là 56,3% (99/176)."),
    ("Bịa nhiều nhất ở đề tài chuyên sâu:", "Tỷ lệ bịa vọt từ 6% lên 28% - 29% ở các đề tài ít được nghiên cứu (đúng chỗ SV làm khóa luận cần nhất!)."),
    ("Vụ GS. Jeff Hancock (ĐH Stanford, 1/2025):", "Bị tòa án bác bỏ toàn bộ bản khai chuyên gia vì lọt 2 trích dẫn do AI bịa.")
], font_size=9.8)

# Right card: Two cognitive traps for HUB students
add_card_with_header(s3, 5.15, 1.25, 4.35, 3.75, C_NAVY, "HAI CÁI BẪY NHẬN THỨC ĐỐI VỚI SINH VIÊN", C_OFF_WHITE, C_NAVY)
add_bullets_box(s3, 5.3, 1.8, 4.05, 3.1, [
    ("1. Ảo tưởng trôi chảy (Fluency Illusion):", "Thấy AI viết bài tiểu luận 1.500 chữ trong 30 giây rất mượt mà nên tưởng mình đã hiểu. Thực chất não bộ không có 'ma sát nhận thức' nên quên 80% sau 24 giờ và không trả lời được khi giảng viên hỏi."),
    ("2. Lệ thuộc nhận thức (Cognitive Offloading):", "Giao phó việc lập dàn ý, suy luận và viết kết luận cho máy làm teo dần năng lực tư duy cấu trúc độc lập."),
    ("3. Rủi ro Pháp lý & Bảo mật dữ liệu:", "Thông tư 49/2026/TT-BGDĐT (hiệu lực 15/8/2026) quy định giấu việc dùng AI là vi phạm liêm chính học thuật; tải dữ liệu khách hàng ngân hàng lên AI công cộng vi phạm Luật Bảo vệ dữ liệu cá nhân 2025.")
], font_size=10)


# ===========================================================================
# SLIDE 4: TRIẾT LÝ SƯ PHẠM & 4 TRỤ CỘT NĂNG LỰC CỦA HỌC PHẦN
# ===========================================================================
s4 = prs.slides.add_slide(blank_layout)
add_content_frame(s4, "01. Bối cảnh & Triết lý đào tạo", "TRIẾT LÝ: TƯ DUY -> KỸ NĂNG -> CÔNG CỤ & 4 TRỤ CỘT CỐT LÕI", 4)

# Top banner: Philosophy
add_rect(s4, 0.5, 1.22, 9.0, 0.82, C_LIGHT_ACCENT, C_ACCENT, 1)
add_text_box(s4, 0.65, 1.26, 8.7, 0.74,
             "TRIẾT LÝ XUYÊN SUỐT:  [1. TƯ DUY LÀM CHỦ]   --->   [2. KỸ NĂNG HỆ THỐNG]   --->   [3. CÔNG CỤ LINH HOẠT]\n"
             "AI đề xuất  |  Bạn quyết định  |  Bạn chịu trách nhiệm  (Phép thử: Nếu AI làm sai bước này mà bạn không phát hiện được -> Đừng giao!)",
             font_name=FONT_BODY, font_size=11, color=C_NAVY, bold=True, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)

# 4 Pillars (2x2 grid)
pillars = [
    (0.5, 2.2, C_RED, "TRỤ CỘT 1: BẢN CHẤT AI, PROMPT, CONTEXT & HARNESS", [
        ("Hiểu bản chất xác suất:", "AI là máy đoán chữ, không phải kho sự thật."),
        ("Từ Prompt đến Context:", "Khung CRISP, 5 kỹ thuật nâng cao & chốt chặn 'Không suy đoán'."),
        ("Kiến trúc Harness:", "Xây 'bộ dây cương' có cổng dừng GATE & xử lý thiếu dữ liệu FALLBACK.")
    ]),
    (5.1, 2.2, C_ACCENT, "TRỤ CỘT 2: SECOND BRAIN & PHÁT TRIỂN SỰ HỌC", [
        ("Kiến trúc PARA & CODE:", "Ngoại hóa tri thức, chống 'nghĩa địa file số'."),
        ("Ghi chú nguyên tử (Atomic Notes):", "1 ghi chú = 1 luận điểm viết bằng ngôn từ riêng + Phản tư 4F."),
        ("Tích hợp RAG (Gemini Notebook):", "Biến AI thành 'Thư ký trung thành' trích dẫn tận dòng.")
    ]),
    (0.5, 3.68, C_GREEN, "TRỤ CỘT 3: AI TRONG NGHIÊN CỨU KHOA HỌC & KIỂM CHỨNG", [
        ("Quy trình 4 bước:", "Tìm -> Đọc -> Tổng hợp -> Viết (Kiểm chứng xuyên suốt)."),
        ("Kỹ năng 'Soi 3 phút':", "Đối chiếu số liệu, truy chỗ AI tự bịa thêm (case Hemani 2026)."),
        ("Màng lọc 3 lớp:", "Checklist 5 bước + Công cụ Tomaca + Khóa chốt Zotero 8.")
    ]),
    (5.1, 3.68, C_ORANGE, "TRỤ CỘT 4: AN TOÀN, ĐẠO ĐỨC & PHÁP LÝ (THÔNG TƯ 49/2026)", [
        ("Pháp lý Việt Nam & Quốc tế:", "Thông tư 49/2026 (Điều 10), Luật AI 134/2025, COPE/ICMJE."),
        ("Đèn giao thông & Khai báo:", "Phân vùng Xanh - Vàng - Đỏ & Mẫu câu khai báo AI chuẩn."),
        ("Bảo mật dữ liệu Ngân hàng:", "Khử định danh & chỉ gửi Schema trước khi phân tích.")
    ])
]

for x, y, col, title, items in pillars:
    add_left_border_card(s4, x, y, 4.4, 1.36, col, C_OFF_WHITE, title, items)


# ===========================================================================
# SLIDE 5: CHUẨN ĐẦU RA HỌC PHẦN (CLO1 - CLO5) & LIÊN KẾT ĐÁNH GIÁ
# ===========================================================================
s5 = prs.slides.add_slide(blank_layout)
add_content_frame(s5, "02. Chuẩn đầu ra & Lộ trình 11 buổi", "5 CHUẨN ĐẦU RA (CLO) Ở MỨC VẬN DỤNG, ĐÁNH GIÁ & SÁNG TẠO", 5)

clos = [
    ("CLO1", "Phân tích (Mức 4)", "Bản chất AI & Phân vai Người - Máy",
     "Giải thích cơ chế xác suất LLM, nguyên nhân Hallucination, Cognitive Offloading và lập bảng phân vai 'Việc nào giao - Việc nào giữ'.",
     "Chấm qua: Hồ sơ Đề án (Phần 1) & Vấn đáp bảo vệ"),
    ("CLO2", "Sáng tạo (Mức 5-6)", "Thiết kế Prompt - Context - Harness",
     "Viết câu lệnh chuẩn CRISP + kỹ thuật nâng cao, làm sạch Context và đóng gói bộ khung điều phối AI (Harness) có cổng GATE & FALLBACK.",
     "Chấm qua: Hồ sơ Đề án (Mảnh ghép 1) & Live Demo"),
    ("CLO3", "Vận dụng (Mức 3)", "Xây dựng Second Brain & Kho RAG",
     "Tổ chức tri thức theo PARA/CODE, tự viết hệ thống Atomic Notes + phản tư 4F và kết nối với Gemini Notebook / Claude Projects.",
     "Chấm qua: Hồ sơ Cá nhân (30% điểm - >= 6 Atomic Notes)"),
    ("CLO4", "Đánh giá (Mức 5)", "Nghiên cứu Khoa học & Kiểm chứng 5 Bước",
     "Thực hiện Tìm - Đọc - Tổng hợp - Viết; thực thi kỹ năng 'Soi 3 phút', Checklist 5 bước, công cụ Tomaca và quản lý trích dẫn bằng Zotero 8.",
     "Chấm qua: Hồ sơ Đề án (Mảnh ghép 3) & Kiểm toán chéo"),
    ("CLO5", "Đánh giá (Mức 5)", "Đạo đức Học thuật, Pháp lý & Bảo mật Dữ liệu",
     "Phân loại rủi ro theo Đèn giao thông (Xanh-Vàng-Đỏ), khử định danh dữ liệu ngân hàng và viết Bản khai báo AI đúng Điều 10 Thông tư 49/2026.",
     "Chấm qua: Hồ sơ Đề án (Mảnh ghép 4) & Kiểm toán chéo")
]

for idx, (code, bloom, name, desc, assess) in enumerate(clos):
    yy = 1.22 + idx * 0.78
    add_rect(s5, 0.5, yy, 9.0, 0.70, C_OFF_WHITE, C_LIGHT_GRAY, 0.75)
    add_rect(s5, 0.5, yy, 1.15, 0.70, C_NAVY if idx % 2 == 0 else C_RED)
    add_text_box(s5, 0.52, yy + 0.06, 1.11, 0.58, f"{code}\n{bloom}",
                 font_name=FONT_BODY, font_size=9.5, color=C_WHITE, bold=True,
                 align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)
    add_text_box(s5, 1.75, yy + 0.04, 4.9, 0.26, name, font_name=FONT_BODY, font_size=11.5, color=C_NAVY, bold=True)
    add_text_box(s5, 1.75, yy + 0.30, 5.1, 0.36, desc, font_name=FONT_BODY, font_size=9.5, color=C_TEXT_DARK)
    add_rect(s5, 6.95, yy + 0.1, 2.45, 0.50, C_LIGHT_ACCENT, C_ACCENT, 0.5)
    add_text_box(s5, 7.0, yy + 0.12, 2.35, 0.46, assess,
                 font_name=FONT_BODY, font_size=9, color=C_ACCENT, bold=True,
                 align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)


# ===========================================================================
# SLIDE 6: BẢN ĐỒ LỘ TRÌNH 11 BUỔI HỌC (44 TIẾT) & 4 CỘT MỐC ĐỀ ÁN
# ===========================================================================
s6 = prs.slides.add_slide(blank_layout)
add_content_frame(s6, "02. Chuẩn đầu ra & Lộ trình 11 buổi", "BẢN ĐỒ TỔNG THỂ 11 BUỔI (44 TIẾT) GẮN VỚI 4 MẢNH GHÉP ĐỀ ÁN", 6)

modules_overview = [
    ("MODULE 1 (Buổi 1 - 3)\n12 Tiết", C_RED, C_LIGHT_RED,
     "BẢN CHẤT AI, PROMPT,\nCONTEXT & HARNESS",
     "• Buổi 1: Bản chất xác suất LLM, Hallucination (1/277) & Phân vai.\n"
     "• Buổi 2: Khung CRISP, 5 kỹ thuật nâng cao & Context Engineering.\n"
     "• Buổi 3: Kiến trúc Harness (GATE & FALLBACK) + Gia sư Socrates.",
     "CHỐT MẢNH GHÉP 1 (Buổi 3):\nBộ Harness Nghiệp vụ vượt 3 kịch bản test"),
    ("MODULE 2 (Buổi 4 - 5)\n8 Tiết", C_ACCENT, C_LIGHT_ACCENT,
     "SECOND BRAIN &\nKHO TRI THỨC RAG",
     "• Buổi 4: Kiến trúc PARA, luồng CODE, viết Atomic Notes & phản tư 4F.\n"
     "• Buổi 5: Bản chất RAG (Thư ký trung thành), Gemini Notebook & truy vấn chéo đa tài liệu.",
     "CHỐT MẢNH GHÉP 2 (Buổi 5):\nKho Second Brain + RAG & Tiến độ Atomic Notes"),
    ("MODULE 3 (Buổi 6 - 8)\n12 Tiết", C_GREEN, C_LIGHT_GREEN,
     "AI TRONG NCKH &\nKIỂM CHỨNG 5 BƯỚC",
     "• Buổi 6: Tìm nguồn thật (Semantic/Elicit/Consensus) & 'Soi 3 phút'.\n"
     "• Buổi 7: Quy luật Linardon, Checklist 5 bước, Tomaca & Zotero 8.\n"
     "• Buổi 8: Ma trận tổng hợp (Synthesis), Viết 4 nhịp & Làm slide 4 lớp.",
     "CHỐT MẢNH GHÉP 3 (Buổi 8):\nBáo cáo NCKH/Nghiệp vụ + 100% nguồn Zotero"),
    ("MODULE 4 (Buổi 9 - 11)\n12 Tiết", C_ORANGE, C_LIGHT_ORANGE,
     "ĐẠO ĐỨC, PHÁP LÝ,\nKIỂM TOÁN & BẢO VỆ",
     "• Buổi 9: Thông tư 49/2026 (Điều 10), COPE, Bảo mật & Khai báo AI.\n"
     "• Buổi 10: Studio Kiểm toán chéo 3 vòng giữa các nhóm (Peer Audit).\n"
     "• Buổi 11: Bảo vệ Đề án, Vấn đáp cá nhân & Tổng kết hành trình.",
     "CHỐT MẢNH GHÉP 4 & BẢO VỆ:\nKhai báo Thông tư 49 + Kiểm toán chéo (100% điểm)")
]

for idx, (m_tag, col, bg_col, m_title, m_sessions, m_mile) in enumerate(modules_overview):
    xx = 0.5 + idx * 2.32
    add_rect(s6, xx, 1.22, 2.18, 3.82, C_WHITE, col, 1.25)
    add_rect(s6, xx, 1.22, 2.18, 0.52, col)
    add_text_box(s6, xx + 0.05, 1.24, 2.08, 0.48, m_tag,
                 font_name=FONT_BODY, font_size=10, color=C_WHITE, bold=True,
                 align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)
    add_text_box(s6, xx + 0.08, 1.80, 2.02, 0.52, m_title,
                 font_name=FONT_BODY, font_size=10.5, color=col, bold=True,
                 align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)
    add_text_box(s6, xx + 0.08, 2.36, 2.02, 1.72, m_sessions,
                 font_name=FONT_BODY, font_size=9.2, color=C_TEXT_DARK, line_spacing=1.15)
    add_rect(s6, xx + 0.06, 4.15, 2.06, 0.82, bg_col, col, 0.75)
    add_text_box(s6, xx + 0.1, 4.18, 1.98, 0.76, m_mile,
                 font_name=FONT_BODY, font_size=8.8, color=col, bold=True,
                 align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)


# ===========================================================================
# SLIDE 7: CHI TIẾT MODULE 1 & MODULE 2 (BUỔI 1 ĐẾN BUỔI 5)
# ===========================================================================
s7 = prs.slides.add_slide(blank_layout)
add_content_frame(s7, "02. Chuẩn đầu ra & Lộ trình 11 buổi", "LỘ TRÌNH CHI TIẾT BUỔI 1 - 5: TỪ PROMPT-HARNESS ĐẾN SECOND BRAIN", 7)

rows_b1_5 = [
    ("Buổi 1\n(4 tiết)", "Bản chất AI & Tư duy người làm chủ: 'AI là Trợ lý, Bạn là Chủ'",
     "Cơ chế xác suất LLM; Hallucination (Topaz 1/277); Cognitive Offloading & Fluency Illusion; Bảng phân vai Người - AI.",
     "Khởi tạo LMS Hub; lập nhóm 3-4 SV; viết Atomic Note & phản tư 4F số 1."),
    ("Buổi 2\n(4 tiết)", "Từ Prompt Engineering đến Context Engineering: Giao diện Tư duy",
     "Khung CRISP 5 thành tố; 5 kỹ thuật nâng cao (CoT, Role, Few-shot, Iterative, Negative + 'Không suy đoán'); Thiết kế gói Context sạch.",
     "Chốt đề tài Đề án nhóm; thiết kế 3 cụm Prompt CRISP + danh mục Context."),
    ("Buổi 3\n(4 tiết)", "Kiến trúc Harness: Xây dựng 'Bộ dây cương' điều phối AI",
     "Phân biệt Prompt - Context - Harness; Thiết kế cổng dừng GATE (🔒) & FALLBACK (❓); Xây dựng Gia sư Socrates với 4 kỹ thuật học sâu.",
     "HOÀN THÀNH MẢNH GHÉP 1: Đóng gói & test 3 kịch bản Bộ Harness của Đề án."),
    ("Buổi 4\n(4 tiết)", "Kiến trúc Second Brain (PARA & CODE) và Ghi chú nguyên tử",
     "Ngoại hóa tri thức; Tổ chức theo hành động PARA; Luồng CODE; Kỹ thuật viết Atomic Note (100% ngôn từ riêng, tiêu đề khẳng định) & 4F.",
     "Dựng không gian Second Brain; viết 3 Atomic Notes đầu tiên; mở kho nhóm."),
    ("Buổi 5\n(4 tiết)", "Tích hợp Second Brain với Công nghệ RAG (Gemini Notebook)",
     "Bản chất RAG (Thư ký trung thành có trích dẫn) vs LLM thuần; Truy vấn chéo đa tài liệu; Vòng lặp Second Brain <-> RAG; Cảnh báo Grounded Garbage.",
     "HOÀN THÀNH MẢNH GHÉP 2: Dựng kho RAG Đề án & Rà soát tiến độ giữa khóa.")
]

# Header row
add_rect(s7, 0.5, 1.20, 9.0, 0.36, C_NAVY)
add_text_box(s7, 0.55, 1.23, 0.85, 0.3, "BUỔI", font_size=10, color=C_WHITE, bold=True, align=PP_ALIGN.CENTER)
add_text_box(s7, 1.45, 1.23, 2.55, 0.3, "CHỦ ĐỀ TRỌNG TÂM", font_size=10, color=C_WHITE, bold=True)
add_text_box(s7, 4.05, 1.23, 3.15, 0.3, "TƯ DUY & KỸ NĂNG CỐT LÕI", font_size=10, color=C_WHITE, bold=True)
add_text_box(s7, 7.25, 1.23, 2.2, 0.3, "SẢN PHẨM LMS & ĐỀ ÁN", font_size=10, color=C_WHITE, bold=True)

for idx, (b_num, b_title, b_skill, b_out) in enumerate(rows_b1_5):
    yy = 1.60 + idx * 0.70
    bg = C_OFF_WHITE if idx % 2 == 0 else C_WHITE
    is_mile = "MẢNH GHÉP" in b_out
    add_rect(s7, 0.5, yy, 9.0, 0.66, bg, C_LIGHT_GRAY, 0.5)
    add_rect(s7, 0.5, yy, 0.9, 0.66, C_RED if idx < 3 else C_ACCENT)
    add_text_box(s7, 0.52, yy + 0.1, 0.86, 0.46, b_num, font_size=9.5, color=C_WHITE, bold=True, align=PP_ALIGN.CENTER)
    add_text_box(s7, 1.45, yy + 0.05, 2.55, 0.56, b_title, font_size=9.8, color=C_NAVY, bold=True)
    add_text_box(s7, 4.05, yy + 0.05, 3.15, 0.56, b_skill, font_size=9.2, color=C_TEXT_DARK)
    if is_mile:
        add_rect(s7, 7.22, yy + 0.04, 2.24, 0.58, C_LIGHT_GREEN, C_GREEN, 0.75)
        add_text_box(s7, 7.26, yy + 0.06, 2.16, 0.54, b_out, font_size=8.8, color=C_GREEN, bold=True)
    else:
        add_text_box(s7, 7.25, yy + 0.05, 2.2, 0.56, b_out, font_size=9.0, color=C_TEXT_MID)


# ===========================================================================
# SLIDE 8: CHI TIẾT MODULE 3 & MODULE 4 (BUỔI 6 ĐẾN BUỔI 11)
# ===========================================================================
s8 = prs.slides.add_slide(blank_layout)
add_content_frame(s8, "02. Chuẩn đầu ra & Lộ trình 11 buổi", "LỘ TRÌNH CHI TIẾT BUỔI 6 - 11: NCKH, KIỂM CHỨNG, ĐẠO ĐỨC & BẢO VỆ", 8)

rows_b6_11 = [
    ("Buổi 6\n(4 tiết)", "NCKH với AI (Bước 1 & 2): Tìm nguồn thật & 'Soi 3 phút'",
     "Quy tắc 'Nguồn thật trước, AI sau'; Phễu câu hỏi; Semantic Scholar, Elicit, Consensus; Prompt 7 mục & 'Soi 3 phút' (Case Hemani 2026).",
     "Mỗi SV tìm 3 bài thật, chạy tóm tắt 7 mục & lập Biên bản Soi 3 phút."),
    ("Buổi 7\n(4 tiết)", "Trích dẫn bịa, Checklist 5 bước, Tomaca & Zotero 8",
     "Quy tắc 'Chưa kiểm chứng, chưa vào bài'; Quy luật Linardon (19,9% / 29%); Checklist 5 bước; Thực hành Tomaca (Máy soát người quyết) & Zotero 8.",
     "Kiểm chứng đủ 9-12 nguồn của Đề án qua 5 bước + Tomaca & nạp Zotero."),
    ("Buổi 8\n(4 tiết)", "NCKH với AI (Bước 3 & 4): Tổng hợp, Viết & Trình bày",
     "Phân biệt Summary vs Synthesis; Lập Ma trận Tổng hợp tìm Research Gap; Viết học thuật 4 nhịp chèn Zotero; Làm slide 4 lớp.",
     "HOÀN THÀNH MẢNH GHÉP 3: Bản thảo Báo cáo có Ma trận tổng hợp & Zotero."),
    ("Buổi 9\n(4 tiết)", "Đạo đức, Pháp lý (Thông tư 49/2026) & An toàn dữ liệu",
     "Thông tư 49/2026/TT-BGDĐT (Điều 10); Luật AI 134/2025; COPE/ICMJE; Vụ GS Hancock; Đèn giao thông (Xanh-Vàng-Đỏ); Khử định danh & Mẫu khai báo.",
     "HOÀN THÀNH MẢNH GHÉP 4: Bảng bảo mật dữ liệu & Bản khai báo Thông tư 49."),
    ("Buổi 10\n(4 tiết)", "Project Clinic & Studio Kiểm toán chéo (Peer Audit)",
     "Kỹ năng Kiểm toán học thuật (Red-Teaming) 3 vòng: Stress-test bộ Harness nhóm bạn, quét Tomaca & mở PDF gốc kiểm tra Checklist 5 bước.",
     "Nộp trọn bộ Hồ sơ Đề án 4 mảnh ghép & Biên bản Kiểm toán chéo (15% điểm)."),
    ("Buổi 11\n(4 tiết)", "Bảo vệ Đề án Cuối khóa (Showcase), Phản biện & Tổng kết",
     "Thuyết trình & Live Demo bộ Harness; Tranh biện cùng Hội đồng Kiểm toán chéo; Vấn đáp chỉ định từng cá nhân trên Second Brain.",
     "CHẤM TỔNG KẾT CUỐI KHÓA (100% ĐIỂM) & Cam kết Người làm chủ AI.")
]

add_rect(s8, 0.5, 1.20, 9.0, 0.34, C_NAVY)
add_text_box(s8, 0.55, 1.22, 0.85, 0.28, "BUỔI", font_size=9.5, color=C_WHITE, bold=True, align=PP_ALIGN.CENTER)
add_text_box(s8, 1.45, 1.22, 2.55, 0.28, "CHỦ ĐỀ TRỌNG TÂM", font_size=9.5, color=C_WHITE, bold=True)
add_text_box(s8, 4.05, 1.22, 3.15, 0.28, "TƯ DUY & KỸ NĂNG CỐT LÕI", font_size=9.5, color=C_WHITE, bold=True)
add_text_box(s8, 7.25, 1.22, 2.2, 0.28, "SẢN PHẨM LMS & ĐỀ ÁN", font_size=9.5, color=C_WHITE, bold=True)

for idx, (b_num, b_title, b_skill, b_out) in enumerate(rows_b6_11):
    yy = 1.56 + idx * 0.60
    bg = C_OFF_WHITE if idx % 2 == 0 else C_WHITE
    is_mile = ("MẢNH GHÉP" in b_out) or ("100% ĐIỂM" in b_out)
    add_rect(s8, 0.5, yy, 9.0, 0.56, bg, C_LIGHT_GRAY, 0.5)
    add_rect(s8, 0.5, yy, 0.9, 0.56, C_GREEN if idx < 3 else C_ORANGE)
    add_text_box(s8, 0.52, yy + 0.06, 0.86, 0.44, b_num, font_size=9, color=C_WHITE, bold=True, align=PP_ALIGN.CENTER)
    add_text_box(s8, 1.45, yy + 0.03, 2.55, 0.50, b_title, font_size=9.2, color=C_NAVY, bold=True)
    add_text_box(s8, 4.05, yy + 0.03, 3.15, 0.50, b_skill, font_size=8.6, color=C_TEXT_DARK)
    if is_mile:
        add_rect(s8, 7.22, yy + 0.03, 2.24, 0.50, C_LIGHT_RED if idx == 5 else C_LIGHT_GREEN, C_RED if idx == 5 else C_GREEN, 0.75)
        add_text_box(s8, 7.26, yy + 0.04, 2.16, 0.48, b_out, font_size=8.4, color=C_RED if idx == 5 else C_GREEN, bold=True)
    else:
        add_text_box(s8, 7.25, yy + 0.03, 2.2, 0.50, b_out, font_size=8.5, color=C_TEXT_MID)


# ===========================================================================
# SLIDE 9: SECTION DIVIDER — CHIẾN LƯỢC ĐÁNH GIÁ CUỐI KHÓA (100% ĐIỂM)
# ===========================================================================
s9 = prs.slides.add_slide(blank_layout)
set_slide_bg(s9, C_NAVY)
add_rect(s9, 0, 0, 10.0, 0.06, C_GOLD)
add_text_box(s9, 0.5, 1.05, 9.0, 0.9, "PHẦN TRỌNG TÂM",
             font_name=FONT_BODY, font_size=14, color=C_GOLD, bold=True, align=PP_ALIGN.CENTER)
add_text_box(s9, 0.5, 1.55, 9.0, 1.2,
             "CHIẾN LƯỢC ĐÁNH GIÁ HỌC PHẦN (100% CUỐI KHÓA)",
             font_name=FONT_TITLE, font_size=28, color=C_WHITE, bold=True, align=PP_ALIGN.CENTER)
add_rect(s9, 3.2, 2.65, 3.6, 0.04, C_GOLD)
add_text_box(s9, 1.0, 2.95, 8.0, 1.4,
             "Đặc thù lớp Chứng chỉ chuẩn đầu ra bắt buộc để tốt nghiệp tại HUB:\n"
             "• Không chia điểm quá trình và điểm thi trắc nghiệm rời rạc như môn chính quy.\n"
             "• Đánh giá 100% qua ĐỀ ÁN TÍCH HỢP LŨY TIẾN (CAPSTONE PORTFOLIO)\n"
             "  kết hợp THUYẾT TRÌNH, VẤN ĐÁP CÁ NHÂN & KIỂM TOÁN CHÉO GIỮA CÁC NHÓM.",
             font_name=FONT_BODY, font_size=13.5, color=C_LIGHT_GRAY, align=PP_ALIGN.CENTER, line_spacing=1.35)


# ===========================================================================
# SLIDE 10: BỨC TRANH TỔNG THỂ CƠ CẤU 100% ĐIỂM CUỐI KHÓA (40% - 30% - 30%)
# ===========================================================================
s10 = prs.slides.add_slide(blank_layout)
add_content_frame(s10, "03. Chiến lược Đánh giá Cuối khóa (100%)", "CƠ CẤU 100% ĐIỂM HẾT MÔN: KẾT HỢP KẾT QUẢ NHÓM & NĂNG LỰC CÁ NHÂN", 10)

add_text_box(s10, 0.5, 1.18, 9.0, 0.35,
             "Mỗi sinh viên nhận 01 điểm tổng kết hết môn (thang 10, Đạt chứng chỉ khi >= 5,0 và không vi phạm Điểm liệt) cấu thành từ 3 phần:",
             font_name=FONT_BODY, font_size=11, color=C_TEXT_DARK, italic=True)

# 3 Cards for 40% - 30% - 30%
comp_cards = [
    (0.5, "CẤU PHẦN 1: HỒ SƠ ĐỀ ÁN NHÓM", "40%", "4,0 điểm / 10", C_NAVY, C_OFF_WHITE, [
        ("Hình thức:", "Chấm chung theo nhóm (3 - 4 SV cùng chuyên ngành)."),
        ("Sản phẩm nộp (Buổi 10):", "Bộ Hồ sơ Đề án Ứng dụng AI gồm 4 Mảnh ghép lũy tiến từ Buổi 1 đến Buổi 9."),
        ("Trọng tâm chấm:", "(1) Thiết kế Prompt-Context & Bộ Harness (15%); (2) Báo cáo nghiên cứu/nghiệp vụ có 9-12 nguồn Zotero đã kiểm chứng 5 bước + Tomaca (15%); (3) Bảo mật dữ liệu & Khai báo AI theo Thông tư 49/2026 (10%).")
    ]),
    (3.55, "CẤU PHẦN 2: DẤU ẤN CÁ NHÂN", "30%", "3,0 điểm / 10", C_RED, C_LIGHT_RED, [
        ("Hình thức:", "Chấm RIÊNG từng thành viên (Chống triệt để 'ăn theo nhóm'!)."),
        ("Kho Second Brain (15%):", "Mỗi cá nhân phải tự tay đóng góp >= 06 Atomic Notes (viết bằng ngôn từ riêng) vào Đề án & hoàn thành >= 80% Nhật ký 4F + Quiz trên LMS."),
        ("Vấn đáp chỉ định (15%):", "Tại Buổi 11, Giảng viên chỉ định ngẫu nhiên BẤT KỲ thành viên nào giải thích bản chất hoặc thao tác live trên Harness/Zotero.")
    ]),
    (6.6, "CẤU PHẦN 3: BẢO VỆ & KIỂM TOÁN", "30%", "3,0 điểm / 10", C_GREEN, C_LIGHT_GREEN, [
        ("Hình thức:", "Thực hiện tại Studio Buổi 10 và Hội đồng Buổi 11."),
        ("Thuyết trình & Demo (15%):", "Nhóm trình bày giải pháp (8-10 phút), Live Demo bộ Harness dừng đúng cổng GATE và trả lời phản biện."),
        ("Kiểm toán chéo nhóm bạn (15%):", "Đóng vai 'Hội đồng Kiểm toán' dùng Stress-test, Tomaca & Checklist 5 bước đi 'soi' đề án của nhóm đối tác.")
    ])
]

for xx, c_title, pct, pts, col, bg_col, items in comp_cards:
    add_rect(s10, xx, 1.58, 2.9, 3.45, bg_col, col, 1.25)
    add_rect(s10, xx, 1.58, 2.9, 0.42, col)
    add_text_box(s10, xx + 0.06, 1.60, 2.78, 0.38, c_title,
                 font_name=FONT_BODY, font_size=10.5, color=C_WHITE, bold=True,
                 align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)
    add_text_box(s10, xx + 0.1, 2.04, 1.3, 0.5, pct,
                 font_name=FONT_TITLE, font_size=26, color=col, bold=True, align=PP_ALIGN.CENTER)
    add_text_box(s10, xx + 1.35, 2.15, 1.45, 0.35, f"({pts})",
                 font_name=FONT_BODY, font_size=11, color=C_TEXT_MID, bold=True)
    add_rect(s10, xx + 0.15, 2.58, 2.6, 0.02, col)
    add_bullets_box(s10, xx + 0.1, 2.66, 2.7, 2.3, items, font_size=9.5, space_after=3)


# ===========================================================================
# SLIDE 11: GIẢI PHẪU 4 MẢNH GHÉP LŨY TIẾN CỦA HỒ SƠ ĐỀ ÁN (CẤU PHẦN 1 - 40%)
# ===========================================================================
s11 = prs.slides.add_slide(blank_layout)
add_content_frame(s11, "04. Giải phẫu Đề án & Kiểm toán chéo", "4 MẢNH GHÉP LŨY TIẾN CỦA ĐỀ ÁN: LÀM TỚI ĐÂU, XONG TỚI ĐÓ!", 11)

add_text_box(s11, 0.5, 1.16, 9.0, 0.32,
             "Sinh viên KHÔNG đợi đến tuần cuối mới làm đề án. Đề án cuối khóa được lắp ghép trực tiếp từ sản phẩm thực hành của 4 Module:",
             font_name=FONT_BODY, font_size=10.5, color=C_TEXT_DARK, italic=True)

milestones = [
    (0.5, 1.54, C_RED, "MẢNH GHÉP 1 (Chốt ở Buổi 3): KIẾN TRÚC PROMPT - CONTEXT - HARNESS", [
        ("Bảng phân vai Người - AI:", "Phân rã bài toán nghiệp vụ (Tài chính, Ngân hàng, Kế toán, Marketing...) theo nguyên tắc kiểm soát lỗi."),
        ("Bộ 3 cụm Prompt CRISP & Context:", "Tích hợp CoT, Few-shot, Iterative và chốt chặn 'Không suy đoán'."),
        ("Đóng gói Bộ Harness sống:", "Cài đặt trên Claude Project / Gemini Gem có cổng dừng GATE (🔒) & FALLBACK (❓), vượt 3 kịch bản test.")
    ]),
    (5.1, 1.54, C_ACCENT, "MẢNH GHÉP 2 (Chốt ở Buổi 5): HỆ THỐNG SECOND BRAIN & KHO RAG", [
        ("Kiến trúc PARA & CODE:", "Tổ chức cây thư mục tri thức của đề án trên Obsidian / Notion / Google Docs."),
        ("Đóng góp cá nhân bắt buộc:", "Mỗi thành viên tự viết tối thiểu 06 Atomic Notes (tiêu đề khẳng định, ngôn từ riêng, có liên kết [[...]])."),
        ("Tích hợp Kho RAG:", "Nạp tài liệu thật + Atomic Notes vào Gemini Notebook để truy vấn chéo có trích dẫn tận dòng.")
    ]),
    (0.5, 3.32, C_GREEN, "MẢNH GHÉP 3 (Chốt ở Buổi 8): BÁO CÁO NGHIÊN CỨU & KIỂM CHỨNG ZOTERO", [
        ("Ma trận Tổng hợp (Synthesis Matrix):", "Đối sánh 09 - 12 nguồn tài liệu thật (mỗi SV phụ trách >= 3 nguồn) tìm từ Semantic Scholar/Elicit/Consensus."),
        ("Hồ sơ Kiểm chứng:", "Ít nhất 02 Biên bản 'Soi 3 phút' + Bảng Checklist kiểm chứng 5 bước + Báo cáo quét trên công cụ Tomaca."),
        ("Khóa chốt Zotero 8:", "Báo cáo dài 2.500 - 4.000 chữ chèn trích dẫn tự động từ Zotero (gửi kèm file thư viện .bib / .ris).")
    ]),
    (5.1, 3.32, C_ORANGE, "MẢNH GHÉP 4 (Chốt ở Buổi 9): AN TOÀN DỮ LIỆU & KHAI BÁO THÔNG TƯ 49", [
        ("Ma trận Đèn giao thông (Xanh-Vàng-Đỏ):", "Phân loại rủi ro dữ liệu của đề án theo Checklist 3 câu hỏi an toàn dữ liệu."),
        ("Minh chứng Khử định danh:", "Đảm bảo 100% dữ liệu mẫu đưa vào AI đã xóa sạch thông tin định danh cá nhân (PII) / bí mật ngân hàng."),
        ("Bản Khai báo Sử dụng AI:", "Viết đúng chuẩn Điều 10 Thông tư 49/2026/TT-BGDĐT và chuẩn quốc tế COPE / ICMJE.")
    ])
]

for x, y, col, title, items in milestones:
    add_left_border_card(s11, x, y, 4.4, 1.66, col, C_OFF_WHITE, title, items)


# ===========================================================================
# SLIDE 12: CẤU PHẦN 2 (30% CÁ NHÂN) — CƠ CHẾ CHỐNG "ĂN THEO NHÓM" (FREE-RIDER)
# ===========================================================================
s12 = prs.slides.add_slide(blank_layout)
add_content_frame(s12, "04. Giải phẫu Đề án & Kiểm toán chéo", "CẤU PHẦN 2 (30% ĐIỂM CÁ NHÂN): TRIỆT TIÊU TÌNH TRẠNG 'ĂN THEO NHÓM'", 12)

# Left box: Why & How
add_card_with_header(s12, 0.5, 1.25, 4.35, 3.75, C_RED, "15% HỒ SƠ SECOND BRAIN CÁ NHÂN TRÊN LMS", C_LIGHT_RED, C_RED)
add_bullets_box(s12, 0.65, 1.78, 4.05, 3.1, [
    ("Mục tiêu:", "Đảm bảo không một sinh viên nào có thể nhận Chứng chỉ chuẩn đầu ra nếu chỉ đứng tên trong nhóm mà không thực hành."),
    ("06 Atomic Notes chuyên môn:", "Mỗi thành viên phải đứng tên tác giả ít nhất 06 Ghi chú nguyên tử trong kho Second Brain của Đề án (mã hóa theo MSSV: AN-2026-MSSV-01...)."),
    ("Tiêu chuẩn Atomic Note:", "Tiêu đề là 1 câu khẳng định sắc bén; nội dung 100-200 chữ viết bằng ngôn từ riêng (cấm copy-paste AI); có nguồn đã qua 5 bước kiểm chứng và có liên kết [[...]]."),
    ("Nhật ký Phản tư 4F & Quiz:", "Hoàn thành đều đặn Nhật ký 4F (Fact - Feelings - Findings - Future) và Quiz Active Recall sau mỗi buổi học trên LMS Hub.")
], font_size=10)

# Right box: Viva defense
add_card_with_header(s12, 5.15, 1.25, 4.35, 3.75, C_NAVY, "15% VẤN ĐÁP CHỈ ĐỊNH TRỰC TIẾP TẠI BUỔI 11", C_OFF_WHITE, C_NAVY)
add_bullets_box(s12, 5.3, 1.78, 4.05, 3.1, [
    ("Quy tắc 'Chỉ định bất kỳ':", "Khi nhóm lên bảo vệ ở Buổi 11, Giảng viên và Hội đồng Kiểm toán có quyền chỉ định BẤT KỲ thành viên nào trả lời hoặc thao tác máy tính (kể cả phần của bạn khác trong nhóm)."),
    ("3 Thử thách Vấn đáp nhanh tại bục giảng:", ""),
    ("Thử thách 1:", "Mở 1 Atomic Note của em và giải thích tại sao em kết nối nó với mục 2 của báo cáo?"),
    ("Thử thách 2:", "Mở thư viện Zotero của nhóm, bấm vào trích dẫn số X và thực hiện thao tác 'Soi 3 phút' ngay trên file PDF gốc."),
    ("Thử thách 3:", "Nhập một dữ liệu thiếu vào Bộ Harness của nhóm và giải thích cách cổng GATE / FALLBACK hoạt động.")
], font_size=10)


# ===========================================================================
# SLIDE 13: CẤU PHẦN 3 (30%) — CƠ CHẾ "KIỂM TOÁN CHÉO" (PEER AUDIT / RED-TEAMING)
# ===========================================================================
s13 = prs.slides.add_slide(blank_layout)
add_content_frame(s13, "04. Giải phẫu Đề án & Kiểm toán chéo", "CẤU PHẦN 3 (30%): BIẾN LỚP HỌC THÀNH HỘI ĐỒNG KIỂM TOÁN HỌC THUẬT", 13)

add_rect(s13, 0.5, 1.20, 9.0, 0.65, C_LIGHT_GREEN, C_GREEN, 1)
add_text_box(s13, 0.65, 1.24, 8.7, 0.57,
             "ĐIỂM ĐỘT PHÁ: Thay vì 'nhận xét chéo xã giao' (khen nhau cho vui), mỗi nhóm được phân công làm HỘI ĐỒNG KIỂM TOÁN (AUDITOR)\n"
             "cho 1 nhóm khác ở Buổi 10. Điểm của Nhóm Kiểm toán (15%) phụ thuộc vào độ sắc bén và bằng chứng khi 'soi' bài của nhóm bạn!",
             font_name=FONT_BODY, font_size=10.5, color=C_GREEN, bold=True, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)

audit_rounds = [
    (0.5, "VÒNG 1: KIỂM TOÁN HARNESS & SECOND BRAIN", C_RED, [
        ("Stress-test 3 kịch bản:", "Nhập dữ liệu chuẩn, dữ liệu thiếu (test FALLBACK ❓) và ra lệnh ép vượt rào (test GATE 🔒) trên bộ Harness của nhóm bạn."),
        ("Thẩm định Atomic Notes:", "Kiểm tra số lượng (>= 6 notes/người) và phát hiện xem có ghi chú nào là bản copy-paste thô từ AI không.")
    ]),
    (3.55, "VÒNG 2: KIỂM TOÁN NGUỒN (TOMACA + 5 BƯỚC)", C_ACCENT, [
        ("Quét tự động trên Tomaca:", "Đưa toàn bộ 9-12 tài liệu tham khảo của nhóm bạn lên Tomaca để tìm DOI giả hoặc metadata-mismatch."),
        ("Soi PDF gốc 3 trích dẫn:", "Bốc ngẫu nhiên 3 trích dẫn trọng yếu, mở bài báo gốc kiểm tra Bước 3 (bài có nói đúng ý đó không?) & Bước 4 (khớp số liệu bảng/hình không?).")
    ]),
    (6.6, "VÒNG 3: KIỂM TOÁN BẢO MẬT & THÔNG TƯ 49", C_ORANGE, [
        ("Rà soát An toàn dữ liệu:", "Kiểm tra xem hồ sơ và prompt của nhóm bạn có làm lộ dữ liệu cá nhân/ngân hàng chưa khử định danh không."),
        ("Đối chiếu Thông tư 49/2026:", "Kiểm tra Bản khai báo AI đã nêu đủ công cụ, phiên bản, thời gian, mục đích và cam kết trách nhiệm chưa.")
    ])
]

for xx, a_title, col, items in audit_rounds:
    add_card_with_header(s13, xx, 2.0, 2.9, 2.95, col, a_title, C_OFF_WHITE, col)
    add_bullets_box(s13, xx + 0.1, 2.48, 2.7, 2.4, items, font_size=9.8, space_after=6)


# ===========================================================================
# SLIDE 14: QUY TẮC "ĐIỂM LIỆT LIÊM CHÍNH" (ZERO-TOLERANCE INTEGRITY RULE)
# ===========================================================================
s14 = prs.slides.add_slide(blank_layout)
add_content_frame(s14, "04. Giải phẫu Đề án & Kiểm toán chéo", "QUY TẮC 'ĐIỂM LIỆT LIÊM CHÍNH' & KHUNG ĐÈN GIAO THÔNG SỬ DỤNG AI", 14)

# Top warning banner
add_rect(s14, 0.5, 1.22, 9.0, 0.95, C_LIGHT_RED, C_RED, 1.5)
add_text_box(s14, 0.65, 1.26, 8.7, 0.87,
             "CẢNH BÁO QUY TẮC ĐIỂM LIỆT LIÊM CHÍNH (ZERO-TOLERANCE INTEGRITY RULE):\n"
             "Nếu trong Hồ sơ Đề án chính thức nộp ở Buổi 10, Giảng viên hoặc Nhóm Kiểm toán chéo phát hiện BẤT KỲ 01 TÀI LIỆU THAM KHẢO NÀO LÀ BỊA\n"
             "(Fabricated Citation) chưa qua kiểm chứng, hoặc KHÔNG KHAI BÁO VIỆC DÙNG AI theo Điều 10 Thông tư 49/2026/TT-BGDĐT:\n"
             "--->  TRỪ THẲNG 50% ĐIỂM HỒ SƠ ĐỀ ÁN VÀ BẮT BUỘC LÀM LẠI PHẦN KIỂM CHỨNG MỚI ĐƯỢC XÉT CẤP CHỨNG CHỈ!",
             font_name=FONT_BODY, font_size=10.2, color=C_RED, bold=True, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)

# Traffic light 3 columns
lights = [
    (0.5, "VÙNG XANH — KHUYẾN KHÍCH DÙNG", C_GREEN, C_LIGHT_GREEN, [
        "Gợi ý từ khóa và hướng tìm kiếm ban đầu.",
        "Giải thích khái niệm, thuật ngữ khó để tự học (Gia sư Socrates).",
        "Phản biện dàn ý do chính bạn tự lập từ Second Brain.",
        "Rà soát lỗi chính tả, ngữ pháp tiếng Việt / tiếng Anh."
    ]),
    (3.55, "VÙNG VÀNG — DÙNG CÓ ĐIỀU KIỆN", C_ORANGE, C_LIGHT_ORANGE, [
        "Dịch tài liệu học thuật -> Phải đối chiếu lại bản PDF gốc.",
        "Tóm tắt bài báo bằng Prompt 7 mục -> Phải 'Soi 3 phút'.",
        "Hỗ trợ viết code R/Python/Excel -> Chỉ gửi Schema, tự chạy lại trên máy.",
        "BẮT BUỘC: Kiểm chứng 5 bước, tự viết lại & Khai báo AI."
    ]),
    (6.6, "VÙNG ĐỎ — CẤM TUYỆT ĐỐI", C_RED, C_LIGHT_RED, [
        "Để AI viết hộ phần Kết quả, Thảo luận, Kết luận.",
        "Đưa trích dẫn chưa qua 5 bước kiểm chứng & Zotero vào bài.",
        "Nộp bài do AI sinh ra mà không khai báo (Vi phạm Thông tư 49).",
        "Tải dữ liệu mật / thông tin định danh khách hàng thật lên AI công cộng."
    ])
]

for xx, l_title, col, bg_col, items in lights:
    add_card_with_header(s14, xx, 2.32, 2.9, 2.70, col, l_title, bg_col, col)
    add_bullets_box(s14, xx + 0.1, 2.80, 2.7, 2.15, items, font_size=9.5, space_after=4)


# ===========================================================================
# SLIDE 15: BẢNG RUBRIC CHẤM ĐIỂM CHI TIẾT 7 TIÊU CHÍ (THANG ĐIỂM 10)
# ===========================================================================
s15 = prs.slides.add_slide(blank_layout)
add_content_frame(s15, "04. Giải phẫu Đề án & Kiểm toán chéo", "MA TRẬN RUBRIC CHẤM ĐIỂM CHI TIẾT 7 TIÊU CHÍ (100% ĐIỂM CUỐI KHÓA)", 15)

rubric_rows = [
    ("1.1. Thiết kế Prompt, Context & Bộ Harness nghiệp vụ", "CLO1, 2", "15%",
     "Phân vai sắc bén; đủ khung CRISP + kỹ thuật nâng cao; Bộ Harness (Gem/Project) có cổng GATE & FALLBACK chạy mượt, vượt 3 kịch bản test."),
    ("1.2. Chất lượng Nghiên cứu, Tổng hợp & Kiểm chứng Zotero", "CLO4", "15%",
     "100% nguồn (9-12 nguồn) là nguồn thật quản lý bằng Zotero 8; có Ma trận tổng hợp, Biên bản Soi 3 phút, Checklist 5 bước & báo cáo Tomaca."),
    ("1.3. Hồ sơ An toàn dữ liệu & Bản khai báo Thông tư 49/2026", "CLO5", "10%",
     "Phân loại rủi ro dữ liệu theo Đèn giao thông; khử định danh dữ liệu mẫu; Bản khai báo AI chi tiết, đúng Điều 10 Thông tư 49/2026 & COPE."),
    ("2.1. Kho Second Brain & Atomic Notes cá nhân trên LMS", "CLO3", "15%",
     "[Chấm cá nhân] Hoàn thành >= 80% Quiz & phản tư 4F trên LMS; đóng góp >= 06 Atomic Notes chất lượng cao, ngôn từ riêng, có liên kết [[...]]."),
    ("2.2. Năng lực làm chủ khi Vấn đáp chỉ định tại Hội đồng", "CLO1-4", "15%",
     "[Chấm cá nhân] Trả lời lưu loát câu hỏi bất kỳ của GV/Hội đồng; giải thích được Atomic Note và thao tác live trên Harness/Zotero ngay tại bục."),
    ("3.1. Thuyết trình Bảo vệ & Live Demo Đề án của Nhóm", "CLO2, 4", "15%",
     "Slide thiết kế chuẩn 4 lớp ('AI làm draft, người làm final'); trình bày đúng giờ (8-10 phút); Live Demo bộ Harness & minh chứng kiểm chứng thuyết phục."),
    ("3.2. Phản biện & Báo cáo Kiểm toán chéo nhóm bạn", "CLO4, 5", "15%",
     "Thực hiện nghiêm túc 3 vòng Kiểm toán chéo nhóm đối tác; phát hiện chính xác điểm mạnh/lỗ hổng kèm bằng chứng trang gốc; đặt 2 câu hỏi sắc bén.")
]

add_rect(s15, 0.5, 1.18, 9.0, 0.34, C_NAVY)
add_text_box(s15, 0.55, 1.20, 2.75, 0.28, "TIÊU CHÍ ĐÁNH GIÁ", font_size=9.5, color=C_WHITE, bold=True)
add_text_box(s15, 3.35, 1.20, 0.7, 0.28, "CLO", font_size=9.5, color=C_WHITE, bold=True, align=PP_ALIGN.CENTER)
add_text_box(s15, 4.10, 1.20, 0.75, 0.28, "TRỌNG SỐ", font_size=9.5, color=C_WHITE, bold=True, align=PP_ALIGN.CENTER)
add_text_box(s15, 4.90, 1.20, 4.55, 0.28, "CHUẨN ĐẠT MỨC TỐT - XUẤT SẮC (8,0 - 10 ĐIỂM)", font_size=9.5, color=C_WHITE, bold=True)

for idx, (r_name, r_clo, r_w, r_desc) in enumerate(rubric_rows):
    yy = 1.54 + idx * 0.51
    bg = C_LIGHT_RED if "Chấm cá nhân" in r_desc else (C_OFF_WHITE if idx % 2 == 0 else C_WHITE)
    add_rect(s15, 0.5, yy, 9.0, 0.48, bg, C_LIGHT_GRAY, 0.5)
    add_text_box(s15, 0.55, yy + 0.03, 2.75, 0.42, r_name, font_size=9.0, color=C_NAVY, bold=True)
    add_text_box(s15, 3.35, yy + 0.08, 0.7, 0.32, r_clo, font_size=8.8, color=C_TEXT_MID, bold=True, align=PP_ALIGN.CENTER)
    add_rect(s15, 4.15, yy + 0.07, 0.65, 0.34, C_RED if "Chấm cá nhân" in r_desc else C_NAVY)
    add_text_box(s15, 4.15, yy + 0.08, 0.65, 0.32, r_w, font_size=9.2, color=C_WHITE, bold=True, align=PP_ALIGN.CENTER)
    add_text_box(s15, 4.90, yy + 0.03, 4.55, 0.42, r_desc, font_size=8.6, color=C_TEXT_DARK)


# ===========================================================================
# SLIDE 16: QUY TẮC VẬN HÀNH LỚP HỌC TRÊN LMS HUB & ĐIỀU KIỆN BẢO VỆ (GATEKEEPING)
# ===========================================================================
s16 = prs.slides.add_slide(blank_layout)
add_content_frame(s16, "05. Quy tắc Vận hành trên LMS Hub", "NHỊP HỌC 200 PHÚT & 3 ĐIỀU KIỆN GÁC CỔNG TRÊN HỆ THỐNG LMS HUB", 16)

# Left: 5 pedagogical steps per 200-minute session
add_card_with_header(s16, 0.5, 1.25, 4.35, 3.75, C_NAVY, "CẤU TRÚC 1 BUỔI HỌC 4 TIẾT (200 PHÚT)", C_OFF_WHITE, C_NAVY)
add_bullets_box(s16, 0.65, 1.75, 4.05, 3.15, [
    ("Trước buổi học (Prep-work trên LMS):", "Đọc trước eBook SCQA của chương và làm thử Vòng Test Level 1."),
    ("Nhịp 1 - Hook & Cái Biết (20 phút):", "Theo dõi hành trình nhân vật Minh tại HUB & khảo sát trải nghiệm thực tế."),
    ("Nhịp 2 - Va chạm & Khái niệm lõi (50 phút):", "Trực tiếp trải nghiệm tình huống AI sai/bịa, sau đó đúc kết nguyên lý & xem Live Demo."),
    ("Nhịp 3 - Thực hành & Studio Đề án (100 phút):", "Thực hành có hướng dẫn trên máy tính cá nhân; giải quyết trực tiếp từng mảnh ghép của Đề án nhóm ngay tại lớp."),
    ("Nhịp 4 - Phản tư 4F & Khóa chốt LMS (30 phút):", "Viết Nhật ký Atomic Note 4F, làm Quiz 5 lượt và gửi Feedback tải bài giảng.")
], font_size=9.8)

# Right: 3 Gatekeeping conditions
add_card_with_header(s16, 5.15, 1.25, 4.35, 3.75, C_RED, "3 ĐIỀU KIỆN BẮT BUỘC ĐỂ ĐƯỢC BẢO VỆ ĐỀ ÁN", C_LIGHT_RED, C_RED)
add_bullets_box(s16, 5.3, 1.75, 4.05, 3.15, [
    ("Điều kiện 1 - Hiện diện trên lớp (>= 80%):", "Tham dự tối thiểu 09 / 11 buổi học trực tiếp và tham gia đầy đủ hoạt động thảo luận, thực hành nhóm."),
    ("Điều kiện 2 - Cơ chế Điểm danh LMS Hub:", "Ở mỗi buổi học, một sinh viên chỉ được hệ thống LMS ghi nhận hoàn thành khi thực hiện đủ 2 thao tác:\n"
     "  (a) Gửi đánh giá Feedback buổi học CÓ KÈM NHẬN XÉT để mở khóa tải Slide/Bài giảng;\n"
     "  (b) Hoàn thành Quiz ôn tập (đạt 10/10 hoặc nỗ lực làm đủ 5 lượt Active Recall để mở khóa lời giải)."),
    ("Điều kiện 3 - Lịch sử Tích lũy Tri thức:", "Có đầy đủ nhật ký Atomic Notes & phản tư 4F tích lũy đều đặn qua từng tuần (Không chấp nhận đề án nộp trống không có lịch sử quá trình!).")
], font_size=9.8)


# ===========================================================================
# SLIDE 17: BỘ 5 CÔNG CỤ BIỂU MẪU (TOOLKITS) & HÀNH ĐỘNG NGAY HÔM NAY (BUỔI 1)
# ===========================================================================
s17 = prs.slides.add_slide(blank_layout)
add_content_frame(s17, "05. Quy tắc Vận hành trên LMS Hub", "BỘ 5 BIỂU MẪU THỰC HÀNH (TOOLKITS) & NHIỆM VỤ NGAY HÔM NAY", 17)

# Left: 5 Toolkits provided by instructor
add_card_with_header(s17, 0.5, 1.25, 4.5, 3.75, C_ACCENT, "5 BIỂU MẪU GIẢNG VIÊN CUNG CẤP SẴN TRÊN LMS", C_LIGHT_ACCENT, C_ACCENT)
add_bullets_box(s17, 0.65, 1.75, 4.2, 3.15, [
    ("Toolkit 1 (Mảnh ghép 1):", "Bảng phân vai Người - AI, Cheatsheet CRISP & Template System Instructions 4 khối cho Bộ Harness."),
    ("Toolkit 2 (Mảnh ghép 2):", "Template Ghi chú nguyên tử (Atomic Note) chuẩn OKF & Mẫu Nhật ký Phản tư 4F."),
    ("Toolkit 3 (Mảnh ghép 3a):", "Prompt Tóm tắt bài báo khoa học 7 mục & Biên bản 'Soi bản tóm tắt trong 3 phút'."),
    ("Toolkit 4 (Mảnh ghép 3b):", "Bảng Checklist Kiểm chứng Trích dẫn 5 bước, Hướng dẫn đọc Tomaca & Quy trình Zotero 8."),
    ("Toolkit 5 (Mảnh ghép 4 & Kiểm toán):", "Mẫu Bản Công bố Sử dụng AI theo Điều 10 Thông tư 49/2026/TT-BGDĐT & Biên bản Kiểm toán chéo 3 vòng.")
], font_size=9.8)

# Right: Checklist to do right in Session 1
add_card_with_header(s17, 5.2, 1.25, 4.3, 3.75, C_GREEN, "4 VIỆC CẦN LÀM NGAY TRONG BUỔI 1 HÔM NAY", C_LIGHT_GREEN, C_GREEN)
add_bullets_box(s17, 5.35, 1.75, 4.0, 3.15, [
    ("Bước 1 - Đăng nhập LMS Hub & Đổi mật khẩu:", "Truy cập đường link LMS của lớp, đăng nhập bằng MSSV và thiết lập Mục tiêu cam kết học tập cá nhân."),
    ("Bước 2 - Lập nhóm Đề án (3 - 4 SV cùng ngành):", "Chọn những người đồng đội cam kết kỷ luật; thảo luận 3 bài toán nghiệp vụ/nghiên cứu tiềm năng của ngành mình."),
    ("Bước 3 - Thực hành Bảng phân vai đầu tiên:", "Áp dụng ngay bài học Buổi 1 để phân định 'Việc nào giao AI - Việc nào giữ' cho bài toán của nhóm."),
    ("Bước 4 - Khóa chốt Buổi 1 trên LMS:", "Viết Nhật ký 4F số 1, làm Quiz Buổi 1 và gửi Feedback kèm nhận xét để tải tài liệu bài giảng.")
], font_size=10)


# ===========================================================================
# SLIDE 18: SLIDE KẾT & THÔNG ĐIỆP ĐỒNG HÀNH (NAVY SANDWICH)
# ===========================================================================
s18 = prs.slides.add_slide(blank_layout)
set_slide_bg(s18, C_NAVY)
add_rect(s18, 0, 0, 10.0, 0.07, C_GOLD)

add_text_box(s18, 0.6, 0.75, 8.8, 0.9,
             "\"AI CÓ THỂ LÀM NHANH HƠN, NHƯNG KHÔNG THỂ\nCHỊU TRÁCH NHIỆM THAY CHO DANH DỰ VÀ TƯƠNG LAI CỦA BẠN.\"",
             font_name=FONT_TITLE, font_size=21, color=C_WHITE, bold=True,
             align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE, line_spacing=1.25)

add_rect(s18, 3.2, 1.75, 3.6, 0.03, C_GOLD)

# 3 Takeaways cards on dark background
takeaways = [
    (0.5, "1. TƯ DUY -> KỸ NĂNG -> CÔNG CỤ",
     "Công cụ thay đổi mỗi ngày, nhưng tư duy điều phối (Prompt - Context - Harness) và Bộ Não Thứ Hai (Second Brain) sẽ đi theo bạn suốt đời."),
    (3.55, "2. NGUỒN THẬT & KIỂM CHỨNG 5 BƯỚC",
     "Nguồn thật trước, AI sau. Chưa qua 5 bước kiểm chứng và chưa vào thư viện Zotero 8 thì tuyệt đối chưa được vào báo cáo."),
    (6.6, "3. MINH BẠCH & LÀM CHỦ (THÔNG TƯ 49)",
     "Dùng AI thì khai báo đàng hoàng. Bảo mật tuyệt đối dữ liệu ngân hàng - khách hàng. AI là trợ lý, bạn là chủ!")
]

for xx, t_head, t_body in takeaways:
    add_rect(s18, xx, 2.0, 2.9, 1.95, C_DARK_NAVY, C_GOLD, 1)
    add_text_box(s18, xx + 0.1, 2.1, 2.7, 0.45, t_head,
                 font_name=FONT_BODY, font_size=11, color=C_GOLD, bold=True, align=PP_ALIGN.CENTER)
    add_text_box(s18, xx + 0.12, 2.6, 2.66, 1.25, t_body,
                 font_name=FONT_BODY, font_size=10, color=C_WHITE, align=PP_ALIGN.CENTER, line_spacing=1.25)

add_text_box(s18, 0.5, 4.2, 9.0, 0.5,
             "Tôi đã chuẩn bị trọn vẹn hệ thống học liệu cho các bạn. Các bạn đã sẵn sàng cam kết cho hành trình 11 buổi này chưa?",
             font_name=FONT_BODY, font_size=13, color=C_GOLD, italic=True, align=PP_ALIGN.CENTER)

add_text_box(s18, 0.5, 4.8, 9.0, 0.45,
             "ThS. Phó Hải Đăng  |  Khoa Hệ thống thông tin quản lý - Trường ĐH Ngân hàng TP.HCM (HUB)  |  Hỏi & Đáp (Q&A)",
             font_name=FONT_BODY, font_size=11, color=C_LIGHT_GRAY, align=PP_ALIGN.CENTER)

out_paths = [
    r"d:\PARA\Projects\second-brain\03-Domains\Teaching\ComputerScience\Ky Nang Ung Dung AI\Slide_00_Gioi_Thieu_De_Cuong_Va_Danh_Gia_HUB.pptx",
    r"d:\PARA\Projects\second-brain\05-Projects\lms-hub\courses\ky-nang-ai-hub\content\slides\Buoi_00_De_Cuong.pptx"
]

for p in out_paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    prs.save(p)
    print(f"Saved: {p}")
