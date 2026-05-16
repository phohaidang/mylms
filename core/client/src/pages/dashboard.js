import { api, getUser } from '../api.js';

export async function renderDashboard(app) {
  const user = getUser();
  
  app.innerHTML = `
    <div class="container page">
      <div class="page-header">
        <h1 class="page-title">Xin chào, ${user.full_name}! 👋</h1>
        <p class="page-subtitle" id="course-subtitle" style="opacity: 0.7">Đang tải thông tin lớp học...</p>
      </div>

      <div class="grid grid-4" id="stats">
        <div class="stat-card"><div class="spinner"></div></div>
        <div class="stat-card"><div class="spinner"></div></div>
        <div class="stat-card"><div class="spinner"></div></div>
        <div class="stat-card"><div class="spinner"></div></div>
      </div>

      <div id="goals-section" style="margin-top: 2rem">
         <div class="card"><div class="spinner"></div> Đang tải mục tiêu học tập...</div>
      </div>

      <div style="margin-top: 2rem">
        <h2 style="margin-bottom: 1rem">🚀 Truy cập nhanh</h2>
        <div class="grid grid-3">
          <a href="#/course" class="card" style="text-decoration:none">
            <h3>📚 Buổi học</h3>
            <p style="color:var(--text-secondary);font-size:0.9rem;margin-top:0.5rem">
              Xem giáo án, slide 6 buổi học
            </p>
          </a>
          <a href="#/ebook" class="card" style="text-decoration:none">
            <h3>📖 eBook</h3>
            <p style="color:var(--text-secondary);font-size:0.9rem;margin-top:0.5rem">
              Ôn tập theo SCQA + 3-Level Test
            </p>
          </a>
          <a href="#/grades" class="card" style="text-decoration:none">
            <h3>📋 Bảng điểm</h3>
            <p style="color:var(--text-secondary);font-size:0.9rem;margin-top:0.5rem">
              Xem điểm quiz, kiểm tra, tổng kết
            </p>
          </a>
        </div>
      </div>
    </div>
  `;

  // Gọi hàm renderGoals
  const goalsContainer = document.getElementById('goals-section');
  if (goalsContainer) {
    renderGoals(goalsContainer);
  }

  // Load stats
  try {
    const [quizzes, grades, courseData] = await Promise.all([
      api.get('/quizzes/my/attempts'),
      api.get('/grades/me'),
      api.get('/courses/sessions')
    ]);

    // Update course info
    const subtitle = document.getElementById('course-subtitle');
    if (subtitle && courseData) {
      subtitle.innerText = `${courseData.course.code} — ${courseData.course.name} | ĐH Ngân Hàng TP.HCM`;
    }

    const quizDone = quizzes.length;
    const avgScore = quizzes.length > 0
      ? (quizzes.reduce((s, q) => s + q.score, 0) / quizzes.length).toFixed(1)
      : '—';
    const examsDone = grades.exams?.length || 0;
    const totalScore = grades.manual?.total_score ?? '—';

    document.getElementById('stats').innerHTML = `
      <div class="stat-card">
        <div class="stat-value">${quizDone}/6</div>
        <div class="stat-label">Quiz đã làm</div>
      </div>
      <div class="stat-card">
        <div class="stat-value">${avgScore}</div>
        <div class="stat-label">Điểm TB Quiz</div>
      </div>
      <div class="stat-card">
        <div class="stat-value">${examsDone}</div>
        <div class="stat-label">Bài kiểm tra</div>
      </div>
      <div class="stat-card">
        <div class="stat-value">${totalScore}</div>
        <div class="stat-label">Điểm tổng kết</div>
      </div>
    `;
  } catch (err) {
    document.getElementById('stats').innerHTML = `
      <div class="alert alert-warning" style="grid-column: 1/-1">
        Tạm thời không thể tải thống kê. Hãy bắt đầu làm quiz!
      </div>
    `;
  }
}

async function renderGoals(container) {
  try {
    const goal = await api.get('/goals/my');
    
    if (!goal.id) {
      container.innerHTML = `
        <div class="goal-cta-card">
          <div class="goal-cta-content">
            <div class="goal-cta-icon">🎯</div>
            <div>
              <h2 style="margin-bottom: 0.5rem; color: white">Xác lập mục tiêu học tập</h2>
              <p style="opacity: 0.85; margin-bottom: 1rem">Viết ra những điều bạn muốn đạt được — đây là bản cam kết với chính mình.</p>
              <a href="#/goals" class="btn btn-secondary" style="background: rgba(255,255,255,0.15); border-color: rgba(255,255,255,0.3); color: white">
                ✍️ Thiết lập ngay
              </a>
            </div>
          </div>
        </div>
      `;
      return;
    }

    // Has goals — show summary card with checklist
    const { items, achievement_percent, total_items, completed_items } = goal;
    const progressColor = achievement_percent >= 80 ? '#22c55e' 
                         : achievement_percent >= 40 ? '#f59e0b' 
                         : '#818cf8';
    
    // Show max 4 items on dashboard
    const displayItems = items.slice(0, 4);
    const hasMore = items.length > 4;

    container.innerHTML = `
      <div class="goal-dashboard-card">
        <div class="goal-dash-header">
          <div>
            <h2 style="margin-bottom: 0.25rem">🎯 Mục tiêu của tôi</h2>
            <span class="goal-dash-count">${completed_items}/${total_items} hoàn thành</span>
          </div>
          <div class="goal-dash-percent" style="color: ${progressColor}">
            ${achievement_percent}%
          </div>
        </div>
        
        <div class="goal-dash-progress">
          <div class="goal-dash-progress-fill" style="width: ${achievement_percent}%; background: linear-gradient(90deg, ${progressColor}, ${progressColor}99)"></div>
        </div>

        <div class="goal-dash-items">
          ${displayItems.map((item, idx) => `
            <div class="goal-dash-item ${item.completed ? 'goal-dash-item-done' : ''}">
              <span class="goal-dash-check">${item.completed ? '✅' : '⬜'}</span>
              <span class="goal-dash-item-text">${item.text}</span>
            </div>
          `).join('')}
          ${hasMore ? `<div style="font-size: 0.82rem; color: var(--text-muted); padding-left: 2rem; margin-top: 0.25rem">... và ${items.length - 4} mục tiêu khác</div>` : ''}
        </div>

        <a href="#/goals" class="btn btn-primary btn-block" style="margin-top: 1.25rem">
          📋 Xem & Check mục tiêu chi tiết
        </a>
      </div>
    `;

  } catch (err) {
    console.error('Goals error:', err);
    container.innerHTML = `
      <div class="alert alert-warning">
        ⚠️ Không thể tải mục tiêu học tập (Lỗi: ${err.message}). <br>
        Có thể Server đang cập nhật, vui lòng F5 lại trang sau 1 phút.
      </div>
    `;
  }
}
