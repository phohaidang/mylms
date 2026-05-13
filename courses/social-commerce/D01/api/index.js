/**
 * LMS Hub — Social Commerce — Lớp D01
 */
import { join } from 'path';
import { config } from 'dotenv';

// Load .env
config();

// Import app factory from local core copy
import { createApp } from '../core/server/index.js';

// On Vercel, process.cwd() is the Root Directory of the project
const rootDir = process.cwd();

const app = createApp({ 
  courseDir: rootDir, 
  classDir: rootDir 
});

export default app;
