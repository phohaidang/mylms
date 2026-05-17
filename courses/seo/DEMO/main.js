import { route, startRouter, navigate } from './router.js';
import { isLoggedIn, isAdmin, getUser, clearToken } from './api.js';
import { renderLogin } from './pages/login.js';
import { renderDashboard } from './pages/dashboard.js';
import { renderCourse } from './pages/course.js';
import { renderLesson } from './pages/lesson.js';
import { renderEbookIndex } from './pages/ebook/index.js';
import { renderEbookChapter } from './pages/ebook/chapter.js';
import { renderEbookTest } from './pages/ebook/test.js';
import { renderQuiz } from './pages/quiz.js';
import { renderQuizResult } from './pages/quiz-result.js';
import { renderExam } from './pages/exam.js';
import { renderGrades } from './pages/grades.js';
import { renderChangePassword } from './pages/change-password.js';
import { renderAdminDashboard } from './pages/admin/dashboard.js';
import { renderAdminGrades } from './pages/admin/grades.js';
import { renderAdminEvidence } from './pages/admin/evidence.js';
import { renderTeacher } from './pages/teacher.js';
import { renderStudentBoard } from './pages/student-board.js';
import { renderGoalsPage } from './pages/goals.js';


// ── Navbar Component ──
function renderNavbar() {
  const user = getUser();
  if (!user) return '';
  
  // Don't show full navbar if password change is required
  if (user.must_change_password) {
    return `
      <nav class="navbar">
        <div class="navbar-top">
          <div class="navbar-inner">
            <div class="navbar-brand">
              <div class="brand-icon">🎓</div>
              <span>LMS Hub</span>
            </div>
            <div class="navbar-user">
              <button class="btn-logout" id="btn-logout">Đăng xuất</button>
            </div>
          </div>
        </div>
      </nav>
    `;
  }

  const adminLinks = isAdmin() ? `
    <li><a href="#/admin/dashboard" class="${location.hash.includes('admin') ? 'active' : ''}">🛠 Admin</a></li>
  ` : '';
  
  return `
    <nav class="navbar">
      <div class="navbar-top">
        <div class="navbar-inner">
          <a href="#/dashboard" class="navbar-brand">
            <div class="brand-icon">🎓</div>
            <span>LMS Hub</span>
          </a>
          <ul class="navbar-nav">
            <li><a href="#/dashboard" class="${location.hash === '#/dashboard' ? 'active' : ''}">📊 Dashboard</a></li>
            <li><a href="#/course" class="${location.hash === '#/course' ? 'active' : ''}">📚 Buổi học</a></li>
            <li><a href="#/ebook" class="${location.hash.startsWith('#/ebook') ? 'active' : ''}">📖 eBook</a></li>
            <li><a href="#/teacher" class="${location.hash === '#/teacher' ? 'active' : ''}">👨‍🏫 Thầy Đăng</a></li>
            <li><a href="#/board" class="${location.hash === '#/board' ? 'active' : ''}">🏆 Lớp học</a></li>
            <li><a href="#/grades" class="${location.hash === '#/grades' ? 'active' : ''}">📋 Bảng điểm</a></li>
            ${adminLinks}
          </ul>
        </div>
      </div>
      <div class="navbar-bottom">
        <div class="navbar-inner" style="height: 40px">
          <div class="navbar-tagline" style="font-size: 0.85rem; color: var(--text-secondary); font-weight: 500; letter-spacing: 0.3px">
            Dạy bằng <span style="color: var(--accent)">TÂM</span> — Dẫn lối bằng <span style="color: var(--accent)">TRI THỨC</span> — Đồng hành bằng <span style="color: var(--accent)">CÂU CHUYỆN THẬT</span>
          </div>
          <div class="navbar-user">
            <span class="user-name">Đang đăng nhập: <strong>${user.full_name}</strong></span>
            <button class="btn-logout" id="btn-logout" style="padding: 0.2rem 0.6rem">Đăng xuất</button>
          </div>
        </div>
      </div>
    </nav>
  `;
}

// ── Auth Guard ──
function requireAuth(handler) {
  return (app, params) => {
    if (!isLoggedIn()) {
      navigate('/login');
      return;
    }
    const user = getUser();
    if (user && user.must_change_password && location.hash !== '#/change-password') {
      navigate('/change-password');
      return;
    }
    return handler(app, params);
  };
}

function withNavbar(handler) {
  return async (app, params) => {
    app.innerHTML = renderNavbar() + '<main id="page-content"></main>';
    
    // Logout button
    document.getElementById('btn-logout')?.addEventListener('click', () => {
      clearToken();
      navigate('/login');
    });
    
    const content = document.getElementById('page-content');
    return handler(content, params);
  };
}

// ── Register Routes ──

// Auth
route('/login', renderLogin);
route('/register', renderLogin);
route('/change-password', requireAuth(withNavbar(renderChangePassword)));

// Student pages
route('/dashboard', requireAuth(withNavbar(renderDashboard)));
route('/course', requireAuth(withNavbar(renderCourse)));
route('/course/lesson/:id', requireAuth(withNavbar(renderLesson)));
route('/ebook', requireAuth(withNavbar(renderEbookIndex)));
route('/ebook/chapter/:id', requireAuth(withNavbar(renderEbookChapter)));
route('/ebook/chapter/:id/test/:level', requireAuth(withNavbar(renderEbookTest)));
route('/quiz/:sessionId', requireAuth(withNavbar(renderQuiz)));
route('/quiz/:sessionId/result', requireAuth(withNavbar(renderQuizResult)));
route('/exam/:examId', requireAuth(renderExam));
route('/grades', requireAuth(withNavbar(renderGrades)));
route('/teacher', requireAuth(withNavbar(renderTeacher)));
route('/board', requireAuth(withNavbar(renderStudentBoard)));
route('/goals', requireAuth(withNavbar(renderGoalsPage)));


// Admin pages
route('/admin/dashboard', requireAuth(withNavbar(renderAdminDashboard)));
route('/admin/grades', requireAuth(withNavbar(renderAdminGrades)));
route('/admin/evidence', requireAuth(withNavbar(renderAdminEvidence)));

// ── Start ──
startRouter();

// Default redirect
if (!location.hash) {
  navigate(isLoggedIn() ? '/dashboard' : '/login');
}
