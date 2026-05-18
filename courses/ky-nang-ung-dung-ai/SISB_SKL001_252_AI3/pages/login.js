import { api, setToken, setUser, isLoggedIn } from '../api.js';
import { navigate } from '../router.js';

export function renderLogin(app) {
  if (isLoggedIn()) {
    navigate('/dashboard');
    return;
  }

  app.innerHTML = `
    <div class="auth-page">
      <div class="auth-card">
        <div class="auth-logo">
          <div class="auth-logo-icon">🎓</div>
          <h1>LMS Hub</h1>
          <p>Hệ thống quản lý học tập</p>
        </div>

        <div id="auth-error" class="alert alert-danger" style="display:none"></div>
        <div id="auth-success" class="alert alert-success" style="display:none"></div>

        <!-- Login Form -->
        <form id="auth-form">
          <div class="form-group">
            <label class="form-label">Email trường</label>
            <input type="email" class="form-input" name="email" placeholder="mssv@hub.edu.vn" required>
          </div>
          
          <div class="form-group">
            <label class="form-label">Mật khẩu</label>
            <input type="password" class="form-input" name="password" placeholder="Mật khẩu của bạn" required>
          </div>

          <button type="submit" class="btn btn-primary btn-block btn-lg" id="auth-submit">
            🔐 Đăng nhập
          </button>
        </form>

        <!-- Reset Password Form (hidden by default) -->
        <form id="reset-form" style="display:none">
          <div class="form-group">
            <label class="form-label">Email trường</label>
            <input type="email" class="form-input" name="reset-email" placeholder="mssv@hub.edu.vn" required>
          </div>
          
          <div class="form-group">
            <label class="form-label">Mã số sinh viên (MSSV)</label>
            <input type="text" class="form-input" name="reset-mssv" placeholder="VD: 2151050123" required>
          </div>

          <button type="submit" class="btn btn-primary btn-block btn-lg" id="reset-submit">
            🔄 Đặt lại mật khẩu
          </button>
        </form>

        <div class="auth-toggle" style="font-size: 0.85rem; margin-top: 1rem; text-align: center;">
          <a href="#" id="toggle-reset" style="color: var(--primary); cursor: pointer; text-decoration: none;">
            Quên mật khẩu?
          </a>
        </div>
      </div>
    </div>
  `;

  const loginForm = document.getElementById('auth-form');
  const resetForm = document.getElementById('reset-form');
  const errorEl = document.getElementById('auth-error');
  const successEl = document.getElementById('auth-success');
  const toggleBtn = document.getElementById('toggle-reset');
  let isResetMode = false;

  // Toggle between login and reset forms
  toggleBtn.addEventListener('click', (e) => {
    e.preventDefault();
    isResetMode = !isResetMode;
    errorEl.style.display = 'none';
    successEl.style.display = 'none';

    if (isResetMode) {
      loginForm.style.display = 'none';
      resetForm.style.display = 'block';
      toggleBtn.textContent = '← Quay lại Đăng nhập';
    } else {
      loginForm.style.display = 'block';
      resetForm.style.display = 'none';
      toggleBtn.textContent = 'Quên mật khẩu?';
    }
  });

  // Login submit
  loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const btn = document.getElementById('auth-submit');
    btn.disabled = true;
    btn.textContent = 'Đang xử lý...';
    errorEl.style.display = 'none';
    successEl.style.display = 'none';

    const formData = new FormData(loginForm);
    const data = Object.fromEntries(formData);

    try {
      const result = await api.post('/auth/login', data);
      setToken(result.token);
      setUser(result.user);
      navigate('/dashboard');
    } catch (err) {
      errorEl.textContent = err.message;
      errorEl.style.display = 'block';
      btn.disabled = false;
      btn.textContent = '🔐 Đăng nhập';
    }
  });

  // Reset password submit
  resetForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const btn = document.getElementById('reset-submit');
    btn.disabled = true;
    btn.textContent = 'Đang xử lý...';
    errorEl.style.display = 'none';
    successEl.style.display = 'none';

    const email = resetForm.querySelector('[name="reset-email"]').value;
    const student_id = resetForm.querySelector('[name="reset-mssv"]').value;

    try {
      const result = await api.post('/auth/reset-password', { email, student_id });
      successEl.textContent = result.message;
      successEl.style.display = 'block';
      
      // Auto switch back to login after 3 seconds
      setTimeout(() => {
        toggleBtn.click();
      }, 3000);
    } catch (err) {
      errorEl.textContent = err.message;
      errorEl.style.display = 'block';
    } finally {
      btn.disabled = false;
      btn.textContent = '🔄 Đặt lại mật khẩu';
    }
  });
}

