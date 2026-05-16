import { Router } from 'express';
import { v4 as uuidv4 } from 'uuid';
import db from '../services/sheets.js';
import { authenticate, adminOnly } from '../middleware/auth.js';

const router = Router();

/**
 * Parse a free-text goal statement into individual items.
 * Handles patterns like:
 *   "1. First goal 2. Second goal 3. Third goal"
 *   "- First goal\n- Second goal"
 *   "First goal. Second goal. Third goal." (sentence-split fallback)
 */
function parseGoalText(text) {
  if (!text) return [];
  
  // Try numbered list: "1. xxx 2. xxx" or "1) xxx 2) xxx"
  const numbered = text.split(/\d+[\.\)]\s+/).filter(s => s.trim().length > 3);
  if (numbered.length >= 2) return numbered.map(s => s.replace(/\s+/g, ' ').trim());
  
  // Try dash/bullet list
  const dashed = text.split(/[\-•]\s+/).filter(s => s.trim().length > 3);
  if (dashed.length >= 2) return dashed.map(s => s.replace(/\s+/g, ' ').trim());
  
  // Try newline split
  const lines = text.split(/\n+/).filter(s => s.trim().length > 3);
  if (lines.length >= 2) return lines.map(s => s.replace(/\s+/g, ' ').trim());
  
  // Fallback: the whole text is one item
  return [text.trim()];
}

/**
 * GET /api/goals/my
 * Get current student's goal + items (checklist)
 */
router.get('/my', authenticate, async (req, res) => {
  try {
    const goal = await db.findOne('course_goals', g => g.student_id === req.user.student_id);
    
    if (!goal || !goal.id) {
      return res.json({ has_goal: false });
    }

    // Get goal items
    const items = await db.find('goal_items', i => i.student_id === req.user.student_id && i.deleted !== 'true');
    
    // Sort by order
    items.sort((a, b) => parseInt(a.order || 0) - parseInt(b.order || 0));
    
    // Calculate real progress
    const totalItems = items.length;
    const completedItems = items.filter(i => i.completed === 'true' || i.completed === true).length;
    const achievement = totalItems > 0 ? Math.round((completedItems / totalItems) * 100) : 0;

    res.json({
      ...goal,
      items: items.map(i => ({
        id: i.id,
        text: i.text,
        completed: i.completed === 'true' || i.completed === true,
        order: parseInt(i.order || 0)
      })),
      achievement_percent: achievement,
      total_items: totalItems,
      completed_items: completedItems
    });
  } catch (err) {
    console.error('Get goal error:', err);
    res.status(500).json({ error: 'Lỗi lấy dữ liệu mục tiêu' });
  }
});

/**
 * POST /api/goals
 * Save or update goal statement + auto-parse into items
 */
router.post('/', authenticate, async (req, res) => {
  try {
    const { goal_statement } = req.body;
    if (!goal_statement || goal_statement.trim().length < 10) {
      return res.status(400).json({ error: 'Mục tiêu cần chi tiết một chút (ít nhất 10 ký tự).' });
    }

    const existing = await db.findOne('course_goals', g => g.student_id === req.user.student_id);
    const now = new Date().toISOString();

    if (existing) {
      await db.update('course_goals', g => g.id === existing.id, {
        goal_statement: goal_statement.trim(),
        updated_at: now
      });
    } else {
      const newGoal = {
        id: uuidv4(),
        session_id: 1,
        student_id: req.user.student_id,
        student_name: req.user.full_name,
        goal_statement: goal_statement.trim(),
        achievement_percent: 0,
        created_at: now,
        updated_at: now
      };
      await db.append('course_goals', newGoal);
    }

    // Auto-parse into goal_items
    const parsedItems = parseGoalText(goal_statement);
    
    // Remove old items for this student
    // (Since sheets don't support delete, we'll mark and recreate)
    // For simplicity: just create items if none exist yet
    const existingItems = await db.find('goal_items', i => i.student_id === req.user.student_id && i.deleted !== 'true');
    
    if (existingItems.length === 0) {
      for (let idx = 0; idx < parsedItems.length; idx++) {
        await db.append('goal_items', {
          id: uuidv4(),
          student_id: req.user.student_id,
          text: parsedItems[idx],
          completed: false,
          order: idx + 1,
          created_at: now,
          updated_at: now
        });
      }
    }

    res.json({ 
      message: 'Đã ghi nhận mục tiêu học tập!',
      items_created: existingItems.length === 0 ? parsedItems.length : 0
    });
  } catch (err) {
    console.error('Save goal error:', err);
    res.status(500).json({ error: 'Lỗi lưu mục tiêu' });
  }
});

/**
 * POST /api/goals/items
 * Add a new goal item to the checklist
 */
router.post('/items', authenticate, async (req, res) => {
  try {
    const { text } = req.body;
    if (!text || text.trim().length < 3) {
      return res.status(400).json({ error: 'Mục tiêu cần ít nhất 3 ký tự.' });
    }

    const existingItems = await db.find('goal_items', i => i.student_id === req.user.student_id && i.deleted !== 'true');
    const nextOrder = existingItems.length + 1;
    const now = new Date().toISOString();

    const item = {
      id: uuidv4(),
      student_id: req.user.student_id,
      text: text.trim(),
      completed: false,
      order: nextOrder,
      created_at: now,
      updated_at: now
    };

    await db.append('goal_items', item);
    
    // Recalculate progress
    const allItems = [...existingItems, item];
    const completed = allItems.filter(i => i.completed === 'true' || i.completed === true).length;
    const percent = Math.round((completed / allItems.length) * 100);
    
    await db.update('course_goals', g => g.student_id === req.user.student_id, {
      achievement_percent: percent,
      updated_at: now
    });

    res.json({ message: 'Đã thêm mục tiêu!', item });
  } catch (err) {
    console.error('Add item error:', err);
    res.status(500).json({ error: 'Lỗi thêm mục tiêu' });
  }
});

/**
 * PUT /api/goals/items/:id/toggle
 * Toggle a goal item's completion status
 */
router.put('/items/:id/toggle', authenticate, async (req, res) => {
  try {
    const itemId = req.params.id;
    const item = await db.findOne('goal_items', 
      i => i.id === itemId && i.student_id === req.user.student_id
    );
    
    if (!item) {
      return res.status(404).json({ error: 'Không tìm thấy mục tiêu này.' });
    }

    const newCompleted = !(item.completed === 'true' || item.completed === true);
    const now = new Date().toISOString();
    
    await db.update('goal_items', i => i.id === itemId, {
      completed: newCompleted,
      updated_at: now
    });

    // Recalculate progress
    const allItems = await db.find('goal_items', i => i.student_id === req.user.student_id && i.deleted !== 'true');
    // Apply the toggle to current item in-memory for accurate count
    const completed = allItems.filter(i => {
      if (i.id === itemId) return newCompleted;
      return i.completed === 'true' || i.completed === true;
    }).length;
    const percent = Math.round((completed / allItems.length) * 100);
    
    await db.update('course_goals', g => g.student_id === req.user.student_id, {
      achievement_percent: percent,
      updated_at: now
    });

    res.json({ 
      message: newCompleted ? '✅ Đã hoàn thành!' : 'Đã bỏ đánh dấu.',
      completed: newCompleted,
      achievement_percent: percent
    });
  } catch (err) {
    console.error('Toggle item error:', err);
    res.status(500).json({ error: 'Lỗi cập nhật' });
  }
});

/**
 * DELETE /api/goals/items/:id
 * Remove a goal item
 */
router.delete('/items/:id', authenticate, async (req, res) => {
  try {
    const itemId = req.params.id;
    
    // We can't easily delete from sheets, so we'll just filter it out in GET
    // Or we could have a 'deleted' flag. 
    // Given the current architecture, 'update' to mark as deleted is safer.
    // However, sheets.js doesn't have a direct 'remove' yet.
    // Let's check if sheets.js supports deletion. 
    // Looking at sheets.js, it doesn't have a 'remove' function.
    // I will add a 'deleted' field and filter in GET.
    
    await db.update('goal_items', i => i.id === itemId && i.student_id === req.user.student_id, {
      deleted: 'true',
      updated_at: new Date().toISOString()
    });

    // Recalculate progress after deletion
    const allItems = await db.find('goal_items', i => i.student_id === req.user.student_id && i.deleted !== 'true');
    const completed = allItems.filter(i => i.completed === 'true' || i.completed === true).length;
    const percent = allItems.length > 0 ? Math.round((completed / allItems.length) * 100) : 0;
    
    await db.update('course_goals', g => g.student_id === req.user.student_id, {
      achievement_percent: percent,
      updated_at: new Date().toISOString()
    });

    res.json({ message: 'Đã xóa mục tiêu!', achievement_percent: percent });
  } catch (err) {
    console.error('Delete item error:', err);
    res.status(500).json({ error: 'Lỗi xóa mục tiêu' });
  }
});

/**
 * POST /api/goals/assess
 * Self-assessment of achievement percentage (legacy support)
 */
router.post('/assess', authenticate, async (req, res) => {
  try {
    const { percent } = req.body;
    const achievement = parseInt(percent);
    
    if (isNaN(achievement) || achievement < 0 || achievement > 100) {
      return res.status(400).json({ error: 'Tỷ lệ phần trăm không hợp lệ.' });
    }

    const existing = await db.findOne('course_goals', g => g.student_id === req.user.student_id);
    if (!existing) {
      return res.status(404).json({ error: 'Bạn chưa thiết lập mục tiêu ban đầu.' });
    }

    await db.update('course_goals', g => g.id === existing.id, {
      achievement_percent: achievement,
      updated_at: new Date().toISOString()
    });

    res.json({ message: `Ghi nhận bạn đã đạt được ${achievement}% mục tiêu đề ra!` });
  } catch (err) {
    console.error('Assess goal error:', err);
    res.status(500).json({ error: 'Lỗi cập nhật đánh giá' });
  }
});

/**
 * GET /api/goals/admin/all
 * Admin-only: Get all student goals
 */
router.get('/admin/all', authenticate, adminOnly, async (req, res) => {
  try {
    const goals = await db.getAll('course_goals');
    res.json(goals);
  } catch (err) {
    console.error('Get all goals error:', err);
    res.status(500).json({ error: 'Lỗi lấy danh sách mục tiêu' });
  }
});

export default router;
