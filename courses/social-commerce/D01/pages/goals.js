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
            <div class="goal-item ${item.completed ? 'goal-item-done' : ''}" data-id="${item.id}" style="cursor: pointer">
              <div class="goal-item-main" style="display: flex; align-items: center; gap: 0.75rem; flex: 1">
                <div class="goal-check-icon">${item.completed ? '✅' : '⬜'}</div>
                <span class="goal-item-num">${idx + 1}</span>
                <span class="goal-item-text ${item.completed ? 'goal-text-done' : ''}">${item.text}</span>
              </div>
              <button class="btn-delete-goal" data-id="${item.id}" title="Xóa mục tiêu" style="background: none; border: none; color: var(--danger); opacity: 0.4; cursor: pointer; padding: 0.5rem; transition: opacity 0.2s">
                🗑️
              </button>
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

    // Toggle item handler (on the whole row)
    app.querySelectorAll('.goal-item-main').forEach(el => {
      el.addEventListener('click', async (e) => {
        const itemEl = el.closest('.goal-item');
        const itemId = itemEl.dataset.id;
        
        // Visual feedback
        itemEl.style.opacity = '0.5';
        itemEl.style.pointerEvents = 'none';
        
        try {
          await api.put(`/goals/items/${itemId}/toggle`);
          renderGoalsPage(app);
        } catch (err) {
          alert(err.message || 'Lỗi cập nhật');
          itemEl.style.opacity = '1';
          itemEl.style.pointerEvents = 'auto';
        }
      });
    });

    // Delete item handler
    app.querySelectorAll('.btn-delete-goal').forEach(btn => {
      btn.addEventListener('mouseover', () => btn.style.opacity = '1');
      btn.addEventListener('mouseout', () => btn.style.opacity = '0.4');
      
      btn.addEventListener('click', async (e) => {
        e.stopPropagation();
        const itemId = btn.dataset.id;
        if (!confirm('Bạn có chắc chắn muốn xóa mục tiêu này?')) return;
        
        btn.disabled = true;
        try {
          await api.delete(`/goals/items/${itemId}`);
          renderGoalsPage(app);
        } catch (err) {
          alert(err.message || 'Lỗi xóa mục tiêu');
          btn.disabled = false;
        }
      });
    });

    // Add new item handler
    const addBtn = document.getElementById('add-goal-btn');
    const addInput = document.getElementById('new-goal-input');

    addBtn.addEventListener('click', async () => {
      const text = addInput.value.trim();
      if (!text || text.length < 3) {
        alert('Mục tiêu cần ít nhất 3 ký tự');
        return;
      }
      
      // Prevent multiple clicks
      addBtn.disabled = true;
      addBtn.innerText = 'Đang thêm...';
      
      try {
        await api.post('/goals/items', { text });
        renderGoalsPage(app);
      } catch (err) {
        alert(err.message || 'Lỗi thêm mục tiêu');
        addBtn.disabled = false;
        addBtn.innerText = 'Thêm';
      }
    });

    // Enter key support
    addInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        addBtn.click();
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
