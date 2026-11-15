# SOP: Quy Tắc Điểm Danh Tự Động LMS Hub

Tài liệu này ghi nhận chi tiết cơ chế và điều kiện để hệ thống LMS Hub tự động công nhận trạng thái "Có mặt" (Điểm danh thành công) cho sinh viên trong từng buổi học.

---

## 1. Bản chất cốt lõi (Core Logic)

Hệ thống LMS Hub **không áp dụng hình thức điểm danh thụ động** (như gọi tên hay quét mã QR đơn thuần). Thay vào đó, việc điểm danh được kích hoạt dựa trên **sự chủ động học tập và phản hồi đa chiều** của sinh viên.

Trạng thái **Có mặt (Attended / ✅ Có mặt)** được tính toán tự động khi sinh viên thỏa mãn **đồng thời cả 2 điều kiện bắt buộc**:

$$\text{Có mặt} = \text{Đã tải Slide (kèm Feedback có bình luận)} \land \text{Hoàn thành Quiz } (\text{Điểm} = 10 \lor \text{Làm đủ } 5 \text{ lần})$$

---

## 2. Chi tiết 2 điều kiện bắt buộc

### Điều kiện 1: Tải Slide bài giảng (Slide Download)
* **Quy tắc bảo vệ Slide:** Sinh viên không thể tải slide trực tiếp. Nút "Tải Slide" bị mờ và khóa cho đến khi sinh viên hoàn thành bước nộp đánh giá buổi học (Feedback).
* **Yêu cầu nộp Feedback:**
  * Sinh viên kéo xuống chân trang bài học (`/course/lesson/:id`).
  * Trả lời 3 câu hỏi khảo sát mức độ (1 đến 5 sao): Độ hiểu bài (Understanding), Tốc độ giảng dạy (Pace), Độ hữu ích (Usefulness).
  * **Bắt buộc nhập bình luận (Comment):** Không được để trống. Đây là điều kiện tiên quyết để hệ thống mở khóa slide.
* **Cơ chế ghi nhận:**
  * Nội dung đánh giá được lưu ẩn danh vào bảng `session_feedback` với `anon_hash` mã hóa từ `student_id` và `session_id`, bảo đảm tuyệt đối tính ẩn danh cho sinh viên.
  * Ngay khi sinh viên nhấn nút tải slide hợp lệ (`GET /api/courses/sessions/:id/slide`), hệ thống ghi nhận một dòng vào bảng `attendance_log` gồm: `student_id`, `student_name`, `session_id`, `checked_in_at` (thời điểm tải slide).

### Điều kiện 2: Hoàn thành bài Quiz buổi học (Quiz Completion)
* **Quy định làm Quiz:**
  * Sinh viên truy cập vào mục Quiz của buổi học tương ứng.
  * Mỗi sinh viên được phép làm lại tối đa **5 lần** (`attempts <= 5`).
* **Tiêu chí hoàn thành (đạt 1 trong 2 trường hợp):**
  * **Trường hợp A (Xuất sắc):** Đạt điểm tuyệt đối **10/10 điểm** (`maxScore >= 10`).
  * **Trường hợp B (Kiên trì, nỗ lực tối đa):** Nếu chưa đạt điểm 10, sinh viên phải làm đủ **5 lần** (`attempts >= 5`).
* **Ý nghĩa sư phạm:** Đảm bảo mọi sinh viên hoặc là nắm vững kiến thức để làm đúng hết, hoặc thể hiện thái độ học tập kiên trì, không bỏ cuộc giữa chừng.

---

## 3. Mã nguồn triển khai (Implementation Reference)

### 3.1. API kiểm tra điểm danh của sinh viên (`GET /api/feedback/my-attendance`)
File: `core/server/routes/feedback.js`
```javascript
// Attended = Slide Downloaded AND Quiz Completed
const attendedSessions = downloadedSessions.filter(sid => 
  quizStatus[sid] && (quizStatus[sid].maxScore >= 10 || quizStatus[sid].attempts >= 5)
);
res.json(attendedSessions);
```

### 3.2. API tổng hợp điểm danh cho Giảng viên (`GET /api/feedback/admin/attendance`)
File: `core/server/routes/feedback.js`
```javascript
// Chỉ ghi nhận sinh viên có mặt nếu thỏa mãn Quiz requirement
const qs = quizStatus[a.student_id]?.[sid];
if (!qs || (qs.maxScore < 10 && qs.attempts < 5)) return;

grouped[sid].students.push({
  student_id: a.student_id,
  student_name: a.student_name,
  checked_in_at: a.checked_in_at // Thời điểm tải slide
});
```

### 3.3. Hiển thị trên giao diện người dùng (UI)
* **Phía Sinh viên (`core/client/src/pages/course.js`):**
  * Buổi học đạt đủ 2 điều kiện: Hiển thị badge xanh `✅ Có mặt`.
  * Buổi học thiếu 1 trong 2 điều kiện: Hiển thị badge đỏ `❌ Vắng`.
* **Phía Giảng viên (`core/client/src/pages/lesson.js`):**
  * Hiển thị bảng danh sách sinh viên có mặt kèm mốc thời gian điểm danh chính xác tại panel "Điểm danh qua Feedback".

---

## 4. Tóm tắt quy trình sinh viên cần làm mỗi buổi

1. **Bước 1:** Vào học và đọc nội dung bài giảng trên web LMS.
2. **Bước 2:** Cuộn xuống cuối trang, gửi form Feedback ẩn danh kèm lời nhận xét, góp ý chân thực.
3. **Bước 3:** Nhấn nút **Tải Slide** (hệ thống tự động ghi nhận mốc thời gian điểm danh).
4. **Bước 4:** Vào làm bài **Quiz** của buổi học cho đến khi đạt điểm 10 hoặc hoàn thành đủ 5 lượt làm bài.
5. **Hoàn tất:** Kiểm tra lại trang Khóa học, thấy hiển thị `✅ Có mặt`.
