import 'dotenv/config';

let key = process.env.GOOGLE_PRIVATE_KEY || '';
console.log('Original Key Length:', key.length);
console.log('Starts with quote?', key.startsWith('"'));
console.log('Ends with quote?', key.endsWith('"'));

let fixed = key;
if (fixed.startsWith('"') && fixed.endsWith('"')) {
  fixed = fixed.substring(1, fixed.length - 1);
}
fixed = fixed.replace(/\\n/g, '\n');

console.log('Fixed Key Length:', fixed.length);
console.log('First 50 chars:', fixed.substring(0, 50));
console.log('Last 50 chars:', fixed.substring(fixed.length - 50));
console.log('Number of newlines:', (fixed.match(/\n/g) || []).length);
