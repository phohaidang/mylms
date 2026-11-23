import { Router } from 'express';
import { v4 as uuidv4 } from 'uuid';
import db from '../services/sheets.js';
import { authenticate, adminOnly } from '../middleware/auth.js';

const router = Router();

/**
 * POST /api/journal/:sessionId
 * Submit journal entry for a session.
 */
router.post('/:sessionId', authenticate, async (req, res) => {
  try {
    const sessionId = parseInt(req.params.sessionId);
    const { recall_text, questions_text, goal_rating, goal_note, mood } = req.body;

    if (isNaN(sessionId) || sessionId < 1 || sessionId > 9) {
      return res.status(400).json({ error: 'Buổi học không hợp lệ (1-9).' });
    }

    if (!recall_text || recall_text.trim().length < 20) {
      return res.status(400).json({ error: 'Phần viết Active Recall quá ngắn (yêu cầu tối thiểu 20 ký tự).' });
    }

    const rating = parseInt(goal_rating);
    if (isNaN(rating) || rating < 1 || rating > 5) {
      return res.status(400).json({ error: 'Đánh giá mục tiêu phải từ 1 đến 5.' });
    }

    // Check if journal already exists for this session
    const existing = await db.findOne('session_journals', 
      j => j.student_id === req.user.student_id && parseInt(j.session_id) === sessionId
    );

    if (existing) {
      return res.status(409).json({ error: 'Bạn đã viết nhật ký cho buổi học này rồi. Vui lòng sử dụng chức năng cập nhật.' });
    }

    const now = new Date().toISOString();
    const newJournal = {
      id: uuidv4(),
      student_id: req.user.student_id,
      student_name: req.user.full_name,
      session_id: sessionId,
      recall_text: recall_text.trim(),
      questions_text: (questions_text || '').trim(),
      goal_rating: rating,
      goal_note: (goal_note || '').trim(),
      mood: mood || '😐',
      created_at: now,
      updated_at: now
    };

    await db.append('session_journals', newJournal);
    res.status(201).json({ message: 'Lưu nhật ký buổi học thành công!', journal: newJournal });
  } catch (err) {
    console.error('Submit journal error:', err);
    res.status(500).json({ error: 'Lỗi lưu nhật ký' });
  }
});

/**
 * PUT /api/journal/:sessionId
 * Update an existing journal entry.
 */
router.put('/:sessionId', authenticate, async (req, res) => {
  try {
    const sessionId = parseInt(req.params.sessionId);
    const { recall_text, questions_text, goal_rating, goal_note, mood } = req.body;

    if (isNaN(sessionId)) {
      return res.status(400).json({ error: 'Buổi học không hợp lệ.' });
    }

    if (!recall_text || recall_text.trim().length < 20) {
      return res.status(400).json({ error: 'Phần viết Active Recall quá ngắn (yêu cầu tối thiểu 20 ký tự).' });
    }

    const rating = parseInt(goal_rating);
    if (isNaN(rating) || rating < 1 || rating > 5) {
      return res.status(400).json({ error: 'Đánh giá mục tiêu phải từ 1 đến 5.' });
    }

    const now = new Date().toISOString();
    const updated = await db.update('session_journals',
      j => j.student_id === req.user.student_id && parseInt(j.session_id) === sessionId,
      {
        recall_text: recall_text.trim(),
        questions_text: (questions_text || '').trim(),
        goal_rating: rating,
        goal_note: (goal_note || '').trim(),
        mood: mood || '😐',
        updated_at: now
      }
    );

    if (!updated) {
      return res.status(404).json({ error: 'Không tìm thấy nhật ký để cập nhật.' });
    }

    res.json({ message: 'Cập nhật nhật ký thành công!', journal: updated });
  } catch (err) {
    console.error('Update journal error:', err);
    res.status(500).json({ error: 'Lỗi cập nhật nhật ký' });
  }
});

/**
 * GET /api/journal/my
 * Get all journal entries of the current student.
 */
router.get('/my', authenticate, async (req, res) => {
  try {
    const myJournals = await db.find('session_journals', j => j.student_id === req.user.student_id);
    // Sort by session_id ascending
    myJournals.sort((a, b) => parseInt(a.session_id) - parseInt(b.session_id));
    res.json(myJournals);
  } catch (err) {
    console.error('Get my journals error:', err);
    res.status(500).json({ error: 'Lỗi lấy danh sách nhật ký' });
  }
});

/**
 * GET /api/journal/my/:sessionId
 * Get single journal entry for a specific session of the current student.
 */
router.get('/my/:sessionId', authenticate, async (req, res) => {
  try {
    const sessionId = parseInt(req.params.sessionId);
    const journal = await db.findOne('session_journals',
      j => j.student_id === req.user.student_id && parseInt(j.session_id) === sessionId
    );
    if (!journal) {
      return res.status(404).json({ error: 'Chưa viết nhật ký cho buổi học này.' });
    }
    res.json(journal);
  } catch (err) {
    console.error('Get single journal error:', err);
    res.status(500).json({ error: 'Lỗi lấy thông tin nhật ký' });
  }
});

/**
 * GET /api/journal/admin/summary
 * Admin-only: Get aggregated journal statistics per session
 */
router.get('/admin/summary', authenticate, adminOnly, async (req, res) => {
  try {
    const allJournals = await db.getAll('session_journals');
    
    // Group by session
    const summary = {};
    for (let i = 1; i <= 9; i++) {
      summary[i] = {
        session_id: i,
        total_journals: 0,
        avg_rating: 0,
        ratings_sum: 0,
        moods: {}
      };
    }

    allJournals.forEach(j => {
      const sid = parseInt(j.session_id);
      if (summary[sid]) {
        summary[sid].total_journals++;
        const rating = parseInt(j.goal_rating) || 0;
        summary[sid].ratings_sum += rating;
        
        const m = j.mood || '😐';
        summary[sid].moods[m] = (summary[sid].moods[m] || 0) + 1;
      }
    });

    const result = Object.values(summary).map(s => {
      return {
        session_id: s.session_id,
        total_journals: s.total_journals,
        avg_rating: s.total_journals > 0 ? Math.round((s.ratings_sum / s.total_journals) * 10) / 10 : 0,
        moods: s.moods
      };
    });

    res.json(result);
  } catch (err) {
    console.error('Get admin journal summary error:', err);
    res.status(500).json({ error: 'Lỗi tổng hợp dữ liệu nhật ký' });
  }
});

/**
 * GET /api/journal/admin/session/:sessionId
 * Admin-only: Get detailed journal entries for a session
 */
router.get('/admin/session/:sessionId', authenticate, adminOnly, async (req, res) => {
  try {
    const sessionId = parseInt(req.params.sessionId);
    if (isNaN(sessionId)) {
      return res.status(400).json({ error: 'Buổi học không hợp lệ.' });
    }

    const allJournals = await db.find('session_journals', j => parseInt(j.session_id) === sessionId);
    // Sort by creation time desc
    allJournals.sort((a, b) => b.created_at.localeCompare(a.created_at));
    res.json(allJournals);
  } catch (err) {
    console.error('Get admin session journal details error:', err);
    res.status(500).json({ error: 'Lỗi lấy chi tiết nhật ký buổi học' });
  }
});

export default router;
