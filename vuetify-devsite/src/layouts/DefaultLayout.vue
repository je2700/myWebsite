<template>
  <v-app class="app-layout">
    <!-- Navigationsleiste -->
    <v-navigation-drawer 
      v-model="drawer" 
      app 
      temporary
      class="nav-drawer"
      elevation="8"
    >
      <!-- Drawer Kopfbereich -->
      <div class="drawer-header">
        <v-avatar size="48" class="drawer-avatar">
          <v-img src="/api/placeholder/48/48" alt="Profil" />
        </v-avatar>
        <div class="drawer-info">
          <div class="drawer-name">Jehad Qassem</div>
          <div class="drawer-title">Full-Stack-Entwickler</div>
        </div>
      </div>

      <v-divider class="mx-4 my-2" />

      <!-- Navigationslinks -->
      <v-list nav density="comfortable" class="nav-list">
        <v-list-item
          v-for="item in items"
          :key="item.to"
          :to="item.to"
          @click="drawer = false"
          class="nav-item"
          :class="{ 'nav-item-active': $route.path === item.to }"
        >
          <template v-slot:prepend>
            <v-icon :icon="item.icon" class="nav-icon" />
          </template>

          <v-list-item-title class="nav-text">{{ item.title }}</v-list-item-title>

          <!-- Aktiver Indikator -->
          <div class="nav-indicator" v-if="$route.path === item.to" />
        </v-list-item>
      </v-list>

      <!-- Drawer Fußbereich -->
      <div class="drawer-footer">
        <v-divider class="mb-4" />
        <div class="theme-toggle-container">
          <ThemeToggle />
        </div>
      </div>

      <!-- Drawer Hintergrund -->
      <div class="drawer-background">
        <div class="drawer-dot dot-1"></div>
        <div class="drawer-dot dot-2"></div>
      </div>
    </v-navigation-drawer>

    <!-- App-Leiste -->
    <v-app-bar 
      app 
      flat 
      density="comfortable"
      class="app-bar"
      :elevation="scrolled ? 4 : 0"
    >
      <!-- Mobile Menü-Button -->
      <v-app-bar-nav-icon 
        class="d-md-none menu-button"
        @click="drawer = !drawer"
        variant="text"
      >
        <v-icon>mdi-menu</v-icon>
      </v-app-bar-nav-icon>

      <!-- Logo/Marke -->
      <router-link to="/" class="brand-link">
        <div class="brand-container">
          <v-icon icon="mdi-code-braces" size="28" class="brand-icon" color="primary" />
          <v-toolbar-title class="brand-title">
            <span class="brand-text">{{ title }}</span>
          </v-toolbar-title>
        </div>
      </router-link>

      <v-spacer />

      <!-- Desktop-Navigation -->
      <div class="desktop-nav">
        <v-btn
          v-for="item in items"
          :key="item.to"
          :to="item.to"
          variant="text"
          class="nav-button"
          :class="{ 'nav-button-active': $route.path === item.to }"
          rounded="lg"
        >
          <template v-slot:prepend>
            <v-icon :icon="item.icon" size="20" class="nav-button-icon" />
          </template>
          {{ item.title }}
        </v-btn>
      </div>

      <v-spacer />

      <!-- Aktionen rechts -->
      <div class="app-bar-actions">

        <!-- GitHub-Link -->
        <v-btn
          icon
          variant="text"
          href="https://github.com/je2700"
          target="_blank"
          class="github-button"
          size="small"
        >
          <v-icon>mdi-github</v-icon>
        </v-btn>
      </div>
    </v-app-bar>

    <!-- Hauptinhalt -->
    <v-main class="app-main">
      <div class="page-content">
        <slot />
      </div>
    </v-main>

    <!-- Fußzeile -->
    <FooterBar />
  </v-app>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { useRoute } from 'vue-router'
import FooterBar from '../components/FooterBar.vue'

const title = 'Jehad Qassem'
const drawer = ref(false)
const scrolled = ref(false)
const route = useRoute()

const items = [
  { title: 'Home', to: '/', icon: 'mdi-home' },
  { title: 'Projekte', to: '/projects', icon: 'mdi-view-grid-outline' },
  { title: 'API-Spielwiese', to: '/playground', icon: 'mdi-console' },
  { title: 'Lebenslauf', to: '/resume', icon: 'mdi-timeline' },
  { title: 'Kontakt', to: '/contact', icon: 'mdi-email' },
]

function handleScroll() {
  scrolled.value = window.scrollY > 20
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped lang="scss">
.app-layout {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
}

.nav-drawer {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
  backdrop-filter: blur(20px);
  position: relative;
  overflow: hidden;
}

.drawer-header {
  padding: 24px 20px 16px;
  display: flex;
  align-items: center;
  gap: 12px;
  position: relative;
  z-index: 2;
}

.drawer-avatar {
  border: 2px solid rgba(255, 255, 255, 0.1);
  background: rgba(255, 255, 255, 0.05);
}

.drawer-info {
  flex: 1;
}

.drawer-name {
  font-weight: 600;
  color: white;
  font-size: 1.125rem;
  line-height: 1.2;
}

.drawer-title {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.875rem;
  margin-top: 2px;
}

.nav-list {
  padding: 8px 12px;
  position: relative;
  z-index: 2;
}

.nav-item {
  border-radius: 12px;
  margin-bottom: 4px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;

  &:hover {
    background: rgba(255, 255, 255, 0.05) !important;
    transform: translateX(4px);
  }

  &.nav-item-active {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.15) 0%, rgba(118, 75, 162, 0.1) 100%) !important;
    border: 1px solid rgba(102, 126, 234, 0.2);

    .nav-icon {
      color: #667eea;
    }

    .nav-text {
      color: white;
      font-weight: 600;
    }
  }
}

.nav-icon {
  color: rgba(255, 255, 255, 0.7);
  transition: color 0.3s ease;
}

.nav-text {
  color: rgba(255, 255, 255, 0.8);
  font-weight: 500;
  transition: all 0.3s ease;
}

.nav-indicator {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  width: 4px;
  height: 20px;
  background: linear-gradient(135deg, #667eea, #764ba2);
  border-radius: 2px;
}

.drawer-footer {
  padding: 16px 20px;
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 2;
}

.theme-toggle-container {
  display: flex;
  justify-content: center;
}

.drawer-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
}

.drawer-dot {
  position: absolute;
  border-radius: 50%;
  background: rgba(102, 126, 234, 0.1);
  animation: float 6s ease-in-out infinite;

  &.dot-1 {
    width: 80px;
    height: 80px;
    bottom: 10%;
    right: -40px;
    animation-delay: 0s;
  }

  &.dot-2 {
    width: 40px;
    height: 40px;
    top: 20%;
    left: -20px;
    animation-delay: 3s;
  }
}

.app-bar {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%) !important;
  backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
  transition: all 0.3s ease;

  &.v-app-bar--is-scrolled {
    background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.95) 100%) !important;
    backdrop-filter: blur(20px);
  }
}

.menu-button {
  color: rgba(255, 255, 255, 0.8) !important;

  &:hover {
    color: white !important;
    background: rgba(255, 255, 255, 0.05) !important;
  }
}

.brand-link {
  text-decoration: none;
  display: flex;
  align-items: center;
}

.brand-container {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 0;
}

.brand-icon {
  filter: drop-shadow(0 2px 4px rgba(102, 126, 234, 0.3));
}

.brand-title {
  color: white;
  font-size: 1.5rem;
  font-weight: 700;
}

.brand-text {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.desktop-nav {
  display: flex;
  gap: 4px;
  align-items: center;

  @media (max-width: 1279px) {
    display: none;
  }
}

.nav-button {
  color: rgba(252, 248, 248, 0.7) !important;
  font-weight: 500;
  text-transform: none;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;

  &:hover {
    color: white !important;
    background: rgba(255, 255, 255, 0.05) !important;
    transform: translateY(-1px);
  }

  &.nav-button-active {
    color: white !important;
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.15) 0%, rgba(118, 75, 162, 0.1) 100%) !important;
    border: 1px solid rgba(102, 126, 234, 0.2);

    .nav-button-icon {
      color: #667eea;
    }

    &::before {
      content: '';
      position: absolute;
      bottom: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 20px;
      height: 2px;
      background: linear-gradient(135deg, #667eea, #764ba2);
      border-radius: 1px;
    }
  }
}

.nav-button-icon {
  transition: color 0.3s ease;
}

.app-bar-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.theme-toggle-desktop {
  @media (max-width: 959px) {
    display: none;
  }
}

.github-button {
  color: rgba(255, 255, 255, 0.7) !important;

  &:hover {
    color: white !important;
    background: rgba(255, 255, 255, 0.05) !important;
    transform: scale(1.1);
  }
}

.app-main {
  background: transparent;
  min-height: 100vh;
}

.page-content {
  min-height: calc(100vh - 64px - 80px); // Subtract header and footer height
}

// Animations
@keyframes float {
  0%, 100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-10px);
  }
}

// Responsive design
@media (max-width: 1279px) {
  .desktop-nav {
    display: none;
  }
}

@media (max-width: 959px) {
  .brand-title {
    font-size: 1.25rem;
  }

  .brand-container {
    gap: 8px;
  }

  .brand-icon {
    font-size: 24px;
  }
}

@media (max-width: 599px) {
  .brand-title {
    font-size: 1.125rem;
  }

  .brand-text {
    display: none;
  }

  .app-bar-actions {
    gap: 4px;
  }
}

// Reduced motion support
@media (prefers-reduced-motion: reduce) {
  .nav-item,
  .nav-button,
  .drawer-dot {
    animation: none;
    transition: none;
  }

  .nav-item:hover,
  .nav-button:hover {
    transform: none;
  }
}

// Dark theme adjustments
:deep(.v-theme--light) {
  .app-layout {
    background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
  }

  .nav-drawer {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(255, 255, 255, 0.8) 100%) !important;
    border-right: 1px solid rgba(0, 0, 0, 0.1) !important;
  }

  .drawer-name {
    color: #1a202c;
  }

  .drawer-title {
    color: rgba(0, 0, 0, 0.7);
  }

  .nav-item {
    &:hover {
      background: rgba(0, 0, 0, 0.05) !important;
    }

    &.nav-item-active {
      background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.05) 100%) !important;
      border: 1px solid rgba(102, 126, 234, 0.2);
    }
  }

  .nav-icon {
    color: rgba(0, 0, 0, 0.7);
  }

  .nav-text {
    color: rgba(0, 0, 0, 0.8);
  }

  .app-bar {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(255, 255, 255, 0.8) 100%) !important;
    border-bottom: 1px solid rgba(0, 0, 0, 0.1) !important;

    &.v-app-bar--is-scrolled {
      background: linear-gradient(135deg, rgba(248, 250, 252, 0.95) 0%, rgba(226, 232, 240, 0.95) 100%) !important;
    }
  }

  .menu-button {
    color: rgba(0, 0, 0, 0.8) !important;

    &:hover {
      color: #1a202c !important;
      background: rgba(0, 0, 0, 0.05) !important;
    }
  }

  .brand-title {
    color: #1a202c;
  }

  .nav-button {
  color: rgba(252, 248, 248, 0.7) !important;
  font-weight: 500;
  text-transform: none;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;

  &:hover {
    color: rgba(252, 248, 248, 0.7) !important;
    background: rgba(255, 255, 255, 0.05) !important;
    transform: translateY(-1px);
  }

  &.nav-button-active {
    color: rgba(252, 248, 248, 0.7) !important;
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.15) 0%, rgba(118, 75, 162, 0.1) 100%) !important;
    border: 1px solid rgba(102, 126, 234, 0.2);

    .nav-button-icon {
      color: #667eea;
    }

    &::before {
      content: '';
      position: absolute;
      bottom: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 20px;
      height: 2px;
      background: linear-gradient(135deg, #667eea, #764ba2);
      border-radius: 1px;
    }
  }
}

  .github-button {
  color: rgba(252, 248, 248, 0.7) !important;

  &:hover {
    color: rgba(252, 248, 248, 0.7) !important;
    background: rgba(255, 255, 255, 0.05) !important;
    transform: scale(1.1);
  }
}
}
</style>