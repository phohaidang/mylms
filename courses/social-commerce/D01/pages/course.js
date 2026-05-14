import { api, getUser } from '../api.js';

export async function renderCourse(app) {
  app.innerHTML = `<div class="container page"><div class="loading"><div class="spinner"></div></div></div>`;
  const user = getUser() || {};
  
  let sessions = [];
  let courseMeta = { name: 'Thương mại Xã hội', code: 'ITS717' };
  let quizMap = {};
  let attendanceSet = new Set();
  let examResults = {};

  try {
    const data = await api.get('/courses/sessions');
    if (Array.isArray(data)) {
      sessions = data;
    } else if (data && data.sessions) {
      sessions = data.sessions;
      courseMeta = data.course || courseMeta;
    }

    const quizAttempts = await api.get('/quizzes/my/attempts') || [];
    quizAttempts.forEach(a => { quizMap[a.session_number] = a; });

    const attendanceData = await api.get('/feedback/my-attendance') || [];
    attendanceSet = new Set(attendanceData);

    // Check exam results
    for (const s of sessions) {
      if (s.hasExam && s.examId) {
        try {
          const result = await api.get(`/exams/${s.examId}/my-result`);
          examResults[s.examId] = result;
        } catch {}
      }
    }
  } catch (err) {
    console.error('Fetch course data failed', err);
  }

  // Lọc và hiển thị danh sách
  const sessionListHtml = sessions.map(s => {
    const paddedId = s.id.toString().padStart(2, '0');
    return `
      <div class="session-card">
        <div class="session-info">
          <div class="session-id">BUỔI ${paddedId}</div>
          <h3 class="session-title">${s.title}</h3>
          <p class="session-topics">${s.topics}</p>
        </div>
        <div class="session-actions">
          <a href="#/course/lesson/${s.id}" class="btn btn-primary">Chi tiết</a>
          ${s.hasExam ? `<a href="#/exam/${s.examId}" class="btn btn-outline">Kiểm tra</a>` : ''}
        </div>
      </div>
    `;
  }).join('');

  app.innerHTML = `
    <div class="container page">
      <div class="page-header">
        <div class="page-title-group">
          <div class="page-icon">📚</div>
          <h1 class="page-title">${courseMeta.name}</h1>
        </div>
        <p class="page-subtitle">${courseMeta.code} — ${sessions.length} buổi học &middot; ${courseMeta.chapters || 9} chương</p>
      </div>

      <div class="sessions-grid">
        ${sessionListHtml || '<p>Đang tải danh sách buổi học...</p>'}
      </div>
    </div>
  `;
}
