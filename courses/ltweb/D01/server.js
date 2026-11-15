import { config } from 'dotenv';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { readFileSync, existsSync } from 'fs';

const __dirname = dirname(fileURLToPath(import.meta.url));
config({ path: join(__dirname, '.env') });

// Load course config (synced from course level)
let courseConfig = { meta: {}, sessions: [] };
const configPath = join(__dirname, 'course-config.json');
if (existsSync(configPath)) {
  courseConfig = JSON.parse(readFileSync(configPath, 'utf-8'));
}

const { createApp } = await import('./_sync/server/index.js');

console.log('🚀 Starting local backend server...');
createApp({ 
  courseDir: __dirname,
  classDir: __dirname,
  contentDir: join(__dirname, 'content'),
  config: courseConfig
});
