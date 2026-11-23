# -*- coding: utf-8 -*-
import os
from module1_engine import render_deck_pptx, render_deck_html

# ===========================================================================
# BUỔI 2 (20 SLIDES): TỪ PROMPT ENGINEERING ĐẾN CONTEXT ENGINEERING (GIAO DIỆN CỦA TƯ DUY)
# ===========================================================================
buoi_02_spec = {
    "doc_title": "Buổi 2: Từ Prompt Engineering đến Context Engineering — ĐH Ngân hàng TP.HCM (HUB)",
    "slides": [
        {
            "type": "cover",
            "module_badge": "MODULE 1 (BUỔI 2 / 11) — BẢN CHẤT AI, PROMPT, CONTEXT & HARNESS",
            "title": "BUỔI 2: TỪ PROMPT ĐẾN CONTEXT ENGINEERING\n\"GIAO DIỆN CỦA TƯ DUY\"",
            "subtitle": "Câu hỏi cốt lõi: Cùng một mô hình AI, vì sao 2 người dùng lại nhận về 2 đẳng cấp kết quả khác hẳn nhau?",
            "badges": [
                "THỜI LƯỢNG: 4 TIẾT (200 PHÚT)\nKhung CRISP & 5 Kỹ thuật nâng cao",
                "CHUẨN ĐẦU RA: CLO2\nThiết kế Gói Ngữ cảnh & Chốt chặn chống bịa",
                "CỘT MỐC ĐỀ ÁN CUỐI KHÓA\nChốt đề tài & Viết 3 cụm Prompt + Context"
            ]
        },
        {
            "type": "numbered_list",
            "section": "Buổi 2 — Mục tiêu & Lộ trình 200 phút",
            "title": "MỤC TIÊU HỌC TẬP & LỘ TRÌNH 4 TIẾT CỦA BUỔI 2",
            "items": [
                ("01", "Tiết 1 (50'): Prompt là tấm gương phản chiếu tư duy & Công thức nền tảng CRISP",
                 "Story Spine nhân vật Minh (Kỳ 2); Giải phẫu 5 thành tố C - R - I - S - P; Live Demo đối chứng 'Trước CRISP vs Sau CRISP' trên bài toán ngành Ngân hàng.", "red"),
                ("02", "Tiết 2 (50'): Năm kỹ thuật điều khiển suy luận nâng cao & Chốt chặn 'Không suy đoán'",
                 "Chain-of-Thought (CoT), Role-based / Multi-Persona, Few-shot, Iterative Refinement, Negative Prompt & Câu khóa sống còn chống Hallucination.", "navy"),
                ("03", "Tiết 3 (50'): Bước chuyển từ Prompt sang Context Engineering (Kỹ nghệ Thiết kế Ngữ cảnh)",
                 "Cơ chế Cửa sổ ngữ cảnh (Context Window) & hiện tượng Context Rot; 4 thành phần của một gói Context sạch; Thực hành va chạm '1 Bài toán - 3 Cấp độ'.", "accent"),
                ("04", "Tiết 4 (50'): Studio Đề án (Thiết kế Bộ 3 cụm Prompt & Context) & Khóa chốt LMS",
                 "Chốt tên đề tài Đề án nhóm; Soạn thảo 3 cụm Prompt CRISP + danh mục Context chuẩn bị cho Buổi 3 đóng gói Harness; Viết Nhật ký 4F số 2 & làm Quiz Buổi 2.", "green")
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 1 — Story Spine & Khung SCQA",
            "title": "CÂU CHUYỆN CỦA MINH (KỲ 2): 'SAO AI CỦA BẠN THÔNG MINH HƠN AI CỦA TÔI?'",
            "banner": ("red", "light_red", "Ngộ nhận phổ biến nhất của người mới: Tưởng rằng ai dùng AI giỏi là nhờ sưu tầm được danh sách '100 câu thần chú bí mật' trên mạng!"),
            "cards": [
                {
                    "header": "S & C — NỖI THẤT VỌNG CỦA MINH KHI PHÂN TÍCH NGÂN HÀNG",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Tình huống (Situation):", "Minh được giao phân tích rủi ro khoản vay của một doanh nghiệp SME từ báo cáo tài chính. Minh mở Claude/ChatGPT và gõ: 'Hãy phân tích rủi ro tín dụng cho doanh nghiệp này giúp tôi'."),
                        ("Biến cố (Complication):", "AI trả về 2 trang lý thuyết sách giáo khoa chung chung ('cần xem xét dòng tiền, tài sản đảm bảo...'). Trong khi đó, bạn Lan ngồi cạnh cũng dùng đúng công cụ miễn phí đó nhưng chỉ sau 10 phút đã có một bảng phân tích 5 chỉ số tài chính sắc bén sát thực tế!"),
                        ("Sự khác biệt nằm ở đâu?", "Không nằm ở công cụ AI, mà nằm ở lượng thông tin, cấu trúc yêu cầu và gói ngữ cảnh (Context) mà Lan đã thiết kế trước khi bấm Enter.")
                    ]
                },
                {
                    "header": "Q & A — PROMPT LÀ GIAO DIỆN CỦA TƯ DUY",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Câu hỏi trọng tâm (Question):", "Làm thế nào để chuyển hóa tư duy chuyên môn trong đầu bạn thành một hệ thống chỉ thị và ngữ cảnh giúp AI làm việc đúng chuẩn chuyên gia ngay từ đầu?"),
                        ("Nguyên lý cốt lõi (Answer):", "• AI không đọc được suy nghĩ của bạn. Tư duy mơ hồ -> Prompt mơ hồ -> Output rác.\n• 10 phút đầu tư viết Prompt & chuẩn bị Context trên giấy giúp tiết kiệm 2 giờ ngồi sửa một kết quả lệch hướng.\n• Chuyển từ hỏi tự phát sang công thức CRISP + 5 kỹ thuật nâng cao + Context Engineering.")
                    ]
                }
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 1 — Bản chất Giao tiếp với Mô hình Xác suất",
            "title": "TẠI SAO CÂU LỆNH NGẮN GỌN LẠI DẪN ĐẾN KẾT QUẢ RÁC?",
            "cards": [
                {
                    "header": "KHI BẠN HỎI MƠ HỒ: KHÔNG GIAN XÁC SUẤT BỊ PHÂN TÁN",
                    "color": "orange",
                    "bg": "light_orange",
                    "bullets": [
                        ("Câu lệnh kiểu cũ:", "'Viết giúp tôi một bài về chuyển đổi số ngân hàng.' (9 chữ)."),
                        ("Điều gì diễn ra bên trong LLM?", "Khi không biết bạn là sinh viên hay giám đốc, đối tượng đọc là ai, phạm vi ở Việt Nam hay thế giới, độ dài bao nhiêu, mô hình xác suất buộc phải chọn những câu chữ có tần suất trung bình cao nhất trên Internet."),
                        ("Kết quả:", "Một bài viết vô thưởng vô phạt, đầy những từ ngữ sáo rỗng ('Trong kỷ nguyên số phát triển vũ bão...'), không có số liệu gốc và rất dễ kèm theo trích dẫn bịa.")
                    ]
                },
                {
                    "header": "KHI BẠN CẤU TRÚC HÓA: THU HẸP KHÔNG GIAN XÁC SUẤT",
                    "color": "green",
                    "bg": "light_green",
                    "bullets": [
                        ("Bản chất của Prompt & Context tốt:", "Là việc dựng lên các 'bức tường rào' thu hẹp không gian xác suất của LLM vào đúng vùng kiến thức chuyên môn, đúng định dạng và đúng tài liệu nguồn mà bạn cung cấp."),
                        ("Tư duy như một Giám đốc giao việc cho Trợ lý mới:", "Nếu bạn giao việc cho một nhân viên thực tập mới vào phòng ngày đầu tiên mà chỉ nói 1 câu cụt lủn, nhân viên đó chắc chắn làm sai."),
                        ("Bạn cần giao đủ 5 yếu tố:", "Bối cảnh (Context) - Vai trò (Role) - Đầu vào & Nhiệm vụ (Input/Instruction) - Ràng buộc cụ thể (Specifics) - Tiêu chuẩn đầu ra (Performance/Preview).")
                    ]
                }
            ]
        },
        {
            "type": "table",
            "section": "Tiết 1 — Công thức Nền tảng CRISP",
            "title": "GIẢI PHẪU KHUNG CRISP: 5 THÀNH TỐ CỦA MỘT CHỈ THỊ CHUẨN MỰC",
            "banner": ("navy", "light_accent", "Quy tắc thực hành: Luôn phác thảo đủ 5 chữ C - R - I - S - P trước khi giao bất kỳ tác vụ học thuật hay nghiệp vụ nào cho AI!"),
            "headers": ["Thành tố CRISP", "Câu hỏi cần trả lời", "Ví dụ thực tế (Ngành Tài chính - Ngân hàng tại HUB)"],
            "col_widths": [1.8, 2.5, 4.7],
            "rows": [
                ["C — Context\n(Bối cảnh)", "Bạn là ai? Đang giải quyết bài toán gì? Trong bối cảnh/môi trường nào?", "Tôi là sinh viên năm 3 ngành Tài chính - Ngân hàng tại ĐH Ngân hàng TP.HCM, đang làm báo cáo phân tích rủi ro tín dụng của nhóm doanh nghiệp vừa và nhỏ (SME) ngành xuất khẩu thủy sản tại Việt Nam giai đoạn 2024 - 2026."],
                ["R — Role\n(Vai trò chuyên môn)", "AI cần đóng vai chuyên gia nào, với góc nhìn và tiêu chuẩn khắt khe gì?", "Bạn đóng vai là Chuyên gia Thẩm định Rủi ro Tín dụng cao cấp tại một Ngân hàng Thương mại cổ phần, có phong cách phân tích thận trọng, dựa hoàn toàn trên bằng chứng số liệu."],
                ["I — Input / Instruction\n(Đầu vào & Nhiệm vụ)", "Tài liệu/dữ liệu cụ thể đính kèm là gì và nhiệm vụ chính cần làm là gì?", "Dựa DUY NHẤT vào báo cáo tài chính và thuyết minh PDF tôi đính kèm, hãy phân tích 4 nhóm chỉ số: Thanh khoản, Đòn bẩy tài chính, Khả năng trả lãi và Vòng quay khoản phải thu."],
                ["S — Specifics\n(Ràng buộc cụ thể)", "Định dạng gì? Độ dài bao nhiêu? Văn phong, ngôn ngữ, thuật ngữ thế nào?", "Trình bày dưới dạng bảng 4 cột (Nhóm chỉ số | Công thức & Giá trị | Nhận xét xu hướng | Cảnh báo rủi ro). Độ dài tối đa 350 chữ, giữ thuật ngữ tiếng Anh trong ngoặc đơn."],
                ["P — Performance / Preview\n(Tiêu chí & Chốt chặn)", "Ai đọc? Tiêu chuẩn đạt là gì? Ràng buộc cấm suy diễn nào phải tuân thủ?", "Báo cáo dùng để bảo vệ trước Hội đồng. Mỗi con số bắt buộc ghi rõ lấy từ trang mấy của PDF. Chỗ nào báo cáo không có số liệu, ghi rõ 'Không nêu trong báo cáo', tuyệt đối không tự suy đoán."]
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 1 — Live Demo Đối chứng",
            "title": "ĐỐI CHỨNG TRỰC TIẾP: PROMPT TỰ PHÁT vs PROMPT CHUẨN CRISP",
            "cards": [
                {
                    "header": "CÁCH 1: PROMPT TỰ PHÁT (KIỂU CŨ)",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Câu lệnh gõ vào AI:", "'Viết email xin thầy gia hạn nộp bài tập lớn môn Tài chính doanh nghiệp.'"),
                        ("Đầu ra của AI:", "• Dài dòng, sáo rỗng, dịch từ văn phong phương Tây ('Tôi hy vọng email này tìm thấy thầy trong trạng thái sức khỏe tốt nhất...').\n• Không có mã lớp, không có lý do học thuật thuyết phục, không có ngày cam kết nộp mới cụ thể, không nói rõ đã hoàn thành được bao nhiêu %."),
                        ("Hệ quả:", "Sinh viên phải ngồi xóa đi viết lại gần hết, hoặc nếu copy gửi thẳng sẽ gây phản cảm lớn với giảng viên.")
                    ]
                },
                {
                    "header": "CÁCH 2: PROMPT ĐẦY ĐỦ 5 THÀNH TỐ CRISP",
                    "color": "green",
                    "bg": "light_green",
                    "bullets": [
                        ("Câu lệnh CRISP:", "• [C] Tôi là nhóm trưởng Nhóm 3 lớp TCDN_D01 tại HUB, hạn nộp báo cáo là 20h ngày 25/11. Nhóm đã xong 80% nhưng đang chờ số liệu báo cáo kiểm toán quý 3 của doanh nghiệp mẫu công bố ngày 26/11.\n• [R] Trợ lý soạn thảo văn bản học thuật lịch sự, cầu thị, ngắn gọn.\n• [I] Viết email gửi giảng viên xin gia hạn nộp bài thêm 48 giờ (đến 20h ngày 27/11).\n• [S] Tối đa 130 chữ, đính kèm link bản thảo 80% đã làm được, không dùng lời lẽ than vãn.\n• [P] Gồm: Tiêu đề chuẩn [Mã lớp - Nhóm 3], Lời chào, Lý do & tiến độ hiện tại, Mốc cam kết mới, Lời cảm ơn."),
                        ("Đầu ra của AI:", "Chuyên nghiệp, đúng trọng tâm, dùng được ngay lập tức!")
                    ]
                }
            ]
        },
        {
            "type": "numbered_list",
            "section": "Tiết 2 — Năm Kỹ thuật Điều khiển Suy luận Nâng cao",
            "title": "5 KỸ THUẬT PROMPT NÂNG CAO GIÚP KHAI THÁC SÂU MÔ HÌNH AI",
            "items": [
                ("01", "Chain-of-Thought (CoT — Suy luận từng bước)",
                 "Yêu cầu AI trình bày rõ từng bước lập luận trung gian trước khi đưa ra kết luận cuối cùng (Dùng cho bài toán tính toán tài chính, phân tích logic, chẩn đoán tình huống).", "navy"),
                ("02", "Role-based & Multi-Persona (Đóng vai & Phản biện đa góc nhìn)",
                 "Đặt AI vào vai chuyên gia cụ thể hoặc cho 2-3 chuyên gia có góc nhìn đối lập cùng tranh biện trên 1 phương án của bạn (ví dụ: Giám đốc Kinh doanh vs Giám đốc Quản trị Rủi ro).", "accent"),
                ("03", "Few-shot Prompting (Học qua 2 - 3 ví dụ mẫu chuẩn mực)",
                 "Đưa cho AI xem trước 2-3 ví dụ mẫu đạt chuẩn (về cấu trúc bảng, cách viết Atomic Note, cách trích xuất biến số) để khóa chặt định dạng và giọng văn đầu ra.", "green"),
                ("04", "Iterative Refinement (Tinh chỉnh đa vòng có kiểm soát)",
                 "Không kỳ vọng câu lệnh đầu tiên hoàn hảo 100%; giữ lại phần đã đúng và chỉ yêu cầu sửa đúng 1-2 tiêu chí cụ thể qua từng lượt đối thoại tiếp theo.", "orange"),
                ("05", "Negative Prompt & Chốt chặn 'Không suy đoán' (Chống Hallucination)",
                 "Chỉ định rõ những điều CẤM AI làm và cài câu khóa bắt buộc: 'Mỗi ý ghi rõ số trang/mục. Chỗ nào tài liệu không nói, ghi không nêu trong bài, tuyệt đối không suy đoán'.", "red")
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 2 — Kỹ thuật 1 & 2: Chain-of-Thought & Multi-Persona",
            "title": "ĐIỀU KHIỂN LUỒNG SUY LUẬN LOGIC & PHẢN BIỆN ĐA GÓC NHÌN",
            "cards": [
                {
                    "header": "1. CHAIN-OF-THOUGHT (CoT): BUỘC AI 'NGHĨ TỪNG BƯỚC'",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Tại sao LLM hay tính sai khi trả lời ngay?", "Vì nếu bắt AI xuất kết quả ở dòng đầu tiên, nó chỉ đoán con số có xác suất bề mặt cao nhất mà chưa qua các bước biến đổi trung gian."),
                        ("Cách kích hoạt CoT chuẩn:", "'Trước khi đưa ra kết luận cuối cùng, hãy thực hiện tuần tự 4 bước suy luận sau: (Bước 1) Trích xuất các biến số đầu vào từ đề bài; (Bước 2) Nêu công thức tài chính áp dụng; (Bước 3) Thay số và kiểm tra đơn vị tính; (Bước 4) Đưa ra kết luận và kiểm tra tính hợp lý.'"),
                        ("Giá trị cho người học:", "Giúp bạn nhìn thấy toàn bộ quá trình suy luận của AI để biết chính xác nó đúng hay sai ở bước nào!")
                    ]
                },
                {
                    "header": "2. MULTI-PERSONA: THUÊ 'HỘI ĐỒNG PHẢN BIỆN' CHO ĐỀ ÁN",
                    "color": "accent",
                    "bg": "light_accent",
                    "bullets": [
                        ("Ứng dụng thực chiến cho Đề án nhóm:", "Khi nhóm bạn vừa đề xuất một giải pháp ứng dụng AI cho ngân hàng, đừng hỏi AI 'Giải pháp này có hay không?' (AI sẽ khen bạn!)."),
                        ("Mẫu Prompt Multi-Persona:", "'Đây là đề xuất giải pháp của nhóm tôi: [...]. Hãy đóng vai một hội đồng gồm 3 người cùng phản biện gay gắt đề xuất này:\n1. Giám đốc Rủi ro & Pháp chế Ngân hàng (soi lỗ hổng bảo mật dữ liệu & Thông tư).\n2. Giảng viên Phương pháp NCKH (soi tính khả thi và căn cứ dữ liệu).\n3. Khách hàng cá nhân khó tính (soi trải nghiệm thực tế).'"),
                        ("Kết quả:", "Nhóm phát hiện trước mọi điểm yếu trước ngày bảo vệ!")
                    ]
                }
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 2 — Kỹ thuật 3 & 4: Few-shot & Iterative Refinement",
            "title": "KHÓA CHẶT ĐỊNH DẠNG BẰNG VÍ DỤ MẪU & TINH CHỈNH ĐA VÒNG",
            "cards": [
                {
                    "header": "3. FEW-SHOT PROMPTING: 'TRĂM NGHE KHÔNG BẰNG MỘT THẤY'",
                    "color": "green",
                    "bg": "light_green",
                    "bullets": [
                        ("Nguyên lý:", "Mô tả bằng lời dài 10 dòng về định dạng bạn muốn vẫn không hiệu quả bằng việc đưa thẳng cho AI xem 2 ví dụ mẫu (shots) hoàn chỉnh."),
                        ("Ví dụ áp dụng:", "Khi cần AI chuyển hóa các ghi chú thô thành bảng Ma trận biến số nghiên cứu, hãy dán 2 dòng mẫu bạn đã tự làm chuẩn:\n• Mẫu 1: [Tên biến: Rủi ro bảo mật cảm nhận (PSR)] | [Định nghĩa: ...] | [Nguồn gốc: Featherman & Pavlou (2003), tr.454]\n• Mẫu 2: [Tên biến: ...] | [Định nghĩa: ...] | [Nguồn gốc: ...]\n• Yêu cầu: Hãy trích xuất 3 biến tiếp theo trong bài báo PDF đính kèm theo ĐÚNG cấu trúc của 2 mẫu trên."),
                        ("Lưu ý vàng:", "Ví dụ mẫu phải thật chuẩn và đã khử thông tin nhạy cảm.")
                    ]
                },
                {
                    "header": "4. ITERATIVE REFINEMENT: NGHỆ THUẬT SỬA DẦN QUA NHIỀU LƯỢT",
                    "color": "orange",
                    "bg": "light_orange",
                    "bullets": [
                        ("Sai lầm thường gặp:", "Thấy bản nháp đầu tiên của AI chưa ưng ý là xóa hết gõ lại câu mới, hoặc bắt AI sửa 10 thứ cùng một lúc khiến AI sửa được chỗ này lại làm hỏng chỗ kia."),
                        ("Quy tắc Iterative chuẩn:", "• Lượt 1: Dựng khung cấu trúc và kiểm tra độ chính xác của dữ liệu.\n• Lượt 2: 'Giữ nguyên toàn bộ số liệu ở bảng trên. Hãy bổ sung thêm cột Số trang trích dẫn ở ngoài cùng bên phải.'\n• Lượt 3: 'Giữ nguyên bảng. Hãy rút gọn phần nhận xét bên dưới xuống còn đúng 120 chữ, bỏ các tính từ cảm thán.'"),
                        ("Khi nào nên dừng Iterative?", "Nếu sau 3-4 lượt mà AI vẫn lệch hướng, hãy quay lại sửa thẳng vào Prompt CRISP gốc!")
                    ]
                }
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 2 — Kỹ thuật 5: Negative Prompt & Chốt chặn Chống bịa",
            "title": "CHỐT CHẶN SỐNG CÒN TRONG HỌC THUẬT: 'KHÔNG SUY ĐOÁN'",
            "banner": ("red", "light_red", "Đây là câu lệnh bắt buộc phải có trong mọi Prompt đọc tài liệu và trong mọi Bộ Harness của môn học này!"),
            "cards": [
                {
                    "header": "NEGATIVE PROMPT (NÓI RÕ ĐIỀU CẤM AI LÀM)",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Tại sao phải có Negative Prompt?", "Để chặn trước các thói quen xấu mặc định của LLM (hay viết mở bài sáo rỗng, hay tự ý làm tròn số, hay thêm lời khuyên đạo lý chung chung)."),
                        ("Nguyên tắc viết Negative Prompt:", "Phải định lượng cụ thể thay vì nói chung chung:\n• Kém hiệu quả: 'Đừng viết dài dòng, đừng dùng văn phong quảng cáo.'\n• Hiệu quả cao: 'KHÔNG viết đoạn mở đầu và kết luận xã giao; KHÔNG dùng các từ ngữ cảm thán (tuyệt vời, đột phá, hoàn hảo); KHÔNG vượt quá 200 chữ; KHÔNG tự ý thay đổi thuật ngữ trong ngoặc đơn.'")
                    ]
                },
                {
                    "header": "CHỐT CHẶN CHỐNG HALLUCINATION KHI ĐỌC TÀI LIỆU",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Vấn đề khi yêu cầu AI điền bảng:", "Khi bạn yêu cầu AI tóm tắt bài báo thành bảng 7 mục, nếu bài báo gốc bỏ trống mục 'Hạn chế của nghiên cứu', AI sẽ có xu hướng tự sáng tác ra hạn chế rồi gán như thể tác giả bài báo đã nói!"),
                        ("CÂU KHÓA BẮT BUỘC CHÉP VÀO SỔ TAY:", "\"Mỗi ý trong bảng bắt buộc phải ghi rõ số trang hoặc tên mục trong bài báo gốc. Chỗ nào bài báo không đề cập, bắt buộc ghi rõ 'Không nêu trong bài', tuyệt đối không tự suy đoán hay lấy kiến thức bên ngoài điền vào.\""),
                        ("Kết nối sang Buổi 6:", "Chính câu khóa này đã giúp chúng ta bắt sống lỗi của bài báo Hemani (2026) trong thực nghiệm NCKH!")
                    ]
                }
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 3 — Bước chuyển lên Context Engineering",
            "title": "TỪ PROMPT ENGINEERING ĐẾN CONTEXT ENGINEERING (KỸ NGHỆ NGỮ CẢNH)",
            "banner": ("navy", "light_accent", "Năm 2023-2024 người ta nói về Prompt Engineering (gọt câu chữ). Từ 2025-2026, năng lực quyết định là Context Engineering (thiết kế gói tri thức đầu vào)!"),
            "cards": [
                {
                    "header": "PROMPT ENGINEERING (CÂU LỆNH ĐƠN LẺ)",
                    "color": "accent",
                    "bg": "light_accent",
                    "bullets": [
                        ("Trọng tâm:", "Tập trung vào cách diễn đạt câu hỏi và yêu cầu trong khung chat."),
                        ("Giới hạn:", "Dù câu lệnh của bạn có viết theo chuẩn CRISP hay đến mấy, nhưng nếu bạn bắt AI phân tích quy chế tín dụng của Ngân hàng X hoặc tóm tắt một bài báo mới mà KHÔNG nạp văn bản thật vào cho nó, thì AI vẫn chỉ đoán mò dựa trên trí nhớ xác suất cũ."),
                        ("Ví von:", "Giống như thuê một đầu bếp giỏi (Prompt hay) nhưng đưa vào một gian bếp trống rỗng không có nguyên liệu tươi (Thiếu Context).")
                    ]
                },
                {
                    "header": "CONTEXT ENGINEERING (THIẾT KẾ GÓI NGỮ CẢNH)",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Định nghĩa:", "Là nghệ thuật và kỹ thuật tuyển chọn, làm sạch, cấu trúc hóa toàn bộ gói thông tin, tài liệu nguồn, dữ liệu mẫu và quy tắc biên để nạp vào Cửa sổ ngữ cảnh (Context Window) của AI trước khi nó suy luận."),
                        ("Câu hỏi cốt lõi của Context Engineer:", "'Để giải quyết chính xác bài toán này mà không phải đoán mò một chi tiết nào, AI cần được nhìn thấy những tài liệu, bảng biểu và quy chuẩn nào ngay trước mắt nó?'"),
                        ("Vai trò của Second Brain (Module 2):", "Chính kho Atomic Notes của bạn sẽ là nguồn nguyên liệu Context đắt giá nhất!")
                    ]
                }
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 3 — Cơ chế Cửa sổ Ngữ cảnh (Context Window)",
            "title": "CỬA SỔ NGỮ CẢNH (CONTEXT WINDOW) & HIỆN TƯỢNG 'LOÃNG NGỮ CẢNH' (CONTEXT ROT)",
            "cards": [
                {
                    "header": "CỬA SỔ NGỮ CẢNH TRƯỢT (SLIDING CONTEXT WINDOW)",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Context Window là gì?", "Là 'bộ nhớ làm việc ngắn hạn' (RAM) của AI trong một phiên trò chuyện, được đo bằng số lượng Token (1.000 tokens tiếng Việt tương đương khoảng 400 - 500 chữ)."),
                        ("Cơ chế cửa sổ trượt:", "• Lúc mới mở phiên chat: Toàn bộ chỉ thị và tài liệu bạn đưa đều nằm gọn trong tầm mắt của AI.\n• Khi cuộc trò chuyện kéo dài hàng chục lượt: Nội dung mới liên tục đẩy nội dung cũ về phía sau."),
                        ("Hai hệ quả tất yếu:", "(1) AI dần quên mất các ràng buộc quan trọng bạn dặn ở đầu buổi; (2) Cùng một yêu cầu nhưng chạy ở đầu phiên chat và cuối phiên chat dài cho ra kết quả không nhất quán.")
                    ]
                },
                {
                    "header": "HIỆN TƯỢNG 'CONTEXT ROT' (THỐI RỮA / LOÃNG NGỮ CẢNH)",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Nhiều hơn KHÔNG phải lúc nào cũng tốt hơn:", "Dù các mô hình năm 2026 có Context Window lớn (200K - 1M tokens), nghiên cứu chỉ ra rằng nếu bạn quăng vào đó hàng trăm trang tài liệu rác, lộn xộn hoặc không liên quan, sự chú ý của AI sẽ bị phân tán (Lost in the Middle)."),
                        ("3 Quy tắc Vệ sinh Ngữ cảnh (Context Hygiene):", "1. Chỉ nạp tài liệu thật sự liên quan và đã kiểm chứng.\n2. Ưu tiên nạp các bản tinh chế (Atomic Notes, bảng trích xuất sạch) thay vì văn bản rác.\n3. Khi chuyển sang một nhiệm vụ hoặc một bài báo mới, hãy mở phiên chat mới (hoặc đóng gói vào Project/Harness ở Buổi 3).")
                    ]
                }
            ]
        },
        {
            "type": "grid_2x2",
            "section": "Tiết 3 — Cấu trúc một Gói Context Chuẩn mực",
            "title": "4 THÀNH PHẦN CỦA MỘT 'GÓI NGỮ CẢNH' (CONTEXT PACKAGE) CHẤT LƯỢNG CAO",
            "banner": ("green", "light_green", "Khi làm Đề án cuối khóa, mỗi lần giao nhiệm vụ lớn cho AI, nhóm bạn hãy kiểm tra xem đã nạp đủ 4 lớp Context này chưa:"),
            "boxes": [
                {
                    "header": "LỚP 1: TÀI LIỆU NGUỒN ĐÃ LÀM SẠCH (SOURCE DATA)",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Nội dung:", "File PDF bài báo khoa học gốc, báo cáo tài chính thật, văn bản thông tư hoặc bảng số liệu đã khử định danh."),
                        ("Nguyên tắc:", "Tải file trực tiếp lên phiên làm việc, đánh tên file rõ ràng (ví dụ: 'Bai_01_Linardon_2025.pdf').")
                    ]
                },
                {
                    "header": "LỚP 2: TIÊU CHUẨN & RUBRIC ĐÁNH GIÁ (DOMAIN RULES)",
                    "color": "accent",
                    "bg": "light_accent",
                    "bullets": [
                        ("Nội dung:", "Rubric chấm điểm của môn học, quy chuẩn trích dẫn APA 7, hoặc bộ tiêu chí phân tích nghiệp vụ ngân hàng."),
                        ("Tác dụng:", "Giúp AI biết thước đo nào để phân biệt một kết quả đạt chuẩn với một kết quả trung bình.")
                    ]
                },
                {
                    "header": "LỚP 3: VÍ DỤ MẪU CHUẨN MỰC (FEW-SHOT EXAMPLES)",
                    "color": "green",
                    "bg": "light_green",
                    "bullets": [
                        ("Nội dung:", "1 đến 2 mẫu đầu ra hoàn chỉnh do chính bạn đã làm và kiểm chứng (ví dụ: 1 mẫu Biên bản Soi 3 phút, 1 mẫu Atomic Note)."),
                        ("Tác dụng:", "Khóa chặt định dạng, độ sâu phân tích và giọng văn học thuật.")
                    ]
                },
                {
                    "header": "LỚP 4: RÀNG BUỘC BIÊN & CHỐT CHẶN (GUARDRAILS)",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Nội dung:", "Các quy tắc Negative Prompt và câu khóa chống suy diễn."),
                        ("Câu lệnh bắt buộc:", "'Chỉ dùng dữ liệu từ Lớp 1. Mọi nhận định phải kèm số trang. Chỗ nào không có trong Lớp 1 thì ghi rõ [Không nêu trong tài liệu], tuyệt đối không suy đoán.'")
                    ]
                }
            ]
        },
        {
            "type": "three_cards",
            "section": "Tiết 3 — Thực hành Va chạm tại Lớp (30 phút)",
            "title": "THỰC HÀNH 2.1: 'CÙNG 1 BÀI TOÁN CHUYÊN NGÀNH — 3 CẤP ĐỘ ĐẦU VÀO'",
            "banner": ("navy", "light_accent", "Mỗi nhóm lấy đúng bài toán Đề án của nhóm mình và chạy thử nghiệm đối chứng ở 3 cấp độ trên Claude / ChatGPT / Gemini:"),
            "cards": [
                {
                    "header": "CẤP ĐỘ 1: HỎI MƠ HỒ (ZERO-CONTEXT)",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Thao tác:", "Chỉ gõ 1 câu hỏi ngắn tự phát (1-2 dòng), không nêu bối cảnh, không đính kèm tài liệu, không có ràng buộc."),
                        ("Ví dụ:", "'Hãy phân tích các yếu tố ảnh hưởng đến ý định sử dụng ngân hàng số của Gen Z.'"),
                        ("Quan sát & Ghi nhận:", "AI trả lời chung chung thế nào? Có bịa số liệu hay nguồn trích dẫn không?")
                    ]
                },
                {
                    "header": "CẤP ĐỘ 2: DÙNG KHUNG CRISP CƠ BẢN",
                    "color": "orange",
                    "bg": "light_orange",
                    "bullets": [
                        ("Thao tác:", "Viết lại yêu cầu đó với đầy đủ 5 thành phần C - R - I - S - P (nêu rõ bối cảnh SV HUB, vai trò trợ lý nghiên cứu, yêu cầu lập bảng 4 cột, độ dài 250 chữ)."),
                        ("Quan sát & Ghi nhận:", "Cấu trúc đầu ra đã thay đổi ra sao so với Cấp độ 1? Nhưng khi chưa có tài liệu PDF thật thì các con số/trích dẫn đã dùng được chưa?")
                    ]
                },
                {
                    "header": "CẤP ĐỘ 3: CRISP + CONTEXT SẠCH + CHỐT CHẶN",
                    "color": "green",
                    "bg": "light_green",
                    "bullets": [
                        ("Thao tác:", "Đính kèm 1 tài liệu PDF thật + Khung CRISP + 1 Ví dụ mẫu (Few-shot) + Câu khóa: 'Mỗi ý ghi rõ số trang; chỗ nào bài không nói thì ghi không nêu trong bài, không suy đoán'."),
                        ("Quan sát & Đúc kết:", "So sánh độ chính xác, khả năng kiểm chứng tận dòng của Cấp độ 3 so với Cấp độ 1 và 2!")
                    ]
                }
            ]
        },
        {
            "type": "table",
            "section": "Tiết 3 — Bản đồ 4 Tầng tiến tới Buổi 3",
            "title": "BẢN ĐỒ TIẾN HÓA: DATA  -->  CONTEXT  -->  KNOWLEDGE  -->  HARNESS (WORKFLOW)",
            "headers": ["Tầng Kiến trúc", "Định nghĩa bản chất", "Ví dụ thực tế trong Đề án của Sinh viên HUB", "Học ở Buổi nào?"],
            "col_widths": [1.8, 2.7, 3.2, 1.3],
            "rows": [
                ["1. DATA\n(Dữ liệu thô)", "Các mảnh thông tin rời rạc, chưa gắn mục đích sử dụng cụ thể.", "Một file PDF bài báo tải về, một bảng số liệu Excel, một văn bản thông tư của Ngân hàng Nhà nước.", "Buổi 1 & Buổi 6"],
                ["2. CONTEXT\n(Ngữ cảnh có cấu trúc)", "Data được làm sạch và gắn thêm: Ai dùng, cho bài toán nào, theo tiêu chí gì (CRISP + 4 lớp Context).", "Gói tài liệu PDF đính kèm + Khung CRISP + Ví dụ mẫu Few-shot + Chốt chặn 'Không suy đoán' cho 1 phiên hỏi đáp.", "Buổi 2 (Hôm nay)"],
                ["3. KNOWLEDGE\n(Tri thức tái sử dụng)", "Khi Data + Context được bạn tinh chế qua não bộ thành quy tắc, mô hình và luận điểm dùng lại được nhiều lần.", "Hệ thống Ghi chú nguyên tử (Atomic Notes) trong Second Brain và bộ Rubric/Thang đo chuẩn của nhóm.", "Buổi 4 & Buổi 5"],
                ["4. HARNESS / WORKFLOW\n(Bộ dây cương điều phối)", "Knowledge và quy tắc được đóng gói thành quy trình nhiều bước có cổng dừng GATE (🔒) & FALLBACK (❓) chạy lặp lại ổn định.", "Một Claude Project hoặc Gemini Gem chuyên biệt cho Đề án của nhóm, tự động chạy đúng 4 bước và dừng chờ nhóm duyệt ở từng cổng.", "Buổi 3 (Tuần tới)"]
            ]
        },
        {
            "type": "two_cards",
            "section": "Tiết 4 — Studio Đề án Cuối khóa (30 phút)",
            "title": "STUDIO ĐỀ ÁN: CHỐT ĐỀ TÀI & SOẠN BỘ 3 CỤM PROMPT + CONTEXT (MẢNH GHÉP 1)",
            "cards": [
                {
                    "header": "NHIỆM VỤ 1: ĐĂNG KÝ CHÍNH THỨC ĐỀ TÀI ĐỀ ÁN NHÓM",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Yêu cầu tên Đề án:", "Rõ bài toán nghiệp vụ hoặc câu hỏi nghiên cứu ứng dụng + Rõ lĩnh vực chuyên ngành (Tài chính, Ngân hàng, Kế toán, Kiểm toán, QTKD, Marketing, MIS, Luật kinh tế...) + Rõ đối tượng/phạm vi."),
                        ("Ví dụ tên Đề án tốt:", "• 'Ứng dụng AI và quy trình kiểm chứng 5 bước trong phân tích các nhân tố ảnh hưởng đến rủi ro tín dụng xanh tại các NHTM Việt Nam.'\n• 'Xây dựng hệ thống AI Harness hỗ trợ kiểm soát chất lượng và rà soát sai sót thuyết minh Báo cáo tài chính doanh nghiệp niêm yết.'")
                    ]
                },
                {
                    "header": "NHIỆM VỤ 2: THIẾT KẾ 3 CỤM PROMPT CRISP + CONTEXT",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Mỗi nhóm soạn thảo 3 cụm Prompt chuẩn CRISP (theo Toolkit 1.2):", ""),
                        ("Cụm Prompt 1 (Khám phá & Thu hẹp câu hỏi):", "Dùng Role-based + CoT để phân rã bài toán và xây dựng phễu từ khóa tra cứu học thuật."),
                        ("Cụm Prompt 2 (Đọc sâu & Trích xuất tài liệu nguồn):", "Dùng CRISP + Few-shot + Chốt chặn 'Không suy đoán, ghi rõ số trang' trên file PDF đính kèm."),
                        ("Cụm Prompt 3 (Phản biện đa góc nhìn - Multi-Persona):", "Thiết lập hội đồng 3 chuyên gia phản biện chéo dàn ý và giải pháp của nhóm.")
                    ]
                }
            ]
        },
        {
            "type": "three_cards",
            "section": "Tiết 4 — Checklist Tự chấm Điểm Prompt & Context",
            "title": "RUBRIC TỰ KIỂM TRA CHẤT LƯỢNG PROMPT & CONTEXT CỦA NHÓM",
            "cards": [
                {
                    "header": "KIỂM TRA 1: ĐỦ 5 THÀNH TỐ CRISP CHƯA?",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        "[  ] Có Context (Bối cảnh ngành, mục tiêu đề án) rõ ràng?",
                        "[  ] Có Role (Vai trò chuyên gia cụ thể)?",
                        "[  ] Có Input & Instruction (Tài liệu đính kèm & nhiệm vụ rõ)?",
                        "[  ] Có Specifics (Định dạng bảng/mục, giới hạn số chữ, thuật ngữ)?",
                        "[  ] Có Performance Criteria (Tiêu chí đánh giá đầu ra)?"
                    ]
                },
                {
                    "header": "KIỂM TRA 2: KỸ THUẬT NÂNG CAO & CHỐT CHẶN?",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        "[  ] Đã tích hợp ít nhất 2 kỹ thuật nâng cao (CoT, Few-shot, Multi-Persona, Iterative, Negative Prompt)?",
                        "[  ] ĐÃ CÓ CÂU KHÓA CHỐNG BỊA: 'Mỗi ý ghi rõ số trang/mục; chỗ nào tài liệu không nói thì ghi không nêu trong bài, tuyệt đối không suy đoán'?",
                        "[  ] Đã loại bỏ hoàn toàn các yêu cầu xin danh mục trích dẫn tự do từ Chatbot?"
                    ]
                },
                {
                    "header": "KIỂM TRA 3: VỆ SINH GÓI CONTEXT?",
                    "color": "green",
                    "bg": "light_green",
                    "bullets": [
                        "[  ] Tài liệu đưa vào làm Context có phải là nguồn thật, chất lượng cao không?",
                        "[  ] Đã khử sạch thông tin định danh cá nhân (PII) hoặc dữ liệu mật trong các ví dụ Few-shot chưa?",
                        "[  ] Đã chạy thử đối chứng (Trước CRISP vs Sau CRISP) và lưu ảnh chụp kết quả vào hồ sơ Mảnh ghép 1 chưa?"
                    ]
                }
            ]
        },
        {
            "type": "three_cards",
            "section": "Tổng kết Buổi 2 — Ôn tập Truy hồi Chủ động (Active Recall)",
            "title": "3 CÂU HỎI CỦNG CỐ TRƯỚC KHI LÀM QUIZ BUỔI 2 TRÊN LMS HUB",
            "cards": [
                {
                    "header": "CÂU HỎI ÔN TẬP 1",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("Hỏi:", "Năm chữ cái C - R - I - S - P trong khung viết câu lệnh chuẩn mực đại diện cho những thành phần nào?"),
                        ("Đáp án cốt lõi:", "Context (Bối cảnh) - Role (Vai trò) - Input/Instruction (Đầu vào & Nhiệm vụ) - Specifics (Ràng buộc cụ thể) - Performance Criteria / Preview (Tiêu chí đánh giá & Hình dung kết quả).")
                    ]
                },
                {
                    "header": "CÂU HỎI ÔN TẬP 2",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("Hỏi:", "Khi một cuộc hội thoại với AI kéo dài quá nhiều lượt với đủ thứ chủ đề lộn xộn, hiện tượng gì sẽ xảy ra với Cửa sổ ngữ cảnh (Context Window)?"),
                        ("Đáp án cốt lõi:", "Xảy ra hiện tượng loãng/trôi ngữ cảnh (Context Rot): các ràng buộc và chỉ thị quan trọng ở đầu buổi bị đẩy ra xa hoặc bị nhiễu, khiến AI trả lời mất nhất quán và dễ quên quy tắc.")
                    ]
                },
                {
                    "header": "CÂU HỎI ÔN TẬP 3",
                    "color": "green",
                    "bg": "light_green",
                    "bullets": [
                        ("Hỏi:", "Câu lệnh chốt chặn nào bắt buộc phải cài vào Prompt khi yêu cầu AI tóm tắt hoặc trích xuất thông tin từ tài liệu khoa học?"),
                        ("Đáp án cốt lõi:", "'Mỗi ý bắt buộc ghi rõ số trang hoặc tên mục. Chỗ nào tài liệu không nói, ghi rõ không nêu trong bài, tuyệt đối không suy đoán.'")
                    ]
                }
            ]
        },
        {
            "type": "two_cards",
            "section": "Nhiệm vụ Khóa chốt Buổi 2 & Chuẩn bị Buổi 3",
            "title": "DANH MỤC NHIỆM VỤ BẮT BUỘC TRÊN LMS HUB & CHUẨN BỊ BUỔI 3",
            "cards": [
                {
                    "header": "NHIỆM VỤ CÁ NHÂN TRÊN LMS HUB",
                    "color": "red",
                    "bg": "light_red",
                    "bullets": [
                        ("1. Làm Quiz Buổi 2 (Active Recall 5 lượt):", "Hoàn thành 10 câu trắc nghiệm Buổi 2 trên LMS Hub để kiểm tra độ hiểu về CRISP, 5 kỹ thuật nâng cao và Context Engineering."),
                        ("2. Viết Nhật ký Học tập (Atomic Note 4F số 2):", "Đúc kết bài học từ trải nghiệm so sánh 3 cấp độ Prompt & Context hôm nay và lưu lại mẫu Prompt CRISP tâm đắc nhất của bạn."),
                        ("3. Gửi Feedback kèm nhận xét để tải Bài giảng:", "Mở khóa tải Slide Buổi 2 và ghi nhận điểm danh."),
                        ("4. Đọc trước eBook SCQA Chương 3:", "Chuẩn bị cho Buổi 3: Kiến trúc Harness — Xây dựng 'Bộ dây cương' điều phối AI.")
                    ]
                },
                {
                    "header": "NHIỆM VỤ NHÓM ĐỀ ÁN (CHUẨN BỊ CHỐT MẢNH GHÉP 1 Ở BUỔI 3)",
                    "color": "navy",
                    "bg": "off_white",
                    "bullets": [
                        ("1. Hoàn thiện bản viết 3 cụm Prompt CRISP + Context:", "Lưu kết quả chạy thử nghiệm đối chứng (Trước vs Sau CRISP) vào file hồ sơ nhóm."),
                        ("2. Chuẩn bị nguyên liệu cho Studio Buổi 3:", "Mang theo 1-2 tài liệu chuẩn của đề tài (đã khử thông tin nhạy cảm) và phác thảo quy trình 3-5 bước xử lý bài toán của nhóm."),
                        ("3. Tài khoản thực hành Buổi 3:", "Đảm bảo mỗi nhóm có sẵn tài khoản Claude (để dùng Claude Projects) hoặc Gemini (để dùng Gems / Gemini Notebook) sẵn sàng đóng gói Bộ Harness ở Buổi 3!")
                    ]
                }
            ]
        },
        {
            "type": "closing",
            "quote": "\"PROMPT LÀ GIAO DIỆN CỦA TƯ DUY.\n10 PHÚT THIẾT KẾ NGỮ CẢNH VÀ RÀNG BUỘC CHUẨN XÁC SẼ TIẾT KIỆM 2 GIỜ SỬA CHỮA MỘT KẾT QUẢ RÁC.\"",
            "takeaways": [
                ("1. CÔNG THỨC CRISP", "Luôn cung cấp đủ Context, Role, Input/Instruction, Specifics và Performance Criteria thay vì hỏi một câu cụt lủn."),
                ("2. CHỐT CHẶN KHÔNG SUY ĐOÁN", "Kết hợp CoT, Few-shot, Iterative, Negative Prompt và luôn bắt AI ghi rõ số trang, chỗ nào không có phải ghi 'Không nêu trong bài'."),
                ("3. CONTEXT ENGINEERING", "Giữ vệ sinh cửa sổ ngữ cảnh (Context Hygiene): nạp tài liệu nguồn sạch, rubric rõ ràng và ví dụ mẫu chuẩn mực.")
            ],
            "cta": "Hẹn gặp lại các bạn ở Buổi 3: Đóng gói toàn bộ Prompt & Context thành Bộ AI Harness (Cổng GATE & FALLBACK) và chốt Mảnh ghép 1!"
        }
    ]
}

out_b2_pptx = [
    r"d:\PARA\Projects\second-brain\03-Domains\Teaching\ComputerScience\Ky Nang Ung Dung AI\Slide_Buoi_02_Prompt_Va_Context_Engineering.pptx",
    r"d:\PARA\Projects\second-brain\05-Projects\lms-hub\courses\ky-nang-ai-hub\content\slides\Buoi_02.pptx"
]
out_b2_html = [
    r"d:\PARA\Projects\second-brain\03-Domains\Teaching\ComputerScience\Ky Nang Ung Dung AI\Slide_Buoi_02_Prompt_Va_Context_Engineering.html",
    r"d:\PARA\Projects\second-brain\05-Projects\lms-hub\courses\ky-nang-ai-hub\content\slides\Buoi_02.html"
]

render_deck_pptx(buoi_02_spec, out_b2_pptx)
render_deck_html(buoi_02_spec, out_b2_html)
print("Buoi 02 slides generated successfully (20 slides).")
