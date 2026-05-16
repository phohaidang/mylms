import 'dotenv/config';

const key = process.env.GOOGLE_PRIVATE_KEY || '';
const buf = Buffer.from(key.substring(0, 50));
console.log('Hex dump of first 50 chars:', buf.toString('hex'));

const cleaned = key.replace(/\\n/g, '\n');
const buf2 = Buffer.from(cleaned.substring(0, 50));
console.log('Hex dump of cleaned first 50 chars:', buf2.toString('hex'));
