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

// Helper: Tìm file slide PDF hoặc file bài giảng motion HTML
function resolveSlideOrMotion(contentDir, paddedId) {
  const pdfPath = join(contentDir, 'slides', `Buoi_${paddedId}.pdf`);
  if (existsSync(pdfPath)) return { path: pdfPath, type: 'pdf' };

  const slideHtml = join(contentDir, 'slides', `Buoi_${paddedId}.html`);
  if (existsSync(slideHtml)) return { path: slideHtml, type: 'html' };

  const lessonHtml = join(contentDir, 'lessons', `Buoi_${paddedId}.html`);
  if (existsSync(lessonHtml)) return { path: lessonHtml, type: 'html' };

  return null;
}

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
  const slideInfo = resolveSlideOrMotion(contentDir, paddedId);

  res.json({
    ...session,
    hasLesson: existsSync(join(lessonsDir, `Buoi_${paddedId}.html`)),
    hasTeacherLesson: existsSync(join(teacherDir, `Buoi_${paddedId}.html`)),
    hasSlide: !!slideInfo,
    slideType: slideInfo?.type || null
  });
});

/**
 * GET /api/courses/sessions/:id/slide
 * Secure slide download endpoint (hoặc file motion HTML)
 */
router.get('/sessions/:id/slide', authenticate, async (req, res) => {
  const { contentDir } = req.app.locals;
  const id = parseInt(req.params.id);
  const paddedId = id.toString().padStart(2, '0');
  const slideInfo = resolveSlideOrMotion(contentDir, paddedId);

  if (!slideInfo) {
    return res.status(404).json({ error: 'Bài giảng / Slide không tồn tại' });
  }

  const sendFileWithAttachment = () => {
    const filename = slideInfo.type === 'html' ? `Buoi_${paddedId}_Motion.html` : `Buoi_${paddedId}_Slide.pdf`;
    res.setHeader('Content-Disposition', `attachment; filename="${filename}"`);
    if (slideInfo.type === 'html') {
      res.setHeader('Content-Type', 'text/html; charset=utf-8');
    } else {
      res.setHeader('Content-Type', 'application/pdf');
    }
    return res.sendFile(slideInfo.path);
  };

  // Admin/Teacher can always download
  if (req.user.role === 'admin' || req.user.role === 'teacher') {
    return sendFileWithAttachment();
  }

  // Student logic
  const anonHash = Buffer.from(req.user.student_id + '_session_' + id).toString('base64');
  try {
    const feedback = await db.findOne('session_feedback', f => f.anon_hash === anonHash);
    
    if (!feedback || !feedback.comment || feedback.comment.trim().length === 0) {
      return res.status(403).json({ error: 'Vui lòng nộp đánh giá có kèm bình luận để tải bài giảng' });
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

    return sendFileWithAttachment();
  } catch (err) {
    console.error('Slide download error:', err);
    res.status(500).json({ error: 'Lỗi kiểm tra quyền tải bài giảng' });
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

