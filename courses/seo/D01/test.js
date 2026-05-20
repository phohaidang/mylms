
import 'dotenv/config';
import db from './_sync/server/services/sheets.js';

async function run() {
  const students = await db.getAll('students');
  console.log('Total students:', students.length);
  const student = students.find(s => s.student_id == '30239230015' || s.student_id == '030239230015' || (s.email && s.email.includes('30239230015')));
  console.log('Found student:', student);
  console.log('First 2 students:', students.slice(0, 2));
}

run().catch(console.error);

