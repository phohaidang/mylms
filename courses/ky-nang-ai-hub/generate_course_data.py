# -*- coding: utf-8 -*-
import os
import json
import shutil

COURSE_DIR = r"d:\PARA\Projects\second-brain\05-Projects\lms-hub\courses\ky-nang-ai-hub"
CONTENT_DIR = os.path.join(COURSE_DIR, "content")

for sub in ["ebook", "questions", "lessons", "slides", "exams", "images"]:
    os.makedirs(os.path.join(CONTENT_DIR, sub), exist_ok=True)

# Copy teacher image if exists
src_img = r"d:\PARA\Projects\second-brain\05-Projects\lms-hub\courses\ky-nang-ung-dung-ai\content\images\teacher.png"
if os.path.exists(src_img):
    shutil.copy2(src_img, os.path.join(CONTENT_DIR, "images", "teacher.png"))

# Copy syllabus
src_syl = r"d:\PARA\Projects\second-brain\03-Domains\Teaching\ComputerScience\Ky Nang Ung Dung AI\de_cuong_11_buoi_hub.md"
if os.path.exists(src_syl):
    shutil.copy2(src_syl, os.path.join(COURSE_DIR, "syllabus.md"))

# 1. course-config.json
course_config = {
    "meta": {
        "code": "HUB_AI_CERT",
        "name": "Kỹ năng ứng dụng AI trong học tập và nghiên cứu",
        "total_sessions": 11,
        "chapters": 11,
        "university": "Trường Đại học Ngân hàng TP.HCM (HUB)",
        "textbook": "Co-Intelligence (Ethan Mollick), Building a Second Brain (Tiago Forte) & Học liệu ThS. Phó Hải Đăng"
    },
    "sessions": [
        {
            "id": 1,
            "chapter": "Ch.1",
            "title": "Bản chất AI & Tư duy người làm chủ: 'AI là Trợ lý, Bạn là Chủ'",
            "topics": "Cơ chế xác suất LLM, Hallucination (Topaz 1/277), Lệ thuộc nhận thức & Ảo tưởng trôi chảy, Bảng phân vai Người - AI, Bản đồ công cụ AI 2026",
            "clo": "CLO1, CLO3",
            "textbook": "Ch.1 eBook SCQA & Co-Intelligence",
            "duration": "4 tiết (200 phút)"
        },
        {
            "id": 2,
            "chapter": "Ch.2",
            "title": "Từ Prompt Engineering đến Context Engineering: Giao diện của Tư duy",
            "topics": "Khung CRISP 5 thành tố, 5 kỹ thuật nâng cao (CoT, Role, Few-shot, Iterative, Negative + Chốt chặn không suy đoán), Thiết kế Context chuẩn",
            "clo": "CLO2",
            "textbook": "Ch.2 eBook SCQA & Anthropic/OpenAI Guides",
            "duration": "4 tiết (200 phút)"
        },
        {
            "id": 3,
            "chapter": "Ch.3",
            "title": "Kiến trúc Harness: Xây dựng 'Bộ dây cương' điều phối AI trong học tập",
            "topics": "Phân biệt Prompt - Context - Harness (System Rules, Workflows, Gates/Fallbacks), Thiết kế Socratic Tutor với 4 kỹ thuật học sâu, Đóng gói Mảnh ghép 1",
            "clo": "CLO1, CLO2",
            "textbook": "Ch.3 eBook SCQA & Agentic Harness Design",
            "duration": "4 tiết (200 phút)"
        },
        {
            "id": 4,
            "chapter": "Ch.4",
            "title": "Kiến trúc Second Brain (PARA & CODE) và Nghệ thuật Ghi chú nguyên tử",
            "topics": "Triết lý ngoại hóa tri thức, Mô hình PARA, Luồng vận hành CODE, Kỹ thuật viết Atomic Note (không copy-paste AI) & Khung phản tư 4F",
            "clo": "CLO3",
            "textbook": "Ch.4 eBook SCQA & Building a Second Brain",
            "duration": "4 tiết (200 phút)"
        },
        {
            "id": 5,
            "chapter": "Ch.5",
            "title": "Tích hợp Second Brain với Công nghệ RAG (Gemini Notebook / Claude Projects)",
            "topics": "Bản chất RAG (Thư ký trung thành) vs LLM thuần (Chuyên gia hay bịa), Truy vấn chéo đa tài liệu có trích dẫn, Vòng lặp Second Brain - RAG, Đóng gói Mảnh ghép 2",
            "clo": "CLO2, CLO3",
            "textbook": "Ch.5 eBook SCQA & RAG Workflows",
            "duration": "4 tiết (200 phút)"
        },
        {
            "id": 6,
            "chapter": "Ch.6",
            "title": "Quy trình NCKH với AI (Bước 1 & 2): Tìm nguồn thật, Đọc tóm tắt & 'Soi 3 phút'",
            "topics": "Quy tắc 'Nguồn thật trước, AI sau', Phễu câu hỏi nghiên cứu, Semantic Scholar/Elicit/Consensus, Prompt tóm tắt 7 mục, Kỹ thuật Soi bản tóm tắt 3 phút (Demo Hemani 2026)",
            "clo": "CLO4",
            "textbook": "Ch.6 eBook SCQA & Tọa đàm NCKH",
            "duration": "4 tiết (200 phút)"
        },
        {
            "id": 7,
            "chapter": "Ch.7",
            "title": "Trích dẫn bịa, Checklist Kiểm chứng 5 bước, Công cụ Tomaca & Zotero 8",
            "topics": "Quy tắc 'Chưa kiểm chứng, chưa vào bài', Quy luật Linardon (19.9% bịa, đề tài ít nghiên cứu 29%), Hình hài trích dẫn bịa, Checklist 5 bước, Tomaca (Máy soát người quyết) & Zotero 8",
            "clo": "CLO4",
            "textbook": "Ch.7 eBook SCQA & Linardon (2025)",
            "duration": "4 tiết (200 phút)"
        },
        {
            "id": 8,
            "chapter": "Ch.8",
            "title": "Quy trình NCKH với AI (Bước 3 & 4): Tổng hợp đa nguồn, Viết học thuật & Trình bày",
            "topics": "Phân biệt Summary vs Synthesis, Lập Synthesis Matrix tìm Research Gap, Quy trình viết 4 nhịp từ Second Brain + Zotero, Làm slide 4 lớp (AI làm draft, người làm final), Đóng gói Mảnh ghép 3",
            "clo": "CLO3, CLO4",
            "textbook": "Ch.8 eBook SCQA & Academic Writing",
            "duration": "4 tiết (200 phút)"
        },
        {
            "id": 9,
            "chapter": "Ch.9",
            "title": "Đạo đức học thuật, Pháp lý (Thông tư 49/2026) & An toàn dữ liệu Ngân hàng",
            "topics": "Quy tắc 'Dùng AI thì khai báo', Thông tư 49/2026/TT-BGDĐT (Điều 10), Luật AI 134/2025, COPE/ICMJE, Vụ GS Hancock, Đèn giao thông (Xanh-Vàng-Đỏ), Bảo mật dữ liệu & Mẫu khai báo AI, Đóng gói Mảnh ghép 4",
            "clo": "CLO5",
            "textbook": "Ch.9 eBook SCQA & Thông tư 49/2026/TT-BGDĐT",
            "duration": "4 tiết (200 phút)"
        },
        {
            "id": 10,
            "chapter": "Ch.10",
            "title": "Project Clinic & Studio Kiểm toán chéo (Peer Audit Studio)",
            "topics": "Hoàn thiện Hồ sơ Đề án 4 mảnh ghép, Phương pháp Kiểm toán chéo (Red-teaming / Peer Audit), Stress-test bộ Harness nhóm bạn, Rà soát danh mục Zotero bằng Tomaca & Checklist 5 bước",
            "clo": "CLO1, CLO2, CLO3, CLO4, CLO5",
            "textbook": "Ch.10 eBook SCQA & Peer Audit Rubric",
            "duration": "4 tiết (200 phút)"
        },
        {
            "id": 11,
            "chapter": "Ch.11",
            "title": "Bảo vệ Đề án cuối khóa (Capstone Showcase), Phản biện & Tổng kết hành trình",
            "topics": "Thuyết trình & Live Demo bộ Harness, Tranh biện cùng Hội đồng Kiểm toán chéo, Vấn đáp cá nhân trên Second Brain, Phản tư tổng kết 4F & Cam kết người làm chủ AI",
            "clo": "CLO1, CLO2, CLO3, CLO4, CLO5",
            "textbook": "Ch.11 eBook SCQA & Capstone Defense Guide",
            "duration": "4 tiết (200 phút)"
        }
    ]
}

with open(os.path.join(COURSE_DIR, "course-config.json"), "w", encoding="utf-8") as f:
    json.dump(course_config, f, ensure_ascii=False, indent=2)

print("course-config.json written successfully.")
