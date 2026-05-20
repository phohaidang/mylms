
import 'dotenv/config';
import db from './_sync/server/services/sheets.js';

async function run() {
  const students = await db.getAll('students');
  const student1 = students.find(s => s.student_id == '30239230177' || s.student_id == '030239230177');
  console.log('Found student 030239230177:', student1);
}

run().catch(console.error);

