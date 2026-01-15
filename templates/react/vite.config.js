import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],

  server: {
    port: 5173,
    host: '127.0.0.1'
  },
  optimizeDeps: {
    include: [
      '@bufbuild/protobuf',
      '@connectrpc/connect',
      '@connectrpc/connect-web',
      'js-cookie',
      'uuid',
      'zod'
    ]
  },
  resolve: {
    alias: {
      '@': '/src'
    }
  }
})
