import { config } from 'dotenv';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';
import { readFileSync, existsSync } from 'fs';

const __dirname = dirname(fileURLToPath(import.meta.url));

// Load .env
config({ path: join(__dirname, '.env') });

// Load course-config.json
let courseConfig = { meta: {}, sessions: [] };
const configPath = join(__dirname, 'course-config.json');
if (existsSync(configPath)) {
  courseConfig = JSON.parse(readFileSync(configPath, 'utf-8'));
}

// Import createApp from synced core server
const { createApp } = await import('./_sync/server/index.js');

console.log('🚀 Khởi động Express API Server cục bộ...');
createApp({
  courseDir: __dirname,
  classDir: __dirname,
  contentDir: join(__dirname, 'content'),
  config: courseConfig
});
