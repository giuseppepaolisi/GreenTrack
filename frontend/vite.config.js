import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0', // Permette l'accesso dalla rete locale
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000', // Usa l'IP invece di localhost
        changeOrigin: true,             // Necessario per evitare problemi di host header
      }
    }
  }
})
