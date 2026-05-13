/**
 * LMS Hub — Social Commerce — Lớp D01 (DEBUG MODE)
 */
import { readFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { config } from 'dotenv';

const __dirname = dirname(fileURLToPath(import.meta.url));

// Load .env
config();

export default async function handler(req, res) {
  try {
    // Nạp JSON theo cách an toàn nhất cho ESM
    const configPath = join(__dirname, '..', 'course-config.json');
    const courseConfig = JSON.parse(readFileSync(configPath, 'utf-8'));

    // Dynamically import core
    const { createApp } = await import('../core/server/index.js');
    
    const rootDir = join(__dirname, '..');
    const app = createApp({ 
      courseDir: rootDir, 
      classDir: rootDir,
      config: courseConfig
    });
    
    return app(req, res);
  } catch (err) {
    console.error('SERVER CRASH:', err);
    res.status(500).json({
      error: 'Server crashed during startup',
      message: err.message,
      stack: err.stack,
      path_attempted: join(__dirname, '..', 'course-config.json')
    });
  }
}
