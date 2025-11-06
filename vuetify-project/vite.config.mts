// Plugins
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import Fonts from 'unplugin-fonts/vite'
import Layouts from 'vite-plugin-vue-layouts-next'
import Vue from '@vitejs/plugin-vue'
import VueRouter from 'unplugin-vue-router/vite'
import { VueRouterAutoImports } from 'unplugin-vue-router'
import Vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'

// Utilities
import { defineConfig, loadEnv } from 'vite'
import { fileURLToPath, URL } from 'node:url'

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => {
  // GitHub Pages: im CI automatisch /<repo>/; lokal '/'
  const env = loadEnv(mode, process.cwd(), '')
  const repo = (env.GITHUB_REPOSITORY || '').split('/')[1]
  const override = env.PUBLIC_BASE || env.VITE_PUBLIC_BASE || ''
  const base = override || (env.GITHUB_ACTIONS && repo ? `/${repo}/` : '/')

  return {
    base,
    plugins: [
      VueRouter({ dts: 'src/typed-router.d.ts' }),
      Layouts(),
      AutoImport({
        imports: ['vue', VueRouterAutoImports, { pinia: ['defineStore', 'storeToRefs'] }],
        dts: 'src/auto-imports.d.ts',
        eslintrc: { enabled: true },
        vueTemplate: true,
      }),
      Components({ dts: 'src/components.d.ts' }),
      Vue({ template: { transformAssetUrls } }),
      Vuetify({
        autoImport: true,
        styles: { configFile: 'src/styles/settings.scss' },
      }),
      Fonts({
        fontsource: {
          families: [
            { name: 'Roboto', weights: [100, 300, 400, 500, 700, 900], styles: ['normal', 'italic'] },
          ],
        },
      }),
    ],
    optimizeDeps: {
      exclude: [
        'vuetify',
        'vue-router',
        'unplugin-vue-router/runtime',
        'unplugin-vue-router/data-loaders',
        'unplugin-vue-router/data-loaders/basic',
      ],
    },
    define: { 'process.env': {} },
    resolve: {
      alias: { '@': fileURLToPath(new URL('./src', import.meta.url)) }, // './src' ist korrekt
      extensions: ['.js', '.json', '.jsx', '.mjs', '.ts', '.tsx', '.vue'],
    },
    server: { port: 3000 },
    build: { outDir: 'dist' },
  }
})
