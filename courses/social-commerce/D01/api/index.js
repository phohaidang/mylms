/**
 * LMS Hub — Social Commerce — Lớp D01
 * 
 * Entry point cho Vercel Serverless Function.
 * Chỉ cần file này + .env + vercel.json cho mỗi lớp.
 */
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { config } from 'dotenv';

const __dirname = dirname(fileURLToPath(import.meta.url));

// Load .env from class directory BEFORE importing core
config({ path: join(__dirname, '..', '.env') });

// Import app factory from core
// Path: api/ → D01/ → social-commerce/ → courses/ → lms-hub/ → core/server/
import { createApp } from '../../../../core/server/index.js';

const courseDir = join(__dirname, '..');  // Giờ đây nội dung đã nằm trong D01
const classDir = join(__dirname, '..');

const app = createApp({ courseDir, classDir });
export default app;
