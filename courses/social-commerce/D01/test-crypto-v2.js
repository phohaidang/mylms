import 'dotenv/config';
import crypto from 'crypto';

try {
  let key = process.env.GOOGLE_PRIVATE_KEY || '';
  
  // Try cleaning map
  const cleaned = key
    .replace(/\\n/g, '\n')
    .split('\n')
    .map(l => l.trim())
    .join('\n')
    .trim();
  
  console.log('Testing key with trim map cleaning...');
  const k = crypto.createPrivateKey(cleaned);
  console.log('✅ Success!');
} catch (err) {
  console.error('❌ Failed!');
  console.error(err.message);
}
