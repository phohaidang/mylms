/**
 * LMS Hub — Social Commerce — Lớp D01
 */
import { config } from 'dotenv';
// Import trực tiếp file cấu hình để Vercel đóng gói vào bundle
import courseConfig from '../course-config.json' assert { type: 'json' };

// Load .env
config();

// Import app factory from local core copy
import { createApp } from '../core/server/index.js';

// Khởi tạo app với cấu hình đã import sẵn
const app = createApp({ 
  courseDir: process.cwd(), 
  classDir: process.cwd(),
  config: courseConfig // Truyền config trực tiếp vào
});

export default app;
