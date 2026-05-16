import { api } from '../api.js';

export async function renderGoalsPage(app) {
  app.innerHTML = `<div class="container page"><div class="loading"><div class="spinner"></div></div></div>`;

  try {
    const goal = await api.get('/goals/my');

    if (!goal.id) {
      app.innerHTML = `
        <div class="container page">
          <div class="page-header">
            <h1 class="page-title">🎯 Mục tiêu học tập</h1>
            <p class="page-subtitle">Thiết lập mục tiêu để bắt đầu hành trình</p>
          </div>
          <div class="goal-setup-card">
            <div class="goal-setup-icon">🚀</div>
            <h2>Bạn chưa thiết lập mục tiêu</h2>
            <p>Hãy viết ra những điều bạn muốn đạt được sau môn học này.<br>
            <em>Mỗi mục tiêu viết trên 1 dòng, hoặc đánh số: 1. 2. 3.</em></p>
            <textarea id="goal-input" class="form-input" 
                      placeholder="Ví dụ:&#10;1. Hiểu rõ các khái niệm cốt lõi&#10;2. Áp dụng được vào dự án thực tế&#10;3. Đạt điểm A môn học"
                      style="min-height: 140px; margin: 1.5rem 0"></textarea>
            <button id="save-goal-btn" class="btn btn-primary btn-lg">💾 Lưu mục tiêu học tập</button>
          </div>
        </div>
      `;

      document.getElementById('save-goal-btn').addEventListener('click', async () => {
        const text = document.getElementById('goal-input').value;
        if (!text || text.trim().length < 10) {
          alert('Vui lòng viết mục tiêu rõ ràng hơn (ít nhất 10 ký tự)');
          return;
        }
        try {
          await api.post('/goals', { goal_statement: text });
          renderGoalsPage(app); // Reload
        } catch (err) {
          alert(err.message || 'Lỗi khi lưu mục tiêu');
        }
      });
      return;
    }

    // Has goals — render checklist
    const { items, achievement_percent, total_items, completed_items } = goal;
    const progressColor = achievement_percent >= 80 ? 'var(--success)' 
                         : achievement_percent >= 40 ? 'var(--warning)' 
                         : 'var(--accent)';

    app.innerHTML = `
      <div class="container page">
        <div class="page-header">
          <h1 class="page-title">🎯 Mục tiêu học tập</h1>
          <p class="page-subtitle">Check từng mục tiêu khi bạn đạt được — tiến trình sẽ tự động cập nhật</p>
        </div>

        <!-- Progress Overview -->
        <div class="goal-progress-card">
          <div class="goal-progress-header">
            <div>
              <div class="goal-progress-title">Tiến trình hoàn thành</div>
              <div class="goal-progress-detail">${completed_items}/${total_items} mục tiêu đã đạt</div>
            </div>
            <div class="goal-progress-percent" style="color: ${progressColor}">${achievement_percent}%</div>
          </div>
          <div class="goal-progress-bar">
            <div class="goal-progress-bar-fill" style="width: ${achievement_percent}%; background: ${progressColor}"></div>
          </div>
          ${achievement_percent === 100 ? `
            <div class="goal-complete-msg">🎉 Xuất sắc! Bạn đã hoàn thành tất cả mục tiêu!</div>
          ` : ''}
        </div>

        <!-- Checklist -->
        <div class="goal-checklist" id="goal-checklist">
          <h2 class="goal-checklist-title">📋 Danh sách mục tiêu</h2>
          ${items.map((item, idx) => `
            <div class="goal-item ${item.completed ? 'goal-item-done' : ''}" data-id="${item.id}">
              <button class="goal-check-btn" data-id="${item.id}" aria-label="Toggle">
                <span class="goal-check-icon">${item.completed ? '✅' : '⬜'}</span>
              </button>
              <span class="goal-item-num">${idx + 1}</span>
              <span class="goal-item-text ${item.completed ? 'goal-text-done' : ''}">${item.text}</span>
            </div>
          `).join('')}
        </div>

        <!-- Add new item -->
        <div class="goal-add-section">
          <h3 style="margin-bottom: 0.75rem; color: var(--text-secondary)">➕ Thêm mục tiêu mới</h3>
          <div style="display: flex; gap: 0.75rem">
            <input type="text" id="new-goal-input" class="form-input" 
                   placeholder="Nhập mục tiêu mới..." style="flex: 1">
            <button id="add-goal-btn" class="btn btn-primary">Thêm</button>
          </div>
        </div>
      </div>
    `;

    // Toggle item handler
    app.querySelectorAll('.goal-check-btn').forEach(btn => {
      btn.addEventListener('click', async () => {
        const itemId = btn.dataset.id;
        btn.disabled = true;
        try {
          const result = await api.put(`/goals/items/${itemId}/toggle`);
          renderGoalsPage(app); // Reload to reflect changes
        } catch (err) {
          alert(err.message || 'Lỗi cập nhật');
          btn.disabled = false;
        }
      });
    });

    // Add new item handler
    document.getElementById('add-goal-btn').addEventListener('click', async () => {
      const input = document.getElementById('new-goal-input');
      const text = input.value.trim();
      if (!text || text.length < 3) {
        alert('Mục tiêu cần ít nhất 3 ký tự');
        return;
      }
      try {
        await api.post('/goals/items', { text });
        renderGoalsPage(app);
      } catch (err) {
        alert(err.message || 'Lỗi thêm mục tiêu');
      }
    });

    // Enter key support
    document.getElementById('new-goal-input').addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        document.getElementById('add-goal-btn').click();
      }
    });

  } catch (err) {
    app.innerHTML = `
      <div class="container page">
        <div class="alert alert-danger">Lỗi tải mục tiêu: ${err.message}</div>
      </div>
    `;
  }
}
