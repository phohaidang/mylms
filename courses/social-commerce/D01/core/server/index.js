import express from 'express';
import { join } from 'path';
import { readFileSync, existsSync } from 'fs';
import cors from 'cors';
import morgan from 'morgan';
import compression from 'compression';
import cookieParser from 'cookie-parser';

// Import routers — MỘT SỐ là factory function, MỘT SỐ là default export
import { createCourseRouter } from './routes/courses.js';
import { createAuthRouter } from './routes/auth.js';
import ebookRouter from './routes/ebook.js';
import quizRouter from './routes/quizzes.js';
import gradesRouter from './routes/grades.js';
import feedbackRouter from './routes/feedback.js';
import examRouter from './routes/exams.js';
import evidenceRouter from './routes/evidence.js';

/**
 * LMS App Factory
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

  // Routes — Factory functions cho courses và auth, default export cho phần còn lại
  app.use('/api/auth', createAuthRouter(options));
  app.use('/api/courses', createCourseRouter({ ...options, courseConfig: app.locals.courseConfig }));
  app.use('/api/ebook', ebookRouter);
  app.use('/api/quizzes', quizRouter);
  app.use('/api/grades', gradesRouter);
  app.use('/api/feedback', feedbackRouter);
  app.use('/api/exams', examRouter);
  app.use('/api/evidence', evidenceRouter);

  return app;
}
