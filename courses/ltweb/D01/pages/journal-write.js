import { api } from '../api.js';
import { navigate } from '../router.js';

export async function renderJournalWrite(app, params) {
  const sessionId = parseInt(params.sessionId);
  if (isNaN(sessionId) || sessionId < 1 || sessionId > 9) {
    app.innerHTML = `
      <div class="container page">
        <div class="alert alert-danger">Buổi học không hợp lệ!</div>
      </div>
    `;
    return;
  }

  app.innerHTML = `
    <div class="container page">
      <div class="loading"><div class="spinner"></div></div>
    </div>
  `;

  // Fetch session metadata and existing journal
  let session = null;
  let journal = null;
  let isEdit = false;

  try {
    const sessionRes = await api.get(`/courses/sessions/${sessionId}`);
    session = sessionRes;
  } catch (err) {
    app.innerHTML = `
      <div class="container page">
        <div class="alert alert-danger">Không thể tải thông tin buổi học.</div>
      </div>
    `;
    return;
  }

  try {
    const existing = await api.get(`/journal/my/${sessionId}`);
    if (existing) {
      journal = existing;
      isEdit = true;
    }
  } catch (err) {
    // 404 is fine, means no journal submitted yet
  }

  app.innerHTML = `
    <div class="container page">
      <div class="journal-write-page">
        <div class="page-header" style="display:flex; justify-content:space-between; align-items:flex-end; flex-wrap:wrap; gap:1rem">
          <div>
            <a href="#/course" class="btn btn-sm btn-secondary" style="margin-bottom: 1rem">
              ⬅ Quay lại danh sách
            </a>
            <h1 class="page-title">📓 ${isEdit ? 'Chỉnh sửa nhật ký' : 'Nhật ký học tập'}</h1>
            <p class="page-subtitle">Buổi ${session.id} · ${session.title}</p>
          </div>
          ${isEdit ? '<span class="badge badge-success">Đã hoàn thành</span>' : '<span class="badge badge-warning">Chưa viết nhật ký</span>'}
        </div>

        <div id="journal-error" class="alert alert-danger" style="display:none"></div>
        <div id="journal-success" class="alert alert-success" style="display:none"></div>

        <form id="journal-form">
          <!-- Active Recall Section -->
          <div class="journal-section">
            <h3 class="journal-section-title">🧠 1. Active Recall — Khôi phục kiến thức</h3>
            <p class="journal-section-desc">
              Hãy cố gắng nhớ lại và ghi lại những kiến thức quan trọng nhất trong buổi học này. 
              <strong>Mẹo:</strong> Không cần tra cứu lại sách vở hay slide! Viết tất cả từ trí nhớ của bạn để kích thích não bộ truy hồi.
            </p>
            <div class="form-group">
              <label class="form-label">Tự viết lại những gì bạn học được (tối thiểu 20 ký tự):</label>
              <textarea class="form-input" id="recall_text" name="recall_text" placeholder="Hôm nay tôi đã học được các kiến thức về..." required minlength="20" style="min-height: 180px">${journal?.recall_text || ''}</textarea>
            </div>
          </div>

          <!-- Question Bank Section -->
          <div class="journal-section">
            <h3 class="journal-section-title">❓ 2. Question Bank — Vùng nghi vấn</h3>
            <p class="journal-section-desc">
              Ghi lại những câu hỏi, khía cạnh bạn chưa hiểu rõ hoặc muốn tự tìm tòi nghiên cứu thêm, hoặc muốn giảng viên giải thích thêm.
            </p>
            <div class="form-group">
              <label class="form-label">Câu hỏi của bạn (nếu có):</label>
              <textarea class="form-input" id="questions_text" name="questions_text" placeholder="Những điểm tôi còn băn khoăn hay muốn hỏi thêm là..." style="min-height: 100px">${journal?.questions_text || ''}</textarea>
            </div>
          </div>

          <!-- Goal Check Section -->
          <div class="journal-section">
            <h3 class="journal-section-title">🎯 3. Goal Check — Đánh giá mục tiêu</h3>
            <p class="journal-section-desc">
              Buổi học này đã giúp bạn đạt được bao nhiêu phần trăm kỳ vọng của bản thân? Bạn đã tiệm cận các mục tiêu cốt lõi chưa?
            </p>
            <div style="display:flex; flex-direction:column; gap:1.25rem">
              <div class="form-group" style="margin-bottom:0">
                <label class="form-label">Mức độ hoàn thành mục tiêu học tập:</label>
                <div class="star-rating">
                  <input type="radio" id="star5" name="goal_rating" value="5" ${(journal?.goal_rating == 5) ? 'checked' : ''} required />
                  <label for="star5" title="Xuất sắc">★</label>
                  <input type="radio" id="star4" name="goal_rating" value="4" ${(journal?.goal_rating == 4) ? 'checked' : ''} />
                  <label for="star4" title="Tốt">★</label>
                  <input type="radio" id="star3" name="goal_rating" value="3" ${(journal?.goal_rating == 3 || !journal) ? 'checked' : ''} />
                  <label for="star3" title="Trung bình">★</label>
                  <input type="radio" id="star2" name="goal_rating" value="2" ${(journal?.goal_rating == 2) ? 'checked' : ''} />
                  <label for="star2" title="Yếu">★</label>
                  <input type="radio" id="star1" name="goal_rating" value="1" ${(journal?.goal_rating == 1) ? 'checked' : ''} />
                  <label for="star1" title="Rất yếu">★</label>
                </div>
              </div>
              
              <div class="form-group" style="margin-bottom:0">
                <label class="form-label">Ghi chú tự đánh giá hoặc kế hoạch khắc phục:</label>
                <textarea class="form-input" id="goal_note" name="goal_note" placeholder="Kế hoạch tự học tiếp theo hoặc tự nhắc nhở bản thân..." style="min-height: 80px">${journal?.goal_note || ''}</textarea>
              </div>
            </div>
          </div>

          <!-- Mood Emoji Section -->
          <div class="journal-section">
            <h3 class="journal-section-title">😊 4. Cảm xúc buổi học</h3>
            <p class="journal-section-desc">Hãy chia sẻ trạng thái tâm lý/năng lượng của bạn sau buổi học này.</p>
            
            <div class="mood-selector">
              <div class="mood-option ${(journal?.mood === '🔥') ? 'selected' : ''}" data-mood="🔥">
                <span>🔥</span>
                <span class="mood-label">Tràn trề</span>
              </div>
              <div class="mood-option ${(journal?.mood === '😊' || !journal) ? 'selected' : ''}" data-mood="😊">
                <span>😊</span>
                <span class="mood-label">Vui vẻ</span>
              </div>
              <div class="mood-option ${(journal?.mood === '😐') ? 'selected' : ''}" data-mood="😐">
                <span>😐</span>
                <span class="mood-label">Bình thường</span>
              </div>
              <div class="mood-option ${(journal?.mood === '😵') ? 'selected' : ''}" data-mood="😵">
                <span>😵</span>
                <span class="mood-label">Mệt mỏi</span>
              </div>
              <div class="mood-option ${(journal?.mood === '😴') ? 'selected' : ''}" data-mood="😴">
                <span>😴</span>
                <span class="mood-label">Buồn ngủ</span>
              </div>
            </div>
            <input type="hidden" name="mood" id="selected-mood" value="${journal?.mood || '😊'}" />
          </div>

          <div style="display:flex; gap:1rem; margin-top:2rem">
            <button type="submit" class="btn btn-primary btn-lg" style="flex:1" id="btn-save">
              💾 ${isEdit ? 'Cập nhật nhật ký' : 'Gửi nhật ký học tập'}
            </button>
            <a href="#/course" class="btn btn-secondary btn-lg">Hủy bỏ</a>
          </div>
        </form>
      </div>
    </div>
  `;

  // Add emoji mood click handler
  const moodOptions = document.querySelectorAll('.mood-option');
  const moodInput = document.getElementById('selected-mood');
  moodOptions.forEach(opt => {
    opt.addEventListener('click', () => {
      moodOptions.forEach(o => o.classList.remove('selected'));
      opt.classList.add('selected');
      moodInput.value = opt.getAttribute('data-mood');
    });
  });

  // Handle Form submit
  const form = document.getElementById('journal-form');
  const errorEl = document.getElementById('journal-error');
  const successEl = document.getElementById('journal-success');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    errorEl.style.display = 'none';
    successEl.style.display = 'none';

    const btnSave = document.getElementById('btn-save');
    btnSave.disabled = true;
    btnSave.textContent = 'Đang lưu nhật ký...';

    const formData = new FormData(form);
    const data = Object.fromEntries(formData);

    try {
      if (isEdit) {
        await api.put(`/journal/${sessionId}`, data);
        successEl.textContent = 'Cập nhật nhật ký buổi học thành công!';
      } else {
        await api.post(`/journal/${sessionId}`, data);
        successEl.textContent = 'Lưu nhật ký buổi học thành công! Chúc bạn học tập tốt!';
      }
      successEl.style.display = 'block';
      window.scrollTo({ top: 0, behavior: 'smooth' });

      // Navigate to /journal after 1.5s
      setTimeout(() => {
        navigate('/journal');
      }, 1500);
    } catch (err) {
      errorEl.textContent = err.message;
      errorEl.style.display = 'block';
      window.scrollTo({ top: 0, behavior: 'smooth' });
      btnSave.disabled = false;
      btnSave.textContent = isEdit ? '💾 Cập nhật nhật ký' : '💾 Gửi nhật ký học tập';
    }
  });
}
