# -*- coding: utf-8 -*-
import os
import json

CONTENT_DIR = r"d:\PARA\Projects\second-brain\05-Projects\lms-hub\courses\ky-nang-ai-hub\content"

lessons_data = [
    {
        "id": 1,
        "module": "MODULE 1: BẢN CHẤT AI, PROMPT, CONTEXT & HARNESS",
        "title": "Buổi 1: Bản chất AI & Tư duy người làm chủ ('AI là Trợ lý, Bạn là Chủ')",
        "subtitle": "Giải mã cơ chế xác suất của LLM, nhận diện Hallucination (Topaz 1/277) và xác lập ranh giới phân vai Người - AI",
        "clo": "CLO1, CLO3",
        "duration": "4 tiết (200 phút)",
        "objectives": [
            "Giải thích được cơ chế dự đoán từ tiếp theo dựa trên xác suất (Next-token Prediction) của Mô hình ngôn ngữ lớn (LLM) và phân biệt rõ LLM với công cụ tìm kiếm truyền thống (CLO1).",
            "Phân tích được nguyên nhân gốc rễ của hiện tượng ảo giác AI (Hallucination - với bằng chứng thực nghiệm 1/277 từ The Lancet 5/2026), lệ thuộc nhận thức (Cognitive Offloading) và ảo tưởng trôi chảy (Fluency Illusion) (CLO1).",
            "Thiết lập được Bảng phân vai 'Việc nào giao cho AI - Việc nào con người giữ' theo bộ ba động từ: <strong>AI đề xuất - Bạn quyết định - Bạn chịu trách nhiệm</strong> (CLO1).",
            "Khởi tạo không gian học tập trên hệ thống LMS Hub, thành lập nhóm Đề án cuối khóa và viết được <strong>Atomic Note phản tư 4F</strong> đầu tiên (CLO3)."
        ],
        "story_hook": "Câu chuyện của Minh (Kỳ 1): Minh - sinh viên năm 2 ngành Tài chính Ngân hàng tại HUB - dùng ChatGPT viết xong bài tiểu luận trong 30 phút với văn phong cực kỳ trôi chảy. Khi lên lớp, giảng viên chỉ hỏi đúng 2 câu: 'Số liệu nợ xấu trang 3 em lấy từ báo cáo nào?' và 'Tại sao em chọn mô hình này?'. Minh đứng hình không trả lời được vì số liệu đó do AI tự bịa và Minh chưa từng thực sự suy nghĩ về bài viết.",
        "warmup_questions": [
            "Hai câu hỏi giơ tay không chấm điểm: (1) Bạn nào trong lớp đã từng dùng AI để tìm tài liệu hoặc làm bài tập, tiểu luận? (2) Trong số các bạn vừa giơ tay, bạn nào đã mở từng tài liệu gốc mà AI đưa ra để kiểm tra xem nó có thật không?",
            "Nếu AI chỉ đoán chữ theo xác suất chứ không hề 'biết' sự thật, chuyện gì sẽ xảy ra với năng lực chuyên môn của bạn sau 3 năm đại học nếu bạn giao toàn bộ việc suy nghĩ cho nó?"
        ],
        "timeline": [
            ("Tiết 1 (00' - 50')", "<strong>Khởi động & Cú sốc nhận thức về AI:</strong><br>• Kể câu chuyện của Minh (Kỳ 1) và thực hiện khảo sát 2 câu hỏi giơ tay.<br>• Công bố số liệu nghiên cứu của Topaz và cs. trên <em>The Lancet</em> (5/2026): kiểm tra 2.5 triệu bài báo trên PubMed, tỷ lệ bài dính trích dẫn bịa tăng gấp 10 lần từ 1/2.828 (2023) lên <strong>1/277</strong> (đầu 2026).<br>• Giới thiệu lộ trình 11 buổi, hệ thống LMS Hub và quy chế Đề án tích hợp 4 mảnh ghép (100% điểm cuối khóa).", "Trả lời khảo sát trực tiếp; quan sát số liệu thực nghiệm; đăng nhập hệ thống LMS Hub.", "Slide Buổi 1; LMS Hub"),
            ("Tiết 2 (50' - 100')", "<strong>Giải mã Hộp đen: AI không phải phép thuật, AI là xác suất:</strong><br>• Live Demo 'Bẫy AI nói nhảm': hỏi AI về một thông tư ngân hàng hoặc một cuốn sách kinh tế hoàn toàn không tồn tại -> AI trả lời rất tự tin.<br>• Giảng giải cơ chế <em>Next-token Prediction</em> và bảng so sánh LLM vs Google Search.<br>• Tổ chức thảo luận cặp đôi (Think-Pair-Share) so sánh truy vấn trên Google và trên Chatbot.", "Thực hành theo cặp: thử đặt cùng 1 câu hỏi chuyên ngành trên Google và Chatbot để chỉ ra 3 điểm khác biệt cốt lõi.", "Máy chiếu Live Demo; Thiết bị cá nhân"),
            ("Tiết 3 (100' - 150')", "<strong>Hai cái bẫy nhận thức & Bảng phân vai 'Việc nào giao - Việc nào giữ':</strong><br>• Phân tích hiện tượng <em>Cognitive Offloading</em> (Lệ thuộc nhận thức) và <em>Fluency Illusion</em> (Ảo tưởng trôi chảy).<br>• Đúc kết 3 động từ: <strong>AI đề xuất - Bạn quyết định - Bạn chịu trách nhiệm</strong> và phép thử vàng khi giao việc.<br>• Giới thiệu Bản đồ hệ sinh thái công cụ AI 2026 theo 4 nhóm tác vụ.", "Thảo luận tình huống phân định ranh giới giao việc trong học tập ngành Ngân hàng, Kế toán, Marketing.", "Sơ đồ Bản đồ công cụ AI 2026"),
            ("Tiết 4 (150' - 200')", "<strong>Thực hành Phân vai, Khởi tạo nhóm Đề án & Khóa chốt LMS:</strong><br>• Hướng dẫn chia nhóm Đề án cuối khóa (3-4 SV cùng chuyên ngành).<br>• Hướng dẫn bài tập phân rã quy trình 1 bài toán nghiệp vụ thành bảng phân vai Người - AI.<br>• Hướng dẫn viết Nhật ký học tập (Atomic Note phản tư 4F) và làm Quiz Active Recall 5 lượt trên LMS.", "Chia nhóm Đề án; lập Bảng phân vai cho 3 ý tưởng đề tài tiềm năng; viết phản tư 4F, gửi Feedback tải slide và hoàn thành Quiz Buổi 1 trên LMS.", "LMS Hub (Quiz 1, Journal 1)")
        ],
        "discussion_questions": [
            "Tại sao một bài văn do AI viết đọc lên rất mượt mà, hợp lý nhưng khi gấp máy tính lại bạn hầu như không nhớ được gì (Fluency Illusion)?",
            "Hãy áp dụng phép thử: 'Nếu AI làm sai bước này, mình có phát hiện ra không?' vào việc làm khóa luận tốt nghiệp. Những bước nào một sinh viên năm 3-4 có thể kiểm tra được AI, và bước nào tuyệt đối không được giao cho AI?",
            "Trong nghiên cứu của Topaz (2026) trên The Lancet, hơn 98% số bài báo chứa trích dẫn bịa vẫn chưa bị nhà xuất bản xử lý tại thời điểm kiểm tra. Điều đó cảnh báo gì cho chúng ta ngay cả khi đọc các bài báo đã xuất bản?"
        ],
        "homework": """
      <div class="homework-box">
        <h3>1. Nhiệm vụ Cá nhân trên LMS Hub (Bắt buộc để ghi nhận chuyên cần & tích lũy Cấu phần 2 - 30%):</h3>
        <ul>
          <li>Hoàn thành đọc và làm Vòng Test 3 cấp độ của <strong>Chương 1 trên eBook SCQA</strong>.</li>
          <li>Hoàn thành <strong>Quiz Buổi 1</strong> (tối đa 5 lượt làm bài Active Recall để đạt điểm tối đa và mở khóa lời giải chi tiết).</li>
          <li>Viết <strong>Nhật ký học tập (Atomic Note số 1 theo khung 4F)</strong> trên LMS: Đúc kết bằng ngôn từ của chính bạn về bản chất xác suất của AI và 1 việc bạn quyết định sẽ ngừng giao phó mù quáng cho AI từ hôm nay.</li>
        </ul>
        <h3>2. Nhiệm vụ Nhóm Đề án cuối khóa (Chuẩn bị cho Mảnh ghép 1):</h3>
        <ul>
          <li>Chốt danh sách nhóm (3-4 thành viên cùng chuyên ngành) và thảo luận chọn ra <strong>01 bài toán nghiệp vụ hoặc chủ đề nghiên cứu ứng dụng</strong> trong ngành (Tài chính, Ngân hàng, Kế toán, Marketing, Quản trị...).</li>
          <li>Lập bản nháp <strong>Bảng phân vai Con người - AI</strong> cho bài toán đó (tối thiểu 4 bước công việc) để mang tới Buổi 2 thiết kế bộ Prompt & Context.</li>
        </ul>
      </div>
        """,
        "review_mc": [
            ("Cơ chế cốt lõi của LLM là gì?", "Dự đoán từ (token) tiếp theo có xác suất cao nhất dựa trên ngữ cảnh đứng trước."),
            ("Tỷ lệ bài báo trên PubMed dính trích dẫn bịa đầu năm 2026 theo Topaz (The Lancet, 5/2026) là bao nhiêu?", "1/277 bài báo (tăng gấp hơn 10 lần so với mức 1/2.828 của năm 2023)."),
            ("Phép thử vàng trước khi giao một bước công việc cho AI là gì?", "Nếu AI làm sai ở bước này, mình có đủ kiến thức và công cụ để phát hiện ra không? Nếu không, đừng giao.")
        ],
        "teacher_notes": [
            "Khi chạy Live Demo 'Bẫy AI nói nhảm' ở Tiết 2, hãy dùng một số hiệu thông tư hoặc tên sách chuyên ngành Ngân hàng do chính giảng viên đặt ra ngay tại lớp để sinh viên thấy rõ AI tự tin bịa điều khoản như thế nào.",
            "Nhắc sinh viên: Để được tính hoàn thành buổi học trên LMS Hub, sinh viên cần nộp Feedback có nhận xét để tải bài giảng và làm Quiz đạt yêu cầu."
        ]
    },
    {
        "id": 2,
        "module": "MODULE 1: BẢN CHẤT AI, PROMPT, CONTEXT & HARNESS",
        "title": "Buổi 2: Từ Prompt Engineering đến Context Engineering (Giao diện của Tư duy)",
        "subtitle": "Làm chủ công thức CRISP, 5 kỹ thuật điều khiển suy luận nâng cao, chốt chặn 'Không suy đoán' và nghệ thuật thiết kế ngữ cảnh",
        "clo": "CLO2",
        "duration": "4 tiết (200 phút)",
        "objectives": [
            "Vận dụng thành thạo công thức <strong>CRISP (Context - Role - Input/Instruction - Specifics - Performance Criteria)</strong> để cấu trúc hóa yêu cầu học tập và nghiệp vụ (CLO2).",
            "Sử dụng kết hợp 5 kỹ thuật nâng cao: <strong>Chain-of-Thought (CoT), Role-based, Few-shot, Iterative Refinement, Negative Prompt</strong> cùng câu khóa <em>'Không suy đoán'</em> (CLO2).",
            "Phân biệt và thực hiện được bước chuyển từ viết câu lệnh lẻ (Prompt Engineering) sang <strong>Thiết kế gói ngữ cảnh chuẩn (Context Engineering)</strong> (CLO2).",
            "Chốt đề tài Đề án nhóm và thiết kế được <strong>Bộ 3 cụm Prompt + Gói Context chuẩn hóa</strong> cho Đề án (CLO2)."
        ],
        "story_hook": "Câu chuyện của Minh (Kỳ 2): Rút kinh nghiệm sau bài tiểu luận 6 điểm, Minh quyết tâm dùng AI nghiêm túc để phân tích báo cáo tài chính của một ngân hàng thương mại. Nhưng Minh chỉ gõ 'Hãy phân tích báo cáo tài chính này giúp tôi' nên AI chỉ trả về những nhận xét chung chung như sách giáo khoa. Khi thấy cô bạn cùng bàn dùng khung CRISP kèm 2 ví dụ mẫu (Few-shot) và chốt chặn 'Không suy đoán' tạo ra bản phân tích sắc sảo chỉ trong 10 phút, Minh nhận ra: Prompt chính là tấm gương phản chiếu độ sắc nét trong tư duy của người hỏi.",
        "warmup_questions": [
            "Hãy mở lại câu lệnh gần nhất bạn gõ vào ChatGPT hoặc Claude tuần qua: câu lệnh đó dài mấy dòng, và trong đó bạn đã cung cấp cho AI những thông tin gì ngoài câu hỏi chính?",
            "Tại sao 10 phút suy nghĩ và viết Prompt + Context trên giấy lại giúp tiết kiệm 2 giờ ngồi sửa một kết quả rác?"
        ],
        "timeline": [
            ("Tiết 1 (00' - 50')", "<strong>Prompt là giao diện của tư duy & Khung nền tảng CRISP:</strong><br>• Điểm lại 2 Atomic Notes xuất sắc của Buổi 1.<br>• Giải phẫu 5 thành tố <strong>C - R - I - S - P</strong>.<br>• Live Demo đối chứng 'Trước CRISP vs Sau CRISP' trên bài toán thực tế ngành Ngân hàng / Marketing.", "Quan sát sự thay đổi chất lượng đầu ra giữa câu lệnh tự phát và câu lệnh CRISP; ghi chép cấu trúc 5 thành tố.", "Slide Buổi 2; Cheatsheet CRISP"),
            ("Tiết 2 (50' - 100')", "<strong>Năm kỹ thuật Prompt nâng cao & Chốt chặn 'Không suy đoán':</strong><br>• Giảng và demo trực tiếp 5 kỹ thuật: (1) <em>Chain-of-Thought</em>, (2) <em>Role-based / Multi-Persona</em>, (3) <em>Few-shot</em>, (4) <em>Iterative Refinement</em>, (5) <em>Negative Prompt & Chốt chặn 'Không suy đoán'</em>.<br>• Phân tích cơ chế hoạt động của từng kỹ thuật trên mô hình xác suất.", "Thực hành biến đổi một câu lệnh đơn giản bằng cách gắn thêm Few-shot và chốt chặn 'Chỗ nào tài liệu không nêu, ghi rõ không nêu trong bài, tuyệt đối không suy đoán'.", "Claude / ChatGPT / Gemini"),
            ("Tiết 3 (100' - 150')", "<strong>Bước chuyển sang Context Engineering & Thực hành '1 Bài toán - 3 Cấp độ':</strong><br>• Khái niệm <em>Context Window</em> (cửa sổ ngữ cảnh trượt), hiện tượng <em>Context Rot</em> (loãng ngữ cảnh) và 4 thành phần của một gói Context sạch.<br>• Tổ chức thực hành va chạm: mỗi nhóm chạy cùng 1 bài toán chuyên ngành ở 3 cấp độ (Hỏi tự nhiên -> CRISP -> CRISP + Few-shot + Context file sạch + Chốt chặn).", "Thực hành nhóm trên máy tính: chạy thử 3 cấp độ, lập bảng so sánh sự khác biệt và trình chiếu kết quả trước lớp.", "Tài liệu chuyên ngành mẫu"),
            ("Tiết 4 (150' - 200')", "<strong>Studio Đề án (Thiết kế Bộ Prompt & Context) & Khóa chốt LMS:</strong><br>• Coaching trực tiếp cho các nhóm chốt tên Đề án cuối khóa và viết 3 cụm Prompt + Context.<br>• Hướng dẫn viết Atomic Note Buổi 2 và làm Quiz Active Recall.", "Chốt tên Đề án nhóm; hoàn thành bản thảo 3 cụm Prompt CRISP + danh mục Context của Đề án; viết phản tư 4F và làm Quiz Buổi 2 trên LMS.", "LMS Hub (Quiz 2, Journal 2)")
        ],
        "discussion_questions": [
            "Trong 5 thành phần của CRISP, thành phần nào sinh viên hay bỏ quên nhất khi giao việc cho AI? Hậu quả của việc bỏ quên thành phần đó là gì?",
            "Khi nào bạn nên dùng kỹ thuật Iterative Refinement (sửa dần trong cùng luồng chat), và khi nào bạn nên xóa luồng chat đó đi để sửa lại Prompt + Context gốc ở một phiên chat mới?",
            "Tại sao một ví dụ mẫu (Few-shot) kém chất lượng đưa vào Context lại nguy hiểm hơn cả việc không đưa ví dụ nào?"
        ],
        "homework": """
      <div class="homework-box">
        <h3>1. Nhiệm vụ Cá nhân trên LMS Hub:</h3>
        <ul>
          <li>Hoàn thành đọc và làm Vòng Test 3 cấp độ của <strong>Chương 2 trên eBook SCQA</strong>.</li>
          <li>Hoàn thành <strong>Quiz Buổi 2</strong> (Active Recall 5 lượt) và nộp Feedback tải tài liệu buổi học.</li>
          <li>Viết <strong>Nhật ký học tập (Atomic Note số 2 theo khung 4F)</strong>: Lưu lại 1 mẫu Prompt CRISP tâm đắc nhất bạn đã tự thiết kế cho môn học chuyên ngành của mình.</li>
        </ul>
        <h3>2. Nhiệm vụ Nhóm Đề án cuối khóa (Chuẩn bị cho Buổi 3 - Mảnh ghép 1):</h3>
        <ul>
          <li>Chuẩn bị sẵn <strong>1-2 tài liệu mẫu thật (đã khử thông tin nhạy cảm)</strong> và quy trình các bước thực hiện của bài toán Đề án nhóm để Buổi 3 đóng gói thành <strong>Bộ AI Harness</strong> hoàn chỉnh.</li>
        </ul>
      </div>
        """,
        "review_mc": [
            ("5 thành tố của khung CRISP là gì?", "Context (Bối cảnh) - Role (Vai trò) - Input/Instruction (Dữ liệu & Nhiệm vụ) - Specifics (Ràng buộc cụ thể) - Performance Criteria/Preview (Tiêu chí & Hình dung đầu ra)."),
            ("Kỹ thuật nào buộc AI trình bày từng bước suy luận logic trước khi kết luận?", "Chain-of-Thought (CoT) Prompting."),
            ("Câu khóa chốt chặn chống bịa thông tin khi làm việc với tài liệu là gì?", "Mỗi ý phải ghi rõ số trang/mục; chỗ nào tài liệu không nêu thì ghi rõ 'không nêu trong bài', tuyệt đối không suy đoán.")
        ],
        "teacher_notes": [
            "Khuyến khích sinh viên viết khung CRISP ra giấy hoặc khung nháp 5 ô trước khi gõ vào AI để rèn thói quen cấu trúc hóa tư duy.",
            "Đi kiểm tra từng nhóm ở Tiết 4 để đảm bảo đề tài Đề án nhóm chọn có tính ứng dụng thực chất và vừa sức với thời lượng môn học."
        ]
    },
    {
        "id": 3,
        "module": "MODULE 1: BẢN CHẤT AI, PROMPT, CONTEXT & HARNESS",
        "title": "Buổi 3: Kiến trúc Harness - Xây dựng 'Bộ dây cương' điều phối AI",
        "subtitle": "Thiết kế quy trình nhiều bước có Cổng xác nhận (GATE), Xử lý ngoại lệ (FALLBACK), Gia sư Socrates và chốt Mảnh ghép 1",
        "clo": "CLO1, CLO2",
        "duration": "4 tiết (200 phút)",
        "objectives": [
            "Phân biệt rõ 3 tầng kiến trúc điều phối AI: <strong>Prompt (Mệnh lệnh tức thời) -> Context (Ngữ cảnh nền) -> Harness (Bộ khung quy tắc, quy trình và chốt chặn kiểm soát)</strong> (CLO1, CLO2).",
            "Thiết kế được quy trình làm việc nhiều bước cho AI có gắn <strong>Cổng dừng xác nhận (GATE 🔒)</strong> và <strong>Cơ chế xử lý khi thiếu dữ liệu/căn cứ (FALLBACK ❓)</strong> (CLO2).",
            "Xây dựng được một <strong>Socratic Harness (Gia sư Socrates)</strong> tích hợp 4 kỹ thuật học sâu (Truy hồi chủ động, Lặp lại ngắt quãng, Xáo trộn, Tự mày mò trước) để phục vụ việc tự học (CLO2).",
            "Đóng gói và kiểm thử thành công <strong>Bộ Harness Nghiệp vụ (Mảnh ghép 1 của Đề án cuối khóa)</strong> vượt qua cả 3 kịch bản stress-test (CLO2)."
        ],
        "story_hook": "Câu chuyện của Minh (Kỳ 3): Minh đã viết được Prompt CRISP rất tốt, nhưng mỗi lần học môn mới hay phân tích một báo cáo mới, Minh lại phải copy-paste lại hàng trang chỉ dẫn. Có lần AI chạy tuốt một mạch từ bước trích xuất số liệu đến bước viết kết luận mà không chờ Minh kiểm tra bảng số liệu trung gian, dẫn đến sai số dây chuyền. Minh học cách đóng gói một 'Bộ dây cương' (Harness) trên Claude Project / Gemini Gem với 2 cổng dừng GATE và tạo riêng một Socratic Tutor để truy bài mình trước kỳ thi.",
        "warmup_questions": [
            "Trong một quy trình nghiệp vụ gồm 5 bước nối tiếp nhau, nếu bước 2 bị sai số liệu mà AI cứ thế chạy thẳng đến bước 5 thì điều gì sẽ xảy ra với kết quả cuối cùng?",
            "Tại sao khi bạn nhờ AI 'giải chi tiết bài tập này giúp tôi', bạn hiểu rất nhanh lúc đọc lời giải nhưng khi vào phòng thi gặp bài tương tự vẫn không làm được?"
        ],
        "timeline": [
            ("Tiết 1 (00' - 50')", "<strong>Kiến trúc 3 tầng Prompt - Context - Harness & Cơ chế GATE / FALLBACK:</strong><br>• Ẩn dụ con ngựa chiến: Prompt (tiếng hô), Context (địa hình), Harness (bộ dây cương, yên ngựa và đường ray).<br>• Giảng viên mở trực tiếp hệ thống Rules, Skills và Project Harness thực tế đang vận hành để demo.<br>• Phân tích sâu 2 chốt chặn kỹ thuật: <strong>GATE (🔒 Dừng chờ người duyệt)</strong> và <strong>FALLBACK (❓ Báo thiếu dữ liệu/chưa đủ căn cứ, không tự đoán)</strong>.", "Quan sát demo thực tế 3 kịch bản: chạy xuôi, thiếu thông tin (FALLBACK kích hoạt) và giục vượt rào (GATE chặn lại).", "Slide Buổi 3; Demo Claude Project / Gem"),
            ("Tiết 2 (50' - 100')", "<strong>Thiết kế Harness cho Sự học: Socratic Tutor & 4 Kỹ thuật học sâu:</strong><br>• Khoa học thần kinh về trí nhớ: <em>Active Recall, Spaced Repetition, Interleaving, Productive Struggle</em>.<br>• Hướng dẫn cấu trúc System Instructions biến AI thành Gia sư Socrates (cấm giải bài hộ, chỉ hỏi gợi mở và chấm từng bước lập luận của sinh viên).", "Tự tay tạo và thử nghiệm 1 Socratic Harness cho môn học chuyên ngành khó nhất đang học tại HUB.", "Thiết bị cá nhân; Template Socratic Harness"),
            ("Tiết 3 (100' - 150')", "<strong>Thực hành Thiết kế & Đóng gói Bộ Harness cho Đề án nhóm:</strong><br>• Nguyên tắc 'Vẽ cho người trước khi vẽ cho AI': các nhóm vẽ sơ đồ quy trình 3-5 bước ra giấy, đánh dấu rõ vị trí GATE 🔒 và FALLBACK ❓.<br>• Số hóa sơ đồ thành System Instructions 4 khối và nạp tài liệu Context mẫu lên Claude Project / Gemini Gem.", "Làm việc nhóm: vẽ sơ đồ quy trình, viết System Instructions 4 khối và đóng gói thành bộ Harness chạy được.", "Giấy thiết kế quy trình; Template Harness 4 khối"),
            ("Tiết 4 (150' - 200')", "<strong>Stress-test 3 kịch bản (Chốt Mảnh ghép 1) & Khóa chốt LMS:</strong><br>• Hướng dẫn các nhóm chạy 3 kịch bản test bắt buộc: (1) Chạy xuôi, (2) Bỏ trống thông tin test FALLBACK, (3) Giục vượt GATE.<br>• Kiểm tra xác nhận hoàn thành <strong>Mảnh ghép 1 của Đề án</strong>.", "Chạy 3 kịch bản test, chụp màn hình minh chứng lưu vào Hồ sơ Đề án (Mảnh ghép 1); viết phản tư 4F và làm Quiz Buổi 3 trên LMS.", "LMS Hub (Quiz 3, Journal 3)")
        ],
        "discussion_questions": [
            "Vì sao 'không đặt cổng GATE ở một bước' cũng phải là một quyết định thiết kế có chủ đích chứ không phải do quên?",
            "Khi mở một cuộc trò chuyện (Conversation) mới bên trong cùng một Project/Gem đã cài Harness, tại sao AI vẫn nhớ toàn bộ quy tắc chấm và tài liệu chuẩn nhưng lại không bị lẫn điểm số của bài làm trước?",
            "Nếu một người bạn nhờ bạn chia sẻ bộ Socratic Harness của bạn, những phần nào bạn có thể giữ nguyên và phần nào bạn ấy cần thay đổi theo mục tiêu riêng?"
        ],
        "homework": """
      <div class="homework-box">
        <h3>1. Nhiệm vụ Cá nhân trên LMS Hub:</h3>
        <ul>
          <li>Hoàn thành đọc và làm Vòng Test 3 cấp độ của <strong>Chương 3 trên eBook SCQA</strong>.</li>
          <li>Hoàn thành <strong>Quiz Buổi 3</strong> (Active Recall 5 lượt) và nộp Feedback tải tài liệu buổi học.</li>
          <li>Viết <strong>Nhật ký học tập (Atomic Note số 3 theo khung 4F)</strong>: Đúc kết trải nghiệm khi tự tay thiết kế cổng GATE/FALLBACK và dùng Socratic Harness để ôn bài.</li>
        </ul>
        <h3>2. Nhiệm vụ Nhóm Đề án cuối khóa (Hoàn tất Mảnh ghép 1):</h3>
        <ul>
          <li>Đóng gói hoàn chỉnh hồ sơ <strong>Mảnh ghép 1</strong> (gồm: Bảng phân vai Người - AI, Sơ đồ quy trình có GATE/FALLBACK, Toàn văn System Instructions + Context mẫu, và Ảnh chụp màn hình vượt qua 3 kịch bản test).</li>
        </ul>
      </div>
        """,
        "review_mc": [
            ("Ba tầng điều phối AI từ thấp đến cao là gì?", "Prompt (Câu lệnh tức thời) -> Context (Ngữ cảnh nền) -> Harness (Bộ khung quy tắc, quy trình nhiều bước và chốt chặn kiểm soát)."),
            ("Hai chốt chặn kỹ thuật quan trọng nhất trong một Workflow Harness là gì?", "GATE (Cổng dừng chờ con người xác nhận) và FALLBACK (Cơ chế báo thiếu thông tin/chưa đủ căn cứ thay vì tự đoán)."),
            ("Bốn kỹ thuật học tập hiệu quả được tích hợp vào Socratic Harness là gì?", "Active Recall (Truy hồi chủ động), Spaced Repetition (Lặp lại ngắt quãng), Interleaving (Xáo trộn) và Productive Struggle (Tự mày mò trước).")
        ],
        "teacher_notes": [
            "Nhắc sinh viên tắt tính năng Memory chéo tự động (nếu cần) khi test các ca nghiệp vụ độc lập để đảm bảo tính khách quan giữa các phiên chạy.",
            "Chấm xác nhận tiến độ Mảnh ghép 1 ngay tại lớp để không nhóm nào bị dồn việc về cuối khóa."
        ]
    },
    {
        "id": 4,
        "module": "MODULE 2: XÂY DỰNG SECOND BRAIN ĐỂ PHÁT TRIỂN SỰ HỌC",
        "title": "Buổi 4: Kiến trúc Second Brain (PARA & CODE) và Ghi chú nguyên tử",
        "subtitle": "Ngoại hóa tri thức, tổ chức thông tin theo hành động (PARA), luồng tinh chế CODE và kỹ thuật viết Atomic Notes + 4F",
        "clo": "CLO3",
        "duration": "4 tiết (200 phút)",
        "objectives": [
            "Giải thích được lý do tại sao người học trong kỷ nguyên AI bắt buộc phải có <strong>Bộ Não Thứ Hai (Second Brain / PKM)</strong> để chống lại sự xói mòn trí nhớ và tạo nguồn Context độc bản (CLO3).",
            "Thiết lập được cấu trúc thư mục quản trị tri thức theo mô hình <strong>PARA (Projects - Areas - Resources - Archives)</strong> và vận hành luồng <strong>CODE (Capture - Organize - Distill - Express)</strong> (CLO3).",
            "Viết được các <strong>Ghi chú nguyên tử (Atomic Notes)</strong> chuẩn mực: 1 ghi chú = 1 luận điểm cốt lõi, tiêu đề khẳng định, diễn đạt 100% bằng ngôn từ của chính mình (không copy-paste AI), có nguồn và liên kết mạng lưới (CLO3).",
            "Khởi tạo kho Second Brain chung cho Đề án nhóm và bắt đầu tích lũy tối thiểu <strong>06 Atomic Notes cá nhân</strong> (chiếm 30% điểm cá nhân cuối khóa) (CLO3)."
        ],
        "story_hook": "Câu chuyện của Minh (Kỳ 4): Sau 3 tuần dùng AI rất mượt, Minh chợt nhận ra ổ cứng của mình có hơn 40 file tài liệu tải về và hàng chục đoạn chat dài với AI, nhưng khi cần viết một trang đề cương nghiên cứu, đầu Minh hoàn toàn trống rỗng. Minh đã mắc chứng 'tích trữ rác số' (digital hoarding): thông tin đi từ AI thẳng vào ổ cứng mà chưa bao giờ đi qua bộ não của Minh. Buổi học thứ 4 giúp Minh đập đi xây lại toàn bộ hệ thống tri thức bằng PARA và những viên gạch Atomic Notes đầu tiên.",
        "warmup_questions": [
            "Thử thách 60 giây: Hãy mở máy tính hoặc điện thoại của bạn và tìm lại một ý tưởng hoặc một kiến thức tâm đắc nhất bạn đã học từ học kỳ trước. Bạn mất bao lâu để tìm ra, hay không thể nhớ nó nằm ở đâu?",
            "Sự khác biệt giữa việc 'lưu một đoạn văn hay của AI vào máy' và việc 'biến kiến thức đó thành tài sản trí tuệ của chính bạn' nằm ở thao tác nào?"
        ],
        "timeline": [
            ("Tiết 1 (00' - 50')", "<strong>Tại sao cần Second Brain trong kỷ nguyên AI & Kiến trúc PARA:</strong><br>• Thử thách tìm lại kiến thức cũ trong 60 giây và phân tích căn bệnh <em>Digital Hoarding</em>.<br>• Triết lý Tiago Forte: <em>'Bộ não sinh ra để nảy sinh ý tưởng, không phải để làm ổ cứng lưu trữ'</em>.<br>• Giải thích mô hình <strong>PARA (Projects - Areas - Resources - Archives)</strong>: nguyên tắc phân loại thông tin theo <em>nơi sẽ hành động</em> thay vì phân loại theo chủ đề tĩnh.", "Kiểm tra lại cách lưu trữ file hiện tại của bản thân; vẽ sơ đồ cây thư mục PARA cho việc học tập và nghiên cứu tại HUB.", "Slide Buổi 4; Sơ đồ PARA"),
            ("Tiết 2 (50' - 100')", "<strong>Luồng vận hành CODE, Giải phẫu Atomic Note & Khung phản tư 4F:</strong><br>• Quy trình 4 bước <strong>C - O - D - E</strong>.<br>• Giải phẫu 4 thành phần của một <strong>Atomic Note</strong> chuẩn: (1) Tiêu đề dạng câu khẳng định (Declarative Title), (2) Nội dung 100-200 chữ bằng ngôn từ riêng, (3) Nguồn tham chiếu chuẩn, (4) Liên kết hai chiều <code>[[Links]]</code>.<br>• Tích hợp khung phản tư <strong>4F (Fact - Feelings - Findings - Future)</strong>.", "So sánh trực diện một bản copy-paste từ AI (Ghi chú rác) và một Atomic Note đã qua tinh chế (Tri thức sống).", "Template Atomic Note & 4F"),
            ("Tiết 3 (100' - 150')", "<strong>Thực hành Dựng không gian Second Brain & Rèn luyện viết Atomic Notes:</strong><br>• Hướng dẫn thiết lập nhanh trên công cụ tự chọn (Obsidian / Notion / Google Docs có cấu trúc liên kết).<br>• Bài tập thực hành: Từ 1 chương tài liệu chuyên ngành, sinh viên đọc hiểu và tự tay viết <strong>03 Atomic Notes</strong> có liên kết chéo với nhau.", "Thực hành cá nhân trên máy tính: dựng PARA và viết 3 Atomic Notes đầu tiên; giảng viên đi từng bàn sửa cách đặt tiêu đề khẳng định.", "Obsidian / Notion / Google Docs"),
            ("Tiết 4 (150' - 200')", "<strong>Studio Đề án (Thiết lập Second Brain dự án) & Khóa chốt LMS:</strong><br>• Hướng dẫn các nhóm thiết lập kho Second Brain cho Đề án và phân công mảng chủ đề để mỗi thành viên tích lũy đủ >= 6 Atomic Notes cá nhân.<br>• Hoàn thành phản tư 4F và Quiz trên LMS.", "Thiết lập quy ước đặt tên và liên kết Atomic Notes trong nhóm Đề án; nộp bài phản tư 4F và hoàn thành Quiz Buổi 4 trên LMS.", "LMS Hub (Quiz 4, Journal 4)")
        ],
        "discussion_questions": [
            "Tại sao cách đặt tiêu đề Atomic Note dạng câu khẳng định hoàn chỉnh (ví dụ: 'Tỷ lệ trích dẫn bịa của LLM tăng mạnh ở các đề tài ít được nghiên cứu') lại vượt trội hơn hẳn cách đặt tiêu đề kiểu nhãn danh từ ('Trích dẫn bịa của AI')?",
            "Làm thế nào một mạng lưới gồm 30 Atomic Notes ngắn gọn lại giúp bạn viết một bài tiểu luận 3.000 chữ nhanh hơn gấp 5 lần so với việc bắt đầu từ một trang Word trắng?",
            "Nếu bạn dùng AI để giải thích một khái niệm khó trong sách, bạn cần làm gì tiếp theo để biến lời giải thích đó thành một Atomic Note hợp lệ của riêng bạn?"
        ],
        "homework": """
      <div class="homework-box">
        <h3>1. Nhiệm vụ Cá nhân trên LMS Hub:</h3>
        <ul>
          <li>Hoàn thành đọc và làm Vòng Test 3 cấp độ của <strong>Chương 4 trên eBook SCQA</strong>.</li>
          <li>Hoàn thành <strong>Quiz Buổi 4</strong> (Active Recall 5 lượt) và nộp Feedback tải tài liệu buổi học.</li>
          <li>Viết <strong>Nhật ký học tập (Atomic Note số 4 theo khung 4F)</strong> và bổ sung tối thiểu <strong>03 Atomic Notes chuyên môn</strong> mới vào thư mục Project Đề án của bạn.</li>
        </ul>
        <h3>2. Nhiệm vụ Nhóm Đề án cuối khóa (Chuẩn bị cho Buổi 5 - Mảnh ghép 2):</h3>
        <ul>
          <li>Mỗi thành viên chuẩn bị sẵn các file tài liệu PDF chuyên ngành và các file Atomic Notes cá nhân của mình để Buổi 5 nạp vào hệ thống <strong>RAG (Gemini Notebook)</strong>.</li>
        </ul>
      </div>
        """,
        "review_mc": [
            ("Bốn thành phần của cấu trúc PARA là gì?", "Projects (Dự án có hạn chót) - Areas (Lĩnh vực trách nhiệm dài hạn) - Resources (Tài nguyên tham khảo) - Archives (Lưu trữ lạnh)."),
            ("Bốn bước của luồng CODE là gì?", "Capture (Thu nạp) -> Organize (Tổ chức) -> Distill (Tinh chế) -> Express (Diễn đạt)."),
            ("Nguyên tắc cốt lõi nhất khi viết nội dung của một Atomic Note là gì?", "Mỗi ghi chú chỉ chứa 1 luận điểm duy nhất, tiêu đề dạng câu khẳng định, được diễn đạt lại bằng 100% ngôn từ và sự hiểu biết của chính mình kèm nguồn và liên kết.")
        ],
        "teacher_notes": [
            "Nhấn mạnh với sinh viên: Công cụ (Obsidian, Notion hay Google Docs) chỉ chiếm 10%, phương pháp viết Atomic Note bằng ngôn từ riêng mới chiếm 90% giá trị.",
            "Nhắc sinh viên đây chính là cấu phần chấm 30% điểm cá nhân ở buổi bảo vệ cuối khóa để mọi thành viên đều tự giác tích lũy ghi chú từ hôm nay."
        ]
    },
    {
        "id": 5,
        "module": "MODULE 2: XÂY DỰNG SECOND BRAIN ĐỂ PHÁT TRIỂN SỰ HỌC",
        "title": "Buổi 5: Tích hợp Second Brain với Công nghệ RAG (Gemini Notebook)",
        "subtitle": "Phân biệt 'Chuyên gia hay bịa' (LLM) với 'Thư ký trung thành' (RAG), truy vấn chéo đa tài liệu và hoàn thành Mảnh ghép 2",
        "clo": "CLO2, CLO3",
        "duration": "4 tiết (200 phút)",
        "objectives": [
            "Giải thích được sự khác biệt về bản chất kỹ thuật giữa <strong>Mô hình ngôn ngữ thuần túy (LLM)</strong> và <strong>Hệ thống tạo sinh tăng cường bằng truy xuất (RAG - như Gemini Notebook / NotebookLM)</strong> (CLO2, CLO3).",
            "Sử dụng thành thạo Gemini Notebook và Claude Projects để nạp đa tài liệu, thực hiện <strong>truy vấn chéo đa nguồn (Cross-document querying)</strong> và kiểm tra trích dẫn tận đoạn văn gốc (CLO3).",
            "Vận hành được vòng lặp cộng hưởng <strong>Second Brain <-> RAG AI</strong> và nhận diện được giới hạn <em>'Grounded Garbage' (Rác nạp vào -> Rác có trích dẫn đi ra)</em> (CLO3).",
            "Hoàn thành và nghiệm thu <strong>Mảnh ghép 2 của Đề án cuối khóa</strong> (Kiến trúc Second Brain + Kho RAG dự án + Tiến độ Atomic Notes cá nhân) (CLO3)."
        ],
        "story_hook": "Câu chuyện của Minh (Kỳ 5): Khi đã có 15 Atomic Notes và 5 báo cáo ngành ngân hàng trong tay, Minh cần đối chiếu xem các báo cáo đó nói gì về rủi ro thanh khoản. Lần này Minh không hỏi khơi khơi trên ChatGPT nữa mà đưa toàn bộ 5 báo cáo cùng các Atomic Notes của mình vào Gemini Notebook (NotebookLM). Ngay lập tức, 'người thư ký trung thành' trả lời kèm các nút trích dẫn [1], [2], [3] nhảy thẳng tới đúng trang 18 và trang 42 của từng báo cáo gốc. Minh đã tìm thấy mảnh ghép kết nối Bộ Não Thứ Hai với sức mạnh xử lý của AI.",
        "warmup_questions": [
            "Nếu bạn giao cho một người thư ký 3 cuốn tài liệu trên bàn và dặn: 'Chỉ được trả lời dựa trên 3 cuốn này và phải chỉ rõ trang mấy', người thư ký đó khác gì với một vị khách chém gió ngoài quán cà phê?",
            "Liệu một hệ thống RAG chỉ đọc tài liệu bạn đưa và luôn trích dẫn đúng số trang có bao giờ đưa ra thông tin sai sự thật không? Khi nào điều đó xảy ra?"
        ],
        "timeline": [
            ("Tiết 1 (00' - 50')", "<strong>Bản chất RAG: 'Thư ký trung thành' vs 'Chuyên gia hay bịa':</strong><br>• Giảng giải cơ chế <em>Retrieval-Augmented Generation (RAG)</em> và bảng so sánh 4 tiêu chí giữa LLM thuần và Gemini Notebook.<br>• Live Demo đối đầu trực tiếp: Cùng một câu hỏi chuyên sâu về quy định ngân hàng, so sánh câu trả lời tự suy diễn của Chatbot thuần với câu trả lời có trích dẫn tận dòng của Gemini Notebook.", "Quan sát Live Demo; ghi nhận cơ chế neo vào nguồn (Grounding) và cách bấm kiểm tra thẻ trích dẫn.", "Slide Buổi 5; Gemini Notebook vs Chatbot"),
            ("Tiết 2 (50' - 100')", "<strong>Vòng lặp Second Brain <-> RAG & Cảnh báo 'Grounded Garbage':</strong><br>• Kỹ thuật nạp đồng thời <em>Tài liệu PDF gốc + Atomic Notes cá nhân</em> vào Gemini Notebook.<br>• Kỹ thuật đặt câu hỏi truy vấn chéo đa tài liệu (so sánh, tìm mâu thuẫn, lập bảng tổng hợp) và khai thác Study Guide / Audio Overview.<br>• Phân tích giới hạn của RAG: <em>'Rác nạp vào -> Rác có trích dẫn đi ra'</em> để dẫn dắt sang Module 3.", "Thực hành kỹ thuật viết câu lệnh truy vấn chéo đa tài liệu và kiểm chứng ngược từng nút trích dẫn [1], [2] trên màn hình.", "Gemini Notebook (notebooklm.google.com)"),
            ("Tiết 3 (100' - 150')", "<strong>Thực hành Xây dựng Kho RAG cho Đề án nhóm:</strong><br>• Mỗi nhóm khởi tạo Kho tri thức RAG cho Đề án cuối khóa, nạp vào các tài liệu chuyên ngành đã thu thập và các Atomic Notes của các thành viên.<br>• Thực hành chạy 3 câu truy vấn đối chiếu đa nguồn và chắt lọc kết quả thành các Atomic Notes mới lưu về Second Brain.", "Làm việc nhóm trên máy tính: dựng kho RAG, chạy truy vấn chéo, bấm kiểm tra từng trích dẫn và viết thêm 2 Atomic Notes mới.", "Thiết bị cá nhân; Kho tài liệu nhóm"),
            ("Tiết 4 (150' - 200')", "<strong>Nghiệm thu Mảnh ghép 2 (Rà soát giữa kỳ) & Khóa chốt LMS:</strong><br>• Giảng viên kiểm tra trực tiếp tiến độ <strong>Mảnh ghép 1 & Mảnh ghép 2</strong> của từng nhóm và rà soát số lượng Atomic Notes cá nhân trên LMS Hub.<br>• Hoàn thành phản tư 4F và Quiz Buổi 5.", "Trình diện cấu trúc PARA, kho RAG và nhật ký Atomic Notes cá nhân để giảng viên rà soát giữa kỳ; làm Quiz Buổi 5 trên LMS.", "LMS Hub (Quiz 5, Journal 5)")
        ],
        "discussion_questions": [
            "Tại sao khi bạn nạp chính các Atomic Notes do bạn viết vào chung với các bài báo khoa học trong Gemini Notebook, kết quả trả về lại sâu sắc và sát với đề tài của bạn hơn hẳn việc chỉ nạp bài báo thô?",
            "Hãy lấy một ví dụ trong ngành Ngân hàng - Tài chính cho thấy hiện tượng 'Grounded Garbage': tài liệu nạp vào có vấn đề dẫn đến câu trả lời của RAG tuy trích dẫn đúng trang nhưng vẫn sai về bản chất khoa học.",
            "Khi nào bạn nên dùng Gemini Notebook, và khi nào bạn nên dùng Claude Projects?"
        ],
        "homework": """
      <div class="homework-box">
        <h3>1. Nhiệm vụ Cá nhân trên LMS Hub:</h3>
        <ul>
          <li>Hoàn thành đọc và làm Vòng Test 3 cấp độ của <strong>Chương 5 trên eBook SCQA</strong>.</li>
          <li>Hoàn thành <strong>Quiz Buổi 5</strong> (Active Recall 5 lượt) và nộp Feedback tải tài liệu buổi học.</li>
          <li>Viết <strong>Nhật ký học tập (Atomic Note số 5 theo khung 4F)</strong>: Đúc kết quy trình phối hợp giữa Second Brain và RAG AI của riêng bạn.</li>
        </ul>
        <h3>2. Nhiệm vụ Nhóm Đề án cuối khóa (Hoàn tất Mảnh ghép 2 & Chuẩn bị sang Module 3 - NCKH):</h3>
        <ul>
          <li>Hoàn thiện hồ sơ <strong>Mảnh ghép 2</strong> (Sơ đồ PARA, Minh chứng kho RAG và tối thiểu 3-4 Atomic Notes đầu tiên của mỗi thành viên).</li>
          <li>Tạo tài khoản miễn phí trên <strong>Semantic Scholar, Elicit và Consensus</strong> để sẵn sàng bước vào Module 3 (Nghiên cứu khoa học & Kiểm chứng) ở Buổi 6.</li>
        </ul>
      </div>
        """,
        "review_mc": [
            ("RAG là viết tắt của cụm từ nào và nguyên lý cốt lõi của nó là gì?", "Retrieval-Augmented Generation: truy xuất các đoạn văn bản liên quan từ kho tài liệu do người dùng nạp vào trước, rồi mới dùng đó làm căn cứ trả lời kèm trích dẫn."),
            ("Trong ẩn dụ sư phạm, Gemini Notebook đóng vai trò gì so với Chatbot LLM thuần?", "Đóng vai trò 'Người thư ký trung thành' chỉ đọc tài liệu được giao và chỉ rõ số trang/đoạn gốc."),
            ("Hiện tượng 'Grounded Garbage' trong RAG nhắc nhở chúng ta điều gì?", "RAG không thể biến tài liệu rác thành vàng; nếu nạp nguồn giả hoặc nguồn kém chất lượng thì RAG sẽ trích dẫn rất trung thành cái sai đó.")
        ],
        "teacher_notes": [
            "Buổi 5 là cột mốc giữa khóa (5/11 buổi): giảng viên dành Tiết 4 để rà soát bảng điều khiển Admin trên LMS Hub, nhắc nhở kịp thời những sinh viên chưa làm đủ Quiz hoặc chưa viết đủ Atomic Notes.",
            "Nhấn mạnh hạn chế 'Grounded Garbage' của RAG ở cuối buổi để tạo động lực tự nhiên cho Buổi 6: Làm sao để tìm và thẩm định được nguồn học thuật thật?"
        ]
    },
    {
        "id": 6,
        "module": "MODULE 3: ỨNG DỤNG AI TRONG NGHIÊN CỨU KHOA HỌC & KIỂM CHỨNG",
        "title": "Buổi 6: Quy trình NCKH với AI (Bước 1 & 2) - Tìm nguồn thật & 'Soi 3 phút'",
        "subtitle": "Quy tắc 'Nguồn thật trước, AI sau', Semantic Scholar/Elicit/Consensus, Prompt tóm tắt 7 mục và thực nghiệm 'Soi 3 phút' (Case Hemani 2026)",
        "clo": "CLO4",
        "duration": "4 tiết (200 phút)",
        "objectives": [
            "Vận hành được bức tranh tổng thể <strong>Quy trình NCKH 4 bước có AI đồng hành (Tìm -> Đọc -> Tổng hợp -> Viết)</strong> với kỷ luật Kiểm chứng xuyên suốt cả 4 bước (CLO4).",
            "Áp dụng được <strong>Phễu thu hẹp câu hỏi nghiên cứu</strong> và sử dụng đúng bộ 3 công cụ tìm nguồn học thuật thật: <strong>Semantic Scholar, Elicit, Consensus</strong> (hiểu đúng Consensus Meter và chuỗi 5 câu hỏi sau chữ Yes) (CLO4).",
            "Sử dụng thành thạo <strong>Prompt tóm tắt bài báo khoa học 7 mục</strong> kèm chốt chặn <em>'Không suy đoán'</em> trên file PDF đính kèm (CLO4).",
            "Thực hiện được kỹ năng <strong>'Soi bản tóm tắt trong 3 phút'</strong> (Đối chiếu số liệu - Truy chỗ AI thêm/thiếu bối cảnh - Hỏi ngược về hạn chế) để phát hiện cả lỗi suy diễn của AI (như vụ tự bịa <code>Pearson's R</code>) lẫn lỗi phương pháp của bài báo gốc (CLO4)."
        ],
        "story_hook": "Câu chuyện của Minh (Kỳ 6): Bắt tay vào viết phần Tổng quan nghiên cứu cho Đề án về Ngân hàng số, Minh tải một bài báo tiếng Anh (bài Hemani, 2026) lên AI để tóm tắt. Nhìn bảng tóm tắt 7 mục chuyên nghiệp có ghi 'Phương pháp: Tương quan Pearson (Pearson's R), mẫu 192 sinh viên, r ~ 0.62', Minh định chép ngay vào bài. Nhưng khi áp dụng kỹ thuật 'Soi 3 phút' của thầy, Minh mở file PDF gốc bấm Ctrl+F tìm chữ 'Pearson' thì kết quả trả về là... 0 lần xuất hiện! Minh bừng tỉnh: AI vừa tự ý nâng cấp một phép tính Excel mơ hồ trong một bài báo kém chất lượng thành thuật ngữ thống kê chuyên ngành nghe cực kỳ kêu!",
        "warmup_questions": [
            "Khi bạn đọc một bản tóm tắt bài báo khoa học do AI xuất ra và thấy các con số (như 82%, r = 0.62) khớp y hệt trang 4 của bài báo gốc, bạn đã có thể yên tâm 100% để dùng con số đó làm bằng chứng khoa học chưa? Vì sao?",
            "Nếu một bài báo gốc viết rất mơ hồ về phương pháp phân tích dữ liệu, tại sao AI lại có xu hướng 'tự điền thêm tên một phương pháp thống kê chuyên nghiệp' vào bản tóm tắt?"
        ],
        "timeline": [
            ("Tiết 1 (00' - 50')", "<strong>Quy trình NCKH 4 bước & Bước 1 (Tìm nguồn thật):</strong><br>• Bức tranh lớn: <strong>Tìm -> Đọc -> Tổng hợp -> Viết</strong> (Kiểm chứng xuyên suốt). Quy tắc số 1: <em>'Nguồn thật trước, AI sau'</em>.<br>• Phễu thu hẹp chủ đề mơ hồ thành câu hỏi nghiên cứu cụ thể.<br>• Thực hành chọn công cụ có kho nguồn thật: <strong>Semantic Scholar</strong> (>200 triệu bài), <strong>Elicit</strong> (bảng trích xuất theo cột), <strong>Consensus</strong> (hiểu đúng Đồng hồ đo Yes/No thực nghiệm và chuỗi 5 câu hỏi sau chữ Yes).", "Thực hành đi qua Phễu thu hẹp cho đề tài Đề án nhóm; tra cứu trực tiếp trên Semantic Scholar, Elicit và Consensus.", "Slide Buổi 6; Semantic Scholar, Elicit, Consensus"),
            ("Tiết 2 (50' - 100')", "<strong>Bước 2 (Đọc với AI) & Giải phẫu Prompt Tóm tắt 7 mục:</strong><br>• Nguyên tắc bất di bất dịch: Tải file PDF đầy đủ lên AI (DeepSeek / Claude / Gemini Notebook), không gõ tên bài bắt AI nhớ lại.<br>• Giải phẫu Prompt 7 mục (Câu hỏi NC, Phương pháp, Mẫu, Kết quả, Hạn chế, Đóng góp, Điều cần kiểm tra lại) + Ràng buộc số trang + Chốt chặn <em>'Chỗ nào bài không nói, ghi không nêu trong bài, không suy đoán'</em>.", "Lưu mẫu Prompt tóm tắt 7 mục vào Second Brain; tải thử 1 file PDF bài báo mẫu để chuẩn bị thực hành soi.", "Mẫu Prompt Tóm tắt 7 mục"),
            ("Tiết 3 (100' - 150')", "<strong>Thực nghiệm 'Soi bản tóm tắt trong 3 phút' (Case study Hemani 2026):</strong><br>• Phát bài báo mẫu <em>Hemani (2026, IJSDR)</em> và bảng kết quả 7 mục của DeepSeek.<br>• Cả lớp cùng thực hiện 3 thao tác soi trực tiếp trên PDF gốc:<br>  1. <em>Soi 1 (Đối chiếu số liệu):</em> 82%, 41%, r ~ 0.62 khớp tr.4 nhưng bài gốc chỉ cho số xấp xỉ '~', thiếu bảng hệ số và thiếu p-value.<br>  2. <em>Soi 2 (Truy chỗ AI thêm & thiếu bối cảnh):</em> Số 192 ở Kết quả (tr.4) vs dự kiến 150-200 ở Phương pháp (tr.3); và phát hiện chấn động: chữ <strong>'Pearson' xuất hiện 0 lần</strong> trong bài gốc!<br>  3. <em>Soi 3 (Hỏi ngược về Hạn chế):</em> Chữ 'limitation' xuất hiện 0 lần; nhờ câu 'không suy đoán' mà AI tách bạch được phần bài không nêu và phần nhận xét của người đọc.", "Mở trực tiếp file PDF Hemani (2026), bấm Ctrl+F kiểm chứng từng phát hiện; thảo luận về 2 tầng phê phán (soi lỗi của AI và soi chất lượng của chính bài báo).", "PDF bài báo Hemani (2026) & Ảnh chụp bảng 7 mục DeepSeek"),
            ("Tiết 4 (150' - 200')", "<strong>Thực hành Tìm nguồn thật & Lập Biên bản 'Soi 3 phút' cho Đề án:</strong><br>• Mỗi thành viên trong nhóm tìm 3 bài báo khoa học thật (có PDF và DOI) cho Đề án nhóm, chọn 1 bài chạy Prompt 7 mục và lập Biên bản Soi 3 phút.<br>• Hoàn thành phản tư 4F và Quiz Buổi 6.", "Tìm 3 bài báo thật/người; chạy tóm tắt 7 mục và điền Biên bản Soi 3 phút cho Đề án nhóm; làm Quiz Buổi 6 trên LMS.", "LMS Hub (Quiz 6, Journal 6)")
        ],
        "discussion_questions": [
            "Tại sao loại lỗi AI tự thêm thuật ngữ chuyên môn (như tự thêm chữ 'Pearson's R' khi thấy ký hiệu r ~ 0.62) lại là loại lỗi nguy hiểm nhất đối với sinh viên làm nghiên cứu?",
            "Sự khác biệt giữa 'bản tóm tắt trung thực với bài báo' và 'bài báo có số liệu đáng tin cậy' là gì? Tại sao người nghiên cứu phải kiểm tra cả hai?",
            "Nếu trong Prompt tóm tắt 7 mục bạn quên viết câu 'Chỗ nào bài không nói, ghi không nêu trong bài, không suy đoán', AI sẽ làm gì ở ô số 5 (Hạn chế của nghiên cứu) đối với một bài báo không hề có mục Limitations?"
        ],
        "homework": """
      <div class="homework-box">
        <h3>1. Nhiệm vụ Cá nhân trên LMS Hub:</h3>
        <ul>
          <li>Hoàn thành đọc và làm Vòng Test 3 cấp độ của <strong>Chương 6 trên eBook SCQA</strong>.</li>
          <li>Hoàn thành <strong>Quiz Buổi 6</strong> (Active Recall 5 lượt) và nộp Feedback tải tài liệu buổi học.</li>
          <li>Viết <strong>Nhật ký học tập (Atomic Note số 6 theo khung 4F)</strong>: Ghi lại bài học lớn nhất của bạn từ màn thực nghiệm 'Soi 3 phút' bài báo Hemani (2026).</li>
        </ul>
        <h3>2. Nhiệm vụ Nhóm Đề án cuối khóa (Chuẩn bị cho Buổi 7 - Kiểm chứng 5 bước & Zotero):</h3>
        <ul>
          <li>Mỗi thành viên hoàn thành tìm kiếm tối thiểu <strong>03 bài báo/nguồn tài liệu thật</strong> cho Đề án (tổng cộng nhóm có 9 - 12 nguồn) kèm ít nhất 02 Biên bản 'Soi 3 phút'.</li>
          <li>Cài đặt sẵn phần mềm <strong>Zotero 8</strong> và tiện ích <strong>Zotero Connector</strong> trên trình duyệt máy tính cá nhân trước khi đến lớp Buổi 7.</li>
        </ul>
      </div>
        """,
        "review_mc": [
            ("Quy tắc số 1 trong nghiên cứu khoa học có AI đồng hành là gì?", "Nguồn thật trước, AI sau: tìm trong kho tài liệu thật (Semantic Scholar, Elicit, Consensus), đọc có đối chiếu rồi mới nhờ AI dựng khung."),
            ("Ba thao tác của quy trình 'Soi bản tóm tắt trong 3 phút' là gì?", "(1) Đối chiếu số liệu với bảng/hình gốc, (2) Truy chỗ AI tự thêm hoặc thiếu bối cảnh, (3) Hỏi ngược về hạn chế (Limitations)."),
            ("Hai loại lỗi tinh vi của AI phát hiện được ở thao tác Soi 2 trong bài Hemani (2026) là gì?", "Một là trích đúng chữ nhưng thiếu bối cảnh (cỡ mẫu thực tế 192 ở Kết quả vs dự kiến 150-200 ở Phương pháp); hai là tự suy diễn thêm thuật ngữ chuyên môn không có trong bài (Pearson's R).")
        ],
        "teacher_notes": [
            "Buổi 6 là một trong những buổi tạo khoảnh khắc 'Aha!' mạnh nhất khóa học nhờ bài báo Hemani (2026). Hãy để sinh viên tự tay bấm Ctrl+F tìm chữ 'Pearson' và chữ 'limitation' trên file PDF để tự chứng nghiệm.",
            "Nhắc sinh viên cài sẵn Zotero 8 ở nhà để Tiết 3 Buổi 7 thực hành trôi chảy."
        ]
    },
    {
        "id": 7,
        "module": "MODULE 3: ỨNG DỤNG AI TRONG NGHIÊN CỨU KHOA HỌC & KIỂM CHỨNG",
        "title": "Buổi 7: Trích dẫn bịa, Checklist Kiểm chứng 5 bước, Tomaca & Zotero 8",
        "subtitle": "Quy tắc 'Chưa kiểm chứng, chưa vào bài', Quy luật Linardon (19.9% / 29%), Thực hành công cụ Tomaca và khóa chốt bằng Zotero 8",
        "clo": "CLO4",
        "duration": "4 tiết (200 phút)",
        "objectives": [
            "Phân tích được quy luật thực nghiệm của <strong>Linardon và cs. (2025)</strong> về trích dẫn bịa (19.9% bịa hoàn toàn, 56.3% có lỗi, tăng lên 28%-29% ở đề tài ít được nghiên cứu) và nhận diện được cấu trúc 'ghép xác' của một trích dẫn giả (CLO4).",
            "Thực hiện thành thạo <strong>Checklist Kiểm chứng một Trích dẫn qua 5 Bước</strong> theo thứ tự từ rẻ đến tốn công (đặc biệt là Bước 3 và Bước 4 trên bản PDF gốc) (CLO4).",
            "Sử dụng được công cụ <strong>Tomaca</strong> để rà soát nhanh danh mục tài liệu, đọc hiểu 3 nhóm kết quả và nắm vững giới hạn thật của máy theo nguyên tắc <em>'Máy soát, người quyết'</em> (CLO4).",
            "Thiết lập và vận hành thành thạo quy trình 3 bước trên <strong>Zotero 8</strong> (<em>'Nguồn vào Zotero trước, rồi mới vào bài'</em>) cho toàn bộ 9-12 nguồn tài liệu của Đề án nhóm (CLO4)."
        ],
        "story_hook": "Câu chuyện của Minh (Kỳ 7): Một thành viên trong nhóm của Minh dùng ChatGPT viết nháp một đoạn tổng quan có kèm 5 trích dẫn nhìn cực kỳ uy tín, có đủ tên tác giả lớn, tên tạp chí Q1 và cả mã DOI. Khi Minh đưa danh sách này qua Checklist 5 bước và công cụ Tomaca, cả nhóm bàng hoàng phát hiện: 2 bài hoàn toàn không tồn tại, và 1 bài có mã DOI thật nhưng khi bấm vào lại dẫn sang một bài báo y khoa về phẫu thuật thận chứ không liên quan gì đến ngân hàng! Minh thiết lập kỷ luật thép cho cả nhóm: Mọi tài liệu phải qua 5 bước kiểm chứng và nằm trong Zotero trước khi được phép bước chân vào file Word của Đề án.",
        "warmup_questions": [
            "Nếu một trích dẫn có tên tác giả thật trong ngành Ngân hàng, tên tạp chí thật, năm 2025 và có cả mã DOI bắt đầu bằng 10.1016/..., theo bạn xác suất nó là một bài báo hoàn toàn không tồn tại là bao nhiêu?",
            "Tại sao AI lại bịa tài liệu tham khảo nhiều nhất ở đúng những đề tài mới, ít người nghiên cứu - nơi mà sinh viên làm khóa luận đang cần nó giúp nhất?"
        ],
        "timeline": [
            ("Tiết 1 (00' - 50')", "<strong>Quy luật Linardon (2025) & Giải phẫu một Trích dẫn bịa dạng 'Ghép xác':</strong><br>• Phân tích số liệu thực nghiệm của Linardon và cs. (2025, <em>JMIR Mental Health</em>): 19.9% bịa hoàn toàn, 56.3% bịa hoặc sai; tỷ lệ bịa vọt từ 6% (chủ đề phổ biến) lên <strong>28% - 29% (đề tài ít được nghiên cứu, p = .001)</strong>.<br>• Giải phẫu trích dẫn bịa trong bài <em>Ren và cs. (2025 - bịa 18/30 trích dẫn = 60%)</em> và hiện tượng 21/33 DOI bịa dẫn sang bài báo không liên quan.", "Phân tích ví dụ thật về trích dẫn bịa; nhận diện 5 mảnh ghép mà AI dùng để ngụy tạo một trích dẫn trông như thật.", "Slide Buổi 7; Nghiên cứu Linardon (2025) & Ren (2025)"),
            ("Tiết 2 (50' - 100')", "<strong>Checklist Kiểm chứng một Trích dẫn qua 5 Bước (Từ rẻ đến tốn công):</strong><br>• Hướng dẫn thực hành 5 bước: (1) <em>Có thật không?</em> (Scholar / doi.org) -> (2) <em>Thông tin thư mục khớp không?</em> -> (3) <em>Bài gốc có nói đúng ý đó không?</em> -> (4) <em>Số liệu khớp bảng/hình không?</em> -> (5) <em>Còn hiệu lực trên Retraction Watch không?</em><br>• Nhấn mạnh tầm quan trọng sống còn của Bước 3 và Bước 4.", "Thực hành kiểm chứng trực tiếp 3 trích dẫn mẫu bằng tay qua đủ 5 bước trên Google Scholar, doi.org, PDF gốc và Retraction Watch.", "Poster Checklist 5 bước"),
            ("Tiết 3 (100' - 150')", "<strong>Công cụ Tomaca ('Máy soát, Người quyết') & Khóa chốt bằng Zotero 8:</strong><br>• Demo và thực hành công cụ <strong>Tomaca</strong> (TS. Trần Việt Tâm): cách đọc 3 nhóm kết quả (<code>verified-doi</code>, <code>no-doi/doi-not-found</code>, <code>metadata-mismatch</code>) và bài học từ bộ test thực tế ngày 17/10/2026 (khi máy bỏ lọt 2 trích dẫn giả có DOI trỏ sang bài khác).<br>• Thực hành 3 bước với <strong>Zotero 8</strong>: Lưu qua Connector từ trang gốc -> Chèn vào Word từ thư viện -> Đổi chuẩn APA 7 / IEEE trong 1 cú nhấp.", "Tải danh sách tài liệu lên Tomaca đọc báo cáo; thực hành lưu bài báo thật qua Zotero Connector và chèn trích dẫn tự động vào file báo cáo.", "pro-tomaca.quyentrungga.com & Phần mềm Zotero 8"),
            ("Tiết 4 (150' - 200')", "<strong>Thử thách 'Lọc rác Học thuật' & Kiểm chứng nguồn Đề án nhóm:</strong><br>• Cuộc thi nhóm 20 phút: Lọc sạch 1 danh sách 10 tài liệu tham khảo ngành Tài chính - Ngân hàng có trộn bẫy.<br>• Các nhóm kiểm chứng toàn bộ 9-12 nguồn của Đề án nhóm qua Checklist 5 bước + Tomaca và nạp 100% vào Zotero.", "Hoàn thành bảng kiểm chứng 5 bước + báo cáo Tomaca + thư viện Zotero cho Đề án nhóm; viết phản tư 4F và làm Quiz Buổi 7 trên LMS.", "LMS Hub (Quiz 7, Journal 7)")
        ],
        "discussion_questions": [
            "Tại sao một trích dẫn 'có thật 100% trên Google Scholar nhưng bị AI gán cho một ý mà tác giả không hề nói' (vi phạm Bước 3) lại khó phát hiện và nguy hiểm hơn cả một trích dẫn bịa hoàn toàn?",
            "Trong thử nghiệm công cụ Tomaca ngày 17/10/2026 với 10 trích dẫn (7 thật, 3 giả), tại sao máy lại báo verified-doi cho 9 mục (bỏ lọt 2 mục giả)? Điều này chứng minh nguyên tắc nào trong làm việc với công cụ kiểm tra tự động?",
            "Quy tắc 'Nguồn vào Zotero trước, rồi mới vào bài' thay đổi thói quen viết báo cáo của bạn như thế nào?"
        ],
        "homework": """
      <div class="homework-box">
        <h3>1. Nhiệm vụ Cá nhân trên LMS Hub:</h3>
        <ul>
          <li>Hoàn thành đọc và làm Vòng Test 3 cấp độ của <strong>Chương 7 trên eBook SCQA</strong>.</li>
          <li>Hoàn thành <strong>Quiz Buổi 7</strong> (Active Recall 5 lượt) và nộp Feedback tải tài liệu buổi học.</li>
          <li>Viết <strong>Nhật ký học tập (Atomic Note số 7 theo khung 4F)</strong>: Đúc kết quy trình 5 bước kiểm chứng và nguyên tắc 'Máy soát, người quyết'.</li>
        </ul>
        <h3>2. Nhiệm vụ Nhóm Đề án cuối khóa (Chuẩn bị cho Buổi 8 - Mảnh ghép 3):</h3>
        <ul>
          <li>Đảm bảo 100% tài liệu tham khảo của Đề án nhóm (9 - 12 nguồn) đã qua <strong>Checklist 5 bước + có báo cáo PDF từ Tomaca + đã nằm gọn trong thư viện Zotero 8</strong> của nhóm để Buổi 8 lập Ma trận tổng hợp và viết báo cáo.</li>
        </ul>
      </div>
        """,
        "review_mc": [
            ("Theo Linardon và cs. (2025), tỷ lệ trích dẫn bịa hoàn toàn và tổng tỷ lệ trích dẫn có vấn đề của GPT-4o là bao nhiêu?", "19.9% bịa hoàn toàn (35/176); nếu tính cả trích dẫn thật nhưng sai thông tin thư mục là 56.3% (99/176)."),
            ("Năm bước trong Checklist kiểm chứng trích dẫn là gì?", "(1) Có thật không? -> (2) Thông tin khớp không? -> (3) Bài nói đúng ý không? -> (4) Số liệu khớp không? -> (5) Còn hiệu lực trên Retraction Watch không?"),
            ("Ba bước của quy trình Zotero 8 để chống trích dẫn bịa là gì?", "(1) Lưu nguồn thật qua Zotero Connector khi đang mở bài gốc -> (2) Chèn trích dẫn từ thư viện Zotero vào Word (không gõ tay/copy AI) -> (3) Chọn/đổi kiểu trích dẫn APA/IEEE tự động.")
        ],
        "teacher_notes": [
            "Chuẩn bị sẵn file bài tập '10 trích dẫn trộn bẫy ngành Tài chính - Ngân hàng' (gồm 5 bài chuẩn, 2 bài bịa hoàn toàn, 2 bài lấy DOI của bài khác ghép vào, 1 bài gán ngược kết luận của tác giả) cho hoạt động đua nhóm ở Tiết 4.",
            "Kiểm tra chắc chắn mỗi nhóm đều xuất được file thư viện Zotero (.bib hoặc .ris) và biết cách chèn citation vào Word/Docs."
        ]
    },
    {
        "id": 8,
        "module": "MODULE 3: ỨNG DỤNG AI TRONG NGHIÊN CỨU KHOA HỌC & KIỂM CHỨNG",
        "title": "Buổi 8: Quy trình NCKH với AI (Bước 3 & 4) - Tổng hợp, Viết & Trình bày",
        "subtitle": "Lập Ma trận Tổng hợp (Synthesis Matrix), Quy trình viết học thuật 4 nhịp từ Second Brain + Zotero và Làm slide 4 lớp (Chốt Mảnh ghép 3)",
        "clo": "CLO3, CLO4",
        "duration": "4 tiết (200 phút)",
        "objectives": [
            "Phân biệt rõ <strong>Tóm tắt rời rạc (Summary)</strong> với <strong>Tổng hợp đối sánh đa nguồn (Synthesis)</strong> và lập được <strong>Ma trận Tổng hợp (Synthesis Matrix)</strong> cho 9-12 nguồn tài liệu của Đề án (CLO4).",
            "Thực hiện được <strong>Quy trình viết học thuật 4 nhịp</strong> kết hợp giữa Atomic Notes trong Second Brain, sự phản biện dàn ý của AI và thao tác chèn trích dẫn chuẩn từ <strong>Zotero 8</strong> (CLO3, CLO4).",
            "Áp dụng được <strong>Quy trình 4 lớp thiết kế bài trình bày khoa học</strong> theo nguyên tắc <em>'AI làm Draft, Người làm Final'</em> (CLO3, CLO4).",
            "Hoàn thành <strong>Mảnh ghép 3 của Đề án cuối khóa</strong> (Bản thảo Báo cáo nghiên cứu/giải pháp nghiệp vụ có Ma trận tổng hợp và trích dẫn Zotero chuẩn APA 7) (CLO4)."
        ],
        "story_hook": "Câu chuyện của Minh (Kỳ 8): Có 10 bài báo thật trong Zotero rồi, nhưng khi ghép lại, bản nháp đầu tiên của nhóm Minh trông giống như 10 đoạn tóm tắt rời rạc dán nối đuôi nhau: 'Tác giả A nói..., Tác giả B nói...'. Giảng viên hướng dẫn nhóm Minh kẻ một bảng Ma trận Tổng hợp (Synthesis Matrix) theo 4 cột chủ đề trên Gemini Notebook + Elicit. Ngay khi nhìn vào bảng, cả nhóm thấy rõ 4 tác giả đồng thuận ở điểm nào, 2 tác giả mâu thuẫn ở đâu và phát hiện ra đúng khoảng trống nghiên cứu cho Đề án của nhóm!",
        "warmup_questions": [
            "Khi đọc phần Tổng quan tài liệu của một bài tiểu luận, làm sao người chấm nhận ra ngay bài đó chỉ là '10 đoạn tóm tắt xếp cạnh nhau' chứ chưa hề có sự 'tổng hợp' (Synthesis)?",
            "Nếu bạn dùng các công cụ như Gamma hay Copilot để tạo 10 trang slide chỉ bằng 1 cú nhấp chuột, điều gì sẽ thiếu vắng trên những trang slide đó khiến Hội đồng chấm điểm không bị thuyết phục?"
        ],
        "timeline": [
            ("Tiết 1 (00' - 50')", "<strong>Bước 3 (Tổng hợp đa nguồn): Lập Ma trận Tổng hợp (Synthesis Matrix):</strong><br>• Phân biệt <em>Summary</em> (kể từng bài A -> B -> C) vs <em>Synthesis</em> (đặt A, B, C lên cùng bàn cân theo biến số/chủ đề để tìm đồng thuận, mâu thuẫn và Research Gap).<br>• Hướng dẫn kết hợp bảng trích xuất của <strong>Elicit</strong> và kho <strong>Gemini Notebook</strong> để lập Synthesis Matrix có gắn số trang kiểm chứng.", "Thực hành nhóm: Thiết kế các cột tiêu chí và lập Ma trận Tổng hợp cho 9-12 nguồn tài liệu đã kiểm chứng của Đề án nhóm.", "Slide Buổi 8; Elicit & Gemini Notebook"),
            ("Tiết 2 (50' - 100')", "<strong>Bước 4 (Viết học thuật 4 nhịp): Second Brain + AI Phản biện + Zotero 8:</strong><br>• Giảng và demo 4 nhịp viết: (1) Sắp xếp <em>Atomic Notes</em> thành dàn ý -> (2) Nhờ AI đóng vai <em>Devil's Advocate</em> phản biện dàn ý -> (3) Người học tự viết bản thảo từ Ma trận tổng hợp và chèn trích dẫn từ <strong>Zotero 8</strong> -> (4) Dùng AI biên tập văn phong với chốt chặn giữ nguyên luận điểm và mã Zotero.", "Thực hành viết 1 mục Tổng quan & Phân tích (300-500 chữ) từ Ma trận tổng hợp của nhóm, thực hành chèn trích dẫn Zotero theo chuẩn APA 7.", "Word / Google Docs + Zotero 8 Plugin"),
            ("Tiết 3 (100' - 150')", "<strong>Quy trình 4 lớp Chuẩn bị Bài trình bày Khoa học ('AI làm Draft, Người làm Final'):</strong><br>• Lớp 1: Cấu trúc Storyline & SCQA.<br>• Lớp 2: Kịch bản thuyết trình gắn trải nghiệm thực nghiệm thật.<br>• Lớp 3: Thiết kế trực quan (dùng tiêu đề kết luận Action Titles, loại bỏ sự chung chung của slide AI tự động).<br>• Lớp 4: Đưa bằng chứng sống (ảnh chạy Harness, báo cáo Tomaca, Zotero, Atomic Notes) lên slide.", "Phác thảo cấu trúc Storyline 10 slide cho bài bảo vệ Đề án cuối khóa của nhóm theo đúng 4 lớp.", "Gamma / PowerPoint / HTML Slides"),
            ("Tiết 4 (150' - 200')", "<strong>Studio Đề án (Chốt Mảnh ghép 3) & Khóa chốt LMS:</strong><br>• Các nhóm hoàn thiện Bản thảo Báo cáo Đề án (Mảnh ghép 3) kèm Ma trận tổng hợp, biên bản Soi 3 phút, bảng kiểm chứng 5 bước và danh mục Zotero.<br>• Hoàn thành phản tư 4F và Quiz Buổi 8.", "Nộp bản thảo Mảnh ghép 3; viết Atomic Note phản tư 4F và hoàn thành Quiz Buổi 8 trên LMS Hub.", "LMS Hub (Quiz 8, Journal 8)")
        ],
        "discussion_questions": [
            "Tại sao ở Nhịp 4 (biên tập văn phong), nếu bạn chỉ nói 'Hãy viết lại đoạn này cho hay hơn' mà không cài chốt chặn 'Cấm thay đổi luận điểm, cấm thêm số liệu và giữ nguyên mã trích dẫn Zotero', AI rất dễ phá hỏng tính chính xác khoa học của đoạn văn bạn vừa dày công kiểm chứng?",
            "Làm thế nào một tiêu đề slide dạng câu kết luận (Action Title - ví dụ: 'Cổng dừng GATE 1 giúp loại bỏ 100% lỗi lệch số liệu trước khi viết nhận xét') lại hiệu quả hơn tiêu đề dạng danh từ chung chung ('Kết quả thử nghiệm hệ thống')?",
            "Trong một nhóm 4 người cùng viết chung một báo cáo Đề án, làm thế nào để sử dụng Zotero Group Library và kho Second Brain chung để không bị trùng lặp hay mất định dạng trích dẫn?"
        ],
        "homework": """
      <div class="homework-box">
        <h3>1. Nhiệm vụ Cá nhân trên LMS Hub:</h3>
        <ul>
          <li>Hoàn thành đọc và làm Vòng Test 3 cấp độ của <strong>Chương 8 trên eBook SCQA</strong>.</li>
          <li>Hoàn thành <strong>Quiz Buổi 8</strong> (Active Recall 5 lượt) và nộp Feedback tải tài liệu buổi học.</li>
          <li>Viết <strong>Nhật ký học tập (Atomic Note số 8 theo khung 4F)</strong> và hoàn tất chỉ tiêu tối thiểu <strong>06 Atomic Notes chuyên môn cá nhân</strong> đóng góp vào Đề án nhóm.</li>
        </ul>
        <h3>2. Nhiệm vụ Nhóm Đề án cuối khóa (Hoàn tất Mảnh ghép 3):</h3>
        <ul>
          <li>Hoàn chỉnh toàn văn <strong>Báo cáo Đề án (Mảnh ghép 3)</strong> có đầy đủ Ma trận tổng hợp, Biên bản Soi 3 phút, Bảng kiểm chứng 5 bước + Báo cáo Tomaca và Danh mục tài liệu tham khảo xuất tự động từ Zotero 8.</li>
        </ul>
      </div>
        """,
        "review_mc": [
            ("Điểm khác biệt cốt lõi của Ma trận Tổng hợp (Synthesis Matrix) so với việc tóm tắt từng bài là gì?", "Đặt nhiều bài báo đã kiểm chứng lên cùng các cột tiêu chí/chủ đề để đối sánh điểm đồng thuận, điểm mâu thuẫn và làm lộ diện khoảng trống nghiên cứu (Research Gap)."),
            ("Bốn nhịp của quy trình viết học thuật với AI là gì?", "(1) Lắp ghép dàn ý từ Atomic Notes trong Second Brain -> (2) Nhờ AI phản biện dàn ý -> (3) Tự viết bản thảo & chèn trích dẫn từ Zotero 8 -> (4) Dùng AI biên tập ngôn ngữ có ràng buộc giữ nguyên luận điểm và trích dẫn."),
            ("Nguyên tắc cốt lõi khi dùng AI hỗ trợ làm slide thuyết trình là gì?", "'AI làm Draft, Người làm Final': con người giữ quyền thiết kế thông điệp kết luận (Action Titles) và đưa bằng chứng thực nghiệm thật của nhóm lên slide.")
        ],
        "teacher_notes": [
            "Hướng dẫn kỹ cho sinh viên cách dùng câu nối tổng hợp đa nguồn (ví dụ: 'Trong khi Nguyễn (2024) và Smith (2025) cùng chỉ ra..., Trần (2026) lại phát hiện rằng...') để nâng tầm văn phong báo cáo.",
            "Kiểm tra để đảm bảo danh mục tài liệu tham khảo cuối báo cáo của các nhóm là trường dữ liệu động (dynamic field) do Zotero tạo ra chứ không phải gõ tay."
        ]
    },
    {
        "id": 9,
        "module": "MODULE 4: AN TOÀN, ĐẠO ĐỨC, PHÁP LÝ & ĐỒ ÁN TỔNG HỢP",
        "title": "Buổi 9: Đạo đức học thuật, Pháp lý (Thông tư 49/2026) & An toàn dữ liệu",
        "subtitle": "Thông tư 49/2026/TT-BGDĐT (Điều 10), Luật AI 134/2025, Chuẩn COPE/ICMJE, Đèn giao thông (Xanh-Vàng-Đỏ), Bảo mật dữ liệu ngân hàng & Mẫu khai báo AI",
        "clo": "CLO5",
        "duration": "4 tiết (200 phút)",
        "objectives": [
            "Nắm vững và vận dụng đúng quy định pháp lý Việt Nam mới nhất về liêm chính học thuật với AI: <strong>Thông tư 49/2026/TT-BGDĐT (Điều 10 - 6 nhóm hành vi vi phạm, nghĩa vụ công bố việc dùng AI)</strong>, <strong>Luật AI 134/2025/QH15</strong> và <strong>Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15</strong> (CLO5).",
            "Tuân thủ <strong>4 nguyên tắc xuất bản quốc tế (COPE, ICMJE, ALLEA, WAME, Elsevier)</strong> và phân định chính xác các hành vi theo <strong>Khung Đèn giao thông (Xanh - Vàng - Đỏ)</strong> (CLO5).",
            "Áp dụng được <strong>Checklist 3 câu hỏi an toàn dữ liệu</strong> và kỹ thuật <strong>Khử định danh (Data Anonymization & Schema-only prompting)</strong> đối với dữ liệu tài chính - ngân hàng - khách hàng (CLO5).",
            "Soạn thảo hoàn chỉnh <strong>Mảnh ghép 4 của Đề án cuối khóa</strong> (Ma trận kiểm soát rủi ro dữ liệu + Bản khai báo sử dụng AI chuẩn mực theo Thông tư 49/2026) (CLO5)."
        ],
        "story_hook": "Câu chuyện của Minh (Kỳ 9): Để có số liệu thực tế cho Đề án, một bạn trong nhóm Minh xin được file Excel 500 hồ sơ khách hàng vay vốn từ anh chị đi làm ở ngân hàng (có cả tên, số điện thoại, thu nhập) và định tải thẳng lên ChatGPT miễn phí để nhờ chạy thống kê! Chưa hết, bạn ấy còn bảo: 'Đừng ghi vào báo cáo là nhóm mình có dùng AI, kẻo thầy trừ điểm!'. Minh lập tức ngăn lại, mở nguyên văn Điều 10 Thông tư 49/2026/TT-BGDĐT và Luật Bảo vệ dữ liệu cá nhân 2025 cho cả nhóm xem: Giấu việc dùng AI chính là hành vi vi phạm liêm chính học thuật, còn tải dữ liệu khách hàng thật lên AI công cộng là vi phạm pháp luật bảo mật ngân hàng!",
        "warmup_questions": [
            "Theo bạn, giữa một sinh viên 'có dùng AI hỗ trợ tóm tắt và chỉnh văn nhưng cố tình giấu không khai báo' và một sinh viên 'khai báo rõ ràng từng bước đã dùng AI và cam kết đã tự kiểm chứng toàn bộ nguồn', ai mới là người vi phạm quy chế theo Thông tư 49/2026/TT-BGDĐT?",
            "Nếu một Giáo sư đầu ngành của ĐH Stanford (nhận thù lao 600 USD/giờ làm nhân chứng chuyên gia trước tòa) để lọt đúng 2 trích dẫn do GPT-4o bịa vào bản khai, theo bạn tòa án sẽ xử lý như thế nào?"
        ],
        "timeline": [
            ("Tiết 1 (00' - 50')", "<strong>Hậu quả thực tế (Vụ GS Hancock) & Hành lang Pháp lý Việt Nam (Thông tư 49/2026):</strong><br>• Chiếu và phân tích vụ GS. Jeff Hancock (ĐH Stanford) bị tòa Minnesota loại toàn bộ bản khai chuyên gia ngày 10/01/2025 vì 2 trích dẫn do GPT-4o bịa.<br>• Phân tích văn bản gốc <strong>Thông tư 49/2026/TT-BGDĐT</strong> (ban hành 30/6/2026, hiệu lực 15/8/2026), <strong>Điều 10</strong>: 6 nhóm hành vi vi phạm liêm chính học thuật (đặc biệt là Khoản 2 Điểm đ: <em>không công bố hoặc công bố không đầy đủ việc sử dụng AI khi có yêu cầu</em>).<br>• Liên hệ <strong>Luật AI 134/2025/QH15 (Điều 4)</strong>, <strong>Thông tư 05/2026</strong> và <strong>EU AI Act (Điều 50)</strong>.", "Đọc trực tiếp văn bản Điều 10 Thông tư 49/2026/TT-BGDĐT; thảo luận mối liên hệ giữa quy định pháp lý và hậu quả thực tế.", "Slide Buổi 9; Văn bản gốc Thông tư 49/2026/TT-BGDĐT"),
            ("Tiết 2 (50' - 100')", "<strong>Chuẩn Quốc tế (COPE, ICMJE), Đèn giao thông (Xanh-Vàng-Đỏ) & Mẫu Khai báo AI:</strong><br>• Bốn nguyên tắc chung của COPE, ICMJE, ALLEA, WAME, Elsevier: (1) AI không làm tác giả & không đưa chatbot vào danh mục References, (2) Công khai cách dùng, (3) Tác giả chịu trách nhiệm toàn bộ, (4) Bảo mật bản thảo khi phản biện.<br>• Thực hành phân loại theo <strong>Đèn giao thông (Xanh - Vàng - Đỏ)</strong>.<br>• Hướng dẫn viết <strong>Mẫu câu khai báo việc dùng AI</strong> chuẩn mực.", "Thảo luận phân vùng Xanh - Vàng - Đỏ cho các tác vụ học tập tại HUB; viết nháp câu khai báo AI cá nhân.", "Bảng Đèn giao thông & Mẫu khai báo AI"),
            ("Tiết 3 (100' - 150')", "<strong>An toàn & Bảo mật Dữ liệu Đặc thù Ngành Ngân hàng - Tài chính:</strong><br>• Phân tích 2 sự cố rò rỉ dữ liệu thật (Samsung 2023; lỗi hiển thị lịch sử ChatGPT 20/03/2023) và quy định về chuyển dữ liệu cá nhân xuyên biên giới theo <strong>Luật Bảo vệ dữ liệu cá nhân 2025 (91/2025/QH15)</strong>.<br>• Nguyên tắc vàng, Checklist 3 câu hỏi và kỹ thuật <strong>Khử định danh / Chỉ gửi Schema (cấu trúc cột)</strong> khi nhờ AI viết code phân tích dữ liệu.<br>• Trò chơi tranh biện cả lớp: Giơ thẻ phân loại 8 tình huống dữ liệu ngân hàng - học thuật.", "Tham gia tranh biện 8 tình huống bảo mật dữ liệu; thực hành khử định danh một bảng dữ liệu mẫu trước khi đưa vào AI.", "Bộ 8 tình huống phân loại dữ liệu"),
            ("Tiết 4 (150' - 200')", "<strong>Studio Đề án (Hoàn thành Mảnh ghép 4) & Khóa chốt LMS:</strong><br>• Các nhóm hoàn thiện <strong>Mảnh ghép 4</strong>: Bảng kiểm soát rủi ro dữ liệu theo Đèn giao thông + Bản Khai báo Sử dụng AI đầy đủ cho toàn bộ Đề án.<br>• Hoàn thành phản tư 4F và Quiz Buổi 9.", "Soạn thảo xong Mảnh ghép 4 và ghép nối trọn bộ 4 Mảnh ghép của Đề án nhóm; làm Quiz Buổi 9 trên LMS Hub.", "LMS Hub (Quiz 9, Journal 9)")
        ],
        "discussion_questions": [
            "Tại sao ICMJE lại khuyến nghị KHÔNG đưa các Chatbot tổng quát vào Danh mục tài liệu tham khảo (References) cuối bài như một bài báo khoa học, mà phải khai báo ở mục Phương pháp hoặc Lời cảm ơn?",
            "Nếu bạn là sinh viên thực tập tại ngân hàng và cần dùng AI để viết công thức Excel / code Python xử lý bảng sao kê của 10.000 khách hàng, bạn sẽ làm thế nào để không một dòng dữ liệu thật nào của khách hàng rời khỏi máy tính nội bộ mà vẫn lấy được đoạn code chuẩn từ AI?",
            "Tại sao nguyên tắc 'Không tải bản thảo chưa công bố của người khác lên AI công cộng khi phản biện' (Nguyên tắc 4 của COPE) lại cực kỳ quan trọng khi các bạn thực hiện Kiểm toán chéo (Peer Audit) ở Buổi 10?"
        ],
        "homework": """
      <div class="homework-box">
        <h3>1. Nhiệm vụ Cá nhân trên LMS Hub:</h3>
        <ul>
          <li>Hoàn thành đọc và làm Vòng Test 3 cấp độ của <strong>Chương 9 trên eBook SCQA</strong>.</li>
          <li>Hoàn thành <strong>Quiz Buổi 9</strong> (Active Recall 5 lượt) và nộp Feedback tải tài liệu buổi học.</li>
          <li>Viết <strong>Nhật ký học tập (Atomic Note số 9 theo khung 4F)</strong>: Ghi lại bộ quy tắc Đạo đức & Bảo mật dữ liệu của riêng bạn.</li>
        </ul>
        <h3>2. Nhiệm vụ Nhóm Đề án cuối khóa (Đóng gói trọn bộ Hồ sơ 4 Mảnh ghép cho Phiên Kiểm toán Buổi 10):</h3>
        <ul>
          <li>Ghép nối hoàn chỉnh <strong>Bộ Hồ sơ Đề án Ứng dụng AI (đủ 4 Mảnh ghép + File thư viện Zotero + Link/Hồ sơ bộ Harness + Danh sách Atomic Notes cá nhân + Bản khai báo AI theo Thông tư 49/2026)</strong> để nộp ngay đầu Tiết 1 Buổi 10 cho Hội đồng Kiểm toán chéo!</li>
        </ul>
      </div>
        """,
        "review_mc": [
            ("Văn bản pháp quy nào của Bộ GD&ĐT (hiệu lực từ 15/8/2026) quy định việc không công bố đầy đủ việc dùng AI khi có yêu cầu là vi phạm liêm chính học thuật?", "Thông tư 49/2026/TT-BGDĐT (Điều 10, Khoản 2, Điểm đ)."),
            ("Bốn nguyên tắc chung của COPE, ICMJE, WAME và Elsevier về AI trong xuất bản khoa học là gì?", "(1) AI không làm tác giả, (2) Công bố minh bạch việc dùng AI, (3) Tác giả con người chịu trách nhiệm toàn bộ nội dung, (4) Không tải bản thảo của người khác lên AI công cộng khi phản biện."),
            ("Ba chỗ trống bắt buộc phải điền cụ thể trong Mẫu câu khai báo việc dùng AI là gì?", "Công cụ nào (kèm phiên bản) - Vào thời gian nào (tháng/năm) - Để làm mục đích/công việc cụ thể gì (kèm cam kết đã tự kiểm chứng và chịu trách nhiệm hoàn toàn).")
        ],
        "teacher_notes": [
            "Chiếu rõ ảnh trang văn bản Điều 10 Thông tư 49/2026/TT-BGDĐT và câu chuyện GS Jeff Hancock để sinh viên thấy tính nghiêm cẩn pháp lý chứ không chỉ là lời khuyên đạo đức suông.",
            "Nhắc các nhóm kiểm tra kỹ quy tắc Điểm liệt Liêm chính trước khi nộp hồ sơ vào Buổi 10."
        ]
    },
    {
        "id": 10,
        "module": "MODULE 4: AN TOÀN, ĐẠO ĐỨC, PHÁP LÝ & ĐỒ ÁN TỔNG HỢP",
        "title": "Buổi 10: Project Clinic & Studio Kiểm toán chéo (Peer Audit Studio)",
        "subtitle": "Nộp trọn bộ Hồ sơ Đề án 4 mảnh ghép và thực hiện 3 vòng Kiểm toán Học thuật chéo giữa các nhóm (Stress-test Harness + Tomaca + Checklist 5 bước)",
        "clo": "CLO1, CLO2, CLO3, CLO4, CLO5",
        "duration": "4 tiết (200 phút)",
        "objectives": [
            "Hoàn thiện và nộp đúng hạn trọn bộ <strong>Hồ sơ Đề án Ứng dụng AI (4 Mảnh ghép lũy tiến)</strong> đáp ứng toàn bộ tiêu chuẩn của Rubric đánh giá cuối khóa (CLO1 -> CLO5).",
            "Đóng vai trò <strong>'Kiểm toán viên Học thuật' (Academic Auditor / Red Team)</strong> để thực hiện 3 vòng kiểm toán kỹ thuật độc lập đối với Đề án của nhóm đối tác (CLO2, CLO4, CLO5).",
            "Thực hiện <strong>Stress-test 3 kịch bản</strong> trên bộ Harness của nhóm bạn và kiểm chứng trực tiếp danh mục tài liệu tham khảo của nhóm bạn bằng <strong>Tomaca + Checklist 5 bước trên bản PDF gốc</strong> (CLO2, CLO4).",
            "Lập được <strong>Biên bản Kiểm toán Học thuật (Peer Audit Report)</strong> sắc bén, dựa trên bằng chứng xác thực và văn minh (chiếm 15% tổng điểm cuối khóa của nhóm kiểm toán) (CLO4, CLO5)."
        ],
        "story_hook": "Câu chuyện của Minh (Kỳ 10): Bước vào Buổi 10, nhóm của Minh được phân công làm Hội đồng Kiểm toán cho Đề án của Nhóm 4. Thay vì nhận xét qua loa cho xong, nhóm Minh chạy thử 1 tình huống thiếu dữ liệu trên bộ Harness của Nhóm 4 và phát hiện FALLBACK chưa hoạt động; tiếp đó, khi mở file PDF gốc của trích dẫn số 6 trong bài Nhóm 4 để đối chiếu Bước 4, Minh phát hiện một con số bị gõ lệch từ 14.5% thành 41.5%! Nhóm 4 vô cùng biết ơn vì nhờ Biên bản Kiểm toán của nhóm Minh mà họ kịp sửa sạch lỗi trước ngày Bảo vệ chính thức, còn nhóm Minh nhận trọn vẹn 15/15 điểm năng lực Kiểm toán!",
        "warmup_questions": [
            "Tại sao một người kiểm toán chỉ ra đúng lỗi sai kèm bằng chứng trang gốc ở Buổi 10 lại là 'người bạn tốt nhất' của nhóm bạn trước ngày bảo vệ Buổi 11?",
            "Nếu điểm số của chính nhóm bạn (15% tổng điểm môn học) được chấm dựa trên độ sắc bén và chính xác của Biên bản Kiểm toán mà nhóm bạn lập ra khi soi bài nhóm khác, bạn sẽ kiểm tra những gì đầu tiên?"
        ],
        "timeline": [
            ("Tiết 1 (00' - 50')", "<strong>Khóa cổng nộp Hồ sơ Đề án 4 Mảnh ghép & Phân cặp Kiểm toán chéo:</strong><br>• Các nhóm nộp trọn bộ Hồ sơ Đề án (4 mảnh ghép + file Zotero + link Harness + danh sách Atomic Notes) lên hệ thống.<br>• Giảng viên phổ biến quy chế Kiểm toán chéo 3 vòng, phát biểu mẫu <em>Peer Audit Rubric</em> và phân cặp các nhóm kiểm toán.", "Nộp Hồ sơ Đề án chính thức; nhận hồ sơ của nhóm đối tác được phân công kiểm toán và phân chia nhiệm vụ 3 vòng trong nhóm.", "LMS Hub; Biểu mẫu Peer Audit Rubric"),
            ("Tiết 2 (50' - 100')", "<strong>Kiểm toán Vòng 1: Stress-test Bộ Harness & Thẩm định Second Brain (Mảnh ghép 1 & 2):</strong><br>• Nhóm Kiểm toán chạy thử 3 kịch bản (Chạy xuôi - Thiếu thông tin test FALLBACK - Giục vượt rào test GATE) trên bộ Harness của nhóm bạn.<br>• Kiểm tra cấu trúc PARA, kho RAG và tính nguyên bản của các Atomic Notes cá nhân.", "Thực hiện Stress-test trực tiếp trên bộ Harness của nhóm đối tác; chụp màn hình bằng chứng kết quả test để đưa vào Biên bản Kiểm toán.", "Claude Project / Gemini Gem của nhóm đối tác"),
            ("Tiết 3 (100' - 150')", "<strong>Kiểm toán Vòng 2 & Vòng 3: Kiểm toán Nguồn trích dẫn (Tomaca + 5 bước) & Đạo đức AI (Mảnh ghép 3 & 4):</strong><br>• Quét toàn bộ danh mục tài liệu của nhóm bạn trên <strong>Tomaca</strong>.<br>• Bốc ngẫu nhiên <strong>03 trích dẫn trọng yếu</strong>, mở file PDF gốc kiểm tra đủ <strong>Checklist 5 bước</strong> và <strong>Soi 3 phút</strong>.<br>• Kiểm tra việc khử định danh dữ liệu và Bản khai báo AI theo Điều 10 Thông tư 49/2026.", "Quét Tomaca, mở 3 bài báo PDF gốc đối chiếu từng dòng luận điểm và bảng số liệu; rà soát Bản khai báo AI của nhóm đối tác.", "Tomaca, Google Scholar, doi.org, Zotero"),
            ("Tiết 4 (150' - 200')", "<strong>Bàn giao Biên bản Kiểm toán chéo, Vá lỗi Đề án & Khóa chốt LMS:</strong><br>• Các nhóm Kiểm toán hoàn thiện và nộp <strong>Biên bản Kiểm toán Học thuật (Peer Audit Report)</strong> lên LMS Hub.<br>• Các nhóm nhận lại phản hồi kiểm toán, tiến hành vá lỗi nóng (hotfix) và hoàn thiện Slide bảo vệ cho Buổi 11.", "Nộp Biên bản Kiểm toán chéo lên LMS; thảo luận nhanh với nhóm đối tác để ghi nhận các điểm cần nâng cấp cho buổi bảo vệ; làm Quiz Buổi 10.", "LMS Hub (Quiz 10, Journal 10, Peer Audit Report)")
        ],
        "discussion_questions": [
            "Qua quá trình trực tiếp đi kiểm toán bộ Harness và danh mục trích dẫn của nhóm bạn, lỗi sai nào bạn thấy các nhóm dễ mắc phải nhất?",
            "Nếu Tomaca báo xanh (verified-doi) cho toàn bộ danh mục tài liệu của nhóm bạn, nhưng khi mở PDF gốc ở Bước 3 bạn phát hiện đoạn văn trong bài gốc nói về 'ngân hàng trung ương' chứ không phải 'ngân hàng thương mại' như nhóm bạn viết, bạn sẽ ghi nhận và chấm điểm thế nào trong Biên bản Kiểm toán?",
            "Làm thế nào để trình bày một phát hiện lỗi sai nghiêm trọng của nhóm bạn với thái độ tôn trọng, khách quan và giúp nhóm bạn tâm phục khẩu phục?"
        ],
        "homework": """
      <div class="homework-box">
        <h3>1. Nhiệm vụ Cá nhân trên LMS Hub:</h3>
        <ul>
          <li>Hoàn thành đọc và làm Vòng Test 3 cấp độ của <strong>Chương 10 trên eBook SCQA</strong>.</li>
          <li>Hoàn thành <strong>Quiz Buổi 10</strong> (Active Recall 5 lượt) và viết <strong>Nhật ký học tập (Atomic Note số 10 theo khung 4F)</strong>.</li>
          <li>Rà soát lại toàn bộ kho <strong>Atomic Notes cá nhân</strong> của mình để sẵn sàng cho phần <strong>Vấn đáp chỉ định cá nhân (30% điểm)</strong> ở Buổi 11.</li>
        </ul>
        <h3>2. Nhiệm vụ Nhóm Đề án cuối khóa (Sẵn sàng 100% cho Lễ Bảo vệ Buổi 11):</h3>
        <ul>
          <li>Khắc phục triệt để các điểm hạn chế đã được chỉ ra trong Biên bản Kiểm toán chéo của Buổi 10.</li>
          <li>Hoàn thiện bộ <strong>Slide Bảo vệ Đề án (8-10 phút trình bày)</strong> có kèm 1 slide tóm tắt <em>'Những điểm nhóm đã nâng cấp sau phiên Kiểm toán chéo'</em> và tập dượt thao tác Live Demo bộ Harness.</li>
        </ul>
      </div>
        """,
        "review_mc": [
            ("Ba vòng của quy trình Kiểm toán chéo (Peer Audit) tại Buổi 10 là gì?", "Vòng 1: Stress-test Bộ Harness & thẩm định Second Brain -> Vòng 2: Kiểm toán nguồn trích dẫn bằng Tomaca + Checklist 5 bước trên PDF gốc -> Vòng 3: Kiểm toán an toàn dữ liệu & Bản khai báo AI theo Thông tư 49/2026."),
            ("Trọng số điểm của phần Thuyết trình bảo vệ và Kiểm toán chéo trong tổng điểm cuối khóa là bao nhiêu?", "30% tổng điểm cuối khóa (15% trình bày & trả lời bảo vệ đề án nhóm mình + 15% chất lượng Biên bản Kiểm toán & phản biện nhóm bạn)."),
            ("Nguyên tắc bảo mật nào theo chuẩn COPE phải được giữ vững trong suốt quá trình Kiểm toán chéo?", "Không tự ý tải toàn bộ hồ sơ hoặc dữ liệu chưa công bố của nhóm bạn lên các công cụ AI công cộng bên ngoài khi chưa được phép.")
        ],
        "teacher_notes": [
            "Phân cặp kiểm toán chéo sao cho các nhóm có cùng lĩnh vực ngành nghề (ví dụ hai nhóm cùng làm về Ngân hàng hoặc hai nhóm cùng làm về Marketing) kiểm toán nhau để tăng chiều sâu chuyên môn.",
            "Giảng viên đọc nhanh các Biên bản Kiểm toán cuối Tiết 4 để nắm sẵn các điểm nóng cần hỏi xoáy trong buổi Bảo vệ ở Buổi 11."
        ]
    },
    {
        "id": 11,
        "module": "MODULE 4: AN TOÀN, ĐẠO ĐỨC, PHÁP LÝ & ĐỒ ÁN TỔNG HỢP",
        "title": "Buổi 11: Bảo vệ Đề án cuối khóa (Capstone Showcase), Phản biện & Tổng kết",
        "subtitle": "Hội đồng Bảo vệ Đề án, Tranh biện Kiểm toán chéo, Vấn đáp cá nhân trên Second Brain (Chấm 100% điểm cuối khóa) & Lễ Cam kết Người làm chủ AI",
        "clo": "CLO1, CLO2, CLO3, CLO4, CLO5",
        "duration": "4 tiết (200 phút)",
        "objectives": [
            "Trình bày và bảo vệ thuyết phục <strong>Đề án Ứng dụng AI cuối khóa</strong> thông qua cấu trúc Storyline SCQA và màn <strong>Live Demo bộ Harness</strong> ngay trước Hội đồng (CLO1, CLO2, CLO4).",
            "Tranh biện khoa học, cầu thị và dựa trên bằng chứng với <strong>Hội đồng Kiểm toán chéo</strong> về chất lượng nguồn trích dẫn Zotero, Ma trận tổng hợp và tuân thủ Thông tư 49/2026 (CLO4, CLO5).",
            "Chứng minh năng lực làm chủ cá nhân (30% điểm cá nhân) qua phần <strong>Vấn đáp chỉ định trực tiếp</strong> trên hệ thống Second Brain Atomic Notes, thao tác Soi 3 phút và kiểm chứng nguồn (CLO1 -> CLO5).",
            "Đúc kết trọn vẹn hành trình 44 tiết học qua <strong>Atomic Note phản tư tổng kết cuối khóa</strong> và xác lập bộ nguyên tắc sử dụng AI có trách nhiệm cho Khóa luận tốt nghiệp và sự nghiệp tương lai (CLO1 -> CLO5)."
        ],
        "story_hook": "Câu chuyện của Minh (Kỳ cuối - Kỳ 11): Đứng trên bục giảng của Buổi 11 tại Trường ĐH Ngân hàng TP.HCM, Minh không còn là cậu sinh viên năm 2 ấp úng vì bài tiểu luận chép từ ChatGPT của 11 tuần trước. Khi giảng viên chỉ định ngẫu nhiên Minh thao tác trực tiếp, Minh mở ngay mạng lưới Atomic Notes trong Second Brain, chạy Live Demo bộ Harness phân tích tín dụng dừng đúng ở cổng GATE 1, và mở Zotero chỉ rõ trang 12 của bài báo gốc đã kiểm chứng qua 5 bước. Minh nhận ra: tấm chứng chỉ hôm nay là kết quả tất yếu, nhưng phần thưởng lớn nhất chính là một Bộ Não Thứ Hai vững chãi và bản lĩnh của một người làm chủ công nghệ.",
        "warmup_questions": [
            "Nhìn lại bản thân bạn ở Buổi 1 và ngày hôm nay (Buổi 11), thói quen nào khi dùng AI bạn đã thay đổi triệt để nhất?",
            "Trong 20 phút đứng trước Hội đồng hôm nay, điều gì sẽ chứng minh rõ nhất rằng nhóm bạn là 'Chủ nhân' còn AI là 'Trợ lý'?"
        ],
        "timeline": [
            ("Tiết 1 & Tiết 2 (00' - 100')", "<strong>Hội đồng Bảo vệ Đề án Cuối khóa (Đợt 1 - Các cặp nhóm 1, 2, 3, 4):</strong><br>• Mỗi nhóm 20 phút theo cấu trúc 3 phần:<br>  1. <em>Trình bày & Live Demo Harness (8-10 phút)</em>.<br>  2. <em>Hội đồng Kiểm toán chéo công bố kết quả Audit & Chất vấn (5-6 phút)</em>.<br>  3. <em>Giảng viên vấn đáp chỉ định từng cá nhân trên Second Brain & Zotero (5-6 phút)</em>.<br>• Chấm điểm trực tiếp 3 cấu phần (40% Hồ sơ nhóm + 30% Cá nhân + 30% Thuyết trình & Kiểm toán chéo).", "Các nhóm trình bày, demo sống bộ Harness, chất vấn chéo và trả lời vấn đáp cá nhân; cả lớp lắng nghe và ghi nhận bài học từ đề án các ngành.", "Slide Bảo vệ; Bộ Harness; Thư viện Zotero; Rubric 100%"),
            ("Tiết 3 (100' - 150')", "<strong>Hội đồng Bảo vệ Đề án Cuối khóa (Đợt 2 - Các cặp nhóm còn lại):</strong><br>• Tiếp tục quy trình bảo vệ, phản biện kiểm toán chéo và vấn đáp cá nhân cho các nhóm còn lại.<br>• Giảng viên nhận xét tổng hợp chất lượng Đề án và công bố kết quả đánh giá sơ bộ của các nhóm.", "Hoàn tất toàn bộ các phiên bảo vệ và phản biện chéo; đối chiếu điểm số trên hệ thống LMS Hub.", "LMS Hub Gradebook"),
            ("Tiết 4 (150' - 200')", "<strong>Phản tư Tổng kết Hành trình 44 tiết & Lễ Cam kết Người làm chủ AI:</strong><br>• Sinh viên viết <strong>Atomic Note phản tư tổng kết cuối khóa</strong> và hoàn thành Quiz tổng kết Buổi 11 trên LMS.<br>• Giảng viên đúc kết 3 thông điệp mang về suốt đời:<br>  1. <em>Tư duy -> Kỹ năng -> Công cụ (Second Brain & Harness là bệ phóng)</em>.<br>  2. <em>Nguồn thật trước, AI sau - Chưa kiểm chứng (5 bước + Zotero), chưa vào bài</em>.<br>  3. <em>Dùng AI thì khai báo (Thông tư 49/2026) - AI là trợ lý, bạn là chủ</em>.", "Viết Atomic Note tổng kết khóa học & Cam kết danh dự trên LMS Hub; hoàn thành Quiz Buổi 11; chia sẻ cảm nhận cuối khóa.", "LMS Hub (Quiz 11, Final Journal)")
        ],
        "discussion_questions": [
            "Sau khi khóa học này kết thúc, làm thế nào để bạn duy trì thói quen viết Atomic Notes vào Second Brain mỗi tuần mà không bị bỏ cuộc giữa chừng?",
            "Nếu ngày mai bạn hướng dẫn một sinh viên khóa dưới cách dùng AI để làm nghiên cứu khoa học tại HUB, đâu là 3 điều quan trọng nhất bạn sẽ truyền lại cho em ấy?",
            "Bạn sẽ ứng dụng Bộ Harness và Kho RAG mà nhóm vừa xây dựng trong môn học này vào Khóa luận tốt nghiệp hoặc kỳ thực tập sắp tới tại ngân hàng/doanh nghiệp như thế nào?"
        ],
        "homework": """
      <div class="homework-box">
        <h3>Nhiệm vụ Khóa chốt Toàn khóa học (Để hoàn tất hồ sơ cấp Chứng chỉ):</h3>
        <ul>
          <li>Kiểm tra trên <strong>Bảng điểm & Tiến độ LMS Hub</strong> để chắc chắn bạn đã hoàn thành đủ >= 80% các bài Quiz Active Recall, Nhật ký học tập (Atomic Notes 4F) và Phản hồi buổi học.</li>
          <li>Hoàn thành <strong>Quiz Tổng kết Buổi 11</strong> và <strong>Atomic Note Phản tư cuối khóa</strong> ngay tại Tiết 4.</li>
          <li>Lưu trữ (Export) bản sao thư viện <strong>Zotero</strong>, bộ <strong>System Instructions của Harness</strong> và thư mục <strong>Second Brain</strong> của Đề án sang thư mục <code>Areas</code> hoặc <code>Archives</code> trong máy tính cá nhân để tiếp tục phát triển cho Khóa luận tốt nghiệp!</li>
        </ul>
      </div>
        """,
        "review_mc": [
            ("Ba cấu phần tạo nên 100% điểm đánh giá cuối khóa của môn học là gì?", "Cấu phần 1: Hồ sơ Đề án 4 mảnh ghép của nhóm (40%) + Cấu phần 2: Dấu ấn cá nhân Second Brain Atomic Notes & Vấn đáp chỉ định (30%) + Cấu phần 3: Thuyết trình bảo vệ & Kiểm toán chéo nhóm bạn (30%)."),
            ("Ba điều cốt lõi nhất sinh viên mang về từ quy trình nghiên cứu có AI đồng hành là gì?", "(1) Nguồn thật trước, AI sau; (2) Chưa kiểm chứng (5 bước + Zotero), chưa vào bài; (3) Dùng AI thì khai báo (Thông tư 49/2026) - Bạn chịu trách nhiệm toàn bộ nội dung."),
            ("Ý nghĩa sâu xa nhất của câu 'AI là trợ lý, bạn là chủ' là gì?", "Làm chủ không có nghĩa là không dùng AI, mà là biết rõ mình đang giao việc gì, điều phối bằng Harness thế nào, kiểm tra lại qua nguồn thật ra sao và luôn sẵn sàng đàng hoàng đứng tên chịu trách nhiệm dưới kết quả.")
        ],
        "teacher_notes": [
            "Trong phần Vấn đáp chỉ định (5-6 phút/nhóm), hãy ưu tiên đặt câu hỏi cho những thành viên ít nói nhất trong lúc thuyết trình để đánh giá công bằng Cấu phần 2 (30% điểm cá nhân).",
            "Khép lại tiết cuối cùng bằng sự lắng đọng và truyền cảm hứng theo đúng triết lý 'Dạy bằng TÂM - Dẫn lối bằng TRI THỨC'."
        ]
    }
]

html_template = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — ĐH Ngân hàng TP.HCM (HUB)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,400&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    :root {{
      --paper: #fdfaf6;
      --card: #ffffff;
      --ink: #1b1714;
      --ink-soft: #4a413a;
      --navy: #0f2942;
      --crimson: #8b2500;
      --gold: #b8893a;
      --border: #e0d7cb;
      --bg-soft: #f3ece2;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Source Serif 4', Georgia, serif;
      line-height: 1.75;
      color: var(--ink);
      background: var(--paper);
      padding: 36px 20px 72px;
    }}
    .container {{ max-width: 920px; margin: 0 auto; }}
    header {{
      border-bottom: 2px solid var(--border);
      padding-bottom: 20px;
      margin-bottom: 28px;
    }}
    .meta-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 12px;
      font-family: 'DM Mono', monospace;
      font-size: 0.8rem;
    }}
    .badge {{
      display: inline-block;
      padding: 4px 10px;
      border-radius: 4px;
      background: var(--bg-soft);
      color: var(--navy);
      font-weight: 600;
      border: 1px solid var(--border);
    }}
    .badge-crimson {{
      background: #fde8e8;
      color: var(--crimson);
      border-color: #f8b4b4;
    }}
    h1 {{
      font-family: 'Cormorant Garamond', Georgia, serif;
      font-size: 2.2rem;
      color: var(--navy);
      line-height: 1.25;
      margin-bottom: 8px;
    }}
    .subtitle {{
      font-size: 1.05rem;
      font-style: italic;
      color: var(--ink-soft);
    }}
    h2.section-title {{
      font-family: 'Cormorant Garamond', Georgia, serif;
      font-size: 1.55rem;
      color: var(--crimson);
      border-bottom: 2px solid var(--border);
      padding-bottom: 6px;
      margin-top: 36px;
      margin-bottom: 16px;
    }}
    h3 {{
      font-size: 1.12rem;
      color: var(--navy);
      margin-top: 16px;
      margin-bottom: 8px;
    }}
    p {{ margin-bottom: 12px; }}
    ul, ol {{ margin: 10px 0 16px 24px; }}
    li {{ margin-bottom: 8px; }}
    .card-box {{
      background: var(--card);
      border: 1px solid var(--border);
      border-left: 4px solid var(--navy);
      border-radius: 6px;
      padding: 18px 22px;
      margin: 16px 0;
      box-shadow: 0 2px 6px rgba(0,0,0,0.02);
    }}
    .scqa-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 12px;
      margin: 14px 0;
    }}
    .scqa-item {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 14px 18px;
    }}
    .scqa-label {{
      font-family: 'DM Mono', monospace;
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--crimson);
      font-weight: 700;
      display: block;
      margin-bottom: 4px;
    }}
    .timeline-table {{
      width: 100%;
      border-collapse: collapse;
      margin: 16px 0;
      background: var(--card);
      font-size: 0.95rem;
    }}
    .timeline-table th, .timeline-table td {{
      border: 1px solid var(--border);
      padding: 12px 14px;
      text-align: left;
      vertical-align: top;
    }}
    .timeline-table th {{
      background: var(--bg-soft);
      color: var(--navy);
      font-weight: 700;
    }}
    .homework-box {{
      background: #fffdf9;
      border: 2px solid var(--gold);
      border-radius: 8px;
      padding: 20px 24px;
      margin: 16px 0;
    }}
    code {{
      font-family: 'DM Mono', monospace;
      font-size: 0.88em;
      background: var(--bg-soft);
      padding: 2px 6px;
      border-radius: 4px;
    }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="meta-bar">
        <span class="badge badge-crimson">{module}</span>
        <span class="badge">Thời lượng: {duration}</span>
        <span class="badge">Chuẩn đầu ra: {clo}</span>
        <span class="badge">GV: ThS. Phó Hải Đăng</span>
      </div>
      <h1>{title}</h1>
      <p class="subtitle">{subtitle}</p>
    </header>

    <!-- PHẦN I: BẮT BUỘC CHỨA TỪ KHÓA 'Mục tiêu' ĐỂ LMS EXTRACT CHO SV -->
    <h2 class="section-title">I. Mục tiêu buổi học</h2>
    <ul>
      {objectives_html}
    </ul>

    <!-- PHẦN II: BẮT BUỘC CHỨA TỪ KHÓA 'SCQA' ĐỂ LMS EXTRACT CHO SV -->
    <h2 class="section-title">II. Khung SCQA của buổi học</h2>
    <div class="scqa-grid">
      <div class="scqa-item">
        <span class="scqa-label">S — Situation (Bối cảnh quen thuộc)</span>
        <p>{scqa_s}</p>
      </div>
      <div class="scqa-item">
        <span class="scqa-label">C — Complication (Mâu thuẫn & Rủi ro thực tế)</span>
        <p>{scqa_c}</p>
      </div>
      <div class="scqa-item">
        <span class="scqa-label">Q — Question (Câu hỏi trọng tâm)</span>
        <p><strong>{scqa_q}</strong></p>
      </div>
      <div class="scqa-item">
        <span class="scqa-label">A — Answer (Định hướng giải quyết trong buổi học)</span>
        <p>{scqa_a}</p>
      </div>
    </div>

    <!-- PHẦN III & IV: KỊCH BẢN DẠY (LMS TỰ ẨN VỚI SV, HIỂN THỊ CHO GV) -->
    <h2 class="section-title">III. Story Spine & Khởi động từ Cái Biết của Sinh viên (20 phút)</h2>
    <div class="card-box">
      <h3>🎬 Story Spine — Hành trình của Minh tại HUB:</h3>
      <p>{story_hook}</p>
      <h3>❓ Câu hỏi kích hoạt tư duy (Warm-up):</h3>
      <ol>
        {warmup_html}
      </ol>
    </div>

    <h2 class="section-title">IV. Lộ trình buổi học & Kịch bản chi tiết theo Timeline (4 tiết = 200 phút)</h2>
    <table class="timeline-table">
      <thead>
        <tr>
          <th style="width: 16%">Thời lượng</th>
          <th style="width: 44%">Hoạt động Giảng viên & Nội dung cốt lõi</th>
          <th style="width: 26%">Hoạt động Sinh viên</th>
          <th style="width: 14%">Học liệu</th>
        </tr>
      </thead>
      <tbody>
        {timeline_html}
      </tbody>
    </table>

    <h2 class="section-title">V. Bảng câu hỏi thảo luận & Va chạm nhận thức</h2>
    <ol>
      {discussion_html}
    </ol>

    <!-- PHẦN VI: BẮT BUỘC CHỨA TỪ KHÓA 'Bài tập về nhà' ĐỂ LMS EXTRACT CHO SV -->
    <h2 class="section-title">VI. Bài tập về nhà & Cột mốc Đề án cuối khóa (BTVN)</h2>
    {homework_html}

    <h2 class="section-title">VII. Câu hỏi ôn tập củng cố cuối buổi (Active Recall)</h2>
    <ul>
      {review_html}
    </ul>

    <h2 class="section-title">VIII. Lưu ý sư phạm & Tình huống dự phòng cho Giảng viên</h2>
    <ul>
      {notes_html}
    </ul>
  </div>
</body>
</html>
"""

for item in lessons_data:
    s = item["id"]
    ch_path = os.path.join(CONTENT_DIR, "ebook", f"chapter-{s}.json")
    with open(ch_path, "r", encoding="utf-8") as f:
        ch = json.load(f)
    
    obj_html = "\n      ".join([f"<li>{o}</li>" for o in item["objectives"]])
    warm_html = "\n        ".join([f"<li>{w}</li>" for w in item["warmup_questions"]])
    disc_html = "\n      ".join([f"<li>{d}</li>" for d in item["discussion_questions"]])
    
    tl_rows = []
    for t_time, t_gv, t_sv, t_mat in item["timeline"]:
        tl_rows.append(f"<tr><td><strong>{t_time}</strong></td><td>{t_gv}</td><td>{t_sv}</td><td>{t_mat}</td></tr>")
    tl_html = "\n        ".join(tl_rows)
    
    rev_html = "\n      ".join([f"<li><strong>Hỏi:</strong> {q}<br><em>Đáp:</em> {a}</li>" for q, a in item["review_mc"]])
    notes_html = "\n      ".join([f"<li>{n}</li>" for n in item["teacher_notes"]])
    
    rendered = html_template.format(
        title=item["title"],
        subtitle=item["subtitle"],
        module=item["module"],
        duration=item["duration"],
        clo=item["clo"],
        objectives_html=obj_html,
        scqa_s=ch["scqa"]["situation"],
        scqa_c=ch["scqa"]["complication"],
        scqa_q=ch["scqa"]["question"],
        scqa_a=ch["scqa"]["answer"],
        story_hook=item["story_hook"],
        warmup_html=warm_html,
        timeline_html=tl_html,
        discussion_html=disc_html,
        homework_html=item["homework"],
        review_html=rev_html,
        notes_html=notes_html
    )
    
    out_file = os.path.join(CONTENT_DIR, "lessons", f"Buoi_{s:02d}.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(rendered)

print("Generated all 11 lesson HTML files (Buoi_01.html .. Buoi_11.html) successfully.")
