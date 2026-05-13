/**
 * LMS Hub — Social Commerce — Lớp D01
 */
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { readFileSync } from 'fs';
import { config } from 'dotenv';

const __dirname = dirname(fileURLToPath(import.meta.url));

// Load .env
config();

// Nạp JSON theo cách thủ công để tránh lỗi cú pháp ESM trên Vercel
const configPath = join(__dirname, '..', 'course-config.json');
const courseConfig = JSON.parse(readFileSync(configPath, 'utf-8'));

// Import app factory from local core
import { createApp } from '../core/server/index.js';

const rootDir = join(__dirname, '..');

const app = createApp({ 
  courseDir: rootDir, 
  classDir: rootDir,
  config: courseConfig
});

export default app;
