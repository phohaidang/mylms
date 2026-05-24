import { api } from '../../api.js';

export async function renderAdminJournal(app) {
  app.innerHTML = `
    <div class="container page">
      <div class="loading"><div class="spinner"></div></div>
    </div>
  `;

  let summary = [];
  let sessionsData = null;

  try {
    const [summaryRes, sessionsRes] = await Promise.all([
      api.get('/journal/admin/summary'),
      api.get('/courses/sessions')
    ]);
    summary = summaryRes;
    sessionsData = sessionsRes;
  } catch (err) {
    app.innerHTML = `
      <div class="container page">
        <div class="alert alert-danger">Lỗi tải dữ liệu tổng hợp nhật ký giảng viên.</div>
      </div>
    `;
    return;
  }

  app.innerHTML = `
    <div class="container page">
      <div class="page-header">
        <h1 class="page-title">🛠 Giám sát Nhật ký Học tập (Admin)</h1>
        <p class="page-subtitle">Xem dữ liệu Active Recall, phân tích câu hỏi chưa hiểu và cảm xúc của sinh viên</p>
      </div>

      <div class="grid grid-3" style="margin-bottom: 2rem">
        ${sessionsData.sessions.map(s => {
          const sSum = summary.find(sm => sm.session_id === s.id) || { total_journals: 0, avg_rating: 0, moods: {} };
          
          return `
            <div class="card session-card" data-session-id="${s.id}" style="cursor:pointer; transition:all var(--transition)">
              <div style="display:flex; justify-content:space-between; align-items:flex-start">
                <span class="badge badge-accent">Buổi ${s.id}</span>
                <span class="badge badge-info" style="font-size:0.75rem">${sSum.total_journals} lượt viết</span>
              </div>
              <h3 style="margin: 0.75rem 0 0.5rem">${s.title}</h3>
              <div style="display:flex; justify-content:space-between; align-items:center; margin-top:1rem; font-size:0.85rem; color:var(--text-secondary)">
                <span>Đánh giá mục tiêu:</span>
                <strong style="color:var(--warning)">${sSum.avg_rating > 0 ? sSum.avg_rating + ' ★' : '—'}</strong>
              </div>
              <div style="display:flex; gap:0.25rem; margin-top:0.5rem; font-size:1.2rem">
                ${Object.entries(sSum.moods).map(([mood, count]) => `
                  <span title="${count} sinh viên chọn ${mood}">${mood}<sup>${count}</sup></span>
                `).join('')}
              </div>
              <div class="btn btn-sm btn-ghost btn-block" style="margin-top:1rem; border: 1px dashed var(--border)">
                📂 Xem chi tiết
              </div>
            </div>
          `;
        }).join('')}
      </div>

      <div id="journal-details-container" style="display:none">
        <hr style="border:1px solid var(--border); margin: 2rem 0">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem">
          <h2 id="details-title">📁 Chi tiết Nhật ký</h2>
          <button class="btn btn-secondary btn-sm" id="btn-close-details">❌ Đóng chi tiết</button>
        </div>

        <!-- Grouped Student Questions Box -->
        <div class="card" style="border-left:4px solid var(--info); margin-bottom:1.5rem; background:rgba(59,130,246,0.03)">
          <h3 style="color:var(--info); display:flex; align-items:center; gap:0.5rem; margin-bottom:0.75rem">
            ❓ Tổng hợp vấn đề sinh viên chưa hiểu
          </h3>
          <ul id="consolidated-questions" style="padding-left:1.25rem; line-height:1.6; font-size:0.9rem">
            <!-- Questions loaded here -->
          </ul>
        </div>

        <div id="student-entries-list">
          <!-- Student entries list -->
        </div>
      </div>
    </div>
  `;

  // Close details panel
  const detailsContainer = document.getElementById('journal-details-container');
  document.getElementById('btn-close-details').addEventListener('click', () => {
    detailsContainer.style.display = 'none';
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  // Session card click listener
  const sessionCards = document.querySelectorAll('.session-card');
  sessionCards.forEach(card => {
    card.addEventListener('click', async () => {
      const sessionId = parseInt(card.getAttribute('data-session-id'));
      const session = sessionsData.sessions.find(s => s.id === sessionId);

      // Reset hover/glow for active card selection
      sessionCards.forEach(c => c.style.borderColor = 'var(--border)');
      card.style.borderColor = 'var(--accent)';

      // Show spinner in details area
      detailsContainer.style.display = 'block';
      document.getElementById('details-title').textContent = `📁 Chi tiết Nhật ký: Buổi ${sessionId} - ${session.title}`;
      const questionsEl = document.getElementById('consolidated-questions');
      const listEl = document.getElementById('student-entries-list');
      
      questionsEl.innerHTML = '<li>Đang tải...</li>';
      listEl.innerHTML = '<div class="loading"><div class="spinner"></div></div>';
      
      // Scroll to details panel
      detailsContainer.scrollIntoView({ behavior: 'smooth' });

      try {
        const details = await api.get(`/journal/admin/session/${sessionId}`);
        
        // Extract and aggregate questions
        const questions = details
          .map(d => ({ name: d.student_name, text: d.questions_text?.trim() }))
          .filter(q => q.text && q.text.length > 0);

        if (questions.length === 0) {
          questionsEl.innerHTML = '<li style="color:var(--text-muted)">Không có câu hỏi băn khoăn nào từ sinh viên trong buổi này.</li>';
        } else {
          questionsEl.innerHTML = questions.map(q => `
            <li style="margin-bottom:0.5rem">
              <strong>${q.name}:</strong> <span style="color:var(--text-primary)">${q.text}</span>
            </li>
          `).join('');
        }

        // Render detailed student list
        if (details.length === 0) {
          listEl.innerHTML = `
            <div class="empty-state">
              <div class="empty-state-icon">📝</div>
              <p>Chưa có sinh viên nào viết nhật ký cho buổi học này.</p>
            </div>
          `;
        } else {
          listEl.innerHTML = details.map(d => {
            const stars = '★'.repeat(d.goal_rating) + '☆'.repeat(5 - d.goal_rating);
            const dateStr = new Date(d.updated_at).toLocaleString('vi-VN');
            return `
              <div class="card" style="margin-bottom:1rem">
                <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:0.5rem; margin-bottom:1rem; border-bottom: 1px solid var(--border); padding-bottom:0.5rem">
                  <div>
                    <h4 style="color:var(--accent)">${d.student_name} (${d.student_id})</h4>
                    <span style="font-size:0.8rem; color:var(--text-muted)">Ngày nộp: ${dateStr}</span>
                  </div>
                  <div style="display:flex; gap:0.75rem; align-items:center">
                    <span style="font-size:1.6rem" title="Cảm xúc sau buổi học">${d.mood || '😐'}</span>
                    <div>
                      <span style="color:var(--warning)">${stars}</span>
                      <span style="font-size:0.8rem; color:var(--text-muted)">(${d.goal_rating}/5)</span>
                    </div>
                  </div>
                </div>

                <div class="journal-entry-body">
                  <div>
                    <strong style="color:var(--accent); font-size:0.85rem; text-transform:uppercase; letter-spacing:0.5px; display:block; margin-bottom:0.25rem">🧠 Active Recall:</strong>
                    <div style="font-size:0.95rem; white-space:pre-wrap; line-height:1.6">${d.recall_text}</div>
                  </div>

                  ${d.questions_text ? `
                    <div style="margin-top:0.75rem">
                      <strong style="color:var(--info); font-size:0.85rem; text-transform:uppercase; letter-spacing:0.5px; display:block; margin-bottom:0.25rem">❓ Câu hỏi / Băn khoăn:</strong>
                      <div style="font-size:0.95rem; white-space:pre-wrap; line-height:1.6">${d.questions_text}</div>
                    </div>
                  ` : ''}

                  ${d.goal_note ? `
                    <div style="margin-top:0.75rem; padding: 0.5rem 0.75rem; background:rgba(255,255,255,0.02); border-radius:4px">
                      <strong style="color:var(--warning); font-size:0.85rem; text-transform:uppercase; letter-spacing:0.5px; display:block; margin-bottom:0.25rem">🎯 Tự đánh giá mục tiêu:</strong>
                      <div style="font-size:0.92rem; font-style:italic; color:var(--text-secondary)">&ldquo;${d.goal_note}&rdquo;</div>
                    </div>
                  ` : ''}
                </div>
              </div>
            `;
          }).join('');
        }
      } catch (err) {
        listEl.innerHTML = '<div class="alert alert-danger">Lỗi tải chi tiết nhật ký sinh viên!</div>';
      }
    });
  });
}
