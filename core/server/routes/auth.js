import { Router } from 'express';
import { authenticate, generateToken } from '../middleware/auth.js';
import { getSheetData, updateSheetData } from '../services/sheets.js';
import bcrypt from 'bcryptjs';

export function createAuthRouter(options) {
  const router = Router();

  router.post('/login', async (req, res) => {
    const { email, password } = req.body;
    try {
      const users = await getSheetData('users');
      const user = users.find(u => u.email === email);

      if (!user || !bcrypt.compareSync(password, user.password)) {
        return res.status(401).json({ error: 'Email hoặc mật khẩu không đúng' });
      }

      const token = generateToken(user);
      res.json({
        token,
        user: {
          id: user.student_id,
          email: user.email,
          full_name: user.full_name,
          role: user.role,
          must_change_password: user.password === 'Admin@2026' || user.password === '123456'
        }
      });
    } catch (err) {
      res.status(500).json({ error: 'Lỗi server: ' + err.message });
    }
  });

  // ... các routes khác cũng tương tự
  return router;
}
