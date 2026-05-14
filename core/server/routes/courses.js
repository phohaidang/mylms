import { Router } from 'express';
import { existsSync } from 'fs';
import { join } from 'path';
import { authenticate } from '../middleware/auth.js';

export function createCourseRouter(options) {
  const router = Router();
  
  // Lấy config từ options hoặc từ app.locals
  const courseConfig = options.courseConfig || { meta: {}, sessions: [] };

  router.get('/sessions', authenticate, (req, res) => {
    // Ưu tiên dùng config truyền vào
    const config = courseConfig;
    res.json({
      course: {
        code: config.meta?.code || process.env.COURSE_CODE || 'ITS717',
        name: config.meta?.name || process.env.COURSE_NAME || 'Thương mại Xã hội',
        description: config.meta?.description || 'Học phần Thương mại Xã hội',
        ...config.meta
      },
      sessions: config.sessions || []
    });
  });

  router.get('/sessions/:id', authenticate, (req, res) => {
    const config = courseConfig;
    const contentDir = options.contentDir || req.app.locals.contentDir;
    const id = parseInt(req.params.id);
    const session = config.sessions.find(s => s.id === id);
    
    if (!session) {
      return res.status(404).json({ error: 'Không tìm thấy buổi học' });
    }

    const lessonsDir = join(contentDir, 'lessons');
    const slidesDir = join(contentDir, 'slides');
    const paddedId = id.toString().padStart(2, '0');

    res.json({
      ...session,
      hasLesson: existsSync(join(lessonsDir, `Buoi_${paddedId}.html`)),
      hasSlide: existsSync(join(slidesDir, `Buoi_${paddedId}.pdf`))
    });
  });

  return router;
}
