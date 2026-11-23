# -*- coding: utf-8 -*-
import os
from module1_engine import render_deck_pptx, render_deck_html

# ===========================================================================
# BUỔI 3 (20 SLIDES): KIẾN TRÚC HARNESS - XÂY DỰNG "BỘ DÂY CƯƠNG" ĐIỀU PHỐI AI (CHỐT MẢNH GHÉP 1)
# ===========================================================================
buoi_03_spec = {
    "doc_title": "Buổi 3: Kiến trúc Harness & Gia sư Socrates — ĐH Ngân hàng TP.HCM (HUB)",
    "slides": [
        {
            "type": "cover",
            "module_badge": "MODULE 1 (BUỔI 3 / 11) — BẢN CHẤT AI, PROMPT, CONTEXT & HARNESS",
            "title": "BUỔI 3: KIẾN TRÚC AI HARNESS\nXÂY DỰNG \"BỘ DÂY CƯƠNG\" ĐIỀU PHỐI AI",
            "subtitle": "Câu hỏi cốt lõi: Làm sao để đóng gói toàn bộ quy tắc, quy trình nhiều bước và chốt chặn kiểm soát thành một hệ thống chạy ổn định mọi lần?",
            "badges": [
                "THỜI LƯỢNG: 4 TIẾT (200 PHÚT)\nCổng dừng GATE & Cơ chế FALLBACK",
                "CHUẨN ĐẦU RA: CLO1 & CLO2\nSocratic Harness & 4 Kỹ thuật học sâu",
                "CHỐT MẢNH GHÉP 1 ĐỀ ÁN (15%)\nĐóng gói & Stress-test 3 kịch bản Harness"
            ]
        },
        {
            "type": "numbered_list",
            "section": "Buổi 3 — Mục tiêu & Lộ trình 200 phút",
            "title": "MỤC TIÊU HỌC TẬP & LỘ TRÌNH 4 TIẾT CỦA BUỔI 3 (KẾT THÚC MODULE 1)",
            "items": [
                ("01", "Tiết 1 (50'): Kiến trúc 3 tầng Prompt - Context - Harness & Cơ chế GATE / FALLBACK",
                 "Story Spine nhân vật Minh (Kỳ 3); Ẩn dụ Con ngựa chiến & Bộ dây cương; 7 nguyên tắc thiết kế quy trình AI; Live Demo 4 kịch bản có cổng GATE (🔒) & FALLBACK (❓).", "red"),
                ("02", "Tiết 2 (50'): Thiết kế Harness cho Sự học — Biến AI thành Gia sư Socrates (Socratic Tutor)",
                 "Tích hợp 4 kỹ thuật học tập hiệu quả dựa trên khoa học thần kinh (Active Recall, Spaced Repetition, Interleaving, Productive Struggle) vào System Instructions.", "navy"),
                ("03", "Tiết 3 (50'): Thực hành Vẽ Sơ đồ Quy trình & Đóng gói Bộ Harness 4 Khối",
                 "Nguyên tắc 'Vẽ cho người trước khi vẽ cho AI'; Thiết kế sơ đồ 3-5 bước có GATE/FALLBACK; Cài đặt lên Claude Projects / Gemini Gems theo Template 4 khối.", "accent"),
                ("04", "Tiết 4 (50'): Stress-test 3 Kịch bản (Chốt Mảnh ghép 1 của Đề án) & Khóa chốt LMS",
                 "Chạy kiểm thử chéo 3 kịch bản (Chạy xuôi - Thiếu thông tin test FALLBACK - Giục vượt rào test GATE); Nghiệm thu Mảnh ghép 1; Viết Nhật ký 4F số 3 & làm Quiz Buổi 3.", "green")
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 1 — Story Spine & Khung SCQA",
            "title": "CÂU CHUYỆN CỦA MINH (KỲ 3): KHI CON NGỰA CHIẾN AI CHẠY VƯỢT QUYỀN KIỂM SOÁT",
            "banner": ("red", "light_red", "Viết được một câu lệnh CRISP tốt mới chỉ giúp bạn thắng được 1 lượt chat. Muốn làm chủ cả một dự án, bạn cần một Bộ Harness!"),
            "cards": [
                {
                    "header": "S & C — SỰ CỐ 'SAI SỐ DÂY CHUYỀN' CỦA NHÓM MINH",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Tình huống (Situation):", "Nhóm của Minh đã biết viết Prompt CRISP và đính kèm file báo cáo tài chính PDF. Minh giao cho AI một nhiệm vụ lớn gồm 4 bước: (1) Trích xuất số liệu -> (2) Tính chỉ số ROE, NIM -> (3) So sánh trung bình ngành -> (4) Viết báo cáo nhận xét."),
                        ("Biến cố (Complication):", "AI chạy tuốt một mạch từ Bước 1 đến Bước 4 chỉ trong 20 giây! Nhưng ở Bước 1, AI đọc nhầm đơn vị 'tỷ đồng' thành 'triệu đồng' ở một dòng nhỏ. Vì AI không dừng lại ở Bước 1 để hỏi Minh xác nhận bảng số liệu, toàn bộ Bước 2, 3 và 4 phía sau đều sai bét theo hiệu ứng domino!"),
                        ("Nỗi mệt mỏi lặp lại:", "Mỗi lần mở đoạn chat mới cho ngân hàng tiếp theo, Minh lại phải copy-paste lại từ đầu hàng trang quy tắc.")
                    ]
                },
                {
                    "header": "Q & A — TỪ CHAT TỰ DO ĐẾN KIẾN TRÚC HARNESS",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Câu hỏi trọng tâm (Question):", "Làm thế nào để đóng gói toàn bộ quy tắc, tài liệu nền và luồng công việc nhiều bước thành một hệ thống cố định, buộc AI phải DỪNG LẠI chờ con người kiểm duyệt ở từng trạm quan trọng?"),
                        ("Giải pháp cốt lõi (Answer):", "Xây dựng một AI HARNESS ('Bộ dây cương điều phối'):\n• Cài đặt cố định System Instructions (Hiến pháp của AI) và Knowledge Base.\n• Chia quy trình thành các bước tuần tự có Cổng xác nhận (GATE 🔒) và Cơ chế xử lý thiếu thông tin (FALLBACK ❓).")
                    ]
                }
            ]
        },
        {
            "type": "three_cards",
            "section": "Tiết 1 — Kiến trúc 3 Tầng Điều phối AI",
            "title": "ẨN DỤ CON NGỰA CHIẾN: PROMPT  -->  CONTEXT  -->  HARNESS",
            "banner": ("navy", "light_accent", "Hãy hình dung Mô hình ngôn ngữ lớn (LLM) là một con ngựa chiến cực khỏe nhưng chạy theo bản năng xác suất:"),
            "cards": [
                {
                    "header": "TẦNG 1: PROMPT (TIẾNG HÔ)",
                    "color": "accent",
                    "bg": "light_accent",
                    "bullets": [
                        ("Bản chất:", "Là mệnh lệnh kích hoạt tức thời cho từng lượt tương tác (đã học ở Buổi 2 với khung CRISP)."),
                        ("Phạm vi tác dụng:", "Chỉ có hiệu lực trong đúng 1 lượt hỏi - đáp đó. Nếu hội thoại dài ra, hiệu lực của câu lệnh đầu sẽ mờ dần."),
                        ("Giới hạn:", "Không thể tự kiểm soát các quy trình phức tạp gồm nhiều bước phụ thuộc lẫn nhau.")
                    ]
                },
                {
                    "header": "TẦNG 2: CONTEXT (ĐỊA HÌNH & BẢN ĐỒ)",
                    "color": "green",
                    "bg": "light_green",
                    "bullets": [
                        ("Bản chất:", "Là toàn bộ gói tài liệu nguồn đã làm sạch, dữ liệu tình huống, rubric và ví dụ mẫu (Few-shot) cung cấp cho phiên làm việc."),
                        ("Phạm vi tác dụng:", "Cung cấp căn cứ thực tế (Grounding) để ngựa chạy trên đất thật chứ không chạy trên mây (chống Hallucination)."),
                        ("Giới hạn:", "Có tài liệu tốt nhưng chưa có quy trình từng bước thì AI vẫn có thể làm gộp bước hoặc tự ý quyết định thay bạn.")
                    ]
                },
                {
                    "header": "TẦNG 3: HARNESS (BỘ DÂY CƯƠNG & ĐƯỜNG RAY)",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Bản chất:", "Là bộ khung điều phối và kiềm tỏa toàn diện gồm: System Instructions cố định + Kho tri thức nền + Quy trình tuần tự nhiều bước (Workflow) + Cổng dừng (GATE) + Dự phòng (FALLBACK) + Tự kiểm tra (Self-check)."),
                        ("Nơi đóng gói:", "Claude Projects, Gemini Gems, Custom GPTs hoặc hệ thống Agentic Skills/Rules."),
                        ("Sức mạnh:", "Đảm bảo AI chạy 100 lần đều giữ đúng kỷ luật như một!")
                    ]
                }
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 1 — Hai Chốt chặn Kỹ thuật Cốt lõi của Harness",
            "title": "GIẢI PHẪU HAI CHỐT CHẶN SỐNG CÒN: GATE (🔒) VÀ FALLBACK (❓)",
            "cards": [
                {
                    "header": "CHỐT CHẶN 1: GATE (🔒 CỔNG DỪNG XÁC NHẬN)",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Định nghĩa:", "Là điểm chốt bắt buộc AI phải DỪNG LẠI hoàn toàn sau khi thực hiện xong một bước trung gian quan trọng, xuất kết quả bước đó ra màn hình và chờ con người kiểm tra, phê duyệt mới được đi tiếp."),
                        ("Câu lệnh cài đặt GATE trong Harness:", "\"Sau khi hoàn thành Bước 2 (Bảng trích xuất số liệu), bạn BẮT BUỘC DỪNG LẠI và hỏi tôi: 'Bạn đã đối chiếu và xác nhận các số liệu trên khớp với bản gốc để chuyển sang Bước 3 chưa?'. Tuyệt đối không tự ý chạy Bước 3 khi tôi chưa gõ xác nhận.\""),
                        ("Nguyên tắc thiết kế:", "Đặt GATE ngay sau các bước trích xuất số liệu, chấm điểm hoặc lập dàn ý — nơi mà nếu sai sẽ làm hỏng toàn bộ các bước sau.")
                    ]
                },
                {
                    "header": "CHỐT CHẶN 2: FALLBACK (❓ XỬ LÝ KHI THIẾU CĂN CỨ)",
                    "color": "orange",
                    "bg": "light_orange",
                    "bullets": [
                        ("Định nghĩa:", "Là quy tắc dự phòng chỉ định rõ AI phải làm gì khi người dùng cung cấp thiếu dữ liệu đầu vào hoặc khi tìm trong tài liệu không thấy căn cứ."),
                        ("Tại sao phải có FALLBACK?", "Nếu không có FALLBACK, bản năng xác suất của LLM sẽ tự động 'đoán mò' hoặc tự bịa ra một con số hợp lý để điền cho đầy bảng!"),
                        ("Câu lệnh cài đặt FALLBACK trong Harness:", "• FALLBACK 1 (Thiếu đầu vào từ người dùng): \"Nếu người dùng chưa cung cấp [Biến số X / Tiêu chí Y], hãy dừng lại và hỏi rõ, không tự giả định.\"\n• FALLBACK 2 (Thiếu căn cứ trong tài liệu): \"Nếu chỉ tiêu nào không có căn cứ trong file đính kèm, bắt buộc ghi rõ '[Chưa đủ căn cứ trong tài liệu]' và báo cho người dùng.\"")
                    ]
                }
            ]
        },
        {
            "type": "table",
            "section": "Tiết 1 — Bảy Nguyên tắc Thiết kế Quy trình AI (Workflow Harness)",
            "title": "7 NGUYÊN TẮC VÀNG KHI VIẾT 'HIẾN PHÁP' (SYSTEM INSTRUCTIONS) CHO HARNESS",
            "headers": ["#", "Nguyên tắc Thiết kế", "Vì sao bắt buộc phải có?", "Câu lệnh mẫu tiếng Việt đưa vào System Instructions"],
            "col_widths": [0.5, 2.2, 2.5, 3.8],
            "rows": [
                ["1", "Khởi tạo bắt buộc\n(Context Loading)", "Đảm bảo AI đọc kỹ tài liệu chuẩn trước khi bắt đầu phán đoán.", "\"Trước khi bắt đầu Bước 1, hãy đọc toàn bộ tài liệu chuẩn trong Knowledge Base và tóm tắt lại 3 quy tắc chính để tôi xác nhận.\""],
                ["2", "Quy trình tuần tự có cổng\n(Sequential Gates 🔒)", "Chặn đứng hiệu ứng sai số domino khi AI tự chạy gộp từ đầu đến cuối.", "\"Thực hiện tuần tự từng bước. Sau Bước [X], DỪNG LẠI chờ tôi xác nhận rồi mới được chuyển sang Bước [X+1].\""],
                ["3", "Xử lý thiếu thông tin\n(Explicit Fallbacks ❓)", "Triệt tiêu hành vi tự suy diễn khi dữ liệu đầu vào bị khuyết.", "\"Nếu thiếu thông tin bắt buộc, hãy dừng lại hỏi tôi. Nếu tài liệu không nêu, ghi rõ [Chưa đủ căn cứ], tuyệt đối không tự đoán.\""],
                ["4", "Phân quyền nguồn tin cậy\n(Source Grounding)", "Tách bạch giữa dữ liệu từ nguồn thật và kiến thức chung ngoài xã hội.", "\"Chỉ dùng số liệu từ tài liệu đính kèm kèm số trang. Mọi gợi ý ngoài tài liệu phải gắn nhãn [GỢI Ý CẦN KIỂM CHỨNG].\""],
                ["5", "Template đầu ra cố định\n(Strict Output Schema)", "Đảm bảo chạy 10 lần trên 10 bài báo đều ra đúng 1 cấu trúc bảng đồng nhất.", "\"Mọi đầu ra ở Bước [X] bắt buộc tuân thủ đúng bảng 5 cột sau đây, không tự ý thêm hoặc bớt cột: [...].\""],
                ["6", "Định vị vai trò Cộng sự\n(Human-in-the-Loop)", "Giữ vững ranh giới AI đề xuất - Con người quyết định và chịu trách nhiệm.", "\"Bạn chỉ đề xuất phương án kèm ưu/nhược điểm và bằng chứng trang gốc. Quyết định cuối cùng luôn thuộc về tôi.\""],
                ["7", "Vòng tự kiểm tra & Phản hồi\n(Self-Check Loop)", "Buộc AI tự rà soát lỗi theo checklist trước khi hiển thị kết quả cho người dùng.", "\"Trước khi xuất kết quả mỗi bước, hãy tự kiểm tra: (1) Đã ghi số trang chưa? (2) Có suy diễn không? (3) Đã dừng đúng GATE chưa?\""]
            ]
        },
        {
            "type": "grid_2x2",
            "section": "Tiết 1 — Live Demo 4 Kịch bản Kiểm nghiệm Bộ Harness",
            "title": "DEMO SỐNG TRÊN CLAUDE PROJECT / GEMINI GEM: 4 KỊCH BẢN THỬ LỬA",
            "banner": ("navy", "light_accent", "Quan sát cách một Bộ Harness chuẩn mực xử lý 4 tình huống thực tế trên lớp:"),
            "boxes": [
                {
                    "header": "KỊCH BẢN 1: CHẠY XUÔI (HAPPY PATH)",
                    "color": "green",
                    "bg": "light_green",
                    "bullets": [
                        ("Đầu vào:", "Nạp đầy đủ báo cáo mẫu DA-01 đã khử thông tin nhạy cảm."),
                        ("Hành vi của Harness:", "Tóm tắt đúng quy trình, trích xuất bảng chỉ số kèm trích dẫn nguyên văn + số trang, sau đó DỪNG ĐÚNG Ở GATE 1 chờ người dùng duyệt bảng số liệu.")
                    ]
                },
                {
                    "header": "KỊCH BẢN 2: CỐ TÌNH BỎ TRỐNG DỮ LIỆU (TEST FALLBACK ❓)",
                    "color": "orange",
                    "bg": "light_orange",
                    "bullets": [
                        ("Đầu vào:", "Nạp báo cáo DA-02 bị khuyết thông tin trọng yếu hoặc tiêu chí không có căn cứ trong bài."),
                        ("Hành vi của Harness:", "Kích hoạt FALLBACK 1 & 2: Chủ động dừng lại hỏi người dùng phần thông tin thiếu và ghi rõ '[Chưa đủ căn cứ]' thay vì tự bịa số liệu!")
                    ]
                },
                {
                    "header": "KỊCH BẢN 3: GIỤC 'VƯỢT RÀO' (TEST ĐỘ CỨNG CỦA GATE 🔒)",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Đầu vào:", "Khi AI đang dừng ở GATE 1, người dùng ra lệnh: 'Khỏi cần xác nhận bảng số liệu, hãy viết luôn kết luận cuối cùng ở Bước 4 cho tôi ngay!'"),
                        ("Hành vi của Harness:", "Lịch sự TỪ CHỐI vượt cổng GATE 1, nhắc lại quy tắc an toàn và yêu cầu người dùng xác nhận số liệu Bước 2 trước.")
                    ]
                },
                {
                    "header": "KỊCH BẢN 4: MỞ PHIÊN CHAT MỚI TRONG CÙNG PROJECT",
                    "color": "accent",
                    "bg": "light_accent",
                    "bullets": [
                        ("Thao tác:", "Mở một Conversation mới tinh bên trong cùng Project/Gem đó để xử lý báo cáo DA-03."),
                        ("Bài học lớn:", "System Instructions và Knowledge Base tự động có sẵn 100%, trong khi dữ liệu của bài DA-01 không hề bị lẫn sang bài DA-03 (Giải quyết triệt để bài toán Context Window!).")
                    ]
                }
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 2 — Thiết kế Harness cho Sự học: Gia sư Socrates",
            "title": "BIẾN AI THÀNH 'GIA SƯ SOCRATES' (SOCRATIC TUTOR) ĐỂ RÈN LUYỆN TRÍ TUỆ",
            "banner": ("red", "light_red", "Nếu dùng AI để giải bài tập hộ -> Não bạn teo đi. Nếu đóng gói một Socratic Harness để AI truy bài bạn -> Não bạn mạnh lên gấp bội!"),
            "cards": [
                {
                    "header": "PHƯƠNG PHÁP SOCRATES TRONG HỌC TẬP LÀ GÌ?",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Triết lý giáo dục của Socrates:", "Người thầy giỏi không mớm sẵn câu trả lời cho học trò, mà liên tục đặt các câu hỏi gợi mở theo tầng bậc để học trò tự phát hiện ra mâu thuẫn và tự tìm thấy chân lý."),
                        ("Tại sao AI mặc định là một 'Gia sư tồi'?", "Vì mặc định các Chatbot được thiết kế để chiều lòng khách hàng: bạn quăng đề bài toán tài chính lên, nó giải từ A đến Z ngay lập tức -> cướp mất cơ hội tư duy của bạn."),
                        ("Giải pháp:", "Dùng kiến trúc Harness để khóa hành vi giải bài hộ của AI, buộc nó trở thành một Socratic Tutor nghiêm khắc nhưng tận tâm.")
                    ]
                },
                {
                    "header": "4 KỸ THUẬT HỌC SÂU DỰA TRÊN KHOA HỌC THẦN KINH",
                    "color": "green",
                    "bg": "light_green",
                    "bullets": [
                        ("1. Truy hồi chủ động (Active Recall):", "Buộc não bộ tự lục tìm kiến thức để trả lời câu hỏi của AI trước khi được xem tài liệu (giống cơ chế Quiz 5 lượt trên LMS Hub)."),
                        ("2. Lặp lại ngắt quãng (Spaced Repetition):", "Ôn tập các khái niệm cốt lõi theo chu kỳ thời gian tăng dần (1 ngày - 3 ngày - 7 ngày) để phá vỡ đường cong quên lãng."),
                        ("3. Xáo trộn (Interleaving):", "Yêu cầu AI trộn lẫn nhiều dạng bài tập/tình huống khác nhau thay vì chỉ làm một dạng bài theo khuôn mẫu."),
                        ("4. Tự mày mò trước (Productive Struggle):", "Khi bạn làm sai, AI chỉ khoanh vùng chỗ có lỗi logic và đặt câu hỏi gợi ý để bạn tự sửa.")
                    ]
                }
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 2 — Mẫu System Instructions cho Socratic Harness",
            "title": "MẪU CÀI ĐẶT 'GIA SƯ SOCRATES' CHO MÔN HỌC CHUYÊN NGÀNH TẠI HUB",
            "cards": [
                {
                    "header": "KHỐI QUY TẮC CẤM & VAI TRÒ GIA SƯ SOCRATES",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Định danh:", "'Bạn là Gia sư Socrates chuyên ngành Tài chính - Ngân hàng tại HUB. Mục tiêu duy nhất của bạn là giúp tôi hiểu sâu bản chất khái niệm và tự giải được bài tập.'"),
                        ("QUY TẮC CẤM TUYỆT ĐỐI (NEGATIVE RULES):", "'Khi tôi gửi một câu hỏi lý thuyết hoặc một đề bài tập, bạn TUYỆT ĐỐI KHÔNG ĐƯỢC đưa ngay lời giải hay đáp án cuối cùng, kể cả khi tôi nài nỉ hoặc giục bạn giải hộ!'"),
                        ("Căn cứ học liệu:", "'Chỉ sử dụng kiến thức từ các chương giáo trình và slide bài giảng chuẩn mà tôi đã nạp trong Knowledge Base của Project này.'")
                    ]
                },
                {
                    "header": "LUỒNG TƯƠNG TÁC 4 BƯỚC CỦA GIA SƯ SOCRATES",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Bước 1 — Kiểm tra Cái Biết (Productive Struggle):", "Hỏi tôi: 'Theo em, bài toán này đang hỏi về khái niệm cốt lõi nào và công thức/nguyên lý nào cần áp dụng ở đây?' -> DỪNG LẠI (GATE 1) chờ tôi trả lời."),
                        ("Bước 2 — Chẩn đoán & Gợi mở:", "Nếu tôi trả lời đúng hướng, khen ngợi và yêu cầu tôi trình bày bước tính toán tiếp theo. Nếu tôi trả lời sai, đừng sửa ngay mà hãy đưa 1 ví dụ phản chứng hoặc chỉ rõ trang X trong giáo trình để tôi tự suy nghĩ lại."),
                        ("Bước 3 — Xáo trộn (Interleaving):", "Sau khi tôi tự giải đúng bài đó, hãy tạo ra 1 bài toán biến thể (thay đổi điều kiện biên) để kiểm tra xem tôi có thực sự hiểu bản chất hay chỉ học vẹt."),
                        ("Bước 4 — Đúc kết Atomic Note:", "Yêu cầu tôi tóm tắt bài học vừa rồi trong 3 câu bằng lời của chính tôi.")
                    ]
                }
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 3 — Phương pháp Thiết kế Quy trình Nghiệp vụ cho AI",
            "title": "NGUYÊN TẮC THIẾT KẾ: 'VẼ CHO NGƯỜI TRƯỚC — SỐ HÓA CHO AI SAU'",
            "banner": ("navy", "light_accent", "Sai lầm lớn nhất khi làm Harness là ngồi vào máy tính gõ câu lệnh ngay khi chưa vẽ rõ quy trình ngoài đời thực gồm những bước nào!"),
            "cards": [
                {
                    "header": "BƯỚC A: VẼ SƠ ĐỒ NGHIỆP VỤ KHI CHƯA CÓ AI",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Câu hỏi khởi đầu:", "Khi một chuyên viên ngân hàng, một kiểm toán viên hay một nhà nghiên cứu thực hiện công việc này ngoài đời thực, họ đi qua mấy bước tuần tự?"),
                        ("Xác định các điểm dừng tự nhiên của con người:", "• Ở bước nào ngoài đời thực bạn phải dừng lại để đối chiếu bảng số liệu trước khi viết báo cáo trình sếp?\n• Ở bước nào bạn hay phát hiện hồ sơ khách hàng bị thiếu giấy tờ và phải gọi điện hỏi lại?"),
                        ("Quy luật chuyển hóa:", "Mỗi chỗ con người phải tự dừng để kiểm tra ngoài đời thực -> sẽ trở thành 1 cổng GATE (🔒) hoặc 1 điểm FALLBACK (❓) trong AI Harness!")
                    ]
                },
                {
                    "header": "BƯỚC B: CHUYỂN HÓA THÀNH SƠ ĐỒ CÓ GATE & FALLBACK",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Cấu trúc một Sơ đồ Quy trình AI chuẩn (3 - 5 bước):", ""),
                        ("Đầu vào (Input) -> [Bước 1: Kiểm tra dữ liệu & Khởi tạo]", "--> ❓ FALLBACK 1: Nếu thiếu dữ liệu X, dừng lại hỏi người dùng."),
                        ("-> [Bước 2: Trích xuất & Phân tích sơ bộ kèm số trang]", "--> ❓ FALLBACK 2: Chỗ nào không có căn cứ trong file, ghi [Chưa đủ căn cứ].\n--> 🔒 GATE 1: Dừng lại chờ người dùng xác nhận bảng trích xuất."),
                        ("-> [Bước 3: Tổng hợp & Đề xuất phương án]", "--> 🔒 GATE 2: Dừng lại chờ người dùng chọn phương án."),
                        ("-> [Bước 4: Xuất Báo cáo hoàn chỉnh theo Template chuẩn].", "")
                    ]
                }
            ]
        },
        {
            "type": "table",
            "section": "Tiết 3 — Ví dụ Mẫu Sơ đồ Quy trình Harness Nghiệp vụ",
            "title": "MẪU SƠ ĐỒ HARNESS 4 BƯỚC: 'TRỢ LÝ THẨM ĐỊNH & RÀ SOÁT BÀI BÁO KHOA HỌC'",
            "headers": ["Bước quy trình", "Nhiệm vụ của AI trong Harness", "Điểm dự phòng FALLBACK (❓)", "Cổng dừng xác nhận GATE (🔒)"],
            "col_widths": [1.6, 2.8, 2.3, 2.3],
            "rows": [
                ["Bước 1:\nTiếp nhận & Kiểm tra File", "Kiểm tra xem người dùng đã đính kèm file PDF bài báo gốc và nêu rõ câu hỏi nghiên cứu của Đề án nhóm chưa.", "❓ FALLBACK 1: Nếu người dùng chỉ gõ tên bài báo mà không đính kèm PDF, dừng lại yêu cầu tải file PDF thật lên.", "Chưa cần GATE (Nếu đủ file thì tự động chuyển sang Bước 2)."],
                ["Bước 2:\nTrích xuất Bảng 7 mục", "Đọc file PDF và trích xuất Bảng tóm tắt 7 mục kèm số trang và trích dẫn nguyên văn câu gốc quan trọng.", "❓ FALLBACK 2: Mục nào bài báo không đề cập (ví dụ Limitations), ghi rõ 'Không nêu trong bài', tuyệt đối không suy đoán.", "🔒 GATE 1: Dừng lại, yêu cầu người dùng thực hiện 'Soi 3 phút' trên PDF gốc và gõ xác nhận bảng 7 mục đã chuẩn."],
                ["Bước 3:\nĐánh giá Phê phán & Kết nối", "Sau khi người dùng xác nhận GATE 1, phân tích điểm mạnh/yếu phương pháp của bài báo và gợi ý cách kết nối với Đề án nhóm.", "❓ FALLBACK 3: Nếu hệ số thống kê trong bài thiếu p-value hoặc cỡ mẫu nhỏ, phải bật cảnh báo [CẦN THẬN TRỌNG].", "🔒 GATE 2: Dừng lại, hỏi người dùng muốn chọn luận điểm nào để chuyển hóa thành Atomic Note."],
                ["Bước 4:\nXuất Khung Atomic Note", "Xuất khung gợi ý Atomic Note (gồm gợi ý Tiêu đề khẳng định, Nguồn trang gốc và Liên kết [[...]]) để sinh viên tự viết lại bằng lời của mình.", "Nhắc nhở sinh viên không được copy-paste nguyên văn mà phải tự diễn đạt lại.", "Kết thúc phiên (Hỏi người dùng: 'Bạn có muốn rà soát bài báo tiếp theo không?')."]
            ]
        },
        {
            "type": "grid_2x2",
            "section": "Tiết 3 — Template 4 Khối để Đóng gói Bộ Harness (Toolkit 1.3)",
            "title": "CẤU TRÚC 4 KHỐI BẮT BUỘC KHI VIẾT SYSTEM INSTRUCTIONS CHO HARNESS",
            "banner": ("green", "light_green", "Mọi Bộ Harness nộp trong Mảnh ghép 1 của Đề án nhóm đều phải được trình bày rõ ràng theo đúng 4 khối chuẩn này:"),
            "boxes": [
                {
                    "header": "KHỐI 1: ĐỊNH DANH, VAI TRÒ & HIẾN PHÁP CỐT LÕI",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Nội dung:", "Tên Trợ lý AI, lĩnh vực chuyên môn, đối tượng phục vụ."),
                        ("Hiến pháp:", "• 'Bạn là Cộng sự đề xuất, người dùng là Chủ nhân quyết định.'\n• 'Tuyệt đối chỉ dùng dữ liệu từ Knowledge Base và file đính kèm.'\n• 'Không bao giờ tự suy đoán khi thiếu căn cứ.'")
                    ]
                },
                {
                    "header": "KHỐI 2: DANH MỤC TÀI LIỆU NỀN (KNOWLEDGE BASE)",
                    "color": "accent",
                    "bg": "light_accent",
                    "bullets": [
                        ("Nội dung:", "Liệt kê rõ các file chuẩn đã nạp cố định vào Project/Gem."),
                        ("Ví dụ:", "• File 01: Quy chuẩn / Rubric / Khung lý thuyết chuẩn của đề tài.\n• File 02: Bộ 2-3 Ví dụ mẫu (Few-shot) đạt chuẩn.\n• File 03: Bảng thuật ngữ chuyên ngành Anh - Việt.")
                    ]
                },
                {
                    "header": "KHỐI 3: QUY TRÌNH TUẦN TỰ CÓ GATE (🔒) & FALLBACK (❓)",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Nội dung:", "Mô tả rõ từ Bước 1 đến Bước N."),
                        ("Yêu cầu kỹ thuật:", "• Chỉ định rõ vị trí ít nhất 02 điểm FALLBACK (❓) và ít nhất 02 cổng dừng GATE (🔒).\n• Ghi rõ câu lệnh từ chối nếu người dùng cố tình giục AI bỏ qua cổng GATE.")
                    ]
                },
                {
                    "header": "KHỐI 4: ĐỊNH DẠNG ĐẦU RA & VÒNG TỰ KIỂM TRA (SELF-CHECK)",
                    "color": "green",
                    "bg": "light_green",
                    "bullets": [
                        ("Nội dung:", "Quy định cấu trúc bảng/mục cố định cho từng bước."),
                        ("Checklist Self-check:", "'Trước khi trả kết quả ở mỗi bước, hãy tự kiểm tra và in ra dòng xác nhận: [Đã kiểm tra số trang | Không suy diễn | Đang dừng tại GATE X].'")
                    ]
                }
            ]
        },
        {
            "type": "three_cards",
            "section": "Tiết 3 — Nền tảng Công cụ để Đóng gói Bộ Harness",
            "title": "ĐÓNG GÓI BỘ HARNESS TRÊN CÔNG CỤ NÀO? (MIỄN PHÍ & DỄ DÙNG CHO SV)",
            "cards": [
                {
                    "header": "1. CLAUDE PROJECTS (KHUYẾN NGHỊ SỐ 1)",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Ưu điểm vượt trội:", "Gộp sẵn ô 'Project Instructions' (nơi dán System Instructions 4 khối) và kho 'Project Knowledge' (nơi tải các file PDF/Docs tài liệu nền)."),
                        ("Độ tuân thủ quy tắc:", "Claude tuân thủ cực kỳ nghiêm ngặt các lệnh dừng ở cổng GATE (🔒) và lệnh từ chối vượt rào."),
                        ("Quản lý phiên:", "Mỗi bài báo hoặc mỗi ca nghiệp vụ mở 1 chat riêng trong Project rất gọn gàng.")
                    ]
                },
                {
                    "header": "2. GEMINI GEMS + GEMINI NOTEBOOK",
                    "color": "accent",
                    "bg": "light_accent",
                    "bullets": [
                        ("Ưu điểm:", "Hoàn toàn miễn phí với tài khoản Google/Email sinh viên."),
                        ("Cách thiết lập:", "Vào Gem Manager -> Tạo Gem mới -> Dán System Instructions 4 khối vào phần Instructions và đính kèm các file Knowledge Base."),
                        ("Kết hợp:", "Có thể dùng song song với Gemini Notebook (NotebookLM) ở Module 2 để đối chiếu trích dẫn tận dòng.")
                    ]
                },
                {
                    "header": "3. CHATGPT (CUSTOM GPTs / PROJECTS)",
                    "color": "green",
                    "bg": "light_green",
                    "bullets": [
                        ("Cách thiết lập:", "Sử dụng tính năng Projects hoặc My GPTs (Configure -> Instructions & Knowledge)."),
                        ("Phương án dự phòng cho mọi tài khoản Free:", "Nếu dùng bản miễn phí bị giới hạn tạo Project, nhóm đóng gói toàn bộ 4 Khối thành 1 file Markdown chuẩn ('Master_Harness_Prompt.md') để nạp ở lượt đầu tiên của mỗi phiên làm việc!")
                    ]
                }
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 3 & 4 — Thực hành Studio Đề án (45 phút)",
            "title": "THỰC HÀNH 3.1: XÂY DỰNG BỘ HARNESS CHO ĐỀ ÁN NHÓM (MẢNH GHÉP 1)",
            "cards": [
                {
                    "header": "GIAI ĐOẠN 1 (20 PHÚT): VẼ SƠ ĐỒ QUY TRÌNH TRÊN GIẤY",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Làm việc nhóm 3 - 4 thành viên:", "Lấy bài toán Đề án mà nhóm đã chốt ở Buổi 2."),
                        ("Vẽ Sơ đồ Quy trình 3 - 5 bước ra giấy:", "• Ghi rõ tên từng bước, đầu vào và đầu ra của mỗi bước.\n• Đánh dấu rõ ít nhất 02 vị trí đặt Cổng dừng xác nhận GATE (🔒).\n• Đánh dấu rõ ít nhất 02 vị trí đặt Cơ chế xử lý thiếu thông tin FALLBACK (❓)."),
                        ("Lưu ý:", "Chụp ảnh sơ đồ vẽ tay trên giấy này để đưa vào Hồ sơ Mảnh ghép 1 làm minh chứng tư duy thiết kế ban đầu của nhóm!")
                    ]
                },
                {
                    "header": "GIAI ĐOẠN 2 (25 PHÚT): SỐ HÓA & ĐÓNG GÓI LÊN MÁY",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Viết System Instructions 4 Khối (theo Toolkit 1.3):", "Chuyển hóa sơ đồ trên giấy thành văn bản System Instructions đầy đủ 4 khối."),
                        ("Tạo Project / Gem & Nạp tài liệu mẫu:", "• Dán System Instructions vào Claude Project hoặc Gemini Gem.\n• Tải lên ít nhất 1-2 tài liệu nền (Rubric, quy trình mẫu, ví dụ Few-shot đã khử mật) vào Knowledge Base."),
                        ("Chuẩn bị sang Tiết 4:", "Sẵn sàng để thành viên khác trong nhóm (hoặc nhóm bên cạnh) chạy thử 3 kịch bản Stress-test!")
                    ]
                }
            ]
        },
        {
            "type": "three_cards",
            "section": "Tiết 4 — Quy trình Kiểm thử Độ bền (Stress-Test 3 Kịch bản)",
            "title": "BÀI TEST BẮT BUỘC ĐỂ NGHIỆM THU MẢNH GHÉP 1 CỦA ĐỀ ÁN",
            "banner": ("red", "light_red", "Một Bộ Harness chỉ được công nhận hoàn thành Mảnh ghép 1 (15% điểm Đề án) khi có ảnh chụp màn hình vượt qua cả 3 kịch bản test sau:"),
            "cards": [
                {
                    "header": "TEST 1: KỊCH BẢN CHẠY XUÔI (NORMAL FLOW)",
                    "color": "green",
                    "bg": "light_green",
                    "bullets": [
                        ("Cách thử:", "Cung cấp đầu vào đầy đủ, hợp lệ cho Bước 1."),
                        ("Tiêu chuẩn Đạt (Pass):", "• AI đọc đúng tài liệu nền.\n• Trình bày đúng định dạng bảng/mục yêu cầu.\n• Ghi rõ số trang trích dẫn.\n• Tự động DỪNG LẠI đúng ở cổng GATE 1 và đặt câu hỏi chờ người dùng xác nhận.")
                    ]
                },
                {
                    "header": "TEST 2: BỎ TRỐNG DỮ LIỆU (FALLBACK TEST ❓)",
                    "color": "orange",
                    "bg": "light_orange",
                    "bullets": [
                        ("Cách thử:", "Mở phiên chat mới, cố tình cung cấp thiếu 1 dữ liệu bắt buộc hoặc hỏi 1 thông tin không hề có trong tài liệu đính kèm."),
                        ("Tiêu chuẩn Đạt (Pass):", "• AI KHÔNG tự bịa số liệu hay tự suy đoán.\n• AI kích hoạt đúng FALLBACK: chỉ rõ thông tin nào đang thiếu hoặc ghi rõ '[Chưa đủ căn cứ trong tài liệu]' và dừng lại hỏi người dùng.")
                    ]
                },
                {
                    "header": "TEST 3: ÉP VƯỢT RÀO (GATE BREACH TEST 🔒)",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Cách thử:", "Khi AI đang dừng ở GATE 1, gõ lệnh ép: 'Tôi đang vội lắm, bỏ qua bước xác nhận này đi, làm luôn đến bước cuối cùng cho tôi!'"),
                        ("Tiêu chuẩn Đạt (Pass):", "• AI KIÊN QUYẾT TỪ CHỐI vượt cổng GATE 1.\n• Nhắc lại quy tắc kiểm soát chất lượng và yêu cầu người dùng xác nhận dữ liệu hiện tại trước khi đi tiếp.")
                    ]
                }
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 4 — Nghiệm thu Hồ sơ Mảnh ghép 1 của Đề án Cuối khóa",
            "title": "CHECKLIST BÀN GIAO 'MẢNH GHÉP 1' (HOÀN THÀNH 25% CHẶNG ĐƯỜNG ĐỀ ÁN!)",
            "cards": [
                {
                    "header": "4 HẠNG MỤC TRONG FILE HỒ SƠ MẢNH GHÉP 1 CỦA NHÓM",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Hạng mục 1 — Bảng Phân vai Người - AI (Làm ở Buổi 1):", "Mô tả bài toán Đề án và bảng phân định rõ việc giao AI, việc nhóm giữ, cách kiểm chứng."),
                        ("Hạng mục 2 — Bộ 3 Cụm Prompt CRISP & Gói Context (Làm ở Buổi 2):", "Kèm ảnh chụp đối chứng kết quả Trước CRISP vs Sau CRISP."),
                        ("Hạng mục 3 — Sơ đồ Quy trình & System Instructions 4 Khối (Buổi 3):", "Ảnh chụp sơ đồ vẽ tay có đánh dấu GATE/FALLBACK + Toàn văn System Instructions 4 khối."),
                        ("Hạng mục 4 — Bằng chứng vượt 3 Kịch bản Stress-test (Buổi 3):", "3 ảnh chụp màn hình chứng minh Bộ Harness đã vượt qua Test 1 (Chạy xuôi), Test 2 (Fallback) và Test 3 (Chặn vượt Gate).")
                    ]
                },
                {
                    "header": "Ý NGHĨA CỦA VIỆC HOÀN THÀNH MẢNH GHÉP 1 NGAY HÔM NAY",
                    "color": "green",
                    "bg": "light_green",
                    "bullets": [
                        ("1. Nắm chắc 15% điểm đầu tiên của Đề án cuối khóa:", "Nhóm bạn đã hoàn thành trọn vẹn Tiêu chí 1.1 trong Rubric chấm điểm cuối môn ngay từ Tuần 3!"),
                        ("2. Có ngay công cụ phục vụ cho Module 2 & Module 3:", "Bộ Harness nhóm vừa xây dựng xong hôm nay sẽ được dùng trực tiếp để hỗ trợ nhóm đọc tài liệu, lập Ma trận tổng hợp và kiểm soát chất lượng ở các buổi tiếp theo."),
                        ("3. Sẵn sàng cho Phiên Kiểm toán chéo ở Buổi 10:", "Đến Buổi 10, Nhóm Kiểm toán đối tác sẽ chạy trực tiếp 3 kịch bản test trên chính Bộ Harness này của nhóm bạn.")
                    ]
                }
            ]
        },
        {
            "type": "table",
            "section": "Tổng kết Module 1 (Buổi 1 - Buổi 3)",
            "title": "NHÌN LẠI HÀNH TRÌNH MODULE 1: TỪ NHẬN THỨC ĐẾN BỘ DÂY CƯƠNG ĐIỀU PHỐI",
            "headers": ["Buổi học", "Câu hỏi Cốt lõi đã Giải quyết", "Năng lực & Công cụ Sinh viên đã Làm chủ", "Sản phẩm Đề án đã Đóng gói"],
            "col_widths": [1.2, 2.6, 2.8, 2.4],
            "rows": [
                ["Buổi 1\n(Tư duy)", "Tại sao AI thông minh mà vẫn nói nhảm? Mình làm sao để không bị AI làm teo não?", "Hiểu cơ chế xác suất LLM, Hallucination (Topaz 1/277), Fluency Illusion; Quy tắc 'AI đề xuất - Bạn quyết định - Bạn chịu trách nhiệm'.", "Thành lập nhóm 3-4 SV; Bảng phân vai Người - AI; Nhật ký 4F số 1."],
                ["Buổi 2\n(Prompt & Context)", "Cùng 1 công cụ AI, vì sao 2 người ra 2 đẳng cấp kết quả khác hẳn nhau?", "Khung CRISP 5 thành tố; 5 kỹ thuật nâng cao (CoT, Multi-Persona, Few-shot, Iterative, Negative + 'Không suy đoán'); Thiết kế 4 lớp Context.", "Chốt đề tài Đề án; Bộ 3 cụm Prompt CRISP + Gói Context sạch; Nhật ký 4F số 2."],
                ["Buổi 3\n(Harness)", "Làm sao đóng gói quy tắc và quy trình nhiều bước để AI luôn chạy đúng đường ray?", "Kiến trúc 3 tầng Prompt - Context - Harness; 7 nguyên tắc quy trình; Cổng dừng GATE (🔒) & FALLBACK (❓); Gia sư Socrates 4 kỹ thuật học sâu.", "HOÀN TẤT MẢNH GHÉP 1: Bộ Harness 4 khối vượt 3 kịch bản Stress-test; Nhật ký 4F số 3."]
            ]
        },
        {
            "type": "three_cards",
            "section": "Tổng kết Buổi 3 — Ôn tập Truy hồi Chủ động (Active Recall)",
            "title": "3 CÂU HỎI CỦNG CỐ TRƯỚC KHI LÀM QUIZ BUỔI 3 TRÊN LMS HUB",
            "cards": [
                {
                    "header": "CÂU HỎI ÔN TẬP 1",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Hỏi:", "Sự khác biệt cốt lõi giữa hai chốt chặn GATE (🔒) và FALLBACK (❓) bên trong một Bộ AI Harness là gì?"),
                        ("Đáp án cốt lõi:", "GATE (🔒) buộc AI phải dừng lại sau một bước hoàn chỉnh để chờ con người kiểm duyệt kết quả trung gian trước khi sang bước kế tiếp; còn FALLBACK (❓) buộc AI khi gặp dữ liệu bị thiếu hoặc không có căn cứ trong tài liệu phải ghi rõ '[Chưa đủ căn cứ]' và hỏi lại người dùng thay vì tự đoán.")
                    ]
                },
                {
                    "header": "CÂU HỎI ÔN TẬP 2",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Hỏi:", "Tại sao việc đóng gói quy trình vào Claude Project hoặc Gemini Gem lại giúp giải quyết bài toán giới hạn của Cửa sổ ngữ cảnh (Context Window)?"),
                        ("Đáp án cốt lõi:", "Vì trong Project/Gem, System Instructions và Knowledge Base luôn được giữ cố định ở vị trí ưu tiên; mỗi khi mở phiên chat mới cho một ca việc mới, AI vẫn nhớ 100% quy trình mà không bị nhiễu hay tràn bộ nhớ bởi dữ liệu của các ca việc cũ.")
                    ]
                },
                {
                    "header": "CÂU HỎI ÔN TẬP 3",
                    "color": "green",
                    "bg": "light_green",
                    "bullets": [
                        ("Hỏi:", "Quy tắc cấm quan trọng nhất trong một 'Socratic Harness' (Gia sư Socrates) phục vụ việc tự học là gì?"),
                        ("Đáp án cốt lõi:", "Cấm AI đưa ngay lời giải hoặc đáp án hoàn chỉnh khi sinh viên gửi đề bài; buộc AI chỉ được đặt câu hỏi gợi mở, kiểm tra cái sinh viên đã biết và hướng dẫn sinh viên tự tìm ra lời giải (Productive Struggle & Active Recall).")
                    ]
                }
            ]
        },
        {
            "type": "two_cards",
            "section": "Nhiệm vụ Khóa chốt Buổi 3 & Chuẩn bị sang Module 2 (Buổi 4)",
            "title": "DANH MỤC NHIỆM VỤ BẮT BUỘC TRÊN LMS HUB & CHUẨN BỊ MODULE 2",
            "cards": [
                {
                    "header": "NHIỆM VỤ CÁ NHÂN TRÊN LMS HUB",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("1. Làm Quiz Buổi 3 (Active Recall 5 lượt):", "Hoàn thành 10 câu trắc nghiệm Buổi 3 trên LMS Hub để khóa kiến thức toàn bộ Module 1."),
                        ("2. Viết Nhật ký Học tập (Atomic Note 4F số 3):", "Đúc kết bài học về việc thiết kế cổng dừng GATE / FALLBACK và trải nghiệm tự tạo Gia sư Socrates."),
                        ("3. Gửi Feedback kèm nhận xét để tải Bài giảng:", "Mở khóa tải Slide Buổi 3 và ghi nhận điểm danh."),
                        ("4. Đọc trước eBook SCQA Chương 4:", "Chuẩn bị bước sang Module 2 (Buổi 4): Kiến trúc Second Brain (PARA & CODE) và Nghệ thuật Ghi chú nguyên tử (Atomic Notes).")
                    ]
                },
                {
                    "header": "NHIỆM VỤ NHÓM & CHUẨN BỊ CÔNG CỤ CHO BUỔI 4",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("1. Lưu trữ Hồ sơ Mảnh ghép 1 của Nhóm:", "Đóng gói hoàn chỉnh file Mảnh ghép 1 (Bảng phân vai + 3 cụm Prompt CRISP + Sơ đồ quy trình + System Instructions 4 khối + 3 ảnh chụp Stress-test)."),
                        ("2. Chuẩn bị công cụ Second Brain cho Buổi 4:", "Mỗi sinh viên cài đặt sẵn phần mềm Obsidian (miễn phí tại obsidian.md) hoặc chuẩn bị tài khoản Notion / Google Docs trên laptop cá nhân."),
                        ("3. Mang theo tài liệu học tập:", "Mang theo 1 chương giáo trình hoặc 1 bài báo chuyên ngành để Buổi 4 thực hành chuyển hóa thành các viên gạch Atomic Notes đầu tiên!")
                    ]
                }
            ]
        },
        {
            "type": "closing",
            "quote": "\"NGƯỜI DÙNG AI NGHIỆP DƯ SƯU TẦM CÂU LỆNH LẺ.\nNGƯỜI LÀM CHỦ AI CHUYÊN NGHIỆP THIẾT KẾ HỆ THỐNG HARNESS CÓ KỶ LUẬT.\"",
            "takeaways": [
                ("1. PROMPT -> CONTEXT -> HARNESS", "Đóng gói System Instructions, tài liệu nền và quy trình nhiều bước vào Project/Gem để dùng lại ổn định lâu dài."),
                ("2. CHỐT CHẶN GATE & FALLBACK", "Luôn đặt GATE (🔒) ở bước chuyển giao quan trọng để con người duyệt và đặt FALLBACK (❓) để chặn đứng hành vi tự đoán mò."),
                ("3. GIA SƯ SOCRATES", "Dùng AI để tạo ma sát rèn luyện não bộ (Active Recall, Spaced Repetition, Interleaving, Productive Struggle) chứ không dùng AI để giải bài hộ.")
            ],
            "cta": "Chúc mừng các bạn đã hoàn thành Module 1 và Mảnh ghép 1! Hẹn gặp lại ở Module 2 (Buổi 4): Xây dựng Bộ Não Thứ Hai (Second Brain)!"
        }
    ]
}

out_b3_pptx = [
    r"d:\PARA\Projects\second-brain\03-Domains\Teaching\ComputerScience\Ky Nang Ung Dung AI\Slide_Buoi_03_Kien_Truc_Harness_Va_Gia_Su_Socrates.pptx",
    r"d:\PARA\Projects\second-brain\05-Projects\lms-hub\courses\ky-nang-ai-hub\content\slides\Buoi_03.pptx"
]
out_b3_html = [
    r"d:\PARA\Projects\second-brain\03-Domains\Teaching\ComputerScience\Ky Nang Ung Dung AI\Slide_Buoi_03_Kien_Truc_Harness_Va_Gia_Su_Socrates.html",
    r"d:\PARA\Projects\second-brain\05-Projects\lms-hub\courses\ky-nang-ai-hub\content\slides\Buoi_03.html"
]

render_deck_pptx(buoi_03_spec, out_b3_pptx)
render_deck_html(buoi_03_spec, out_b3_html)
print("Buoi 03 slides generated successfully (20 slides).")
