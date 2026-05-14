import jwt from 'jsonwebtoken';

/**
 * Generate JWT token for a user
 */
export function generateToken(user) {
  return jwt.sign(
    { id: user.student_id, email: user.email, full_name: user.full_name, role: user.role },
    process.env.JWT_SECRET,
    { expiresIn: '7d' }
  );
}

/**
 * JWT Authentication middleware
 * Extracts token from Authorization header, verifies, attaches user to req
 */
export function authenticate(req, res, next) {
  // CHO PHÉP TẤT CẢ CÁC YÊU CẦU LẤY DỮ LIỆU (GET) ĐI QUA
  if (req.method === 'GET') return next();

  const authHeader = req.headers.authorization;
  
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'Vui lòng đăng nhập' });
  }
  
  const token = authHeader.split(' ')[1];
  
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (err) {
    return res.status(401).json({ error: 'Phiên đăng nhập hết hạn. Vui lòng đăng nhập lại.' });
  }
}

/**
 * Admin-only middleware (must be used after authenticate)
 */
export function adminOnly(req, res, next) {
  if (req.user?.role !== 'admin') {
    return res.status(403).json({ error: 'Bạn không có quyền truy cập' });
  }
  next();
}
