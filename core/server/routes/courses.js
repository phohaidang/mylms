import { Router } from 'express';
import { existsSync } from 'fs';
import { join } from 'path';
import { authenticate } from '../middleware/auth.js';

const router = Router();

/**
 * GET /api/courses/sessions
 * List all sessions — reads from course-config.json via app.locals
 */
router.get('/sessions', authenticate, (req, res) => {
  const { courseConfig } = req.app.locals;
  res.json({
    course: courseConfig.meta,
    sessions: courseConfig.sessions
  });
});

/**
 * GET /api/courses/sessions/:id
 * Get single session metadata
 */
router.get('/sessions/:id', authenticate, (req, res) => {
  const { courseConfig, contentDir } = req.app.locals;
  const id = parseInt(req.params.id);
  const session = courseConfig.sessions.find(s => s.id === id);
  
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

export default router;
