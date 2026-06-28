import { Router } from 'express';
import { existsSync, readFileSync } from 'fs';
import { join } from 'path';
import { authenticate, adminOnly } from '../middleware/auth.js';
import { v4 as uuidv4 } from 'uuid';
import db from '../services/sheets.js';

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
    hasSlide: existsSync(join(contentDir, 'slides', `Buoi_${paddedId}.pdf`))
  });
});

/**
 * GET /api/courses/sessions/:id/slide
 * Secure slide download endpoint
 */
router.get('/sessions/:id/slide', authenticate, async (req, res) => {
  const { contentDir } = req.app.locals;
  const id = parseInt(req.params.id);
  const paddedId = id.toString().padStart(2, '0');
  const slidePath = join(contentDir, 'slides', `Buoi_${paddedId}.pdf`);

  if (!existsSync(slidePath)) {
    return res.status(404).json({ error: 'Slide không tồn tại' });
  }

  // Admin/Teacher can always download
  if (req.user.role === 'admin' || req.user.role === 'teacher') {
    return res.sendFile(slidePath);
  }

  // Student logic
  const anonHash = Buffer.from(req.user.student_id + '_session_' + id).toString('base64');
  try {
    const feedback = await db.findOne('session_feedback', f => f.anon_hash === anonHash);
    
    if (!feedback || !feedback.comment || feedback.comment.trim().length === 0) {
      return res.status(403).json({ error: 'Vui lòng nộp đánh giá có kèm bình luận để tải slide' });
    }

    // Log slide download (used for attendance)
    const now = new Date().toISOString();
    const existingLog = await db.findOne('attendance_log', a => a.student_id === req.user.student_id && a.session_id == id);
    if (!existingLog) {
      await db.append('attendance_log', {
        id: uuidv4(),
        session_id: id,
        student_id: req.user.student_id,
        student_name: req.user.full_name,
        checked_in_at: now
      });
    }

    res.sendFile(slidePath);
  } catch (err) {
    console.error('Slide download error:', err);
    res.status(500).json({ error: 'Lỗi kiểm tra quyền tải slide' });
  }
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

