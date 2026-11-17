import { api } from '../api.js';

export async function renderStudentBoard(app) {
  app.innerHTML = `<div class="container page"><div class="loading"><div class="spinner"></div></div></div>`;

  try {
    const data = await api.get('/board/students');
    const { summary, students } = data;

    app.innerHTML = `
      <div class="container page">
        <div class="page-header">
          <h1 class="page-title">🏆 Bảng Tiến Trình Lớp Học</h1>
          <p class="page-subtitle">Mỗi người một hành trình — so sánh với chính mình ngày hôm qua</p>
        </div>

        <!-- Summary Stats -->
        <div class="grid grid-4 board-summary">
          <div class="stat-card">
            <div class="stat-value">${summary.total_students}</div>
            <div class="stat-label">Sinh viên</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">${summary.with_goals}</div>
            <div class="stat-label">Đã đặt mục tiêu</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">${summary.with_quizzes}</div>
            <div class="stat-label">Đã làm quiz</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">${summary.avg_engagement}</div>
            <div class="stat-label">TB Hoạt động</div>
          </div>
        </div>

        <!-- Filter -->
        <div class="board-filter">
          <button class="btn btn-sm board-filter-btn active" data-filter="all">Tất cả</button>
          <button class="btn btn-sm board-filter-btn" data-filter="has-goal">Có mục tiêu</button>
          <button class="btn btn-sm board-filter-btn" data-filter="active">Tích cực</button>
          <button class="btn btn-sm board-filter-btn" data-filter="need-push">Cần động lực</button>
        </div>

        <!-- Student Cards -->
        <div class="board-grid" id="board-grid">
          ${students.map((s, i) => renderStudentCard(s, i)).join('')}
        </div>

        ${students.length === 0 ? `
          <div class="empty-state">
            <div class="empty-state-icon">📭</div>
            <p>Chưa có sinh viên nào trong lớp.</p>
          </div>
        ` : ''}
      </div>
    `;

    // Filter logic
    const filterBtns = app.querySelectorAll('.board-filter-btn');
    const cards = app.querySelectorAll('.board-student-card');

    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const filter = btn.dataset.filter;

        cards.forEach(card => {
          const engagement = parseInt(card.dataset.engagement);
          const hasGoal = card.dataset.hasGoal === 'true';

          if (filter === 'all') {
            card.style.display = '';
          } else if (filter === 'has-goal') {
            card.style.display = hasGoal ? '' : 'none';
          } else if (filter === 'active') {
            card.style.display = engagement >= 3 ? '' : 'none';
          } else if (filter === 'need-push') {
            card.style.display = engagement < 2 ? '' : 'none';
          }
        });
      });
    });

  } catch (err) {
    app.innerHTML = `
      <div class="container page">
        <div class="alert alert-danger">Lỗi tải dữ liệu: ${err.message}</div>
      </div>
    `;
  }
}

function renderStudentCard(student, index) {
  const {
    full_name, goal_statement, achievement_percent,
    quiz_count, quiz_avg, exam_count, feedback_count,
    has_goal, engagement
  } = student;

  // Engagement level
  let engagementLevel, engagementLabel, engagementColor;
  if (engagement >= 4) {
    engagementLevel = 'high';
    engagementLabel = '🔥 Tích cực';
    engagementColor = 'var(--success)';
  } else if (engagement >= 2) {
    engagementLevel = 'medium';
    engagementLabel = '⚡ Đang tiến bộ';
    engagementColor = 'var(--warning)';
  } else {
    engagementLevel = 'low';
    engagementLabel = '💤 Chờ khởi động';
    engagementColor = 'var(--text-muted)';
  }

  // Quiz badge color
  const quizBadge = quiz_avg !== null
    ? (quiz_avg >= 8 ? 'badge-success' : quiz_avg >= 5 ? 'badge-warning' : 'badge-danger')
    : '';

  return `
    <div class="board-student-card" 
         data-engagement="${engagement}" 
         data-has-goal="${has_goal}"
         style="animation-delay: ${index * 0.05}s">
      <div class="board-card-header">
        <div class="board-avatar">${getInitials(full_name)}</div>
        <div class="board-name-wrap">
          <div class="board-name">${full_name}</div>
          <div class="board-engagement" style="color: ${engagementColor}">${engagementLabel}</div>
        </div>
      </div>

      ${has_goal ? `
        <div class="board-goal">
          <div class="board-goal-label">🎯 Mục tiêu</div>
          <p class="board-goal-text">"${truncate(goal_statement, 120)}"</p>
          ${achievement_percent > 0 ? `
            <div style="margin-top: 0.5rem">
              <div style="display: flex; justify-content: space-between; font-size: 0.8rem; margin-bottom: 0.3rem">
                <span style="color: var(--text-muted)">Tự đánh giá</span>
                <span style="color: var(--accent); font-weight: 600">${achievement_percent}%</span>
              </div>
              <div class="progress-bar">
                <div class="progress-bar-fill" style="width: ${achievement_percent}%"></div>
              </div>
            </div>
          ` : ''}
        </div>
      ` : `
        <div class="board-goal board-no-goal">
          <span style="color: var(--text-muted); font-size: 0.85rem">Chưa đặt mục tiêu</span>
        </div>
      `}

      <div class="board-stats">
        <div class="board-stat-item">
          <span class="board-stat-num">${quiz_count}</span>
          <span class="board-stat-label">Quiz</span>
        </div>
        <div class="board-stat-item">
          ${quiz_avg !== null 
            ? `<span class="badge ${quizBadge}" style="font-size: 0.75rem">${quiz_avg}</span>`
            : `<span class="board-stat-num">—</span>`
          }
          <span class="board-stat-label">TB Quiz</span>
        </div>
        <div class="board-stat-item">
          <span class="board-stat-num">${exam_count}</span>
          <span class="board-stat-label">Exam</span>
        </div>
        <div class="board-stat-item">
          <span class="board-stat-num">${feedback_count}</span>
          <span class="board-stat-label">Feedback</span>
        </div>
      </div>
    </div>
  `;
}

function getInitials(name) {
  if (!name) return '?';
  const parts = name.trim().split(/\s+/);
  if (parts.length === 1) return parts[0].charAt(0).toUpperCase();
  return (parts[parts.length - 2].charAt(0) + parts[parts.length - 1].charAt(0)).toUpperCase();
}

function truncate(str, max) {
  if (!str) return '';
  return str.length > max ? str.substring(0, max) + '...' : str;
}
