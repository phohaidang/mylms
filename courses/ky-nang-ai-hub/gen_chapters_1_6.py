# -*- coding: utf-8 -*-
import os
import json

CONTENT_DIR = r"d:\PARA\Projects\second-brain\05-Projects\lms-hub\courses\ky-nang-ai-hub\content"
null = None
true = True
false = False

chapters_1_to_6 = [
    {
        "chapter": 1,
        "title": "Bản chất AI & Tư duy người làm chủ: 'AI là Trợ lý, Bạn là Chủ'",
        "sessions": [1],
        "scqa": {
            "situation": "Mỗi khi nhận đề tiểu luận hay bài tập lớn tại Trường ĐH Ngân hàng TP.HCM, thao tác đầu tiên của hầu hết sinh viên hiện nay là mở ChatGPT, Claude hoặc Gemini, gõ vài dòng yêu cầu và nhận về một bài viết 1.500 chữ trôi chảy chỉ sau 30 giây.",
            "complication": "Tuy nhiên, khi giảng viên hỏi 'Số liệu tỷ lệ nợ xấu trang 3 em lấy từ báo cáo nào?' hoặc 'Tại sao em chọn mô hình này?', người nộp bài hoàn toàn lúng túng vì không biết AI lấy số đó ở đâu. Nghiêm trọng hơn, nghiên cứu của Topaz và cộng sự trên tạp chí y khoa danh tiếng The Lancet (5/2026) chỉ ra rằng cứ 277 bài báo khoa học trên PubMed đầu năm 2026 thì có 1 bài dính tài liệu tham khảo hoàn toàn không tồn tại do AI bịa ra (tăng gấp 10 lần so với năm 2023). Việc giao phó tư duy cho một cỗ máy xác suất đang âm thầm tạo ra hiện tượng lệ thuộc nhận thức (cognitive offloading) và ảo tưởng trôi chảy (fluency illusion).",
            "question": "Nếu AI không thực sự 'biết' những gì nó đang viết ra, làm thế nào để sinh viên khai thác sức mạnh của AI mà không bị nó dắt mũi hay làm teo đi năng lực tư duy độc lập của chính mình?",
            "answer": "Bắt đầu từ triết lý 'Tư duy -> Kỹ năng -> Công cụ': hiểu rõ AI là cỗ máy dự đoán từ tiếp theo dựa trên xác suất, thiết lập nguyên tắc phân vai 'AI đề xuất - Bạn quyết định - Bạn chịu trách nhiệm', và chỉ giao cho AI những bước mà chính bạn có đủ năng lực kiểm tra lại."
        },
        "concepts": [
            {
                "id": "c1-xac-suat-llm",
                "session": 1,
                "term": "Bản chất xác suất của Mô hình ngôn ngữ lớn (LLM)",
                "definition": "Mô hình ngôn ngữ lớn (Large Language Model - LLM) không phải là một kho lưu trữ sự thật hay bộ não có ý thức, mà là một hệ thống toán học dự đoán từ (token) tiếp theo có xác suất xuất hiện cao nhất dựa trên ngữ cảnh đứng trước nó.",
                "key_points": [
                    "<strong>Cơ chế vận hành:</strong> Khi bạn nhập câu hỏi, LLM tính toán phân phối xác suất trên hàng tỷ tham số để chọn ra chuỗi từ nghe hợp lý nhất về mặt ngôn ngữ.",
                    "<strong>Khác biệt với Google Search:</strong> Công cụ tìm kiếm tra cứu và trả về đường dẫn tới các văn bản có sẵn trên Internet; ngược lại, LLM <em>tạo sinh (generate)</em> văn bản mới từng chữ một theo thời gian thực.",
                    "<strong>Hệ quả tất yếu:</strong> Vì ưu tiên tính trôi chảy của ngôn ngữ hơn tính xác thực của dữ liệu, một câu trả lời cực kỳ mạch lạc, văn phong học thuật vẫn có thể sai hoàn toàn về mặt sự thật."
                ],
                "case_study": {
                    "title": "Bẫy thông tư ngân hàng không tồn tại",
                    "context": "Trong giờ học, giảng viên yêu cầu AI tóm tắt 'Thông tư 99/2025/TT-NHNN về quy định cấp tín dụng xanh cho sinh viên khởi nghiệp' (một văn bản hoàn toàn bịa).",
                    "analysis": "Nếu không có ràng buộc chặt, AI vẫn tự tin liệt kê đủ Điều 1, Điều 2, lãi suất ưu đãi 4.5%/năm với giọng văn hành chính chuẩn mực vì các cụm từ này có xác suất đi cùng nhau rất cao trong tập dữ liệu huấn luyện.",
                    "lesson_learned": "Sự tự tin và trôi chảy của AI không bao giờ là bằng chứng của sự thật."
                },
                "related_concepts": ["c1-hallucination", "c1-phan-vai"]
            },
            {
                "id": "c1-hallucination",
                "session": 1,
                "term": "Ảo giác AI (Hallucination) & Bằng chứng thực nghiệm",
                "definition": "Hiện tượng mô hình AI tạo ra thông tin sai lệch, số liệu giả hoặc tài liệu tham khảo không tồn tại nhưng trình bày với hình thức và giọng điệu vô cùng thuyết phục.",
                "key_points": [
                    "<strong>Bằng chứng từ The Lancet (Topaz và cs., 5/2026):</strong> Kiểm tra gần 2.5 triệu bài báo trên PubMed (97 triệu tài liệu tham khảo), phát hiện 4.046 trích dẫn bịa trong 2.810 bài báo. Tỷ lệ bài có trích dẫn bịa tăng vọt từ <strong>1/2.828 (năm 2023)</strong> lên <strong>1/458 (năm 2025)</strong> và chạm mức <strong>1/277 (7 tuần đầu năm 2026)</strong>.",
                    "<strong>Nguyên nhân gốc rễ:</strong> Hallucination gắn liền với cơ chế dự đoán xác suất của LLM khi nó cố gắng 'lấp đầy chỗ trống' để chiều lòng người hỏi, đặc biệt ở các chủ đề chuyên sâu hoặc ít dữ liệu.",
                    "<strong>Cách phòng vệ ban đầu:</strong> Không bao giờ dùng Chatbot tổng quát làm nguồn tra cứu danh mục tài liệu tham khảo; luôn yêu cầu đính kèm tài liệu gốc và kiểm chứng độc lập."
                ],
                "case_study": null,
                "related_concepts": ["c1-xac-suat-llm"]
            },
            {
                "id": "c1-cognitive-traps",
                "session": 1,
                "term": "Lệ thuộc nhận thức (Cognitive Offloading) & Ảo tưởng trôi chảy (Fluency Illusion)",
                "definition": "Hai căn bệnh nhận thức nguy hiểm nhất của người học trong kỷ nguyên AI: giao phó hoàn toàn việc suy nghĩ cho máy (làm teo cơ tư duy) và nhầm lẫn giữa việc 'đọc thấy bài AI viết dễ hiểu' với việc 'bản thân đã thực sự hiểu và nắm vững kiến thức đó'.",
                "key_points": [
                    "<strong>Ảo tưởng trôi chảy (Fluency Illusion):</strong> Não bộ con người chỉ tạo ra liên kết thần kinh bền vững khi phải trải qua <em>ma sát nhận thức (productive struggle)</em>. Khi đọc bản tóm tắt mượt mà của AI, bạn thấy gật gù dễ hiểu nhưng sau 24 giờ sẽ quên tới 80% vì não chưa hề tiêu hóa.",
                    "<strong>Lệ thuộc nhận thức (Cognitive Offloading):</strong> Giống như dùng xe máy để đi quãng đường 100 mét mỗi ngày, việc nhờ AI viết hộ từng đoạn văn ngắn hay giải hộ bài tập cơ bản sẽ làm mất dần khả năng lập luận cấu trúc và viết độc lập.",
                    "<strong>Thuốc giải:</strong> Dùng AI để <em>tạo ma sát có hướng dẫn</em> (hỏi ngược, phản biện dàn ý của bạn) chứ không dùng AI để triệt tiêu ma sát học tập."
                ],
                "case_study": null,
                "related_concepts": ["c1-phan-vai"]
            },
            {
                "id": "c1-phan-vai",
                "session": 1,
                "term": "Khung phân vai: 'AI là Trợ lý, Bạn là Chủ'",
                "definition": "Nguyên tắc định vị quyền hạn và trách nhiệm giữa con người và AI dựa trên 3 động từ cốt lõi: AI đề xuất - Bạn quyết định - Bạn chịu trách nhiệm.",
                "key_points": [
                    "<strong>AI đề xuất (Propose):</strong> Gợi ý từ khóa, tóm lược sơ bộ văn bản đính kèm, dựng dàn ý nháp, phản biện lỗ hổng lập luận, rà soát ngữ pháp.",
                    "<strong>Bạn quyết định (Decide):</strong> Chọn câu hỏi nghiên cứu, thẩm định độ tin cậy của nguồn, chốt cấu trúc lập luận và đưa ra kết luận chuyên môn.",
                    "<strong>Bạn chịu trách nhiệm (Accountable):</strong> Kiểm chứng từng con số và trích dẫn, khai báo việc dùng AI minh bạch. Tên của bạn đứng trên trang bìa báo cáo chứ không phải tên của ChatGPT hay Claude.",
                    "<strong>Phép thử vàng khi giao việc cho AI:</strong> <em>'Nếu AI làm sai ở bước này, mình có đủ kiến thức và công cụ để phát hiện ra không?'</em> Nếu câu trả lời là KHÔNG, tuyệt đối đừng giao bước đó cho AI."
                ],
                "case_study": null,
                "related_concepts": ["c1-ban-do-cong-cu"]
            },
            {
                "id": "c1-ban-do-cong-cu",
                "session": 1,
                "term": "Bản đồ hệ sinh thái công cụ AI 2026 theo tác vụ",
                "definition": "Phân loại các công cụ AI thành 4 nhóm chuyên biệt dựa trên kiến trúc truy xuất dữ liệu, giúp người học chọn đúng công cụ cho đúng mục đích thay vì dùng một Chatbot cho mọi việc.",
                "key_points": [
                    "<strong>1. Hội thoại đa năng & Suy luận (ChatGPT, Claude, Gemini, DeepSeek):</strong> Mạnh về brainstorm, phân tích logic, giải thích khái niệm, thiết kế quy trình; nhưng <em>tuyệt đối không dùng để lấy danh mục tài liệu tham khảo</em> vì dễ bịa nguồn.",
                    "<strong>2. Tìm kiếm web có trích nguồn (Perplexity, ChatGPT Search):</strong> Hữu ích để tra cứu tin tức, báo cáo thị trường mới; vẫn cần bấm vào link gốc để kiểm tra.",
                    "<strong>3. Tìm kiếm & Tổng hợp học thuật thật (Semantic Scholar, Elicit, Consensus):</strong> Kết nối trực tiếp với kho hơn 200 triệu bài báo khoa học có thật và mã DOI chuẩn.",
                    "<strong>4. Quản trị tri thức & RAG cá nhân (Gemini Notebook / NotebookLM, Claude Projects):</strong> Chỉ trả lời dựa trên tập tài liệu chuẩn mà bạn tải lên và trích dẫn chính xác về đúng đoạn văn gốc."
                ],
                "case_study": null,
                "related_concepts": ["c1-phan-vai"]
            }
        ],
        "tests": {
            "level_1": {
                "name": "🎯 Level 1: Khái niệm cốt lõi",
                "description": "Nhận biết bản chất xác suất của LLM, số liệu thực nghiệm và nguyên tắc phân vai.",
                "bloom_level": "Remember",
                "questions": [
                    {
                        "id": "L1-c1-q1",
                        "type": "mc",
                        "concept_ref": "c1-xac-suat-llm",
                        "question": "Cơ chế cốt lõi giúp các Mô hình ngôn ngữ lớn (LLM) như ChatGPT hay Claude tạo ra câu trả lời là gì?",
                        "options": [
                            "A. Tra cứu trực tiếp từ một cơ sở dữ liệu sự thật đã được kiểm duyệt 100%",
                            "B. Dự đoán từ (token) tiếp theo có xác suất xuất hiện cao nhất dựa trên ngữ cảnh đứng trước",
                            "C. Sao chép nguyên văn các đoạn văn bản từ Google Scholar theo thời gian thực",
                            "D. Sử dụng tư duy nhận thức và sự hiểu biết chuyên môn giống như bộ não chuyên gia"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L1-c1-q2",
                        "type": "mc",
                        "concept_ref": "c1-hallucination",
                        "question": "Theo nghiên cứu của Topaz và cộng sự đăng trên tạp chí The Lancet (5/2026) khi kiểm tra gần 2.5 triệu bài báo trên PubMed, tỷ lệ bài báo có chứa ít nhất một tài liệu tham khảo bịa trong 7 tuần đầu năm 2026 là bao nhiêu?",
                        "options": [
                            "A. 1/2.828 bài báo",
                            "B. 1/1.000 bài báo",
                            "C. 1/277 bài báo",
                            "D. 1/10 bài báo"
                        ],
                        "correct": "C"
                    },
                    {
                        "id": "L1-c1-q3",
                        "type": "mc",
                        "concept_ref": "c1-cognitive-traps",
                        "question": "Hiện tượng sinh viên đọc bản tóm tắt rất mượt mà của AI, cảm thấy mình đã hiểu hết bài nhưng thực chất não bộ chưa hề xử lý sâu và nhanh chóng quên sạch được gọi là gì?",
                        "options": [
                            "A. Ảo giác dữ liệu (Data Hallucination)",
                            "B. Ảo tưởng trôi chảy (Fluency Illusion)",
                            "C. Quá tải ngữ cảnh (Context Overflow)",
                            "D. Học tập chủ động (Active Recall)"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L1-c1-q4",
                        "type": "mc",
                        "concept_ref": "c1-phan-vai",
                        "question": "Trong mô hình 'AI là Trợ lý, Bạn là Chủ', bộ ba động từ nào định vị đúng vai trò của AI và người học?",
                        "options": [
                            "A. AI quyết định - Bạn thực thi - Nhà trường chịu trách nhiệm",
                            "B. AI tìm nguồn - AI viết bài - Bạn đứng tên",
                            "C. AI đề xuất - Bạn quyết định - Bạn chịu trách nhiệm",
                            "D. Bạn đề xuất - AI quyết định - Cùng chịu trách nhiệm"
                        ],
                        "correct": "C"
                    }
                ]
            },
            "level_2": {
                "name": "📝 Level 2: Hiểu và phân biệt",
                "description": "Phân tích nguyên nhân của Hallucination và ranh giới giao việc cho AI.",
                "bloom_level": "Understand",
                "questions": [
                    {
                        "id": "L2-c1-q1",
                        "type": "mc",
                        "concept_ref": "c1-xac-suat-llm",
                        "question": "Vì sao một mô hình AI có thể bịa ra một thông tư ngân hàng hoặc một trích dẫn khoa học không hề tồn tại với giọng văn vô cùng tự tin?",
                        "options": [
                            "A. Vì thuật toán đoán chữ chỉ ưu tiên ghép các cụm từ có xác suất ngôn ngữ hợp lý nhất với câu hỏi, chứ không có cơ chế tự kiểm tra sự thật",
                            "B. Vì nhà phát triển lập trình cho AI tính năng nói dối khi gặp câu hỏi khó",
                            "C. Vì máy tính của người dùng bị nhiễm mã độc làm sai lệch kết quả",
                            "D. Vì AI chỉ bịa khi người dùng sử dụng phiên bản miễn phí"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L2-c1-q2",
                        "type": "mc",
                        "concept_ref": "c1-phan-vai",
                        "question": "Theo nguyên tắc phân vai 'Việc nào giao, việc nào giữ', câu hỏi tự kiểm tra nào giúp bạn biết có nên giao một bước công việc cho AI hay không?",
                        "options": [
                            "A. Bước này AI làm có nhanh hơn mình làm không?",
                            "B. Nếu AI làm sai ở bước này, mình có đủ khả năng và công cụ phát hiện ra không?",
                            "C. Bước này có tốn nhiều dung lượng token của AI không?",
                            "D. Bạn bè trong lớp có dùng AI cho bước này không?"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L2-c1-q3",
                        "type": "mc",
                        "concept_ref": "c1-ban-do-cong-cu",
                        "question": "Khi bạn cần hỏi đáp và trích xuất thông tin chỉ gói gọn trong 3 cuốn giáo trình PDF của môn học mà không muốn AI suy diễn thêm từ bên ngoài, nhóm công cụ nào là phù hợp nhất?",
                        "options": [
                            "A. Chatbot hội thoại tổng quát không đính kèm tài liệu",
                            "B. Công cụ tạo hình ảnh tự động",
                            "C. Công cụ RAG quản trị tài liệu cá nhân như Gemini Notebook (NotebookLM)",
                            "D. Công cụ kiểm tra đạo văn"
                        ],
                        "correct": "C"
                    },
                    {
                        "id": "L2-c1-q4",
                        "type": "mc",
                        "concept_ref": "c1-cognitive-traps",
                        "question": "Cách sử dụng AI nào dưới đây giúp RÈN LUYỆN tư duy thay vì rơi vào bẫy lệ thuộc nhận thức (Cognitive Offloading)?",
                        "options": [
                            "A. Nhờ AI viết trọn vẹn bài tiểu luận rồi học thuộc lòng để đi thi",
                            "B. Tự mình phác thảo dàn ý và luận điểm trước, sau đó dùng AI đóng vai người phản biện để chỉ ra các lỗ hổng logic trong dàn ý của mình",
                            "C. Chép đề bài tập lên AI và chép nguyên lời giải vào vở",
                            "D. Nhờ AI đọc hộ toàn bộ bài báo mà không bao giờ mở file PDF gốc"
                        ],
                        "correct": "B"
                    }
                ]
            },
            "level_3": {
                "name": "🚀 Level 3: Vận dụng thực tế",
                "description": "Áp dụng tư duy làm chủ AI vào tình huống học tập tại ĐH Ngân hàng TP.HCM.",
                "bloom_level": "Apply",
                "questions": [
                    {
                        "id": "L3-c1-q1",
                        "type": "mc",
                        "concept_ref": "c1-ban-do-cong-cu",
                        "question": "Minh đang làm đề tài về 'Rủi ro tín dụng xanh tại các ngân hàng thương mại Việt Nam'. Minh mở một Chatbot tổng quát và gõ: 'Hãy cho tôi 10 tài liệu tham khảo uy tín kèm DOI về đề tài này'. Hành động này vi phạm nguyên tắc nào?",
                        "options": [
                            "A. Dùng sai công cụ cho tác vụ cần nguồn thật: Chatbot tổng quát sinh văn bản theo xác suất nên rất dễ ghép các mảnh thông tin thành trích dẫn bịa và DOI giả",
                            "B. Xin quá ít tài liệu tham khảo, lẽ ra phải xin 50 tài liệu một lúc",
                            "C. Không vi phạm gì, đây là cách tìm tài liệu chuẩn xác nhất hiện nay",
                            "D. Vi phạm vì không viết câu lệnh bằng tiếng Anh"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L3-c1-q2",
                        "type": "mc",
                        "concept_ref": "c1-phan-vai",
                        "question": "Trong 4 công việc dưới đây khi làm tiểu luận ngành Tài chính - Ngân hàng, công việc nào người học BẮT BUỘC phải tự giữ quyền quyết định cuối cùng, không được giao phó cho AI?",
                        "options": [
                            "A. Gợi ý các từ khóa tiếng Anh tương đương để tra cứu trên Semantic Scholar",
                            "B. Rà soát lỗi chính tả và ngữ pháp của bản thảo",
                            "C. Kiểm chứng độ tin cậy của số liệu gốc và chốt kết luận học thuật của bài viết",
                            "D. Chuyển đổi một đoạn ghi chú nháp thành bảng tóm tắt sơ bộ"
                        ],
                        "correct": "C"
                    },
                    {
                        "id": "L3-c1-essay1",
                        "type": "essay",
                        "concept_ref": "c1-phan-vai",
                        "question": "Hãy chọn một bài tập lớn hoặc đề tài môn chuyên ngành bạn đang học tại HUB. Chia quy trình làm bài đó thành 4 bước, và lập bảng phân vai rõ ràng: Ở mỗi bước, việc gì bạn giao cho AI đề xuất, việc gì bạn tự quyết định, và bạn sẽ kiểm tra kết quả của AI bằng cách nào?",
                        "rubric": "Nêu rõ tên bài tập/đề tài chuyên ngành tại HUB (20%) · Phân tách quy trình 4 bước mạch lạc (20%) · Phân vai đúng nguyên tắc AI đề xuất - Người quyết định (30%) · Nêu được cơ chế kiểm chứng cụ thể ở từng bước giao cho AI (30%)",
                        "max_words": 300
                    }
                ]
            }
        }
    },
    {
        "chapter": 2,
        "title": "Từ Prompt Engineering đến Context Engineering: Giao diện của Tư duy",
        "sessions": [2],
        "scqa": {
            "situation": "Cùng sử dụng một phiên bản Claude hoặc ChatGPT như nhau trong lớp học, nhưng có sinh viên chỉ mất 15 phút để thu được một bảng phân tích sâu sắc, sát thực tế ngành ngân hàng; trong khi sinh viên ngồi cạnh hỏi đi hỏi lại cả tiếng đồng hồ vẫn chỉ nhận được những đoạn văn chung chung, sáo rỗng.",
            "complication": "Nhiều bạn nghĩ rằng bí quyết nằm ở việc sưu tầm các 'câu thần chú' (magic prompts) trên mạng. Thực tế, AI không đọc được suy nghĩ trong đầu bạn: khi tư duy của bạn mơ hồ và bạn đưa vào một ngữ cảnh nghèo nàn, AI buộc phải lấy mức trung bình cộng của dữ liệu Internet để trả lời ('Rác vào thì Rác ra').",
            "question": "Làm thế nào để chuyển hóa tư duy của người làm chủ thành những chỉ thị sắc bén và thiết kế được 'môi trường ngữ cảnh' (Context) giúp AI làm việc đúng chuẩn chuyên môn ngay từ đầu?",
            "answer": "Làm chủ công thức cấu trúc hóa câu lệnh CRISP, kết hợp 5 kỹ thuật điều khiển suy luận nâng cao (đặc biệt là chốt chặn 'Không suy đoán'), và tiến lên tầng Context Engineering: cung cấp dữ liệu nền đã làm sạch cùng tiêu chuẩn đầu ra rõ ràng."
        },
        "concepts": [
            {
                "id": "c2-crisp",
                "session": 2,
                "term": "Khung cấu trúc câu lệnh CRISP",
                "definition": "Phương pháp cấu trúc hóa yêu cầu gửi cho AI gồm 5 thành tố cốt lõi giúp loại bỏ sự mơ hồ và định hướng không gian xác suất của mô hình vào đúng mục tiêu chuyên môn.",
                "key_points": [
                    "<strong>C - Context (Bối cảnh):</strong> Bạn là ai, đang giải quyết bài toán gì, trong môi trường hay điều kiện ràng buộc nào?",
                    "<strong>R - Role (Vai trò):</strong> AI cần đóng vai chuyên gia nào, với góc nhìn và tiêu chuẩn chuyên môn gì?",
                    "<strong>I - Input / Instruction (Dữ liệu đầu vào & Nhiệm vụ):</strong> Tài liệu/số liệu cụ thể bạn cung cấp là gì và nhiệm vụ cốt lõi cần thực hiện là gì?",
                    "<strong>S - Specifics (Yêu cầu cụ thể):</strong> Định dạng đầu ra (bảng, gạch đầu dòng), độ dài, văn phong, thuật ngữ cần giữ.",
                    "<strong>P - Performance Criteria / Preview (Tiêu chí đánh giá & Hình dung kết quả):</strong> Ai sẽ đọc kết quả này, tiêu chuẩn nào để đánh giá là đạt, và những điều gì tuyệt đối không được vi phạm."
                ],
                "case_study": {
                    "title": "Phân tích rủi ro khoản vay doanh nghiệp vừa và nhỏ (SME)",
                    "context": "So sánh câu lệnh mơ hồ: 'Phân tích rủi ro cho vay SME' với câu lệnh CRISP đầy đủ bối cảnh ngân hàng thương mại Việt Nam, dữ liệu báo cáo tài chính đính kèm và yêu cầu xuất bảng 5 tiêu chí.",
                    "analysis": "Câu lệnh mơ hồ trả về lý thuyết sách giáo khoa. Câu lệnh CRISP giúp AI tập trung phân tích đúng dòng tiền và vòng quay hàng tồn kho từ dữ liệu đính kèm.",
                    "lesson_learned": "10 phút đầu tư viết Prompt & Context chuẩn CRISP giúp tiết kiệm 2 giờ sửa chữa đầu ra."
                },
                "related_concepts": ["c2-5-ky-thuat", "c2-context-engineering"]
            },
            {
                "id": "c2-5-ky-thuat",
                "session": 2,
                "term": "Năm kỹ thuật Prompt nâng cao & Chốt chặn 'Không suy đoán'",
                "definition": "Bộ 5 kỹ thuật điều khiển luồng suy luận và giới hạn hành vi của AI trong các tác vụ học thuật và phân tích chuyên sâu.",
                "key_points": [
                    "<strong>1. Chain-of-Thought (CoT - Suy luận từng bước):</strong> Yêu cầu AI trình bày rõ các bước lập luận trung gian trước khi đưa ra kết luận cuối cùng.",
                    "<strong>2. Role-based / Multi-Persona (Đa góc nhìn):</strong> Yêu cầu AI phân tích cùng một vấn đề dưới góc nhìn đối lập (ví dụ: Cán bộ thẩm định rủi ro vs Chuyên viên quan hệ khách hàng).",
                    "<strong>3. Few-shot Prompting (Học qua ví dụ mẫu):</strong> Cung cấp 2-3 ví dụ mẫu đạt chuẩn để AI bắt chước chính xác cấu trúc và giọng điệu.",
                    "<strong>4. Iterative Refinement (Tinh chỉnh đa vòng):</strong> Giữ phần đã đúng, chỉ yêu cầu sửa 1-2 tiêu chí cụ thể qua từng lượt đối thoại.",
                    "<strong>5. Negative Prompt & Chốt chặn 'Không suy đoán':</strong> Chỉ rõ những điều cấm làm. Đặc biệt trong học thuật, luôn cài câu khóa: <em>'Mỗi ý phải ghi rõ số trang/mục trong tài liệu. Chỗ nào tài liệu không nêu, ghi rõ không nêu trong bài, tuyệt đối không suy đoán.'</em>"
                ],
                "case_study": null,
                "related_concepts": ["c2-crisp"]
            },
            {
                "id": "c2-context-engineering",
                "session": 2,
                "term": "Context Engineering (Kỹ nghệ Thiết kế Ngữ cảnh)",
                "definition": "Bước tiến hóa từ việc 'chăm chút một câu hỏi lẻ' (Prompt Engineering) sang việc 'thiết kế toàn bộ gói thông tin, tài liệu nguồn, ví dụ mẫu và quy tắc biên' được nạp vào cửa sổ ngữ cảnh (Context Window) của AI.",
                "key_points": [
                    "<strong>Bản chất:</strong> Một Prompt hay đến mấy cũng vô dụng nếu AI không có dữ liệu thật của bài toán. Context Engineering trả lời câu hỏi: <em>AI cần nhìn thấy những tài liệu và quy tắc nào trước khi bắt đầu suy nghĩ?</em>",
                    "<strong>4 thành phần của một Context tốt:</strong> (1) Tài liệu nguồn đã làm sạch (PDF bài báo, bảng số liệu), (2) Rubric hoặc tiêu chuẩn chất lượng, (3) Ví dụ mẫu (Few-shot), (4) Ràng buộc biên (chốt chặn chống suy diễn).",
                    "<strong>Quản trị Context Window:</strong> Cửa sổ ngữ cảnh là bộ nhớ làm việc có giới hạn; đưa tài liệu rác hoặc hội thoại lan man quá dài sẽ làm loãng sự chú ý của mô hình (Context Rot)."
                ],
                "case_study": null,
                "related_concepts": ["c2-crisp"]
            }
        ],
        "tests": {
            "level_1": {
                "name": "🎯 Level 1: Khái niệm cốt lõi",
                "description": "Nhận diện 5 thành phần khung CRISP và các kỹ thuật Prompt/Context nền tảng.",
                "bloom_level": "Remember",
                "questions": [
                    {
                        "id": "L1-c2-q1",
                        "type": "mc",
                        "concept_ref": "c2-crisp",
                        "question": "Trong công thức viết câu lệnh CRISP, chữ 'S' (Specifics) đại diện cho yêu cầu nào?",
                        "options": [
                            "A. Các ràng buộc và yêu cầu cụ thể về định dạng, độ dài, văn phong, ngôn ngữ đầu ra",
                            "B. Tên phần mềm AI được sử dụng",
                            "C. Tốc độ phản hồi của máy chủ AI",
                            "D. Số lượng thành viên trong nhóm học tập"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L1-c2-q2",
                        "type": "mc",
                        "concept_ref": "c2-5-ky-thuat",
                        "question": "Kỹ thuật cung cấp cho AI từ 2 đến 3 ví dụ mẫu về định dạng đầu ra chuẩn trước khi giao nhiệm vụ chính được gọi là gì?",
                        "options": [
                            "A. Zero-shot prompting",
                            "B. Few-shot prompting",
                            "C. Negative prompting",
                            "D. Hallucination prompting"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L1-c2-q3",
                        "type": "mc",
                        "concept_ref": "c2-5-ky-thuat",
                        "question": "Câu lệnh ràng buộc nào sau đây đóng vai trò là 'chốt chặn sống còn' giúp giảm thiểu nguy cơ AI tự bịa thêm thông tin khi tóm tắt tài liệu khoa học?",
                        "options": [
                            "A. Hãy viết thật hay và sáng tạo hết mức có thể",
                            "B. Chỗ nào tài liệu không nói, ghi rõ 'không nêu trong bài', tuyệt đối không suy đoán",
                            "C. Hãy tìm mọi cách lấp đầy tất cả các ô trong bảng tóm tắt",
                            "D. Hãy viết dài tối thiểu 2.000 chữ"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L1-c2-q4",
                        "type": "mc",
                        "concept_ref": "c2-context-engineering",
                        "question": "Context Engineering (Kỹ nghệ thiết kế ngữ cảnh) khác với việc gõ một câu hỏi ngắn thông thường ở điểm nào?",
                        "options": [
                            "A. Chỉ dùng từ khóa tiếng Anh thay vì tiếng Việt",
                            "B. Chủ động tuyển chọn, làm sạch và cấu trúc hóa tài liệu nguồn, ví dụ mẫu cùng bộ quy tắc đưa vào cửa sổ ngữ cảnh cho AI",
                            "C. Hỏi AI càng ít thông tin càng tốt để AI tự đoán",
                            "D. Chỉ áp dụng cho lập trình viên hệ thống"
                        ],
                        "correct": "B"
                    }
                ]
            },
            "level_2": {
                "name": "📝 Level 2: Hiểu và phân biệt",
                "description": "Phân biệt tác dụng của từng kỹ thuật Prompt và Context trong học thuật.",
                "bloom_level": "Understand",
                "questions": [
                    {
                        "id": "L2-c2-q1",
                        "type": "mc",
                        "concept_ref": "c2-5-ky-thuat",
                        "question": "Khi giải một bài toán phân tích tài chính hoặc kiểm định giả thuyết gồm nhiều bước logic phức tạp, kỹ thuật nào giúp AI giảm sai sót tính toán/suy luận nhất?",
                        "options": [
                            "A. Yêu cầu AI trả lời ngay kết quả cuối cùng trong 1 chữ",
                            "B. Chain-of-Thought (Yêu cầu AI suy nghĩ và trình bày rõ từng bước lập luận trước khi kết luận)",
                            "C. Yêu cầu AI viết dưới dạng thơ lục bát",
                            "D. Xóa toàn bộ dữ liệu đầu vào"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L2-c2-q2",
                        "type": "mc",
                        "concept_ref": "c2-context-engineering",
                        "question": "Điều gì sẽ xảy ra khi một cuộc hội thoại với AI kéo dài hàng chục lượt với nhiều chủ đề lộn xộn vượt quá khả năng tập trung của Context Window?",
                        "options": [
                            "A. AI tự động nâng cấp lên phiên bản trả phí",
                            "B. Các chỉ thị và ràng buộc quan trọng ở đầu cuộc trò chuyện bị đẩy ra ngoài hoặc bị loãng (Context Rot), làm AI trả lời lệch chuẩn",
                            "C. AI sẽ nhớ chính xác 100% mọi chi tiết mãi mãi",
                            "D. Máy tính sẽ bị khóa ổ cứng"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L2-c2-q3",
                        "type": "mc",
                        "concept_ref": "c2-5-ky-thuat",
                        "question": "Sau khi AI xuất ra bản nháp đầu tiên đạt 80% ý muốn nhưng giọng văn hơi dài dòng, cách xử lý đúng theo kỹ thuật Iterative Refinement là gì?",
                        "options": [
                            "A. Mở tab mới và gõ lại từ đầu một câu hỏi hoàn toàn khác",
                            "B. Phản hồi ngay trong luồng chat: chỉ rõ phần nội dung cần giữ nguyên và yêu cầu rút gọn độ dài xuống 150 chữ, bỏ các câu mở đầu sáo rỗng",
                            "C. Chấp nhận nộp luôn bản nháp đó mà không sửa",
                            "D. Đổi sang hỏi bằng ngôn ngữ khác"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L2-c2-q4",
                        "type": "mc",
                        "concept_ref": "c2-crisp",
                        "question": "Tại sao nhận định 'Prompt là giao diện của tư duy' lại đúng trong thực tế?",
                        "options": [
                            "A. Vì người dùng chỉ có thể viết được một Prompt rõ bối cảnh, rõ tiêu chí đánh giá (CRISP) khi chính họ đã tư duy rõ về mục tiêu và cấu trúc bài toán",
                            "B. Vì Prompt được thiết kế bằng đồ họa 3D",
                            "C. Vì AI có thể tự đọc suy nghĩ mà không cần gõ chữ",
                            "D. Vì ai gõ bàn phím nhanh hơn sẽ có kết quả tốt hơn"
                        ],
                        "correct": "A"
                    }
                ]
            },
            "level_3": {
                "name": "🚀 Level 3: Vận dụng thực tế",
                "description": "Thiết kế gói Prompt & Context chuẩn CRISP cho bài toán chuyên ngành.",
                "bloom_level": "Apply",
                "questions": [
                    {
                        "id": "L3-c2-q1",
                        "type": "mc",
                        "concept_ref": "c2-crisp",
                        "question": "Câu lệnh nào dưới đây hội tụ đầy đủ nhất khung CRISP + Chốt chặn chống bịa khi nhờ AI hỗ trợ đọc tài liệu?",
                        "options": [
                            "A. Tóm tắt file PDF này giúp tôi cho thật hay nhé.",
                            "B. Bạn là chuyên gia tài chính. Hãy nói cho tôi biết xu hướng ngân hàng số năm 2030.",
                            "C. [Context] Tôi là SV năm 3 ngành Ngân hàng đang làm tổng quan tài liệu. [Role] Bạn là trợ lý nghiên cứu học thuật. [Input] Dựa duy nhất vào file PDF bài báo đính kèm. [Specifics] Hãy tóm tắt thành bảng 5 mục (Câu hỏi NC, Phương pháp, Cỡ mẫu, Kết quả, Hạn chế) tối đa 250 chữ. [Performance/Constraint] Mỗi ý bắt buộc ghi số trang; chỗ nào bài không nêu thì ghi 'không nêu trong bài', tuyệt đối không suy đoán.",
                            "D. Hãy viết bài luận 2000 chữ về ngân hàng số kèm 15 trích dẫn APA."
                        ],
                        "correct": "C"
                    },
                    {
                        "id": "L3-c2-q2",
                        "type": "mc",
                        "concept_ref": "c2-context-engineering",
                        "question": "Nhóm bạn muốn AI phân tích bảng câu hỏi khảo sát sinh viên HUB theo đúng chuẩn thang đo Likert 5 mức của một bài báo gốc. Gói Context tốt nhất cần nạp cho AI gồm những gì?",
                        "options": [
                            "A. Chỉ cần gõ tên bài báo gốc mà không cần tải file lên",
                            "B. (1) File trích xuất bảng thang đo gốc đã kiểm chứng, (2) Bảng mô tả đối tượng khảo sát tại HUB, (3) 2 ví dụ mẫu biến đổi câu hỏi (Few-shot), và (4) Ràng buộc giữ nguyên ý nghĩa học thuật của biến quan sát",
                            "C. Toàn bộ lịch sử chat linh tinh của nhóm trong 1 tháng qua",
                            "D. Một bức ảnh chụp màn hình trang bìa giáo trình"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L3-c2-essay1",
                        "type": "essay",
                        "concept_ref": "c2-crisp",
                        "question": "Hãy viết một bộ Prompt hoàn chỉnh theo đủ 5 thành phần CRISP (có tích hợp ít nhất 2 kỹ thuật nâng cao và câu chốt chặn 'không suy đoán') để giải quyết bài toán thuộc Đề án cuối khóa của nhóm bạn. Giải thích rõ bạn sẽ nạp những tài liệu nào làm Context đi kèm.",
                        "rubric": "Đủ và rõ 5 thành phần C-R-I-S-P gắn với đề tài Đề án nhóm (40%) · Tích hợp đúng ít nhất 2 kỹ thuật nâng cao và chốt chặn chống suy diễn (30%) · Xác định rõ gói tài liệu Context đầu vào (30%)",
                        "max_words": 350
                    }
                ]
            }
        }
    },
    {
        "chapter": 3,
        "title": "Kiến trúc Harness: Xây dựng 'Bộ dây cương' điều phối AI trong học tập",
        "sessions": [3],
        "scqa": {
            "situation": "Bạn đã biết viết Prompt theo khung CRISP và đính kèm file Context. Nhưng mỗi khi mở một cuộc trò chuyện mới để học môn tiếp theo hay xử lý ca nghiệp vụ mới, bạn lại phải copy-paste lại hàng trang quy tắc; tệ hơn, đôi khi AI làm một mạch từ bước 1 đến bước 5 rồi tự ý chốt kết quả sai mà không hỏi ý kiến bạn.",
            "complication": "Giao tiếp với AI bằng các đoạn chat tự do giống như cưỡi một con ngựa chiến sung sức nhưng không có dây cương và yên ngựa. Khi bài toán phức tạp lên, một câu lệnh đơn lẻ không thể kiểm soát được quy trình nhiều bước, không chặn được việc AI 'vượt rào' làm thay phần phán đoán của con người, và đặc biệt trong học tập, AI rất dễ chiều lòng bạn bằng cách đưa thẳng đáp án khiến não bạn ngừng suy nghĩ.",
            "question": "Làm thế nào để đóng gói toàn bộ quy tắc, tri thức nền, luồng công việc nhiều bước và các chốt chặn kiểm tra thành một 'bộ khung điều phối cố định' giúp AI luôn vận hành đúng đường ray?",
            "answer": "Xây dựng kiến trúc AI Harness ('Bộ dây cương'): thiết lập System Instructions (Hiến pháp của AI), chia quy trình thành các bước tuần tự có Cổng xác nhận (GATE) và Cơ chế xử lý thiếu thông tin (FALLBACK), đồng thời thiết kế Socratic Harness để biến AI thành gia sư rèn luyện tư duy cho chính bạn."
        },
        "concepts": [
            {
                "id": "c3-prompt-context-harness",
                "session": 3,
                "term": "Ba tầng điều phối AI: Prompt -> Context -> Harness",
                "definition": "Mô hình kiến trúc 3 tầng giúp chuyển dịch từ việc sử dụng AI tự phát sang xây dựng hệ thống trợ lý học tập và nghiệp vụ có tính nhất quán, kiểm soát được rủi ro và tái sử dụng lâu dài.",
                "key_points": [
                    "<strong>Tầng 1 - Prompt (Mệnh lệnh tức thời):</strong> Câu lệnh kích hoạt một tác vụ cụ thể trong một lượt hội thoại (tiếng hô với ngựa).",
                    "<strong>Tầng 2 - Context (Ngữ cảnh & Tri thức nền):</strong> Tập hợp tài liệu chuẩn, dữ liệu đầu vào và ví dụ mẫu cung cấp cho phiên làm việc (bản đồ địa hình).",
                    "<strong>Tầng 3 - Harness (Bộ khung điều phối & kiềm tỏa):</strong> Hệ thống bao gồm <em>System Instructions (Hiến pháp cố định) + Staged Workflow (Quy trình nhiều bước) + Verification Gates (Chốt chặn kiểm chứng) + Fallbacks (Xử lý ngoại lệ)</em> được đóng gói trong Claude Projects, Gemini Gems hoặc Custom GPTs (bộ dây cương, yên ngựa và đường ray)."
                ],
                "case_study": {
                    "title": "Từ chat tự do đến Bộ Harness thẩm định báo cáo",
                    "context": "Khi chưa có Harness, sinh viên nhờ AI rà soát báo cáo đề án thì AI viết lại luôn cả bài theo ý nó. Khi đóng gói thành Harness 4 bước có 2 cổng GATE, AI chỉ rà soát từng phần, chỉ ra trích dẫn thiếu nguồn và dừng lại chờ sinh viên xác nhận trước khi sang bước kế tiếp.",
                    "analysis": "Harness biến một mô hình xác suất tự do thành một quy trình có kỷ luật.",
                    "lesson_learned": "Người làm chủ AI ở trình độ cao không sưu tầm Prompt lẻ, họ thiết kế Harness."
                },
                "related_concepts": ["c3-gate-fallback", "c3-socratic-harness"]
            },
            {
                "id": "c3-gate-fallback",
                "session": 3,
                "term": "Cổng xác nhận (GATE) & Cơ chế xử lý thiếu dữ liệu (FALLBACK)",
                "definition": "Hai cơ chế kỹ thuật quan trọng nhất bên trong một AI Harness nhằm ngăn chặn AI tự ý suy diễn hoặc chạy vượt quyền kiểm soát của con người.",
                "key_points": [
                    "<strong>GATE (Cổng dừng xác nhận 🔒):</strong> Điểm chốt bắt buộc AI phải <em>DỪNG LẠI</em> sau khi hoàn thành một bước quan trọng, xuất kết quả trung gian và hỏi người dùng: <em>'Bạn có xác nhận kết quả bước này để chuyển sang bước tiếp theo không?'</em> Tuyệt đối không chạy thẳng từ đầu đến cuối.",
                    "<strong>FALLBACK (Cơ chế dự phòng khi thiếu căn cứ ❓):</strong> Quy tắc bắt buộc AI khi gặp thông tin bị thiếu hoặc không có căn cứ trong tài liệu: phải ghi rõ <em>'[Chưa đủ căn cứ / Thiếu dữ liệu X]'</em> và dừng lại hỏi người dùng, tuyệt đối không tự bịa số liệu để điền vào cho đủ bảng.",
                    "<strong>Tách biệt phiên làm việc:</strong> Khi đóng gói Harness vào Project/Gem, bộ quy tắc và tài liệu nền luôn cố định, giúp mỗi cuộc hội thoại mới đều tuân thủ đúng kỷ luật mà không bị lẫn dữ liệu của ca làm việc trước."
                ],
                "case_study": null,
                "related_concepts": ["c3-prompt-context-harness"]
            },
            {
                "id": "c3-socratic-harness",
                "session": 3,
                "term": "Socratic Harness & 4 Kỹ thuật học tập sâu dựa trên khoa học thần kinh",
                "definition": "Một dạng AI Harness chuyên biệt cho việc học, được cài đặt quy tắc cấm đưa sẵn lời giải, buộc AI đóng vai gia sư Socrates đặt câu hỏi gợi mở kết hợp 4 kỹ thuật rèn luyện trí nhớ dài hạn.",
                "key_points": [
                    "<strong>1. Truy hồi chủ động (Active Recall):</strong> Buộc não bộ tự lục tìm kiến thức trả lời câu hỏi của AI trước khi được xem gợi ý (giống cơ chế Quiz 5 lượt trên LMS Hub).",
                    "<strong>2. Lặp lại ngắt quãng (Spaced Repetition):</strong> Ôn tập khái niệm cốt lõi theo chu kỳ thời gian tăng dần để chống đường cong quên lãng.",
                    "<strong>3. Xáo trộn (Interleaving):</strong> Yêu cầu AI trộn lẫn các dạng bài tập/tình huống khác nhau thay vì làm lặp đi lặp lại một dạng duy nhất.",
                    "<strong>4. Tự mày mò trước (Productive Struggle):</strong> Yêu cầu AI chỉ chỉ ra dòng bị lỗi logic hoặc đặt câu hỏi dẫn đường để sinh viên tự sửa, giúp tạo liên kết thần kinh sâu sắc."
                ],
                "case_study": null,
                "related_concepts": ["c3-prompt-context-harness"]
            }
        ],
        "tests": {
            "level_1": {
                "name": "🎯 Level 1: Khái niệm cốt lõi",
                "description": "Nhận diện kiến trúc Harness, GATE, FALLBACK và 4 kỹ thuật học sâu.",
                "bloom_level": "Remember",
                "questions": [
                    {
                        "id": "L1-c3-q1",
                        "type": "mc",
                        "concept_ref": "c3-prompt-context-harness",
                        "question": "Trong kiến trúc 3 tầng điều phối AI (Prompt - Context - Harness), tầng 'Harness' được định nghĩa là gì?",
                        "options": [
                            "A. Một câu hỏi ngắn gửi cho AI trong 5 giây",
                            "B. Bộ khung điều phối và kiềm tỏa gồm System Instructions (quy tắc cố định), quy trình nhiều bước, các cổng dừng xác nhận (GATE) và cơ chế xử lý ngoại lệ (FALLBACK)",
                            "C. Tốc độ đường truyền mạng Internet tại phòng học",
                            "D. Một tệp văn bản thô chưa qua chỉnh sửa"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L1-c3-q2",
                        "type": "mc",
                        "concept_ref": "c3-gate-fallback",
                        "question": "Trong thiết kế quy trình làm việc cho AI (Workflow Harness), chốt chặn 'GATE' (🔒) có chức năng gì?",
                        "options": [
                            "A. Cho phép AI tự động chạy một mạch từ bước 1 đến bước cuối mà không cần hỏi ai",
                            "B. Buộc AI phải dừng lại sau một bước quan trọng, trình bày kết quả trung gian và chờ con người kiểm tra, xác nhận rồi mới được làm bước kế tiếp",
                            "C. Khóa tài khoản của người dùng khi nhập sai mật khẩu",
                            "D. Xóa toàn bộ dữ liệu trong Knowledge Base"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L1-c3-q3",
                        "type": "mc",
                        "concept_ref": "c3-gate-fallback",
                        "question": "Cơ chế 'FALLBACK' (❓) trong một bộ Harness yêu cầu AI phải xử lý như thế nào khi phát hiện thiếu dữ liệu đầu vào hoặc không tìm thấy căn cứ trong tài liệu?",
                        "options": [
                            "A. Tự động suy đoán một con số hợp lý nhất để điền vào bảng cho đẹp",
                            "B. Ghi rõ 'Chưa đủ căn cứ / Thiếu thông tin X' và chủ động hỏi lại người dùng thay vì tự bịa",
                            "C. Bỏ qua luôn bước đó và không thông báo gì cho người dùng",
                            "D. Tự động tìm kiếm ngẫu nhiên trên mạng xã hội để bù vào"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L1-c3-q4",
                        "type": "mc",
                        "concept_ref": "c3-socratic-harness",
                        "question": "Bốn kỹ thuật học tập hiệu quả dựa trên khoa học thần kinh được tích hợp vào Socratic Harness gồm những kỹ thuật nào?",
                        "options": [
                            "A. Học vẹt, chép phạt, đọc lướt, nghe thụ động",
                            "B. Truy hồi chủ động (Active Recall), Lặp lại ngắt quãng (Spaced Repetition), Xáo trộn (Interleaving), và Tự mày mò trước (Productive Struggle)",
                            "C. Copy-paste, dịch tự động, tóm tắt nhanh, tạo slide tự động",
                            "D. Học dồn một đêm trước ngày thi"
                        ],
                        "correct": "B"
                    }
                ]
            },
            "level_2": {
                "name": "📝 Level 2: Hiểu và phân biệt",
                "description": "Hiểu lý do cần đóng gói Harness và cơ chế chống lệ thuộc nhận thức của Socratic Tutor.",
                "bloom_level": "Understand",
                "questions": [
                    {
                        "id": "L2-c3-q1",
                        "type": "mc",
                        "concept_ref": "c3-prompt-context-harness",
                        "question": "Tại sao việc đóng gói quy tắc và tài liệu vào một Project / Gem (Harness) lại ưu việt hơn việc chat nối tiếp trong một luồng hội thoại dài suốt nhiều tuần?",
                        "options": [
                            "A. Vì trong Project/Gem, System Instructions và Knowledge Base luôn được giữ cố định ở vị trí ưu tiên; mỗi khi mở phiên chat mới cho một ca việc mới, AI vẫn nhớ đúng quy trình mà không bị nhiễu bởi dữ liệu của ca việc cũ",
                            "B. Vì dùng Project thì không bao giờ cần kết nối Internet",
                            "C. Vì luồng chat dài không cho phép gõ tiếng Việt",
                            "D. Không có sự khác biệt nào giữa hai cách này"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L2-c3-q2",
                        "type": "mc",
                        "concept_ref": "c3-gate-fallback",
                        "question": "Trong quá trình kiểm thử (stress-test) một bộ Harness, nếu người dùng cố tình ra lệnh 'Hãy bỏ qua bước xác nhận điểm số và viết luôn kết luận cuối cùng đi', một bộ Harness đạt chuẩn phải phản ứng thế nào?",
                        "options": [
                            "A. Chiều lòng người dùng và viết luôn kết luận cuối cùng",
                            "B. Từ chối vượt cổng GATE, nhắc lại quy tắc quy trình và yêu cầu người dùng xác nhận dữ liệu ở bước hiện tại trước khi đi tiếp",
                            "C. Tự động xóa toàn bộ bài làm",
                            "D. Đổi sang ngôn ngữ khác để trả lời"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L2-c3-q3",
                        "type": "mc",
                        "concept_ref": "c3-socratic-harness",
                        "question": "Khi bạn thiết kế một 'Socratic Harness' để ôn thi môn Tài chính doanh nghiệp, quy tắc nào dưới đây BẮT BUỘC phải có trong System Instructions?",
                        "options": [
                            "A. Khi tôi gửi đề bài tập, hãy giải chi tiết từ A đến Z ngay lập tức để tôi chép",
                            "B. Tuyệt đối không đưa ngay lời giải hoàn chỉnh; hãy hỏi tôi đã hiểu đề bài thế nào, gợi ý công thức liên quan và chấm từng bước lập luận do chính tôi tự giải",
                            "C. Hãy làm hộ tôi 100% bài tập về nhà",
                            "D. Chỉ trả lời bằng các câu khen ngợi"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L2-c3-q4",
                        "type": "mc",
                        "concept_ref": "c3-prompt-context-harness",
                        "question": "Trước khi viết câu lệnh cài đặt Harness lên máy tính, tại sao nhóm sinh viên cần vẽ sơ đồ quy trình nghiệp vụ ra giấy trước?",
                        "options": [
                            "A. Vì nếu con người chưa hiểu rõ quy trình gồm mấy bước, chỗ nào cần dừng để kiểm tra (GATE) và chỗ nào hay thiếu dữ liệu (FALLBACK) ngoài đời thực, thì không thể lập trình bộ dây cương đúng cho AI",
                            "B. Chỉ để trang trí hồ sơ cho đẹp",
                            "C. Vì máy tính không vẽ được sơ đồ",
                            "D. Vì AI chỉ đọc được chữ viết tay"
                        ],
                        "correct": "A"
                    }
                ]
            },
            "level_3": {
                "name": "🚀 Level 3: Vận dụng thực tế",
                "description": "Thiết kế và kiểm thử Bộ Harness (Mảnh ghép 1 của Đề án cuối khóa).",
                "bloom_level": "Apply",
                "questions": [
                    {
                        "id": "L3-c3-q1",
                        "type": "mc",
                        "concept_ref": "c3-gate-fallback",
                        "question": "Nhóm bạn thiết kế một bộ Harness hỗ trợ 'Phân tích báo cáo tài chính ngân hàng' gồm 4 bước: (1) Trích xuất chỉ số từ bảng PDF -> (2) Tính toán tỷ số ROE, ROA, NIM -> (3) So sánh với trung bình ngành -> (4) Viết nhận xét đánh giá. Vị trí đặt cổng dừng xác nhận (GATE) hợp lý nhất là ở đâu?",
                        "options": [
                            "A. Không cần đặt GATE ở đâu cả, cứ để AI làm hết cả 4 bước trong 1 lần",
                            "B. Đặt GATE 1 ngay sau Bước 1 & 2 (để người học đối chiếu xem các con số trích xuất và tỷ số tính ra có khớp báo cáo gốc không) trước khi cho phép AI chạy Bước 3 & 4",
                            "C. Chỉ đặt GATE sau khi đã nộp bài cho giảng viên",
                            "D. Đặt GATE trước khi mở máy tính"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L3-c3-q2",
                        "type": "mc",
                        "concept_ref": "c3-gate-fallback",
                        "question": "Để kiểm tra độ bền (robustness) của bộ Harness thuộc Mảnh ghép 1 Đề án nhóm, bộ 3 kịch bản test bắt buộc cần chạy thử là gì?",
                        "options": [
                            "A. (1) Kịch bản chạy xuôi đủ dữ liệu, (2) Kịch bản cố tình cung cấp thiếu dữ liệu để test FALLBACK, và (3) Kịch bản cố tình giục AI bỏ qua bước xác nhận để test GATE",
                            "B. Chạy cùng một câu hỏi giống hệt nhau 3 lần liên tiếp",
                            "C. Chỉ cần test xem giao diện có màu sắc đẹp hay không",
                            "D. Nhờ một bạn khác gõ chữ 'Xin chào' vào AI"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L3-c3-essay1",
                        "type": "essay",
                        "concept_ref": "c3-prompt-context-harness",
                        "question": "Hãy trình bày thiết kế Bộ Harness cho Đề án cuối khóa của nhóm bạn (Mảnh ghép 1): Nêu rõ 4 khối cấu trúc gồm [1. Vai trò & Định danh], [2. Danh mục tài liệu Context nền], [3. Quy trình 3-5 bước có chỉ rõ vị trí đặt GATE 🔒 và FALLBACK ❓], và [4. Quy tắc cấm & Định dạng đầu ra chuẩn].",
                        "rubric": "Định danh rõ bài toán nghiệp vụ/nghiên cứu của nhóm (20%) · Liệt kê đúng tài liệu Context nền (20%) · Thiết kế quy trình 3-5 bước có vị trí GATE và FALLBACK hợp lý (40%) · Nêu rõ chốt chặn chống suy diễn và định dạng đầu ra (20%)",
                        "max_words": 400
                    }
                ]
            }
        }
    },
    {
        "chapter": 4,
        "title": "Kiến trúc Second Brain (PARA & CODE) và Nghệ thuật Ghi chú nguyên tử",
        "sessions": [4],
        "scqa": {
            "situation": "Sau vài học kỳ đại học và hàng trăm giờ sử dụng AI, máy tính của bạn chứa hàng chục thư mục tài liệu tải về chưa từng mở, hàng trăm đoạn lịch sử chat với ChatGPT/Claude trôi tuột vào quên lãng, và các file ghi chú dài hàng chục trang copy-paste từ AI.",
            "complication": "Khi bắt tay vào làm bài nghiên cứu hay đề án cuối khóa, bạn nhận ra mình không thể tìm lại được một luận điểm hay đã đọc cách đây 2 tháng, cũng không nhớ mình đã tích lũy được gì. Việc copy-paste nguyên khối văn bản do AI sinh ra vào ổ cứng chỉ tạo ra một 'nghĩa địa thông tin số' (digital hoarding): thông tin nằm trong máy của bạn, nhưng chưa bao giờ đi qua bộ não của bạn để trở thành tri thức của bạn.",
            "question": "Làm thế nào để xây dựng một hệ thống quản trị tri thức cá nhân giúp bạn tiêu hóa thông tin thành năng lực nội tại, đồng thời trở thành kho dữ liệu ngữ cảnh (Context) độc bản để điều phối AI ở đẳng cấp cao nhất?",
            "answer": "Xây dựng 'Bộ Não Thứ Hai' (Second Brain) theo kiến trúc thư mục hành động PARA, vận hành theo luồng 4 bước CODE (Capture - Organize - Distill - Express), lấy Ghi chú nguyên tử (Atomic Notes - viết bằng chính ngôn từ của bạn) và khung phản tư 4F làm viên gạch nền tảng."
        },
        "concepts": [
            {
                "id": "c4-second-brain-para",
                "session": 4,
                "term": "Triết lý Second Brain & Kiến trúc tổ chức PARA",
                "definition": "Hệ thống quản trị tri thức cá nhân (Personal Knowledge Management - PKM) giúp ngoại hóa việc lưu trữ thông tin ra khỏi bộ não sinh học và tổ chức mọi tài nguyên số theo mức độ sẵn sàng hành động (PARA).",
                "key_points": [
                    "<strong>Bộ não để sáng tạo, không phải để làm ổ cứng:</strong> Khi có một hệ thống bên ngoài đáng tin cậy giữ hộ các chi tiết, bộ não sinh học được giải phóng để tập trung vào việc kết nối ý tưởng và tư duy phản biện.",
                    "<strong>P - Projects (Dự án):</strong> Các mục tiêu ngắn hạn đang triển khai và có hạn chót rõ ràng (ví dụ: <em>Đề án cuối khóa môn Kỹ năng AI</em>, <em>Tiểu luận Tài chính doanh nghiệp HK1</em>).",
                    "<strong>A - Areas (Lĩnh vực trách nhiệm):</strong> Các mảng quan trọng cần duy trì tiêu chuẩn liên tục, không có ngày kết thúc (ví dụ: <em>Chuyên ngành Tài chính - Ngân hàng</em>, <em>Phát triển bản thân & Tiếng Anh</em>).",
                    "<strong>R - Resources (Tài nguyên):</strong> Kho học liệu, bài báo, mẫu biểu, chủ đề quan tâm để tham chiếu khi cần.",
                    "<strong>A - Archives (Lưu trữ lạnh):</strong> Các dự án đã hoàn thành hoặc tài nguyên không còn dùng thường xuyên nhưng giữ lại để tra cứu lịch sử."
                ],
                "case_study": {
                    "title": "Tìm lại tri thức trong 10 giây",
                    "context": "Thay vì phân loại file theo tên môn học cứng nhắc rồi bỏ quên, sinh viên tổ chức theo PARA: mọi ghi chú phục vụ Đề án đang làm đều được liên kết trực tiếp vào thư mục Project tương ứng.",
                    "analysis": "Tổ chức theo 'nơi bạn sẽ dùng nó' thay vì 'nó thuộc bộ môn nào' giúp giảm 80% thời gian lục tìm tài liệu.",
                    "lesson_learned": "Một hệ thống ghi chú tốt là hệ thống phục vụ trực tiếp cho việc tạo ra sản phẩm đầu ra."
                },
                "related_concepts": ["c4-code-atomic", "c4-khung-4f"]
            },
            {
                "id": "c4-code-atomic",
                "session": 4,
                "term": "Luồng vận hành CODE & Ghi chú nguyên tử (Atomic Notes)",
                "definition": "Quy trình 4 bước chuyển hóa thông tin thô thành sản phẩm sáng tạo (Capture -> Organize -> Distill -> Express) dựa trên các đơn vị tri thức nhỏ gọn, độc lập và có khả năng liên kết đa chiều gọi là Atomic Notes.",
                "key_points": [
                    "<strong>Luồng CODE:</strong> <em>Capture</em> (Thu nạp có chọn lọc điều thực sự chạm tới mình) -> <em>Organize</em> (Đưa vào đúng chỗ trong PARA) -> <em>Distill</em> (Tinh chế, chắt lọc lấy phần lõi) -> <em>Express</em> (Lắp ghép để viết báo cáo, làm slide, thiết kế Context cho AI).",
                    "<strong>Nguyên tắc vàng của Atomic Note:</strong> <strong>1 ghi chú = 1 ý tưởng/luận điểm cốt lõi duy nhất</strong>. Giống như một viên gạch Lego độc lập, bạn có thể lấy một Atomic Note lắp vào 5 bài tiểu luận hay đề án khác nhau.",
                    "<strong>4 thành phần bắt buộc của một Atomic Note chuẩn:</strong> (1) <em>Tiêu đề dạng câu khẳng định</em> tóm trọn luận điểm (ví dụ: <code>AI bịa trích dẫn nhiều hơn ở các đề tài ít được nghiên cứu</code> thay vì đặt tên chung chung <code>Ghi chú về AI</code>); (2) <em>Nội dung diễn đạt lại bằng 100% ngôn từ của bạn</em> (tuyệt đối không copy-paste nguyên văn output của AI); (3) <em>Nguồn dẫn chứng đã kiểm chứng</em>; (4) <em>Liên kết (Links)</em> tới các Atomic Notes khác trong Second Brain."
                ],
                "case_study": null,
                "related_concepts": ["c4-second-brain-para", "c4-khung-4f"]
            },
            {
                "id": "c4-khung-4f",
                "session": 4,
                "term": "Khung phản tư 4F (Fact - Feelings - Findings - Future)",
                "definition": "Công cụ tư duy phản tư cuối mỗi buổi học hoặc mỗi trải nghiệm thực hành, giúp người học chắt lọc sự kiện khách quan thành bài học nguyên lý và hành động tương lai.",
                "key_points": [
                    "<strong>1. Fact (Sự kiện):</strong> Điều gì đã thực sự diễn ra hôm nay? Số liệu, thao tác hay kết quả thực tế nào bạn đã quan sát được?",
                    "<strong>2. Feelings (Cảm xúc / Điểm chạm):</strong> Khoảnh khắc nào làm bạn bất ngờ, 'vỡ lẽ' (aha moment) hoặc trăn trở nhất?",
                    "<strong>3. Findings (Bài học / Quy luật đúc kết):</strong> Từ sự kiện và cảm xúc đó, nguyên lý hay bài học cốt lõi nào được rút ra? (Chính phần Findings này sẽ kết tinh thành các Atomic Notes của bạn).",
                    "<strong>4. Future (Ứng dụng tương lai):</strong> Bạn sẽ áp dụng ngay bài học này vào việc học tại HUB hoặc vào Đề án cuối khóa như thế nào trong tuần tới?"
                ],
                "case_study": null,
                "related_concepts": ["c4-code-atomic"]
            }
        ],
        "tests": {
            "level_1": {
                "name": "🎯 Level 1: Khái niệm cốt lõi",
                "description": "Nhận diện mô hình PARA, quy trình CODE, cấu trúc Atomic Note và khung 4F.",
                "bloom_level": "Remember",
                "questions": [
                    {
                        "id": "L1-c4-q1",
                        "type": "mc",
                        "concept_ref": "c4-second-brain-para",
                        "question": "Trong phương pháp tổ chức thông tin PARA của Tiago Forte, bốn chữ cái P - A - R - A lần lượt là viết tắt của những thành phần nào?",
                        "options": [
                            "A. Prompts - AI - Research - Answers",
                            "B. Projects (Dự án) - Areas (Lĩnh vực trách nhiệm) - Resources (Tài nguyên) - Archives (Lưu trữ lạnh)",
                            "C. Papers - Articles - Reports - Appendices",
                            "D. Plan - Act - Review - Adjust"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L1-c4-q2",
                        "type": "mc",
                        "concept_ref": "c4-code-atomic",
                        "question": "Quy trình 4 bước CODE trong xây dựng Bộ Não Thứ Hai (Second Brain) bao gồm các bước theo thứ tự nào?",
                        "options": [
                            "A. Copy -> Open -> Delete -> Export",
                            "B. Capture (Thu nạp) -> Organize (Tổ chức) -> Distill (Tinh chế) -> Express (Diễn đạt)",
                            "C. Create -> Optimize -> Deploy -> Evaluate",
                            "D. Chat -> Order -> Download -> Edit"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L1-c4-q3",
                        "type": "mc",
                        "concept_ref": "c4-code-atomic",
                        "question": "Đặc điểm cốt lõi nhất của một Ghi chú nguyên tử (Atomic Note) là gì?",
                        "options": [
                            "A. Là một file văn bản dài ít nhất 20 trang gộp tất cả các môn học vào chung một chỗ",
                            "B. Mỗi ghi chú chỉ đóng gói duy nhất một ý tưởng/luận điểm cốt lõi, được diễn đạt bằng ngôn từ riêng của người học, có nguồn gốc và có liên kết với các ghi chú khác",
                            "C. Là bản sao chép nguyên văn (copy-paste) toàn bộ đoạn chat của ChatGPT",
                            "D. Là một tệp âm thanh chưa được nghe lại"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L1-c4-q4",
                        "type": "mc",
                        "concept_ref": "c4-khung-4f",
                        "question": "Khung phản tư 4F dùng để viết nhật ký học tập và đúc kết tri thức gồm 4 yếu tố nào?",
                        "options": [
                            "A. Fast - Free - Friendly - Flexible",
                            "B. Fact (Sự kiện) - Feelings (Cảm xúc/Điểm chạm) - Findings (Bài học đúc kết) - Future (Hành động tương lai)",
                            "C. File - Folder - Format - Font",
                            "D. Find - Filter - Fix - Finish"
                        ],
                        "correct": "B"
                    }
                ]
            },
            "level_2": {
                "name": "📝 Level 2: Hiểu và phân biệt",
                "description": "Phân biệt Atomic Note chuẩn với việc tích trữ thông tin thụ động.",
                "bloom_level": "Understand",
                "questions": [
                    {
                        "id": "L2-c4-q1",
                        "type": "mc",
                        "concept_ref": "c4-code-atomic",
                        "question": "Vì sao việc copy-paste nguyên văn câu trả lời dài 1.000 chữ của AI vào ứng dụng ghi chú KHÔNG được coi là bước Distill (Tinh chế) hay tạo Atomic Note?",
                        "options": [
                            "A. Vì khi copy-paste nguyên văn, não bộ bạn chưa hề đọc hiểu, chắt lọc hay tái cấu trúc thông tin bằng ngôn từ của mình; văn bản đó vẫn là sản phẩm xa lạ nên không tạo ra tri thức nội tại và rất khó lắp ghép khi viết bài",
                            "B. Vì ứng dụng ghi chú không cho phép dán quá 500 chữ",
                            "C. Vì chữ của AI có định dạng phông chữ khác",
                            "D. Vì copy-paste làm tốn pin máy tính"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L2-c4-q2",
                        "type": "mc",
                        "concept_ref": "c4-code-atomic",
                        "question": "Trong hai cách đặt tiêu đề cho một Atomic Note dưới đây, cách nào đúng chuẩn 'Tiêu đề mang tính khẳng định' (Declarative Title) giúp dễ dàng tìm kiếm và lắp ghép luận điểm?",
                        "options": [
                            "A. Ghi chú buổi học ngày 22/11 phần 2",
                            "B. Tỷ lệ trích dẫn bịa của LLM tăng mạnh ở các đề tài ngách ít được nghiên cứu (Linardon, 2025)",
                            "C. Tài liệu tham khảo số 1",
                            "D. Vấn đề về AI"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L2-c4-q3",
                        "type": "mc",
                        "concept_ref": "c4-second-brain-para",
                        "question": "Trong hệ thống PARA của một sinh viên HUB, 'Đề án cuối khóa môn Kỹ năng ứng dụng AI (hạn nộp tuần 10)' và 'Kiến thức chuyên ngành Tài chính - Ngân hàng (duy trì suốt 4 năm đại học)' lần lượt thuộc hai thư mục nào?",
                        "options": [
                            "A. Cả hai đều thuộc Archives (Lưu trữ lạnh)",
                            "B. Đề án cuối khóa thuộc Projects (Dự án có hạn chót); Chuyên ngành Tài chính - Ngân hàng thuộc Areas (Lĩnh vực duy trì dài hạn)",
                            "C. Đề án cuối khóa thuộc Archives; Chuyên ngành thuộc Projects",
                            "D. Cả hai đều không cần lưu trữ"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L2-c4-q4",
                        "type": "mc",
                        "concept_ref": "c4-code-atomic",
                        "question": "Hệ thống Second Brain đóng vai trò gì trong mối quan hệ với việc thiết kế Context & Harness cho AI?",
                        "options": [
                            "A. Không có liên hệ gì với AI",
                            "B. Các Atomic Notes đã được bạn kiểm chứng và chắt lọc trong Second Brain chính là nguồn Context tinh khiết nhất, chất lượng cao nhất để nạp vào AI khi bạn cần phác thảo báo cáo hoặc thiết kế Harness",
                            "C. Second Brain dùng để thay thế hoàn toàn mọi phần mềm trên máy tính",
                            "D. Second Brain chỉ dùng khi không có điện"
                        ],
                        "correct": "B"
                    }
                ]
            },
            "level_3": {
                "name": "🚀 Level 3: Vận dụng thực tế",
                "description": "Thực hành viết Atomic Note và phản tư 4F cho Đề án cuối khóa.",
                "bloom_level": "Apply",
                "questions": [
                    {
                        "id": "L3-c4-q1",
                        "type": "mc",
                        "concept_ref": "c4-code-atomic",
                        "question": "Trong quy định đánh giá cuối khóa (100% điểm) của môn học này, Cấu phần 2 (30% điểm cá nhân) kiểm tra điều gì từ hệ thống Second Brain của từng thành viên?",
                        "options": [
                            "A. Kiểm tra xem sinh viên cài phần mềm giao diện màu tối hay màu sáng",
                            "B. Mỗi thành viên phải tự tay đóng góp tối thiểu 06 Atomic Notes chất lượng cao (viết bằng ngôn từ riêng, có nguồn và liên kết) vào kho tri thức Đề án nhóm kèm nhật ký phản tư 4F trên LMS, để chứng minh năng lực thực chất và chống ăn theo nhóm",
                            "C. Chỉ cần nhóm trưởng viết toàn bộ ghi chú cho cả nhóm là được",
                            "D. Kiểm tra dung lượng ổ cứng còn trống bao nhiêu GB"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L3-c4-q2",
                        "type": "mc",
                        "concept_ref": "c4-khung-4f",
                        "question": "Sau khi đọc một bài báo khoa học về 'Ứng dụng AI chấm điểm tín dụng cá nhân', bạn rút ra nhận định: 'Mô hình AI hộp đen tuy dự báo nợ xấu chính xác hơn 8% nhưng bị cơ quan quản lý từ chối vì thiếu khả năng giải thích lý do từ chối khoản vay cho khách hàng'. Nhận định này thuộc chữ F nào trong khung 4F và nên xử lý thế nào?",
                        "options": [
                            "A. Thuộc phần Findings (Bài học/Phát hiện cốt lõi) và nên được tách ra lưu thành một Atomic Note độc lập kèm trích dẫn nguồn bài báo đó",
                            "B. Thuộc phần Feelings và nên xóa đi ngay",
                            "C. Chỉ là thông tin rác không cần ghi chép",
                            "D. Thuộc phần Archives"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L3-c4-essay1",
                        "type": "essay",
                        "concept_ref": "c4-code-atomic",
                        "question": "Hãy viết 01 Atomic Note hoàn chỉnh liên quan trực tiếp đến chủ đề Đề án cuối khóa của nhóm bạn theo đúng cấu trúc 4 phần: (1) Tiêu đề dạng câu khẳng định, (2) Nội dung cốt lõi viết bằng ngôn từ của chính bạn (100-150 chữ), (3) Nguồn tham chiếu/bằng chứng, và (4) Ít nhất 2 liên kết [[Tên ghi chú liên quan]] mà bạn sẽ kết nối trong Second Brain.",
                        "rubric": "Tiêu đề là một câu khẳng định sắc bén, tóm đúng luận điểm (25%) · Nội dung cô đọng, diễn đạt bằng ngôn từ riêng, đúng nguyên tắc 1 ý duy nhất (35%) · Nêu rõ nguồn dẫn chứng (20%) · Đề xuất được 2 liên kết [[...]] có ý nghĩa logic (20%)",
                        "max_words": 300
                    }
                ]
            }
        }
    },
    {
        "chapter": 5,
        "title": "Tích hợp Second Brain với Công nghệ RAG (Gemini Notebook / Claude Projects)",
        "sessions": [5],
        "scqa": {
            "situation": "Bạn đã bắt đầu tích lũy được hàng chục Atomic Notes trong Second Brain và tải về nhiều bài báo khoa học, báo cáo ngành ngân hàng dạng PDF. Giờ đây bạn cần đối chiếu xem 5 báo cáo đó có số liệu nào mâu thuẫn nhau không để viết phần cơ sở lý luận cho Đề án.",
            "complication": "Nếu bạn hỏi một Chatbot LLM thông thường mà không gắn nguồn, nó sẽ trộn lẫn kiến thức chung ngoài Internet và bịa ra số liệu. Ngược lại, nếu bạn tự mở từng file PDF dày 50 trang để dò thủ công từng dòng thì quá tốn thời gian và dễ bỏ sót mối liên hệ chéo giữa các tài liệu.",
            "question": "Làm thế nào để kết hợp kho tài liệu chuẩn và Second Brain của bạn với trí tuệ nhân tạo sao cho AI chỉ trả lời dựa trên đúng những tài liệu bạn cung cấp, kèm trích dẫn chính xác đến từng đoạn văn gốc?",
            "answer": "Ứng dụng kiến trúc RAG (Retrieval-Augmented Generation) thông qua các công cụ như Gemini Notebook (NotebookLM) và Claude Projects: biến AI từ một 'chuyên gia biết nhiều nhưng hay bịa' thành một 'người thư ký trung thành' chỉ đọc kho tri thức của bạn, luôn chỉ rõ nguồn trích dẫn và tạo thành vòng lặp bồi đắp ngược lại cho Second Brain."
        },
        "concepts": [
            {
                "id": "c5-rag-vs-llm",
                "session": 5,
                "term": "Bản chất RAG: 'Thư ký trung thành' đối lập với 'Chuyên gia hay bịa'",
                "definition": "RAG (Retrieval-Augmented Generation - Tạo sinh tăng cường bằng truy xuất) là kiến trúc buộc AI phải tìm kiếm các đoạn văn bản liên quan trực tiếp trong kho tài liệu do người dùng nạp vào trước, rồi mới dùng các đoạn văn đó làm căn cứ để tổng hợp câu trả lời.",
                "key_points": [
                    "<strong>LLM thuần túy (Chuyên gia đàm đạo):</strong> Trả lời dựa trên trí nhớ xác suất từ dữ liệu huấn luyện tổng quát -> Không chỉ được số trang gốc -> Rất dễ bịa (hallucinate) khi hỏi chi tiết cụ thể.",
                    "<strong>Hệ thống RAG - Gemini Notebook / NotebookLM (Thư ký trung thành):</strong> Chỉ làm việc trên các nguồn (Sources) bạn tải lên -> Mọi câu trả lời đều đính kèm nút trích dẫn (Citation) nhảy thẳng về đúng đoạn văn trong tài liệu gốc -> Sẵn sàng trả lời 'Tài liệu không đề cập' khi thông tin không có trong nguồn.",
                    "<strong>Ứng dụng cốt lõi:</strong> Dùng LLM thuần để mở rộng góc nhìn và brainstorm; dùng RAG (Gemini Notebook) khi cần độ chính xác tuyệt đối trên giáo trình, văn bản pháp luật và bài báo khoa học."
                ],
                "case_study": {
                    "title": "Tra cứu quy chế tín dụng trên ChatGPT thuần vs Gemini Notebook",
                    "context": "Cùng hỏi về điều kiện miễn giảm lãi vay theo một quy định cụ thể: ChatGPT thuần tự suy diễn ra mức giảm 2%/năm; trong khi Gemini Notebook (đã nạp file PDF quy định thật) chỉ rõ trang 14, khoản 3 và trích nguyên văn điều kiện áp dụng.",
                    "analysis": "Khả năng neo vào nguồn (Grounding) của RAG giúp giảm thiểu rủi ro bịa thông tin xuống mức thấp nhất.",
                    "lesson_learned": "Khi làm việc với tài liệu học thuật và nghiệp vụ, luôn ưu tiên kiến trúc RAG."
                },
                "related_concepts": ["c5-vong-lap-sb-rag", "c5-gioi-han-rag"]
            },
            {
                "id": "c5-vong-lap-sb-rag",
                "session": 5,
                "term": "Vòng lặp cộng hưởng: Second Brain <-> RAG AI",
                "definition": "Quy trình kết nối hai chiều giữa kho Ghi chú nguyên tử (Second Brain) của con người và hệ thống truy vấn RAG (Gemini Notebook / Claude Projects) để không ngừng nâng cấp chất lượng tri thức.",
                "key_points": [
                    "<strong>Chiều đi (Second Brain -> RAG):</strong> Bạn nạp các bài báo PDF đã chọn lọc CÙNG VỚI các file Atomic Notes do chính bạn viết vào Gemini Notebook. Nhờ đó, AI không chỉ đọc tài liệu thô mà còn hiểu được góc nhìn và các luận điểm riêng của bạn.",
                    "<strong>Truy vấn chéo đa tài liệu (Cross-Document Querying):</strong> Đặt câu hỏi yêu cầu RAG đối chiếu: <em>'So sánh phương pháp đo lường rủi ro giữa Bài báo A, Bài báo B và Ghi chú cá nhân của tôi; chỉ rõ điểm đồng thuận và mâu thuẫn kèm trích dẫn.'</em>",
                    "<strong>Chiều về (RAG -> Second Brain):</strong> Sau khi kiểm tra các đoạn trích dẫn gốc mà Gemini Notebook chỉ ra, bạn chắt lọc phát hiện mới và tự tay viết thành các Atomic Notes mới lưu về Second Brain."
                ],
                "case_study": null,
                "related_concepts": ["c5-rag-vs-llm"]
            },
            {
                "id": "c5-gioi-han-rag",
                "session": 5,
                "term": "Giới hạn của RAG: 'Rác nạp vào -> Rác có trích dẫn đi ra'",
                "definition": "Nhận thức phản biện quan trọng: RAG chỉ đảm bảo câu trả lời trung thành với tài liệu được nạp vào, chứ không thể biến một tài liệu sai lệch hoặc kém chất lượng thành sự thật khoa học.",
                "key_points": [
                    "<strong>Grounded Garbage (Rác có trích dẫn):</strong> Nếu bạn tải lên Gemini Notebook một bài báo từ tạp chí săn mồi (predatory journal) hoặc một báo cáo có số liệu sai, Gemini Notebook sẽ trích dẫn rất chính xác cái số liệu sai đó!",
                    "<strong>Diễn giải lệch ngữ cảnh:</strong> Đôi khi RAG vẫn có thể ghép hai đoạn văn ở hai trang khác nhau dẫn đến tóm tắt chưa trọn vẹn bối cảnh. Vì vậy, <em>luôn phải bấm vào con số trích dẫn</em> để đọc đoạn văn gốc xung quanh nó.",
                    "<strong>Kết nối sang Module 3:</strong> Để RAG phát huy sức mạnh, bước đầu tiên bắt buộc phải là kỹ năng <em>Tìm nguồn học thuật thật và Kiểm chứng chất lượng nguồn</em>."
                ],
                "case_study": null,
                "related_concepts": ["c5-rag-vs-llm"]
            }
        ],
        "tests": {
            "level_1": {
                "name": "🎯 Level 1: Khái niệm cốt lõi",
                "description": "Nhận biết cơ chế RAG, vai trò của Gemini Notebook và giới hạn của hệ thống.",
                "bloom_level": "Remember",
                "questions": [
                    {
                        "id": "L1-c5-q1",
                        "type": "mc",
                        "concept_ref": "c5-rag-vs-llm",
                        "question": "Điểm khác biệt cốt lõi nhất của công cụ ứng dụng kiến trúc RAG như Gemini Notebook (NotebookLM) so với Chatbot tổng quát thông thường là gì?",
                        "options": [
                            "A. Gemini Notebook chỉ trả lời dựa trên tập tài liệu nguồn do chính người dùng tải lên và luôn đính kèm trích dẫn trỏ về đúng đoạn văn gốc trong tài liệu đó",
                            "B. Gemini Notebook có thể tự động làm giả số liệu khảo sát",
                            "C. Gemini Notebook không cần tài liệu đầu vào vẫn tự biết mọi thứ",
                            "D. Gemini Notebook chỉ dùng để chỉnh sửa ảnh"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L1-c5-q2",
                        "type": "mc",
                        "concept_ref": "c5-rag-vs-llm",
                        "question": "Trong ẩn dụ sư phạm của môn học, nếu Chatbot LLM thuần túy giống như một 'Chuyên gia biết rộng nhưng đôi khi hay bịa', thì hệ thống RAG như Gemini Notebook đóng vai trò như ai?",
                        "options": [
                            "A. Một người thư ký trung thành: chỉ đọc đúng các hồ sơ bạn giao trên bàn và luôn chỉ rõ thông tin nằm ở trang nào, dòng nào",
                            "B. Một nhà tiên tri dự đoán tương lai không cần dữ liệu",
                            "C. Một tác giả đứng tên thay cho bạn trên bài báo",
                            "D. Một công cụ tìm kiếm mạng xã hội"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L1-c5-q3",
                        "type": "mc",
                        "concept_ref": "c5-vong-lap-sb-rag",
                        "question": "Khi thực hiện 'Truy vấn chéo đa tài liệu' trên Gemini Notebook cho Đề án nhóm, thao tác nào sau đây khai thác tốt nhất sức mạnh của công cụ?",
                        "options": [
                            "A. Chỉ tải lên 1 trang giấy trắng",
                            "B. Tải lên cùng lúc 5-10 bài báo khoa học thật và các Atomic Notes của nhóm, sau đó yêu cầu AI lập bảng so sánh điểm giống/khác nhau về phương pháp và kết quả kèm trích dẫn nguồn",
                            "C. Hỏi AI về dự báo thời tiết ngày mai",
                            "D. Nhờ AI tìm tài liệu mới ngoài Internet mà không nạp nguồn nào"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L1-c5-q4",
                        "type": "mc",
                        "concept_ref": "c5-gioi-han-rag",
                        "question": "Khái niệm 'Grounded Garbage' (Rác có trích dẫn) trong hệ thống RAG cảnh báo người học về rủi ro nào?",
                        "options": [
                            "A. Hệ thống RAG tự động xóa file PDF của người dùng",
                            "B. Nếu tài liệu bạn nạp vào RAG ngay từ đầu là bài báo giả hoặc có số liệu rác, thì RAG sẽ trích dẫn cực kỳ chính xác cái thông tin sai lệch đó",
                            "C. Hệ thống RAG không đọc được tiếng Việt",
                            "D. Hệ thống RAG luôn bịa nguồn bên ngoài"
                        ],
                        "correct": "B"
                    }
                ]
            },
            "level_2": {
                "name": "📝 Level 2: Hiểu và phân biệt",
                "description": "Phân tích quy trình kết hợp Second Brain với RAG và kiểm tra trích dẫn.",
                "bloom_level": "Understand",
                "questions": [
                    {
                        "id": "L2-c5-q1",
                        "type": "mc",
                        "concept_ref": "c5-vong-lap-sb-rag",
                        "question": "Tại sao trong vòng lặp Second Brain <-> RAG, bạn nên nạp cả các file Atomic Notes do chính bạn viết vào cùng với các bài báo PDF gốc?",
                        "options": [
                            "A. Để giúp AI đối chiếu được giữa dữ liệu của các bài báo gốc với chính những ý tưởng, giả thuyết và cấu trúc lập luận cá nhân mà bạn đã chắt lọc trong Second Brain",
                            "B. Để làm cho dung lượng bộ nhớ nặng hơn",
                            "C. Vì Gemini Notebook bắt buộc phải có file ghi chú mới cho phép mở file PDF",
                            "D. Để AI tự động xóa các bài báo PDF đi"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L2-c5-q2",
                        "type": "mc",
                        "concept_ref": "c5-gioi-han-rag",
                        "question": "Ngay cả khi Gemini Notebook đã hiển thị con số trích dẫn [1], [2] ở cuối câu trả lời, người học nghiêm túc vẫn cần thực hiện thao tác nào tiếp theo?",
                        "options": [
                            "A. Copy luôn câu trả lời đó vào báo cáo mà không cần xem lại",
                            "B. Bấm trực tiếp vào con số trích dẫn [1], [2] để đọc đoạn văn gốc được tô sáng trong tài liệu, kiểm tra xem AI có tóm tắt đúng ngữ cảnh của tác giả hay không",
                            "C. Xóa các con số trích dẫn đi rồi nộp bài",
                            "D. Không cần làm gì thêm vì RAG đúng tuyệt đối 100% trong mọi trường hợp"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L2-c5-q3",
                        "type": "mc",
                        "concept_ref": "c5-rag-vs-llm",
                        "question": "Tình huống nào sau đây bạn NÊN dùng Gemini Notebook (RAG) thay vì dùng một cửa sổ chat AI tổng quát không đính kèm tài liệu?",
                        "options": [
                            "A. Khi muốn AI nghĩ ra 10 tên slogan vui nhộn cho câu lạc bộ sinh viên",
                            "B. Khi cần đối chiếu chính xác các điều khoản trong Thông tư 49/2026/TT-BGDĐT và 5 bài báo khoa học PDF đã tải về máy để viết báo cáo Đề án",
                            "C. Khi muốn trò chuyện giải trí cuối tuần",
                            "D. Khi chưa có bất kỳ tài liệu nào và chỉ muốn nảy ý tưởng từ khóa ban đầu"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L2-c5-q4",
                        "type": "mc",
                        "concept_ref": "c5-vong-lap-sb-rag",
                        "question": "Tính năng Audio Overview hoặc Study Guide trên Gemini Notebook hỗ trợ gì cho quá trình học tập của sinh viên?",
                        "options": [
                            "A. Chuyển hóa nội dung từ chính các tài liệu chuẩn bạn đã nạp thành bộ câu hỏi ôn tập, bảng thuật ngữ hoặc đoạn hội thoại âm thanh để bạn ôn bài đa giác quan và tự kiểm tra (Active Recall)",
                            "B. Tự động nộp bài thi cuối kỳ thay cho sinh viên",
                            "C. Thay thế hoàn toàn việc đọc tài liệu gốc",
                            "D. Tự động tải thêm tài liệu chưa kiểm chứng từ mạng xã hội vào bài"
                        ],
                        "correct": "A"
                    }
                ]
            },
            "level_3": {
                "name": "🚀 Level 3: Vận dụng thực tế",
                "description": "Thiết lập kho RAG và hoàn thiện Mảnh ghép 2 cho Đề án cuối khóa.",
                "bloom_level": "Apply",
                "questions": [
                    {
                        "id": "L3-c5-q1",
                        "type": "mc",
                        "concept_ref": "c5-vong-lap-sb-rag",
                        "question": "Để hoàn thành Mảnh ghép 2 của Đề án cuối khóa ở Buổi 5, nhóm sinh viên cần chứng minh quy trình kết nối Second Brain và RAG như thế nào?",
                        "options": [
                            "A. Chỉ cần chụp màn hình trang chủ Google",
                            "B. Thiết lập cấu trúc PARA của dự án, mỗi thành viên nạp các tài liệu chuyên ngành đã chọn lọc cùng các Atomic Notes cá nhân vào một Notebook chung, thực hiện truy vấn đối chiếu đa nguồn có trích dẫn và đúc kết thành các Atomic Notes tổng hợp mới",
                            "C. Copy nguyên một bài báo tiếng Anh dán vào Word rồi nộp",
                            "D. Nhờ AI tự tạo ra 10 file PDF giả để nạp vào Notebook"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L3-c5-q2",
                        "type": "mc",
                        "concept_ref": "c5-gioi-han-rag",
                        "question": "Khi bạn hỏi Gemini Notebook một câu hỏi mà cả 5 tài liệu PDF bạn tải lên đều không hề đề cập, phản hồi chuẩn mực của hệ thống RAG là gì và bạn nên làm gì?",
                        "options": [
                            "A. Hệ thống báo rằng thông tin không có trong các nguồn được cung cấp; lúc này bạn biết mình đang thiếu hụt tài liệu ở khía cạnh đó và cần đi tìm thêm bài báo khoa học thật từ Semantic Scholar/Elicit để bổ sung vào kho nguồn",
                            "B. Ép hệ thống phải tự bịa ra câu trả lời bằng mọi giá",
                            "C. Tự viết đại một con số không có nguồn vào báo cáo",
                            "D. Bỏ luôn đề tài đang làm"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L3-c5-essay1",
                        "type": "essay",
                        "concept_ref": "c5-vong-lap-sb-rag",
                        "question": "Hãy mô tả cấu trúc Kho tri thức RAG (trên Gemini Notebook hoặc Claude Project) mà nhóm bạn đã dựng cho Đề án cuối khóa (Mảnh ghép 2): Bạn đã nạp vào đó những nguồn tài liệu nào? Hãy ghi lại 01 câu truy vấn chéo đa tài liệu (Cross-document prompt) mà nhóm đã chạy thử và phát hiện thú vị nhất (kèm nguồn trích dẫn cụ thể) mà nhóm thu được từ câu truy vấn đó.",
                        "rubric": "Liệt kê rõ các nguồn tài liệu thật và Atomic Notes đã nạp vào kho RAG của nhóm (30%) · Câu truy vấn chéo đa tài liệu được thiết kế sắc bén, yêu cầu đối chiếu và trích dẫn rõ ràng (35%) · Trình bày được phát hiện thực tế kèm vị trí trích dẫn đã kiểm tra lại trên bản gốc (35%)",
                        "max_words": 350
                    }
                ]
            }
        }
    },
    {
        "chapter": 6,
        "title": "Quy trình NCKH với AI (Bước 1 & 2): Tìm nguồn thật, Đọc tóm tắt & 'Soi 3 phút'",
        "sessions": [6],
        "scqa": {
            "situation": "Bước vào giai đoạn làm nghiên cứu khoa học hoặc cơ sở lý luận cho Đề án ngành Ngân hàng - Kinh tế, sinh viên đứng trước hàng triệu bài báo học thuật bằng tiếng Anh. Để tiết kiệm thời gian, nhiều bạn nhờ AI tìm tài liệu rồi quăng file PDF bài báo cho AI tóm tắt và chép thẳng bảng tóm tắt đó vào bài làm.",
            "complication": "Trong thực nghiệm trực tiếp tại buổi tọa đàm khoa học (với bài báo mẫu Hemani, 2026), ngay cả khi đã dùng Prompt chuẩn yêu cầu tóm tắt file PDF đính kèm, mô hình AI (DeepSeek) vẫn tự ý nâng cấp một kế hoạch tính toán Excel mơ hồ trong bài gốc thành thuật ngữ chuyên môn 'hệ số tương quan Pearson (Pearson's R)' dù chữ 'Pearson' xuất hiện đúng 0 lần trong toàn bộ bài báo! Hơn thế nữa, AI trích đúng con số cỡ mẫu '192 sinh viên' ở trang 4 nhưng không báo cho người đọc biết trang 3 chỉ ghi ước tính '150-200', cũng như không thể thay người đọc phán đoán việc bài báo chỉ ghi số xấp xỉ (~0.62) mà không có bảng hệ số hay p-value.",
            "question": "Làm thế nào để tìm đúng nguồn học thuật thật và kiểm soát chặt chẽ bản tóm tắt của AI để không bao giờ bị đánh lừa bởi những chi tiết do AI tự suy diễn thêm hoặc từ chính một bài báo gốc kém chất lượng?",
            "answer": "Tuân thủ kỷ luật 'Nguồn thật trước, AI sau': tìm bài trên kho dữ liệu học thuật thật (Semantic Scholar, Elicit, Consensus), dùng Prompt tóm tắt 7 mục có chốt chặn 'Không suy đoán', và bắt buộc thực hiện quy trình 'Soi bản tóm tắt trong 3 phút' (Đối chiếu số liệu - Truy chỗ AI thêm - Hỏi ngược về hạn chế)."
        },
        "concepts": [
            {
                "id": "c6-nguon-that-cong-cu",
                "session": 6,
                "term": "Quy tắc 'Nguồn thật trước, AI sau' & Chọn công cụ theo đúng việc",
                "definition": "Nguyên tắc nền tảng trong nghiên cứu có AI đồng hành: việc nào cần nguồn tài liệu thật thì bắt buộc phải bắt đầu từ công cụ kết nối với cơ sở dữ liệu học thuật thật, tuyệt đối không xin danh mục tài liệu từ Chatbot tổng quát.",
                "key_points": [
                    "<strong>Phễu thu hẹp câu hỏi nghiên cứu:</strong> Đi từ Chủ đề rộng -> Thêm đối tượng, bối cảnh, biến số -> Câu hỏi nghiên cứu cụ thể -> Xác định loại câu hỏi rồi mới chọn công cụ.",
                    "<strong>Semantic Scholar (semanticscholar.org):</strong> Tìm bài báo khoa học thật, miễn phí trên kho hơn 200 triệu công trình có mã DOI chuẩn.",
                    "<strong>Elicit (elicit.com):</strong> Gom nhiều bài báo thật vào một bảng trích xuất theo các cột do bạn đặt (câu hỏi, phương pháp, cỡ mẫu, kết quả chính).",
                    "<strong>Consensus (consensus.app):</strong> Xem nhanh bằng chứng thực nghiệm nghiêng về phía nào qua Đồng hồ đo (<em>Consensus Meter</em>). Lưu ý: Đồng hồ đo chỉ hợp với câu hỏi <strong>Yes/No dựa trên bằng chứng thực nghiệm</strong>; và chữ 'Yes' chỉ là điểm bắt đầu cho chuỗi 5 câu hỏi đào sâu (Có xảy ra không? Xảy ra bao nhiêu %? Khi nào nặng hơn? Làm sao phát hiện? Hệ quả gì?)."
                ],
                "case_study": null,
                "related_concepts": ["c6-prompt-7-muc", "c6-soi-3-phut"]
            },
            {
                "id": "c6-prompt-7-muc",
                "session": 6,
                "term": "Khung Prompt Tóm tắt Bài báo Khoa học 7 mục",
                "definition": "Cấu trúc câu lệnh tiêu chuẩn gồm 4 thành phần (Vai trò - Đầu vào PDF 7 mục - Ràng buộc nguồn - Định dạng) giúp trích xuất có kiểm soát một bài báo khoa học đầy đủ.",
                "key_points": [
                    "<strong>Nguyên tắc đầu vào:</strong> Phải tải trực tiếp file PDF bài báo đầy đủ lên AI (DeepSeek, Claude, Gemini Notebook), không gõ tên bài báo rồi bắt AI nhớ lại.",
                    "<strong>7 mục bắt buộc trong bảng tóm tắt:</strong> (1) Câu hỏi nghiên cứu, (2) Phương pháp, (3) Dữ liệu hoặc cỡ mẫu, (4) Kết quả chính, (5) Hạn chế của nghiên cứu, (6) Đóng góp, (7) Điều người đọc cần kiểm tra lại.",
                    "<strong>Câu khóa ràng buộc nguồn (Quan trọng nhất):</strong> <em>'Mỗi ý ghi rõ số trang hoặc tên mục. Chỗ nào bài không nói, ghi rõ không nêu trong bài, không suy đoán. Tối đa 300 chữ, tiếng Việt, giữ thuật ngữ gốc tiếng Anh trong ngoặc.'</em>"
                ],
                "case_study": null,
                "related_concepts": ["c6-soi-3-phut"]
            },
            {
                "id": "c6-soi-3-phut",
                "session": 6,
                "term": "Kỹ năng 'Soi bản tóm tắt trong 3 phút' & Hai loại lỗi tinh vi của AI",
                "definition": "Quy trình 3 thao tác kiểm định nhanh bản tóm tắt của AI ngay trên file PDF gốc nhằm phát hiện cả lỗi suy diễn của AI lẫn điểm yếu phương pháp luận của chính bài báo.",
                "key_points": [
                    "<strong>Thao tác 1 - Đối chiếu số liệu:</strong> Chọn ít nhất 2-3 con số trong bản tóm tắt, mở đúng trang/bảng của bài gốc để so. <em>Bài học từ case Hemani (2026):</em> Các số 82%, 41%, r ~ 0.62 và r ~ -0.48 đều khớp nguyên văn trang 4 bài gốc, nhưng bài gốc chỉ ghi dấu xấp xỉ (~) mà không có bảng hệ số hay p-value -> <strong>Số khớp chứng minh bản tóm tắt trung thực với bài, không chứng minh con số của bài báo đó đáng tin!</strong>",
                    "<strong>Thao tác 2 - Truy chỗ AI thêm & thiếu bối cảnh:</strong> Hỏi AI <em>'Chi tiết này nằm ở đoạn nào trong bài?'</em> và kiểm tra toàn văn. Nhận diện 2 loại lỗi: (a) <em>Đúng chữ nhưng thiếu bối cảnh</em> (AI ghi cỡ mẫu 192 ở phần Kết quả tr.4 nhưng không báo phần Phương pháp tr.3 ghi cỡ mẫu dự kiến là 150-200); (b) <em>Chi tiết AI tự suy diễn thêm nguy hiểm nhất</em> (AI tự ghi phương pháp là <code>Pearson's R</code> trong khi chữ <code>Pearson</code> xuất hiện <strong>0 lần</strong> trong toàn bài!).",
                    "<strong>Thao tác 3 - Hỏi ngược về Hạn chế (Limitations):</strong> Kiểm tra xem bài gốc có tự nêu hạn chế không. Nhờ câu 'không suy đoán', AI mới chịu ghi 'không nêu trong bài' (vì chữ limitation xuất hiện 0 lần trong bài Hemani) rồi mới tách riêng các điểm yếu phương pháp do người đọc/AI nhận xét."
                ],
                "case_study": {
                    "title": "Case study thực nghiệm bài báo Hemani (2026) trên DeepSeek",
                    "context": "Đưa bài báo Hemani (2026, tạp chí IJSDR, 6 trang - được chọn có chủ đích vì chất lượng yếu) vào DeepSeek với Prompt 7 mục.",
                    "analysis": "AI tự phát hiện được một số điểm yếu (thiếu p-value, lệch nhãn Bảng 3 và Hình 3), nhưng lại tự bịa thêm chữ 'Pearson's R' vào hàng Phương pháp vì thấy có ký hiệu r ~ 0.62.",
                    "lesson_learned": "AI thêm vào những thuật ngữ nghe cực kỳ chuyên môn chính là loại lỗi dễ đánh lừa sinh viên nhất nếu không mở PDF gốc bấm Ctrl+F để truy nguyên."
                },
                "related_concepts": ["c6-prompt-7-muc"]
            }
        ],
        "tests": {
            "level_1": {
                "name": "🎯 Level 1: Khái niệm cốt lõi",
                "description": "Nhận diện quy trình 4 bước NCKH, công cụ tìm nguồn thật và 3 thao tác soi bản tóm tắt.",
                "bloom_level": "Remember",
                "questions": [
                    {
                        "id": "L1-c6-q1",
                        "type": "mc",
                        "concept_ref": "c6-nguon-that-cong-cu",
                        "question": "Trong quy trình nghiên cứu khoa học có AI đồng hành gồm 4 bước (1. Tìm -> 2. Đọc -> 3. Tổng hợp -> 4. Viết), hoạt động 'Kiểm chứng' nằm ở vị trí nào?",
                        "options": [
                            "A. Chỉ thực hiện ở bước cuối cùng sau khi đã viết xong toàn bộ khóa luận",
                            "B. Đi xuyên suốt cả 4 bước: kiểm từ nguồn có thật không, tóm tắt có khớp bản gốc không, nhận định tổng hợp có đúng nguồn không, đến trích dẫn có chính xác không",
                            "C. Giao hoàn toàn cho AI tự kiểm chứng, con người không cần can thiệp",
                            "D. Chỉ kiểm chứng khi giảng viên yêu cầu"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L1-c6-q2",
                        "type": "mc",
                        "concept_ref": "c6-nguon-that-cong-cu",
                        "question": "Tính năng Đồng hồ đo (Consensus Meter) trên công cụ Consensus.app phù hợp nhất với loại câu hỏi nghiên cứu nào?",
                        "options": [
                            "A. Câu hỏi Yes/No (Có/Không) dựa trên bằng chứng thực nghiệm (ví dụ: 'Do large language models fabricate citations?')",
                            "B. Câu hỏi yêu cầu viết một bài thơ",
                            "C. Câu hỏi mở mang tính triết học hoặc chuẩn mực đạo đức ('Chúng ta có nên...')",
                            "D. Câu hỏi xin danh sách điểm thi của lớp"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L1-c6-q3",
                        "type": "mc",
                        "concept_ref": "c6-soi-3-phut",
                        "question": "Ba thao tác cốt lõi trong quy trình 'Soi bản tóm tắt bài báo trong 3 phút' là gì?",
                        "options": [
                            "A. Đọc lướt tiêu đề, đếm số trang, và xem ảnh tác giả",
                            "B. (1) Đối chiếu số liệu với bảng/hình gốc, (2) Truy chỗ AI tự thêm hoặc thiếu bối cảnh, và (3) Hỏi ngược về hạn chế (Limitations) của bài báo",
                            "C. Dịch sang tiếng Anh, đổi phông chữ, và in ra giấy",
                            "D. Copy bản tóm tắt sang một Chatbot khác để hỏi xem có hay không"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L1-c6-q4",
                        "type": "mc",
                        "concept_ref": "c6-soi-3-phut",
                        "question": "Trong thực nghiệm Demo 1 với bài báo Hemani (2026), chi tiết nào ở mục Phương pháp đã bị AI tự ý suy diễn thêm dù xuất hiện đúng 0 lần trong toàn bộ bài báo gốc?",
                        "options": [
                            "A. Phần mềm Microsoft Excel",
                            "B. Cụm thuật ngữ hệ số tương quan 'Pearson's R'",
                            "C. Phương pháp lấy mẫu ngẫu nhiên (random sampling)",
                            "D. Bảng hỏi 30 câu"
                        ],
                        "correct": "B"
                    }
                ]
            },
            "level_2": {
                "name": "📝 Level 2: Hiểu và phân biệt",
                "description": "Phân tích hai loại lỗi của AI khi tóm tắt và bài học về đọc phê phán.",
                "bloom_level": "Understand",
                "questions": [
                    {
                        "id": "L2-c6-q1",
                        "type": "mc",
                        "concept_ref": "c6-soi-3-phut",
                        "question": "Khi bạn đối chiếu các con số trong bản tóm tắt của AI (như 82%, 41%, r ~ 0.62) và thấy chúng khớp 100% với trang 4 của bài báo gốc, tại sao bạn vẫn chưa thể kết luận ngay rằng các con số đó đáng tin cậy về mặt khoa học?",
                        "options": [
                            "A. Vì số khớp chỉ chứng minh bản tóm tắt của AI trung thực với văn bản bài báo, chứ không chứng minh phương pháp thu thập và phân tích của chính bài báo đó đạt chuẩn khoa học (ví dụ bài gốc chỉ ghi số xấp xỉ '~' mà không có bảng hệ số hay p-value)",
                            "B. Vì mọi con số trong mọi bài báo khoa học đều là giả",
                            "C. Vì số trang 4 luôn luôn sai",
                            "D. Vì AI đã tự sửa file PDF gốc của bạn"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L2-c6-q2",
                        "type": "mc",
                        "concept_ref": "c6-soi-3-phut",
                        "question": "Trong bài báo Hemani (2026), mục Phương pháp (tr.3) ghi 'Estimated total sample size: 150-200 students', còn mục Kết quả (tr.4) ghi 'out of 192 students surveyed'. Khi AI chỉ trích con số 192 vào bảng tóm tắt, bài học rút ra về việc kiểm chứng là gì?",
                        "options": [
                            "A. AI đã bịa hoàn toàn con số 192",
                            "B. Đây không phải mâu thuẫn của bài báo (150-200 là cỡ mẫu dự kiến khi thiết kế, 192 là mẫu thực tế thu được), nhưng lỗi của AI là trích đúng chữ ở phần Kết quả mà bỏ qua bối cảnh ở phần Phương pháp; người đọc phải luôn hỏi tiếp: 'Trong bài còn chỗ nào nói khác về con số này không?'",
                            "C. Phải lấy 150 cộng 200 chia đôi mới đúng",
                            "D. Không cần quan tâm đến cỡ mẫu khi đọc bài báo"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L2-c6-q3",
                        "type": "mc",
                        "concept_ref": "c6-prompt-7-muc",
                        "question": "Tác dụng trực tiếp nhất của câu ràng buộc 'Chỗ nào bài không nói, ghi không nêu trong bài, không suy đoán' trong Prompt tóm tắt 7 mục là gì?",
                        "options": [
                            "A. Giúp AI biết dừng lại và ghi đúng 'không nêu trong bài' ở những mục bài báo gốc bỏ trống (như mục Limitations của bài Hemani), thay vì tự bịa ra nội dung để điền cho kín bảng 7 mục",
                            "B. Làm cho AI từ chối tóm tắt toàn bộ bài báo",
                            "C. Giúp AI tự động dịch bài báo sang 10 thứ tiếng",
                            "D. Giúp tăng tốc độ mạng Internet"
                        ],
                        "correct": "A"
                    },
                    {
                        "id": "L2-c6-q4",
                        "type": "mc",
                        "concept_ref": "c6-nguon-that-cong-cu",
                        "question": "Khi dùng Consensus.app để hỏi một câu hỏi thực nghiệm và thấy đồng hồ Consensus Meter chỉ 100% Yes, tại sao người nghiên cứu không nên dừng lại ở chữ Yes đó?",
                        "options": [
                            "A. Vì chữ Yes chỉ trả lời câu hỏi đầu tiên ('Hiện tượng đó có xảy ra không?'); người nghiên cứu cần mở từng bài báo bên dưới để đào sâu chuỗi câu hỏi tiếp theo: Xảy ra ở mức độ bao nhiêu (ví dụ 19.9% hay 1/277)? Khi nào nặng hơn? Cơ chế là gì? Hệ quả ra sao?",
                            "B. Vì đồng hồ Consensus luôn chỉ ngược với sự thật",
                            "C. Vì Consensus không chứa bài báo thật",
                            "D. Vì chữ Yes có nghĩa là đề tài đã bị cấm nghiên cứu"
                        ],
                        "correct": "A"
                    }
                ]
            },
            "level_3": {
                "name": "🚀 Level 3: Vận dụng thực tế",
                "description": "Thực hành tìm nguồn thật và lập biên bản 'Soi 3 phút' cho Đề án nhóm.",
                "bloom_level": "Apply",
                "questions": [
                    {
                        "id": "L3-c6-q1",
                        "type": "mc",
                        "concept_ref": "c6-soi-3-phut",
                        "question": "Khi bạn yêu cầu AI tóm tắt một bài báo kinh tế bằng file PDF đính kèm và thấy trong bảng tóm tắt xuất hiện câu: 'Nghiên cứu sử dụng mô hình hồi quy GMM hai bước với p-value < 0.001'. Thao tác kiểm chứng đầu tiên bạn phải làm ngay trong 60 giây là gì?",
                        "options": [
                            "A. Chép luôn câu đó vào báo cáo Đề án vì thuật ngữ GMM nghe rất cao cấp",
                            "B. Mở file PDF bài báo gốc, bấm Ctrl+F tìm từ khóa 'GMM' và '0.001' (hoặc mở đúng số trang AI ghi) để kiểm tra xem bài gốc có thực sự dùng GMM với p < 0.001 hay AI tự suy diễn từ một phương pháp khác",
                            "C. Hỏi lại AI xem GMM là viết tắt của từ gì",
                            "D. Xóa file PDF gốc đi cho nhẹ máy"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L3-c6-q2",
                        "type": "mc",
                        "concept_ref": "c6-nguon-that-cong-cu",
                        "question": "Một bạn sinh viên có ý tưởng ban đầu rất mơ hồ: 'Em muốn nghiên cứu về AI trong ngân hàng'. Trình tự đi qua 'Phễu thu hẹp' và chọn công cụ nào dưới đây là đúng chuẩn phương pháp luận?",
                        "options": [
                            "A. Gõ thẳng chữ 'AI trong ngân hàng' vào Chatbot rồi chép 5 trang đầu tiên nộp bài",
                            "B. Thu hẹp dần: Chủ đề (AI trong ngân hàng) -> Thêm đối tượng & bối cảnh (Khách hàng Gen Z dùng chatbot CSKH tại NHTM Việt Nam) -> Câu hỏi cụ thể (Rủi ro cảm nhận về bảo mật ảnh hưởng thế nào đến ý định tiếp tục sử dụng?) -> Dùng Semantic Scholar và Elicit để tìm và lập bảng các bài báo thực nghiệm thật",
                            "C. Lên mạng xã hội hỏi ý kiến ngẫu nhiên",
                            "D. Bỏ qua bước tìm tài liệu, tự chế số liệu khảo sát ngay lập tức"
                        ],
                        "correct": "B"
                    },
                    {
                        "id": "L3-c6-essay1",
                        "type": "essay",
                        "concept_ref": "c6-soi-3-phut",
                        "question": "Hãy chọn 01 bài báo khoa học thật (PDF) phục vụ cho Đề án cuối khóa của nhóm bạn (tìm từ Semantic Scholar hoặc Elicit). Chạy Prompt tóm tắt 7 mục và viết 'Biên bản Soi 3 phút' gồm: (1) Thông tin bài báo gốc & DOI, (2) Hai con số bạn đã đối chiếu trực tiếp với trang/bảng gốc (khớp hay lệch?), (3) Một chi tiết bạn đã truy nguyên xem AI có tự suy diễn hay thiếu bối cảnh không, và (4) Nhận định của riêng bạn về chất lượng/hạn chế của bài báo đó.",
                        "rubric": "Nêu rõ bài báo thật có DOI liên quan đến Đề án nhóm (20%) · Đối chiếu cụ thể 2 số liệu kèm số trang/bảng gốc (30%) · Truy nguyên rõ ràng chỗ AI tóm tắt đúng hoặc tự suy diễn/thiếu bối cảnh (30%) · Đưa ra nhận định phê phán độc lập về hạn chế của bài báo (20%)",
                        "max_words": 400
                    }
                ]
            }
        }
    }
]

for ch in chapters_1_to_6:
    path = os.path.join(CONTENT_DIR, "ebook", f"chapter-{ch['chapter']}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(ch, f, ensure_ascii=False, indent=2)

print("Chapters 1 to 6 generated successfully.")
