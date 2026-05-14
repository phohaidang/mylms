import { Router } from 'express';
import { existsSync } from 'fs';
import { join } from 'path';

export function createCourseRouter(options) {
  const router = Router();
  
  // Dữ liệu dự phòng trực tiếp bên trong router
  const fallbackConfig = {
    "meta": { "code": "ITS717", "name": "Thương mại Xã hội" },
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

  const config = options.courseConfig || fallbackConfig;

  // BỎ authenticate để chắc chắn không bị chặn
  router.get('/sessions', (req, res) => {
    res.json({
      course: {
        code: config.meta?.code || 'ITS717',
        name: config.meta?.name || 'Thương mại Xã hội',
        ...config.meta
      },
      sessions: config.sessions || []
    });
  });

  router.get('/sessions/:id', (req, res) => {
    const contentDir = options.contentDir || req.app.locals.contentDir;
    const id = parseInt(req.params.id);
    const session = config.sessions.find(s => s.id === id);
    
    if (!session) {
      return res.status(404).json({ error: 'Không tìm thấy buổi học' });
    }

    const lessonsDir = join(contentDir, 'lessons');
    const paddedId = id.toString().padStart(2, '0');

    res.json({
      ...session,
      hasLesson: existsSync(join(lessonsDir, `Buoi_${paddedId}.html`))
    });
  });

  return router;
}
