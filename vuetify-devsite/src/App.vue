<template>
  <v-app class="portfolio-app">
    <!-- Hintergrund-Elemente für die gesamte App -->
    <div class="app-background">
      <div class="bg-gradient"></div>
      <div class="floating-particles">
        <div class="particle particle-1"></div>
        <div class="particle particle-2"></div>
        <div class="particle particle-3"></div>
        <div class="particle particle-4"></div>
        <div class="particle particle-5"></div>
      </div>
      <div class="grid-overlay"></div>
    </div>

    <!-- Haupt-App-Struktur -->
    <DefaultLayout>
      <router-view v-slot="{ Component, route }">
        <!-- Routen-Übergänge -->
        <transition
          :name="typeof route.meta.transition === 'string' ? route.meta.transition : 'fade'"
          mode="out-in"
          @enter="onPageEnter"
          @leave="onPageLeave"
        >
          <component :is="Component" :key="route.path" />
        </transition>
      </router-view>
    </DefaultLayout>

    <!-- Globaler Lade-Indikator -->
    <v-fade-transition>
      <div v-if="loading" class="global-loading">
        <v-progress-circular
          indeterminate
          size="108"
          width="4"
          color="primary"
          class="loading-spinner"
        >
          <v-img
              src="/favicon.png?v=2"
            alt="Logo"
            class="loader-logo"
            width="72"
            height="72"
            contain
          />
        </v-progress-circular>
        <div class="loading-text">Lade beeindruckende Inhalte...</div>
      </div>
    </v-fade-transition>

    <!-- Globaler Snackbar für Benachrichtigungen -->
    <v-snackbar
      v-model="snackbar.visible"
      :color="snackbar.color"
      :timeout="snackbar.timeout"
      location="top"
      elevation="24"
      rounded="pill"
      class="global-snackbar"
    >
      <div class="snackbar-content">
        <v-icon :icon="snackbar.icon" class="mr-3" size="20" />
        <span class="snackbar-text">{{ snackbar.message }}</span>
      </div>
      <template v-slot:actions>
        <v-btn
          icon
          variant="text"
          @click="snackbar.visible = false"
          size="small"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </template>
    </v-snackbar>
  </v-app>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import DefaultLayout from './layouts/DefaultLayout.vue'

const router = useRouter()
const loading = ref(false)
const snackbar = reactive({
  visible: false,
  message: '',
  color: 'primary',
  icon: 'mdi-information',
  timeout: 5000
})

// Seitenübergangs-Handler
function onPageEnter() {
  loading.value = false
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

function onPageLeave() {
  loading.value = true
}

// Globale Benachrichtigungsfunktion
function showNotification(message: string, type: 'success' | 'error' | 'warning' | 'info' = 'info') {
  const config = {
    success: { color: 'success', icon: 'mdi-check-circle' },
    error: { color: 'error', icon: 'mdi-alert-circle' },
    warning: { color: 'warning', icon: 'mdi-alert' },
    info: { color: 'primary', icon: 'mdi-information' }
  }[type]

  Object.assign(snackbar, {
    ...config,
    message,
    visible: true
  })
}

// Behandle globale Fehler
function handleGlobalError(event: ErrorEvent) {
  console.error('Globaler Fehler:', event.error)
  showNotification('Ein unerwarteter Fehler ist aufgetreten', 'error')
}

// Behandle nicht behandelte Promise-Abweisungen
function handleUnhandledRejection(event: PromiseRejectionEvent) {
  console.error('Nicht behandelte Promise-Abweisung:', event.reason)
  showNotification('Etwas ist schiefgelaufen', 'error')
}

// Exponiere globale Funktionen für Debugging
onMounted(() => {
  // Füge globale Fehler-Handler hinzu
  window.addEventListener('error', handleGlobalError)
  window.addEventListener('unhandledrejection', handleUnhandledRejection)

  // Exponiere Utility-Funktionen für die Entwicklung
  if (import.meta.env.DEV) {
    ;(window as any).$app = {
      showNotification,
      reload: () => window.location.reload()
    }
  }

  // Initialisiere die App
  console.log('🎉 Portfolio-App erfolgreich initialisiert!')
})

onUnmounted(() => {
  // Räume Event-Listener auf
  window.removeEventListener('error', handleGlobalError)
  window.removeEventListener('unhandledrejection', handleUnhandledRejection)
})

// Stelle globale Funktionen für Komponenten bereit
defineExpose({
  showNotification
})
</script>

<style scoped lang="scss">
.portfolio-app {
  position: relative;
  min-height: 100vh;
  background: transparent;
  overflow-x: hidden;
}

.app-background {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  z-index: -1;
}

.bg-gradient {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, 
    rgba(102, 126, 234, 0.03) 0%, 
    rgba(118, 75, 162, 0.02) 25%, 
    rgba(79, 209, 197, 0.01) 50%, 
    rgba(237, 137, 54, 0.005) 75%, 
    transparent 100%);
}

.floating-particles {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.particle {
  position: absolute;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea, #764ba2);
  opacity: 0.1;
  animation: float-particle 15s ease-in-out infinite;

  &.particle-1 {
    width: 120px;
    height: 120px;
    top: 10%;
    left: 5%;
    animation-delay: 0s;
  }

  &.particle-2 {
    width: 80px;
    height: 80px;
    top: 60%;
    left: 10%;
    animation-delay: 3s;
  }

  &.particle-3 {
    width: 160px;
    height: 160px;
    top: 20%;
    right: 8%;
    animation-delay: 6s;
  }

  &.particle-4 {
    width: 60px;
    height: 60px;
    bottom: 15%;
    right: 15%;
    animation-delay: 9s;
  }

  &.particle-5 {
    width: 100px;
    height: 100px;
    bottom: 25%;
    left: 20%;
    animation-delay: 12s;
  }
}

.grid-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: 
    linear-gradient(rgba(255, 255, 255, 0.015) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.015) 1px, transparent 1px);
  background-size: 60px 60px;
  opacity: 0.3;
}

// Seiten-Übergänge
.fade-enter-active,
.fade-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.fade-enter-from {
  opacity: 0;
  transform: translateY(20px);
}

.fade-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

.slide-enter-active,
.slide-leave-active {
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.slide-enter-from {
  opacity: 0;
  transform: translateX(30px);
}

.slide-leave-to {
  opacity: 0;
  transform: translateX(-30px);
}

.scale-enter-active,
.scale-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.scale-enter-from {
  opacity: 0;
  transform: scale(0.95);
}

.scale-leave-to {
  opacity: 0;
  transform: scale(1.05);
}

// Globaler Lade-Indikator
.global-loading {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(15, 23, 42, 0.8);
  backdrop-filter: blur(10px);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}

.loading-spinner {
  margin-bottom: 20px;
  filter: drop-shadow(0 4px 12px rgba(0, 0, 0, 0.3));
}

.loader-logo {
  width: 72px;
  height: 72px;
  padding: 0;
  background: transparent;
  border: none;
  border-radius: 0;
}

.loading-text {
  color: rgba(255, 255, 255, 0.8);
  font-size: 1.125rem;
  font-weight: 500;
  text-align: center;
}

// Globaler Snackbar
.global-snackbar {
  :deep(.v-snackbar__content) {
    padding: 16px 20px;
  }
}

.snackbar-content {
  display: flex;
  align-items: center;
}

.snackbar-text {
  font-weight: 500;
  font-size: 0.875rem;
}

// Animationen
@keyframes float-particle {
  0%, 100% {
    transform: translateY(0px) rotate(0deg);
  }
  25% {
    transform: translateY(-20px) rotate(90deg);
  }
  50% {
    transform: translateY(10px) rotate(180deg);
  }
  75% {
    transform: translateY(-10px) rotate(270deg);
  }
}

@keyframes pulse-glow {
  0%, 100% {
    opacity: 0.1;
  }
  50% {
    opacity: 0.2;
  }
}

// Responsive Anpassungen
@media (max-width: 960px) {
  .particle {
    &.particle-1,
    &.particle-3 {
      width: 80px;
      height: 80px;
    }

    &.particle-2,
    &.particle-4,
    &.particle-5 {
      width: 40px;
      height: 40px;
    }
  }

  .loading-text {
    font-size: 1rem;
  }
}

@media (max-width: 600px) {
  .global-snackbar {
    margin: 8px;
    
    :deep(.v-snackbar__content) {
      padding: 12px 16px;
    }
  }

  .snackbar-content {
    font-size: 0.8rem;
  }
}

// Reduced Motion Support
@media (prefers-reduced-motion: reduce) {
  .floating-particles,
  .fade-enter-active,
  .fade-leave-active,
  .slide-enter-active,
  .slide-leave-active,
  .scale-enter-active,
  .scale-leave-active {
    animation: none;
    transition: none;
  }

  .particle {
    animation: none;
  }
}

// Druck-Stile
@media print {
  .app-background,
  .global-loading,
  .global-snackbar {
    display: none !important;
  }

  .portfolio-app {
    background: white !important;
  }
}

// High Contrast Mode Support
@media (prefers-contrast: high) {
  .bg-gradient {
    opacity: 0.05;
  }

  .particle {
    opacity: 0.15;
  }
}

// Dunkles Design Anpassungen
:deep(.v-theme--light) {
  .app-background {
    .bg-gradient {
      background: linear-gradient(135deg, 
        rgba(102, 126, 234, 0.02) 0%, 
        rgba(118, 75, 162, 0.015) 25%, 
        rgba(79, 209, 197, 0.01) 50%, 
        rgba(237, 137, 54, 0.005) 75%, 
        transparent 100%);
    }

    .grid-overlay {
      background-image: 
        linear-gradient(rgba(0, 0, 0, 0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 0, 0, 0.03) 1px, transparent 1px);
    }
  }

  .global-loading {
    background: rgba(248, 250, 252, 0.9);
    
    .loading-text {
      color: rgba(0, 0, 0, 0.8);
    }
  }
}

:deep(.v-theme--dark) {
  .app-background {
    .bg-gradient {
      background: linear-gradient(135deg, 
        rgba(102, 126, 234, 0.05) 0%, 
        rgba(118, 75, 162, 0.04) 25%, 
        rgba(79, 209, 197, 0.03) 50%, 
        rgba(237, 137, 54, 0.02) 75%, 
        transparent 100%);
    }

    .grid-overlay {
      background-image: 
        linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
      opacity: 0.4;
    }

    .particle {
      background: linear-gradient(135deg, #4f6beb, #8a4dbf);
      opacity: 0.08;
    }
  }

  .global-loading {
    background: rgba(3, 7, 18, 0.9);
    
    .loading-text {
      color: rgba(255, 255, 255, 0.9);
    }
  }
}

// Performance-Optimierungen
@media (prefers-reduced-transparency: reduce) {
  .app-background {
    .bg-gradient {
      opacity: 0.01;
    }
    
    .grid-overlay {
      opacity: 0.1;
    }
  }
}
</style>

<style>
/* Globale App-Stile */
:root {
  --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --success-gradient: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
  --warning-gradient: linear-gradient(135deg, #ed8936 0%, #dd6b20 100%);
  --error-gradient: linear-gradient(135deg, #f56565 0%, #e53e3e 100%);
}

/* Sanftes Scrollen für die gesamte App */
html {
  scroll-behavior: smooth;
}

/* Benutzerdefinierte Scrollbar für Webkit-Browser */
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 4px;
}

::-webkit-scrollbar-thumb {
  background: linear-gradient(135deg, #667eea, #764ba2);
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(135deg, #5a6fd8, #6a4190);
}

/* Auswahl-Stile */
::selection {
  background: rgba(102, 126, 234, 0.3);
  color: inherit;
}

::-moz-selection {
  background: rgba(102, 126, 234, 0.3);
  color: inherit;
}

/* Fokus-Stile für Barrierefreiheit */
*:focus-visible {
  outline: 2px solid #667eea;
  outline-offset: 2px;
}

/* Verbessere Text-Darstellung */
body {
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Druck-Stile */
@media print {
  * {
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  
  .no-print {
    display: none !important;
  }
}

/* Utility-Klassen für globale Verwendung */
.gradient-text {
  background: var(--primary-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.glass-effect {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.shadow-glow {
  box-shadow: 0 8px 32px rgba(102, 126, 234, 0.15);
}

/* Animation Utilities */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in-up {
  animation: fadeInUp 0.6s ease-out;
}

/* Responsive Text-Skalierung */
.text-responsive {
  font-size: clamp(1rem, 2.5vw, 1.5rem);
}

/* Lade-Skeleton-Animation */
@keyframes skeleton-loading {
  0% {
    background-position: -200px 0;
  }
  100% {
    background-position: calc(200px + 100%) 0;
  }
}

.skeleton {
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200px 100%;
  animation: skeleton-loading 1.5s infinite;
}

/* Dunkles Design Anpassungen für Skeleton */
.v-theme--dark .skeleton {
  background: linear-gradient(90deg, #2d3748 25%, #4a5568 50%, #2d3748 75%);
  background-size: 200px 100%;
}

/* Verbesserte Scrollbar für dunkles Design */
.v-theme--dark ::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.1);
}

.v-theme--dark ::-webkit-scrollbar-thumb {
  background: linear-gradient(135deg, #4f6beb, #8a4dbf);
}

.v-theme--dark ::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(135deg, #3d56d4, #7a3ca9);
}

/* Angepasste Auswahl-Farben für dunkles Design */
.v-theme--dark ::selection {
  background: rgba(79, 107, 235, 0.4);
}

.v-theme--dark ::-moz-selection {
  background: rgba(79, 107, 235, 0.4);
}

/* Verbesserte Glas-Effekte für beide Designs */
.v-theme--light .glass-effect {
  background: rgba(255, 255, 255, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.v-theme--dark .glass-effect {
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

/* Angepasste Schatten für beide Designs */
.v-theme--light .shadow-glow {
  box-shadow: 0 8px 32px rgba(102, 126, 234, 0.15);
}

.v-theme--dark .shadow-glow {
  box-shadow: 0 8px 32px rgba(79, 107, 235, 0.2);
}
</style>