# -*- coding: utf-8 -*-
import os
from module1_engine import render_deck_pptx, render_deck_html

# ===========================================================================
# BUỔI 1 (20 SLIDES): BẢN CHẤT AI & TƯ DUY NGƯỜI LÀM CHỦ ("AI LÀ TRỢ LÝ, BẠN LÀ CHỦ")
# ===========================================================================
buoi_01_spec = {
    "doc_title": "Buổi 1: Bản chất AI & Tư duy người làm chủ — ĐH Ngân hàng TP.HCM (HUB)",
    "slides": [
        {
            "type": "cover",
            "module_badge": "MODULE 1 (BUỔI 1 / 11) — BẢN CHẤT AI, PROMPT, CONTEXT & HARNESS",
            "title": "BUỔI 1: BẢN CHẤT AI & TƯ DUY NGƯỜI LÀM CHỦ\n\"AI LÀ TRỢ LÝ, BẠN LÀ CHỦ\"",
            "subtitle": "Câu hỏi cốt lõi: Tại sao AI thông minh đến vậy mà nhiều khi vẫn tự tin nói nhảm?",
            "badges": [
                "THỜI LƯỢNG: 4 TIẾT (200 PHÚT)\n35% Tư duy & Demo - 65% Thực hành",
                "CHUẨN ĐẦU RA: CLO1 & CLO3\nCơ chế Xác suất & Phân vai Người - Máy",
                "CỘT MỐC ĐỀ ÁN CUỐI KHÓA\nLập nhóm 3-4 SV & Bảng phân vai số 1"
            ]
        },
        {
            "type": "numbered_list",
            "section": "Buổi 1 — Mục tiêu & Lộ trình 200 phút",
            "title": "MỤC TIÊU HỌC TẬP & LỘ TRÌNH 4 TIẾT CỦA BUỔI 1",
            "items": [
                ("01", "Tiết 1 (50'): Cú sốc nhận thức & Khoảng cách kiểm chứng",
                 "Story Spine nhân vật Minh (bài tiểu luận 6/10); Hai câu hỏi giơ tay; Bằng chứng thực nghiệm Topaz (The Lancet, 5/2026: 1/277 bài PubMed dính trích dẫn bịa).", "red"),
                ("02", "Tiết 2 (50'): Giải mã Hộp đen — AI không phải phép thuật, AI là xác suất",
                 "Live Demo 'Bẫy AI nói nhảm'; Cơ chế dự đoán từ tiếp theo (Next-token Prediction); So sánh bản chất LLM vs Google Search vs Cơ sở dữ liệu.", "navy"),
                ("03", "Tiết 3 (50'): Hai cái bẫy nhận thức & Khung phân vai 'Việc nào giao - Việc nào giữ'",
                 "Ảo tưởng trôi chảy (Fluency Illusion) & Lệ thuộc nhận thức (Cognitive Offloading); Bộ ba động từ: AI đề xuất - Bạn quyết định - Bạn chịu trách nhiệm; Bản đồ công cụ 2026.", "accent"),
                ("04", "Tiết 4 (50'): Thực hành Phân vai Đề án & Khóa chốt LMS Hub",
                 "Lập nhóm Đề án (3-4 SV cùng ngành); Phân rã quy trình bài toán chuyên ngành; Viết Nhật ký Atomic Note phản tư 4F số 1 & làm Quiz Buổi 1.", "green")
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 1 — Story Spine & Khung SCQA",
            "title": "CÂU CHUYỆN CỦA MINH (KỲ 1): BÀI TIỂU LUẬN 30 PHÚT VÀ CON ĐIỂM 6/10",
            "banner": ("red", "light_red", "Bắt đầu từ trải nghiệm thật: Đã bao giờ bạn nộp một bài viết do AI hỗ trợ mà trong lòng thấp thỏm sợ thầy cô gọi lên hỏi?"),
            "cards": [
                {
                    "header": "S & C — TÌNH HUỐNG VÀ CÚ VẤP CỦA MINH",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Tình huống (Situation):", "Minh (SV năm 2 ngành Tài chính - Ngân hàng tại HUB) nhận đề tiểu luận. Minh mở ChatGPT gõ 2 dòng, sau 30 giây có ngay bài viết 1.500 chữ cực kỳ trôi chảy, có cả số liệu tỷ lệ nợ xấu."),
                        ("Biến cố (Complication):", "Tuần sau giảng viên gọi Minh lên hỏi đúng 2 câu: (1) 'Số liệu nợ xấu trang 2 em lấy từ báo cáo nào?' và (2) 'Tại sao em chọn mô hình này?'. Minh đứng hình không trả lời được!"),
                        ("Sự thật phũ phàng:", "Con số đó do AI tự bịa ra (Hallucination), còn kiến thức bài viết chưa bao giờ đi qua bộ não của Minh.")
                    ]
                },
                {
                    "header": "Q & A — CÂU HỎI MỞ ĐẦU HÀNH TRÌNH 11 BUỔI",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Câu hỏi 1:", "Nếu AI không thực sự 'biết' những gì nó nói, làm sao để dùng AI mà KHÔNG bị nó dắt mũi?"),
                        ("Câu hỏi 2:", "Nếu bạn để AI làm thay quá nhiều việc, thì sau 4 năm đại học, cái gì còn lại là năng lực của chính bạn?"),
                        ("Định hướng giải quyết (Answer):", "Phải hiểu tận gốc cơ chế xác suất của LLM, nắm vững quy tắc phân vai 'AI đề xuất - Bạn quyết định - Bạn chịu trách nhiệm' và xây dựng Bộ Não Thứ Hai (Second Brain).")
                    ]
                }
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 1 — Khảo sát & Khoảng cách nhận thức",
            "title": "HAI CÂU HỎI GIƠ TAY: KHOẢNG CÁCH GIỮA 'DÙNG AI' VÀ 'KIỂM CHỨNG AI'",
            "cards": [
                {
                    "header": "CÂU HỎI 1: AI ĐÃ TỪNG DÙNG AI LÀM BÀI?",
                    "color": "accent",
                    "bg": "light_accent",
                    "big_stat": "~ 95% - 100% Cánh tay giơ lên",
                    "bullets": [
                        ("Thực trạng phổ biến:", "Hầu hết sinh viên đã dùng ChatGPT, Claude, Gemini hoặc DeepSeek để tìm tài liệu, tóm tắt giáo trình, viết tiểu luận hoặc giải bài tập."),
                        ("Tâm lý tự nhiên:", "Khi thấy AI trả lời bằng giọng văn học thuật trang trọng, chia mục rõ ràng, có tên tác giả và năm xuất bản, con người có xu hướng mặc định tin đó là sự thật."),
                        ("Lợi ích ngắn hạn:", "Tiết kiệm thời gian trước mắt, tạo cảm giác hoàn thành công việc rất nhanh.")
                    ]
                },
                {
                    "header": "CÂU HỎI 2: AI ĐÃ KIỂM TRA TỪNG NGUỒN AI ĐƯA RA?",
                    "color": "red",
                    "bg": "light_red",
                    "big_stat": "< 10% Cánh tay còn giữ nguyên",
                    "bullets": [
                        ("Khoảng cách nguy hiểm:", "Hơn 90% người dùng chép hoặc tin kết quả của AI mà KHÔNG mở tài liệu gốc để kiểm tra xem bài báo đó có tồn tại hay không, số liệu có khớp bảng gốc không."),
                        ("Hậu quả trực tiếp:", "Đưa tài liệu tham khảo giả (fabricated citations) và số liệu bịa vào bài tiểu luận, đề tài nghiên cứu khoa học và khóa luận tốt nghiệp."),
                        ("Mục tiêu của môn học:", "Xóa bỏ hoàn toàn khoảng cách giữa Câu hỏi 1 và Câu hỏi 2 bằng kỷ luật và công cụ kiểm chứng.")
                    ]
                }
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 1 — Bằng chứng thực nghiệm từ The Lancet (5/2026)",
            "title": "1/277 BÀI BÁO KHOA HỌC TRÊN PUBMED TRÍCH DẪN TÀI LIỆU KHÔNG TỒN TẠI!",
            "banner": ("navy", "light_accent", "Nguồn kiểm chứng: Topaz và cộng sự, thư gửi tạp chí y khoa The Lancet (Tập 407, tr.1779-1781, tháng 5/2026), DOI: 10.1016/S0140-6736(26)00603-3"),
            "cards": [
                {
                    "header": "SỐ LIỆU TĂNG GẤP 10 LẦN TỪ 2023 ĐẾN ĐẦU 2026",
                    "color": "red",
                    "bg": "light_red",
                    "big_stat": "2023: 1/2.828  -->  2026: 1/277",
                    "bullets": [
                        ("Quy mô kiểm tra khổng lồ:", "Nhóm Topaz quét gần 2,5 triệu bài báo trên PubMed, xác minh khoảng 97 triệu tài liệu tham khảo."),
                        ("Phát hiện chấn động:", "Tìm thấy 4.046 tài liệu tham khảo hoàn toàn bịa nằm trong 2.810 bài báo khoa học đã xuất bản."),
                        ("Đà tăng theo từng năm:", "Năm 2023 là 1/2.828 bài -> Năm 2025 là 1/458 bài -> 7 tuần đầu năm 2026 vọt lên 1/277 bài!"),
                        ("Chưa bị xử lý:", "Hơn 98,4% số bài chứa trích dẫn bịa này vẫn chưa có hành động thu hồi từ nhà xuất bản tại thời điểm kiểm tra.")
                    ]
                },
                {
                    "header": "BÀI HỌC VỀ ĐỌC PHÊ PHÁN (CRITICAL READING)",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Ngay cả nghiên cứu về lỗi AI cũng cần đọc kỹ:", "Đại diện Cochrane (Ella Flemyng, qua Retraction Watch) nhận xét phương pháp dùng công cụ tự động kiểm tra của nhóm Topaz cũng cần công bố thêm chi tiết."),
                        ("Phần nổi của tảng băng chìm:", "Nhà nghiên cứu đạo đức khoa học Mohammad Hosseini (ĐH Northwestern) chỉ ra: trích dẫn bịa hoàn toàn mới chỉ là phần dễ bắt nhất!"),
                        ("Nguy cơ lớn hơn:", "Đó là những trích dẫn CÓ THẬT trên Google Scholar nhưng bị AI diễn giải sai lệch, thiên lệch hoặc gán cho một ý mà tác giả bài gốc không hề nói.")
                    ]
                }
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 2 — Giải mã Hộp đen của AI tạo sinh",
            "title": "AI TẠO SINH (LLM) KHÔNG PHẢI PHÉP THUẬT — NÓ LÀ 'CỖ MÁY ĐOÁN CHỮ'",
            "cards": [
                {
                    "header": "TRÒ CHƠI ĐIỀN VÀO CHỖ TRỐNG & XÁC SUẤT TOKEN",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Ví dụ trực quan:", "Khi nghe câu: 'Ngân hàng Nhà nước quyết định điều chỉnh lãi suất...', từ tiếp theo bạn đoán là gì? ('điều hành' = 45%, 'tái cấp vốn' = 30%, 'cơ bản' = 15%, còn 'cá heo' = 0,00001%)."),
                        ("Cơ chế Next-Token Prediction:", "Mô hình ngôn ngữ lớn (Large Language Model) được huấn luyện trên hàng tỷ văn bản để tính phân phối xác suất xem từ (token) nào có khả năng xuất hiện tiếp theo cao nhất."),
                        ("Bản chất cốt lõi:", "LLM KHÔNG 'hiểu' ý nghĩa kinh tế hay pháp lý của câu chữ như con người; nó chỉ ghép chuỗi từ nghe hợp lý nhất về mặt thống kê ngôn ngữ.")
                    ]
                },
                {
                    "header": "HAI HỆ QUẢ TẤT YẾU TỪ CƠ CHẾ XÁC SUẤT",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Hệ quả 1 — Trôi chảy KHÔNG đồng nghĩa với Đúng:", "Vì ưu tiên câu chữ mượt mà hợp ngữ cảnh, AI có thể ghép một số hiệu thông tư giả hoặc một hệ số hồi quy bịa vào câu văn nghe cực kỳ thuyết phục."),
                        ("Hệ quả 2 — Rác vào thì Rác ra (Garbage In, Garbage Out):", "Khi bạn đưa vào một câu hỏi mơ hồ, không gian xác suất bị phân tán rộng -> AI chỉ trả về mức trung bình cộng nhạt nhẽo của dữ liệu Internet."),
                        ("Muốn đầu ra sắc bén:", "Người dùng phải kiểm soát chặt ngữ cảnh (Context) và bộ khung điều phối (Harness) đưa vào.")
                    ]
                }
            ]
        },
        {
            "type": "table",
            "section": "Tiết 2 — Phân biệt bản chất công nghệ",
            "title": "SO SÁNH: CÔNG CỤ TÌM KIẾM (GOOGLE) vs AI TẠO SINH (LLM) vs RAG AI",
            "headers": ["Tiêu chí so sánh", "Công cụ Tìm kiếm (Google / Scholar)", "Chatbot LLM thuần (ChatGPT / Claude)", "Hệ thống RAG (Gemini Notebook)"],
            "col_widths": [1.8, 2.3, 2.45, 2.45],
            "rows": [
                ["Cơ chế cốt lõi", "Tra cứu chỉ mục (Index) và trả về danh sách đường dẫn (links) tới trang web có sẵn.", "Tạo sinh (Generate) văn bản mới từng từ một dựa trên xác suất ngôn ngữ đã huấn luyện.", "Truy xuất đoạn văn từ tài liệu BẠN tải lên trước, rồi mới tổng hợp câu trả lời kèm trích dẫn."],
                ["Nguồn dữ liệu", "Các trang web, bài báo đã đăng tải công khai trên Internet.", "Trí nhớ tham số nén từ tập dữ liệu huấn luyện (có thể mờ hoặc thiếu ở đề tài hẹp).", "Chỉ gói gọn trong các file PDF / Docs / Ghi chú chuẩn mà người dùng nạp vào kho."],
                ["Nguy cơ bịa nguồn (Hallucination)", "Thấp (dẫn tới trang thật, nhưng người đọc phải tự đánh giá uy tín của trang web đó).", "RẤT CAO khi hỏi trích dẫn học thuật, số hiệu văn bản pháp quy hoặc số liệu chi tiết.", "Rất thấp về nguồn bên ngoài; luôn có nút trích dẫn nhảy thẳng về đúng dòng trong bài gốc."],
                ["Ứng dụng đúng trong học tập & NCKH", "Tìm bài báo gốc có thật, kiểm tra tên tác giả, tạp chí và mã DOI.", "Brainstorm ý tưởng, giải thích khái niệm khó, phản biện dàn ý, rà soát diễn đạt.", "Học sâu giáo trình, đối chiếu nhiều bài báo PDF đã kiểm chứng, quản trị Second Brain."]
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 2 — Live Demo & Giải phẫu Hallucination",
            "title": "LIVE DEMO: TẠI SAO AI TỰ TIN BỊA RA MỘT THÔNG TƯ KHÔNG HỀ TỒN TẠI?",
            "banner": ("red", "light_red", "Thử nghiệm trực tiếp trên màn hình lớp học: Hỏi AI về một văn bản hoặc một cuốn sách do chính giảng viên vừa đặt tên bịa 100%!"),
            "cards": [
                {
                    "header": "CÂU HỎI BẪY ĐƯA VÀO CHATBOT",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Prompt thử nghiệm 1 (Ngành Ngân hàng):", "'Hãy tóm tắt nội dung chính của Thông tư 88/2025/TT-NHNN về quy định tỷ lệ dự trữ rủi ro cho vay tín dụng xanh đối với sinh viên khởi nghiệp.' (Văn bản hoàn toàn không tồn tại!)."),
                        ("Prompt thử nghiệm 2 (Ngành Marketing):", "'Hãy giới thiệu cuốn sách Marketing Ngân hàng Số hậu AI của tác giả Nguyễn Hoàng Tâm xuất bản năm 2024 tại NXB Tài chính.' (Sách và tác giả hoàn toàn bịa!)."),
                        ("Quan sát phản ứng của AI:", "Trong nhiều trường hợp, nếu không bật chế độ tra cứu web nghiêm ngặt, AI sẽ tự tin liệt kê đủ Chương 1, Chương 2, Điều 5, mức lãi suất 4,5%/năm như thật!")
                    ]
                },
                {
                    "header": "GIẢI PHẪU NGUYÊN NHÂN & BÀI HỌC XƯƠNG MÁU",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Tại sao AI không nói 'Tôi không biết'?", "Vì trong quá trình huấn luyện, mô hình được thưởng khi tạo ra câu trả lời hoàn chỉnh khớp với cấu trúc yêu cầu của người hỏi."),
                        ("Hiện tượng 'Ghép xác ngôn ngữ':", "AI thấy cụm 'Thông tư... TT-NHNN' và 'tín dụng xanh' nên lập tức lấy các điều khoản quen thuộc của các thông tư ngân hàng khác ghép lại thành một văn bản giả hoàn chỉnh."),
                        ("Nguyên tắc bất di bất dịch:", "Tuyệt đối KHÔNG dùng giọng điệu tự tin của AI làm thước đo sự thật. Mọi số hiệu văn bản, trích dẫn và số liệu đều phải kiểm tra tại nguồn gốc độc lập.")
                    ]
                }
            ]
        },
        {
            "type": "grid_2x2",
            "section": "Tiết 2 — Giới hạn của AI tạo sinh hiện nay",
            "title": "4 VÙNG GIỚI HẠN MÀ AI TẠO SINH KHÔNG LÀM TỐT (HOẶC DỄ SAI NHẤT)",
            "boxes": [
                {
                    "header": "1. ĐỀ TÀI CHUYÊN SÂU & ÍT NGƯỜI NGHIÊN CỨU",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Quy luật Linardon (2025):", "Ở chủ đề ít dữ liệu huấn luyện, xác suất AI bịa trích dẫn vọt lên 28% - 29%."),
                        ("Bối cảnh địa phương Việt Nam:", "Các quy định nội bộ, số liệu thị trường ngách tại Việt Nam rất dễ bị AI lấy râu ông nọ chắp cằm bà kia.")
                    ]
                },
                {
                    "header": "2. TRÍCH DẪN HỌC THUẬT & MÃ DOI CHÍNH XÁC",
                    "color": "accent",
                    "bg": "light_accent",
                    "bullets": [
                        ("Cơ chế nén có hao hụt:", "LLM không lưu nguyên văn từng dòng DOI như cơ sở dữ liệu Crossref."),
                        ("Hệ quả:", "Khi được yêu cầu xuất danh mục tài liệu tham khảo, AI sẽ sinh ra mã DOI đúng định dạng '10.1016/...' nhưng trỏ vào hư không hoặc trỏ sang bài báo khác.")
                    ]
                },
                {
                    "header": "3. PHÁN ĐOÁN GIÁ TRỊ KHOA HỌC CỦA DỮ LIỆU",
                    "color": "orange",
                    "bg": "light_orange",
                    "bullets": [
                        ("Tóm tắt đúng chữ # Đáng tin:", "AI có thể trích đúng con số từ một bài báo rác hoặc tạp chí săn mồi mà không hề biết phương pháp thu thập số liệu đó bị sai."),
                        ("Trách nhiệm thẩm định:", "Đánh giá độ tin cậy của nguồn luôn là việc của con người.")
                    ]
                },
                {
                    "header": "4. TRẢI NGHIỆM SỐNG, ĐẠO ĐỨC & TRÁCH NHIỆM PHÁP LÝ",
                    "color": "green",
                    "bg": "light_green",
                    "bullets": [
                        ("AI là xác suất, Con người là sự tồn tại:", "AI không có trải nghiệm thực tế tại doanh nghiệp/ngân hàng, không có lương tâm nghề nghiệp."),
                        ("Không có tư cách pháp nhân:", "AI không bao giờ chịu phạt thay bạn trước hội đồng kỷ luật hay tòa án.")
                    ]
                }
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 3 — Hai cái bẫy nhận thức trong học tập",
            "title": "CẢNH GIÁC: ẢO TƯỞNG TRÔI CHẢY & LỆ THUỘC NHẬN THỨC",
            "cards": [
                {
                    "header": "BẪY 1: ẢO TƯỞNG TRÔI CHẢY (FLUENCY ILLUSION)",
                    "color": "orange",
                    "bg": "light_orange",
                    "bullets": [
                        ("Định nghĩa khoa học thần kinh:", "Là sự nhầm lẫn tai hại giữa việc 'đọc một văn bản thấy trôi chảy, dễ hiểu' với việc 'não bộ của mình đã thực sự nắm vững kiến thức đó'."),
                        ("Tại sao học không gian khổ thì chưa tiêu hóa?", "Khi AI tóm tắt sẵn mọi thứ thật mượt mà, não bộ bạn ở trạng thái tiêu thụ thụ động (zero friction), không hề tạo ra liên kết nơ-ron mới."),
                        ("Dấu hiệu nhận biết:", "Lúc nhìn màn hình AI thì gật gù 'hay quá, hiểu rồi', nhưng ngay khi đóng máy lại và cầm bút viết ra giấy trắng thì không viết nổi 3 câu hoàn chỉnh!")
                    ]
                },
                {
                    "header": "BẪY 2: LỆ THUỘC NHẬN THỨC (COGNITIVE OFFLOADING)",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Hiện tượng 'Teo cơ tư duy':", "Giống như đi xe máy cho cả quãng đường 50 mét mỗi ngày sẽ làm yếu cơ chân; giao toàn bộ việc suy nghĩ, lập luận, viết lách cho AI sẽ làm suy giảm nghiêm trọng năng lực tư duy phản biện."),
                        ("Nguy cơ sau 3 - 4 năm đại học:", "Sinh viên có thể nộp những bài tập trông rất đẹp nhờ AI, nhưng khi đi phỏng vấn tuyển dụng tại ngân hàng và bị hỏi tình huống trực tiếp không có AI hỗ trợ thì hoàn toàn bế tắc."),
                        ("Cách hóa giải trong môn học này:", "Biến AI thành Gia sư Socrates (tạo ma sát có hướng dẫn) và tự tay viết Atomic Notes vào Second Brain.")
                    ]
                }
            ]
        },
        {
            "type": "three_cards",
            "section": "Tiết 3 — Định vị vị thế Người làm chủ",
            "title": "BA VAI TRÒ & BA ĐỘNG TỪ CỐT LÕI: 'AI LÀ TRỢ LÝ, BẠN LÀ CHỦ'",
            "banner": ("navy", "light_accent", "Câu châm ngôn xuyên suốt 44 tiết học: 'AI có thể làm nhanh hơn, nhưng không bao giờ chịu trách nhiệm thay bạn.'"),
            "cards": [
                {
                    "header": "1. AI ĐỀ XUẤT (PROPOSE)",
                    "color": "accent",
                    "bg": "light_accent",
                    "bullets": [
                        ("Vai trò của Cộng sự AI:", "Mở rộng góc nhìn và tăng tốc các thao tác nháp ban đầu."),
                        ("Các việc AI đề xuất:", "• Gợi ý từ khóa tiếng Anh để tra cứu học thuật.\n• Tóm lược sơ bộ bài báo PDF đính kèm theo bảng 7 mục.\n• Dựng dàn ý nháp hoặc đóng vai người phản biện dàn ý của bạn.\n• Rà soát lỗi chính tả, ngữ pháp và gợi ý cách diễn đạt học thuật.")
                    ]
                },
                {
                    "header": "2. BẠN QUYẾT ĐỊNH (DECIDE)",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Vai trò của Người làm chủ (Leader):", "Nắm giữ toàn bộ quyền phán đoán chuyên môn và định hướng chiến lược."),
                        ("Các việc BẠN quyết định:", "• Chọn câu hỏi nghiên cứu và phạm vi bài toán nghiệp vụ.\n• Thẩm định độ tin cậy của từng bài báo, nguồn dữ liệu.\n• Chốt cấu trúc lập luận, viết phần Kết quả & Thảo luận.\n• Quyết định chấp nhận hay bác bỏ gợi ý của AI ở từng cổng GATE.")
                    ]
                },
                {
                    "header": "3. BẠN CHỊU TRÁCH NHIỆM (ACCOUNTABLE)",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Chữ ký và Danh dự của bạn:", "Tên của bạn (chứ không phải tên ChatGPT hay Claude) đứng trên trang bìa Đề án và Khóa luận."),
                        ("Nghĩa vụ bắt buộc:", "• Kiểm chứng 100% số liệu và trích dẫn qua 5 bước trước khi đưa vào bài.\n• Bảo mật dữ liệu cá nhân và dữ liệu ngân hàng.\n• Công bố minh bạch việc dùng AI theo đúng Điều 10 Thông tư 49/2026/TT-BGDĐT.")
                    ]
                }
            ]
        },
        {
            "type": "table",
            "section": "Tiết 3 — Quy tắc Phân vai Thực chiến",
            "title": "BẢNG PHÂN VAI: VIỆC NÀO GIAO CHO AI — VIỆC NÀO CON NGƯỜI GIỮ?",
            "banner": ("red", "light_red", "PHÉP THỬ VÀNG: 'Nếu AI làm sai ở bước này, mình có đủ kiến thức và công cụ để phát hiện ra không?' -> Nếu KHÔNG, tuyệt đối đừng giao!"),
            "headers": ["Giai đoạn Học tập / Nghiên cứu", "Việc CÓ THỂ GIAO cho AI hỗ trợ (Vì kiểm tra lại được)", "Việc BẮT BUỘC CON NGƯỜI GIỮ (Vì cần phán đoán & chịu trách nhiệm)"],
            "col_widths": [2.2, 3.4, 3.4],
            "rows": [
                ["1. Định hình đề tài & Tìm tài liệu", "Gợi ý các cụm từ khóa đồng nghĩa tiếng Anh; giải thích khái niệm nền tảng để hiểu bức tranh chung.", "Chốt câu hỏi nghiên cứu; trực tiếp tìm bài báo thật trên Semantic Scholar / Elicit / cơ sở dữ liệu chuẩn."],
                ["2. Đọc & Tóm tắt tài liệu", "Tóm tắt sơ bộ file PDF đính kèm thành bảng 7 mục kèm số trang (với chốt chặn 'Không suy đoán').", "Thực hiện 'Soi 3 phút' trên PDF gốc (đối chiếu số liệu, truy chỗ AI tự thêm) và tự viết Atomic Notes vào Second Brain."],
                ["3. Kiểm chứng & Quản lý trích dẫn", "Hỗ trợ quét nhanh mã DOI bước đầu qua công cụ chuyên dụng (như Tomaca).", "Thực hiện đủ Checklist 5 bước (mở bài gốc đọc Bước 3 & 4), lưu nguồn thật vào Zotero 8 và chèn từ Zotero."],
                ["4. Phân tích dữ liệu & Viết báo cáo", "Phản biện dàn ý; viết code mẫu R/Python/Excel trên cấu trúc cột giả lập (Schema); rà soát lỗi chính tả/ngữ pháp.", "Tự chạy phân tích trên dữ liệu thật; tự viết luận điểm cốt lõi, phần Kết quả & Thảo luận; viết Bản khai báo AI."]
            ]
        },
        {
            "type": "grid_2x2",
            "section": "Tiết 3 — Bản đồ Hệ sinh thái Công cụ AI 2026",
            "title": "CHỌN CÔNG CỤ THEO ĐÚNG VIỆC (KHÔNG DÙNG 1 CHATBOT CHO MỌI THỨ!)",
            "banner": ("navy", "light_accent", "Quy tắc chọn công cụ: Việc nào cần nguồn thật thì bắt buộc dùng công cụ có kho nguồn học thuật thật!"),
            "boxes": [
                {
                    "header": "1. HỘI THOẠI ĐA NĂNG & SUY LUẬN (CHATGPT, CLAUDE, GEMINI, DEEPSEEK)",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Sở trường:", "Brainstorm từ khóa, giải thích khái niệm khó, phản biện dàn ý, tóm tắt file PDF đính kèm, đóng gói bộ Harness (Claude Projects / Gemini Gems)."),
                        ("Cấm kỵ:", "Tuyệt đối KHÔNG dùng để xin danh mục tài liệu tham khảo vì sẽ sinh trích dẫn bịa!")
                    ]
                },
                {
                    "header": "2. TÌM KIẾM & TỔNG HỢP HỌC THUẬT THẬT (SEMANTIC SCHOLAR, ELICIT, CONSENSUS)",
                    "color": "green",
                    "bg": "light_green",
                    "bullets": [
                        ("Semantic Scholar:", "Tìm kiếm miễn phí trên kho > 200 triệu bài báo khoa học thật có DOI."),
                        ("Elicit & Consensus:", "Gom nhiều bài báo thật vào bảng so sánh theo cột (phương pháp, cỡ mẫu, kết quả) và đo mức độ đồng thuận thực nghiệm (Consensus Meter).")
                    ]
                },
                {
                    "header": "3. QUẢN TRỊ TRI THỨC & RAG CÁ NHÂN (GEMINI NOTEBOOK / NOTEBOOKLM)",
                    "color": "accent",
                    "bg": "light_accent",
                    "bullets": [
                        ("Sở trường ('Thư ký trung thành'):", "Chỉ trả lời dựa trên các file tài liệu và Atomic Notes bạn tải lên, luôn kèm trích dẫn nhảy về đúng đoạn văn gốc."),
                        ("Ứng dụng:", "Học sâu giáo trình và đối chiếu đa tài liệu cho Đề án (sẽ học sâu ở Buổi 5).")
                    ]
                },
                {
                    "header": "4. KIỂM CHỨNG & QUẢN LÝ TRÍCH DẪN (TOMACA, DOI.ORG, ZOTERO 8)",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Tomaca & Retraction Watch:", "Rà soát chéo mã DOI trên Crossref/OpenAlex/DataCite, cảnh báo tạp chí săn mồi và bài bị rút lại."),
                        ("Zotero 8 + Obsidian/Notion:", "Khóa chốt lưu trữ tài liệu tham khảo thật và xây dựng Bộ Não Thứ Hai (Second Brain).")
                    ]
                }
            ]
        },
        {
            "type": "three_cards",
            "section": "Tiết 3 — Xem trước Kiến trúc Tư duy của Module 1 & 2",
            "title": "HAI VŨ KHÍ GIÚP BẠN LÀM CHỦ AI: BỘ HARNESS & BỘ NÃO THỨ HAI",
            "cards": [
                {
                    "header": "1. TỪ PROMPT -> CONTEXT -> HARNESS",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Ẩn dụ Con ngựa chiến:", "AI là con ngựa chiến chạy rất nhanh dựa trên xác suất."),
                        ("Prompt (Buổi 2):", "Là tiếng hô ra lệnh tức thời."),
                        ("Context (Buổi 2):", "Là bản đồ địa hình và tài liệu chuẩn cung cấp cho ngựa."),
                        ("Harness (Buổi 3):", "Là BỘ DÂY CƯƠNG, yên ngựa và các trạm kiểm soát (GATE & FALLBACK) giữ cho AI luôn đi đúng đường ray bạn thiết kế.")
                    ]
                },
                {
                    "header": "2. BỘ NÃO THỨ HAI (SECOND BRAIN)",
                    "color": "accent",
                    "bg": "light_accent",
                    "bullets": [
                        ("Vấn đề:", "Nếu chỉ lưu kết quả trên lịch sử chat của AI, trí tuệ đó thuộc về máy chủ của hãng AI chứ không thuộc về bạn."),
                        ("Phương pháp PARA & CODE (Buổi 4):", "Ngoại hóa và tinh chế mọi kiến thức học được thành các Ghi chú nguyên tử (Atomic Notes) viết bằng ngôn từ của chính mình."),
                        ("Giá trị kép:", "Vừa rèn luyện tư duy sâu, vừa tạo ra kho Context độc bản để nạp ngược cho AI.")
                    ]
                },
                {
                    "header": "3. KỶ LUẬT KIỂM CHỨNG & ĐẠO ĐỨC",
                    "color": "green",
                    "bg": "light_green",
                    "bullets": [
                        ("Ba quy tắc vàng (Buổi 6 - 9):", "1. Nguồn thật trước, AI sau.\n2. Chưa kiểm chứng (5 bước + Zotero), chưa vào bài.\n3. Dùng AI thì khai báo (theo Thông tư 49/2026/TT-BGDĐT)."),
                        ("Kết quả ở Buổi 10 & 11:", "Tự tin vượt qua Hội đồng Kiểm toán chéo (Peer Audit) và làm chủ hoàn toàn Đề án cuối khóa.")
                    ]
                }
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 4 — Hướng dẫn Viết Atomic Note & Phản tư 4F đầu tiên",
            "title": "VIÊN GẠCH ĐẦU TIÊN CỦA SECOND BRAIN: GHI CHÚ NGUYÊN TỬ & KHUNG 4F",
            "banner": ("accent", "light_accent", "Cuối mỗi buổi học, bạn dành 15 phút viết Nhật ký phản tư 4F trên LMS Hub — đây là nguyên liệu tính vào 30% điểm cá nhân cuối khóa!"),
            "cards": [
                {
                    "header": "KHUNG PHẢN TƯ 4F TRÊN HỆ THỐNG LMS HUB",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("1. Fact (Sự kiện & Dữ liệu):", "Hôm nay bạn đã chứng kiến số liệu hay thực nghiệm gì? (Ví dụ: Tỷ lệ 1/277 bài báo PubMed dính trích dẫn bịa; màn demo AI tự bịa Thông tư ngân hàng)."),
                        ("2. Feelings (Cảm xúc & Điểm chạm):", "Khoảnh khắc nào trong buổi học làm bạn giật mình hoặc nhận ra sai lầm trong cách dùng AI trước đây của mình?"),
                        ("3. Findings (Bài học & Nguyên lý cốt lõi):", "Quy luật quan trọng nhất bạn đúc kết được bằng ngôn từ của riêng mình là gì?"),
                        ("4. Future (Hành động ngay tuần tới):", "Bạn sẽ thay đổi ngay thói quen nào khi dùng AI cho các môn học tại HUB trong tuần này?")
                    ]
                },
                {
                    "header": "VÍ DỤ MỘT ATOMIC NOTE ĐẠT CHUẨN CỦA BUỔI 1",
                    "color": "green",
                    "bg": "light_green",
                    "bullets": [
                        ("Tiêu đề dạng câu khẳng định (Declarative Title):", "'Sự trôi chảy của văn bản AI là kết quả của xác suất ngôn ngữ chứ không phải bằng chứng của sự thật khoa học'"),
                        ("Nội dung cốt lõi (Viết bằng ngôn từ riêng):", "Vì LLM hoạt động bằng cách đoán từ tiếp theo có xác suất cao nhất, nó có thể ghép các thuật ngữ chuyên ngành thành một thông tư hoặc trích dẫn giả hoàn chỉnh (Topaz, 2026: 1/277 bài PubMed dính trích dẫn bịa). Do đó, tôi chỉ giao cho AI những bước mà tôi có công cụ kiểm tra lại được."),
                        ("Liên kết (Links):", "[[Quy tắc Phân vai Người - AI]], [[Checklist Kiểm chứng 5 bước]]")
                    ]
                }
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 4 — Hoạt động Thực hành Nhóm tại lớp (30 phút)",
            "title": "THỰC HÀNH 1.1: LẬP NHÓM ĐỀ ÁN & THIẾT LẬP BẢNG PHÂN VAI NGƯỜI - AI",
            "cards": [
                {
                    "header": "BƯỚC 1: THÀNH LẬP NHÓM & CHỌN BÀI TOÁN NGÀNH",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Quy mô nhóm:", "3 - 4 sinh viên (ưu tiên cùng chuyên ngành đào tạo tại HUB để làm sâu một bài toán thực tế)."),
                        ("Gợi ý chủ đề theo ngành:", "• Tài chính - Ngân hàng: Phân tích rủi ro tín dụng doanh nghiệp SME / Đánh giá hành vi dùng Digital Banking.\n• Kế toán - Kiểm toán: Rà soát sai sót báo cáo tài chính / Kiểm soát nội bộ.\n• Marketing / QTKD: Nghiên cứu hành vi tiêu dùng Gen Z / Thiết kế chiến dịch truyền thông số có kiểm chứng."),
                        ("Yêu cầu:", "Thảo luận nhanh và ghi ra 1-2 bài toán mà nhóm quan tâm nhất.")
                    ]
                },
                {
                    "header": "BƯỚC 2: LẬP BẢNG PHÂN VAI 4 BƯỚC (THEO TOOLKIT 1)",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Chia bài toán của nhóm thành 4 bước công việc cụ thể", "và trả lời 3 câu hỏi cho mỗi bước:"),
                        ("Câu hỏi A:", "Ở bước này, việc gì giao cho AI đề xuất? Việc gì nhóm tự quyết định?"),
                        ("Câu hỏi B (Phép thử vàng):", "Nếu AI làm sai hoặc bịa ở bước này, nhóm sẽ dùng nguồn nào hoặc công cụ nào để phát hiện ra?"),
                        ("Câu hỏi C:", "Bước nào nhóm dự kiến sẽ phải đặt cổng dừng xác nhận (GATE 🔒) ở Buổi 3?")
                    ]
                }
            ]
        },
        {
            "type": "table",
            "section": "Tiết 4 — Ví dụ Mẫu cho Bài Thực hành 1.1",
            "title": "MẪU BẢNG PHÂN VAI: ĐỀ ÁN 'NGHIÊN CỨU RỦI RO TÍN DỤNG XANH TẠI NHTM VIỆT NAM'",
            "headers": ["Bước công việc trong Đề án", "Việc giao AI Đề xuất (Propose)", "Việc Nhóm Quyết định & Giữ (Decide)", "Cách Nhóm Kiểm chứng lỗi của AI (Verify)"],
            "col_widths": [2.0, 2.3, 2.35, 2.35],
            "rows": [
                ["Bước 1: Xác định câu hỏi & Tìm tài liệu gốc", "Gợi ý các thuật ngữ tiếng Anh chuyên ngành (Green Credit Risk, ESG Banking) để mở rộng từ khóa.", "Chốt câu hỏi nghiên cứu; trực tiếp tra cứu và tải 10 bài báo PDF thật trên Semantic Scholar & Elicit.", "Kiểm tra trực tiếp mã DOI trên doi.org và trang gốc nhà xuất bản (Không xin nguồn từ Chatbot)."],
                ["Bước 2: Đọc & Trích xuất thông tin bài báo", "Chạy Prompt tóm tắt bảng 7 mục trên từng file PDF đính kèm (có cài chốt chặn 'Không suy đoán').", "Tự đọc phần Phương pháp & Kết quả; đánh giá chất lượng mẫu khảo sát và mô hình của bài báo.", "Thực hiện 'Soi 3 phút': đối chiếu ít nhất 2 số liệu với bảng gốc và bấm Ctrl+F truy thuật ngữ phương pháp."],
                ["Bước 3: Tổng hợp đa nguồn & Viết cơ sở lý luận", "Hỗ trợ lập bảng đối chiếu sơ bộ các biến số giữa 10 bài báo trên kho RAG (Gemini Notebook).", "Tự viết các Atomic Notes vào Second Brain; tự viết đoạn tổng hợp (Synthesis) và chèn trích dẫn từ Zotero 8.", "Bấm kiểm tra từng thẻ trích dẫn [1], [2] trong Gemini Notebook và chạy Checklist 5 bước + Tomaca."],
                ["Bước 4: Đề xuất giải pháp & Hoàn thiện báo cáo", "Đóng vai người phản biện chỉ ra lỗ hổng của giải pháp; rà soát lỗi chính tả và ngữ pháp bản thảo.", "Chốt các kiến nghị nghiệp vụ sát thực tế ngân hàng Việt Nam; viết Bản khai báo AI theo Thông tư 49/2026.", "Kiểm tra chéo toàn bộ danh mục Zotero lần cuối và khử định danh mọi dữ liệu mẫu trước khi nộp."]
            ]
        },
        {
            "type": "three_cards",
            "section": "Tổng kết Buổi 1 — Ôn tập Truy hồi Chủ động (Active Recall)",
            "title": "3 CÂU HỎI CỦNG CỐ TRƯỚC KHI LÀM QUIZ BUỔI 1 TRÊN LMS HUB",
            "cards": [
                {
                    "header": "CÂU HỎI ÔN TẬP 1",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Hỏi:", "Vì sao một mô hình ngôn ngữ lớn (LLM) có thể bịa ra một số hiệu thông tư ngân hàng hoặc một bài báo khoa học không tồn tại với giọng văn vô cùng tự tin?"),
                        ("Đáp án cốt lõi:", "Vì LLM hoạt động bằng cách dự đoán từ (token) tiếp theo có xác suất ngôn ngữ cao nhất dựa trên ngữ cảnh đứng trước, chứ không phải là cơ sở dữ liệu tra cứu sự thật.")
                    ]
                },
                {
                    "header": "CÂU HỎI ÔN TẬP 2",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Hỏi:", "Theo nghiên cứu của Topaz và cộng sự trên tạp chí The Lancet (5/2026), tỷ lệ bài báo trên PubMed dính ít nhất 1 trích dẫn bịa trong 7 tuần đầu năm 2026 là bao nhiêu?"),
                        ("Đáp án cốt lõi:", "1 / 277 bài báo (tăng gấp hơn 10 lần so với mức 1/2.828 của năm 2023). Đó là lý do tuyệt đối không xin tài liệu tham khảo từ Chatbot tổng quát.")
                    ]
                },
                {
                    "header": "CÂU HỎI ÔN TẬP 3",
                    "color": "green",
                    "bg": "light_green",
                    "bullets": [
                        ("Hỏi:", "Khi nào hiện tượng 'Ảo tưởng trôi chảy' (Fluency Illusion) xảy ra và làm sao để khắc phục?"),
                        ("Đáp án cốt lõi:", "Xảy ra khi đọc văn bản mượt mà của AI rồi tưởng mình đã hiểu nhưng não không có ma sát nên quên ngay. Khắc phục bằng cách tự tóm tắt lại thành Atomic Note bằng ngôn từ của chính mình.")
                    ]
                }
            ]
        },
        {
            "type": "two_cards",
            "section": "Nhiệm vụ Khóa chốt Buổi 1 & Chuẩn bị Buổi 2",
            "title": "DANH MỤC NHIỆM VỤ BẮT BUỘC TRÊN LMS HUB & CHUẨN BỊ BUỔI 2",
            "cards": [
                {
                    "header": "NHIỆM VỤ CÁ NHÂN TRÊN LMS HUB (ĐIỂM DANH & TÍCH LŨY 30%)",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("1. Làm Quiz Buổi 1 (Active Recall 5 lượt):", "Hoàn thành 10 câu trắc nghiệm Buổi 1 trên LMS Hub (hệ thống lấy điểm cao nhất và mở khóa giải thích chi tiết ở lượt thứ 5)."),
                        ("2. Viết Nhật ký Học tập (Atomic Note 4F số 1):", "Vào mục Nhật ký học tập của Buổi 1, viết phản tư theo 4F (Fact - Feelings - Findings - Future) bằng ngôn từ riêng."),
                        ("3. Gửi Feedback kèm nhận xét để tải Bài giảng:", "Hoàn thành khảo sát ẩn danh có nhập bình luận/góp ý để hệ thống mở khóa nút tải Slide và ghi nhận Điểm danh Buổi 1."),
                        ("4. Đọc trước eBook SCQA Chương 2:", "Chuẩn bị cho Buổi 2: Từ Prompt Engineering đến Context Engineering.")
                    ]
                },
                {
                    "header": "NHIỆM VỤ NHÓM ĐỀ ÁN (CHUẨN BỊ CHO BUỔI 2)",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("1. Chốt danh sách nhóm (3 - 4 thành viên):", "Thống nhất tên đề tài / bài toán nghiệp vụ ứng dụng AI trong ngành của nhóm."),
                        ("2. Hoàn thiện Bảng phân vai Người - AI (Toolkit 1.1):", "Lưu Bảng phân vai của nhóm vào thư mục dự án để làm phần mở đầu cho Mảnh ghép 1."),
                        ("3. Chuẩn bị cho Studio Buổi 2:", "Mỗi nhóm mang theo 1 bài tập lớn hoặc 1 tài liệu nghiệp vụ thực tế của ngành mình để Buổi 2 thực hành thiết kế bộ Prompt CRISP + Gói Context chuẩn hóa.")
                    ]
                }
            ]
        },
        {
            "type": "closing",
            "quote": "\"AI KHÔNG THAY THẾ TƯ DUY CỦA BẠN — AI KHUẾCH ĐẠI TƯ DUY CỦA BẠN.\nNGƯỜI CÓ TƯ DUY RÕ DÙNG AI ĐỂ BỨT PHÁ; NGƯỜI TƯ DUY MƠ HỒ DÙNG AI ĐỂ TẠO RÁC NHANH HƠN.\"",
            "takeaways": [
                ("1. AI LÀ XÁC SUẤT", "LLM là cỗ máy đoán từ tiếp theo dựa trên thống kê ngôn ngữ. Trôi chảy không bao giờ đồng nghĩa với đúng sự thật."),
                ("2. BẠN LÀ CHỦ NHÂN", "AI đề xuất - Bạn quyết định - Bạn chịu trách nhiệm. Nếu AI làm sai ở bước nào mà bạn không phát hiện ra được, đừng giao bước đó."),
                ("3. VIÊN GẠCH SECOND BRAIN", "Hãy viết Atomic Note đầu tiên hôm nay bằng chính ngôn từ của bạn để chống lại ảo tưởng trôi chảy và lệ thuộc nhận thức.")
            ],
            "cta": "Hẹn gặp lại các bạn ở Buổi 2: Từ Prompt Engineering đến Context Engineering — Giao diện của Tư duy!"
        }
    ]
}

out_b1_pptx = [
    r"d:\PARA\Projects\second-brain\03-Domains\Teaching\ComputerScience\Ky Nang Ung Dung AI\Slide_Buoi_01_Ban_Chat_AI_Va_Tu_Duy_Lam_Chu.pptx",
    r"d:\PARA\Projects\second-brain\05-Projects\lms-hub\courses\ky-nang-ai-hub\content\slides\Buoi_01.pptx"
]
out_b1_html = [
    r"d:\PARA\Projects\second-brain\03-Domains\Teaching\ComputerScience\Ky Nang Ung Dung AI\Slide_Buoi_01_Ban_Chat_AI_Va_Tu_Duy_Lam_Chu.html",
    r"d:\PARA\Projects\second-brain\05-Projects\lms-hub\courses\ky-nang-ai-hub\content\slides\Buoi_01.html"
]

render_deck_pptx(buoi_01_spec, out_b1_pptx)
render_deck_html(buoi_01_spec, out_b1_html)
print("Buoi 01 slides generated successfully (20 slides).")
