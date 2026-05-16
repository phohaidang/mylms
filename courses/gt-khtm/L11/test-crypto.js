import 'dotenv/config';
import crypto from 'crypto';

try {
  let key = process.env.GOOGLE_PRIVATE_KEY || '';
  key = key.replace(/\\n/g, '\n');
  
  console.log('Testing key with crypto.createPrivateKey...');
  const k = crypto.createPrivateKey(key);
  console.log('✅ Success! Key is valid.');
} catch (err) {
  console.error('❌ Failed!');
  console.error('Error Code:', err.code);
  console.error('Error Message:', err.message);
  console.error('Full Error:', err);
}
