/**
 * LMS Hub — Social Commerce — Lớp D01
 */
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { readFileSync } from 'fs';
import { config } from 'dotenv';

const __dirname = dirname(fileURLToPath(import.meta.url));

// Import config directly to ensure bundling
import courseConfig from '../course-config.json' assert { type: 'json' };

// Load .env
config();

// Import app factory from local core
import { createApp } from '../core/server/index.js';

const rootDir = join(__dirname, '..');

const app = createApp({ 
  courseDir: rootDir, 
  classDir: rootDir,
  config: courseConfig
});

export default app;
