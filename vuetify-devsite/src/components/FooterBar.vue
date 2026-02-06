<template>
  <v-footer
    app
    class="custom-footer"
    :class="{ 'footer-scrolled': scrolled, 'footer-fixed': fixed }"
    height="80"
  >
    <!-- Main Footer Content -->
    <v-container class="footer-container">
      <!-- Scroll progress (subtle) -->
      <v-progress-linear
        :model-value="scrollProgress"
        height="2"
        rounded
        class="footer-progress"
      />

      <div class="footer-content">
        <!-- Left Section -->
        <div class="footer-left">
          <div class="copyright-section">
            <v-icon icon="mdi-heart" size="16" class="heart-icon" />
            <span class="copyright-text">
              © {{ currentYear }} ·
              <span class="name-gradient">Jehad Qassem</span>
            </span>

            <v-chip
              variant="outlined"
              size="x-small"
              class="version-chip"
              color="primary"
            >
              v{{ appVersion }}
            </v-chip>
          </div>

          <div class="footer-message">
            Built with
            <v-icon icon="mdi-vuejs" size="16" class="tech-icon" color="#41b883" />
            Vue 3 &
            <v-icon icon="mdi-vuetify" size="16" class="tech-icon" color="#1867C0" />
            Vuetify
          </div>
        </div>

        <!-- Right Section -->
        <div class="footer-right">
          <div class="social-links">
            <v-tooltip
              v-for="link in socialLinks"
              :key="link.name"
              location="top"
              transition="slide-y-transition"
            >
              <template #activator="{ props }">
                <v-btn
                  v-bind="props"
                  :icon="link.icon"
                  variant="text"
                  :href="link.url"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="social-btn"
                  :class="`social-${link.name.toLowerCase()}`"
                  size="small"
                  :aria-label="link.ariaLabel"
                >
                  <v-icon :icon="link.icon" size="20" />
                  <div class="social-glow" />
                </v-btn>
              </template>
              <span>{{ link.tooltip }}</span>
            </v-tooltip>

            <!-- Copy email -->
            <v-tooltip location="top" transition="slide-y-transition">
              <template #activator="{ props }">
                <v-btn
                  v-bind="props"
                  icon="mdi-content-copy"
                  variant="text"
                  class="social-btn social-copy"
                  size="small"
                  @click="copyEmail"
                  aria-label="E-Mail kopieren"
                >
                  <v-icon icon="mdi-content-copy" size="20" />
                  <div class="social-glow" />
                </v-btn>
              </template>
              <span>E-Mail kopieren</span>
            </v-tooltip>

            <!-- Theme toggle (light/dark/system) -->
            <v-tooltip location="top" transition="slide-y-transition">
              <template #activator="{ props }">
                <v-btn
                  v-bind="props"
                  :icon="themeIcon"
                  variant="text"
                  @click="cycleTheme"
                  class="theme-btn"
                  size="small"
                  aria-label="Theme wechseln"
                >
                  <v-icon :icon="themeIcon" size="20" />
                  <div class="theme-glow" />
                </v-btn>
              </template>
              <span>{{ themeTooltip }}</span>
            </v-tooltip>
          </div>
        </div>
      </div>

      <!-- Footer Wave -->
      <div class="footer-wave">
        <svg viewBox="0 0 1200 120" preserveAspectRatio="none">
          <path
            d="M0,0V46.29c47.79,22.2,103.59,32.17,158,28,70.36-5.37,136.33-33.31,206.8-37.5C438.64,32.43,512.34,53.67,583,72.05c69.27,18,138.3,24.88,209.4,13.08,36.15-6,69.85-17.84,104.45-29.34C989.49,25,1113-14.29,1200,52.47V0Z"
            opacity=".25"
            class="shape-fill"
          />
          <path
            d="M0,0V15.81C13,36.92,27.64,56.86,47.69,72.05,99.41,111.27,165,111,224.58,91.58c31.15-10.15,60.09-26.07,89.67-39.8,40.92-19,84.73-46,130.83-49.67,36.26-2.85,70.9,9.42,98.6,31.56,31.77,25.39,62.32,62,103.63,73,40.44,10.79,81.35-6.69,119.13-24.28s75.16-39,116.92-43.05c59.73-5.85,113.28,22.88,168.9,38.84,30.2,8.66,59,6.17,87.09-7.5,22.43-10.89,48-26.93,60.65-49.24V0Z"
            opacity=".5"
            class="shape-fill"
          />
          <path
            d="M0,0V5.63C149.93,59,314.09,71.32,475.83,42.57c43-7.64,84.23-20.12,127.61-26.46,59-8.63,112.48,12.24,165.56,35.4C827.93,77.22,886,95.24,951.2,90c86.53-7,172.46-45.71,248.8-84.81V0Z"
            class="shape-fill"
          />
        </svg>
      </div>
    </v-container>

    <!-- Scroll to Top Button -->
    <v-fade-transition>
      <v-btn
        v-if="scrolled"
        icon
        variant="flat"
        class="scroll-top-btn"
        @click="scrollToTop"
        color="primary"
        size="small"
        aria-label="Nach oben scrollen"
      >
        <v-icon icon="mdi-chevron-up" />
      </v-btn>
    </v-fade-transition>

    <!-- Snackbar -->
    <v-snackbar v-model="snackbar" timeout="1800" location="top" class="footer-snackbar">
      {{ snackbarText }}
    </v-snackbar>
  </v-footer>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { useTheme } from 'vuetify'

const theme = useTheme()
const currentYear = new Date().getFullYear()

const scrolled = ref(false)
const fixed = ref(false)
const scrollProgress = ref(0)

const snackbar = ref(false)
const snackbarText = ref('')

const username = import.meta.env.VITE_GITHUB_USERNAME || 'je2700'

// Optional: set via VITE_APP_VERSION in build/CI
const appVersion = import.meta.env.VITE_APP_VERSION ?? 'dev'

const emailAddress = 'qassemjehad@outlook.de'
const repoUrl = `https://github.com/${username}`
const linkedinUrl = 'https://www.linkedin.com/in/jehad-qassem-3455373ab/'

const socialLinks = [
  {
    name: 'GitHub',
    icon: 'mdi-github',
    url: repoUrl,
    tooltip: 'Code auf GitHub ansehen',
    ariaLabel: 'GitHub Profil öffnen'
  },
  {
    name: 'LinkedIn',
    icon: 'mdi-linkedin',
    url: linkedinUrl,
    tooltip: 'LinkedIn Profil ansehen',
    ariaLabel: 'LinkedIn Profil öffnen'
  },
  {
    name: 'Email',
    icon: 'mdi-email',
    url: `mailto:${emailAddress}`,
    tooltip: 'E-Mail senden',
    ariaLabel: 'E-Mail senden'
  }
]

// Theme: light / dark / system
type ThemeMode = 'light' | 'dark' | 'system'

const themeMode = ref<ThemeMode>(
  (localStorage.getItem('theme:mode') as ThemeMode) ?? 'system'
)

const mq = typeof window !== 'undefined' ? window.matchMedia?.('(prefers-color-scheme: dark)') : null
const systemPrefersDark = ref(!!mq?.matches)

function applyTheme() {
  const dark =
    themeMode.value === 'system' ? systemPrefersDark.value : themeMode.value === 'dark'
  theme.global.name.value = dark ? 'dark' : 'light'
}

function cycleTheme() {
  themeMode.value =
    themeMode.value === 'light' ? 'dark' : themeMode.value === 'dark' ? 'system' : 'light'
  localStorage.setItem('theme:mode', themeMode.value)
  applyTheme()
}

const themeIcon = computed(() => {
  if (themeMode.value === 'system') return 'mdi-theme-light-dark'
  return themeMode.value === 'dark' ? 'mdi-weather-sunny' : 'mdi-weather-night'
})

const themeTooltip = computed(() => {
  if (themeMode.value === 'system') return 'Theme: System (Klick: Hell)'
  return themeMode.value === 'dark' ? 'Theme: Dunkel (Klick: System)' : 'Theme: Hell (Klick: Dunkel)'
})

async function copyEmail() {
  try {
    await navigator.clipboard.writeText(emailAddress)
    snackbarText.value = 'E-Mail kopiert ✅'
  } catch {
    snackbarText.value = 'Kopieren nicht möglich ❌'
  } finally {
    snackbar.value = true
  }
}

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

function handleScroll() {
  const scrollY = window.scrollY
  const windowHeight = window.innerHeight
  const documentHeight = document.documentElement.scrollHeight

  scrolled.value = scrollY > 100

  const max = Math.max(1, documentHeight - windowHeight)
  scrollProgress.value = Math.min(100, Math.max(0, (scrollY / max) * 100))

  // Footer fixieren, wenn am Ende oder zu wenig Content
  const isAtBottom = scrollY + windowHeight >= documentHeight - 100
  const isShortPage = documentHeight <= windowHeight
  fixed.value = isAtBottom || isShortPage
}

function onSystemThemeChange(e: MediaQueryListEvent) {
  systemPrefersDark.value = e.matches
  applyTheme()
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  handleScroll()

  mq?.addEventListener?.('change', onSystemThemeChange)
  applyTheme()
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
  mq?.removeEventListener?.('change', onSystemThemeChange)
})
</script>

<style scoped lang="scss">
.custom-footer {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  position: relative;
  overflow: hidden;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);

  // Standard-Position (am Ende des Contents)
  position: relative;
  margin-top: auto;

  &.footer-scrolled {
    backdrop-filter: blur(10px);
    background: linear-gradient(
      135deg,
      rgba(102, 126, 234, 0.95) 0%,
      rgba(118, 75, 162, 0.95) 100%
    ) !important;
  }

  // Fixierte Position (immer sichtbar am unteren Bildschirmrand)
  &.footer-fixed {
    position: fixed !important;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.1);

    .footer-wave {
      display: none; // Wave ausblenden wenn fixiert
    }
  }
}

// Sicherstellen, dass der Hauptinhalt genug Platz für den fixierten Footer hat
:deep(.v-main) {
  min-height: calc(100vh - 80px);
  padding-bottom: 80px;
  box-sizing: border-box;
}

// Für Seiten mit wenig Inhalt
:deep(.page-content) {
  min-height: calc(100vh - 80px - 64px);
  display: flex;
  flex-direction: column;
}

.footer-container {
  position: relative;
  z-index: 2;
  max-width: 1200px;
  margin: 0 auto;
}

// Progress bar styling
.footer-progress {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  opacity: 0.7;
  z-index: 3;
}

.footer-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 16px;
  height: 100%;
  flex-wrap: wrap;
  gap: 20px;

  @media (max-width: 768px) {
    flex-direction: column;
    text-align: center;
    gap: 16px;
    padding: 16px;
  }
}

.footer-left {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.copyright-section {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.heart-icon {
  color: #f56565;
  animation: heartbeat 2s ease-in-out infinite;
}

.copyright-text {
  color: rgba(255, 255, 255, 0.9);
  font-weight: 500;
}

.name-gradient {
  background: linear-gradient(135deg, #fff 0%, #e2e8f0 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 600;
}

.version-chip {
  backdrop-filter: blur(10px);
  background: rgba(255, 255, 255, 0.15) !important;
  border-color: rgba(255, 255, 255, 0.3) !important;
  color: white !important;
  font-weight: 600;
}

.footer-message {
  display: flex;
  align-items: center;
  gap: 6px;
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.875rem;
  flex-wrap: wrap;
}

.tech-icon {
  margin: 0 2px;
}

.footer-right {
  display: flex;
  align-items: center;
}

.social-links {
  display: flex;
  align-items: center;
  gap: 4px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 50px;
  padding: 8px;
}

.social-btn {
  position: relative;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  color: white !important;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  overflow: hidden;

  &:hover {
    transform: translateY(-2px);
    background: rgba(255, 255, 255, 0.15) !important;

    .social-glow {
      opacity: 1;
      transform: scale(1);
    }
  }

  .v-icon {
    position: relative;
    z-index: 2;
  }
}

.social-glow {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(circle at center, rgba(255, 255, 255, 0.3) 0%, transparent 70%);
  border-radius: 50%;
  opacity: 0;
  transform: scale(0.8);
  transition: all 0.3s ease;
}

// Specific hover colors
.social-github:hover {
  background: linear-gradient(135deg, rgba(51, 51, 51, 0.3) 0%, rgba(110, 84, 148, 0.3) 100%) !important;
}
.social-source:hover {
  background: linear-gradient(135deg, rgba(20, 20, 20, 0.25) 0%, rgba(100, 100, 100, 0.25) 100%) !important;
}
.social-issues:hover {
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.25) 0%, rgba(239, 68, 68, 0.25) 100%) !important;
}
.social-linkedin:hover {
  background: linear-gradient(135deg, rgba(10, 102, 194, 0.28) 0%, rgba(0, 119, 181, 0.28) 100%) !important;
}
.social-email:hover {
  background: linear-gradient(135deg, rgba(219, 68, 55, 0.3) 0%, rgba(183, 28, 28, 0.3) 100%) !important;
}
.social-copy:hover {
  background: linear-gradient(135deg, rgba(34, 197, 94, 0.22) 0%, rgba(16, 185, 129, 0.22) 100%) !important;
}

.theme-btn {
  position: relative;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  color: white !important;
  transition: all 0.3s ease;
  overflow: hidden;

  &:hover {
    transform: translateY(-2px);
    background: rgba(255, 255, 255, 0.15) !important;

    .theme-glow {
      opacity: 1;
      transform: scale(1);
    }
  }

  .v-icon {
    position: relative;
    z-index: 2;
  }
}

.theme-glow {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(circle at center, rgba(255, 255, 255, 0.4) 0%, transparent 70%);
  border-radius: 50%;
  opacity: 0;
  transform: scale(0.8);
  transition: all 0.3s ease;
}

.footer-wave {
  position: absolute;
  bottom: 100%;
  left: 0;
  width: 100%;
  overflow: hidden;
  line-height: 0;
  transform: rotate(180deg);

  svg {
    position: relative;
    display: block;
    width: calc(100% + 1.3px);
    height: 60px;
  }

  .shape-fill {
    fill: rgba(102, 126, 234, 0.1);
  }
}

.scroll-top-btn {
  position: fixed !important;
  bottom: 100px;
  right: 24px;
  z-index: 1001;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
  color: white !important;
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
  transition: all 0.3s ease;

  &:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 30px rgba(102, 126, 234, 0.6);
  }
}

// Animations
@keyframes heartbeat {
  0%,
  100% { transform: scale(1); }
  25% { transform: scale(1.1); }
  50% { transform: scale(1); }
  75% { transform: scale(1.05); }
}

@keyframes float {
  0%,
  100% { transform: translateY(0px); }
  50% { transform: translateY(-5px); }
}

.social-btn {
  animation: float 3s ease-in-out infinite;
}

.social-btn:nth-child(2) { animation-delay: 0.2s; }
.social-btn:nth-child(3) { animation-delay: 0.4s; }
.social-btn:nth-child(4) { animation-delay: 0.6s; }
.social-btn:nth-child(5) { animation-delay: 0.8s; }
.theme-btn { animation-delay: 1s; }

// Responsive
@media (max-width: 768px) {
  .footer-content {
    flex-direction: column;
    text-align: center;
  }

  .copyright-section {
    justify-content: center;
  }

  .footer-message {
    justify-content: center;
  }

  .social-links {
    align-self: center;
  }

  .scroll-top-btn {
    bottom: 90px;
    right: 16px;
  }

  :deep(.v-main) {
    padding-bottom: 80px;
  }
}

@media (max-width: 480px) {
  .social-links {
    gap: 2px;
    padding: 6px;
  }

  .social-btn,
  .theme-btn {
    width: 36px;
    height: 36px;

    .v-icon {
      font-size: 18px;
    }
  }

  .copyright-text {
    font-size: 0.875rem;
  }

  .footer-message {
    font-size: 0.8rem;
  }
}

// Dark theme adjustments
:deep(.v-theme--dark) {
  .custom-footer {
    background: linear-gradient(135deg, #2d3748 0%, #1a202c 100%) !important;

    &.footer-scrolled {
      background: linear-gradient(
        135deg,
        rgba(45, 55, 72, 0.95) 0%,
        rgba(26, 32, 44, 0.95) 100%
      ) !important;
    }
  }

  .footer-wave .shape-fill {
    fill: rgba(45, 55, 72, 0.1);
  }
}

// Reduced motion
@media (prefers-reduced-motion: reduce) {
  .social-btn,
  .theme-btn {
    animation: none;
  }

  .scroll-top-btn:hover {
    transform: none;
  }

  .heart-icon {
    animation: none;
  }
}
</style>
