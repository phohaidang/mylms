import { Router } from 'express';
import { existsSync, readFileSync } from 'fs';
import { join } from 'path';
import { authenticate, adminOnly } from '../middleware/auth.js';

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
  const teacherDir = join(contentDir, 'lessons-teacher');

  res.json({
    ...session,
    hasLesson: existsSync(join(lessonsDir, `Buoi_${paddedId}.html`)),
    hasTeacherLesson: existsSync(join(teacherDir, `Buoi_${paddedId}.html`)),
    hasSlide: false
  });
});

/**
 * GET /api/courses/sessions/:id/teacher-lesson
 * Admin-only: Get full teaching script HTML
 */
router.get('/sessions/:id/teacher-lesson', authenticate, adminOnly, (req, res) => {
  const { contentDir } = req.app.locals;
  const id = parseInt(req.params.id);
  const paddedId = id.toString().padStart(2, '0');
  const teacherFile = join(contentDir, 'lessons-teacher', `Buoi_${paddedId}.html`);

  if (!existsSync(teacherFile)) {
    return res.status(404).json({ error: 'Kịch bản giảng dạy chưa được upload cho buổi này' });
  }

  const html = readFileSync(teacherFile, 'utf-8');
  res.setHeader('Content-Type', 'text/html; charset=utf-8');
  res.send(html);
});

export default router;

