import { Router } from 'express';
import db from '../services/sheets.js';
import { authenticate, adminOnly } from '../middleware/auth.js';

const router = Router();

/**
 * POST /api/admin/backup
 * Create a backup of the spreadsheet on Google Drive
 */
router.post('/backup', authenticate, adminOnly, async (req, res) => {
  try {
    const result = await db.createBackup();
    res.json(result);
  } catch (err) {
    res.status(500).json({ error: 'Không thể tạo bản sao lưu' });
  }
});

/**
 * GET /api/admin/export
 * Download all data as JSON
 */
router.get('/export', authenticate, adminOnly, async (req, res) => {
  try {
    const data = await db.exportAllData();
    const timestamp = new Date().toISOString().split('T')[0];
    const filename = `lms_backup_${timestamp}.json`;
    
    res.setHeader('Content-Type', 'application/json');
    res.setHeader('Content-Disposition', `attachment; filename=${filename}`);
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: 'Không thể xuất dữ liệu' });
  }
});

export default router;
