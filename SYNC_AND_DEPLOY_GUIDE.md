# 📚 Cẩm Nang Đồng Bộ và Triển Khai LMS Hub (Local & Production)

Tài liệu này hướng dẫn chi tiết cách đồng bộ mã nguồn (Sync) từ lõi chung (`core/`) sang toàn bộ 7 lớp học, cách chạy thử nghiệm ở môi trường máy cá nhân (Local), và quy trình triển khai lên môi trường thực tế (Production Live) thông qua GitHub và Vercel.

---

## 🔒 1. Quản lý File và Bảo Mật (GitHub & .gitignore)

Để tránh rò rỉ thông tin nhạy cảm của lớp học (như mật khẩu, thông tin học viên, khóa bảo mật Google Service Account), dự án đã cấu hình nghiêm ngặt các tệp tin được phép đưa lên GitHub thông qua file `.gitignore`.

### 🚫 Các file KHÔNG ĐƯỢC PHÉP và ĐÃ ĐƯỢC BỎ QUA khi push lên GitHub:
*   **`.env`**: Nằm trong từng thư mục lớp (ví dụ: `courses/social-commerce/D01/.env`). File này chứa thông tin kết nối Google Sheets (`GOOGLE_SHEETS_ID`) và khóa riêng tư (`GOOGLE_PRIVATE_KEY`).
*   **`_tmp_key_import.json` hoặc `_tmp_*.json`**: Các file khóa tạm thời chứa thông tin xác thực Google Cloud.
*   **`node_modules/`**: Các thư viện dependencies cài đặt qua npm.
*   **`dist/`**: Thư mục chứa mã nguồn client sau khi build để phân phối (Vercel sẽ tự động build lại trên cloud).
*   **`data/_mock_db.json`**: Cơ sở dữ liệu mock ở chế độ offline cục bộ.
*   **`*.log`**: Nhật ký chạy server cục bộ.

### ✅ Các file CẦN đưa lên GitHub:
*   Thư mục **`core/`**: Chứa toàn bộ nhân logic (Server, SPA Client, Scripts) dùng chung cho toàn bộ các lớp.
*   Thư mục **`courses/`**: Chứa cấu hình đề cương học tập (`course-config.json`), nội dung học liệu (`content/lessons/`, `ebook/`, `exams/`, `questions/`) và danh sách học viên (`roster.md`) của mỗi lớp.
*   Các file cấu hình deploy: `vercel.json`, `vite.config.js`, `package.json`, `index.html`, `main.js`, `router.js`, `api.js` của mỗi lớp (chứa cấu hình rỗng hoặc config chung).

---

## 🔄 2. Quy Trình Đồng Bộ Mã Nguồn (Sync Core to Classes)

Khi bạn thực hiện bất kỳ chỉnh sửa nào ở nhân chung **`core/`** (ví dụ: bổ sung tính năng Nhật ký buổi học ở `core/client/src/pages/journal.js` hoặc sửa API ở `core/server/routes/journal.js`), bạn **phải chạy lệnh đồng bộ** để tự động cập nhật code mới nhất sang tất cả các lớp.

Mã nguồn đồng bộ được xử lý tự động qua script `core/scripts/sync-deploy.js`.

### 📌 Lệnh 1: Đồng bộ cho một lớp học cụ thể (để test trước)
```bash
# Cú pháp: npm run sync -- <course-slug> <class-id>
# Ví dụ: Đồng bộ lớp D01 môn Social Commerce
npm run sync -- social-commerce D01
```

### 📌 Lệnh 2: Liệt kê danh sách toàn bộ các lớp học đang hoạt động
```bash
npm run sync:list
```

### 📌 Lệnh 3: Đồng bộ hàng loạt cho TẤT CẢ 7 LỚP HỌC (Trước khi Git push)
```bash
npm run sync:all
```
*Lưu ý: Lệnh này sẽ tự động dọn dẹp các thư mục `_sync/server/`, `pages/`, `styles/`, `main.js`, `router.js`, `api.js` và `content/` ở từng lớp học, sau đó sao chép phiên bản mới nhất từ `core/` sang.*

---

## 💻 3. Chạy và Thử Nghiệm Dưới Local (Offline/Dev Mode)

Môi trường local dùng để lập trình và kiểm thử nhanh các tính năng trước khi đưa lên production.

### Bước 1: Đồng bộ mã nguồn mới nhất
```bash
# Đứng tại thư mục gốc lms-hub
npm run sync social-commerce D01
```

### Bước 2: Di chuyển vào thư mục lớp học cần chạy thử
```bash
# Chú ý: TUYỆT ĐỐI không dùng lệnh cd thông qua AI, bạn hãy tự gõ lệnh cd trên terminal của mình:
cd courses/social-commerce/D01
```

### Bước 3: Cài đặt thư viện dependencies (Nếu có thư viện mới)
```bash
npm install
```

### Bước 4: Khởi động hệ thống local song song
Mở hai cửa sổ terminal tại thư mục lớp (`courses/social-commerce/D01`):

*   **Terminal 1 (Chạy Backend Server):**
    ```bash
    npm run server
    ```
    *Cổng chạy mặc định: `http://localhost:3010`*
*   **Terminal 2 (Chạy Vite Client Dev Server):**
    ```bash
    npm run client
    ```
    *Cổng chạy mặc định: `http://localhost:5173` (hoặc cổng được Vite cấp)*

### Bước 5: Kiểm tra
Truy cập `http://localhost:5173` để trải nghiệm trực quan.

---

## ☁️ 4. Triển Khai Lên Môi Trường Production Live (Vercel)

Sau khi kiểm tra local hoạt động hoàn hảo, thực hiện quy trình sau để đưa code lên môi trường production live cho sinh viên sử dụng.

### Bước 1: Thực hiện đồng bộ toàn diện cho tất cả các lớp
Đứng tại thư mục gốc `lms-hub`, chạy:
```bash
npm run sync:all
```

### Bước 2: Commit và Push mã nguồn lên GitHub
Sử dụng các lệnh Git tại thư mục gốc để đẩy các chỉnh sửa dùng chung của `core/` và bản build cập nhật của các lớp lên kho chứa:
```bash
git add .
git commit -m "feat: integrate premium session journal feature across all classes"
git push origin main
```

### Bước 3: Tự động deploy qua Vercel CI/CD
*   Hệ thống Vercel đã được cấu hình liên kết với kho GitHub này.
*   Ngay khi bạn `git push`, Vercel sẽ tự động phát hiện các lớp thay đổi, kích hoạt trình build `vite build` ngay trên serverless, và cập nhật trực tiếp lên các domain live của học viên (Ví dụ: `tmxh-252-d01.vercel.app`).
*   **Kiểm tra trạng thái:** Bạn có thể đăng nhập vào bảng điều khiển Vercel của mình để xem tiến trình build của từng lớp.

---

## 💡 Mẹo Sử Dụng Thực Tế (Tips & Tricks)

1.  **Chế độ Mock Offline:** Nếu không muốn kết nối Google Sheets thực tế khi code ở local, bạn chỉ cần tạm thời bỏ biến `GOOGLE_SHEETS_ID` trong file `.env` của lớp đó (ví dụ đổi tên thành `_GOOGLE_SHEETS_ID`). Backend sẽ tự động lưu trữ dữ liệu offline vào tệp `data/_mock_db.json`.
2.  **Khởi động lại Server:** Mỗi khi bạn chỉnh sửa file cấu hình môi trường `.env` hoặc file cấu hình môn học `course-config.json` ở local, bạn **bắt buộc phải nhấn Ctrl + C** và chạy lại `npm run server` thì cấu hình mới được nạp lại.
3.  **Khắc phục lỗi CORS/Proxy:** Hãy chắc chắn cổng backend trong file `.env` khớp với proxy khai báo trong `vite.config.js` (Mặc định là cổng `3010`).
