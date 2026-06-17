import { Router } from 'express';
import db from '../services/sheets.js';
import { authenticate } from '../middleware/auth.js';

const router = Router();

function parseSessionNumber(val) {
  if (val === undefined || val === null) return 0;
  const str = String(val).trim();
  const match = str.match(/\d+/);
  return match ? parseInt(match[0], 10) : parseInt(str, 10) || 0;
}

/**
 * GET /api/board/students
 * Public (authenticated): Get summary of all students' progress
 * Shows: name, goal statement, quiz count, avg quiz score, achievement %
 * Does NOT expose sensitive data (student_id, email, password)
 */
router.get('/students', authenticate, async (req, res) => {
  try {
    const [students, goals, quizAttempts, examAttempts, feedbacks] = await Promise.all([
      db.getAll('students'),
      db.getAll('course_goals'),
      db.getAll('quiz_attempts'),
      db.getAll('exam_attempts'),
      db.getAll('feedbacks')
    ]);

    const board = students
      .filter(s => s.role !== 'admin')
      .map(s => {
        // Goal
        const goal = goals.find(g => g.student_id === s.student_id);
        
        // Quiz stats: group attempts by session and select the highest score for each session
        const studentQuizzes = quizAttempts.filter(a => a.student_id === s.student_id);
        const bestScores = {};
        for (const a of studentQuizzes) {
          const sess = parseSessionNumber(a.session_number);
          const score = parseFloat(a.score || 0);
          if (bestScores[sess] === undefined || score > bestScores[sess]) {
            bestScores[sess] = score;
          }
        }
        const bestScoresArr = Object.values(bestScores);
        const quizCount = bestScoresArr.length;
        const quizAvg = quizCount > 0
          ? Math.round(bestScoresArr.reduce((sum, scoreVal) => sum + scoreVal, 0) / quizCount * 10) / 10
          : null;
        
        // Exam stats
        const studentExams = examAttempts.filter(a => a.student_id === s.student_id);
        
        // Feedback count
        const studentFeedbacks = feedbacks.filter(f => f.student_id === s.student_id);

        return {
          full_name: s.full_name,
          goal_statement: goal?.goal_statement || null,
          achievement_percent: goal ? parseInt(goal.achievement_percent || 0) : 0,
          quiz_count: quizCount,
          quiz_avg: quizAvg,
          exam_count: studentExams.length,
          feedback_count: studentFeedbacks.length,
          has_goal: !!goal?.goal_statement,
          // Engagement score (simple metric)
          engagement: quizCount + studentExams.length + studentFeedbacks.length + (goal?.goal_statement ? 1 : 0)
        };
      })
      // Sort by engagement (most active first)
      .sort((a, b) => b.engagement - a.engagement);

    // Summary stats
    const totalStudents = board.length;
    const withGoals = board.filter(s => s.has_goal).length;
    const withQuizzes = board.filter(s => s.quiz_count > 0).length;
    const avgEngagement = totalStudents > 0
      ? Math.round(board.reduce((sum, s) => sum + s.engagement, 0) / totalStudents * 10) / 10
      : 0;

    res.json({
      summary: {
        total_students: totalStudents,
        with_goals: withGoals,
        with_quizzes: withQuizzes,
        avg_engagement: avgEngagement
      },
      students: board
    });
  } catch (err) {
    console.error('Board error:', err);
    res.status(500).json({ error: 'Lỗi lấy dữ liệu bảng sinh viên' });
  }
});

export default router;
