import 'dotenv/config';
import crypto from 'crypto';

try {
  let key = process.env.GOOGLE_PRIVATE_KEY || '';
  key = key.replace(/\\n/g, '\n');
  
  console.log('Testing key with explicit format/type...');
  const k = crypto.createPrivateKey({
    key: key,
    format: 'pem',
    type: 'pkcs8'
  });
  console.log('✅ Success!');
} catch (err) {
  console.error('❌ Failed!');
  console.error(err.message);
}
