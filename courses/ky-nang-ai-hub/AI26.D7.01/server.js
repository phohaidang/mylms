import { config } from 'dotenv';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { readFileSync, existsSync } from 'fs';

const __dirname = dirname(fileURLToPath(import.meta.url));
config({ path: join(__dirname, '.env') });

process.env.PORT = process.env.PORT || '3016';
process.env.ADMIN_EMAIL = process.env.ADMIN_EMAIL || 'dangph@hub.edu.vn';
process.env.ADMIN_PASSWORD = process.env.ADMIN_PASSWORD || 'admin2026';
process.env.ADMIN_NAME = process.env.ADMIN_NAME || 'ThS. Phó Hải Đăng';
process.env.COURSE_CODE = process.env.COURSE_CODE || 'AI26.D7.01';
process.env.COURSE_NAME = process.env.COURSE_NAME || 'Kỹ năng ứng dụng AI trong học tập và nghiên cứu (AI26.D7.01)';
process.env.ALLOWED_EMAIL_DOMAIN = process.env.ALLOWED_EMAIL_DOMAIN || 'st.hub.edu.vn';
process.env.JWT_SECRET = process.env.JWT_SECRET || 'jwt-secret-ai26-d7-01-hub-20261123';
process.env.JWT_EXPIRES_IN = process.env.JWT_EXPIRES_IN || '24h';
process.env.ALLOW_SELF_REGISTER = process.env.ALLOW_SELF_REGISTER || 'true';

let courseConfig = { meta: {}, sessions: [] };
const configPath = join(__dirname, 'course-config.json');
if (existsSync(configPath)) {
  courseConfig = JSON.parse(readFileSync(configPath, 'utf-8'));
}

const { createApp } = await import('./_sync/server/index.js');
console.log('🚀 Starting local backend server for AI26.D7.01...');
createApp({ 
  courseDir: __dirname,
  classDir: __dirname,
  contentDir: join(__dirname, 'content'),
  config: courseConfig
});
