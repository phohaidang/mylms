/**
 * Local development server for daukhi2026 class
 * Run: node local-server.js
 */
import { config } from 'dotenv';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';
import { readFileSync, existsSync } from 'fs';

const __dirname = dirname(fileURLToPath(import.meta.url));
config({ path: join(__dirname, '.env') });

// Load course config
let courseConfig = { meta: {}, sessions: [] };
const configPath = join(__dirname, 'course-config.json');
if (existsSync(configPath)) {
  courseConfig = JSON.parse(readFileSync(configPath, 'utf-8'));
}

const { createApp } = await import('./_sync/server/index.js');

createApp({
  courseDir: __dirname,
  classDir: __dirname,
  contentDir: join(__dirname, 'content'),
  config: courseConfig
});
