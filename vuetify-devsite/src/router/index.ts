// src/router/index.ts
import { createRouter, createWebHashHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'  // ⬅️ Typ-Import

const routes: RouteRecordRaw[] = [
  { path: '/', name: 'home', component: () => import('../pages/Home.vue'), meta: { title: 'Home' } },
  { path: '/projects', name: 'projects', component: () => import('../pages/Projects.vue'), meta: { title: 'Projekte' } },
  { path: '/playground', name: 'playground', component: () => import('../pages/Playground.vue'), meta: { title: 'API-Playground' } },
  { path: '/resume', name: 'resume', component: () => import('../pages/Resume.vue'), meta: { title: 'Lebenslauf' } },
  { path: '/contact', name: 'contact', component: () => import('../pages/Contact.vue'), meta: { title: 'Kontakt' } },
  { path: '/:pathMatch(.*)*', redirect: '/' },
]

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes,
  scrollBehavior() { return { top: 0 } },
})

router.afterEach((to) => {
  const base = 'Portfolio'
  const title = to.meta?.title ? String(to.meta.title) : base
  document.title = title === base ? base : `${title} · ${base}`
})

export default router
