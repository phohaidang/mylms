/**
 * LMS Hub — Social Commerce — Lớp D01 (DEBUG MODE)
 */
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { config } from 'dotenv';

const __dirname = dirname(fileURLToPath(import.meta.url));

// Load .env from class directory (local testing)
config({ path: join(__dirname, '..', '.env') });

export default async function handler(req, res) {
  try {
    // Dynamically import to catch startup errors
    const { createApp } = await import('../core/server/index.js');
    
    const courseDir = join(__dirname, '..');
    const classDir = join(__dirname, '..');
    
    const app = createApp({ courseDir, classDir });
    
    // Manual handling for Express in Vercel Function
    return app(req, res);
  } catch (err) {
    console.error('SERVER CRASH:', err);
    res.status(500).json({
      error: 'Server crashed during startup',
      message: err.message,
      stack: err.stack,
      env_check: {
        has_sheets_id: !!process.env.GOOGLE_SHEETS_ID,
        has_service_account: !!process.env.GOOGLE_SERVICE_ACCOUNT_EMAIL,
        has_private_key: !!process.env.GOOGLE_PRIVATE_KEY
      }
    });
  }
}
