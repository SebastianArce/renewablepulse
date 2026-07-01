import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// Proxy /api to the backend in dev/preview; in production Traefik routes it.
// Target is env-driven: 127.0.0.1 for host dev, http://backend:8000 inside compose.
const target = process.env.VITE_API_PROXY ?? 'http://127.0.0.1:8000'
const proxy = { '/api': target }

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: { '@': fileURLToPath(new URL('./src', import.meta.url)) },
  },
  server: { proxy },
  preview: { proxy },
})
