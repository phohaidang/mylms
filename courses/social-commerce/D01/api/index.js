/**
 * LMS Hub — Social Commerce — Lớp D01
 */
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { readFileSync, existsSync } from 'fs';
import { config } from 'dotenv';

const __dirname = dirname(fileURLToPath(import.meta.url));

// Load .env
config();

// Nạp JSON theo cách đã xác nhận chạy được
const configPath = join(__dirname, '..', 'course-config.json');
let courseConfig = { meta: {}, sessions: [] };
try {
  courseConfig = JSON.parse(readFileSync(configPath, 'utf-8'));
} catch (err) {
  console.error('Failed to load course-config.json', err);
}

// Import app factory from local core
import { createApp } from '../core/server/index.js';

// Dùng process.cwd() cho các thư mục tĩnh trên Vercel
const rootDir = process.cwd();

const app = createApp({ 
  courseDir: rootDir, 
  classDir: rootDir,
  config: courseConfig
});

export default app;
