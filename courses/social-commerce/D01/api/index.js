/**
 * LMS Hub — Social Commerce — Lớp D01 (PRODUCTION)
 */
import { config } from 'dotenv';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const D01_DIR = join(__dirname, '..'); // = /var/task/courses/social-commerce/D01

config();

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

export default async function handler(req, res) {
  try {
    const { createApp } = await import('../core/server/index.js');
    
    const app = createApp({ 
      courseDir: D01_DIR,   // Trỏ đúng thư mục D01
      classDir: D01_DIR,
      config: courseConfig
    });
    
    // Debug endpoint để kiểm tra đường dẫn
    app.get('/api/debug-paths', async (req, res) => {
      const { readdirSync, existsSync } = await import('fs');
      const contentDir = app.locals.contentDir;
      let files = [];
      try { files = readdirSync(contentDir); } catch(e) { files = ['ERROR: ' + e.message]; }
      let lessonFiles = [];
      try { lessonFiles = readdirSync(contentDir + '/lessons'); } catch(e) { lessonFiles = ['ERROR: ' + e.message]; }
      res.json({ 
        dirname: __dirname, 
        D01_DIR, 
        cwd: process.cwd(),
        contentDir,
        contentExists: existsSync(contentDir),
        files,
        lessonFiles
      });
    });
    
    return app(req, res);
  } catch (err) {
    res.status(500).json({
      error: 'Server crashed',
      message: err.message,
      stack: err.stack?.split('\n').slice(0, 5)
    });
  }
}
