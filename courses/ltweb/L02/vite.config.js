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
      '/api/': 'http://localhost:3011',
      '/lessons': 'http://localhost:3011',
      '/slides': 'http://localhost:3011',
      '/images': 'http://localhost:3011'
    }
  }
});
