# ĐỀ CƯƠNG CHI TIẾT CHƯƠNG TRÌNH ĐÀO TẠO (bản cập nhật v3 — rà soát 26/10/2026)

## XÂY DỰNG TRỢ LÝ AI THỰC HIỆN CÔNG VIỆC THEO QUY TRÌNH NGHIỆP VỤ

**Đơn vị thụ hưởng:** Tập đoàn Dầu Khí Việt Nam (Petrovietnam) — phiên dành cho giảng viên và cán bộ đào tạo
**Giảng viên:** ThS. Phó Hải Đăng
**Thời lượng:** 2 ngày — 4 buổi × 3 tiếng (tổng 12 giờ)

> **Giả định vận hành:** Lớp 24–32 học viên, chia 4 nhóm theo cụm đơn vị/bộ môn. Mỗi học viên có laptop và tài khoản Claude **cá nhân (Free/Pro, không phải gói Team)** từ Buổi 1 — vì vậy mọi dữ liệu đưa vào Claude/Gemini Notebook trong lớp chỉ là dữ liệu công khai hoặc dữ liệu mẫu đã khử định danh. Phòng học có máy chiếu, wifi ổn định, bảng trắng và giấy note-dán. Giảng viên cần thêm 1 máy tính cài Claude Desktop (đã kiểm tra Cowork chạy được, đã bật code execution) để chạy 2 demo Cowork ở Buổi 3; Cowork đã được gộp vào ứng dụng Claude từ 16/09/2026, nên kiểm tra giao diện thật trên máy demo trước giờ dạy thay vì dựa vào mô tả cũ.

> **Thay đổi so với bản gốc:** (1) Bỏ phần phá băng + câu chuyện thất bại cá nhân ở đầu Buổi 1, thay bằng bức tranh tổng thể Data → Context → Knowledge → Workflow, mở bằng 1 pain point cụ thể; (2) Case study "Second Brain /daily-capture" ở Buổi 2 được thay bằng case study xuyên suốt "Chấm đồ án sinh viên" (bản đầu là "Tuyển dụng Kỹ sư Vận hành" — xem ghi chú rà soát 26/10/2026) chạy trên Claude Project, dùng bộ học liệu đóng gói riêng; (3) Case study "Second Brain /teach-prep" ở đầu Buổi 3 được thay bằng 2 demo Claude Cowork (mức giao mục tiêu + mức dùng Skill) trên cùng case study đó, chỉ demo không hướng dẫn thực hành; (4) Một case study duy nhất chạy xuyên suốt Buổi 2–3 thay vì hai case study rời rạc.

> **Thay đổi so với bản v2 (rà soát khi làm slide Buổi 1 thực tế):** (1) Ví dụ demo CRISP đổi từ "soạn công văn mời họp giao ban tháng" sang "viết email xin gia hạn báo cáo" — khớp đúng bộ demo đã dựng trên slide thật (4 ảnh chụp before/after), không sửa slide theo đề cương vì slide đã có sẵn và chất lượng tốt hơn; (2) Mục "Bản đồ công cụ AI" (150–165') đổi từ so sánh mạnh/yếu theo hãng sang phân loại theo loại tác vụ, và bỏ lý do "chọn Claude vì dữ liệu không training" — không chính xác, vì bản doanh nghiệp của ChatGPT (Business/Enterprise) và Gemini (Workspace/Enterprise) cũng cam kết không dùng dữ liệu training y hệt Claude Team/Enterprise; thay bằng lý do thực chất: Claude Projects (Custom Instructions + Knowledge Base gộp sẵn) và Cowork (demo bước xa hơn cùng 1 hãng).

> **Thay đổi so với bản v3 gốc (rà soát khi làm kịch bản giảng dạy Buổi 2 thực tế):** Khối 05–20' của Buổi 2 — "Demo mở màn: Vì sao prompt đơn lẻ không đủ?" (15', giao Claude 1 việc phức tạp bằng 1 prompt duy nhất để lộ 3 lỗi: quên context, không nhất quán, tự ý quyết thay người dùng) + case study 4 kịch bản (30') — đổi thành khối 05–10' lý thuyết ngắn "Context Window là gì" (5', giải thích bằng diagram cửa sổ trượt, dẫn ra đúng 2 hệ quả quên context/không nhất quán mà không cần demo sống) + case study 4 kịch bản (40', dồn thêm 10' từ demo bị cắt). Lý do: Context Window của Claude hiện tại đủ lớn khiến việc demo sống "AI quên context" trong 1 prompt duy nhất khó xảy ra đáng tin cậy trên lớp — rủi ro demo "thành công" ngoài ý muốn, phản tác dụng sư phạm. Kịch bản 4 (mở Conversation mới, xem mục Buổi 2 bên dưới) nay đóng vai kép: vừa minh họa trực tiếp khái niệm Context Window vừa trả lời "vì sao phải dùng Project thay vì 1 đoạn chat dài". Không đổi tổng thời lượng buổi (vẫn 180'), không đổi các khối còn lại.

> **Thay đổi so với bản v3 (bổ sung Buổi 4, rà soát khung pháp lý Việt Nam mới):** Khối "3 rủi ro AI" (20–50') và khối "Checklist an toàn dữ liệu" (50–70') của Buổi 4 được bổ sung nội dung về 3 văn bản pháp luật Việt Nam liên quan trực tiếp bối cảnh doanh nghiệp nhà nước: (1) **Luật Bảo vệ dữ liệu cá nhân 2025** (số 91/2025/QH15, hiệu lực 1/1/2026) — đưa dữ liệu cá nhân thật (CV, hồ sơ nhân sự...) vào AI có máy chủ nước ngoài có thể là hành vi "chuyển dữ liệu cá nhân xuyên biên giới", phát sinh nghĩa vụ lập hồ sơ đánh giá tác động trong 60 ngày, nghĩa vụ này độc lập với việc nhà cung cấp có dùng dữ liệu để training hay không; (2) **Luật Bảo vệ bí mật nhà nước** (ghi nhận lúc đó là Luật 2018 sửa đổi — đã đính chính thành Luật số 117/2025/QH15 ở ghi chú rà soát 26/10/2026 bên dưới) — quy định nơi được soạn thảo/lưu giữ tài liệu bí mật nhà nước, khác hẳn khái niệm "Tối mật" theo quy chế nội bộ doanh nghiệp mà Bài tập 4.1 đang dùng — cần tách bạch hai khái niệm này khi giảng, kẻo học viên hiểu lầm "dùng Claude Team là đủ an toàn" cho mọi loại tài liệu mật; (3) **Luật Trí tuệ nhân tạo 2025** (số 134/2025/QH15, hiệu lực 1/3/2026) — nhắc 1 câu để học viên biết khung pháp lý AI đang hình thành. Không đổi tổng thời lượng buổi (vẫn 180'), không đổi mốc phút của từng khối, không đổi CLO/Rubric/Bài tập 4.1 — chỉ làm giàu nội dung giảng trong 2 khối đã có sẵn.

> **Thay đổi so với bản v3 (rà soát tổng hợp 26/10/2026 — phiên giảng viên, case study Chấm đồ án, Siêu trợ lý):** (1) **Đối tượng + case study:** phiên này dành cho giảng viên và cán bộ đào tạo; case study xuyên suốt đổi từ "Tuyển dụng Kỹ sư Vận hành" sang **"Chấm đồ án sinh viên"** (1 giáo viên hướng dẫn, phiếu chấm 10 điểm; quy trình 5 bước, 2 GATE, 2 FALLBACK; 4 kịch bản demo trên 3 báo cáo mẫu DA-01/02/03; bộ học liệu đóng gói riêng, đánh số 00–13). Bộ học liệu tuyển dụng giữ nguyên để dùng cho phiên khác. (2) **Buổi 2:** khối 10–50' chạy 4 kịch bản chấm đồ án, nhịp 2'/8'/6'/8'/8'/8' (tổng vẫn 40'); khối 130–175' tách thành sơ đồ nghiệp vụ 3' + sơ đồ GATE/FALLBACK 7' + hướng dẫn 5' + thực hành 30' (tổng vẫn 45'); bảng 7 nguyên tắc nối từng nguyên tắc với đúng khoảnh khắc trong demo; bài về nhà thêm việc tạo sẵn Project Siêu trợ lý (~10'). (3) **Siêu trợ lý (mô hình lai):** thêm công cụ "Siêu trợ lý" — một Claude Project hỗ trợ tạo trợ lý quy trình (nhận mô tả quy trình đã khử thông tin → phỏng vấn tối đa 8 câu → xuất 7 phần: tóm tắt, Custom Instructions, 2 sơ đồ, danh sách Knowledge Base, hướng dẫn thiết lập + 3 kịch bản test, danh sách giả định cần soát). Nhóm **vẽ sơ đồ A3 trước, dùng Siêu trợ lý sau, rồi đối chiếu** — nên CLO3 vẫn chấm trên sơ đồ A3 nhóm tự vẽ, không đổi CLO/Rubric. Giai đoạn 1–2 của Buổi 3 vẫn 35'. Prompt Siêu trợ lý (bản 08/10) là tài liệu #9. (4) **Buổi 3 đồng bộ thứ tự đã chốt ngày 28/09/2026:** thực hành xây dựng trước, demo Cowork (mức 1 + mức 2 + chốt Project/Cowork, 35') dời xuống sau Trình bày chéo; tên buổi và tổng 180' giữ nguyên; demo Cowork chuyển sang dữ liệu chấm đồ án. (5) **Buổi 4 và vận hành:** demo NotebookLM đổi tên thành Gemini Notebook, demo 4 nguồn (PDF, YouTube, DOCX, ghi âm) chủ đề "họp hiệu quả"; thêm 2 sự cố thật làm slide (Samsung 2023; lỗi ChatGPT ngày 20/03/2023); ví dụ dữ liệu cá nhân đổi từ CV/hồ sơ nhân sự sang bài làm, bảng điểm, hồ sơ sinh viên; bỏ khuyến nghị gói Team — lớp dùng tài khoản cá nhân nên dữ liệu Nội bộ trở lên chỉ vào công cụ doanh nghiệp do đơn vị cấp. (6) **Đính chính pháp lý:** Luật Bảo vệ bí mật nhà nước hiện hành là Luật số 117/2025/QH15 (hiệu lực 01/3/2026, thay Luật 2018); bỏ cách diễn đạt "cấm tuyệt đối" của ghi chú trước, diễn đạt lại ở khối 50–70' Buổi 4. Giảng viên đối chiếu văn bản chính thức và nghị định hướng dẫn trước khi dạy. Không đổi CLO, Rubric, Phần 2, Template 5.2, đáp án Bài tập 4.1; mọi buổi vẫn đúng 180'.

---

# PHẦN 1 — TỔNG QUAN CHƯƠNG TRÌNH

## 1.1. Tên chương trình

**"Từ Prompt đến Quy trình: Xây dựng Trợ lý AI làm việc theo quy trình nghiệp vụ với Claude"**

## 1.2. Mục tiêu tổng quát

1. Chuyển học viên từ trạng thái **hoài nghi/chưa dùng AI** sang trạng thái **chủ động dùng AI đúng cách** — hiểu bản chất, biết giới hạn, kiểm soát được rủi ro.
2. Giúp học viên nắm được **bức tranh tổng thể**: dữ liệu rời rạc (Data) → gắn ngữ cảnh (Context) → trở thành quy tắc áp dụng được (Knowledge) → vận hành thành quy trình chạy lặp lại được (Workflow).
3. Trang bị năng lực **thiết kế quy trình nghiệp vụ nhiều bước cho AI**: điều kiện chuyển bước có xác nhận, xử lý thiếu thông tin, kiểm soát đầu ra.
4. Mỗi nhóm học viên **tự tay xây dựng và bàn giao 1 Claude Project hoạt động được** cho một quy trình nghiệp vụ thực tế của đơn vị/bộ môn mình, với sự hỗ trợ của Siêu trợ lý (trợ lý AI giúp tạo trợ lý quy trình).
5. Hình thành **văn hóa sử dụng AI an toàn** trong môi trường dầu khí và đào tạo: phân loại dữ liệu, nhận diện hallucination, giữ vai trò "Bạn là Leader, AI là Cộng sự".

## 1.3. Đối tượng

Giảng viên và cán bộ đào tạo (khoa/bộ môn, phòng đào tạo, khảo thí, hành chính...). Không yêu cầu biết lập trình. Không yêu cầu kinh nghiệm AI trước đó. *(Phiên dành cho khối văn phòng Tập đoàn — Nhân sự, Hành chính, Kế hoạch, Tài chính, Kỹ thuật, HSE, Pháp chế — dùng bộ học liệu Tuyển dụng Kỹ sư Vận hành, vẫn giữ trong Project.)*

## 1.4. Phương pháp giảng dạy

- **Mở bằng bức tranh tổng thể, không mở bằng lý thuyết rời rạc** — học viên biết ngay 2 ngày này đi từ đâu đến đâu trước khi học chi tiết từng phần.
- **Mục tiêu của HỌ, không phải giáo án của bạn** — thu thập mục tiêu bằng note-dán ngay buổi đầu, treo lên "Bảng Mục Tiêu", tick từng mục trong suốt khóa học và tổng kết ở buổi cuối.
- **Một case study xuyên suốt** — "Chấm đồ án sinh viên" chạy liên tục từ Buổi 2 (Project) sang cuối Buổi 3 (Cowork), giúp học viên thấy rõ 1 quy trình đi qua các mức công cụ khác nhau, không phải nhiều ví dụ rời rạc.
- **Quy trình 3 bước lặp cho mọi chủ đề:** Bản chất (lý thuyết ≤5 phút) → Framework (cách dùng) → Demo + Case study dầu khí.
- **Tỷ lệ thời lượng:** Demo thực tế 60–70% | Thực hành 20–30% | Lý thuyết 10%.
- **Nguyên tắc vàng xuyên suốt:** "Bạn là Leader, AI là Cộng sự."

## 1.5. Công cụ sử dụng

| Công cụ | Vai trò trong khóa |
|---|---|
| **Claude (Projects + Custom Instructions)** | Công cụ chính — toàn bộ thực hành xây AI Assistant |
| **Claude Cowork** | Demo mở rộng tầm nhìn (không thực hành) — cho thấy bước xa hơn Project: giao mục tiêu để AI tự thực thi nhiều bước, và viết Skill để chạy quy trình có sẵn ngoài khung chat |
| **Siêu trợ lý** (Claude Project, prompt bản 08/10) | Công cụ tạo trợ lý quy trình: phỏng vấn người dùng rồi xuất Custom Instructions, 2 sơ đồ, hướng dẫn thiết lập và kịch bản test — dùng ở Buổi 3 sau khi nhóm đã vẽ A3 |
| Case study "Chấm đồ án sinh viên" (bộ học liệu đóng gói riêng) | Case study xuyên suốt Buổi 2–3, minh họa nguyên tắc thiết kế quy trình trên cả Project lẫn Cowork |
| Gemini Notebook (trước đây NotebookLM) | Giới thiệu ở mức demo — hỏi đáp theo nguồn đã nạp, có trích dẫn (RAG); với tài khoản cá nhân chỉ dùng nguồn công khai/mẫu |
| ChatGPT, Gemini | Chỉ giới thiệu ở mức bản đồ công cụ tổng quan |
| Giấy A3 + note-dán + bút | Vẽ quy trình trên giấy trước khi số hóa — bắt buộc |

---

# PHẦN 2 — CHUẨN ĐẦU RA (CLOs)

*(Không đổi so với bản gốc)*

| Mã | Chuẩn đầu ra | Mức Bloom |
|---|---|---|
| **CLO1** | **Giải thích** được bản chất AI tạo sinh ("máy đoán chữ"), hiện tượng hallucination, và giới hạn của AI trong nghiệp vụ dầu khí | Understand |
| **CLO2** | **Viết** được prompt hiệu quả theo framework CRISP và **vận dụng** các kỹ thuật iterative, negative, few-shot để cải thiện đầu ra | Apply |
| **CLO3** | **Phân tích** một quy trình nghiệp vụ của phòng ban thành các bước tuần tự, xác định được: điểm cần cổng xác nhận (gate), điểm có thể thiếu thông tin (fallback), và chuẩn đầu ra từng bước | Analyze |
| **CLO4** | **Xây dựng** được một Claude Project hoàn chỉnh với Custom Instructions tuân thủ 7 nguyên tắc thiết kế quy trình AI, hoạt động đúng: dừng chờ xác nhận, hỏi khi thiếu thông tin, đầu ra theo template chuẩn | Create |
| **CLO5** | **Đánh giá** được chất lượng đầu ra của AI: phát hiện hallucination, kiểm tra tính nhất quán, đề xuất cách cải thiện prompt/quy trình | Evaluate |
| **CLO6** | **Phân loại** được dữ liệu công việc theo 4 mức mật (Công khai / Nội bộ / Bí mật / Tối mật) và **áp dụng** đúng checklist an toàn khi đưa dữ liệu vào công cụ AI | Apply |

---

# PHẦN 3 — NỘI DUNG CHI TIẾT TỪNG BUỔI

## BUỔI 1 (Ngày 1 — Sáng): "AI TẠO SINH & KỸ THUẬT PROMPT CƠ BẢN"

**Mục tiêu buổi:** Cho học viên thấy bức tranh tổng thể + trang bị kỹ năng giao tiếp với AI hiệu quả.
**Mapping CLO:** CLO1, CLO2.

### Timeline phút-phút

| Thời gian | Phút | Nội dung | Hình thức |
|---|---|---|---|
| 00–05 | 5' | **Mở đầu bằng pain point:** "Anh/chị đã bao giờ hỏi AI xong phải giải thích lại từ đầu ở lần hỏi sau chưa? Hay tìm một công văn cũ mãi không ra khi cần đối chiếu?" — không cần cả lớp trả lời, chỉ cần họ gật đầu nhận ra vấn đề | Dẫn nhập ngắn |
| 05–20 | 15' | **Bức tranh tổng thể — Data → Context → Knowledge → Workflow:** Data thô (công văn, hợp đồng, email) → gắn Context để có nghĩa (ai, khi nào, thuộc quy trình nào) → tích lũy thành Knowledge (quy tắc áp dụng lại được) → đóng gói thành Workflow chạy lặp lại được. Đây là bản đồ cho toàn bộ 2 ngày, sẽ quay lại đúng slide này ở đầu mỗi buổi sau | Trình bày 1 slide bản đồ |
| 20–35 | 15' | **Bảng Mục Tiêu:** mỗi học viên viết 1–2 mong muốn cụ thể lên note-dán ("Tôi muốn AI giúp tôi ___"), dán lên bảng. Giảng viên gom nhóm nhanh, cam kết giải quyết trong 2 ngày | Note-dán |
| 35–50 | 15' | **Bản chất AI tạo sinh** (lý thuyết ≤5'): "máy đoán chữ", vì sao AI bịa (hallucination). Demo sống: hỏi Claude một quy chuẩn HSE không tồn tại → phân tích cách AI phản ứng | Lý thuyết ngắn + demo |
| 50–80 | 30' | **Framework CRISP** (Context – Role – Instruction – Specifics – Preview). Demo so sánh trên Claude: prompt xấu vs prompt CRISP với cùng 1 việc — *viết email xin gia hạn báo cáo* | Demo đối chứng |
| 80–95 | 15' | **Giải lao** | |
| 95–125 | 30' | **Thực hành 1.1:** Viết prompt CRISP **trên giấy trước** cho 1 công việc thật của mình → gõ vào Claude → dùng Trợ lý chấm Prompt theo CRISP (link riêng) để tự chấm chéo bản của mình → so sánh với người ngồi cạnh. Giảng viên chọn 2–3 cặp trình chiếu, cả lớp góp ý | Thực hành cá nhân + peer review |
| 125–150 | 25' | **Kỹ thuật nâng cao:** Iterative (sửa dần qua nhiều lượt), Negative (nói rõ điều KHÔNG muốn), Few-shot (đưa ví dụ mẫu). Demo mỗi kỹ thuật trên chính prompt học viên vừa viết | Demo trên bài học viên |
| 150–165 | 15' | **Bản đồ công cụ AI theo tác vụ:** Hội thoại đa năng (ChatGPT/Claude/Gemini — có thể bịa nguồn) / Tìm kiếm có nguồn (Perplexity, ChatGPT Search — vẫn cần verify) / Quản trị tri thức (Gemini Notebook, trước đây NotebookLM — chỉ trả lời dựa trên nguồn bạn nạp nên ít bịa hơn, nhưng vẫn phải kiểm tra trích dẫn). Nêu rõ lý do khóa này chọn Claude để thực hành: Projects gộp sẵn Custom Instructions + Knowledge Base, và Cowork demo được bước xa hơn cùng 1 hãng — không phải vì dữ liệu an toàn hơn (bản doanh nghiệp Claude Team, ChatGPT Business, Gemini Workspace đều cam kết không dùng dữ liệu training). Nhắc: lớp dùng tài khoản cá nhân nên chỉ đưa dữ liệu công khai hoặc dữ liệu mẫu đã khử định danh | Trình bày + hỏi đáp |
| 165–180 | 15' | Chốt buổi: quay lại Bảng Mục Tiêu, tick các mục đã chạm. Nhắc lại bức tranh tổng thể — hôm nay mới ở tầng Data/Context, chiều nay sang Knowledge. Giao "bài tập trưa": nghĩ về 1 quy trình lặp lại nhiều nhất ở đơn vị/bộ môn của mình | Chốt |

### Hoạt động thực hành cụ thể

**Thực hành 1.1 — Prompt CRISP đầu tiên (30 phút)**
- Đầu vào: 1 công việc văn bản thật học viên đang làm (công văn, email, tóm tắt báo cáo...)
- Yêu cầu: viết đủ 5 thành phần CRISP trên phiếu giấy phát sẵn → nhập vào Claude → chạy 2 lần: bản gốc "kiểu cũ" và bản CRISP
- Bước bổ sung: dán prompt CRISP của mình vào Trợ lý chấm Prompt theo CRISP (link chia sẻ đầu giờ) để nhận đánh giá chi tiết 5 thành phần + bản gợi ý chỉnh sửa, trước khi so sánh với người ngồi cạnh
- Sản phẩm: 2 đầu ra đối chứng + 1 nhận xét cá nhân "khác nhau ở đâu"

### Công cụ & tài liệu chuẩn bị

- Slide bản đồ Data → Context → Knowledge → Workflow (dùng lại ở đầu Buổi 2, 3, 4)
- Phiếu giấy CRISP in sẵn (mỗi người 2 tờ), note-dán 3 màu, Bảng Mục Tiêu (giấy A0)
- Tài khoản Claude cá nhân của từng học viên đã kích hoạt và test đăng nhập trước buổi học
- Kịch bản demo: prompt xấu/tốt cho email xin gia hạn báo cáo; câu hỏi bẫy hallucination về quy chuẩn HSE
- Link "Trợ lý chấm Prompt theo CRISP" — đã test hoạt động với ít nhất 1 tài khoản khác tài khoản giảng viên; chuẩn bị mã QR chiếu lên màn hình để học viên quét, tránh gõ tay đường link dài

### Tiêu chí đánh giá hoạt động

- Prompt của học viên có đủ 5 thành phần CRISP (đánh giá nhanh trên phiếu giấy)
- Học viên nêu được ít nhất 1 khác biệt cụ thể giữa 2 đầu ra đối chứng

---

## BUỔI 2 (Ngày 1 — Chiều): "TỪ PROMPT ĐƠN LẺ ĐẾN QUY TRÌNH NHIỀU BƯỚC"

**Mục tiêu buổi:** Hiểu khái niệm quy trình AI + làm quen Claude Projects, qua case study xuyên suốt "Chấm đồ án sinh viên", và làm quen Siêu trợ lý (trợ lý AI hỗ trợ tạo trợ lý quy trình) qua bài về nhà.
**Mapping CLO:** CLO3, CLO4 (khởi động).

### Timeline phút-phút

| Thời gian | Phút | Nội dung | Hình thức |
|---|---|---|---|
| 00–05 | 5' | Quay lại slide bản đồ Data→Context→Knowledge→Workflow, khoanh tròn vào Knowledge — "Sáng nay ta học cách đưa đúng Data+Context vào prompt. Chiều nay: khi Data+Context lặp lại nhiều lần, nó trở thành Knowledge — quy tắc dùng lại được" | Trình bày 1 slide |
| 05–10 | 5' | **Bản chất — Context Window là gì:** AI trả lời dựa trên "trí nhớ" có giới hạn (cửa sổ ngữ cảnh) — minh họa bằng diagram cửa sổ trượt: lúc mới bắt đầu, toàn bộ tin nhắn đều nằm trong cửa sổ; sau nhiều lượt trao đổi, tin nhắn đầu bị đẩy ra ngoài. Từ đó dẫn ra 2 hệ quả khi cuộc trò chuyện dài ra: quên context (điều dặn ở đầu bị đẩy ra ngoài khung) và không nhất quán (cùng 1 yêu cầu, chạy ở đầu và chạy khi hội thoại đã dài có thể ra kết quả khác nhau) | Lý thuyết ngắn (diagram) |
| 10–50 | 40' | **Case study "Chấm đồ án sinh viên" trên Claude Project — 4 kịch bản** (nhịp: 2' dẫn nhập · 8' · 6' · 8' · 8' · 8' phân tích chung): (1) chạy xuôi (DA-01) — Claude tóm tắt 5 bước, chấm N1–N5 kèm trích dẫn nguyên văn từ báo cáo, rồi dừng ở GATE 1 chờ giáo viên xác nhận Bảng điểm; (2) thiếu thông tin (DA-02) — giáo viên chưa đưa điểm Chuyên cần/Hình thức, Claude hỏi lại thay vì tự đoán (FALLBACK 1); tiêu chí không có căn cứ trong bài thì ghi "Chưa đủ căn cứ" và hỏi (FALLBACK 2); (3) giục "vượt gate" — Claude từ chối viết nhận xét khi chưa xác nhận điểm; sau đó giáo viên chỉnh điểm, xác nhận GATE 1 → nhận xét → GATE 2 → phiếu chấm hoàn chỉnh (mục 1–5 để "[GV tự điền]", dữ liệu sinh viên không đi qua AI); (4) mở Conversation mới trong cùng Project cho báo cáo khác (DA-03) — Instructions+KB tự động có sẵn nhưng điểm bài DA-01 không lẫn sang. Kịch bản 4 đồng thời minh họa trực tiếp Context Window vừa học (Instructions+KB nằm trong Project chứ không trong cuộc trò chuyện, nên không bị "đẩy ra khỏi khung" khi mở Conversation mới) và trả lời câu hỏi "vì sao phải dùng Project thay vì 1 đoạn chat dài". Chuẩn bị: Memory đã tắt, 3 Conversation mở sẵn. *(Xem chi tiết kịch bản trong bộ học liệu đóng gói riêng.)* | Demo sống + phân tích chung |
| 50–80 | 30' | **Claude Projects hands-on:** từng học viên tự tạo Project đầu tiên theo giảng viên: (1) tạo Project, (2) viết Custom Instructions ngắn 5 dòng, (3) upload 1 tài liệu mẫu vào Knowledge Base, (4) test 1 câu hỏi để thấy AI trả lời dựa trên tài liệu | Làm theo từng bước |
| 80–95 | 15' | **Giải lao** | |
| 95–130 | 35' | **7 Nguyên tắc thiết kế quy trình AI** — mỗi nguyên tắc trình bày theo công thức: tên → vì sao cần (nối lại đúng khoảnh khắc vừa thấy ở case study chấm đồ án — vd: nguyên tắc 2 ← GATE 1 và cú từ chối ở kịch bản 3; nguyên tắc 3 ← kịch bản 2) → câu prompt mẫu tiếng Việt để hiện thực hóa. Trọng tâm demo kỹ nguyên tắc 2 (gate) và 3 (fallback) | Lý thuyết ngắn + demo từng nguyên tắc |
| 130–133 | 3' | **Sơ đồ nghiệp vụ mẫu:** chiếu quy trình chấm đồ án khi chưa có AI (một người, một phiếu, năm bước) — "trước khi vẽ cho AI, vẽ cho người"; hỏi lớp: chỗ nào thầy cô thật ra đã tự dừng lại? | Trình bày 1 slide |
| 133–140 | 7' | **Sơ đồ GATE/FALLBACK mẫu:** chiếu quy trình giao một phần cho AI — 2 GATE (sau Bảng điểm, sau Nhận xét) và 2 FALLBACK (thiếu điểm giáo viên nắm, thiếu căn cứ trong bài); mỗi dấu là một việc người vẫn tự dừng ngoài đời, nay viết ra. Nhấn: không có GATE ở một bước cũng là một quyết định thiết kế | Trình bày 1 slide |
| 140–145 | 5' | Hướng dẫn Thực hành 2.1: phát Phiếu Thiết Kế Quy Trình (A3), nhắc chọn quy trình thật của đơn vị/bộ môn | Giao việc |
| 145–175 | 30' | **Thực hành 2.1 (nhóm):** Chọn 1 quy trình đơn giản của đơn vị/bộ môn → vẽ thành sơ đồ 3–5 bước trên giấy A3 → đánh dấu gate 🔒 và điểm fallback ❓ → viết bản nháp Custom Instructions đầu tiên. Giảng viên đi từng nhóm | Thực hành nhóm |
| 175–180 | 5' | Mỗi nhóm nói 1 câu về quy trình đã chọn. Giao bài về nhà: (1) mang theo 1–2 tài liệu mẫu thật (đã khử thông tin mật) của quy trình đó cho ngày mai; (2) tạo sẵn Project Siêu trợ lý theo hướng dẫn Chương 3 của ebook (~10') | Chia sẻ nhanh |

### 7 Nguyên tắc thiết kế quy trình AI (nội dung lõi của khóa)

*(Không đổi — nguồn ví dụ minh họa là case study Chấm đồ án sinh viên; bảng nối từng nguyên tắc với khoảnh khắc trong demo nằm trong kịch bản giảng dạy)*

| # | Nguyên tắc | Câu prompt mẫu (tiếng Việt) |
|---|---|---|
| 1 | **Khởi tạo bắt buộc** — AI phải đọc context trước khi làm | "Trước khi bắt đầu, hãy đọc toàn bộ tài liệu trong Knowledge Base và tóm tắt lại để tôi xác nhận bạn đã hiểu đúng." |
| 2 | **Quy trình tuần tự có cổng** — chỉ tiếp tục khi người dùng xác nhận | "Sau mỗi bước, DỪNG LẠI và hỏi: 'Bạn xác nhận chuyển sang bước tiếp theo chứ?'. Tuyệt đối không tự làm bước kế tiếp." |
| 3 | **Xử lý thiếu thông tin** — hỏi hoặc dùng mặc định | "Nếu thiếu thông tin bắt buộc, hãy hỏi tôi. Nếu thiếu thông tin không bắt buộc, dùng giá trị mặc định sau: [...] và ghi chú rõ đã dùng mặc định." |
| 4 | **Phân quyền tin cậy** — nguồn đáng tin vs chưa xác minh | "Chỉ dùng số liệu từ tài liệu tôi cung cấp. Kiến thức chung phải đánh dấu [CẦN KIỂM CHỨNG]." |
| 5 | **Template đầu ra chuẩn** — nhất quán mọi lần | "Mọi đầu ra phải theo đúng cấu trúc sau, không thêm không bớt mục: [...]" |
| 6 | **Vai trò rõ ràng** — AI là cộng sự, không phải người quyết định | "Bạn đề xuất phương án kèm ưu/nhược điểm. Quyết định cuối cùng luôn thuộc về tôi." |
| 7 | **Vòng phản hồi** — kết quả quay lại cải thiện quy trình | "Cuối phiên làm việc, hỏi tôi: 'Bước nào trong quy trình cần điều chỉnh cho lần sau?'" |

### Công cụ & tài liệu chuẩn bị

- Bộ học liệu "Chấm đồ án sinh viên" (đóng gói riêng, setup Project trước giờ dạy): Custom Instructions (`01`), 4 file Knowledge Base (`02`–`05`), 3 báo cáo mẫu `DA-01/02/03.docx` đã khử thông tin sinh viên, kịch bản test 4 tình huống (`06`); **tắt Memory** khi chạy Kịch bản 4; chuẩn bị ảnh chụp dự phòng
- File prompt Siêu trợ lý (`.md`, bản 08/10) + hướng dẫn Chương 3 của ebook — gửi học viên qua LMS cho bài về nhà
- 1 tài liệu mẫu công khai để học viên upload thử vào Knowledge Base của Project riêng mình (VD: quy chế văn thư mẫu)
- Giấy A3, sticker 🔒 và ❓, bút dạ
- Handout "7 Nguyên tắc + câu prompt mẫu" (in màu, 1 trang)

### Tiêu chí đánh giá hoạt động

- Học viên tự tạo được Project và Knowledge Base hoạt động (kiểm tra trực tiếp)
- Sơ đồ nhóm có tối thiểu 3 bước, ít nhất 1 gate và 1 điểm fallback được đánh dấu đúng chỗ (CLO3)

---

## BUỔI 3 (Ngày 2 — Sáng): "TỪ WORKFLOW TRONG CHAT ĐẾN TỰ ĐỘNG HOÁ, RỒI THỰC HÀNH XÂY DỰNG"

**Mục tiêu buổi:** Tự tay xây dựng AI Assistant hoàn chỉnh cho quy trình nghiệp vụ thực tế (vẽ A3 trước, dùng Siêu trợ lý sau), rồi thấy bước xa hơn của Workflow (Cowork).
**Mapping CLO:** CLO3, CLO4, CLO5. **Đây là buổi tạo ra sản phẩm cuối khóa.**

### Timeline phút-phút

| Thời gian | Phút | Nội dung | Hình thức |
|---|---|---|---|
| 00–15 | 15' | Recap ngày 1 bằng trò chơi hỏi nhanh (7 nguyên tắc là gì? gate để làm gì? vì sao Conversation mới trong Project vẫn "nhớ" đúng quy trình?). Giải đáp thắc mắc tồn đọng | Quiz tương tác |
| 15–25 | 10' | Quay lại slide bản đồ, khoanh tròn Workflow — "Hôm qua các anh chị đã thấy Knowledge biến thành Workflow chạy trong Project. Sáng nay chính các anh chị biến quy trình của mình thành một Workflow như vậy; làm xong và test đạt, ta sẽ xem thêm một bước xa hơn" | Trình bày + dẫn nhập |
| 25–35 | 10' | Brief 4 tình huống thực hành, chia nhóm theo đơn vị/bộ môn, phát Phiếu Thiết Kế Quy Trình và Rubric (nhóm biết trước mình được chấm gì). Nhắc: chụp/nộp sơ đồ A3 tự vẽ TRƯỚC khi chạy Siêu trợ lý | Tổ chức nhóm |
| 35–70 | 35' | **Giai đoạn 1–2 (mô hình lai: vẽ A3 trước, Siêu trợ lý sau):** (a) ~10': hoàn thiện sơ đồ A3 của nhóm từ Buổi 2 (các bước, gate 🔒, fallback ❓, đầu ra từng bước), chụp ảnh lưu lại; (b) ~20': đưa mô tả quy trình (đã khử thông tin) và bản nháp Buổi 2 vào Siêu trợ lý, trả lời phỏng vấn tối đa 8 câu, nhận 7 phần đầu ra (tóm tắt, Custom Instructions, 2 sơ đồ, danh sách Knowledge Base, hướng dẫn thiết lập + 3 kịch bản test, danh sách giả định cần soát); (c) ~5': đối chiếu sơ đồ A3 với sơ đồ Siêu trợ lý, soát mục "giả định tôi đã tự điền" và rà Custom Instructions với Template chuẩn (Phần 5.2) / 7 nguyên tắc | Thực hành nhóm |
| 70–80 | 10' | **Giải lao** | |
| 80–120 | 40' | **Giai đoạn 3–4:** Tạo Claude Project theo hướng dẫn thiết lập do Siêu trợ lý xuất, nhập Custom Instructions, upload tài liệu mẫu → **test theo 3 kịch bản bắt buộc:** (1) chạy xuôi bình thường, (2) cố tình bỏ trống thông tin xem AI có hỏi lại không, (3) thử "vượt gate" xem AI có dừng không. Test lỗi thì sửa tay hoặc nhờ Siêu trợ lý xuất lại đúng phần bị ảnh hưởng. Giảng viên đi từng nhóm coaching, chấm điểm quá trình | Thực hành nhóm + coaching |
| 120–140 | 20' | **Trình bày chéo:** mỗi nhóm 3' demo sống Project của mình + 2' nhóm khác phản biện ("thử phá" bằng 1 câu hỏi bất ngờ). Học hỏi chéo giữa các đơn vị/bộ môn | Demo nhóm + phản biện |
| 140–155 | 15' | **Demo Cowork mức 1 — Giao mục tiêu:** nối từ câu "xem thêm một bước xa hơn". Dùng thư mục dữ liệu chấm đồ án (`Demo-Cowork-ChamDoAn/`, có `DiemGV.md`), giao Cowork một mục tiêu cuối cùng; Claude tự lập kế hoạch và xuất file thật (`BangDiemGoiY.xlsx`, `NhanXet.docx`, `PhieuCham_DA-0x.docx`). Nhấn: đây là Claude tự sáng tác quy trình, không có script viết sẵn; chỉ cấp quyền đúng thư mục demo | Demo sống (Claude Desktop) |
| 155–170 | 15' | **Demo Cowork mức 2 — Dùng Skill (quy trình viết sẵn):** cùng case study, chạy qua Skill chấm đồ án đã viết sẵn 5 bước + 2 gate giống Custom Instructions của Project. Nhấn: Cowork vẫn dừng đúng ở GATE 1 (Bảng điểm, kèm "Chưa đủ căn cứ" ở bài DA-02) và GATE 2 (Nhận xét) dù đang tự động hoá — khác biệt Project/Cowork nằm ở nơi thực thi và loại đầu ra, không phải "có viết được quy trình hay không" | Demo sống (Claude Desktop) |
| 170–175 | 5' | Chốt nhanh: Project = quy trình chạy trong chat, đầu ra là văn bản, phù hợp việc cần trao đổi qua lại nhiều. Cowork = quy trình chạm vào file/công cụ thật, phù hợp việc đã định hình rõ, cần giao và lấy kết quả cuối. Phần này chỉ để biết, khóa nâng cao sau sẽ thực hành | Chốt |
| 175–180 | 5' | Chốt buổi: mỗi nhóm đã có 1 Project vượt 3 kịch bản test; giảng viên tổng hợp lỗi hay gặp của cả 4 nhóm, hẹn buổi chiều hoàn thiện | Chốt |

> **Lưu ý thời lượng Trình bày chéo:** rút từ 5' xuống 3'/nhóm demo so với bản gốc để bù giờ cho phần Cowork cuối buổi — vẫn đủ cho 4 nhóm demo + phản biện trong 20'.

> **Thứ tự Buổi 3:** thực hành xây dựng trước, demo Cowork sau (chốt với giảng viên ngày 28/09/2026, đồng bộ vào đề cương ngày 26/10/2026); tên buổi giữ nguyên dù mạch kể đã đảo lại.

### 4 Tình huống thực hành (chia nhóm theo đơn vị/bộ môn)

*(Không đổi, trừ 1 điều chỉnh ở nhóm Hành chính/Pháp chế — xem ghi chú. Cập nhật 26/10/2026: với phiên giảng viên, bảng này là gợi ý dự phòng — nhóm được chọn quy trình thật của đơn vị/bộ môn mình, ví dụ soạn đề kiểm tra, chấm bài, lập kế hoạch giảng dạy; không bắt buộc trùng bảng.)*

| Nhóm | Tình huống | Quy trình gợi ý | Gate bắt buộc tối thiểu |
|---|---|---|---|
| Nhân sự / Đào tạo | Xây dựng chương trình đào tạo nội bộ | Xác định nhu cầu → Thiết kế nội dung → Tạo tài liệu → Đánh giá | Sau "Thiết kế nội dung" — người phụ trách duyệt khung trước khi AI viết chi tiết |
| Kỹ thuật / Dự án | Lập hồ sơ mời thầu | Thu thập yêu cầu → Soạn TOR → Review → Tổng hợp hồ sơ | Sau "Soạn TOR" — không tổng hợp hồ sơ khi TOR chưa được xác nhận |
| Hành chính / Pháp chế | Soạn thảo và rà soát văn bản | Xác định loại VB → Soạn thảo → **Rà soát rủi ro pháp lý/điều khoản** → Phê duyệt | Sau "Rà soát rủi ro" — AI liệt kê điều khoản có rủi ro, người dùng xác nhận đã xử lý *(đổi từ "Kiểm tra thể thức" — rủi ro thật của pháp chế nằm ở nội dung/ràng buộc, không phải trình bày)* |
| Tài chính / Kế hoạch | Tổng hợp và phân tích báo cáo | Thu thập dữ liệu → Phân tích → Trực quan hóa → Tóm tắt | Sau "Phân tích" — người dùng xác nhận số liệu đúng trước khi AI viết tóm tắt trình lãnh đạo |

### Công cụ & tài liệu chuẩn bị

- **Bộ học liệu Cowork:** hướng dẫn demo mức 1 + mức 2 (`08`), Skill chấm đồ án (`09`) đã cài sẵn và test trước trên máy giảng viên, thư mục `Demo-Cowork-ChamDoAn/` (có `DiemGV.md`; đầu ra gồm `BangDiemGoiY.xlsx`, `NhanXet.docx`, `PhieuCham_DA-0x.docx`; dùng chung dữ liệu với case study Buổi 2)
- **Siêu trợ lý (prompt bản 08/10):** mỗi học viên đã tạo sẵn Project Siêu trợ lý từ bài về nhà Buổi 2; giảng viên có 1 Project dự phòng đã test, và kiểm tra trước cách xem sơ đồ mermaid (nhờ Claude tạo Artifact, hoặc dán vào mermaid.live)
- **Phiếu Thiết Kế Quy Trình** (A3, in sẵn khung: Bước / Đầu vào / Đầu ra / Gate? / Fallback?)
- **Template Custom Instructions chuẩn** (xem Phần 5) — mỗi nhóm 1 bản in + 1 bản mềm
- Bộ tài liệu mẫu đã khử mật cho từng tình huống (đề phòng nhóm quên mang tài liệu thật)
- Rubric in sẵn phát trước khi thực hành

### Tiêu chí đánh giá hoạt động

Đánh giá theo Rubric sản phẩm cuối khóa (Phần 4). Riêng buổi này, điều kiện đạt tối thiểu: Project **vượt qua cả 3 kịch bản test** (chạy xuôi — hỏi khi thiếu — dừng ở gate), và nhóm **nộp ảnh sơ đồ A3 tự vẽ TRƯỚC khi chạy Siêu trợ lý** (sơ đồ do Siêu trợ lý xuất chỉ để đối chiếu, không thay thế bài vẽ tay).

---

## BUỔI 4 (Ngày 2 — Chiều): "NÂNG CAO, AN TOÀN & LỘ TRÌNH TƯƠNG LAI"

**Mục tiêu buổi:** Xử lý edge cases + an toàn dữ liệu + tự tin áp dụng sau khóa học.
**Mapping CLO:** CLO5, CLO6.

*(Cập nhật: bổ sung nội dung khung pháp lý Việt Nam mới trong khối "3 rủi ro AI" và "Checklist an toàn dữ liệu" — xem ghi chú thay đổi ở đầu văn bản. Các khối còn lại không đổi so với bản gốc. Cập nhật 26/10/2026: đính chính tên và nội dung Luật Bảo vệ bí mật nhà nước, thêm 2 sự cố thật, đổi demo sang Gemini Notebook, đổi ví dụ dữ liệu cá nhân sang bối cảnh nhà trường.)*

### Timeline phút-phút

| Thời gian | Phút | Nội dung | Hình thức |
|---|---|---|---|
| 00–20 | 20' | **Kỹ thuật nâng cao:** bắt AI tự kiểm tra (self-check: "trước khi trả kết quả, hãy rà lại theo checklist sau..."), yêu cầu AI trích dẫn nguồn từ Knowledge Base, xử lý quy trình rẽ nhánh (nếu A thì... nếu B thì...). Mở đầu bằng 1 câu nối: "Sáng nay các anh chị đã thấy Workflow chạy được tới đâu — Project và cả Cowork. Chiều nay: làm sao để Workflow đó *đáng tin*". Demo trên chính Project của các nhóm | Demo trên sản phẩm học viên |
| 20–50 | 30' | **3 rủi ro AI:** (1) Hallucination — case study minh họa dầu khí (nêu rõ là tình huống dựng, không phải sự kiện thật): AI bịa quy chuẩn an toàn nghe rất thuyết phục, hậu quả nếu đưa vào hồ sơ HSE thật; (2) Rò rỉ dữ liệu — mở bằng 2 sự cố có thật làm slide (Samsung 2023: nhân viên dán mã nguồn và nội dung họp nội bộ vào ChatGPT; lỗi hệ thống ChatGPT ngày 20/03/2023: một số người dùng thấy tiêu đề hội thoại của người khác — giảng viên kiểm lại nguồn trước khi chiếu); so sánh chính sách xử lý dữ liệu Claude / ChatGPT / Gemini, bản free/cá nhân vs bản doanh nghiệp; **nhắc thêm: đưa dữ liệu cá nhân thật (bài làm, bảng điểm, hồ sơ sinh viên...) vào một AI có máy chủ ở nước ngoài — dù bản doanh nghiệp không dùng để training — vẫn có thể là hành vi "chuyển dữ liệu cá nhân xuyên biên giới" theo Luật Bảo vệ dữ liệu cá nhân 2025 (số 91/2025/QH15, hiệu lực 1/1/2026), phát sinh nghĩa vụ lập hồ sơ đánh giá tác động; nghĩa vụ pháp lý này độc lập với chính sách training của nhà cung cấp**; (3) Phụ thuộc quá mức — mất tư duy phản biện, quy tắc "AI viết nháp, người ký chịu trách nhiệm" | Case study + thảo luận |
| 50–70 | 20' | **Checklist an toàn dữ liệu cho doanh nghiệp dầu khí:** phân loại 4 mức (Công khai / Nội bộ / Bí mật / Tối mật) — đây là phân loại theo quy chế nội bộ doanh nghiệp; **cần tách bạch với khái niệm "bí mật nhà nước" theo Luật Bảo vệ bí mật nhà nước số 117/2025/QH15 (hiệu lực 01/3/2026, thay Luật 2018): tài liệu bí mật nhà nước chỉ được soạn thảo, lưu giữ theo đúng quy định của luật và nghị định hướng dẫn — trên máy tính/mạng nội bộ độc lập không kết nối Internet — và luật cấm lợi dụng AI vào hoạt động trái quy định về bí mật nhà nước; vì vậy không đưa tài liệu bí mật nhà nước vào bất kỳ công cụ AI nào kết nối Internet, kể cả bản doanh nghiệp. Đây là ranh giới pháp lý, khác hẳn mức "Tối mật" theo quy chế nội bộ ở bài tập tiếp theo**; quy tắc KHÔNG đưa dữ liệu mật vào AI công cộng; giải pháp thực tế: dữ liệu từ mức Nội bộ trở lên chỉ đưa vào công cụ AI doanh nghiệp do đơn vị cấp và quản trị — tài khoản cá nhân, dù đã tắt training, vẫn không đạt chuẩn cho loại dữ liệu này; với dữ liệu cần dùng thử trong lớp, dùng kỹ thuật khử định danh (tách/thay thế thông tin nhạy cảm) trước khi đưa vào AI. **Với dữ liệu cá nhân dùng thật ngoài phạm vi lớp học (bài làm, bảng điểm, hồ sơ sinh viên...): nhắc quy trình cần qua bộ phận pháp chế/an ninh thông tin đánh giá trước khi đưa vào bất kỳ công cụ AI nào, theo Luật Bảo vệ dữ liệu cá nhân 2025 — không chỉ dựa vào phân loại 4 mức nội bộ.** Nối lại case chấm đồ án đã demo: báo cáo được khử thông tin sinh viên trước khi tải lên, mục 1–5 của phiếu để giáo viên tự điền, Memory của Project tắt khi chạy dữ liệu bài làm. Nhắc riêng: Cowork vừa xem sáng nay có quyền truy cập file thật + internet — rủi ro dữ liệu cao hơn Project, tuyệt đối không trỏ vào thư mục chứa dữ liệu mật khi chưa qua đào tạo an toàn riêng | Trình bày + demo khử mật |
| 70–90 | 20' | **Bài tập 4.1 — Phân loại 8 tình huống:** học viên giơ thẻ ✅/🚫 cho từng tình huống (VD: "Đưa hợp đồng mua bán khí chưa ký vào ChatGPT free để tóm tắt" → 🚫). Tranh luận các tình huống gây chia rẽ ý kiến | Trò chơi cả lớp |
| 90–100 | 10' | **Giải lao** | |
| 100–120 | 20' | **Demo Gemini Notebook** (trước đây NotebookLM) — hỏi đáp theo nguồn đã nạp (RAG): nạp 4 nguồn mẫu chủ đề "họp hiệu quả" (PDF, video YouTube, DOCX, file ghi âm — nguồn công khai/dựng minh họa), hỏi đáp có trích dẫn nguồn và kiểm tra trích dẫn; lưu câu trả lời hay vào Knowledge Base của Claude Project; làm rõ khác biệt với Claude Projects và khi nào dùng công cụ nào | Demo |
| 120–140 | 20' | **Hoàn thiện sản phẩm:** các nhóm áp dụng self-check + checklist an toàn để nâng cấp Project của mình lần cuối. Giảng viên chấm bản chính thức theo Rubric | Thực hành nhóm |
| 140–160 | 20' | **Quay lại Bảng Mục Tiêu:** tick từng note-dán, mục nào chưa giải quyết thì giải đáp tại chỗ hoặc hướng dẫn hướng tự học. **"5 bước bắt đầu ngay khi về đơn vị"** (handout mang về; bước 3–4 dùng Siêu trợ lý) | Tổng kết tương tác |
| 160–180 | 20' | Q&A mở + **Cam kết hành động:** mỗi học viên viết 1 câu "Trong 7 ngày tới, tôi sẽ dùng AI Assistant của nhóm để ___" dán lên bảng. Lời nhắn cuối: *"Hành trình vạn dặm bắt đầu từ một bước chân — và bước chân đó các anh chị đã đi hôm nay: mang về đơn vị một trợ lý AI do chính tay mình xây."* | Cam kết + bế giảng |

### Bài tập 4.1 — 8 tình huống phân loại dữ liệu (đáp án cho giảng viên)

*(Không đổi so với bản gốc. Lưu ý khi giảng: tình huống 5 là ✅ vì dùng tài khoản doanh nghiệp (Team); lớp này dùng tài khoản cá nhân, nên hỏi thêm "nếu là tài khoản cá nhân của thầy cô thì sao?" → với dữ liệu Nội bộ, đáp án đổi thành 🚫.)*

| # | Tình huống | Đáp án |
|---|---|---|
| 1 | Dùng Claude viết lại thông cáo báo chí đã công bố cho dễ đọc hơn | ✅ Công khai |
| 2 | Đưa hợp đồng mua bán khí chưa ký vào ChatGPT bản free để tóm tắt | 🚫 Bí mật + công cụ free |
| 3 | Nhờ AI soát chính tả công văn nội bộ đã xóa tên người, số hợp đồng | ✅ Đã khử định danh |
| 4 | Upload bản đồ vị trí giếng khoan thăm dò mới vào AI để phân tích | 🚫 Tối mật |
| 5 | Dùng Claude Project (tài khoản Team) soạn khung chương trình đào tạo nội bộ | ✅ Nội bộ + công cụ doanh nghiệp |
| 6 | Đưa danh sách lương nhân viên vào AI để "nhờ tính giúp cho nhanh" | 🚫 Dữ liệu cá nhân nhạy cảm |
| 7 | Hỏi AI kiến thức chung về quy chuẩn API 650 cho bồn chứa | ✅ Kiến thức công khai — nhưng phải kiểm chứng lại (nối về hallucination) |
| 8 | Dán biên bản họp HĐQT vào AI để viết tóm tắt gửi lãnh đạo | 🚫 Bí mật |

### Công cụ & tài liệu chuẩn bị

- Case study minh họa hallucination (kịch bản demo đã dựng sẵn, ghi rõ là minh họa)
- Thẻ ✅/🚫 phát mỗi học viên; slide 8 tình huống
- Bộ 4 nguồn mẫu cho demo Gemini Notebook (PDF, link YouTube, DOCX, file ghi âm — chủ đề "họp hiệu quả", nguồn công khai hoặc dựng minh họa)
- Slide 2 sự cố thật (Samsung 2023; lỗi ChatGPT ngày 20/03/2023) — kiểm lại nguồn trước khi chiếu
- Handout: Checklist an toàn dữ liệu + "5 bước bắt đầu"
- **Giảng viên tự rà soát lại trước ngày dạy:** hiệu lực và nội dung của Luật Bảo vệ dữ liệu cá nhân 2025, Luật Bảo vệ bí mật nhà nước số 117/2025/QH15, Luật Trí tuệ nhân tạo 2025 và các nghị định hướng dẫn — khung pháp lý này còn đang được cụ thể hóa bằng nghị định/thông tư, không trả lời học viên từ trí nhớ nếu đề cương được dùng lại sau nhiều tháng

### Tiêu chí đánh giá hoạt động

- Bài tập 8 tình huống: học viên đúng ≥6/8 (CLO6)
- Project cuối được nâng cấp có tối thiểu 1 cơ chế self-check (CLO5)

---

# PHẦN 4 — MA TRẬN ĐÁNH GIÁ

*(Không đổi so với bản gốc)*

## 4.1. Mapping CLO — Hoạt động đánh giá

| CLO | Hoạt động đánh giá | Buổi | Hình thức | Trọng số |
|---|---|---|---|---|
| CLO1 | Quiz recap + phát hiện hallucination trong demo | 1, 3 | Quan sát + quiz | 10% |
| CLO2 | Thực hành 1.1 — Prompt CRISP đối chứng | 1 | Phiếu giấy + kiểm tra trực tiếp | 15% |
| CLO3 | Sơ đồ quy trình A3 (gate + fallback đánh dấu đúng) | 2, 3 | Chấm sơ đồ nhóm | 15% |
| CLO4 | **Sản phẩm cuối khóa: Claude Project hoạt động** | 3, 4 | Rubric bên dưới | **40%** |
| CLO5 | Phản biện chéo + cơ chế self-check trong Project | 3, 4 | Quan sát + chấm Project | 10% |
| CLO6 | Bài tập 8 tình huống phân loại dữ liệu | 4 | Đúng ≥6/8 | 10% |

**Điều kiện hoàn thành khóa học:** tổng ≥70% VÀ sản phẩm cuối khóa đạt tối thiểu mức "Đạt" ở cả 5 tiêu chí Rubric.

> **Ghi chú (mô hình lai Siêu trợ lý):** CLO3 chấm trên sơ đồ A3 nhóm tự vẽ trước khi chạy Siêu trợ lý; sơ đồ do Siêu trợ lý xuất chỉ dùng để đối chiếu, không tính vào điểm CLO3.

## 4.2. Rubric sản phẩm cuối khóa — AI Assistant (Claude Project)

*(Không đổi so với bản gốc)*

Thang 4 mức mỗi tiêu chí: **Xuất sắc (4) — Tốt (3) — Đạt (2) — Chưa đạt (1)**

| Tiêu chí | Xuất sắc (4) | Tốt (3) | Đạt (2) | Chưa đạt (1) |
|---|---|---|---|---|
| **1. Cấu trúc quy trình** (CLO3) | ≥4 bước rõ ràng, đầu vào/đầu ra từng bước được định nghĩa, có nhánh xử lý ngoại lệ | 3–4 bước rõ ràng, đầu ra từng bước được định nghĩa | 3 bước, trình tự hợp lý nhưng đầu ra từng bước còn mơ hồ | Các bước lẫn lộn, AI làm gộp không theo trình tự |
| **2. Cổng xác nhận (Gate)** (CLO4) | AI dừng đúng mọi gate, hỏi xác nhận bằng câu rõ ràng, thử "vượt gate" 1 cách không qua được | AI dừng đúng mọi gate khi test thông thường | Có ít nhất 1 gate và AI dừng được ở gate đó | Không có gate, hoặc AI tự chạy hết quy trình không chờ xác nhận |
| **3. Xử lý thiếu thông tin (Fallback)** (CLO4) | Phân biệt thông tin bắt buộc (hỏi lại) vs không bắt buộc (dùng mặc định có ghi chú); test bỏ trống nhiều kiểu đều xử lý đúng | AI hỏi lại đúng khi thiếu thông tin bắt buộc | AI có hỏi lại khi thiếu thông tin trong kịch bản test chuẩn | AI tự bịa thông tin thiếu để làm tiếp |
| **4. Kiểm soát đầu ra** (CLO4, CLO5) | Đầu ra đúng template 100% qua ≥3 lần chạy; có cơ chế self-check; nội dung từ Knowledge Base được ưu tiên và kiến thức ngoài được đánh dấu | Đầu ra đúng template, nhất quán qua 2 lần chạy | Đầu ra theo template nhưng còn dao động nhỏ giữa các lần chạy | Không có template, mỗi lần chạy một kiểu |
| **5. Tính khả dụng thực tế** | Dùng được ngay cho công việc thật của phòng ban; đồng nghiệp chưa học khóa này vẫn dùng được nhờ hướng dẫn trong Instructions | Dùng được cho công việc thật với chút chỉnh sửa | Chạy đúng với tình huống mẫu trong lớp | Chỉ là chatbot hỏi đáp chung, không gắn quy trình nghiệp vụ thật |

> **Ghi chú:** hạ ngưỡng "Xuất sắc" ở tiêu chí 2 từ "thử vượt gate 2 cách" xuống "1 cách" so với bản gốc — mức 2 cách đòi hỏi kỹ năng adversarial prompting cao hơn thực tế 12 giờ đào tạo cho phép.

---

# PHẦN 5 — TÀI LIỆU HỖ TRỢ

## 5.1. Danh sách tài liệu phát tay

| # | Tài liệu | Phát ở buổi | Ghi chú |
|---|---|---|---|
| 1 | Phiếu CRISP (khung 5 ô điền tay) | 1 | Mỗi người 2 tờ |
| 2 | Bản đồ công cụ AI 1 trang | 1 | Claude / ChatGPT / Gemini / Gemini Notebook |
| 3 | Poster "7 Nguyên tắc thiết kế quy trình AI" + câu prompt mẫu | 2 | In màu, khuyến khích dán tại bàn làm việc |
| 4 | Phiếu Thiết Kế Quy Trình (A3) | 2, 3 | Khung: Bước / Đầu vào / Đầu ra / Gate / Fallback |
| 5 | Template Custom Instructions chuẩn (bản in + file) | 3 | Xem 5.2 |
| 6 | Rubric sản phẩm cuối khóa | 3 | Phát TRƯỚC khi thực hành |
| 7 | Checklist an toàn dữ liệu 4 mức | 4 | Kèm 8 tình huống + đáp án |
| 8 | "5 bước bắt đầu ngay khi về đơn vị/bộ môn" | 4 | 1 trang mang về |
| 9 | Prompt Siêu trợ lý (file `.md`, bản 08/10) + hướng dẫn Chương 3 của ebook | 2 (bài về nhà), 3 | Bản mềm qua LMS; mỗi học viên tự tạo Project Siêu trợ lý |
| 10 | Ebook khóa học trên LMS (4 chương theo SCQA + bài test 3 mức) | Từ Buổi 1 | Học liệu tự học và ôn tập sau từng buổi |

## 5.2. Template Custom Instructions chuẩn (phát cho học viên)

*(Không đổi so với bản gốc)*

```
# VAI TRÒ
Bạn là trợ lý [tên nghiệp vụ] của [phòng ban]. Bạn là cộng sự hỗ trợ,
KHÔNG phải người ra quyết định. Mọi quyết định cuối cùng thuộc về tôi.

# KHỞI TẠO BẮT BUỘC
Khi bắt đầu phiên làm việc mới, hãy:
1. Đọc toàn bộ tài liệu trong Knowledge Base
2. Tóm tắt ngắn quy trình bạn sẽ thực hiện để tôi xác nhận
3. Chỉ bắt đầu Bước 1 sau khi tôi đồng ý

# QUY TRÌNH (thực hiện TUẦN TỰ, không bỏ bước, không gộp bước)
Bước 1: [tên bước] — Đầu vào: [...] — Đầu ra: [...]
Bước 2: [tên bước] — Đầu vào: [...] — Đầu ra: [...]
Bước 3: ...

# CỔNG XÁC NHẬN
Sau khi hoàn thành mỗi bước, DỪNG LẠI và hỏi:
"Bạn xác nhận kết quả Bước [X] và cho phép chuyển sang Bước [X+1] chứ?"
Tuyệt đối không tự thực hiện bước tiếp theo khi chưa có xác nhận.

# XỬ LÝ THIẾU THÔNG TIN
- Thông tin BẮT BUỘC còn thiếu: [liệt kê] → hỏi tôi, không được tự giả định
- Thông tin KHÔNG bắt buộc còn thiếu → dùng mặc định: [liệt kê]
  và ghi chú rõ "[ĐÃ DÙNG GIÁ TRỊ MẶC ĐỊNH]"

# NGUỒN TIN CẬY
- Ưu tiên tuyệt đối: tài liệu trong Knowledge Base
- Kiến thức chung ngoài tài liệu: phải đánh dấu [CẦN KIỂM CHỨNG]
- Không được bịa số liệu, tên văn bản, số hiệu quy chuẩn

# TEMPLATE ĐẦU RA
Mọi kết quả cuối cùng trình bày theo đúng cấu trúc:
[dán cấu trúc chuẩn của phòng ban]

# TỰ KIỂM TRA
Trước khi trả kết quả cuối, rà lại theo checklist:
□ Đúng template? □ Có mục nào bịa/thiếu nguồn? □ Đã qua đủ các gate?

# KẾT THÚC PHIÊN
Hỏi tôi: "Bước nào trong quy trình cần điều chỉnh cho lần sau?"
```

## 5.3. Handout "5 bước bắt đầu ngay khi về đơn vị/bộ môn"

*(Cập nhật 26/10/2026: bước 3–4 dùng Siêu trợ lý; các bước khác không đổi)*

1. **Ngày 1–2:** Chọn 1 quy trình lặp lại nhiều nhất, ít nhạy cảm nhất ở phòng bạn. Đừng chọn việc khó nhất — chọn việc *chán nhất*.
2. **Ngày 3:** Vẽ quy trình đó ra giấy theo Phiếu Thiết Kế (bước – gate – fallback). Chưa mở máy tính vội.
3. **Ngày 4–5:** Mô tả quy trình đã vẽ cho Siêu trợ lý (đã khử thông tin mật) để nhận Custom Instructions + hướng dẫn thiết lập; tạo Claude Project, upload 1–2 tài liệu mẫu (đã khử thông tin mật theo checklist) và đối chiếu Custom Instructions với Template chuẩn.
4. **Ngày 6–7:** Test 3 kịch bản (Siêu trợ lý đã xuất sẵn): chạy xuôi — bỏ trống thông tin — thử vượt gate. Sửa Instructions sau mỗi lần test, có thể nhờ Siêu trợ lý xuất lại đúng phần bị ảnh hưởng.
5. **Tuần 2:** Dùng thật cho 1 việc thật, cho 1 đồng nghiệp dùng thử, ghi lại điều cần cải thiện. Nhớ nguyên tắc vàng: **Bạn là Leader, AI là Cộng sự — AI viết nháp, người ký chịu trách nhiệm.**

## 5.4. Checklist chuẩn bị của giảng viên trước khóa học

- [ ] Xác nhận mỗi học viên có tài khoản Claude cá nhân (Free/Pro), test đăng nhập; nhắc cả lớp chỉ đưa dữ liệu công khai hoặc dữ liệu mẫu đã khử định danh vào Claude và Gemini Notebook *(đã chốt dùng tài khoản cá nhân — nội dung Buổi 1 và Buổi 4 đã viết theo giả định này)*
- [ ] Setup sẵn Claude Project "Chấm đồ án sinh viên" (Custom Instructions `01` + 4 file KB `02`–`05`) từ bộ học liệu, 3 Conversation mở sẵn, 3 file DA-01/02/03.docx, **tắt Memory**, test đủ 4 kịch bản (`06`) và chụp ảnh dự phòng trước ngày dạy
- [ ] Cài Claude Desktop trên máy giảng viên, xác nhận Cowork chạy được, bật code execution, cài sẵn và test Skill chấm đồ án (`09`) với thư mục `Demo-Cowork-ChamDoAn/` trước ngày dạy; Cowork đã gộp vào ứng dụng Claude nên kiểm tra giao diện thật
- [ ] Tạo sẵn Project Siêu trợ lý (prompt bản 08/10), chạy thử 1 lượt phỏng vấn → xuất đủ 7 phần; kiểm tra cách xem sơ đồ mermaid (Artifact hoặc mermaid.live); gửi file prompt + Chương 3 ebook cho học viên trước khi Buổi 2 kết thúc
- [ ] Chuẩn bị bộ tài liệu mẫu đã khử mật cho 4 tình huống thực hành (dự phòng nhóm không mang tài liệu)
- [ ] In tài liệu phát tay #1–#8 (#9–#10 gửi bản mềm qua LMS); chuẩn bị Bảng Mục Tiêu A0, note-dán, thẻ ✅/🚫, giấy A3, sticker 🔒❓
- [ ] Gửi trước cho đầu mối đơn vị tổ chức: yêu cầu học viên mang laptop + nghĩ sẵn 1 quy trình của đơn vị/bộ môn muốn tự động hóa
