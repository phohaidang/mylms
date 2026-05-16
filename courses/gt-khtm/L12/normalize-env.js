import { readFileSync, writeFileSync } from 'fs';

const path = '.env';
let content = readFileSync(path, 'utf-8');

// Find the GOOGLE_PRIVATE_KEY line
// It might span multiple lines if it has real newlines inside quotes
const lines = content.split('\n');
let startIndex = -1;
let endIndex = -1;

for (let i = 0; i < lines.length; i++) {
  if (lines[i].startsWith('GOOGLE_PRIVATE_KEY=')) {
    startIndex = i;
    // Check if it ends on this line or later
    let currentLine = lines[i];
    if (currentLine.match(/"[^"]*"$/)) {
      endIndex = i;
      break;
    }
    // Search for the closing quote
    for (let j = i; j < lines.length; j++) {
      if (lines[j].includes('"') && j > i) {
         if (lines[j].trim().endsWith('"')) {
            endIndex = j;
            break;
         }
      }
    }
    break;
  }
}

if (startIndex !== -1 && endIndex !== -1) {
  console.log(`Found key from line ${startIndex + 1} to ${endIndex + 1}`);
  let keyLines = lines.slice(startIndex, endIndex + 1);
  let rawKeyString = keyLines.join('\n');
  
  // Extract the value inside quotes
  let value = rawKeyString.split('=')[1].trim();
  if (value.startsWith('"')) value = value.substring(1);
  if (value.endsWith('"')) value = value.substring(0, value.length - 1);
  
  // Clean it: remove real newlines and then replace literal \n with real ones, 
  // but wait, let's just make it a clean one-line escaped string for .env
  let cleaned = value.replace(/[\r\n]/g, '').replace(/\\n/g, '\n');
  let reEscaped = cleaned.replace(/\n/g, '\\n');
  
  let newKeyLine = `GOOGLE_PRIVATE_KEY="${reEscaped}"`;
  
  lines.splice(startIndex, (endIndex - startIndex) + 1, newKeyLine);
  writeFileSync(path, lines.join('\n'));
  console.log('Successfully normalized .env key');
} else {
  console.log('Could not find key or closing quote');
}
