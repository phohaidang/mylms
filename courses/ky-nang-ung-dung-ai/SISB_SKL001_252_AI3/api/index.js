/**
 * LMS Hub — Kỹ năng sử dụng AI trong nghiên cứu, học tập — Lớp SISB_SKL001_252_AI3 (PRODUCTION)
 * 
 * Vercel Serverless Function entry point.
 * Imports createApp from synced core (populated by sync-deploy.js)
 */
import { config } from 'dotenv';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';
import { readFileSync, existsSync } from 'fs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const CLASS_DIR = join(__dirname, '..');                 // = SISB_SKL001_252_AI3/
const CONTENT_DIR = join(CLASS_DIR, 'content');          // = SISB_SKL001_252_AI3/content/ (synced from course)

config({ path: join(CLASS_DIR, '.env') });

// Load course config (synced from course level)
let courseConfig = { meta: {}, sessions: [] };
const configPath = join(CLASS_DIR, 'course-config.json');
if (existsSync(configPath)) {
  courseConfig = JSON.parse(readFileSync(configPath, 'utf-8'));
}

export default async function handler(req, res) {
  try {
    // Import from synced core (populated by: npm run sync ky-nang-ung-dung-ai SISB_SKL001_252_AI3)
    const { createApp } = await import('../_sync/server/index.js');
    
    const app = createApp({ 
      courseDir: CLASS_DIR,
      classDir: CLASS_DIR,
      contentDir: CONTENT_DIR,
      config: courseConfig
    });
    
    return app(req, res);
  } catch (err) {
    res.status(500).json({
      error: 'Server crashed',
      message: err.message,
      stack: err.stack?.split('\n').slice(0, 5)
    });
  }
}
