import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  root: '.',
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
      },
    },
  },
  server: {
    proxy: {
      '/api': 'http://localhost:3013',
      '/lessons': 'http://localhost:3013',
      '/slides': 'http://localhost:3013',
      '/images': 'http://localhost:3013'
    }
  }
});
