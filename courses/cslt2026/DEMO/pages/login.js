import { api, setToken, setUser, isLoggedIn } from '../api.js';
import { navigate } from '../router.js';

export async function renderLogin(app) {
  if (isLoggedIn()) {
    navigate('/dashboard');
    return;
  }

  // Check if self-registration is enabled
  let allowSelfRegister = false;
  try {
    const config = await api.get('/auth/config');
    allowSelfRegister = config.allowSelfRegister;
  } catch (e) {
    // If config endpoint fails, default to no registration
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
            <label class="form-label">Email</label>
            <input type="email" class="form-input" name="email" placeholder="${allowSelfRegister ? 'your@email.com' : 'mssv@hub.edu.vn'}" required>
          </div>
          
          <div class="form-group">
            <label class="form-label">Mật khẩu</label>
            <input type="password" class="form-input" name="password" placeholder="Mật khẩu của bạn" required>
          </div>

          <button type="submit" class="btn btn-primary btn-block btn-lg" id="auth-submit">
            🔐 Đăng nhập
          </button>
        </form>

        <!-- Register Form (hidden by default, only shown when allowSelfRegister) -->
        <form id="register-form" style="display:none">
          <div class="form-group">
            <label class="form-label">Họ và tên</label>
            <input type="text" class="form-input" name="full_name" placeholder="Nguyễn Văn A" required>
          </div>

          <div class="form-group">
            <label class="form-label">Email</label>
            <input type="email" class="form-input" name="email" placeholder="your@email.com" required>
          </div>
          
          <div class="form-group">
            <label class="form-label">Mật khẩu</label>
            <input type="password" class="form-input" name="password" placeholder="Ít nhất 6 ký tự" required minlength="6">
          </div>

          <div class="form-group">
            <label class="form-label">Xác nhận mật khẩu</label>
            <input type="password" class="form-input" name="password_confirm" placeholder="Nhập lại mật khẩu" required minlength="6">
          </div>

          <button type="submit" class="btn btn-primary btn-block btn-lg" id="register-submit">
            ✨ Đăng ký
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
          ${allowSelfRegister 
            ? '<a href="#" id="toggle-register" style="color: var(--primary); cursor: pointer; text-decoration: none;">Chưa có tài khoản? Đăng ký</a>'
            : '<a href="#" id="toggle-reset" style="color: var(--primary); cursor: pointer; text-decoration: none;">Quên mật khẩu?</a>'
          }
        </div>
      </div>
    </div>
  `;

  const loginForm = document.getElementById('auth-form');
  const resetForm = document.getElementById('reset-form');
  const registerForm = document.getElementById('register-form');
  const errorEl = document.getElementById('auth-error');
  const successEl = document.getElementById('auth-success');

  // === MODE TOGGLE ===
  let currentMode = 'login'; // 'login' | 'register' | 'reset'

  function switchMode(mode) {
    currentMode = mode;
    errorEl.style.display = 'none';
    successEl.style.display = 'none';
    loginForm.style.display = 'none';
    registerForm.style.display = 'none';
    resetForm.style.display = 'none';

    const toggleEl = document.querySelector('.auth-toggle');

    if (mode === 'login') {
      loginForm.style.display = 'block';
      if (allowSelfRegister) {
        toggleEl.innerHTML = '<a href="#" id="toggle-register" style="color: var(--primary); cursor: pointer; text-decoration: none;">Chưa có tài khoản? Đăng ký</a>';
      } else {
        toggleEl.innerHTML = '<a href="#" id="toggle-reset" style="color: var(--primary); cursor: pointer; text-decoration: none;">Quên mật khẩu?</a>';
      }
    } else if (mode === 'register') {
      registerForm.style.display = 'block';
      toggleEl.innerHTML = '<a href="#" id="toggle-login" style="color: var(--primary); cursor: pointer; text-decoration: none;">← Đã có tài khoản? Đăng nhập</a>';
    } else if (mode === 'reset') {
      resetForm.style.display = 'block';
      toggleEl.innerHTML = '<a href="#" id="toggle-login" style="color: var(--primary); cursor: pointer; text-decoration: none;">← Quay lại Đăng nhập</a>';
    }

    // Re-attach toggle listeners
    const toggleRegister = document.getElementById('toggle-register');
    const toggleLogin = document.getElementById('toggle-login');
    const toggleReset = document.getElementById('toggle-reset');
    
    if (toggleRegister) toggleRegister.addEventListener('click', (e) => { e.preventDefault(); switchMode('register'); });
    if (toggleLogin) toggleLogin.addEventListener('click', (e) => { e.preventDefault(); switchMode('login'); });
    if (toggleReset) toggleReset.addEventListener('click', (e) => { e.preventDefault(); switchMode('reset'); });
  }

  // Initial toggle setup
  const initToggleRegister = document.getElementById('toggle-register');
  const initToggleReset = document.getElementById('toggle-reset');
  if (initToggleRegister) initToggleRegister.addEventListener('click', (e) => { e.preventDefault(); switchMode('register'); });
  if (initToggleReset) initToggleReset.addEventListener('click', (e) => { e.preventDefault(); switchMode('reset'); });

  // === LOGIN SUBMIT ===
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

  // === REGISTER SUBMIT ===
  if (registerForm) {
    registerForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const btn = document.getElementById('register-submit');
      btn.disabled = true;
      btn.textContent = 'Đang xử lý...';
      errorEl.style.display = 'none';
      successEl.style.display = 'none';

      const formData = new FormData(registerForm);
      const data = Object.fromEntries(formData);

      // Validate password match
      if (data.password !== data.password_confirm) {
        errorEl.textContent = 'Mật khẩu xác nhận không khớp';
        errorEl.style.display = 'block';
        btn.disabled = false;
        btn.textContent = '✨ Đăng ký';
        return;
      }

      try {
        const result = await api.post('/auth/register', {
          full_name: data.full_name,
          email: data.email,
          password: data.password
        });
        // Auto-login on successful registration
        setToken(result.token);
        setUser(result.user);
        navigate('/dashboard');
      } catch (err) {
        errorEl.textContent = err.message;
        errorEl.style.display = 'block';
        btn.disabled = false;
        btn.textContent = '✨ Đăng ký';
      }
    });
  }

  // === RESET PASSWORD SUBMIT ===
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
        switchMode('login');
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
