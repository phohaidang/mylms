import { defineConfig } from 'vite';
import { resolve, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));

export default defineConfig({
  root: '.',
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    rollupOptions: {
      input: { main: resolve(__dirname, 'index.html') }
    }
  },
  server: {
    proxy: {
      '/api/': 'http://localhost:3020',
      '/lessons': 'http://localhost:3020',
      '/slides': 'http://localhost:3020',
      '/images': 'http://localhost:3020'
    }
  }
});
