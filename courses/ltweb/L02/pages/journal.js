import { api, getUser } from '../api.js';

export async function renderJournal(app) {
  app.innerHTML = `
    <div class="container page">
      <div class="loading"><div class="spinner"></div></div>
    </div>
  `;

  let journals = [];
  let sessionsData = null;

  try {
    const [journalsRes, sessionsRes] = await Promise.all([
      api.get('/journal/my'),
      api.get('/courses/sessions')
    ]);
    journals = journalsRes;
    sessionsData = sessionsRes;
  } catch (err) {
    app.innerHTML = `
      <div class="container page">
        <div class="alert alert-danger">Lỗi tải dữ liệu nhật ký học tập.</div>
      </div>
    `;
    return;
  }

  const user = getUser();
  const totalSessions = sessionsData.sessions.length;
  const journaledCount = journals.length;

  // Streak calculation: Longest consecutive run of session IDs
  const sessionIds = journals.map(j => parseInt(j.session_id)).sort((a, b) => a - b);
  let longestStreak = 0;
  let currentStreak = 0;
  let lastId = null;

  sessionIds.forEach(id => {
    if (lastId === null) {
      currentStreak = 1;
    } else if (id === lastId + 1) {
      currentStreak++;
    } else if (id !== lastId) {
      if (currentStreak > longestStreak) {
        longestStreak = currentStreak;
      }
      currentStreak = 1;
    }
    lastId = id;
  });
  if (currentStreak > longestStreak) {
    longestStreak = currentStreak;
  }

  // Calculate average goal rating
  const avgGoalRating = journals.length > 0
    ? (journals.reduce((sum, j) => sum + (parseInt(j.goal_rating) || 0), 0) / journals.length).toFixed(1)
    : '—';

  // Gamification recall badge text
  let masterClass = 'Mới bắt đầu 🌱';
  let badgeColor = 'badge-info';
  if (journaledCount >= 7) {
    masterClass = 'Bậc thầy phản tư 🏆';
    badgeColor = 'badge-success';
  } else if (journaledCount >= 4) {
    masterClass = 'Phản tư năng động 🚀';
    badgeColor = 'badge-accent';
  }

  app.innerHTML = `
    <div class="container page">
      <div class="page-header" style="display:flex; justify-content:space-between; align-items:flex-end; flex-wrap:wrap; gap:1rem">
        <div>
          <h1 class="page-title">📓 Nhật ký học tập của tôi</h1>
          <p class="page-subtitle">Sử dụng Active Recall để chuyển hóa kiến thức từ trí nhớ ngắn hạn sang dài hạn</p>
        </div>
        <div class="badge ${badgeColor}" style="padding: 0.5rem 1rem; font-size: 0.85rem">
          Cấp độ: ${masterClass}
        </div>
      </div>

      <!-- Journal Statistics Dashboard -->
      <div class="journal-stats">
        <div class="stat-card">
          <div class="stat-value">${journaledCount}/${totalSessions}</div>
          <div class="stat-label">Buổi đã viết</div>
        </div>
        <div class="stat-card">
          <div class="stat-value" style="display:flex; align-items:center; justify-content:center; gap:0.25rem">
            ${longestStreak}
            ${longestStreak > 0 ? '<span class="streak-badge">🔥</span>' : ''}
          </div>
          <div class="stat-label">Chuỗi viết liên tục</div>
        </div>
        <div class="stat-card">
          <div class="stat-value">${avgGoalRating}</div>
          <div class="stat-label">Điểm Mục tiêu TB</div>
        </div>
        <div class="stat-card">
          <div class="stat-value">
            ${journals.length > 0 ? (journals.filter(j => ['🔥', '😊'].includes(j.mood)).length / journals.length * 100).toFixed(0) + '%' : '—'}
          </div>
          <div class="stat-label">Năng lượng Tích cực</div>
        </div>
      </div>

      <h2 style="margin-bottom:1.5rem">📜 Timeline Nhật ký hành trình</h2>

      <div class="journal-timeline">
        ${sessionsData.sessions.map(s => {
          const entry = journals.find(j => parseInt(j.session_id) === s.id);
          
          if (entry) {
            const stars = '★'.repeat(entry.goal_rating) + '☆'.repeat(5 - entry.goal_rating);
            const dateStr = new Date(entry.updated_at).toLocaleString('vi-VN', {
              day: 'numeric',
              month: 'numeric',
              year: 'numeric',
              hour: '2-digit',
              minute: '2-digit'
            });

            return `
              <div class="journal-entry">
                <div class="journal-entry-dot written">📓</div>
                <div class="journal-entry-header">
                  <div>
                    <span class="badge badge-accent" style="margin-bottom: 0.4rem">Buổi ${s.id}</span>
                    <h3 class="journal-entry-title">
                      ${s.title}
                      <span style="font-size:1.5rem" title="Cảm xúc sau buổi học">${entry.mood || '😐'}</span>
                    </h3>
                  </div>
                  <div style="text-align: right">
                    <div class="journal-entry-meta">Viết lúc: ${dateStr}</div>
                    <a href="#/journal/write/${s.id}" class="btn btn-sm btn-secondary" style="margin-top: 0.5rem">
                      ✏️ Chỉnh sửa
                    </a>
                  </div>
                </div>

                <div class="journal-entry-body">
                  <div class="journal-sub-section">
                    <div class="journal-sub-title recall">🧠 Active Recall — Những gì ghi nhớ được:</div>
                    <div class="journal-sub-content">${entry.recall_text}</div>
                  </div>

                  ${entry.questions_text ? `
                    <div class="journal-sub-section">
                      <div class="journal-sub-title questions">❓ Vấn đề còn băn khoăn / Muốn hỏi thêm:</div>
                      <div class="journal-sub-content">${entry.questions_text}</div>
                    </div>
                  ` : ''}

                  <div class="journal-sub-section">
                    <div class="journal-sub-title goals">🎯 Đánh giá hiệu suất học tập:</div>
                    <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.25rem">
                      <span style="color:var(--warning); font-size:1.2rem">${stars}</span>
                      <span style="color:var(--text-muted); font-size:0.85rem">(${entry.goal_rating}/5)</span>
                    </div>
                    ${entry.goal_note ? `
                      <div class="journal-sub-content" style="font-style: italic; color: var(--text-secondary)">
                        &ldquo;${entry.goal_note}&rdquo;
                      </div>
                    ` : ''}
                  </div>
                </div>
              </div>
            `;
          } else {
            return `
              <div class="journal-entry" style="opacity: 0.75; border-style: dashed">
                <div class="journal-entry-dot">😴</div>
                <div class="journal-entry-header" style="margin-bottom:0">
                  <div>
                    <span class="badge badge-accent" style="margin-bottom: 0.4rem; background: rgba(255,255,255,0.05); color: var(--text-muted)">Buổi ${s.id}</span>
                    <h3 class="journal-entry-title" style="color: var(--text-muted)">
                      ${s.title}
                    </h3>
                    <p style="color: var(--text-muted); font-size: 0.85rem; margin-top:0.25rem">Bạn chưa viết nhật ký cho buổi này.</p>
                  </div>
                  <div>
                    <a href="#/journal/write/${s.id}" class="btn btn-sm btn-primary">
                      📓 Viết nhật ký
                    </a>
                  </div>
                </div>
              </div>
            `;
          }
        }).join('')}
      </div>
    </div>
  `;
}
