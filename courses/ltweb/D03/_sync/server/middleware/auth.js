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
  const authHeader = req.headers.authorization;
  let token;
  if (authHeader && authHeader.startsWith('Bearer ')) {
    token = authHeader.split(' ')[1];
  } else if (req.query.token) {
    token = req.query.token;
  }
  
  if (!token) {
    return res.status(401).json({ error: 'Vui lòng đăng nhập' });
  }
  
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
