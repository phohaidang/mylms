import express from 'express';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { readFileSync, existsSync } from 'fs';
import cors from 'cors';
import morgan from 'morgan';
import compression from 'compression';
import cookieParser from 'cookie-parser';

const __dirname = dirname(fileURLToPath(import.meta.url));

import { createAuthRouter } from './routes/auth.js';
import { createCourseRouter } from './routes/courses.js';
import { createEbookRouter } from './routes/ebook.js';
import { createQuizRouter } from './routes/quizzes.js';
import { createGradesRouter } from './routes/grades.js';
import { createFeedbackRouter } from './routes/feedback.js';
import { createExamRouter } from './routes/exams.js';
import { createEvidenceRouter } from './routes/evidence.js';

/**
 * LMS App Factory
 * @param {Object} options
 * @param {string} options.courseDir - Path to the course directory
 * @param {string} options.classDir - Path to the class directory
 * @param {Object} options.config - Pre-loaded configuration object
 */
export function createApp(options) {
  const { courseDir, classDir, contentDir } = options;
  const app = express();

  // Load course configuration
  if (options.config) {
    app.locals.courseConfig = options.config;
  } else {
    const configPath = join(courseDir, 'course-config.json');
    if (existsSync(configPath)) {
      app.locals.courseConfig = JSON.parse(readFileSync(configPath, 'utf-8'));
    } else {
      app.locals.courseConfig = { meta: {}, sessions: [] };
    }
  }

  // Paths
  app.locals.courseDir = courseDir;
  app.locals.classDir = classDir;
  app.locals.contentDir = contentDir || join(courseDir, 'content');

  // Middleware
  app.use(express.json());
  app.use(express.urlencoded({ extended: true }));
  app.use(cookieParser());
  app.use(cors());
  app.use(compression());
  if (process.env.NODE_ENV !== 'production') {
    app.use(morgan('dev'));
  }

  // Routes
  // LƯU Ý: Truyền thẳng courseConfig vào để tránh việc router tự đọc lại file
  app.use('/api/auth', createAuthRouter(options));
  app.use('/api/courses', createCourseRouter({ ...options, courseConfig: app.locals.courseConfig }));
  app.use('/api/ebook', createEbookRouter(options));
  app.use('/api/quizzes', createQuizRouter(options));
  app.use('/api/grades', createGradesRouter(options));
  app.use('/api/feedback', createFeedbackRouter(options));
  app.use('/api/exams', createExamRouter(options));
  app.use('/api/evidence', createEvidenceRouter(options));

  return app;
}
