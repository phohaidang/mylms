import { Router } from 'express';
import { existsSync } from 'fs';
import { join } from 'path';
import { authenticate } from '../middleware/auth.js';

const router = Router();

/**
 * GET /api/courses/sessions
 * List all sessions — reads from course-config.json via app.locals
 */
router.get('/sessions', (req, res) => {
  const { courseConfig } = req.app.locals;
  res.json({
    course: {
      code: courseConfig.meta?.code || process.env.COURSE_CODE || 'LMS',
      name: courseConfig.meta?.name || process.env.COURSE_NAME || 'LMS Hub',
      description: courseConfig.meta?.description || '',
      ...courseConfig.meta
    },
    sessions: courseConfig.sessions || []
  });
});

/**
 * GET /api/courses/sessions/:id
 * Get single session metadata
 */
router.get('/sessions/:id', (req, res) => {
  const { courseConfig, contentDir } = req.app.locals;
  const id = parseInt(req.params.id);
  const session = courseConfig.sessions.find(s => s.id === id);
  
  if (!session) {
    return res.status(404).json({ error: 'Không tìm thấy buổi học' });
  }

  const paddedId = id.toString().padStart(2, '0');
  const lessonsDir = join(contentDir, 'lessons');

  res.json({
    ...session,
    hasLesson: existsSync(join(lessonsDir, `Buoi_${paddedId}.html`)),
    hasSlide: false
  });
});

export default router;
