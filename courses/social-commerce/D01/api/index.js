/**
 * LMS Hub — Social Commerce — Lớp D01 (FINAL INLINE CONFIG)
 */
import { config } from 'dotenv';
import { join } from 'path';

// Load .env
config();

// Dán trực tiếp dữ liệu môn học vào đây để đảm bảo 100% không lỗi nạp file trên Vercel
const courseConfig = {
  "meta": {
    "code": "ITS717",
    "name": "Thương mại Xã hội",
    "description": "Lớp học Social Commerce — ĐH Ngân Hàng TP.HCM",
    "total_sessions": 9,
    "chapters": 9
  },
  "sessions": [
    { "id": 1, "title": "Giới thiệu về Thương mại Xã hội", "topics": "Tổng quan và xu hướng", "chapter": "Chương 1" },
    { "id": 2, "title": "Tâm lý người tiêu dùng trên MXH", "topics": "Hành vi và quyết định mua hàng", "chapter": "Chương 2" },
    { "id": 3, "title": "Xây dựng thương hiệu cá nhân", "topics": "Personal Branding trên nền tảng số", "chapter": "Chương 3" },
    { "id": 4, "title": "Content Marketing cho Social Commerce", "topics": "Kỹ thuật viết và sáng tạo nội dung", "chapter": "Chương 4" },
    { "id": 5, "title": "Video Marketing & Livestream", "topics": "Kỹ năng bán hàng qua video", "chapter": "Chương 5" },
    { "id": 6, "title": "Quảng cáo trên Mạng xã hội", "topics": "Facebook, TikTok Ads cơ bản", "chapter": "Chương 6" },
    { "id": 7, "title": "Social CRM & Chăm sóc khách hàng", "topics": "Quản lý mối quan hệ khách hàng", "chapter": "Chương 7" },
    { "id": 8, "title": "Phân tích dữ liệu Social", "topics": "Đo lường hiệu quả chiến dịch", "chapter": "Chương 8" },
    { "id": 9, "title": "Tổng kết và Seminar", "topics": "Báo cáo cuối kỳ", "chapter": "Chương 9" }
  ]
};

// Import app factory from local core
import { createApp } from '../core/server/index.js';

const rootDir = process.cwd();

const app = createApp({ 
  courseDir: rootDir, 
  classDir: rootDir,
  config: courseConfig // Dùng dữ liệu inline
});

export default app;
