/**
 * LMS Hub — App Factory
 * 
 * Creates an Express app configured for a specific course/class.
 * This is the SINGLE source of truth for the server — all classes share this code.
 * 
 * Usage (from a class entry point):
 *   import { createApp } from '../../../core/server/index.js';
 *   const app = createApp({ courseDir, classDir });
 *   export default app;
 */

import 'dotenv/config';
import express from 'express';
import cors from 'cors';
import morgan from 'morgan';
import { readFileSync, existsSync } from 'fs';
import { join } from 'path';

import authRoutes from './routes/auth.js';
import courseRoutes from './routes/courses.js';
import quizRoutes from './routes/quizzes.js';
import ebookRoutes from './routes/ebook.js';
import examRoutes from './routes/exams.js';
import gradeRoutes from './routes/grades.js';
import evidenceRoutes from './routes/evidence.js';
import feedbackRoutes from './routes/feedback.js';
import goalsRoutes from './routes/goals.js';
import boardRoutes from './routes/board.js';

/**
 * Create and configure the Express app
 * @param {Object} options
 * @param {string} options.courseDir - Path to the course directory (contains course-config.json, content/)
 * @param {string} options.classDir - Path to the class directory (contains .env)
 * @param {string} [options.contentDir] - Optional explicit content directory (defaults to courseDir/content)
 * @param {Object} [options.config] - Pre-loaded config (skips reading course-config.json)
 */
export function createApp({ courseDir, classDir, contentDir, config }) {
  const app = express();
  const PORT = process.env.PORT || 3000;

  // Load course configuration — ưu tiên config truyền vào
  if (config) {
    app.locals.courseConfig = config;
  } else {
    const configPath = join(courseDir, 'course-config.json');
    if (existsSync(configPath)) {
      app.locals.courseConfig = JSON.parse(readFileSync(configPath, 'utf-8'));
    } else {
      console.warn(`⚠️  course-config.json not found at ${configPath}`);
      app.locals.courseConfig = { meta: {}, sessions: [] };
    }
  }

  // Store paths for routes to use
  app.locals.courseDir = courseDir;
  app.locals.classDir = classDir;
  app.locals.contentDir = contentDir || join(courseDir, 'content');

  // Middleware
  app.use(cors());
  if (process.env.NODE_ENV !== 'production') {
    app.use(morgan('dev'));
  }
  app.use(express.json({ limit: '10mb' }));

  // Static files — served from content directory
  const cDir = app.locals.contentDir;
  app.use('/lessons', express.static(join(cDir, 'lessons')));
  app.use('/slides', express.static(join(cDir, 'slides')));
  app.use('/images', express.static(join(cDir, 'images')));

  // API Routes
  app.use('/api/auth', authRoutes);
  app.use('/api/courses', courseRoutes);
  app.use('/api/quizzes', quizRoutes);
  app.use('/api/ebook', ebookRoutes);
  app.use('/api/exams', examRoutes);
  app.use('/api/grades', gradeRoutes);
  app.use('/api/evidence', evidenceRoutes);
  app.use('/api/feedback', feedbackRoutes);
  app.use('/api/goals', goalsRoutes);
  app.use('/api/board', boardRoutes);

  // Root route
  app.get('/', (req, res) => {
    const meta = app.locals.courseConfig.meta || {};
    res.send(`
      <html>
        <body style="font-family: sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; background: #f0f2f5;">
          <div style="background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center;">
            <h1 style="color: #1a73e8;">LMS Hub API — ${meta.code || process.env.COURSE_CODE}</h1>
            <p>${meta.name || process.env.COURSE_NAME || 'LMS Hub'}</p>
            <hr style="margin: 1.5rem 0; border: 0; border-top: 1px solid #eee;">
            <p>Server is running on port ${PORT}</p>
          </div>
        </body>
      </html>
    `);
  });

  // Health check
  app.get('/api/health', (req, res) => {
    res.json({
      status: 'ok',
      course: app.locals.courseConfig.meta?.code || process.env.COURSE_CODE,
      name: app.locals.courseConfig.meta?.name || process.env.COURSE_NAME,
      timestamp: new Date().toISOString()
    });
  });

  // Serve frontend in production
  if (process.env.NODE_ENV === 'production') {
    const distDir = join(classDir, 'dist');
    if (existsSync(distDir)) {
      app.use(express.static(distDir));
      app.get('*', (req, res) => {
        res.sendFile(join(distDir, 'index.html'));
      });
    }
  }

  // Start server (only when not on Vercel)
  if (!process.env.VERCEL) {
    app.listen(PORT, () => {
      const meta = app.locals.courseConfig.meta || {};
      console.log(`
  ╔═══════════════════════════════════════════════╗
  ║         LMS Hub — ${meta.code || ''}
  ║         ${meta.name || ''}
  ║         http://localhost:${PORT}
  ╚═══════════════════════════════════════════════╝
      `);
    });
  }

  return app;
}
