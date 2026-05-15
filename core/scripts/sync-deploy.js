#!/usr/bin/env node

/**
 * LMS Hub — Sync Deploy Script
 * 
 * Pre-deploy build script that syncs shared code into class directories
 * before deploying to Vercel.
 * 
 * Usage:
 *   node core/scripts/sync-deploy.js <course> <class>
 *   node core/scripts/sync-deploy.js social-commerce D01
 *   node core/scripts/sync-deploy.js --all  (sync all classes)
 * 
 * What it syncs:
 *   1. core/server/        → courses/{course}/{class}/_sync/server/
 *   2. courses/{course}/content/ → courses/{course}/{class}/content/
 *   3. courses/{course}/course-config.json → courses/{course}/{class}/course-config.json
 */

import { existsSync, readdirSync, statSync, cpSync, rmSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..', '..');
const CORE_SERVER = join(ROOT, 'core', 'server');
const COURSES_DIR = join(ROOT, 'courses');

// Files/dirs that indicate a class directory (not a course-level dir)
const CLASS_MARKERS = ['.env', '.env.example', 'api', 'vercel.json'];

function isClassDir(dirPath) {
  return CLASS_MARKERS.some(marker => existsSync(join(dirPath, marker)));
}

function syncDir(src, dest, label) {
  if (!existsSync(src)) {
    console.warn(`  ⚠️  Source not found: ${src}`);
    return;
  }

  // Remove existing dest to ensure clean sync
  if (existsSync(dest)) {
    rmSync(dest, { recursive: true });
  }

  cpSync(src, dest, { recursive: true });
  
  // Count files
  let fileCount = 0;
  function countFiles(dir) {
    const entries = readdirSync(dir);
    for (const entry of entries) {
      const fullPath = join(dir, entry);
      if (statSync(fullPath).isDirectory()) {
        countFiles(fullPath);
      } else {
        fileCount++;
      }
    }
  }
  countFiles(dest);
  console.log(`  ✅ ${label}: ${fileCount} files synced`);
}

function syncFile(src, dest, label) {
  if (!existsSync(src)) {
    console.warn(`  ⚠️  Source not found: ${src}`);
    return;
  }
  
  const destDir = dirname(dest);
  if (!existsSync(destDir)) {
    mkdirSync(destDir, { recursive: true });
  }
  
  cpSync(src, dest);
  console.log(`  ✅ ${label}: synced`);
}

function syncClass(courseName, className) {
  const courseDir = join(COURSES_DIR, courseName);
  const classDir = join(courseDir, className);
  
  if (!existsSync(classDir)) {
    console.error(`❌ Class directory not found: ${classDir}`);
    process.exit(1);
  }
  
  console.log(`\n📦 Syncing ${courseName}/${className}...`);
  
  // 1. Sync core/server/ → class/_sync/server/
  const syncServerDest = join(classDir, '_sync', 'server');
  syncDir(CORE_SERVER, syncServerDest, 'core/server');
  
  // 2. Sync course content/ → class/content/
  const courseContent = join(courseDir, 'content');
  const classContent = join(classDir, 'content');
  syncDir(courseContent, classContent, 'content');
  
  // 3. Sync course-config.json
  const courseConfig = join(courseDir, 'course-config.json');
  const classConfig = join(classDir, 'course-config.json');
  syncFile(courseConfig, classConfig, 'course-config.json');
  
  console.log(`✨ Done! ${courseName}/${className} is ready for deploy.\n`);
}

function discoverClasses() {
  const classes = [];
  
  if (!existsSync(COURSES_DIR)) {
    console.error('❌ No courses directory found');
    process.exit(1);
  }
  
  const courses = readdirSync(COURSES_DIR).filter(f => {
    return statSync(join(COURSES_DIR, f)).isDirectory();
  });
  
  for (const course of courses) {
    const courseDir = join(COURSES_DIR, course);
    const entries = readdirSync(courseDir).filter(f => {
      const fullPath = join(courseDir, f);
      return statSync(fullPath).isDirectory() && isClassDir(fullPath);
    });
    
    for (const cls of entries) {
      classes.push({ course, class: cls });
    }
  }
  
  return classes;
}

// ============ CLI ============
const args = process.argv.slice(2);

if (args.length === 0 || args[0] === '--help') {
  console.log(`
LMS Hub — Sync Deploy Script

Usage:
  node core/scripts/sync-deploy.js <course> <class>   Sync one class
  node core/scripts/sync-deploy.js --all              Sync all classes
  node core/scripts/sync-deploy.js --list             List discoverable classes

Examples:
  node core/scripts/sync-deploy.js social-commerce D01
  node core/scripts/sync-deploy.js gt-khtm L10
  node core/scripts/sync-deploy.js --all
  `);
  process.exit(0);
}

if (args[0] === '--list') {
  const classes = discoverClasses();
  console.log('\n📋 Discovered classes:\n');
  for (const c of classes) {
    console.log(`  • ${c.course}/${c.class}`);
  }
  console.log(`\n  Total: ${classes.length} classes\n`);
  process.exit(0);
}

if (args[0] === '--all') {
  const classes = discoverClasses();
  console.log(`\n🔄 Syncing all ${classes.length} classes...\n`);
  for (const c of classes) {
    syncClass(c.course, c.class);
  }
  console.log(`\n🎉 All ${classes.length} classes synced!\n`);
  process.exit(0);
}

if (args.length < 2) {
  console.error('❌ Usage: node core/scripts/sync-deploy.js <course> <class>');
  process.exit(1);
}

syncClass(args[0], args[1]);
