#!/usr/bin/env python3
"""
HTML to Markdown Roster Converter for LMS Hub
Chuyển đổi file danh sách sinh viên xuất từ cổng đào tạo HUB (dạng bảng HTML/Excel .xls)
thành file Markdown (.md) chuẩn gồm các cột: MSSV, Họ Tên, Email, Số Điện Thoại, Lớp.

Cách dùng:
    python core/scripts/html-to-roster.py <input_html_path> <output_md_path>
Ví dụ:
    python core/scripts/html-to-roster.py d:/export_L01.html courses/ltweb/roster-L01.md
"""

import sys
import os
import html
import re

def convert_html_to_roster(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Error: Không tìm thấy file đầu vào tại: {input_path}")
        sys.exit(1)

    with open(input_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Trích xuất metadata lớp học nếu có
    course_match = re.search(r"Học phần:\s*([^<]+)", content)
    class_match = re.search(r"Lớp học phần:\s*([^<]+)", content)
    term_match = re.search(r"Học kỳ:\s*([^<]+)", content)
    year_match = re.search(r"Năm học:\s*([^<]+)", content)
    time_match = re.search(r"Thời gian học[^\n<]*", content)

    course_name = course_match.group(1).strip() if course_match else "Chưa xác định"
    class_code = class_match.group(1).strip() if class_match else "Chưa xác định"
    term_name = term_match.group(1).strip() if term_match else ""
    year_name = year_match.group(1).strip() if year_match else ""
    time_info = time_match.group(0).strip() if time_match else ""

    # Trích xuất dữ liệu từng dòng sinh viên
    pattern = r"<tr>\s*<td[^>]*>(\d+)</td>\s*<td[^>]*>(\d+)</td>\s*<td[^>]*>([^<]*)</td>\s*<td>([^<]*)</td>\s*<td>([^<]*)</td>"
    matches = re.findall(pattern, content)

    if not matches:
        # Thử regex linh hoạt hơn nếu cấu trúc bảng hơi khác
        pattern_alt = r"<td[^>]*>(\d+)</td>\s*<td[^>]*class=[\"']studyprogram_normal_dl[\"']>(\d+)</td>\s*<td[^>]*>([^<]*)</td>\s*<td[^>]*>([^<]*)</td>\s*<td[^>]*>([^<]*)</td>"
        matches = re.findall(pattern_alt, content)

    if not matches:
        print("Error: Không nhận diện được dữ liệu sinh viên trong bảng HTML.")
        sys.exit(1)

    students = []
    for stt, mssv, lop, ho, ten in matches:
        ho_clean = html.unescape(ho).strip()
        ten_clean = html.unescape(ten).strip()
        full_name = re.sub(r"\s+", " ", f"{ho_clean} {ten_clean}").strip()
        email = f"{mssv}@st.hub.edu.vn"
        phone = ""  # Cổng trường không xuất số điện thoại
        students.append({
            "stt": stt,
            "mssv": mssv,
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "lop": lop.strip()
        })

    # Tạo nội dung Markdown
    md_lines = [
        f"# Danh Sách Sinh Viên - Lớp {class_code}",
        "",
        f"- **Học phần:** {course_name}",
        f"- **Lớp học phần:** {class_code}",
        f"- **Học kỳ:** {term_name} - {year_name}",
        f"- **Thông tin lịch học:** {time_info}",
        f"- **Sĩ số:** {len(students)} sinh viên",
        "- **Ghi chú:** Cột số điện thoại để trống để sinh viên tự cập nhật khi đăng nhập.",
        "",
        "| STT | MSSV | Họ Tên | Email | Số Điện Thoại | Lớp |",
        "|:---:|:---:|:---|:---|:---:|:---:|"
    ]

    for s in students:
        md_lines.append(f"| {s['stt']} | {s['mssv']} | {s['full_name']} | {s['email']} | {s['phone']} | {s['lop']} |")

    md_output = "\n".join(md_lines) + "\n"

    # Ghi file
    out_dir = os.path.dirname(output_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_output)

    print(f"✅ Đã trích xuất thành công {len(students)} sinh viên vào: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Sử dụng: python html-to-roster.py <input.html> <output.md>")
        sys.exit(1)
    convert_html_to_roster(sys.argv[1], sys.argv[2])
