# -*- coding: utf-8 -*-
import os
import json

CONTENT_DIR = r"d:\PARA\Projects\second-brain\05-Projects\lms-hub\courses\ky-nang-ai-hub\content"
null = None
true = True
false = False

chapters_7_to_11 = [
    {
        "chapter": 7,
        "title": "Trích dẫn bịa, Checklist Kiểm chứng 5 bước, Công cụ Tomaca & Zotero 8",
        "sessions": [7],
        "scqa": {
            "situation": "Khi viết báo cáo nghiên cứu hoặc khóa luận tốt nghiệp, bạn cần khoảng 15-20 tài liệu tham khảo uy tín. Bạn thấy những trích dẫn do AI gợi ý có tên tác giả rất nổi tiếng trong ngành, tên tạp chí đúng chuẩn quốc tế, có cả số tập, số trang và mã DOI đúng cú pháp `10.xxxx/...` nên yên tâm đưa thẳng vào bài.",
            "complication": "Nghiên cứu thực nghiệm của Linardon và cộng sự (2025, JMIR Mental Health) trên 176 trích dẫn do GPT-4o tạo ra cho thấy: 19.9% bịa hoàn toàn và tới 56.3% là bịa hoặc sai thông tin thư mục! Nguy hiểm hơn, tỷ lệ bịa tăng vọt từ 6% ở chủ đề phổ biến lên tới 28% - 29% ở các đề tài ít được nghiên cứu (p = .001) - tức là AI bịa nhiều nhất ở đúng những đề tài chuyên sâu mà sinh viên cần nó nhất. Trong một bài báo thực tế (Ren và cs., 2025), tới 18/30 trích dẫn (60%) là bịa và 21/33 mã DOI giả lại dẫn sang một bài báo thật hoàn toàn không liên quan!",
            "question": "Nếu không thể dựa vào cảm giác 'trông rất giống thật' hay 'có mã DOI', làm thế nào để xây dựng một màng lọc kỹ thuật đảm bảo 100% tài liệu tham khảo trong Đề án của bạn là nguồn thật, đúng ý và sạch lỗi?",
            "answer": "Khắc cốt ghi tâm quy tắc 'Chưa kiểm chứng, chưa vào bài': thực thi Checklist kiểm chứng 5 bước từ rẻ đến tốn công, kết hợp công cụ rà soát tự động Tomaca theo nguyên tắc 'Máy soát, người quyết', và khóa chặt đầu vào bằng phần mềm Zotero 8 ('Nguồn vào Zotero trước, vào bài sau')."
        },
        "concepts": [
            {
                "id": "c7-linardon-citation",
                "session": 7,
                "term": "Quy luật Trích dẫn bịa của Linardon (2025) & Hình hài một trích dẫn 'ghép xác'",
                "definition": "Bằng chứng khoa học giải thích khi nào LLM bịa trích dẫn nhiều nhất và cách thức mô hình xác suất lắp ghép các mảnh thông tin thật thành một tài liệu tham khảo giả mạo hoàn hảo.",
                "key_points": [
                    "<strong>Quy luật Linardon và cs. (2025, JMIR Ment Health 12:e80371):</strong> Kiểm tra 176 trích dẫn từ 6 bài tổng quan do GPT-4o viết -> <strong>19.9% (35/176) bịa hoàn toàn</strong>; gộp cả bài có thật nhưng sai thông tin thư mục là <strong>56.3% (99/176)</strong>.",
                    "<strong>Bịa theo mức độ được nghiên cứu (p = .001):</strong> Tỷ lệ bịa chỉ <strong>6%</strong> ở đề tài được nghiên cứu nhiều, nhưng vọt lên <strong>28% - 29%</strong> ở đề tài ít được nghiên cứu (chứ không phụ thuộc đề tài hẹp hay rộng, p = .21). <em>AI không bịa ngẫu nhiên, nó bịa nhiều nhất ở chỗ nó biết ít nhất!</em>",
                    "<strong>Giải phẫu một trích dẫn 'ghép xác':</strong> AI ghép (1) Tên tác giả có thật trong ngành + (2) Tên tạp chí có thật + (3) Số tập, số trang hợp lý + (4) Mã DOI đúng cú pháp (nhưng không tồn tại hoặc 21/33 trường hợp trỏ sang bài báo khác không liên quan) + (5) Tiêu đề bài báo khớp đúng đề tài của bạn."
                ],
                "case_study": {
                    "title": "Bài báo dính 60% trích dẫn bịa (Ren và cs., 2025)",
                    "context": "Kiểm tra một bài viết chuyên ngành trong đó 18 trên 30 tài liệu tham khảo (60%) là sản phẩm do AI bịa ra nhưng tất cả tiêu đề đều bám cực sát chủ đề bài viết.",
                    "analysis": "Người đọc bình thường nếu chỉ nhìn danh mục tài liệu tham khảo bằng mắt thường sẽ không bao giờ phát hiện ra.",
                    "lesson_learned": "Tuyệt đối không đánh giá độ thật/giả của trích dẫn bằng cảm giác 'nghe đúng chủ đề'."
                },
                "related_concepts": ["c7-checklist-5-buoc", "c7-tomaca-zotero"]
            },
            {
                "id": "c7-checklist-5-buoc",
                "session": 7,
                "term": "Checklist Kiểm chứng một Trích dẫn qua 5 Bước (Từ rẻ đến tốn công)",
                "definition": "Quy trình 5 câu hỏi tuần tự giúp lọc sạch cả trích dẫn bịa hoàn toàn lẫn trích dẫn có thật nhưng bị AI gán sai nội dung hoặc đã bị rút lại.",
                "key_points": [
                    "<strong>Bước 1 - Có thật không?</strong> Tra tiêu đề trên Google Scholar / Semantic Scholar hoặc tra mã DOI trên <code>doi.org</code>.",
                    "<strong>Bước 2 - Thông tin thư mục có khớp không?</strong> Tên tác giả, năm xuất bản, tên tạp chí, số tập, số trang phải trùng khớp với trang gốc của nhà xuất bản.",
                    "<strong>Bước 3 - Bài gốc có nói đúng ý đó không? (Bước hay bị bỏ qua nhất!)</strong> Mở file PDF bản gốc, tìm đúng đoạn văn được trích dẫn để chắc chắn tác giả thực sự nói ý đó (chống lại lỗi gán ghép luận điểm giả vào một bài báo có thật).",
                    "<strong>Bước 4 - Số liệu có khớp không?</strong> Đối chiếu trực tiếp con số trích dẫn với Bảng (Table) và Hình (Figure) trong bài báo gốc.",
                    "<strong>Bước 5 - Bài báo còn hiệu lực không?</strong> Tra cứu trên <em>Retraction Watch Database</em> xem bài báo có bị rút lại (retracted) vì gian lận khoa học hay không."
                ],
                "case_study": null,
                "related_concepts": ["c7-linardon-citation", "c7-tomaca-zotero"]
            },
            {
                "id": "c7-tomaca-zotero",
                "session": 7,
                "term": "Công cụ Tomaca ('Máy soát, Người quyết') & Quy trình khóa chốt Zotero 8",
                "definition": "Sự kết hợp giữa công cụ kiểm tra trích dẫn tự động đa cơ sở dữ liệu (Tomaca) và phần mềm quản lý tài liệu tham khảo mã nguồn mở (Zotero 8) để xây dựng quy trình tài liệu tham khảo không thể bị nhiễm rác AI.",
                "key_points": [
                    "<strong>Cơ chế của Tomaca (TS. Trần Việt Tâm - pro-tomaca.quyentrungga.com):</strong> Đối chiếu chéo DOI trên Crossref, OpenAlex, DataCite; cảnh báo tạp chí săn mồi/mạo danh và xếp hạng Q. Phân loại 3 nhóm kết quả: <em>Đạt</em> (<code>verified-doi</code>, <code>verified-book</code>), <em>Không đạt</em> (<code>no-doi</code>, <code>doi-not-found</code>), và <em>Chưa nêu rõ - Cần người xem lại</em> (<code>metadata-mismatch</code>: DOI thật nhưng năm/tên lệch).",
                    "<strong>Giới hạn thực nghiệm của máy ('Máy soát, Người quyết'):</strong> Trong bộ test thực tế 10 trích dẫn (7 thật, 3 giả ngày 17/10/2026), Tomaca báo 9 <code>verified-doi</code> và 1 <code>metadata-mismatch</code>, bỏ lọt 2 mục giả vì DOI giả tình cờ trỏ về một bài báo có thật khác! Do đó, máy chỉ giúp lọc nhanh bước đầu, con người bắt buộc phải đọc nguồn gốc để quyết định.",
                    "<strong>Quy tắc vàng với Zotero 8: 'Nguồn vào Zotero trước, rồi mới vào bài':</strong> (1) Chỉ lưu bài vào Zotero qua Zotero Connector khi mắt bạn đang mở trang bài báo thật sau khi đã kiểm chứng -> (2) Trong Word/Docs, chỉ chèn trích dẫn từ thư viện Zotero, tuyệt đối không gõ tay hay copy từ AI -> (3) Đổi chuẩn APA 7 / IEEE tự động cho toàn bài chỉ bằng 1 cú nhấp chuột."
                ],
                "case_study": null,
                "related_concepts": ["c7-checklist-5-buoc"]
            }
        ],
        "tests": {
            "level_1": {
                "name": "🎯 Level 1: Khái niệm cốt lõi",
                "description": "Nhận biết số liệu Linardon (2025), Checklist 5 bước, 3 nhóm kết quả Tomaca và quy trình Zotero.",
                "bloom_level": "Remember",
                "questions": [
                    {
                        "id": "L1-c7-q1",
                        "type": "mc",
                        "concept_ref": "c7-linardon-citation",
                        "question": "Theo nghiên cứu của Linardon và cộng sự (2025) trên tạp chí JMIR Mental Health khi kiểm tra 176 trích dẫn do GPT-4o tạo ra, tổng tỷ lệ trích dẫn bịa hoàn toàn (19.9%) cộng với trích dẫn có thật nhưng sai thông tin thư mục là bao nhiêu?",
                        "options": [
                            "A. Chỉ khoảng 2%",
                            "B. 56.3% (99 trên 176 trích dẫn có vấn đề)",
                            "C. 10%",
                            "D. 0%"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L1-c7-q2",
                        "type": "mc",
                        "concept_ref": "c7-linardon-citation",
                        "question": "Cũng theo nghiên cứu của Linardon và cộng sự (2025), yếu tố nào quyết định việc AI bịa trích dẫn nhiều hơn (tăng từ 6% lên tới 28%-29%, với p = .001)?",
                        "options": [
                            "A. Mức độ chủ đề đó đã được nghiên cứu kỹ hay ít được nghiên cứu (AI bịa nhiều hơn ở các đề tài ít được nghiên cứu)",
                            "B. Thời tiết vào ngày người dùng đặt câu hỏi",
                            "C. Độ dài của tên tác giả",
                            "D. Màu sắc giao diện của phần mềm AI"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L1-c7-q3",
                        "type": "mc",
                        "concept_ref": "c7-checklist-5-buoc",
                        "question": "Năm bước trong Checklist kiểm chứng một trích dẫn khoa học theo thứ tự từ rẻ đến tốn công là gì?",
                        "options": [
                            "A. (1) Có thật không? -> (2) Thông tin thư mục khớp không? -> (3) Bài gốc có nói đúng ý đó không? -> (4) Số liệu khớp bảng/hình không? -> (5) Còn hiệu lực trên Retraction Watch không?",
                            "B. Copy -> Paste -> Đổi phông chữ -> Căn lề -> Nộp bài",
                            "C. Hỏi ChatGPT -> Hỏi Claude -> Hỏi Gemini -> Lấy trung bình cộng",
                            "D. Chỉ cần kiểm tra xem mã DOI có bắt đầu bằng số 10 hay không"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L1-c7-q4",
                        "type": "mc",
                        "concept_ref": "c7-tomaca-zotero",
                        "question": "Khi sử dụng công cụ kiểm tra trích dẫn Tomaca, nhãn kết quả `metadata-mismatch` thuộc nhóm 'Chưa nêu rõ' có ý nghĩa là gì?",
                        "options": [
                            "A. Mã DOI có tồn tại trên cơ sở dữ liệu nhưng thông tin năm xuất bản, tiêu đề hoặc tên tác giả trong bài của bạn bị lệch so với bản gốc, bắt buộc con người phải mở ra kiểm tra lại",
                            "B. Trích dẫn đã hoàn hảo 100%, không cần xem lại",
                            "C. Máy chủ đang bảo trì",
                            "D. Bài báo được viết bằng tiếng Pháp"
                        ],
                        "correct": "A"
                    }
                ]
            },
            "level_2": {
                "name": "📝 Level 2: Hiểu và phân biệt",
                "description": "Hiểu tại sao Bước 3 hay bị bỏ qua nhất và tại sao công cụ tự động vẫn có thể bỏ lọt trích dẫn giả.",
                "bloom_level": "Understand",
                "questions": [
                    {
                        "id": "L2-c7-q1",
                        "type": "mc",
                        "concept_ref": "c7-checklist-5-buoc",
                        "question": "Tại sao trong Checklist 5 bước, Bước 3 ('Mở bản gốc kiểm tra xem bài báo có thực sự nói đúng ý đó không') lại là bước quan trọng để chống lại loại lỗi nguy hiểm hơn cả trích dẫn bịa hoàn toàn?",
                        "options": [
                            "A. Vì rất nhiều trường hợp bài báo, tên tác giả và mã DOI đều có thật 100% (vượt qua Bước 1 và 2 dễ dàng), nhưng AI lại gán cho bài báo đó một kết luận hoặc số liệu mà tác giả bài gốc không hề nói tới, hoặc nói ngược lại!",
                            "B. Vì Bước 1 và Bước 2 không cần làm",
                            "C. Vì mở file PDF giúp máy tính chạy nhanh hơn",
                            "D. Vì Bước 3 giúp tự động dịch bài báo"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L2-c7-q2",
                        "type": "mc",
                        "concept_ref": "c7-tomaca-zotero",
                        "question": "Trong thử nghiệm thực tế ngày 17/10/2026 trên bộ test 10 trích dẫn (7 thật, 3 giả), tại sao công cụ Tomaca lại báo `verified-doi` cho cả 2 trích dẫn giả và bài học rút ra là gì?",
                        "options": [
                            "A. Vì AI khi bịa trích dẫn đã lấy một mã DOI có thật của một bài báo khác không liên quan ghép vào tiêu đề bịa; máy kiểm tra thấy DOI tồn tại nên báo đạt. Bài học: 'Máy soát, người quyết' - con người luôn phải mở nguồn gốc để đối chiếu tiêu đề và nội dung",
                            "B. Vì không bao giờ nên dùng bất kỳ công cụ kiểm tra nào",
                            "C. Vì trích dẫn giả đó đã tự động biến thành bài báo thật",
                            "D. Vì chỉ cần máy báo verified-doi là được miễn trách nhiệm học thuật"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L2-c7-q3",
                        "type": "mc",
                        "concept_ref": "c7-tomaca-zotero",
                        "question": "Vì sao việc tuân thủ nghiêm ngặt quy trình 'Nguồn vào Zotero trước, rồi mới vào bài' lại giúp loại bỏ tận gốc nguy cơ lọt trích dẫn do AI bịa vào báo cáo Đề án?",
                        "options": [
                            "A. Vì bạn chỉ bấm nút Zotero Connector để lưu tài liệu khi chính mắt bạn đang mở trang bài báo thật của nhà xuất bản (sau khi đã kiểm chứng), và trong Word bạn chỉ chèn trích dẫn từ thư viện Zotero đó chứ không bao giờ copy-paste dòng trích dẫn từ cửa sổ chat của AI",
                            "B. Vì Zotero là một trí tuệ nhân tạo biết tự viết báo cáo",
                            "C. Vì Zotero cấm người dùng gõ tiếng Việt",
                            "D. Vì Zotero tự động xóa mọi bài báo xuất bản trước năm 2025"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L2-c7-q4",
                        "type": "mc",
                        "concept_ref": "c7-linardon-citation",
                        "question": "Khi giảng viên nói 'AI bịa nhiều hơn ở đề tài ít được nghiên cứu chứ không phải đề tài hẹp', điều này cảnh báo gì cho sinh viên ngành Ngân hàng - Kinh tế khi làm đề tài mới tại Việt Nam?",
                        "options": [
                            "A. Những đề tài mang tính địa phương hoặc bối cảnh mới tại Việt Nam có ít dữ liệu học thuật quốc tế trong tập huấn luyện của LLM, nên nếu sinh viên nhờ Chatbot viết tổng quan tài liệu cho các đề tài này, tỷ lệ AI bịa trích dẫn sẽ ở mức cao nhất",
                            "B. Sinh viên không được phép chọn đề tài mới tại Việt Nam",
                            "C. Đề tài tại Việt Nam thì AI không bao giờ bịa",
                            "D. Chỉ cần viết câu hỏi ngắn lại là AI sẽ không bịa"
                        ],
                        "correct": "A"
                    }
                ]
            },
            "level_3": {
                "name": "🚀 Level 3: Vận dụng thực tế",
                "description": "Thực hành kiểm chứng danh mục tài liệu của Đề án nhóm qua Checklist 5 bước, Tomaca và Zotero.",
                "bloom_level": "Apply",
                "questions": [
                    {
                        "id": "L3-c7-q1",
                        "type": "mc",
                        "concept_ref": "c7-checklist-5-buoc",
                        "question": "Trong khi Kiểm toán chéo (Peer Audit) báo cáo của nhóm bạn, bạn thấy câu: 'Theo Nguyễn và Trần (2025, Journal of Banking & Finance, DOI: 10.1016/j.jbankfin.2024.107111), 74% ngân hàng Việt Nam đã dùng AI duyệt vay'. Khi bạn bấm vào link DOI đó trên doi.org, trang web mở ra một bài báo năm 2024 của tác giả Smith về thị trường chứng khoán Mỹ. Kết luận kiểm toán của bạn là gì?",
                        "options": [
                            "A. Trích dẫn đạt chuẩn vì mã DOI có hoạt động và dẫn tới tạp chí Journal of Banking & Finance thật",
                            "B. Đây là một trích dẫn bịa điển hình dạng 'ghép xác' (ghép tác giả Việt Nam và luận điểm bịa vào một mã DOI có thật của bài báo khác); nhóm bạn đã không thực hiện Bước 2 và Bước 3 của Checklist 5 bước nên đã vi phạm Điểm liệt Liêm chính",
                            "C. Chỉ là lỗi đánh máy nhỏ, không cần sửa",
                            "D. Lỗi do trang web doi.org bị hỏng"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L3-c7-q2",
                        "type": "mc",
                        "concept_ref": "c7-tomaca-zotero",
                        "question": "Khi chạy danh mục 12 tài liệu tham khảo của Đề án nhóm trên Tomaca, có 1 báo cáo thường niên của Ngân hàng Nhà nước Việt Nam bị báo nhãn `no-doi` (Không có DOI). Cách xử lý đúng chuẩn 'Máy soát, người quyết' là gì?",
                        "options": [
                            "A. Tự chế ra một mã DOI giả điền vào để Tomaca báo xanh",
                            "B. Hiểu rằng các báo cáo ngành, văn bản pháp quy hoặc sách chuyên khảo trong nước thường không đăng ký mã DOI; nhóm tự kiểm chứng thủ công đường dẫn URL chính thức trên cổng thông tin Ngân hàng Nhà nước, lưu metadata chuẩn vào Zotero và ghi chú rõ trong biên bản kiểm chứng",
                            "C. Xóa bỏ hoàn toàn mọi báo cáo của Ngân hàng Nhà nước khỏi đề án",
                            "D. Nhờ ChatGPT cấp mã DOI cho báo cáo đó"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L3-c7-essay1",
                        "type": "essay",
                        "concept_ref": "c7-checklist-5-buoc",
                        "question": "Hãy lấy 03 tài liệu tham khảo trong Đề án cuối khóa của nhóm bạn và lập 'Bảng Báo cáo Kiểm chứng 5 bước & Zotero': Với mỗi tài liệu, ghi rõ kết quả kiểm tra ở từng bước (Bước 1: Link DOI/Scholar; Bước 2: Khớp thư mục; Bước 3: Trích nguyên văn câu trong bài gốc chứng minh bài báo có nói đúng luận điểm nhóm bạn trích; Bước 4: Số liệu; Bước 5: Tình trạng hiệu lực) và kết quả quét trên Tomaca.",
                        "rubric": "Đủ 3 tài liệu thật phục vụ Đề án nhóm (20%) · Điền đầy đủ và trung thực kết quả cả 5 bước kiểm chứng cho từng bài (40%) · Ở Bước 3 trích dẫn được chính xác câu/đoạn văn gốc kèm số trang (25%) · Nêu rõ kết quả đối chiếu trên Tomaca và xác nhận đã nạp Zotero (15%)",
                        "max_words": 400
                    }
                ]
            }
        }
    },
    {
        "chapter": 8,
        "title": "Quy trình NCKH với AI (Bước 3 & 4): Tổng hợp đa nguồn, Viết học thuật & Trình bày",
        "sessions": [8],
        "scqa": {
            "situation": "Nhóm của bạn đã tìm được 10 bài báo khoa học thật, đã 'soi' từng bản tóm tắt, kiểm chứng qua 5 bước và nạp toàn bộ vào Zotero cũng như Second Brain. Giờ là lúc phải viết phần Tổng quan tài liệu (Literature Review) dài 1.500 chữ và thiết kế bộ Slide bảo vệ Đề án.",
            "complication": "Rất nhiều nhóm sinh viên rơi vào cảnh viết 'Tổng quan tài liệu kiểu liệt kê': đoạn 1 tóm tắt bài của tác giả A, đoạn 2 tóm tắt bài của tác giả B, đoạn 3 tóm tắt bài của tác giả C... mà không có bất kỳ sợi dây liên kết hay so sánh nào giữa các bài. Hoặc tệ hơn, nhóm quăng cả 10 bài cho AI viết hộ một mạch rồi dùng công cụ tạo slide tự động (Gamma) xuất ra những trang slide lòe loẹt nhưng rỗng tuếch, làm mất hoàn toàn tiếng nói học thuật và dấu ấn cá nhân của nhóm.",
            "question": "Làm thế nào để chuyển hóa 10 bài báo rời rạc thành một bức tranh tổng hợp sắc bén chỉ ra được khoảng trống nghiên cứu (Research Gap), viết báo cáo chuẩn mực từ Second Brain + Zotero, và thiết kế bài trình bày mang đậm bản sắc của người làm chủ?",
            "answer": "Sử dụng Ma trận Tổng hợp (Synthesis Matrix) trên Elicit và Gemini Notebook để so sánh chéo đa nguồn theo chủ đề; thực hiện quy trình viết học thuật 4 nhịp từ Atomic Notes kết hợp chèn trích dẫn Zotero; và áp dụng quy trình 4 lớp làm slide theo nguyên tắc 'AI làm Draft, Người làm Final'."
        },
        "concepts": [
            {
                "id": "c8-synthesis-matrix",
                "session": 8,
                "term": "Phân biệt Tóm tắt (Summary) vs Tổng hợp (Synthesis) & Ma trận Tổng hợp",
                "definition": "Bước chuyển từ việc kể lại nội dung từng tài liệu riêng lẻ (Summary) sang việc đặt nhiều tài liệu lên cùng một bàn cân theo từng trục chủ đề, phương pháp hoặc biến số để tìm ra điểm đồng thuận, điểm tranh luận và khoảng trống nghiên cứu (Synthesis).",
                "key_points": [
                    "<strong>Bẫy liệt kê đơn tuyến (A -> B -> C):</strong> Viết theo từng bài báo làm người đọc không thấy được bức tranh chung của lĩnh vực.",
                    "<strong>Ma trận Tổng hợp (Synthesis Matrix):</strong> Bảng hai chiều trong đó <em>hàng ngang là các Bài báo đã kiểm chứng</em> (Nguồn 1, Nguồn 2, Nguồn 3...) và <em>cột dọc là các Khía cạnh/Chủ đề so sánh</em> (Bối cảnh mẫu, Phương pháp/Mô hình, Các yếu tố tác động chính, Hạn chế chưa giải quyết).",
                    "<strong>Cách dùng AI ở Bước 3 (Tổng hợp):</strong> Dùng bảng Elicit và nạp các bài báo đã kiểm chứng vào Gemini Notebook để trích xuất dữ liệu vào từng ô của Ma trận (kèm số trang); sau đó <em>chính con người nhìn vào Ma trận để rút ra nhận định so sánh và phát hiện Research Gap</em>."
                ],
                "case_study": {
                    "title": "Tìm ra khoảng trống nghiên cứu từ Ma trận 5 bài báo",
                    "context": "Khi đặt 5 bài báo về hành vi dùng Mobile Banking lên cùng một bảng Synthesis Matrix, nhóm sinh viên nhận thấy cả 5 bài đều khảo sát ở nhóm khách hàng thành thị trẻ, chưa bài nào đo lường yếu tố 'chi phí chuyển đổi nhận thức' ở nhóm khách hàng trung niên.",
                    "analysis": "Khoảng trống nghiên cứu (Research Gap) tự động lộ diện khi các nguồn được đặt cạnh nhau theo cột chuẩn.",
                    "lesson_learned": "AI giúp lập bảng so sánh nhanh, nhưng con mắt phát hiện khoảng trống nghiên cứu là của bạn."
                },
                "related_concepts": ["c8-viet-4-nhip", "c8-slide-4-lop"]
            },
            {
                "id": "c8-viet-4-nhip",
                "session": 8,
                "term": "Quy trình Viết học thuật 4 nhịp (Second Brain + AI + Zotero)",
                "definition": "Phương pháp viết báo cáo nghiên cứu và đề án đảm bảo tính nguyên bản của tư duy, sự chặt chẽ của lập luận và độ chính xác tuyệt đối của trích dẫn.",
                "key_points": [
                    "<strong>Nhịp 1 - Lắp ghép khung từ Second Brain:</strong> Người học tự sắp xếp các <em>Atomic Notes</em> của mình thành dàn ý chi tiết và chuỗi luận điểm gốc.",
                    "<strong>Nhịp 2 - Nhờ AI phản biện dàn ý (Devil's Advocate):</strong> Yêu cầu AI đóng vai người phản biện khó tính: <em>'Hãy chỉ ra 3 điểm chuyển ý còn yếu hoặc thiếu bằng chứng thực nghiệm trong dàn ý này của tôi.'</em>",
                    "<strong>Nhịp 3 - Tự viết bản thảo & Chèn trích dẫn Zotero 8:</strong> Người học tự viết nội dung từng mục từ Ma trận tổng hợp và bấm chèn trích dẫn trực tiếp từ thư viện <strong>Zotero</strong> (tuyệt đối không để AI tự viết phần Kết quả, Thảo luận hay tự gõ trích dẫn).",
                    "<strong>Nhịp 4 - Biên tập văn phong có ràng buộc:</strong> Nhờ AI rà soát lỗi chính tả, độ mạch lạc và chuẩn hóa thuật ngữ với câu khóa: <em>'Chỉ gợi ý chỉnh sửa diễn đạt câu chữ cho rõ ràng và học thuật hơn; tuyệt đối không thêm bớt số liệu, không thay đổi luận điểm và giữ nguyên các mã trích dẫn Zotero.'</em>"
                ],
                "case_study": null,
                "related_concepts": ["c8-synthesis-matrix"]
            },
            {
                "id": "c8-slide-4-lop",
                "session": 8,
                "term": "Quy trình 4 lớp chuẩn bị Bài trình bày ('AI làm Draft, Người làm Final')",
                "definition": "Phương pháp ứng dụng AI để tăng tốc việc thiết kế bài thuyết trình học thuật mà không rơi vào căn bệnh 'slide công nghiệp chung chung, thiếu hồn cốt'.",
                "key_points": [
                    "<strong>Lớp 1 - Cấu trúc thông điệp (Storyline & SCQA):</strong> Xác định rõ khán giả là ai (Hội đồng kiểm toán chéo & Giảng viên), dùng khung SCQA để mở đầu bằng một con số hoặc mâu thuẫn đắt giá thay vì mở đầu nhàm chán.",
                    "<strong>Lớp 2 - Kịch bản thuyết trình (Speaker Script):</strong> AI hỗ trợ chia thời lượng từng phút, nhưng người nói phải đưa trải nghiệm thực nghiệm của chính nhóm mình (ví dụ: câu chuyện nhóm đã phát hiện AI bịa chữ Pearson's R như thế nào) vào lời nói.",
                    "<strong>Lớp 3 - Thiết kế trực quan (Visual Slide):</strong> Có thể dùng Gamma, PowerPoint Copilot hoặc HTML/Claude Artifacts để dựng khung bố cục nhanh, nhưng bắt buộc con người phải tinh chỉnh lại typography, bảng biểu và thay thế các câu chữ sáo rỗng bằng tiêu đề mang tính kết luận (Action Titles).",
                    "<strong>Lớp 4 - Minh họa dữ liệu & Bằng chứng thật:</strong> Đưa ảnh chụp màn hình thực nghiệm thật của nhóm (ảnh chạy bộ Harness, ảnh báo cáo Tomaca, ảnh thư viện Zotero) lên slide làm bằng chứng sống."
                ],
                "case_study": null,
                "related_concepts": ["c8-viet-4-nhip"]
            }
        ],
        "tests": {
            "level_1": {
                "name": "🎯 Level 1: Khái niệm cốt lõi",
                "description": "Nhận diện sự khác biệt giữa Summary và Synthesis, quy trình viết 4 nhịp và làm slide 4 lớp.",
                "bloom_level": "Remember",
                "questions": [
                    {
                        "id": "L1-c8-q1",
                        "type": "mc",
                        "concept_ref": "c8-synthesis-matrix",
                        "question": "Sự khác biệt căn bản giữa 'Tóm tắt từng bài' (Summary) và 'Tổng hợp đa nguồn' (Synthesis) trong nghiên cứu khoa học là gì?",
                        "options": [
                            "A. Tóm tắt là kể lại lần lượt từng bài riêng lẻ; còn Tổng hợp là đặt nhiều bài lên cùng các trục chủ đề/phương pháp để so sánh điểm đồng thuận, điểm mâu thuẫn và tìm ra khoảng trống nghiên cứu",
                            "B. Tóm tắt viết bằng tiếng Việt, còn Tổng hợp viết bằng tiếng Anh",
                            "C. Tóm tắt dài hơn Tổng hợp 10 lần",
                            "D. Hai khái niệm này hoàn toàn giống hệt nhau"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L1-c8-q2",
                        "type": "mc",
                        "concept_ref": "c8-viet-4-nhip",
                        "question": "Trong Quy trình viết học thuật 4 nhịp, việc chèn trích dẫn vào bài báo cáo Đề án ở Nhịp 3 được thực hiện bằng cách nào?",
                        "options": [
                            "A. Nhờ ChatGPT tự gõ danh sách trích dẫn vào cuối đoạn văn",
                            "B. Người học tự viết luận điểm từ Ma trận tổng hợp/Second Brain và chèn trích dẫn trực tiếp từ thư viện phần mềm Zotero 8 (nơi chỉ chứa các nguồn thật đã qua 5 bước kiểm chứng)",
                            "C. Gõ tay tên tác giả theo trí nhớ mang máng",
                            "D. Copy danh mục tài liệu tham khảo từ một bài luận mẫu trên mạng"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L1-c8-q3",
                        "type": "mc",
                        "concept_ref": "c8-slide-4-lop",
                        "question": "Nguyên tắc 'AI làm Draft, Người làm Final' khi thiết kế slide báo cáo Đề án có nghĩa là gì?",
                        "options": [
                            "A. Dùng AI (như Gamma, Copilot, Claude) để dựng nhanh cấu trúc bố cục nháp ban đầu, sau đó con người phải biên tập lại tiêu đề, gọt giũa số liệu chuẩn xác và đưa các minh chứng thực nghiệm thật của nhóm vào bản cuối",
                            "B. Bấm nút cho AI tạo slide trong 1 phút rồi mang thẳng lên hội đồng trình chiếu mà không cần đọc lại",
                            "C. Cấm tuyệt đối việc dùng máy tính làm slide",
                            "D. Để AI tự thuyết trình bằng giọng đọc máy suốt 15 phút"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L1-c8-q4",
                        "type": "mc",
                        "concept_ref": "c8-viet-4-nhip",
                        "question": "Ở Nhịp 4 của quy trình viết học thuật, khi nhờ AI biên tập và nâng cấp văn phong cho bản thảo đã viết, ràng buộc nào sau đây là bắt buộc?",
                        "options": [
                            "A. Cho phép AI tự do sáng tác thêm số liệu mới cho bài viết sinh động",
                            "B. Yêu cầu AI chỉ chỉnh sửa diễn đạt ngữ pháp cho rõ ràng và học thuật hơn, tuyệt đối không thay đổi luận điểm gốc, không tự thêm số liệu và giữ nguyên các mã trích dẫn Zotero",
                            "C. Yêu cầu AI xóa hết các trích dẫn Zotero đi",
                            "D. Yêu cầu AI viết lại thành một chủ đề khác"
                        ],
                        "correct": "B"
                    }
                ]
            },
            "level_2": {
                "name": "📝 Level 2: Hiểu và phân biệt",
                "description": "Phân tích cách dùng Synthesis Matrix và lý do không giao phần Kết quả/Thảo luận cho AI viết hộ.",
                "bloom_level": "Understand",
                "questions": [
                    {
                        "id": "L2-c8-q1",
                        "type": "mc",
                        "concept_ref": "c8-synthesis-matrix",
                        "question": "Tại sao việc lập Ma trận Tổng hợp (Synthesis Matrix) trước khi đặt bút viết lại giúp sinh viên tránh được lỗi đạo văn và lỗi viết rời rạc?",
                        "options": [
                            "A. Vì khi nhìn vào một cột chủ đề trong Ma trận, sinh viên thấy ngay nhóm tác giả nào đồng ý, nhóm tác giả nào phản đối và số liệu chênh nhau ra sao, từ đó tự viết được một đoạn văn đối thoại học thuật đa nguồn thay vì chép lại từng bài đơn lẻ",
                            "B. Vì Ma trận Tổng hợp giúp che giấu nguồn gốc tài liệu",
                            "C. Vì giảng viên không đọc được bảng Ma trận",
                            "D. Vì lập bảng xong thì không cần viết chữ nào nữa"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L2-c8-q2",
                        "type": "mc",
                        "concept_ref": "c8-viet-4-nhip",
                        "question": "Vì sao trong nghiên cứu khoa học và làm Đề án, bạn không bao giờ được để AI tự viết hoàn toàn phần 'Kết quả và Thảo luận' (Results & Discussion)?",
                        "options": [
                            "A. Vì Kết quả và Thảo luận là linh hồn và đóng góp trí tuệ cốt lõi của nhóm tác giả dựa trên dữ liệu thực tế mà nhóm thu thập/phân tích; nếu để AI tự viết, nó sẽ bịa ra các nhận định chung chung không khớp với dữ liệu thật và vi phạm vùng Đỏ của đạo đức học thuật",
                            "B. Vì phần Kết quả thường rất ngắn nên không bõ công dùng AI",
                            "C. Vì AI không biết gõ các con số thập phân",
                            "D. Vì phần Thảo luận không quan trọng trong bài báo"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L2-c8-q3",
                        "type": "mc",
                        "concept_ref": "c8-slide-4-lop",
                        "question": "Nhược điểm dễ nhận biết nhất của một bộ slide do AI (như Gamma hay Tome) tạo tự động 100% mà người học chưa biên tập lại là gì?",
                        "options": [
                            "A. Thiết kế trông có vẻ bóng bẩy ở cái nhìn đầu tiên nhưng nội dung bên trong dàn trải, chữ nghĩa chung chung sáo rỗng, các biểu đồ/hình ảnh minh họa mang tính trang trí vô hồn (stock photos) chứ không chứa bằng chứng dữ liệu thật của đề tài",
                            "B. Phông chữ luôn bị lỗi không đọc được tiếng Việt",
                            "C. Không thể xuất ra màn hình máy chiếu",
                            "D. Có quá nhiều số liệu kiểm chứng chi tiết"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L2-c8-q4",
                        "type": "mc",
                        "concept_ref": "c8-viet-4-nhip",
                        "question": "Việc dùng AI đóng vai 'Người phản biện khó tính' (Devil's Advocate) ở Nhịp 2 để soi dàn ý của bạn trước khi bạn viết chi tiết mang lại lợi ích gì?",
                        "options": [
                            "A. Giúp phát hiện sớm các bước nhảy logic thiếu căn cứ hoặc các khía cạnh bị bỏ sót ngay từ khi còn là dàn ý, giúp bạn tiết kiệm hàng giờ viết đi viết lại mà vẫn giữ trọn quyền làm chủ tư duy",
                            "B. Để AI làm nhụt chí khiến bạn bỏ cuộc",
                            "C. Để copy lời chê của AI nộp thay cho báo cáo",
                            "D. Không mang lại lợi ích gì"
                        ],
                        "correct": "A"
                    }
                ]
            },
            "level_3": {
                "name": "🚀 Level 3: Vận dụng thực tế",
                "description": "Hoàn thành Mảnh ghép 3 (Ma trận tổng hợp & Bản thảo báo cáo có trích dẫn Zotero).",
                "bloom_level": "Apply",
                "questions": [
                    {
                        "id": "L3-c8-q1",
                        "type": "mc",
                        "concept_ref": "c8-synthesis-matrix",
                        "question": "Khi nhóm bạn đã có 3 bài báo thật đã kiểm chứng: Bài 1 (Smith, 2024) và Bài 2 (Lê, 2025) đều kết luận 'Chatbot AI giúp giảm 30% chi phí vận hành ngân hàng', trong khi Bài 3 (Trần, 2026) chỉ ra 'Ở nhóm khách hàng lớn tuổi, Chatbot AI làm giảm 25% mức độ hài lòng vì thiếu sự thấu cảm'. Cách viết đoạn văn tổng hợp (Synthesis) nào dưới đây đạt chuẩn học thuật cao nhất?",
                        "options": [
                            "A. Viết 3 đoạn rời nhau: Đoạn 1 kể về Smith (2024). Đoạn 2 kể về Lê (2025). Đoạn 3 kể về Trần (2026).",
                            "B. Viết thành một luận điểm tổng hợp đối sánh: 'Mặc dù các nghiên cứu gần đây đồng thuận rằng việc triển khai Chatbot AI giúp tối ưu hóa đáng kể chi phí vận hành của ngân hàng (Lê, 2025; Smith, 2024), hiệu quả của công nghệ này không đồng nhất trên mọi phân khúc; cụ thể, ở nhóm khách hàng cao tuổi, sự thiếu hụt tương tác thấu cảm từ AI lại dẫn đến sự sụt giảm rõ rệt về mức độ hài lòng (Trần, 2026).'",
                            "C. Bỏ bài của Trần (2026) đi vì dám kết luận ngược với 2 bài kia",
                            "D. Không trích dẫn tên tác giả nào cả"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L3-c8-q2",
                        "type": "mc",
                        "concept_ref": "c8-slide-4-lop",
                        "question": "Trong bài thuyết trình bảo vệ Đề án cuối khóa ở Buổi 11 (chỉ có 8-10 phút trình bày), những minh chứng trực quan nào nhóm bạn BẮT BUỘC phải đưa lên slide để thuyết phục Hội đồng kiểm toán chéo?",
                        "options": [
                            "A. Chỉ cần đưa các hình vẽ hoạt hình AI đẹp mắt và những câu danh ngôn nổi tiếng",
                            "B. (1) Sơ đồ quy trình GATE/FALLBACK và demo sống Bộ Harness của nhóm, (2) Ma trận tổng hợp & ảnh chụp thư viện Zotero + báo cáo kiểm chứng Tomaca/Checklist 5 bước, (3) Minh chứng mạng lưới Atomic Notes trong Second Brain của từng thành viên, và (4) Bản khai báo AI theo Thông tư 49/2026",
                            "C. Copy nguyên văn 3.000 chữ trong file Word dán kín lên 10 slide chữ nhỏ li ti",
                            "D. Chỉ chiếu trang bìa rồi đọc giấy suốt 10 phút"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L3-c8-essay1",
                        "type": "essay",
                        "concept_ref": "c8-synthesis-matrix",
                        "question": "Hãy trích xuất từ Mảnh ghép 3 của Đề án nhóm bạn: (1) Bảng Ma trận Tổng hợp (Synthesis Matrix) so sánh ít nhất 3 nguồn tài liệu thật đã kiểm chứng của nhóm theo 3 tiêu chí, và (2) Viết 01 đoạn văn tổng hợp học thuật (150-200 chữ) kết nối cả 3 nguồn đó theo chuẩn trích dẫn APA 7 để chỉ ra điểm đồng thuận, khác biệt hoặc khoảng trống nghiệp vụ/nghiên cứu.",
                        "rubric": "Trình bày rõ Ma trận so sánh 3 nguồn thật đã kiểm chứng theo các tiêu chí cụ thể (40%) · Đoạn văn viết có tính tổng hợp (Synthesis) đối sánh chéo các nguồn chứ không liệt kê rời rạc (40%) · Trích dẫn trong bài đúng chuẩn APA 7 và chỉ ra được nhận định của nhóm (20%)",
                        "max_words": 400
                    }
                ]
            }
        }
    },
    {
        "chapter": 9,
        "title": "Đạo đức học thuật, Pháp lý (Thông tư 49/2026) & An toàn dữ liệu Ngân hàng",
        "sessions": [9],
        "scqa": {
            "situation": "Trong quá trình hoàn thiện Đề án và đi thực tập tại các ngân hàng, công ty chứng khoán hay doanh nghiệp, sinh viên thường xuyên tiếp xúc với bảng dữ liệu khảo sát, báo cáo nội bộ, danh sách khách hàng và các bản thảo nghiên cứu. Nhiều bạn hồn nhiên tải toàn bộ file Excel dữ liệu thật lên các công cụ AI miễn phí để nhờ vẽ biểu đồ, rồi khi nộp báo cáo cho trường thì giấu nhẹm việc mình đã dùng AI vì sợ bị trừ điểm.",
            "complication": "Tháng 1/2025, Giáo sư Jeff Hancock của ĐH Stanford (chuyên gia hàng đầu thế giới về thông tin sai lệch, nhận thù lao 600 USD/giờ) đã bị thẩm phán tòa án bang Minnesota loại bỏ toàn bộ bản khai chuyên gia vì để lọt 2 trích dẫn bịa do GPT-4o tạo ra. Tại Việt Nam, kể từ ngày 15/8/2026, Thông tư 49/2026/TT-BGDĐT (Điều 10) của Bộ Giáo dục và Đào tạo chính thức có hiệu lực: quy định rõ hành vi 'không công bố hoặc công bố không đầy đủ việc sử dụng AI khi có yêu cầu' là vi phạm liêm chính học thuật! Đồng thời, việc đưa dữ liệu cá nhân/nội bộ ngân hàng lên AI công cộng có máy chủ nước ngoài có thể vi phạm nghiêm trọng Luật Bảo vệ dữ liệu cá nhân 2025 (91/2025/QH15) và quy định bảo mật ngân hàng.",
            "question": "Đâu là ranh giới pháp lý và đạo đức rõ ràng giữa việc sử dụng AI hợp pháp và gian lận học thuật? Làm thế nào để khai báo AI đúng chuẩn và bảo vệ tuyệt đối an toàn dữ liệu trong môi trường tài chính - ngân hàng?",
            "answer": "Tuân thủ nghiêm ngặt Điều 10 Thông tư 49/2026/TT-BGDĐT và 4 nguyên tắc xuất bản quốc tế (COPE/ICMJE); áp dụng Khung Đèn giao thông (Xanh - Vàng - Đỏ) cùng Mẫu câu khai báo AI chuẩn mực; và thực thi Checklist 3 câu hỏi an toàn dữ liệu kèm kỹ thuật khử định danh (Data Anonymization) trước khi chạm vào bất kỳ công cụ AI nào."
        },
        "concepts": [
            {
                "id": "c9-thong-tu-49-phap-ly",
                "session": 9,
                "term": "Thông tư 49/2026/TT-BGDĐT (Điều 10) & Hệ thống Pháp lý AI Việt Nam",
                "definition": "Khung pháp lý bắt buộc về liêm chính học thuật và trách nhiệm con người khi ứng dụng trí tuệ nhân tạo trong học tập, nghiên cứu và công việc tại Việt Nam.",
                "key_points": [
                    "<strong>Thông tư 49/2026/TT-BGDĐT (ban hành 30/6/2026, hiệu lực 15/8/2026, Điều 10):</strong> Lần đầu tiên Bộ GD&ĐT quy định cụ thể nguyên tắc: <em>AI chỉ là công cụ hỗ trợ, không thay thế trách nhiệm học thuật của người học, nhà giáo và nhà nghiên cứu</em>.",
                    "<strong>6 nhóm hành vi vi phạm liêm chính học thuật theo Điều 10 Thông tư 49/2026:</strong> (1) Dùng công nghệ, kể cả AI, để gian lận; (2) Đạo văn, sao chép, dùng trái phép dữ liệu; (3) Giả mạo hoặc làm sai lệch dữ liệu, kết quả; (4) Nhờ người khác (hoặc để công cụ) làm thay bài học tập, nghiên cứu; (5) <strong>Không công bố hoặc công bố không đầy đủ việc dùng AI khi có yêu cầu (Khoản 2 Điểm đ)</strong>; (6) Các hành vi khác vi phạm quy chế liêm chính.",
                    "<strong>Các đạo luật liên quan trực tiếp:</strong> <strong>Luật Trí tuệ nhân tạo số 134/2025/QH15 (Điều 4)</strong> khẳng định AI không thay thế trách nhiệm pháp lý của con người; <strong>Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15</strong> kiểm soát chặt hành vi chuyển dữ liệu cá nhân xuyên biên giới khi tải dữ liệu thật lên máy chủ AI nước ngoài; và <strong>Luật Bảo vệ bí mật nhà nước số 117/2025/QH15</strong>."
                ],
                "case_study": {
                    "title": "Bài học đắt giá từ vụ Giáo sư Stanford Jeff Hancock (10/01/2025)",
                    "context": "GS. Jeff Hancock (ĐH Stanford) được thuê làm nhân chứng chuyên gia (600 USD/giờ) trong vụ kiện Kohls v. Ellison tại tòa Minnesota. Ông dùng GPT-4o hỗ trợ soạn thảo và để lọt 2 trích dẫn không tồn tại vào bản khai có tuyên thệ.",
                    "analysis": "Dù ông khẳng định mình tự viết nội dung chính và chỉ nhờ AI gợi ý chỗ chèn trích dẫn, thẩm phán vẫn bác bỏ toàn bộ giá trị lời khai chuyên gia của ông vì thiếu kiểm chứng.",
                    "lesson_learned": "Dù bạn là giáo sư đầu ngành hay sinh viên năm nhất, chữ ký của bạn dưới văn bản đồng nghĩa với việc bạn chịu 100% trách nhiệm cho mọi lỗi sai do AI tạo ra."
                },
                "related_concepts": ["c9-cope-den-giao-thong", "c9-mau-khai-bao-privacy"]
            },
            {
                "id": "c9-cope-den-giao-thong",
                "session": 9,
                "term": "Bốn nguyên tắc Quốc tế (COPE, ICMJE) & Khung Đèn giao thông (Xanh - Vàng - Đỏ)",
                "definition": "Chuẩn mực đạo đức xuất bản khoa học toàn cầu (từ COPE, ICMJE, ALLEA, WAME, Elsevier) và bảng phân vùng ranh giới thực hành hàng ngày cho sinh viên.",
                "key_points": [
                    "<strong>4 nguyên tắc quốc tế bất di bất dịch:</strong> (1) <em>AI không bao giờ được đứng tên là tác giả (No Authorship)</em> và không trích dẫn chatbot như một nguồn tài liệu khoa học vì không thể kiểm chứng; (2) <em>Công khai minh bạch cách dùng</em> ở phần Phương pháp hoặc Lời cảm ơn; (3) <em>Tác giả chịu trách nhiệm toàn bộ</em>; (4) <em>Bảo mật bản thảo khi phản biện</em> (không tải bài của người khác lên AI công cộng để nhờ nhận xét).",
                    "<strong>🟢 Vùng XANH (Nên dùng):</strong> Gợi ý từ khóa và hướng tìm kiếm; giải thích khái niệm khó để tự học; phản biện dàn ý do bạn tự lập; kiểm tra lỗi chính tả, ngữ pháp.",
                    "<strong>🟡 Vùng VÀNG (Dùng có điều kiện - Phải kiểm chứng, tự viết lại & khai báo):</strong> Dịch thuật tài liệu tham khảo (rồi đối chiếu bản gốc); gợi ý cấu trúc nháp từ Atomic Notes của bạn (rồi tự viết lại); hỗ trợ viết code thống kê R/Python/SPSS (rồi tự chạy lại trên dữ liệu thật).",
                    "<strong>🔴 Vùng ĐỎ (Cấm tuyệt đối):</strong> Để AI viết phần Kết quả, Thảo luận, Kết luận; tạo dữ liệu khảo sát giả hoặc dùng trích dẫn chưa qua 5 bước kiểm chứng; nộp văn bản do AI viết như bài của mình mà không khai báo; tải dữ liệu mật của ngân hàng/doanh nghiệp hoặc dữ liệu định danh cá nhân (PII) lên AI công cộng."
                ],
                "case_study": null,
                "related_concepts": ["c9-thong-tu-49-phap-ly", "c9-mau-khai-bao-privacy"]
            },
            {
                "id": "c9-mau-khai-bao-privacy",
                "session": 9,
                "term": "Mẫu câu Khai báo AI chuẩn mực & Bảo mật Dữ liệu Ngân hàng - Kinh tế",
                "definition": "Công thức khai báo việc sử dụng AI đáp ứng đầy đủ Điều 10 Thông tư 49/2026/TT-BGDĐT cùng bộ quy tắc bảo vệ dữ liệu nhạy cảm trong lĩnh vực tài chính - ngân hàng.",
                "key_points": [
                    "<strong>Mẫu câu khai báo việc dùng AI (đặt ở mục Phương pháp, Lời cảm ơn hoặc Phụ lục Đề án):</strong> <em>'Nhóm tác giả đã sử dụng [tên công cụ, phiên bản - ví dụ: Claude 3.7 Sonnet / Gemini Notebook] vào [tháng/năm] để [mục đích cụ thể - ví dụ: gợi ý từ khóa tìm kiếm, tóm tắt sơ bộ các bài báo PDF đã tải về và rà soát lỗi diễn đạt]. Nhóm đã tự kiểm chứng toàn bộ trích dẫn qua 5 bước, tự thực hiện toàn bộ phân tích dữ liệu và chịu trách nhiệm hoàn toàn về nội dung của báo cáo này.'</em>",
                    "<strong>Nguyên tắc vàng về Bảo mật dữ liệu:</strong> <em>'Bất kỳ dữ liệu nào bạn không dám in ra giấy dán lên bảng thông báo công cộng của toàn trường hoặc toàn ngân hàng, thì tuyệt đối không được paste nguyên bản vào các công cụ AI tài khoản cá nhân/miễn phí!'</em>",
                    "<strong>Checklist 3 câu hỏi & Kỹ thuật Khử định danh (Data Anonymization):</strong> Trước khi đưa dữ liệu vào AI, luôn hỏi: (1) Có chứa thông tin định danh cá nhân (họ tên, CCCD, số tài khoản, MSSV, bảng điểm) hay bí mật kinh doanh không? (2) Tài khoản AI đang dùng có đạt chuẩn bảo mật doanh nghiệp và tuân thủ Luật Bảo vệ dữ liệu cá nhân 2025 không? (3) Đã thực hiện <strong>khử định danh</strong> (xóa cột tên/mã số thật, thay bằng mã giả <code>KH_01</code>, hoặc chỉ gửi cấu trúc tên cột <code>schema</code> để nhờ AI viết công thức/code rồi mang công thức về máy mình tự chạy) hay chưa?"
                ],
                "case_study": null,
                "related_concepts": ["c9-thong-tu-49-phap-ly"]
            }
        ],
        "tests": {
            "level_1": {
                "name": "🎯 Level 1: Khái niệm cốt lõi",
                "description": "Nhận diện Thông tư 49/2026/TT-BGDĐT, chuẩn COPE/ICMJE, Đèn giao thông và Mẫu khai báo AI.",
                "bloom_level": "Remember",
                "questions": [
                    {
                        "id": "L1-c9-q1",
                        "type": "mc",
                        "concept_ref": "c9-thong-tu-49-phap-ly",
                        "question": "Theo Điều 10 của Thông tư 49/2026/TT-BGDĐT (ban hành ngày 30/6/2026, có hiệu lực từ 15/8/2026 của Bộ Giáo dục và Đào tạo), việc sinh viên sử dụng AI hỗ trợ làm bài nhưng KHÔNG công bố hoặc công bố không đầy đủ khi có yêu cầu được xếp vào loại hành vi nào?",
                        "options": [
                            "A. Là quyền riêng tư bình thường, được khuyến khích",
                            "B. Là hành vi vi phạm liêm chính học thuật trong hoạt động đào tạo và nghiên cứu khoa học (theo Khoản 2 Điểm đ Điều 10)",
                            "C. Chỉ là thiếu sót nhỏ về trình bày, không ảnh hưởng gì",
                            "D. Chỉ áp dụng cho giảng viên, không áp dụng cho sinh viên"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L1-c9-q2",
                        "type": "mc",
                        "concept_ref": "c9-cope-den-giao-thong",
                        "question": "Theo chuẩn mực của Ủy ban Đạo đức Xuất bản Quốc tế (COPE) và ICMJE, tại sao các công cụ AI (như ChatGPT, Claude, Gemini) KHÔNG BAO GIỜ được phép đứng tên làm đồng tác giả (co-author) của một bài báo hay đề án khoa học?",
                        "options": [
                            "A. Vì các công cụ AI không có tư cách pháp nhân và không thể chịu trách nhiệm pháp lý hay đạo đức về tính trung thực, chính xác của công trình khoa học",
                            "B. Vì tên của các công cụ AI quá ngắn",
                            "C. Vì AI chưa đóng phí xuất bản cho tạp chí",
                            "D. Vì AI không có địa chỉ email cá nhân"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L1-c9-q3",
                        "type": "mc",
                        "concept_ref": "c9-cope-den-giao-thong",
                        "question": "Trong Khung Đèn giao thông cho việc sử dụng AI trong học thuật, hành vi nào dưới đây nằm trong VÙNG ĐỎ (Cấm tuyệt đối)?",
                        "options": [
                            "A. Nhờ AI giải thích một thuật ngữ kinh tế lượng khó hiểu để tự học",
                            "B. Nhờ AI phản biện dàn ý bài viết do chính bạn tự lập",
                            "C. Để AI tự viết phần Kết quả và Thảo luận, dùng trích dẫn chưa qua kiểm chứng hoặc tải dữ liệu mật của khách hàng ngân hàng lên AI công cộng",
                            "D. Nhờ AI kiểm tra lỗi chính tả tiếng Anh sau khi bạn đã tự viết xong đoạn văn"
                        ],
                        "correct": "C"
                    },
                    {
                        "id": "L1-c9-q4",
                        "type": "mc",
                        "concept_ref": "c9-mau-khai-bao-privacy",
                        "question": "Một Bản khai báo việc sử dụng AI (AI Disclosure Statement) đạt chuẩn trong báo cáo Đề án cần nêu rõ những thông tin tối thiểu nào?",
                        "options": [
                            "A. Chỉ cần ghi một câu 'Bài này có dùng AI'",
                            "B. Nêu rõ: (1) Tên công cụ và phiên bản đã dùng, (2) Thời gian sử dụng (tháng/năm), (3) Mục đích và phạm vi công việc cụ thể đã nhờ AI hỗ trợ, và (4) Cam kết đã tự kiểm chứng toàn bộ trích dẫn/số liệu và chịu trách nhiệm 100% về nội dung bài viết",
                            "C. Nêu cấu hình phần cứng máy tính và giá tiền gói cước Internet",
                            "D. Nêu danh sách tất cả các phần mềm từng cài trong máy tính từ năm nhất"
                        ],
                        "correct": "B"
                    }
                ]
            },
            "level_2": {
                "name": "📝 Level 2: Hiểu và phân biệt",
                "description": "Phân tích ranh giới pháp lý bảo vệ dữ liệu cá nhân và nguyên tắc bảo mật khi phản biện chéo.",
                "bloom_level": "Understand",
                "questions": [
                    {
                        "id": "L2-c9-q1",
                        "type": "mc",
                        "concept_ref": "c9-thong-tu-49-phap-ly",
                        "question": "Tại sao việc một nhân viên ngân hàng hoặc sinh viên thực tập dán bảng Excel chứa Họ tên, Số CCCD, Số điện thoại và Lịch sử nợ của 500 khách hàng thật vào một Chatbot AI nước ngoài để nhờ phân loại rủi ro lại vi phạm pháp luật ngay cả khi tài khoản AI đó đã bật chế độ 'Không dùng dữ liệu để huấn luyện' (Opt-out of training)?",
                        "options": [
                            "A. Vì theo Luật Bảo vệ dữ liệu cá nhân 2025 (số 91/2025/QH15) và quy định bảo mật ngân hàng, ngay khoảnh khắc bạn truyền dữ liệu định danh cá nhân thật của khách hàng ra máy chủ nước ngoài khi chưa được phép và chưa đánh giá tác động chuyển dữ liệu xuyên biên giới, hành vi rò rỉ/chuyển giao trái phép đã xảy ra độc lập với việc hãng AI có dùng để training hay không",
                            "B. Vì bảng Excel 500 dòng quá nhỏ so với khả năng của AI",
                            "C. Vì AI nước ngoài không tính được tiền Việt Nam Đồng",
                            "D. Không hề vi phạm gì nếu đã tắt nút training"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L2-c9-q2",
                        "type": "mc",
                        "concept_ref": "c9-cope-den-giao-thong",
                        "question": "Theo nguyên tắc thứ 4 của COPE/ICMJE/Elsevier về 'Bảo mật bản thảo khi phản biện', điều gì bạn cần lưu ý khi thực hiện Kiểm toán chéo (Peer Audit) đề án của nhóm bạn hoặc khi phản biện bài báo khoa học?",
                        "options": [
                            "A. Không được phép tự ý tải toàn bộ tài liệu chưa công bố hoặc dữ liệu nhạy cảm của tác giả khác lên các công cụ AI công cộng bên ngoài khi chưa có sự đồng ý hoặc chưa khử định danh, nhằm bảo vệ quyền sở hữu trí tuệ và bảo mật của nhóm tác giả",
                            "B. Được phép đăng bài của nhóm bạn lên mạng xã hội để nhờ cư dân mạng chấm hộ",
                            "C. Không cần đọc bài của nhóm bạn mà chỉ cần chấm điểm ngẫu nhiên",
                            "D. Phải xóa tên tác giả của nhóm bạn rồi nộp thành bài của nhóm mình"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L2-c9-q3",
                        "type": "mc",
                        "concept_ref": "c9-cope-den-giao-thong",
                        "question": "Tại sao khuyến nghị của ICMJE lại quy định: 'Không đưa Chatbot tổng quát (như ChatGPT) vào Danh mục tài liệu tham khảo (References) như một nguồn khoa học'?",
                        "options": [
                            "A. Vì văn bản do Chatbot sinh ra biến thiên theo xác suất ở từng phiên chat của từng người, người đọc khác không thể truy xuất và kiểm chứng lại nguồn đó như một bài báo có DOI cố định; do đó việc dùng AI phải được ghi ở mục Phương pháp hoặc Lời cảm ơn/Khai báo AI chứ không phải mục Tài liệu tham khảo",
                            "B. Vì tên ChatGPT khó viết theo chuẩn APA",
                            "C. Vì ICMJE muốn giấu việc các nhà khoa học dùng AI",
                            "D. Vì danh mục tài liệu tham khảo chỉ cho phép tối đa 5 bài"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L2-c9-q4",
                        "type": "mc",
                        "concept_ref": "c9-thong-tu-49-phap-ly",
                        "question": "Sự tương đồng cốt lõi nhất giữa Thông tư 49/2026/TT-BGDĐT của Việt Nam, Luật AI 134/2025/QH15, EU AI Act (Điều 50) và tuyên bố của COPE/ICMJE là gì?",
                        "options": [
                            "A. Tất cả đều cấm sinh viên và nhà nghiên cứu sử dụng AI dưới mọi hình thức",
                            "B. Tất cả đều hội tụ về 2 trụ cột: (1) Minh bạch (dùng AI ở đâu phải công khai, khai báo rõ ràng ở đó) và (2) Trách nhiệm giải trình thuộc về con người (AI chỉ là công cụ hỗ trợ, con người chịu trách nhiệm 100% về tính chính xác và trung thực của sản phẩm)",
                            "C. Tất cả đều cho phép AI đứng tên làm tác giả chính",
                            "D. Tất cả đều quy định chỉ được dùng một hãng AI duy nhất"
                        ],
                        "correct": "B"
                    }
                ]
            },
            "level_3": {
                "name": "🚀 Level 3: Vận dụng thực tế",
                "description": "Xử lý tình huống khử định danh dữ liệu ngân hàng và viết Bản khai báo AI cho Đề án (Mảnh ghép 4).",
                "bloom_level": "Apply",
                "questions": [
                    {
                        "id": "L3-c9-q1",
                        "type": "mc",
                        "concept_ref": "c9-mau-khai-bao-privacy",
                        "question": "Bạn đang có một file Excel dữ liệu thật gồm 2.000 hồ sơ vay vốn tại một chi nhánh ngân hàng (có cột Họ tên, CCCD, Thu nhập, Dư nợ, Nhóm nợ) và bạn muốn nhờ AI viết đoạn code Python/R để chạy mô hình hồi quy Logistic dự báo nợ xấu. Cách làm nào dưới đây vừa khai thác được AI tối đa, vừa đảm bảo AN TOÀN DỮ LIỆU tuyệt đối?",
                        "options": [
                            "A. Tải thẳng file Excel 2.000 khách hàng thật đó lên ChatGPT miễn phí và bảo 'Hãy chạy hồi quy giúp tôi'",
                            "B. Tuyệt đối không tải file dữ liệu thật lên AI; chỉ mô tả cho AI cấu trúc tên các cột (schema) cùng kiểu dữ liệu (hoặc tạo 5 dòng dữ liệu giả lập hoàn toàn), nhờ AI viết đoạn code Python/R, sau đó copy đoạn code đó về máy tính cá nhân của mình để tự chạy offline trên file dữ liệu thật và tự kiểm tra kết quả",
                            "C. Chỉ xóa cột Họ tên, giữ nguyên cột số CCCD và số điện thoại thật rồi tải lên AI công cộng",
                            "D. Chụp ảnh màn hình danh sách khách hàng rồi gửi lên AI"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L3-c9-q2",
                        "type": "mc",
                        "concept_ref": "c9-cope-den-giao-thong",
                        "question": "Nhóm bạn sử dụng công cụ 'AI Detector' (phần mềm phát hiện văn bản do AI viết) để quét thử một đoạn văn của thành viên trong nhóm và thấy máy báo '85% khả năng do AI viết'. Theo tinh thần khoa học và hướng dẫn học thuật hiện đại, nhóm nên xử lý kết quả này như thế nào?",
                        "options": [
                            "A. Kết luận ngay lập tức bạn đó gian lận 100% vì máy quét không bao giờ sai",
                            "B. Hiểu rằng các công cụ AI Detector hiện nay có tỷ lệ dương tính giả và âm tính giả rất cao, không được coi là bằng chứng kết tội duy nhất; thay vào đó, nhóm phải kiểm tra xem thành viên đó có chuỗi Atomic Notes quá trình trong Second Brain không, có hiểu sâu để giải thích miệng được đoạn văn đó không, và các nguồn trích dẫn trong đoạn đó có qua 5 bước kiểm chứng trong Zotero hay không",
                            "C. Dùng một công cụ AI khác để xào nấu chữ nghĩa (paraphrase) nhằm qua mặt máy quét mà không cần hiểu nội dung",
                            "D. Xóa bỏ đoạn văn đó mà không cần hỏi tác giả"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L3-c9-essay1",
                        "type": "essay",
                        "concept_ref": "c9-mau-khai-bao-privacy",
                        "question": "Hãy soạn thảo hoàn chỉnh Mảnh ghép 4 cho Đề án cuối khóa của nhóm bạn gồm 2 phần: (1) Bảng phân loại Đèn giao thông (Xanh - Vàng - Đỏ) và quy trình khử định danh/bảo mật đối với các dữ liệu mà nhóm sử dụng trong Đề án; (2) Bản Khai báo Sử dụng AI (AI Disclosure Statement) chính thức của nhóm tuân thủ đúng Điều 10 Thông tư 49/2026/TT-BGDĐT và chuẩn COPE/ICMJE.",
                        "rubric": "Phân loại rõ 3 vùng Xanh - Vàng - Đỏ gắn sát với dữ liệu và tác vụ thực tế của Đề án nhóm (35%) · Nêu rõ biện pháp khử định danh/bảo mật dữ liệu (25%) · Bản khai báo AI đầy đủ tên công cụ, phiên bản, thời gian, mục đích từng bước và lời cam kết chịu trách nhiệm theo Thông tư 49/2026 (40%)",
                        "max_words": 400
                    }
                ]
            }
        }
    },
    {
        "chapter": 10,
        "title": "Project Clinic & Studio Kiểm toán chéo (Peer Audit Studio)",
        "sessions": [10],
        "scqa": {
            "situation": "Sau 9 buổi học, các nhóm đều đã lắp ghép đủ 4 Mảnh ghép của Hồ sơ Đề án cuối khóa (Bộ Harness nghiệp vụ, Kho Second Brain + RAG, Báo cáo nghiên cứu có Zotero đã kiểm chứng, và Bản khai báo AI theo Thông tư 49/2026). Ai cũng tin rằng hồ sơ của nhóm mình đã hoàn hảo.",
            "complication": "Trong thực tế nghiên cứu và làm việc, 'điểm mù của tác giả' khiến chúng ta rất dễ bỏ sót một lỗi suy diễn tinh vi của AI, một lỗ hổng trong cổng dừng GATE của bộ Harness, hoặc một trích dẫn bị lệch năm xuất bản. Mặt khác, ở các lớp học thông thường, hoạt động 'nhận xét chéo giữa các nhóm' thường diễn ra rất hình thức: sinh viên chỉ khen nhau xã giao ('Nhóm bạn làm đẹp lắm') để cả làng cùng vui, khiến hoạt động phản biện mất đi giá trị học thuật.",
            "question": "Làm thế nào để biến buổi rà soát cuối khóa thành một 'Phiên Kiểm toán Học thuật' (Academic Red-Teaming / Peer Audit) thực chất, giúp từng nhóm phát hiện và vá sạch mọi lỗ hổng trước giờ bảo vệ, đồng thời đo lường chính xác năng lực thẩm định AI của sinh viên?",
            "answer": "Áp dụng cơ chế Kiểm toán chéo có tính điểm (15% trọng số cuối khóa tính vào năng lực 'soi' lỗi của Hội đồng Kiểm toán): mỗi nhóm dùng chính bộ công cụ đã học (Stress-test 3 kịch bản cho Harness, Tomaca + Checklist 5 bước + Kỹ thuật Soi 3 phút cho danh mục trích dẫn, và Rubric Thông tư 49/2026) để lập Báo cáo Kiểm toán độc lập cho nhóm đối tác."
        },
        "concepts": [
            {
                "id": "c10-peer-audit-redteam",
                "session": 10,
                "term": "Phương pháp Kiểm toán chéo Học thuật (Peer Audit & AI Red-Teaming)",
                "definition": "Quy trình thẩm định đồng đẳng có cấu trúc, trong đó một nhóm sinh viên đóng vai trò 'Kiểm toán viên độc lập' (Auditor / Red Team) sử dụng các tiêu chuẩn kỹ thuật để kiểm thử độ tin cậy của bộ Harness và tính xác thực của toàn bộ nguồn dữ liệu trong Đề án của nhóm khác.",
                "key_points": [
                    "<strong>Khác biệt với nhận xét xã giao:</strong> Điểm số của Nhóm Kiểm toán (15% tổng điểm môn học) không phụ thuộc vào việc khen hay chê cảm tính, mà được chấm dựa trên <em>độ chính xác, bằng chứng cụ thể và tính xây dựng</em> trong Biên bản Kiểm toán mà nhóm lập ra.",
                    "<strong>Tinh thần Phản biện Xây dựng (Từ Bi & Chân Thật):</strong> Mục tiêu của Kiểm toán chéo không phải là 'dìm điểm' bạn, mà là giúp nhóm bạn phát hiện ra những 'quả bom nổ chậm' (trích dẫn lỗi, Harness bị lọt cổng GATE) ngay tại Buổi 10 để kịp khắc phục trước khi bước lên bục bảo vệ chính thức ở Buổi 11.",
                    "<strong>Học sâu qua vai trò người thẩm định:</strong> Khi bạn tự tay đi 'soi' 10 trích dẫn và bộ Harness của nhóm khác, kỹ năng kiểm chứng của chính bạn sẽ đạt tới mức phản xạ tự nhiên (bậc Đánh giá - Evaluate cao nhất của thang Bloom)."
                ],
                "case_study": {
                    "title": "Phát hiện lỗi lệch bảng số liệu nhờ Kiểm toán chéo",
                    "context": "Trong phiên Peer Audit, Nhóm Kiểm toán B bốc ngẫu nhiên trích dẫn số 4 trong báo cáo của Nhóm A, mở file PDF gốc đối chiếu (Bước 3 & 4) và phát hiện AI của Nhóm A đã lấy nhầm cột số liệu năm 2022 thành năm 2024.",
                    "analysis": "Nhờ phát hiện này ở Buổi 10, Nhóm A kịp sửa lại số liệu đúng trước khi bảo vệ chính thức, còn Nhóm B đạt điểm tối đa cho phần năng lực Kiểm toán.",
                    "lesson_learned": "Một người bạn kiểm toán nghiêm khắc là món quà quý giá nhất trong học thuật."
                },
                "related_concepts": ["c10-audit-harness-zotero"]
            },
            {
                "id": "c10-audit-harness-zotero",
                "session": 10,
                "term": "Quy trình 3 Vòng Kiểm toán Hồ sơ Đề án Ứng dụng AI",
                "definition": "Checklist chuẩn hóa gồm 3 vòng kiểm tra kỹ thuật mà Hội đồng Kiểm toán chéo thực hiện trong 120 phút tại Studio Buổi 10.",
                "key_points": [
                    "<strong>Vòng 1 - Kiểm toán Bộ Harness & Second Brain (Mảnh ghép 1 & 2):</strong> Nhập 3 kịch bản test vào bộ Harness của nhóm bạn: (a) Dữ liệu chuẩn, (b) Dữ liệu thiếu một biến trọng yếu xem FALLBACK có kích hoạt không, (c) Ra lệnh ép AI bỏ qua GATE xem Harness có chặn đứng được không. Kiểm tra xem mỗi thành viên có đủ >= 6 Atomic Notes viết bằng ngôn từ riêng hay không.",
                    "<strong>Vòng 2 - Kiểm toán Nguồn trích dẫn & Số liệu (Mảnh ghép 3):</strong> Đưa toàn bộ danh mục tài liệu tham khảo của nhóm bạn lên <strong>Tomaca</strong> để quét tự động; sau đó chọn ngẫu nhiên <strong>03 trích dẫn cốt lõi</strong> để mở bản PDF gốc thực hiện đầy đủ <strong>Checklist 5 bước</strong> và <strong>Soi 3 phút</strong> (đối chiếu tận dòng và bảng số liệu).",
                    "<strong>Vòng 3 - Kiểm toán An toàn dữ liệu & Khai báo AI (Mảnh ghép 4):</strong> Đối chiếu xem báo cáo có làm lộ dữ liệu định danh chưa khử mật không, và Bản khai báo AI đã đáp ứng đủ các yếu tố của Điều 10 Thông tư 49/2026/TT-BGDĐT chưa."
                ],
                "case_study": null,
                "related_concepts": ["c10-peer-audit-redteam"]
            }
        ],
        "tests": {
            "level_1": {
                "name": "🎯 Level 1: Khái niệm cốt lõi",
                "description": "Nắm vững cấu trúc Hồ sơ Đề án 4 mảnh ghép và quy trình Kiểm toán chéo 3 vòng.",
                "bloom_level": "Remember",
                "questions": [
                    {
                        "id": "L1-c10-q1",
                        "type": "mc",
                        "concept_ref": "c10-audit-harness-zotero",
                        "question": "Bộ Hồ sơ Đề án Ứng dụng AI hoàn chỉnh nộp ở Buổi 10 bao gồm 4 Mảnh ghép lũy tiến nào?",
                        "options": [
                            "A. (1) Thiết kế Kiến trúc AI & Bộ Harness nghiệp vụ; (2) Hệ thống Second Brain (Atomic Notes cá nhân) & Kho RAG; (3) Báo cáo nghiên cứu/nghiệp vụ có Ma trận tổng hợp & Trích dẫn Zotero đã kiểm chứng; (4) Hồ sơ An toàn dữ liệu & Bản khai báo AI theo Thông tư 49/2026",
                            "B. Chỉ gồm 1 file trình chiếu PowerPoint 5 trang không có tài liệu tham khảo",
                            "C. Chỉ gồm ảnh chụp màn hình 1 câu hỏi trên ChatGPT",
                            "D. Gồm 1 bài văn chép tay không dùng máy tính"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L1-c10-q2",
                        "type": "mc",
                        "concept_ref": "c10-peer-audit-redteam",
                        "question": "Trong cơ cấu 100% điểm đánh giá cuối khóa của môn học, hoạt động 'Thuyết trình, Phản biện & Kiểm toán chéo giữa các nhóm (Peer Audit)' chiếm tổng trọng số là bao nhiêu?",
                        "options": [
                            "A. 0% (không tính điểm)",
                            "B. 30% tổng điểm cuối khóa (gồm 15% điểm Thuyết trình & trả lời bảo vệ đề án của nhóm mình + 15% điểm năng lực Kiểm toán chéo & phản biện đề án của nhóm bạn)",
                            "C. 5%",
                            "D. 100%"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L1-c10-q3",
                        "type": "mc",
                        "concept_ref": "c10-audit-harness-zotero",
                        "question": "Ở Vòng 2 của quy trình Kiểm toán chéo (Kiểm toán Nguồn trích dẫn & Số liệu), bên cạnh việc quét toàn bộ danh mục bằng công cụ Tomaca, Nhóm Kiểm toán bắt buộc phải làm thêm thao tác thủ công nào?",
                        "options": [
                            "A. Không cần làm gì thêm, tin tuyệt đối 100% vào màu xanh của Tomaca",
                            "B. Chọn ít nhất 03 trích dẫn trọng yếu trong bài của nhóm bạn để mở file PDF bản gốc, thực hiện đầy đủ Checklist 5 bước (đặc biệt là Bước 3 và Bước 4 xem bài gốc có nói đúng luận điểm và khớp số liệu bảng/hình hay không)",
                            "C. Xóa bớt tài liệu tham khảo của nhóm bạn",
                            "D. Đổi tên tác giả trong bài của nhóm bạn"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L1-c10-q4",
                        "type": "mc",
                        "concept_ref": "c10-audit-harness-zotero",
                        "question": "Theo 'Quy tắc Điểm liệt Liêm chính' (Zero-Tolerance Integrity Rule) của môn học, hậu quả gì sẽ xảy ra nếu trong Hồ sơ Đề án chính thức bị phát hiện có trích dẫn bịa (fabricated citation) hoặc không khai báo AI theo Thông tư 49/2026?",
                        "options": [
                            "A. Được cộng thêm điểm khuyến khích",
                            "B. Bị trừ thẳng 50% tổng điểm Cấu phần 1 (Hồ sơ Đề án nhóm) và bắt buộc phải rà soát, khắc phục lại toàn bộ phần kiểm chứng mới được xét đạt chứng chỉ",
                            "C. Không bị ảnh hưởng gì đến điểm số",
                            "D. Chỉ bị nhắc nhở nhẹ"
                        ],
                        "correct": "B"
                    }
                ]
            },
            "level_2": {
                "name": "📝 Level 2: Hiểu và phân biệt",
                "description": "Hiểu phương pháp Stress-test bộ Harness và cách viết Biên bản Kiểm toán văn minh, dựa trên bằng chứng.",
                "bloom_level": "Understand",
                "questions": [
                    {
                        "id": "L2-c10-q1",
                        "type": "mc",
                        "concept_ref": "c10-audit-harness-zotero",
                        "question": "Khi Kiểm toán Bộ Harness của nhóm bạn ở Vòng 1, tại sao bạn không nên chỉ thử nghiệm bằng một dữ liệu đẹp và đầy đủ (happy path)?",
                        "options": [
                            "A. Vì một bộ Harness yếu và một câu Prompt sơ sài đều có thể trả lời tốt khi dữ liệu đầu vào hoàn hảo; bản lĩnh thực sự của một bộ Harness chỉ lộ diện khi bị thử thách bằng tình huống biên (thiếu dữ liệu để xem FALLBACK có dừng lại hỏi không, và giục vượt rào xem GATE có giữ vững kỷ luật không)",
                            "B. Vì dữ liệu đầy đủ làm máy tính chạy chậm",
                            "C. Vì mục tiêu của kiểm toán là phá hỏng máy tính của nhóm bạn",
                            "D. Vì AI không đọc được dữ liệu đầy đủ"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L2-c10-q2",
                        "type": "mc",
                        "concept_ref": "c10-peer-audit-redteam",
                        "question": "Nhận xét kiểm toán chéo nào dưới đây thể hiện đúng nhất tinh thần học thuật chuyên nghiệp, có bằng chứng xác thực và mang tính xây dựng?",
                        "options": [
                            "A. 'Nhóm bạn làm bài tốt lắm, slide đẹp, nhóm mình chấm 10/10 không có góp ý gì thêm.'",
                            "B. 'Bài của nhóm bạn dở quá, chắc chắn là nhờ AI viết hết rồi.'",
                            "C. 'Qua kiểm toán Vòng 2, nhóm mình xác nhận 10/11 trích dẫn của nhóm bạn khớp hoàn toàn trên Tomaca và bản PDF gốc. Tuy nhiên, ở trích dẫn số 7 (Phạm, 2025, tr.12), bảng gốc của tác giả ghi tỷ lệ chấp nhận là 64.2% trên mẫu N=310, nhưng trong trang 8 báo cáo của nhóm bạn đang ghi là 74.2%. Đề nghị nhóm kiểm tra và đính chính lại con số này trước buổi bảo vệ.'",
                            "D. 'Nhóm mình không thích màu xanh trên trang bìa báo cáo của nhóm bạn.'"
                        ],
                        "correct": "C"
                    },
                    {
                        "id": "L2-c10-q3",
                        "type": "mc",
                        "concept_ref": "c10-audit-harness-zotero",
                        "question": "Làm thế nào để Nhóm Kiểm toán phân biệt được một Atomic Note cá nhân do sinh viên tự tư duy đúc kết với một ghi chú do copy-paste đối phó từ AI?",
                        "options": [
                            "A. Atomic Note thực chất có tiêu đề là một câu khẳng định sắc gọn, nội dung cô đọng (100-200 chữ) gắn chặt với bối cảnh bài toán của nhóm, có liên kết [[...]] hợp lý tới các ghi chú khác và người viết có thể giải thích ngay lập tức ý nghĩa của nó mà không cần nhìn màn hình",
                            "B. Ghi chú nào dài trên 3.000 chữ và có nhiều biểu tượng cảm xúc (emoji) đầu dòng của ChatGPT là ghi chú tốt nhất",
                            "C. Không thể phân biệt được bằng bất kỳ cách nào",
                            "D. Chỉ nhìn vào ngày giờ tạo file"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L2-c10-q4",
                        "type": "mc",
                        "concept_ref": "c10-peer-audit-redteam",
                        "question": "Sau khi nhận được Biên bản Kiểm toán chéo từ nhóm đối tác ở cuối Buổi 10, thái độ và hành động đúng đắn nhất của nhóm sở hữu Đề án là gì?",
                        "options": [
                            "A. Tranh cãi gay gắt để phủ nhận mọi lỗi sai dù bằng chứng PDF gốc đã rõ ràng",
                            "B. Đón nhận các phát hiện kiểm toán như một cơ hội quý báu để hoàn thiện sản phẩm: lập tức đối chiếu lại với nguồn gốc, vá lại các lỗ hổng trong câu lệnh GATE/FALLBACK của bộ Harness, sửa lại các trích dẫn lệch và chuẩn bị slide giải trình rõ những gì nhóm đã nâng cấp cho buổi Bảo vệ ở Buổi 11",
                            "C. Bỏ mặc không sửa gì cả",
                            "D. Tìm cách trả đũa bằng cách chấm điểm thấp vô căn cứ cho nhóm bạn"
                        ],
                        "correct": "B"
                    }
                ]
            },
            "level_3": {
                "name": "🚀 Level 3: Vận dụng thực tế",
                "description": "Thực hiện Biên bản Kiểm toán chéo 3 vòng tại Studio Buổi 10.",
                "bloom_level": "Apply",
                "questions": [
                    {
                        "id": "L3-c10-q1",
                        "type": "mc",
                        "concept_ref": "c10-audit-harness-zotero",
                        "question": "Trong lúc kiểm toán Mảnh ghép 3 của nhóm đối tác, bạn thấy nhóm bạn có đính kèm file thư viện Zotero (`.bib`/`.ris`), nhưng trong file Word báo cáo lại có 3 trích dẫn ở phần Thảo luận không hề nằm trong file Zotero đó và cũng không có trong Danh mục tài liệu tham khảo cuối bài. Phát hiện này cho thấy điều gì?",
                        "options": [
                            "A. Nhóm đối tác đã vi phạm quy trình 'Nguồn vào Zotero trước, vào bài sau' ở phần Thảo luận (rất có thể đã copy-paste trực tiếp một đoạn văn do AI sinh ra kèm trích dẫn trôi nổi vào bài mà quên kiểm chứng và nạp Zotero); cần yêu cầu nhóm đối tác kiểm chứng 5 bước hoặc loại bỏ ngay 3 trích dẫn đó",
                            "B. Đó là cách trích dẫn sáng tạo mới, không cần sửa",
                            "C. Chỉ cần xóa file Zotero đi là xong",
                            "D. Không cần ghi vào biên bản kiểm toán"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L3-c10-q2",
                        "type": "mc",
                        "concept_ref": "c10-audit-harness-zotero",
                        "question": "Khi kiểm toán Mảnh ghép 4 (Hồ sơ An toàn dữ liệu & Đạo đức AI) của một nhóm làm đề tài 'Ứng dụng AI phân tích phản hồi khách hàng trên fanpage Ngân hàng X', bạn thấy nhóm đã xóa toàn bộ tên và số điện thoại khách hàng trong file bình luận mẫu trước khi đưa vào Claude Project, đồng thời có Bản khai báo AI nêu rõ phiên bản Claude, thời gian và các prompt đã dùng. Đánh giá kiểm toán đúng cho Mảnh ghép 4 này là gì?",
                        "options": [
                            "A. Đạt mức Xuất sắc (8.5 - 10 điểm): nhóm đã thực hiện đúng kỹ thuật khử định danh dữ liệu cá nhân (Data Anonymization) và tuân thủ đầy đủ nghĩa vụ công bố minh bạch theo Điều 10 Thông tư 49/2026/TT-BGDĐT",
                            "B. Không đạt vì lẽ ra phải giữ nguyên số điện thoại thật của khách hàng",
                            "C. Không đạt vì đã dùng Claude Project",
                            "D. Không đạt vì khai báo quá chi tiết"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L3-c10-essay1",
                        "type": "essay",
                        "concept_ref": "c10-audit-harness-zotero",
                        "question": "Hãy tóm tắt 'Biên bản Kiểm toán chéo (Peer Audit Report)' mà nhóm bạn đã thực hiện đối với Hồ sơ Đề án của nhóm đối tác tại Buổi 10 theo 3 vòng: (1) Kết quả stress-test Bộ Harness & đánh giá Second Brain của nhóm bạn; (2) Kết quả quét Tomaca và đối chiếu Checklist 5 bước trên 3 trích dẫn PDF gốc của nhóm bạn; (3) Đánh giá Bản khai báo AI theo Thông tư 49/2026 và 02 câu hỏi chất vấn sắc bén nhất bạn sẽ đặt cho nhóm đó tại Hội đồng Buổi 11.",
                        "rubric": "Báo cáo rõ kết quả test 3 kịch bản trên bộ Harness của nhóm bạn (25%) · Nêu bằng chứng cụ thể từ việc quét Tomaca và mở 3 bài báo gốc đối chiếu theo Checklist 5 bước (35%) · Đánh giá chính xác mức độ tuân thủ Thông tư 49/2026 và bảo mật dữ liệu (20%) · Đặt được 2 câu hỏi phản biện sâu sắc, mang tính xây dựng cho buổi bảo vệ (20%)",
                        "max_words": 450
                    }
                ]
            }
        }
    },
    {
        "chapter": 11,
        "title": "Bảo vệ Đề án cuối khóa (Capstone Showcase), Phản biện & Tổng kết hành trình",
        "sessions": [11],
        "scqa": {
            "situation": "Hôm nay là Buổi 11 - buổi học cuối cùng khép lại chặng đường 44 tiết của học phần 'Kỹ năng ứng dụng AI trong học tập và nghiên cứu'. Các nhóm bước lên bục bảo vệ Đề án cuối khóa trước Giảng viên và Hội đồng Kiểm toán chéo để nhận đánh giá tổng kết 100% điểm công nhận Chứng chỉ chuẩn đầu ra.",
            "complication": "Một tấm chứng chỉ in trên giấy chỉ giúp bạn đủ điều kiện hành chính để tốt nghiệp. Nhưng ngay ngày mai, khi bạn bước ra khỏi giảng đường để làm khóa luận tốt nghiệp hay đi làm tại các ngân hàng, định chế tài chính, các mô hình AI sẽ lại tiếp tục nâng cấp lên những phiên bản mới mạnh hơn, cám dỗ làm thay con người sẽ càng lớn hơn, và rủi ro đánh mất năng lực tư duy độc lập vẫn luôn rình rập.",
            "question": "Làm thế nào để phần bảo vệ Đề án hôm nay thực sự tỏa sáng bản lĩnh của một 'Người làm chủ AI', và đâu là hệ thống nguyên tắc cốt lõi bạn sẽ mang theo suốt sự nghiệp sau khi khóa học này khép lại?",
            "answer": "Tự tin chứng minh sự kết hợp nhuần nhuyễn giữa Tư duy - Kỹ năng - Công cụ qua màn Live Demo bộ Harness, hệ thống Second Brain và hồ sơ nghiên cứu 100% nguồn thật trong Zotero; đồng thời khắc sâu 3 nguyên tắc trọn đời: 'Nguồn thật trước, AI sau', 'Chưa kiểm chứng, chưa vào bài', và 'Dùng AI thì khai báo - AI là trợ lý, bạn là chủ'."
        },
        "concepts": [
            {
                "id": "c11-capstone-defense",
                "session": 11,
                "term": "Nghệ thuật Bảo vệ Đề án & Vấn đáp Cá nhân (Capstone Showcase & Viva)",
                "definition": "Cấu trúc phiên bảo vệ 20 phút giúp nhóm trình bày trọn vẹn giá trị của 4 Mảnh ghép Đề án và giúp từng thành viên chứng minh năng lực làm chủ thực chất (30% điểm cá nhân).",
                "key_points": [
                    "<strong>1. Trình bày & Live Demo (8-10 phút):</strong> Đi thẳng vào bài toán nghiệp vụ theo khung SCQA -> Chiếu sơ đồ phân vai và <strong>Live Demo bộ Harness</strong> (chứng minh GATE và FALLBACK hoạt động thật) -> Trình bày Ma trận tổng hợp, kết quả kiểm chứng nguồn Zotero/Tomaca và giải pháp đề xuất -> Chiếu Bản khai báo AI theo Thông tư 49/2026.",
                    "<strong>2. Tranh biện cùng Hội đồng Kiểm toán chéo (5-6 phút):</strong> Lắng nghe nhóm Kiểm toán công bố kết quả rà soát; giải trình ngắn gọn, thẳng thắn dựa trên bằng chứng gốc và chỉ rõ những điểm nhóm đã nâng cấp sau phiên Peer Audit Buổi 10.",
                    "<strong>3. Vấn đáp chỉ định cá nhân (5-6 phút - Chiếm 30% tổng điểm):</strong> Giảng viên chỉ định bất kỳ thành viên nào giải thích một Atomic Note trong Second Brain, tự tay thực hiện thao tác 'Soi 3 phút' hoặc tra cứu một trích dẫn trong thư viện Zotero ngay trên bục giảng."
                ],
                "case_study": null,
                "related_concepts": ["c11-ba-dieu-mang-ve"]
            },
            {
                "id": "c11-ba-dieu-mang-ve",
                "session": 11,
                "term": "Ba Nguyên tắc Vàng mang theo suốt sự nghiệp Học tập, Nghiên cứu & Làm việc",
                "definition": "Bản đúc kết tối hậu của 44 tiết học, giúp sinh viên Đại học Ngân hàng TP.HCM luôn giữ vững vị thế người làm chủ dù công nghệ AI có thay đổi nhanh đến đâu trong 10 hay 20 năm tới.",
                "key_points": [
                    "<strong>Nguyên tắc 1 - Tư duy -> Kỹ năng -> Công cụ (Với Second Brain & Harness là bệ phóng):</strong> Công cụ AI sẽ thay đổi mỗi quý, nhưng năng lực tư duy phân vai, kỹ năng thiết kế Prompt - Context - Harness và kho tri thức nguyên tử trong Bộ Não Thứ Hai (Second Brain) là tài sản trí tuệ đi theo bạn suốt đời.",
                    "<strong>Nguyên tắc 2 - Nguồn thật trước, AI sau & Chưa kiểm chứng, chưa vào bài:</strong> Tìm trong kho tài liệu thật (Semantic Scholar, Elicit, Consensus), đọc có đối chiếu ('Soi 3 phút'), và mỗi trích dẫn bắt buộc phải đi qua <strong>5 bước kiểm chứng + vào thư viện Zotero</strong> trước khi được phép xuất hiện trong bất kỳ báo cáo hay khóa luận nào của bạn.",
                    "<strong>Nguyên tắc 3 - Dùng AI thì khai báo & Bảo mật dữ liệu tuyệt đối:</strong> Nêu rõ công cụ, phiên bản và mục đích theo đúng Điều 10 Thông tư 49/2026/TT-BGDĐT; khử định danh mọi dữ liệu nhạy cảm của khách hàng/ngân hàng trước khi đưa vào AI. <em>Làm chủ không có nghĩa là không dùng AI, mà là biết mình đang giao việc gì, kiểm tra lại thế nào và luôn sẵn sàng đàng hoàng đứng tên dưới kết quả!</em>"
                ],
                "case_study": {
                    "title": "Hành trình trưởng thành của Minh tại ĐH Ngân hàng TP.HCM",
                    "context": "Từ một sinh viên năm 2 lúng túng vì nộp bài tiểu luận copy từ ChatGPT bị 6 điểm ở Buổi 1, đến Buổi 11 Minh đã sở hữu một hệ thống Second Brain hơn 50 Atomic Notes ngành Tài chính - Ngân hàng, một bộ Harness trợ lý phân tích tín dụng có cổng GATE chặt chẽ, một thư viện Zotero sạch 100% trích dẫn bịa và phong thái đĩnh đạc khi bảo vệ đề án.",
                    "analysis": "Sự khác biệt không nằm ở việc Minh mua tài khoản AI đắt tiền hơn, mà nằm ở sự chuyển hóa từ người tiêu thụ thụ động sang người kiến tạo có hệ thống.",
                    "lesson_learned": "AI là bệ phóng, còn trí tuệ, đạo đức và cái tâm của bạn mới là người bay."
                },
                "related_concepts": ["c11-capstone-defense"]
            }
        ],
        "tests": {
            "level_1": {
                "name": "🎯 Level 1: Tổng kết Khái niệm cốt lõi toàn khóa",
                "description": "Ôn tập bức tranh tổng thể 4 Module của học phần Kỹ năng ứng dụng AI.",
                "bloom_level": "Remember",
                "questions": [
                    {
                        "id": "L1-c11-q1",
                        "type": "mc",
                        "concept_ref": "c11-ba-dieu-mang-ve",
                        "question": "Triết lý sư phạm cốt lõi xuyên suốt 11 buổi (44 tiết) của học phần này được sắp xếp theo trật tự ưu tiên nào?",
                        "options": [
                            "A. Công cụ -> Mẹo bấm nút -> Sao chép nhanh",
                            "B. Tư duy (Hiểu bản chất xác suất & vị thế làm chủ) -> Kỹ năng (Prompt-Context-Harness, Second Brain, Kiểm chứng NCKH, Đạo đức & Bảo mật) -> Công cụ (Chọn đúng công cụ cho đúng việc)",
                            "C. Học thuộc lòng tên các phần mềm AI",
                            "D. Giao toàn bộ việc học cho AI tự động hóa"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L1-c11-q2",
                        "type": "mc",
                        "concept_ref": "c11-ba-dieu-mang-ve",
                        "question": "Ba thông điệp hành động cốt lõi trong nghiên cứu khoa học có AI đồng hành mà sinh viên cần ghi nhớ suốt đời là gì?",
                        "options": [
                            "A. (1) Nguồn thật trước, AI sau; (2) Chưa kiểm chứng (5 bước + Zotero), chưa vào bài; và (3) Dùng AI thì khai báo (theo Thông tư 49/2026) - Bạn chịu trách nhiệm toàn bộ nội dung",
                            "B. (1) AI tìm nguồn trước; (2) Chép thẳng vào bài; (3) Giấu việc dùng AI",
                            "C. (1) Chỉ dùng 1 công cụ duy nhất; (2) Không cần đọc bài báo gốc; (3) Để AI đứng tên đồng tác giả",
                            "D. Không bao giờ sử dụng máy tính khi làm nghiên cứu"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L1-c11-q3",
                        "type": "mc",
                        "concept_ref": "c11-capstone-defense",
                        "question": "Trong phiên Bảo vệ Đề án cuối khóa ở Buổi 11, phần Vấn đáp chỉ định cá nhân (chiếm 30% tổng điểm cuối khóa của từng sinh viên) nhằm mục đích chính là gì?",
                        "options": [
                            "A. Kiểm tra xem sinh viên có thuộc lòng từng dấu chấm phẩy trong báo cáo không",
                            "B. Đánh giá năng lực thực chất của từng cá nhân thông qua hệ thống Atomic Notes trong Second Brain và khả năng thao tác trực tiếp trên bộ Harness/Zotero của nhóm, đảm bảo không ai có thể 'ăn theo nhóm' (free-rider) để lấy chứng chỉ",
                            "C. Chỉ hỏi riêng một mình nhóm trưởng",
                            "D. Hỏi các câu đố vui không liên quan đến môn học"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L1-c11-q4",
                        "type": "mc",
                        "concept_ref": "c11-ba-dieu-mang-ve",
                        "question": "Theo định nghĩa 'Làm chủ AI' được đúc kết ở cuối khóa học, người làm chủ AI thực sự là người như thế nào?",
                        "options": [
                            "A. Là người từ chối dùng mọi công nghệ hiện đại",
                            "B. Là người biết rõ mình đang giao việc gì cho AI, thiết lập được bộ khung điều phối (Harness), biết cách kiểm chứng lại kết quả qua nguồn thật, giữ vững tư duy độc lập trong Second Brain và đàng hoàng đứng tên chịu trách nhiệm dưới sản phẩm của mình",
                            "C. Là người đăng ký mua tất cả các gói AI trả phí đắt nhất thế giới",
                            "D. Là người để AI tự quyết định mọi việc thay mình"
                        ],
                        "correct": "B"
                    }
                ]
            },
            "level_2": {
                "name": "📝 Level 2: Kết nối Hệ thống 4 Module",
                "description": "Phân tích mối liên kết hữu cơ giữa Prompt-Context-Harness, Second Brain, Kiểm chứng NCKH và Đạo đức AI.",
                "bloom_level": "Understand",
                "questions": [
                    {
                        "id": "L2-c11-q1",
                        "type": "mc",
                        "concept_ref": "c11-ba-dieu-mang-ve",
                        "question": "Bốn trụ cột của môn học (1. Prompt-Context-Harness; 2. Second Brain; 3. Nghiên cứu & Kiểm chứng 5 bước; 4. Đạo đức & Bảo mật dữ liệu) bổ trợ cho nhau như thế nào trong một quy trình làm việc hoàn chỉnh?",
                        "options": [
                            "A. Bốn trụ cột này hoàn toàn tách rời, không liên quan gì đến nhau",
                            "B. Quy trình Nghiên cứu & Kiểm chứng 5 bước giúp lọc lấy 'nguồn tri thức thật'; hệ thống Second Brain giúp bạn tiêu hóa nguồn thật đó thành 'Atomic Notes của riêng mình'; các Atomic Notes này trở thành nguồn 'Context sạch' để nạp vào bộ 'Harness' điều phối AI tạo ra sản phẩm chất lượng cao; và khung 'Đạo đức & Bảo mật' giữ cho toàn bộ quá trình đó an toàn, hợp pháp và minh bạch",
                            "C. Chỉ cần học Trụ cột 1 là có thể bỏ qua 3 trụ cột còn lại",
                            "D. Second Brain chỉ dùng để lưu mật khẩu, còn Harness dùng để thay thế Zotero"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L2-c11-q2",
                        "type": "mc",
                        "concept_ref": "c11-capstone-defense",
                        "question": "Khi Hội đồng Kiểm toán chéo chỉ ra một điểm hạn chế có thật trong Đề án của nhóm bạn tại buổi bảo vệ, cách phản hồi nào dưới đây thể hiện bản lĩnh học thuật cao nhất?",
                        "options": [
                            "A. Đổ lỗi cho AI: 'Tại hôm qua ChatGPT/Claude nó xuất ra như vậy chứ nhóm em không biết!'",
                            "B. Thẳng thắn ghi nhận phát hiện xác đáng của Hội đồng Kiểm toán, giải thích rõ nguyên nhân kỹ thuật (ví dụ: điều kiện ở cổng GATE 1 chưa bao quát trường hợp ngoại lệ đó), và trình bày ngay phương án điều chỉnh câu lệnh/số liệu mà nhóm đã cập nhật",
                            "C. Cãi chày cãi cối để bảo vệ cái sai bằng mọi giá",
                            "D. Im lặng không trả lời"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L2-c11-q3",
                        "type": "mc",
                        "concept_ref": "c11-ba-dieu-mang-ve",
                        "question": "Tại sao câu trả lời 'Tại AI làm sai chứ không phải lỗi của em!' lại là câu trả lời bị trừ điểm nặng nhất trong cả môi trường học thuật lẫn môi trường làm việc tại ngân hàng/doanh nghiệp?",
                        "options": [
                            "A. Vì câu nói đó chứng tỏ người nói đã từ bỏ vị thế 'Bạn là Chủ' và vi phạm trực tiếp nguyên tắc chịu trách nhiệm của Thông tư 49/2026/TT-BGDĐT, Luật AI 134/2025 cũng như chuẩn COPE/ICMJE: AI chỉ là công cụ, người sử dụng công cụ và đặt tên mình lên báo cáo phải chịu trách nhiệm 100% về việc kiểm chứng đầu ra",
                            "B. Vì giảng viên không thích nghe nhắc đến tên AI",
                            "C. Vì AI luôn luôn đúng 100%, không bao giờ làm sai",
                            "D. Vì câu trả lời đó quá ngắn"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L2-c11-q4",
                        "type": "mc",
                        "concept_ref": "c11-ba-dieu-mang-ve",
                        "question": "Khi một thế hệ mô hình AI mới (ví dụ GPT-6, Claude 5 hay Gemini 4) ra mắt vào năm sau với nhiều tính năng tự động hóa mạnh hơn, người đã nắm vững phương pháp của môn học này sẽ tiếp cận nó như thế nào?",
                        "options": [
                            "A. Hoang mang vì phải học lại cách bấm nút từ đầu",
                            "B. Bình tĩnh đặt công cụ mới vào đúng vị trí của tầng 'Công cụ': dùng tư duy xác suất để biết nó vẫn có thể bịa ở vùng dữ liệu thưa, tiếp tục dùng kho Second Brain của mình làm Context, dùng kiến trúc Harness (GATE/FALLBACK) để điều phối nó và giữ nguyên kỷ luật kiểm chứng 5 bước + Zotero",
                            "C. Xóa bỏ toàn bộ Second Brain và Zotero vì nghĩ AI mới không bao giờ sai nữa",
                            "D. Ngừng tư duy và giao hết công việc cho mô hình mới"
                        ],
                        "correct": "B"
                    }
                ]
            },
            "level_3": {
                "name": "🚀 Level 3: Phản tư Tổng kết & Cam kết Người làm chủ AI",
                "description": "Đúc kết hành trình 11 buổi và xác lập bộ nguyên tắc ứng dụng AI cho khóa luận và sự nghiệp.",
                "bloom_level": "Apply",
                "questions": [
                    {
                        "id": "L3-c11-q1",
                        "type": "mc",
                        "concept_ref": "c11-ba-dieu-mang-ve",
                        "question": "Học kỳ tới, bạn bắt đầu thực hiện Khóa luận tốt nghiệp ngành Tài chính - Ngân hàng tại HUB. Trình tự khởi đầu nào dưới đây áp dụng chuẩn xác nhất toàn bộ tinh thần của học phần này?",
                        "options": [
                            "A. Mở Chatbot bảo viết hộ đề cương và 50 tài liệu tham khảo trong 5 phút",
                            "B. (1) Tạo thư mục Project cho Khóa luận trong Second Brain; (2) Dùng Phễu thu hẹp để xác định câu hỏi nghiên cứu và tìm 10-15 bài báo gốc thật trên Semantic Scholar/Elicit; (3) Đọc sâu, chạy Prompt 7 mục và 'Soi 3 phút' từng bài; (4) Kiểm chứng qua Checklist 5 bước, lưu vào Zotero 8 và đúc kết các Atomic Notes vào Second Brain; (5) Đóng gói kho RAG trên Gemini Notebook và thiết kế bộ Harness có cổng GATE để đồng hành xuyên suốt khóa luận kèm nhật ký lưu thông tin khai báo AI theo Thông tư 49/2026",
                            "C. Đợi đến tuần cuối cùng trước hạn nộp mới nhờ AI viết toàn bộ khóa luận",
                            "D. Mua một bài khóa luận có sẵn trên mạng"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L3-c11-q2",
                        "type": "mc",
                        "concept_ref": "c11-ba-dieu-mang-ve",
                        "question": "Khi đi thực tập tại phòng Tín dụng hoặc Marketing của một ngân hàng thương mại, bạn muốn đề xuất ứng dụng AI để rút ngắn 50% thời gian tổng hợp báo cáo tuần của phòng. Bước đầu tiên bạn cần làm để thể hiện sự chuyên nghiệp và an toàn là gì?",
                        "options": [
                            "A. Tự ý lấy toàn bộ hồ sơ khách hàng thật của ngân hàng tải lên tài khoản AI cá nhân của mình",
                            "B. Áp dụng khung phân loại dữ liệu và Đèn giao thông: xác định rõ dữ liệu nào là công khai, dữ liệu nào là nội bộ/định danh phải khử mật hoặc chỉ được chạy trên hệ thống được bộ phận An ninh thông tin/Pháp chế của ngân hàng cấp phép; thiết kế bản mẫu Workflow Harness trên dữ liệu giả lập có cổng GATE kiểm chứng số liệu rõ ràng rồi mới trình quản lý phê duyệt",
                            "C. Giấu quản lý, lén dùng AI làm xong rồi nhận là mình tự làm thủ công",
                            "D. Nhờ AI tự ký tên phê duyệt báo cáo gửi Ban Giám đốc"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L3-c11-essay1",
                        "type": "essay",
                        "concept_ref": "c11-ba-dieu-mang-ve",
                        "question": "Phản tư Tổng kết Cuối khóa (Theo khung 4F): Hãy nhìn lại toàn bộ hành trình 11 buổi học của bạn và viết Atomic Note tổng kết cuối cùng: (1) Fact & Feelings: Sự thay đổi lớn nhất trong cách bạn nhìn nhận và sử dụng AI giữa Buổi 1 và Buổi 11 là gì? Khoảnh khắc 'va chạm' nào trong môn học làm bạn nhớ nhất? (2) Findings & Future: Ba nguyên tắc cốt lõi bạn đúc kết được và 01 cam kết danh dự với chính mình về cách sử dụng AI trong Khóa luận tốt nghiệp và sự nghiệp tương lai.",
                        "rubric": "Phản tư chân thực, sâu sắc về sự chuyển hóa tư duy từ Buổi 1 đến Buổi 11 qua trải nghiệm cụ thể (35%) · Đúc kết sắc bén 3 nguyên tắc thuộc về Tư duy - Kỹ năng - Đạo đức/Kiểm chứng (35%) · Nêu kế hoạch hành động và cam kết cụ thể, khả thi cho khóa luận/công việc sắp tới (30%)",
                        "max_words": 450
                    }
                ]
            }
        }
    }
]

for ch in chapters_7_to_11:
    path = os.path.join(CONTENT_DIR, "ebook", f"chapter-{ch['chapter']}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(ch, f, ensure_ascii=False, indent=2)

print("Chapters 7 to 11 generated successfully.")
