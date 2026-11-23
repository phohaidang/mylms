# -*- coding: utf-8 -*-
"""
Generator tạo 3 bộ Slide Bài giảng chuyên sâu cho MODULE 1 (Buổi 1, Buổi 2, Buổi 3)
Mỗi buổi 20 slides (Tổng cộng 60 slides cho Module 1) xuất ra cả 2 định dạng:
- PowerPoint (.pptx) theo chuẩn Design System academic-presentation-vn (Navy/Red/Gold, Georgia/Calibri, 16:9 Card-based)
- Web Slide tương tác (.html) đồng bộ vào LMS Hub (cho phép SV tải về xem hoặc GV trình chiếu trực tiếp)
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ---------------------------------------------------------------------------
# DESIGN SYSTEM COLORS & FONTS
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
C_LIGHT_GRAY = RGBColor(0xE0, 0xE0, 0xE0)
C_TEXT_DARK = RGBColor(0x21, 0x21, 0x21)
C_TEXT_MID = RGBColor(0x42, 0x42, 0x42)
C_TEXT_LIGHT = RGBColor(0x75, 0x75, 0x75)

COLOR_MAP = {
    "navy": (C_NAVY, "#1B2558"),
    "dark_navy": (C_DARK_NAVY, "#111A40"),
    "white": (C_WHITE, "#FFFFFF"),
    "off_white": (C_OFF_WHITE, "#F5F6FA"),
    "red": (C_RED, "#C62828"),
    "light_red": (C_LIGHT_RED, "#FFEBEE"),
    "accent": (C_ACCENT, "#1565C0"),
    "light_accent": (C_LIGHT_ACCENT, "#E3F2FD"),
    "gold": (C_GOLD, "#F9A825"),
    "green": (C_GREEN, "#2E7D32"),
    "light_green": (C_LIGHT_GREEN, "#E8F5E9"),
    "orange": (C_ORANGE, "#E65100"),
    "light_orange": (C_LIGHT_ORANGE, "#FFF3E0"),
}

FONT_TITLE = "Georgia"
FONT_BODY = "Calibri"


def rgb(key):
    return COLOR_MAP.get(key, (C_NAVY, "#1B2558"))[0]


def hex_c(key):
    return COLOR_MAP.get(key, (C_NAVY, "#1B2558"))[1]


# ---------------------------------------------------------------------------
# PPTX HELPER FUNCTIONS
# ---------------------------------------------------------------------------
def set_slide_bg(slide, color):
    fill = slide.background.fill
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


def add_oval(slide, x, y, w, h, fill_color, text="", font_size=13, text_color=C_WHITE):
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

    lines = str(text).split("\n")
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


def add_bullets_box(slide, x, y, w, h, items, font_size=10.2, color=C_TEXT_DARK, space_after=4):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.06)
    tf.margin_right = Inches(0.06)
    tf.margin_top = Inches(0.03)
    tf.margin_bottom = Inches(0.03)

    for idx, item in enumerate(items):
        p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.line_spacing = 1.15
        p.space_after = Pt(space_after)
        if isinstance(item, (tuple, list)) and len(item) == 2:
            lead, rest = item
            r1 = p.add_run()
            r1.text = "• " + str(lead) + " "
            r1.font.name = FONT_BODY
            r1.font.size = Pt(font_size)
            r1.font.bold = True
            r1.font.color.rgb = C_NAVY
            r2 = p.add_run()
            r2.text = str(rest)
            r2.font.name = FONT_BODY
            r2.font.size = Pt(font_size)
            r2.font.bold = False
            r2.font.color.rgb = color
        else:
            p.text = "• " + str(item)
            p.font.name = FONT_BODY
            p.font.size = Pt(font_size)
            p.font.color.rgb = color
    return tb


def add_frame(slide, section_label, title_text, slide_num, total_slides):
    set_slide_bg(slide, C_WHITE)
    add_rect(slide, 0, 0, 10.0, 0.56, C_NAVY)
    add_text_box(slide, 0.5, 0.07, 8.8, 0.42, section_label.upper(),
                 font_name=FONT_TITLE, font_size=12, color=C_WHITE, bold=True, valign=MSO_ANCHOR.MIDDLE)
    add_text_box(slide, 0.5, 0.65, 9.0, 0.48, title_text,
                 font_name=FONT_TITLE, font_size=19.5, color=C_RED, bold=True, valign=MSO_ANCHOR.MIDDLE)
    add_rect(slide, 0, 5.25, 10.0, 0.375, C_NAVY)
    add_text_box(slide, 0.5, 5.27, 7.6, 0.32,
                 "Trường ĐH Ngân hàng TP.HCM (HUB)  |  Kỹ năng ứng dụng AI trong học tập và nghiên cứu  |  ThS. Phó Hải Đăng",
                 font_name=FONT_BODY, font_size=9, color=C_LIGHT_GRAY, valign=MSO_ANCHOR.MIDDLE)
    add_text_box(slide, 8.6, 5.27, 0.9, 0.32, f"{slide_num} / {total_slides}",
                 font_name=FONT_BODY, font_size=9.5, color=C_GOLD, bold=True,
                 align=PP_ALIGN.RIGHT, valign=MSO_ANCHOR.MIDDLE)


def render_deck_pptx(deck_spec, out_pptx_paths):
    prs = Presentation()
    prs.slide_width = Inches(10.0)
    prs.slide_height = Inches(5.625)
    blank = prs.slide_layouts[6]
    slides_data = deck_spec["slides"]
    total = len(slides_data)

    for idx, sp in enumerate(slides_data, start=1):
        sl = prs.slides.add_slide(blank)
        stype = sp["type"]

        if stype == "cover":
            set_slide_bg(sl, C_NAVY)
            add_rect(sl, 0, 0, 10.0, 0.07, C_GOLD)
            add_text_box(sl, 0.5, 0.50, 9.0, 0.35, "TRƯỜNG ĐẠI HỌC NGÂN HÀNG TP. HỒ CHÍ MINH (HUB)",
                         font_name=FONT_BODY, font_size=13, color=C_GOLD, bold=True, align=PP_ALIGN.CENTER)
            add_text_box(sl, 0.5, 0.85, 9.0, 0.30, sp.get("module_badge", "MODULE 1: BẢN CHẤT AI, PROMPT, CONTEXT & HARNESS"),
                         font_name=FONT_BODY, font_size=11, color=C_LIGHT_GRAY, align=PP_ALIGN.CENTER)
            add_rect(sl, 3.0, 1.25, 4.0, 0.03, C_GOLD)
            add_text_box(sl, 0.6, 1.45, 8.8, 1.35, sp["title"],
                         font_name=FONT_TITLE, font_size=24, color=C_WHITE, bold=True,
                         align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE, line_spacing=1.25)
            add_text_box(sl, 0.8, 2.88, 8.4, 0.42, sp["subtitle"],
                         font_name=FONT_BODY, font_size=13, color=C_GOLD, italic=True, align=PP_ALIGN.CENTER)
            for b_i, b_text in enumerate(sp.get("badges", [])):
                xx = 1.1 + b_i * 2.7
                add_rect(sl, xx, 3.50, 2.4, 0.78, C_DARK_NAVY, C_GOLD, 1)
                add_text_box(sl, xx + 0.05, 3.55, 2.3, 0.68, b_text,
                             font_name=FONT_BODY, font_size=10.5, color=C_WHITE, bold=True,
                             align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)
            add_rect(sl, 0, 4.65, 10.0, 0.975, C_DARK_NAVY)
            add_text_box(sl, 0.5, 4.75, 9.0, 0.75,
                         "Giảng viên: ThS. Phó Hải Đăng  |  Khoa Hệ thống thông tin quản lý  |  Email: dangph@hub.edu.vn",
                         font_name=FONT_BODY, font_size=11, color=C_WHITE, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)

        elif stype == "closing":
            set_slide_bg(sl, C_NAVY)
            add_rect(sl, 0, 0, 10.0, 0.07, C_GOLD)
            add_text_box(sl, 0.6, 0.65, 8.8, 0.95, sp["quote"],
                         font_name=FONT_TITLE, font_size=20, color=C_WHITE, bold=True,
                         align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE, line_spacing=1.25)
            add_rect(sl, 3.2, 1.70, 3.6, 0.03, C_GOLD)
            cards = sp.get("takeaways", [])
            for c_i, (th, tb) in enumerate(cards):
                xx = 0.5 + c_i * 3.05
                add_rect(sl, xx, 1.95, 2.9, 2.05, C_DARK_NAVY, C_GOLD, 1)
                add_text_box(sl, xx + 0.08, 2.03, 2.74, 0.45, th,
                             font_name=FONT_BODY, font_size=11, color=C_GOLD, bold=True, align=PP_ALIGN.CENTER)
                add_text_box(sl, xx + 0.1, 2.52, 2.7, 1.4, tb,
                             font_name=FONT_BODY, font_size=9.8, color=C_WHITE, align=PP_ALIGN.CENTER, line_spacing=1.2)
            add_text_box(sl, 0.5, 4.22, 9.0, 0.45, sp.get("cta", ""),
                         font_name=FONT_BODY, font_size=12.5, color=C_GOLD, italic=True, align=PP_ALIGN.CENTER)
            add_text_box(sl, 0.5, 4.80, 9.0, 0.45,
                         "ThS. Phó Hải Đăng  |  Trường ĐH Ngân hàng TP.HCM (HUB)  |  LMS Hub: Hoàn thành Quiz, Nhật ký 4F & Feedback",
                         font_name=FONT_BODY, font_size=10.5, color=C_LIGHT_GRAY, align=PP_ALIGN.CENTER)

        elif stype == "numbered_list":
            add_frame(sl, sp["section"], sp["title"], idx, total)
            items = sp["items"]
            step_h = 3.8 / max(len(items), 1)
            for i_idx, (num, head, desc, col_key) in enumerate(items):
                yy = 1.22 + i_idx * step_h
                box_h = step_h - 0.10
                add_rect(sl, 0.5, yy, 9.0, box_h, C_OFF_WHITE, C_LIGHT_GRAY, 0.75)
                add_oval(sl, 0.65, yy + (box_h - 0.46) / 2, 0.46, 0.46, rgb(col_key), num, 12)
                add_text_box(sl, 1.28, yy + 0.04, 8.05, 0.28, head, font_size=12, color=C_NAVY, bold=True)
                add_text_box(sl, 1.28, yy + 0.32, 8.05, box_h - 0.36, desc, font_size=10, color=C_TEXT_DARK)

        elif stype == "two_cards":
            add_frame(sl, sp["section"], sp["title"], idx, total)
            y_start = 1.22
            h_card = 3.82
            if sp.get("banner"):
                b_col, b_bg, b_txt = sp["banner"]
                add_rect(sl, 0.5, 1.20, 9.0, 0.62, rgb(b_bg), rgb(b_col), 1)
                add_text_box(sl, 0.6, 1.23, 8.8, 0.56, b_txt,
                             font_size=10.2, color=rgb(b_col), bold=True, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)
                y_start = 1.92
                h_card = 3.12
            for c_i, card in enumerate(sp["cards"]):
                xx = 0.5 + c_i * 4.65
                col = rgb(card["color"])
                bg = rgb(card.get("bg", "off_white"))
                add_rect(sl, xx, y_start, 4.35, h_card, bg, col, 1)
                add_rect(sl, xx, y_start, 4.35, 0.42, col)
                add_text_box(sl, xx + 0.08, y_start + 0.03, 4.19, 0.36, card["header"],
                             font_size=11, color=C_WHITE, bold=True, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)
                cur_y = y_start + 0.48
                if card.get("big_stat"):
                    add_text_box(sl, xx + 0.1, cur_y, 4.15, 0.45, card["big_stat"],
                                 font_name=FONT_TITLE, font_size=18, color=col, bold=True, align=PP_ALIGN.CENTER)
                    cur_y += 0.46
                add_bullets_box(sl, xx + 0.12, cur_y, 4.11, h_card - (cur_y - y_start) - 0.08,
                                card["bullets"], font_size=9.8, space_after=4)

        elif stype == "three_cards":
            add_frame(sl, sp["section"], sp["title"], idx, total)
            y_start = 1.22
            h_card = 3.82
            if sp.get("banner"):
                b_col, b_bg, b_txt = sp["banner"]
                add_rect(sl, 0.5, 1.20, 9.0, 0.62, rgb(b_bg), rgb(b_col), 1)
                add_text_box(sl, 0.6, 1.23, 8.8, 0.56, b_txt,
                             font_size=10.2, color=rgb(b_col), bold=True, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)
                y_start = 1.92
                h_card = 3.12
            for c_i, card in enumerate(sp["cards"]):
                xx = 0.5 + c_i * 3.05
                col = rgb(card["color"])
                bg = rgb(card.get("bg", "off_white"))
                add_rect(sl, xx, y_start, 2.9, h_card, bg, col, 1)
                add_rect(sl, xx, y_start, 2.9, 0.42, col)
                add_text_box(sl, xx + 0.06, y_start + 0.03, 2.78, 0.36, card["header"],
                             font_size=10.5, color=C_WHITE, bold=True, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)
                add_bullets_box(sl, xx + 0.10, y_start + 0.48, 2.70, h_card - 0.54,
                                card["bullets"], font_size=9.5, space_after=4)

        elif stype == "grid_2x2":
            add_frame(sl, sp["section"], sp["title"], idx, total)
            y_start = 1.22
            card_h = 1.82
            gap_y = 1.94
            if sp.get("banner"):
                b_col, b_bg, b_txt = sp["banner"]
                add_rect(sl, 0.5, 1.20, 9.0, 0.58, rgb(b_bg), rgb(b_col), 1)
                add_text_box(sl, 0.6, 1.22, 8.8, 0.54, b_txt,
                             font_size=10, color=rgb(b_col), bold=True, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)
                y_start = 1.88
                card_h = 1.50
                gap_y = 1.60
            for c_i, box in enumerate(sp["boxes"]):
                col_idx = c_i % 2
                row_idx = c_i // 2
                xx = 0.5 + col_idx * 4.6
                yy = y_start + row_idx * gap_y
                col = rgb(box["color"])
                bg = rgb(box.get("bg", "off_white"))
                add_rect(sl, xx, yy, 4.4, card_h, bg, C_LIGHT_GRAY, 0.75)
                add_rect(sl, xx, yy, 0.08, card_h, col)
                add_text_box(sl, xx + 0.15, yy + 0.05, 4.18, 0.30, box["header"],
                             font_size=11.2, color=col, bold=True)
                add_bullets_box(sl, xx + 0.14, yy + 0.34, 4.18, card_h - 0.38,
                                box["bullets"], font_size=9.5, space_after=3)

        elif stype == "table":
            add_frame(sl, sp["section"], sp["title"], idx, total)
            y_start = 1.22
            if sp.get("banner"):
                b_col, b_bg, b_txt = sp["banner"]
                add_rect(sl, 0.5, 1.20, 9.0, 0.55, rgb(b_bg), rgb(b_col), 1)
                add_text_box(sl, 0.6, 1.22, 8.8, 0.50, b_txt,
                             font_size=10, color=rgb(b_col), bold=True, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)
                y_start = 1.82
            headers = sp["headers"]
            col_w = sp["col_widths"]
            rows = sp["rows"]
            # Header bar
            add_rect(sl, 0.5, y_start, 9.0, 0.36, C_NAVY)
            cur_x = 0.5
            for h_txt, w_val in zip(headers, col_w):
                add_text_box(sl, cur_x + 0.04, y_start + 0.03, w_val - 0.08, 0.30, h_txt,
                             font_size=9.8, color=C_WHITE, bold=True, valign=MSO_ANCHOR.MIDDLE)
                cur_x += w_val
            avail_h = 5.08 - (y_start + 0.38)
            row_h = avail_h / max(len(rows), 1)
            for r_i, r_cells in enumerate(rows):
                yy = y_start + 0.38 + r_i * row_h
                bg = C_OFF_WHITE if r_i % 2 == 0 else C_WHITE
                add_rect(sl, 0.5, yy, 9.0, row_h - 0.03, bg, C_LIGHT_GRAY, 0.5)
                cur_x = 0.5
                for c_i, (cell_txt, w_val) in enumerate(zip(r_cells, col_w)):
                    is_first = (c_i == 0)
                    add_text_box(sl, cur_x + 0.04, yy + 0.02, w_val - 0.08, row_h - 0.06, cell_txt,
                                 font_size=9.2, color=C_NAVY if is_first else C_TEXT_DARK,
                                 bold=is_first, valign=MSO_ANCHOR.MIDDLE)
                    cur_x += w_val

    for p in out_pptx_paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        prs.save(p)
        print(f"Saved PPTX: {p}")


def render_deck_html(deck_spec, out_html_paths):
    slides_data = deck_spec["slides"]
    total = len(slides_data)
    sections_html = []

    for idx, sp in enumerate(slides_data, start=1):
        stype = sp["type"]
        active_cls = " active" if idx == 1 else ""

        if stype == "cover":
            badges_html = "".join([
                f'<div style="background: var(--dark-navy); border: 1.5px solid var(--gold); padding: 14px; border-radius: 6px;">'
                f'<div style="color: var(--white); font-weight: 700; font-size: 15px; white-space: pre-line;">{b}</div></div>'
                for b in sp.get("badges", [])
            ])
            sec = f"""
  <section class="slide navy-bg{active_cls}">
    <div class="gold-top-bar"></div>
    <div style="padding: 44px 64px; text-align: center; flex: 1; display: flex; flex-direction: column; justify-content: center;">
      <div style="color: var(--gold); font-size: 17px; font-weight: 700; letter-spacing: 3px; margin-bottom: 6px;">TRƯỜNG ĐẠI HỌC NGÂN HÀNG TP. HỒ CHÍ MINH (HUB)</div>
      <div style="color: #CBD5E1; font-size: 14.5px; letter-spacing: 2px; margin-bottom: 20px;">{sp.get("module_badge", "")}</div>
      <div style="width: 400px; height: 3px; background: var(--gold); margin: 0 auto 24px;"></div>
      <h1 style="font-family: Georgia, serif; font-size: 34px; line-height: 1.35; color: var(--white); margin-bottom: 16px; white-space: pre-line;">{sp["title"]}</h1>
      <div style="color: var(--gold); font-size: 18px; font-style: italic; margin-bottom: 32px;">{sp["subtitle"]}</div>
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 22px; max-width: 960px; margin: 0 auto;">{badges_html}</div>
    </div>
    <div style="background: var(--dark-navy); padding: 16px 60px; text-align: center; font-size: 14.5px; color: #E2E8F0; border-top: 1px solid #2D3A7B;">
      <strong>Giảng viên: ThS. Phó Hải Đăng</strong> &nbsp;|&nbsp; Khoa Hệ thống thông tin quản lý &nbsp;|&nbsp; Email: dangph@hub.edu.vn
    </div>
  </section>"""
            sections_html.append(sec)

        elif stype == "closing":
            t_html = "".join([
                f'<div style="background: var(--dark-navy); border: 1.5px solid var(--gold); border-radius: 6px; padding: 18px;">'
                f'<div style="color: var(--gold); font-weight: 700; font-size: 15.5px; margin-bottom: 8px;">{th}</div>'
                f'<div style="font-size: 14px; color: #E2E8F0; line-height: 1.5;">{tb}</div></div>'
                for th, tb in sp.get("takeaways", [])
            ])
            sec = f"""
  <section class="slide navy-bg{active_cls}">
    <div class="gold-top-bar"></div>
    <div style="padding: 44px 64px; text-align: center; flex: 1; display: flex; flex-direction: column; justify-content: center;">
      <h1 style="font-family: Georgia, serif; font-size: 28px; line-height: 1.35; color: var(--white); margin-bottom: 16px; white-space: pre-line;">{sp["quote"]}</h1>
      <div style="width: 380px; height: 3px; background: var(--gold); margin: 0 auto 24px;"></div>
      <div class="grid-3" style="max-height: 250px; margin-bottom: 24px;">{t_html}</div>
      <div style="color: var(--gold); font-size: 17px; font-style: italic; margin-bottom: 14px;">{sp.get("cta", "")}</div>
      <div style="color: #CBD5E1; font-size: 14.5px;">ThS. Phó Hải Đăng &nbsp;|&nbsp; Trường ĐH Ngân hàng TP.HCM (HUB) &nbsp;|&nbsp; LMS Hub: Hoàn thành Quiz, Nhật ký 4F &amp; Feedback</div>
    </div>
  </section>"""
            sections_html.append(sec)

        elif stype == "numbered_list":
            rows_h = []
            for num, head, desc, col_key in sp["items"]:
                rows_h.append(
                    f'<div style="display:flex;align-items:center;gap:16px;background:var(--off-white);padding:12px 18px;border-radius:6px;border:1px solid var(--border);">'
                    f'<div style="width:44px;height:44px;border-radius:50%;background:{hex_c(col_key)};color:white;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:16px;flex-shrink:0;">{num}</div>'
                    f'<div><div style="font-size:16px;font-weight:700;color:var(--navy);">{head}</div>'
                    f'<div style="font-size:13.8px;color:var(--text-dark);margin-top:2px;">{desc}</div></div></div>'
                )
            sec = f"""
  <section class="slide{active_cls}">
    <div class="header-bar"><span>{sp["section"]}</span><span>HUB_AI_CERT</span></div>
    <div class="slide-body">
      <h1 class="page-title">{sp["title"]}</h1>
      <div style="display:flex;flex-direction:column;gap:12px;flex:1;justify-content:center;">{"".join(rows_h)}</div>
    </div>
    <div class="footer-bar"><span>Trường ĐH Ngân hàng TP.HCM (HUB) | Kỹ năng ứng dụng AI trong học tập và nghiên cứu | ThS. Phó Hải Đăng</span><span class="page-num">{idx} / {total}</span></div>
  </section>"""
            sections_html.append(sec)

        elif stype in ("two_cards", "three_cards"):
            grid_cls = "grid-2" if stype == "two_cards" else "grid-3"
            banner_html = ""
            if sp.get("banner"):
                b_col, b_bg, b_txt = sp["banner"]
                banner_html = f'<div class="banner" style="background:{hex_c(b_bg)};border:1.5px solid {hex_c(b_col)};color:{hex_c(b_col)};white-space:pre-line;">{b_txt}</div>'
            cards_h = []
            for card in sp["cards"]:
                col_hex = hex_c(card["color"])
                bg_hex = hex_c(card.get("bg", "off_white"))
                stat_h = f'<div style="font-family:Georgia,serif;font-size:23px;font-weight:700;color:{col_hex};text-align:center;margin:4px 0 10px;">{card["big_stat"]}</div>' if card.get("big_stat") else ""
                li_h = []
                for b in card["bullets"]:
                    if isinstance(b, (tuple, list)) and len(b) == 2:
                        li_h.append(f'<li><strong style="color:var(--navy);">{b[0]}</strong> {b[1]}</li>')
                    else:
                        li_h.append(f'<li>{b}</li>')
                cards_h.append(
                    f'<div class="card" style="background:{bg_hex};border-color:{col_hex};">'
                    f'<div class="card-header" style="background:{col_hex};">{card["header"]}</div>'
                    f'<div class="card-content">{stat_h}<ul>{"".join(li_h)}</ul></div></div>'
                )
            sec = f"""
  <section class="slide{active_cls}">
    <div class="header-bar"><span>{sp["section"]}</span><span>HUB_AI_CERT</span></div>
    <div class="slide-body">
      <h1 class="page-title">{sp["title"]}</h1>
      {banner_html}
      <div class="{grid_cls}">{"".join(cards_h)}</div>
    </div>
    <div class="footer-bar"><span>Trường ĐH Ngân hàng TP.HCM (HUB) | Kỹ năng ứng dụng AI trong học tập và nghiên cứu | ThS. Phó Hải Đăng</span><span class="page-num">{idx} / {total}</span></div>
  </section>"""
            sections_html.append(sec)

        elif stype == "grid_2x2":
            banner_html = ""
            if sp.get("banner"):
                b_col, b_bg, b_txt = sp["banner"]
                banner_html = f'<div class="banner" style="background:{hex_c(b_bg)};border:1.5px solid {hex_c(b_col)};color:{hex_c(b_col)};white-space:pre-line;">{b_txt}</div>'
            boxes_h = []
            for box in sp["boxes"]:
                col_hex = hex_c(box["color"])
                bg_hex = hex_c(box.get("bg", "off_white"))
                li_h = []
                for b in box["bullets"]:
                    if isinstance(b, (tuple, list)) and len(b) == 2:
                        li_h.append(f'<li><strong style="color:var(--navy);">{b[0]}</strong> {b[1]}</li>')
                    else:
                        li_h.append(f'<li>{b}</li>')
                boxes_h.append(
                    f'<div class="left-card" style="background:{bg_hex};border-left-color:{col_hex};">'
                    f'<h3 style="color:{col_hex};">{box["header"]}</h3>'
                    f'<ul>{"".join(li_h)}</ul></div>'
                )
            sec = f"""
  <section class="slide{active_cls}">
    <div class="header-bar"><span>{sp["section"]}</span><span>HUB_AI_CERT</span></div>
    <div class="slide-body">
      <h1 class="page-title">{sp["title"]}</h1>
      {banner_html}
      <div class="grid-2" style="gap:16px;">{"".join(boxes_h)}</div>
    </div>
    <div class="footer-bar"><span>Trường ĐH Ngân hàng TP.HCM (HUB) | Kỹ năng ứng dụng AI trong học tập và nghiên cứu | ThS. Phó Hải Đăng</span><span class="page-num">{idx} / {total}</span></div>
  </section>"""
            sections_html.append(sec)

        elif stype == "table":
            banner_html = ""
            if sp.get("banner"):
                b_col, b_bg, b_txt = sp["banner"]
                banner_html = f'<div class="banner" style="background:{hex_c(b_bg)};border:1.5px solid {hex_c(b_col)};color:{hex_c(b_col)};white-space:pre-line;">{b_txt}</div>'
            ths = "".join([f'<th>{h}</th>' for h in sp["headers"]])
            trs = []
            for r in sp["rows"]:
                tds = "".join([f'<td>{"<strong>"+c+"</strong>" if ci==0 else c}</td>' for ci, c in enumerate(r)])
                trs.append(f'<tr>{tds}</tr>')
            sec = f"""
  <section class="slide{active_cls}">
    <div class="header-bar"><span>{sp["section"]}</span><span>HUB_AI_CERT</span></div>
    <div class="slide-body">
      <h1 class="page-title">{sp["title"]}</h1>
      {banner_html}
      <table class="acad-table"><thead><tr>{ths}</tr></thead><tbody>{"".join(trs)}</tbody></table>
    </div>
    <div class="footer-bar"><span>Trường ĐH Ngân hàng TP.HCM (HUB) | Kỹ năng ứng dụng AI trong học tập và nghiên cứu | ThS. Phó Hải Đăng</span><span class="page-num">{idx} / {total}</span></div>
  </section>"""
            sections_html.append(sec)

    full_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{deck_spec["doc_title"]}</title>
  <style>
    :root {{
      --navy: #1B2558; --dark-navy: #111A40; --white: #FFFFFF; --off-white: #F5F6FA;
      --red: #C62828; --light-red: #FFEBEE; --accent: #1565C0; --light-accent: #E3F2FD;
      --gold: #F9A825; --green: #2E7D32; --light-green: #E8F5E9; --orange: #E65100;
      --light-orange: #FFF3E0; --text-dark: #212121; --text-mid: #424242;
      --text-light: #757575; --border: #E0E0E0;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: #0d122a; font-family: 'Calibri', 'Segoe UI', sans-serif; color: var(--text-dark);
      height: 100vh; overflow: hidden; display: flex; flex-direction: column; align-items: center; justify-content: center;
    }}
    .deck-viewport {{
      width: 1280px; height: 720px; position: relative; background: var(--white);
      box-shadow: 0 20px 60px rgba(0,0,0,0.6); border-radius: 6px; overflow: hidden; transform-origin: center center;
    }}
    .slide {{ width: 1280px; height: 720px; position: absolute; top: 0; left: 0; display: none; flex-direction: column; background: var(--white); }}
    .slide.active {{ display: flex; }}
    .slide.navy-bg {{ background: var(--navy); color: var(--white); }}
    .gold-top-bar {{ width: 100%; height: 9px; background: var(--gold); flex-shrink: 0; }}
    .header-bar {{
      width: 100%; height: 64px; background: var(--navy); color: var(--white);
      display: flex; align-items: center; justify-content: space-between; padding: 0 52px;
      font-family: Georgia, serif; font-size: 15.5px; font-weight: 700; letter-spacing: 1.8px; text-transform: uppercase; flex-shrink: 0;
    }}
    .footer-bar {{
      width: 100%; height: 42px; background: var(--navy); color: #D0D5E8;
      display: flex; align-items: center; justify-content: space-between; padding: 0 52px; font-size: 13px; margin-top: auto; flex-shrink: 0;
    }}
    .footer-bar .page-num {{ color: var(--gold); font-weight: 700; font-size: 14px; }}
    .slide-body {{ padding: 20px 52px 16px; flex: 1; display: flex; flex-direction: column; overflow: hidden; }}
    h1.page-title {{ font-family: Georgia, serif; font-size: 25px; color: var(--red); font-weight: 700; margin-bottom: 12px; line-height: 1.25; }}
    .grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 22px; flex: 1; }}
    .grid-3 {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 18px; flex: 1; }}
    .card {{ background: var(--off-white); border: 1.5px solid var(--border); border-radius: 6px; overflow: hidden; display: flex; flex-direction: column; box-shadow: 0 3px 8px rgba(0,0,0,0.05); }}
    .card-header {{ padding: 10px 14px; color: var(--white); font-weight: 700; font-size: 14.5px; text-align: center; text-transform: uppercase; }}
    .card-content {{ padding: 14px 16px; font-size: 14px; line-height: 1.48; flex: 1; }}
    .card-content ul {{ padding-left: 18px; }}
    .card-content li {{ margin-bottom: 7px; }}
    .left-card {{ background: var(--off-white); border: 1px solid var(--border); border-left: 8px solid var(--navy); border-radius: 4px; padding: 12px 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.04); }}
    .left-card h3 {{ font-size: 15px; margin-bottom: 6px; text-transform: uppercase; }}
    .left-card ul {{ padding-left: 18px; font-size: 13.6px; line-height: 1.45; }}
    .left-card li {{ margin-bottom: 5px; }}
    .banner {{ padding: 10px 18px; border-radius: 6px; margin-bottom: 12px; font-size: 14px; line-height: 1.42; text-align: center; font-weight: 600; }}
    table.acad-table {{ width: 100%; border-collapse: collapse; font-size: 13.2px; }}
    table.acad-table th {{ background: var(--navy); color: var(--white); padding: 9px 12px; text-align: left; font-weight: 700; }}
    table.acad-table td {{ padding: 8px 12px; border: 1px solid var(--border); vertical-align: middle; line-height: 1.38; }}
    table.acad-table tr:nth-child(even) {{ background: var(--off-white); }}
    .controls-bar {{ margin-top: 10px; display: flex; align-items: center; gap: 14px; color: #cbd5e1; font-size: 13px; }}
    .controls-bar button {{ background: #1e293b; color: #f8fafc; border: 1px solid #475569; padding: 6px 14px; border-radius: 4px; cursor: pointer; font-weight: 600; }}
    .controls-bar button:hover {{ background: #334155; }}
  </style>
</head>
<body>
<div class="deck-viewport" id="viewport">
{"".join(sections_html)}
</div>
<div class="controls-bar">
  <button onclick="prevSlide()">&larr; Trang trước</button>
  <span id="slide-indicator">Slide 1 / {total}</span>
  <button onclick="nextSlide()">Trang tiếp &rarr;</button>
  <button onclick="toggleFullScreen()">Toàn màn hình (F)</button>
</div>
<script>
  const slides = document.querySelectorAll('.slide');
  const indicator = document.getElementById('slide-indicator');
  const viewport = document.getElementById('viewport');
  let current = 0;
  function showSlide(idx) {{
    if (idx < 0) idx = 0;
    if (idx >= slides.length) idx = slides.length - 1;
    slides.forEach((s, i) => s.classList.toggle('active', i === idx));
    current = idx;
    indicator.textContent = `Slide ${{current + 1}} / ${{slides.length}}`;
  }}
  function nextSlide() {{ showSlide(current + 1); }}
  function prevSlide() {{ showSlide(current - 1); }}
  function toggleFullScreen() {{
    if (!document.fullscreenElement) document.documentElement.requestFullscreen();
    else document.exitFullscreen();
  }}
  function fitViewport() {{
    const scale = Math.min((window.innerWidth - 36) / 1280, (window.innerHeight - 66) / 720);
    viewport.style.transform = `scale(${{Math.min(scale, 1.15)}})`;
  }}
  window.addEventListener('resize', fitViewport);
  window.addEventListener('keydown', (e) => {{
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{ e.preventDefault(); nextSlide(); }}
    if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{ e.preventDefault(); prevSlide(); }}
    if (e.key === 'f' || e.key === 'F') toggleFullScreen();
  }});
  fitViewport();
</script>
</body>
</html>"""

    for p in out_html_paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"Saved HTML: {p}")


print("Core slide engine module1_engine.py initialized.")
