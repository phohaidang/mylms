# -*- coding: utf-8 -*-
import os
import json

CONTENT_DIR = r"d:\PARA\Projects\second-brain\05-Projects\lms-hub\courses\ky-nang-ai-hub\content"

# Build session-1.json .. session-11.json and bank.json
# Each session quiz has 10 MC questions (extracting the 10 MC questions from chapter-N.json + adding detailed explanations for 5-attempt unlock!)

explanations_map = {
    # Session 1
    "L1-c1-q1": "Mô hình ngôn ngữ lớn (LLM) hoạt động bằng cách tính toán phân phối xác suất để dự đoán từ (token) tiếp theo hợp lý nhất dựa trên ngữ cảnh đứng trước, chứ không tra cứu cơ sở dữ liệu sự thật.",
    "L1-c1-q2": "Theo nghiên cứu của Topaz và cộng sự trên The Lancet (5/2026) kiểm tra 2.5 triệu bài trên PubMed, tỷ lệ bài dính trích dẫn bịa tăng từ 1/2.828 (2023) lên 1/458 (2025) và đạt 1/277 trong 7 tuần đầu năm 2026.",
    "L1-c1-q3": "Ảo tưởng trôi chảy (Fluency Illusion) xảy ra khi văn bản AI tạo ra quá mượt mà khiến người đọc tưởng mình đã hiểu sâu, nhưng thực chất não bộ chưa trải qua ma sát nhận thức nên sẽ quên rất nhanh.",
    "L1-c1-q4": "Ba động từ định vị vị thế làm chủ là: AI đề xuất (Propose) - Bạn quyết định (Decide) - Bạn chịu trách nhiệm (Accountable).",
    "L2-c1-q1": "Do cơ chế đoán chữ ưu tiên sự hợp lý về mặt ngôn ngữ và không có bước kiểm tra sự thật nội tại, AI dễ ghép các từ có xác suất đi cùng nhau cao thành thông tin bịa (Hallucination) với giọng rất tự tin.",
    "L2-c1-q2": "Phép thử vàng trước khi giao việc cho AI: 'Nếu AI làm sai ở bước này, mình có đủ kiến thức và công cụ để phát hiện ra không?' Nếu không phát hiện được thì tuyệt đối không giao.",
    "L2-c1-q3": "Các công cụ RAG như Gemini Notebook (NotebookLM) chỉ trả lời dựa trên nguồn tài liệu người dùng tải lên và có trích dẫn trỏ về đúng đoạn văn gốc.",
    "L2-c1-q4": "Tự lập dàn ý trước rồi dùng AI đóng vai người phản biện giúp tạo ra ma sát nhận thức có lợi, tránh lệ thuộc nhận thức (Cognitive Offloading).",
    "L3-c1-q1": "Chatbot tổng quát không phải là kho tài liệu học thuật; dùng nó để xin danh mục tài liệu tham khảo và DOI sẽ dẫn tới trích dẫn bịa dạng ghép xác.",
    "L3-c1-q2": "Việc thẩm định độ tin cậy của số liệu gốc và chốt kết luận học thuật đòi hỏi phán đoán chuyên môn và trách nhiệm cá nhân nên con người bắt buộc phải tự nắm giữ.",
    # Session 2
    "L1-c2-q1": "Trong khung CRISP, chữ S (Specifics) quy định các yêu cầu và ràng buộc cụ thể về định dạng, độ dài, văn phong và thuật ngữ của đầu ra.",
    "L1-c2-q2": "Few-shot prompting là kỹ thuật cung cấp từ 2 đến 3 ví dụ mẫu chuẩn mực để AI học theo cấu trúc và giọng điệu mong muốn.",
    "L1-c2-q3": "Câu khóa 'Chỗ nào tài liệu không nói, ghi rõ không nêu trong bài, tuyệt đối không suy đoán' là chốt chặn sống còn ngăn AI tự bịa thông tin lấp vào chỗ trống.",
    "L1-c2-q4": "Context Engineering là nghệ thuật tuyển chọn, làm sạch và cấu trúc hóa toàn bộ gói tài liệu nguồn, ví dụ mẫu và quy tắc biên nạp vào cửa sổ ngữ cảnh cho AI.",
    "L2-c2-q1": "Chain-of-Thought (Suy luận từng bước) buộc AI phải trình bày các bước lập luận trung gian, giúp giảm thiểu sai sót trong các bài toán logic và phân tích định lượng.",
    "L2-c2-q2": "Khi hội thoại quá dài và lộn xộn, các chỉ thị ban đầu bị đẩy ra xa hoặc bị pha loãng trong Context Window (Context Rot), làm giảm độ nhất quán của kết quả.",
    "L2-c2-q3": "Iterative Refinement (Tinh chỉnh đa vòng) là giữ lại phần đã đúng và chỉ yêu cầu điều chỉnh từng tiêu chí cụ thể (độ dài, giọng văn) qua các lượt kế tiếp.",
    "L2-c2-q4": "Prompt là giao diện của tư duy: chỉ khi người học hiểu rõ cấu trúc bài toán và tiêu chí đánh giá thì mới viết được một câu lệnh CRISP sắc bén.",
    "L3-c2-q1": "Một câu lệnh đọc tài liệu chuẩn mực phải hội tụ đủ 5 yếu tố CRISP, đính kèm file gốc và có chốt chặn yêu cầu ghi số trang, không suy đoán.",
    "L3-c2-q2": "Gói Context tốt nhất gồm bảng thang đo gốc đã kiểm chứng, mô tả mẫu khảo sát, ví dụ mẫu Few-shot và ràng buộc giữ nguyên bản chất biến quan sát.",
    # Session 3
    "L1-c3-q1": "Harness là bộ khung điều phối và kiềm tỏa AI gồm System Instructions (quy tắc cố định), quy trình nhiều bước, cổng xác nhận (GATE) và xử lý ngoại lệ (FALLBACK).",
    "L1-c3-q2": "Cổng dừng xác nhận GATE (🔒) buộc AI phải dừng lại sau một bước quan trọng, xuất kết quả trung gian và chờ con người duyệt mới được chuyển sang bước tiếp theo.",
    "L1-c3-q3": "Cơ chế FALLBACK (❓) buộc AI khi thiếu dữ liệu hoặc không tìm thấy căn cứ trong bài phải ghi rõ 'Chưa đủ căn cứ / Thiếu dữ liệu' và hỏi lại người dùng thay vì tự đoán.",
    "L1-c3-q4": "Bốn kỹ thuật học tập hiệu quả gồm: Truy hồi chủ động (Active Recall), Lặp lại ngắt quãng (Spaced Repetition), Xáo trộn (Interleaving) và Tự mày mò trước (Productive Struggle).",
    "L2-c3-q1": "Đóng gói vào Project/Gem giúp giữ cố định System Instructions và Knowledge Base; mỗi phiên chat mới đều tuân thủ đúng quy trình mà không bị lẫn dữ liệu của ca việc trước.",
    "L2-c3-q2": "Khi bị giục vượt rào, một bộ Harness đạt chuẩn phải từ chối bỏ qua cổng GATE và nhắc người dùng xác nhận dữ liệu bước hiện tại trước khi đi tiếp.",
    "L2-c3-q3": "Socratic Harness phải cấm AI giải bài hộ ngay lập tức, buộc AI đặt câu hỏi gợi mở và chấm từng bước lập luận do chính sinh viên tự làm.",
    "L2-c3-q4": "Con người phải vẽ sơ đồ quy trình nghiệp vụ ra giấy trước để xác định rõ các bước, điểm dừng GATE và điểm thiếu dữ liệu FALLBACK ngoài đời thực rồi mới số hóa cho AI.",
    "L3-c3-q1": "Đặt GATE ngay sau bước trích xuất và tính toán chỉ số tài chính giúp người học đối chiếu số liệu khớp với báo cáo gốc trước khi AI viết phần so sánh và nhận xét.",
    "L3-c3-q2": "Bộ 3 kịch bản stress-test một bộ Harness gồm: (1) chạy xuôi đủ dữ liệu, (2) cố tình bỏ thiếu dữ liệu để test FALLBACK, và (3) cố tình giục vượt rào để test GATE.",
    # Session 4
    "L1-c4-q1": "PARA gồm 4 nhóm theo mức độ hành động: Projects (Dự án có hạn chót) - Areas (Lĩnh vực trách nhiệm dài hạn) - Resources (Tài nguyên tham khảo) - Archives (Lưu trữ lạnh).",
    "L1-c4-q2": "Luồng vận hành CODE gồm 4 bước: Capture (Thu nạp có chọn lọc) -> Organize (Tổ chức theo PARA) -> Distill (Tinh chế tìm lõi) -> Express (Diễn đạt thành sản phẩm).",
    "L1-c4-q3": "Atomic Note (Ghi chú nguyên tử) là đơn vị tri thức đóng gói duy nhất 1 ý tưởng cốt lõi, diễn đạt bằng ngôn từ riêng của người học, có nguồn gốc và liên kết hai chiều.",
    "L1-c4-q4": "Khung phản tư 4F gồm: Fact (Sự kiện khách quan) - Feelings (Cảm xúc/Điểm chạm) - Findings (Bài học/Quy luật đúc kết) - Future (Định hướng áp dụng tương lai).",
    "L2-c4-q1": "Copy-paste nguyên văn output của AI không qua xử lý của não bộ chỉ tạo ra rác thông tin (digital hoarding), không tạo ra sự hiểu biết nội tại hay khả năng lắp ghép luận điểm.",
    "L2-c4-q2": "Tiêu đề chuẩn của một Atomic Note phải là một câu khẳng định tóm trọn luận điểm cốt lõi (Declarative Title) giúp nhìn vào hiểu ngay ý chính để lắp ghép khi viết báo cáo.",
    "L2-c4-q3": "Đề án cuối khóa có hạn chót cụ thể nên thuộc Projects; còn kiến thức chuyên ngành theo đuổi suốt nhiều năm thuộc Areas.",
    "L2-c4-q4": "Các Atomic Notes đã được bạn tinh chế trong Second Brain chính là nguồn Context độc bản, tinh khiết nhất để nạp ngược vào AI khi thiết kế Harness hoặc viết báo cáo.",
    "L3-c4-q1": "Cấu phần 2 (30% điểm cá nhân) yêu cầu mỗi thành viên tự đóng góp tối thiểu 6 Atomic Notes viết bằng ngôn từ riêng kèm phản tư 4F trên LMS để chống ăn theo nhóm.",
    "L3-c4-q2": "Phát hiện về sự đánh đổi giữa độ chính xác và khả năng giải thích của mô hình AI thuộc phần Findings (Bài học cốt lõi) và cần được lưu thành một Atomic Note độc lập.",
    # Session 5
    "L1-c5-q1": "Công cụ RAG như Gemini Notebook chỉ trả lời dựa trên tập tài liệu do người dùng nạp vào và luôn đính kèm trích dẫn trỏ về đúng đoạn văn gốc.",
    "L1-c5-q2": "Nếu Chatbot LLM thuần túy là 'chuyên gia biết rộng nhưng đôi khi hay bịa', thì hệ thống RAG đóng vai trò là 'người thư ký trung thành' chỉ đọc tài liệu bạn giao.",
    "L1-c5-q3": "Truy vấn chéo đa tài liệu trên RAG là nạp nhiều bài báo thật cùng Atomic Notes vào Notebook rồi yêu cầu đối chiếu điểm giống/khác nhau kèm số trang trích dẫn.",
    "L1-c5-q4": "Grounded Garbage (Rác có trích dẫn) cảnh báo rằng nếu bạn nạp tài liệu sai lệch hoặc từ tạp chí săn mồi vào RAG, hệ thống sẽ trích dẫn rất chính xác cái thông tin sai đó.",
    "L2-c5-q1": "Nạp cả Atomic Notes cá nhân vào cùng các bài báo PDF giúp RAG kết nối được bằng chứng từ tài liệu gốc với chính cấu trúc lập luận và góc nhìn riêng của bạn.",
    "L2-c5-q2": "Ngay cả khi RAG có số trích dẫn [1], [2], người học vẫn phải bấm vào con số đó để đọc đoạn văn gốc được tô sáng nhằm chắc chắn AI không ghép lệch ngữ cảnh.",
    "L2-c5-q3": "Khi cần độ chính xác tuyệt đối trên các văn bản pháp quy (như Thông tư 49/2026) và các bài báo khoa học PDF, bắt buộc phải ưu tiên dùng kiến trúc RAG.",
    "L2-c5-q4": "Study Guide và Audio Overview trong Gemini Notebook giúp chuyển hóa tài liệu chuẩn thành câu hỏi ôn tập và hội thoại âm thanh để rèn luyện Active Recall.",
    "L3-c5-q1": "Mảnh ghép 2 của Đề án đòi hỏi nhóm thiết lập cấu trúc PARA, xây kho RAG chung từ tài liệu thật + Atomic Notes cá nhân và thực hiện truy vấn đối chiếu đa nguồn.",
    "L3-c5-q2": "Khi kho RAG báo tài liệu không đề cập, đó là tín hiệu chính xác giúp nhóm biết mình đang thiếu nguồn ở khía cạnh đó để đi tìm bổ sung từ Semantic Scholar/Elicit.",
    # Session 6
    "L1-c6-q1": "Trong quy trình NCKH 4 bước (Tìm - Đọc - Tổng hợp - Viết), hoạt động Kiểm chứng đi xuyên suốt cả 4 bước chứ không phải đợi đến cuối mới kiểm.",
    "L1-c6-q2": "Đồng hồ đo Consensus Meter chỉ phù hợp với các câu hỏi Yes/No dựa trên bằng chứng thực nghiệm.",
    "L1-c6-q3": "Ba thao tác 'Soi bản tóm tắt trong 3 phút' gồm: (1) Đối chiếu số liệu với bảng/hình gốc, (2) Truy chỗ AI tự thêm hoặc thiếu bối cảnh, và (3) Hỏi ngược về hạn chế.",
    "L1-c6-q4": "Trong thực nghiệm với bài báo Hemani (2026), AI đã tự suy diễn thêm thuật ngữ 'Pearson's R' vào hàng Phương pháp dù chữ 'Pearson' xuất hiện 0 lần trong bài gốc.",
    "L2-c6-q1": "Số liệu trong bản tóm tắt khớp với bài báo gốc chỉ chứng minh bản tóm tắt trung thực với văn bản đó, chưa chứng minh con số của bài báo đó đáng tin về mặt khoa học.",
    "L2-c6-q2": "Trong bài Hemani (2026), 150-200 ở tr.3 là cỡ mẫu dự kiến còn 192 ở tr.4 là mẫu thực tế; AI trích đúng số 192 nhưng thiếu bối cảnh, nên người đọc luôn phải hỏi xem trong bài còn chỗ nào nói khác không.",
    "L2-c6-q3": "Câu khóa 'không suy đoán' buộc AI phải ghi trung thực 'không nêu trong bài' khi bài báo gốc bỏ trống mục Limitations, thay vì tự bịa nội dung cho kín bảng.",
    "L2-c6-q4": "Chữ Yes trên Consensus Meter chỉ là câu hỏi đầu tiên; người nghiên cứu phải mở từng bài báo để đào sâu chuỗi câu hỏi: Xảy ra bao nhiêu %? Khi nào nặng hơn? Cơ chế và hệ quả là gì?",
    "L3-c6-q1": "Khi thấy AI tóm tắt một thuật ngữ chuyên môn cao (như GMM hay Pearson's R), phải mở ngay PDF gốc bấm Ctrl+F hoặc dò đúng số trang xem bài gốc có thực sự dùng phương pháp đó không.",
    "L3-c6-q2": "Phễu thu hẹp đi từ Chủ đề rộng -> Thêm đối tượng/bối cảnh ngành -> Câu hỏi nghiên cứu cụ thể -> Dùng công cụ có kho nguồn thật như Semantic Scholar và Elicit.",
    # Session 7
    "L1-c7-q1": "Theo nghiên cứu của Linardon và cs. (2025, JMIR Mental Health), có 19.9% (35/176) trích dẫn bịa hoàn toàn, và nếu gộp cả trích dẫn sai thông tin thư mục thì lên tới 56.3% (99/176).",
    "L1-c7-q2": "Linardon và cs. (2025) chứng minh tỷ lệ bịa trích dẫn tăng mạnh theo mức độ chủ đề ít được nghiên cứu (từ 6% lên 28%-29%, p = .001): AI bịa nhiều nhất ở chỗ nó biết ít nhất.",
    "L1-c7-q3": "Checklist 5 bước kiểm chứng từ rẻ đến tốn công: (1) Có thật không? -> (2) Thông tin thư mục khớp không? -> (3) Bài gốc nói đúng ý không? -> (4) Số liệu khớp bảng/hình không? -> (5) Còn hiệu lực trên Retraction Watch không?",
    "L1-c7-q4": "Nhãn `metadata-mismatch` trên Tomaca báo hiệu mã DOI có tồn tại nhưng thông tin tên tác giả, năm hoặc tiêu đề bị lệch, bắt buộc con người phải mở nguồn gốc kiểm tra.",
    "L2-c7-q1": "Bước 3 (mở bài gốc xem có nói đúng ý đó không) giúp chặn đứng loại lỗi rất phổ biến: bài báo và DOI có thật 100%, nhưng bị AI gán cho một luận điểm mà tác giả không hề nói.",
    "L2-c7-q2": "Khi AI ghép một mã DOI có thật của bài báo khác vào một tiêu đề bịa, công cụ tự động có thể báo `verified-doi` và bỏ lọt; vì vậy luôn phải giữ nguyên tắc 'Máy soát, người quyết'.",
    "L2-c7-q3": "Quy trình 'Nguồn vào Zotero trước, rồi mới vào bài' đảm bảo mọi tài liệu trong thư viện Zotero đều là bài bạn đã tự tay mở trang gốc kiểm chứng, triệt tiêu hoàn toàn trích dẫn bịa của AI.",
    "L2-c7-q4": "Đề tài mới hoặc bối cảnh đặc thù tại Việt Nam thường có ít dữ liệu trong tập huấn luyện của LLM, nên nếu nhờ Chatbot sinh trích dẫn ở vùng này thì nguy cơ bịa sẽ cao nhất.",
    "L3-c7-q1": "Mã DOI trỏ sang một bài báo khác không liên quan là dấu hiệu kinh điển của trích dẫn bịa dạng 'ghép xác'; hành vi này vi phạm Điểm liệt Liêm chính của môn học.",
    "L3-c7-q2": "Với các văn bản pháp quy hoặc báo cáo ngành trong nước không có mã DOI (`no-doi`), nhóm cần kiểm chứng thủ công tại cổng thông tin chính thức của cơ quan ban hành rồi lưu vào Zotero.",
    # Session 8
    "L1-c8-q1": "Summary là tóm tắt rời rạc từng bài; Synthesis là tổng hợp đa nguồn trên cùng các trục chủ đề/phương pháp để chỉ ra điểm đồng thuận, mâu thuẫn và khoảng trống nghiên cứu.",
    "L1-c8-q2": "Trong quy trình viết 4 nhịp, người học tự viết bản thảo từ Ma trận tổng hợp/Second Brain và chỉ chèn trích dẫn trực tiếp từ thư viện Zotero 8.",
    "L1-c8-q3": "'AI làm Draft, Người làm Final' nghĩa là AI chỉ hỗ trợ dựng bố cục nháp ban đầu, còn con người phải biên tập lại thông điệp, số liệu và đưa bằng chứng thực nghiệm thật vào bản cuối.",
    "L1-c8-q4": "Ở Nhịp 4 (biên tập văn phong), phải khóa chặt ràng buộc: chỉ sửa diễn đạt ngữ pháp cho học thuật hơn, tuyệt đối không đổi luận điểm, không thêm số liệu và giữ nguyên mã Zotero.",
    "L2-c8-q1": "Ma trận Tổng hợp (Synthesis Matrix) giúp nhìn xuyên suốt nhiều bài báo theo từng cột chủ đề, từ đó viết được đoạn văn đối thoại học thuật đa nguồn thay vì liệt kê từng bài.",
    "L2-c8-q2": "Phần Kết quả và Thảo luận là đóng góp trí tuệ cốt lõi dựa trên dữ liệu thực tế của nhóm; giao cho AI viết hộ sẽ dẫn tới nhận định bịa đặt và vi phạm Vùng Đỏ đạo đức học thuật.",
    "L2-c8-q3": "Slide do AI tạo tự động 100% thường mắc bệnh thiết kế công nghiệp chung chung (generic), chữ nghĩa sáo rỗng và thiếu hẳn các bằng chứng thực nghiệm thật của đề tài.",
    "L2-c8-q4": "Nhờ AI đóng vai 'Người phản biện khó tính' (Devil's Advocate) ở Nhịp 2 giúp phát hiện sớm các lỗ hổng lập luận ngay từ giai đoạn dàn ý.",
    "L3-c8-q1": "Một đoạn văn tổng hợp (Synthesis) chuẩn mực phải đặt các nguồn đồng thuận và trái chiều vào cùng một cấu trúc lập luận đối sánh có trích dẫn APA chuẩn xác.",
    "L3-c8-q2": "Slide bảo vệ Đề án cuối khóa bắt buộc phải chứa các bằng chứng sống: sơ đồ và demo bộ Harness, Ma trận tổng hợp, thư viện Zotero + báo cáo Tomaca/5 bước, Atomic Notes và Khai báo AI.",
    # Session 9
    "L1-c9-q1": "Theo Điều 10 (Khoản 2 Điểm đ) của Thông tư 49/2026/TT-BGDĐT (hiệu lực từ 15/8/2026), không công bố hoặc công bố không đầy đủ việc sử dụng AI khi có yêu cầu là hành vi vi phạm liêm chính học thuật.",
    "L1-c9-q2": "Theo COPE và ICMJE, công cụ AI không bao giờ được đứng tên làm tác giả vì AI không thể chịu trách nhiệm pháp lý và đạo đức về công trình khoa học.",
    "L1-c9-q3": "Để AI viết phần Kết quả/Thảo luận, dùng trích dẫn chưa kiểm chứng hoặc tải dữ liệu mật của ngân hàng lên AI công cộng đều thuộc Vùng Đỏ (Cấm tuyệt đối).",
    "L1-c9-q4": "Mẫu khai báo AI chuẩn mực phải nêu rõ: Tên công cụ + phiên bản, thời gian dùng, mục đích/phạm vi cụ thể, và lời cam kết đã tự kiểm chứng số liệu/trích dẫn, chịu trách nhiệm 100%.",
    "L2-c9-q1": "Theo Luật Bảo vệ dữ liệu cá nhân 2025 (91/2025/QH15), việc tải dữ liệu định danh khách hàng thật lên máy chủ AI nước ngoài đã cấu thành hành vi chuyển dữ liệu xuyên biên giới trái phép, độc lập với chế độ training.",
    "L2-c9-q2": "Nguyên tắc thứ 4 của COPE/ICMJE quy định phải bảo mật bản thảo khi phản biện: không được tự ý tải bài làm hoặc dữ liệu chưa công bố của người khác lên AI công cộng khi chưa được phép.",
    "L2-c9-q3": "ICMJE khuyến nghị không đưa Chatbot vào Danh mục tài liệu tham khảo vì hội thoại AI không phải nguồn khoa học cố định có thể kiểm chứng lại; việc dùng AI phải khai báo ở mục Phương pháp hoặc Lời cảm ơn.",
    "L2-c9-q4": "Mọi văn bản pháp lý và chuẩn mực quốc tế (Thông tư 49/2026, Luật AI 134/2025, EU AI Act, COPE) đều hội tụ về 2 nguyên tắc: Minh bạch (khai báo rõ) và Con người chịu trách nhiệm cuối cùng.",
    "L3-c9-q1": "Để bảo mật dữ liệu ngân hàng tuyệt đối, chỉ gửi cấu trúc tên cột (schema) hoặc dữ liệu giả lập để nhờ AI viết code Python/R, rồi mang code về máy mình tự chạy offline trên dữ liệu thật.",
    "L3-c9-q2": "Các công cụ AI Detector có tỷ lệ báo giả cao nên không được dùng làm bằng chứng kết tội duy nhất; phải đánh giá qua hồ sơ quá trình (Atomic Notes, Zotero, kiểm chứng 5 bước và vấn đáp trực tiếp).",
    # Session 10
    "L1-c10-q1": "Hồ sơ Đề án 4 mảnh ghép gồm: (1) Bộ Harness nghiệp vụ, (2) Hệ thống Second Brain & RAG, (3) Báo cáo nghiên cứu có Ma trận tổng hợp & Zotero đã kiểm chứng, (4) Hồ sơ An toàn dữ liệu & Khai báo AI theo Thông tư 49/2026.",
    "L1-c10-q2": "Hoạt động Thuyết trình, Phản biện và Kiểm toán chéo giữa các nhóm (Peer Audit) chiếm 30% tổng điểm cuối khóa (15% trình bày bảo vệ + 15% năng lực kiểm toán nhóm bạn).",
    "L1-c10-q3": "Ở Vòng 2 Kiểm toán chéo, ngoài việc quét Tomaca, Nhóm Kiểm toán bắt buộc phải chọn ít nhất 3 trích dẫn trọng yếu để mở PDF gốc kiểm tra đủ 5 bước (đặc biệt là Bước 3 và Bước 4).",
    "L1-c10-q4": "Theo Quy tắc Điểm liệt Liêm chính, nếu để lọt trích dẫn bịa hoặc không khai báo AI theo Thông tư 49/2026 vào báo cáo chính thức, nhóm bị trừ thẳng 50% điểm Cấu phần 1 và phải làm lại phần kiểm chứng.",
    "L2-c10-q1": "Kiểm toán bộ Harness phải dùng các tình huống biên (thiếu dữ liệu để thử FALLBACK, giục vượt rào để thử GATE) thì mới đánh giá được độ vững chắc thực sự của thiết kế.",
    "L2-c10-q2": "Một nhận xét kiểm toán chuẩn mực phải chỉ rõ bằng chứng cụ thể (trang mấy, trích dẫn nào, khớp hay lệch bao nhiêu % so với bảng gốc) kèm đề xuất chỉnh sửa mang tính xây dựng.",
    "L2-c10-q3": "Atomic Note thực chất luôn có tiêu đề khẳng định sắc gọn, nội dung viết bằng ngôn từ riêng gắn với đề án, có liên kết [[...]] và tác giả giải thích được ngay bản chất khi vấn đáp.",
    "L2-c10-q4": "Nhận được Biên bản Kiểm toán ở Buổi 10 là cơ hội vàng để nhóm vá lại lỗ hổng GATE/FALLBACK và đính chính số liệu/trích dẫn trước khi bước vào buổi Bảo vệ chính thức.",
    "L3-c10-q1": "Trích dẫn xuất hiện trong văn bản Word nhưng không nằm trong thư viện Zotero là dấu hiệu vi phạm quy tắc 'Nguồn vào Zotero trước, vào bài sau', cần yêu cầu kiểm chứng 5 bước hoặc loại bỏ ngay.",
    "L3-c10-q2": "Xóa sạch thông tin định danh khách hàng trước khi đưa vào Project và viết đầy đủ Bản khai báo AI theo Điều 10 Thông tư 49/2026 là thực hành đạt mức Xuất sắc ở Mảnh ghép 4.",
    # Session 11
    "L1-c11-q1": "Triết lý xuyên suốt của học phần là Tư duy -> Kỹ năng -> Công cụ: lấy tư duy làm gốc, rèn luyện kỹ năng hệ thống làm trụ cột, và sử dụng công cụ linh hoạt theo đúng tác vụ.",
    "L1-c11-q2": "Ba nguyên tắc vàng trong nghiên cứu có AI đồng hành: (1) Nguồn thật trước, AI sau; (2) Chưa kiểm chứng (5 bước + Zotero), chưa vào bài; (3) Dùng AI thì khai báo - Bạn chịu trách nhiệm toàn bộ.",
    "L1-c11-q3": "Phần Vấn đáp chỉ định cá nhân (30% điểm) đánh giá trực tiếp trên kho Atomic Notes cá nhân và thao tác live trên Harness/Zotero để đảm bảo mọi sinh viên đạt chứng chỉ đều có năng lực thực chất.",
    "L1-c11-q4": "Làm chủ AI không phải là né tránh dùng AI, mà là biết rõ mình giao việc gì, thiết kế được Harness điều phối, kiểm chứng được đầu ra và đàng hoàng đứng tên chịu trách nhiệm.",
    "L2-c11-q1": "Bốn trụ cột liên kết chặt chẽ: Kiểm chứng NCKH lọc nguồn thật -> Second Brain tinh chế thành Atomic Notes -> Atomic Notes làm Context sạch cho bộ Harness -> Đạo đức & Bảo mật giữ toàn bộ quy trình an toàn, hợp pháp.",
    "L2-c11-q2": "Khi Hội đồng chỉ ra hạn chế đúng, thái độ học thuật chuẩn mực là thẳng thắn ghi nhận dựa trên bằng chứng, giải thích nguyên nhân kỹ thuật và trình bày phương án khắc phục.",
    "L2-c11-q3": "Đổ lỗi 'Tại AI làm sai' là vi phạm trực tiếp nguyên tắc trách nhiệm của Thông tư 49/2026, Luật AI 134/2025 và COPE: người đặt tên mình lên bài phải chịu trách nhiệm 100% về mọi nội dung trong bài.",
    "L2-c11-q4": "Khi công cụ AI thế hệ mới ra đời, người có nền tảng Tư duy - Kỹ năng (Second Brain, Harness, Kiểm chứng 5 bước) sẽ lập tức làm chủ công cụ mới mà không bao giờ bị lỗi thời hay bị dắt mũi.",
    "L3-c11-q1": "Khi làm Khóa luận tốt nghiệp, hãy bắt đầu từ việc lập Project trong Second Brain, tìm nguồn thật trên Semantic Scholar/Elicit, soi 3 phút, kiểm chứng 5 bước vào Zotero, dựng kho RAG và Harness đồng hành kèm nhật ký khai báo AI.",
    "L3-c11-q2": "Khi đề xuất ứng dụng AI tại ngân hàng/doanh nghiệp, bước đầu tiên luôn là phân loại mức độ mật của dữ liệu, tuân thủ quy định An ninh thông tin/Luật Bảo vệ dữ liệu cá nhân và thiết kế Harness có cổng GATE trên dữ liệu giả lập."
}

bank = []

for s in range(1, 12):
    ch_path = os.path.join(CONTENT_DIR, "ebook", f"chapter-{s}.json")
    with open(ch_path, "r", encoding="utf-8") as f:
        ch = json.load(f)
    
    session_questions = []
    # Collect all MC questions from level_1, level_2, level_3 (4 + 4 + 2 = 10 questions)
    for lvl_idx, lvl_key in enumerate(["level_1", "level_2", "level_3"], start=1):
        qs = ch["tests"][lvl_key]["questions"]
        for q in qs:
            if q["type"] == "mc":
                q_id = f"aihub-s{s:02d}-{q['id']}"
                exp = explanations_map.get(q["id"], "Hãy đối chiếu lại với khái niệm cốt lõi trong eBook SCQA của buổi học này.")
                q_item = {
                    "id": q_id,
                    "type": "mc",
                    "question": q["question"],
                    "options": q["options"],
                    "correct": q["correct"],
                    "explanation": exp
                }
                session_questions.append(q_item)
                bank.append({
                    "id": q_id,
                    "chapter": s,
                    "level": lvl_idx,
                    "session": s,
                    "type": "mc",
                    "question": q["question"],
                    "options": q["options"],
                    "correct": q["correct"],
                    "explanation": exp
                })
    
    session_data = {
        "session": s,
        "chapter": f"Ch.{s}",
        "title": ch["title"],
        "time_limit_minutes": 15,
        "questions": session_questions
    }
    
    s_path = os.path.join(CONTENT_DIR, "questions", f"session-{s}.json")
    with open(s_path, "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=2)

bank_path = os.path.join(CONTENT_DIR, "questions", "bank.json")
with open(bank_path, "w", encoding="utf-8") as f:
    json.dump(bank, f, ensure_ascii=False, indent=2)

print(f"Generated 11 session quiz files and bank.json with {len(bank)} total questions.")
