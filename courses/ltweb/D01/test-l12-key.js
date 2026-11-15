import { readFileSync } from 'fs';
import crypto from 'crypto';

try {
  const content = readFileSync('d:/PARA/Projects/second-brain/05-Projects/lms-gtkhmt/L12/.env', 'utf-8');
  const match = content.match(/GOOGLE_PRIVATE_KEY="(.+?)"/);
  if (match) {
    let key = match[1].replace(/\\n/g, '\n');
    console.log('Testing L12 key with crypto...');
    crypto.createPrivateKey(key);
    console.log('✅ Success! L12 key is valid.');
  } else {
    console.log('Could not find key in L12/.env');
  }
} catch (err) {
  console.error('❌ Failed!');
  console.error(err.message);
}
