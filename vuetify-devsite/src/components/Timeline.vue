<template>
  <div class="timeline-container">
    <!-- Header -->
    <div class="timeline-header">
      <v-icon icon="mdi-timeline-clock-outline" size="48" class="header-icon" />
      <div class="header-text">
        <h2 class="text-h3 font-weight-bold">Berufliche Laufbahn</h2>
        <p class="text-subtitle-1 text-white">
          Ein Überblick über meine berufliche Entwicklung in den letzten Jahren
        </p>
      </div>
    </div>

    <!-- Timeline -->
    <v-timeline
      density="comfortable"
      side="end"
      align="start"
      class="custom-timeline"
      truncate-line="both"
    >
      <v-timeline-item
        v-for="(e, i) in entries"
        :key="i"
        :dot-color="e.color"
        :icon="e.icon"
        size="small"
        class="timeline-item"
      >
        <!-- Gegenseite - Zeitraum -->
        <template #opposite>
          <v-card class="period-card" :class="`period-${i}`" elevation="4" rounded="lg">
            <v-card-text class="period-content">
              <div class="text-body-1 font-weight-bold">{{ e.period }}</div>
              <v-icon
                :icon="getPeriodIcon(e.period)"
                size="16"
                class="period-icon"
                :color="e.color"
              />
            </v-card-text>
            <div class="period-glow" :style="{ backgroundColor: getColorValue(e.color) }" />
          </v-card>
        </template>

        <!-- Hauptinhalt -->
        <v-card
          class="experience-card"
          :class="`experience-${i}`"
          elevation="8"
          rounded="xl"
          hover
        >
          <!-- Kartenkopf -->
          <div class="card-header" :style="{ background: getGradient(e.color) }">
            <div class="header-background">
              <div class="bg-dot dot-1"></div>
              <div class="bg-dot dot-2"></div>
              <div class="bg-dot dot-3"></div>
            </div>
            <div class="title-section">
              <v-icon :icon="e.icon" size="28" class="title-icon" />
              <div class="title-content">
                <div class="text-h5 font-weight-bold">{{ e.title }}</div>
                <div class="text-subtitle-1 company-name">{{ e.company }}</div>
              </div>
            </div>
            <div class="duration-badge">
              <v-chip :color="e.color" variant="flat" size="small" class="duration-chip">
                {{ getDuration(e.period) }}
              </v-chip>
            </div>
          </div>

          <!-- Karteninhalt -->
          <v-card-text class="card-content">
            <div class="description-text">
              {{ e.description }}
            </div>

            <!-- Schlagworte -->
            <div class="tags-section">
              <v-chip
                v-for="t in e.tags"
                :key="t"
                :color="e.color"
                variant="outlined"
                size="small"
                class="tech-tag"
              >
                <v-icon :icon="getTagIcon(t)" size="16" class="mr-1" />
                {{ t }}
              </v-chip>
            </div>

            <!-- Fortschrittsanzeige -->
            <div class="progress-section">
              <div class="progress-label">
                <span class="text-caption text-medium-emphasis">Erfahrungsstufe</span>
                <span
                  class="text-caption font-weight-bold"
                  :style="{ color: getColorValue(e.color) }"
                >
                  {{ getExperienceLevel(i) }}
                </span>
              </div>
              <v-progress-linear
                :model-value="getProgressValue(i)"
                :color="e.color"
                height="6"
                rounded
                class="progress-bar"
              />
            </div>
          </v-card-text>

          <!-- Karten-Leuchteffekt -->
          <div class="card-glow" :style="{ background: getGradient(e.color) }" />
        </v-card>
      </v-timeline-item>
    </v-timeline>

    <!-- Visualisierung des Karrierewegs -->
    <div class="career-path">
      <div class="path-line">
        <div
          v-for="(entry, i) in entries"
          :key="i"
          class="path-marker"
          :style="{
            backgroundColor: getColorValue(entry.color),
            animationDelay: `${(i + 1) * 0.2}s`
          }"
        ></div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
type TimelineColor = 'primary' | 'secondary' | 'success' | 'warning' | 'error' | 'info'

export interface Entry {
  period: string
  title: string
  company: string
  description: string
  tags: string[]
  color: TimelineColor
  icon: string
}

const entries: Entry[] = [
  {
    period: '2024–heute',
    title: 'Full-Stack Web-Developer',
    company: 'Freiberuflich',
    description:
      'Entwicklung moderner, responsiver Webanwendungen mit Vue.js 3, Vuetify und TypeScript. Aufbau skalierbarer Backend-Systeme mit Node.js, Express und PostgreSQL. Implementierung von REST-APIs mit JWT-Authentifizierung und Fokus auf Clean Code sowie Best Practices.',
    tags: ['Vue 3', 'TypeScript', 'Node.js', 'PostgreSQL', 'Express', 'Vuetify'],
    color: 'success',
    icon: 'mdi-laptop-account',
  },
  {
    period: '2023–2024',
    title: 'Mobile & Web App Developer',
    company: 'Freiberuflich',
    description:
      'Entwicklung hybrider mobiler Anwendungen mit Apache Cordova für iOS und Android. Erstellung von Progressive Web Apps (PWA) mit modernen Web-Technologien. Integration von REST-APIs, Implementierung von Offline-Funktionalität und Push-Benachrichtigungen.',
    tags: ['Apache Cordova', 'PWA', 'JavaScript', 'HTML5', 'CSS3', 'REST API'],
    color: 'info',
    icon: 'mdi-cellphone-link',
  },
  {
    period: '2023–2024',
    title: 'Frontend Developer',
    company: 'Freiberuflich',
    description:
      'Entwicklung interaktiver Single Page Applications mit React und Angular. Implementierung responsiver Benutzeroberflächen, State Management mit Redux und Angular Services. Arbeit mit modernen Build-Tools und Component-Libraries.',
    tags: ['React', 'Angular', 'TypeScript', 'Redux', 'Responsive Design'],
    color: 'warning',
    icon: 'mdi-react',
  },
  {
    period: '2022–2023',
    title: 'Web-App Developer Ausbildung',
    company: 'SGD Darmstadt',
    description:
      'Intensives Fernstudium zum Web-App Developer mit Schwerpunkt auf moderne JavaScript-Frameworks. Erlernen von Full-Stack-Entwicklung, Datenbank-Design, RESTful APIs und agilen Entwicklungsmethoden. Abschluss mit Zertifizierung in allen relevanten Web-Technologien.',
    tags: ['JavaScript', 'Node.js', 'jQuery', 'Datenbanken', 'Webdesign'],
    color: 'primary',
    icon: 'mdi-school',
  },
]

const COLOR_MAP: Record<TimelineColor, string> = {
  primary: '#667eea',
  secondary: '#764ba2',
  success: '#41b883',
  warning: '#f6ad55',
  error: '#f56565',
  info: '#4299e1',
}

const GRADIENT_MAP: Record<TimelineColor, string> = {
  primary: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
  secondary: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
  success: 'linear-gradient(135deg, #41b883 0%, #34495e 100%)',
  warning: 'linear-gradient(135deg, #f6ad55 0%, #ed8936 100%)',
  error: 'linear-gradient(135deg, #f56565 0%, #e53e3e 100%)',
  info: 'linear-gradient(135deg, #4299e1 0%, #3182ce 100%)',
}

function getColorValue(color: TimelineColor): string {
  return COLOR_MAP[color]
}

function getGradient(color: TimelineColor): string {
  return GRADIENT_MAP[color]
}

function getPeriodIcon(period: string): string {
  if (period.includes('heute')) return 'mdi-clock-fast'
  if (period.includes('–')) return 'mdi-calendar-range'
  return 'mdi-calendar'
}

function getTagIcon(tag: string): string {
  const key = tag.replace(/\u2011/g, '-') // geschützter Bindestrich → normaler Bindestrich

  const icons = {
    'Vue 3': 'mdi-vuejs',
    Vue: 'mdi-vuejs',
    TypeScript: 'mdi-language-typescript',
    'Node.js': 'mdi-nodejs',
    Express: 'mdi-nodejs',
    PostgreSQL: 'mdi-database',
    Vuetify: 'mdi-palette',
    'Apache Cordova': 'mdi-cordova',
    PWA: 'mdi-cellphone-link',
    JavaScript: 'mdi-language-javascript',
    HTML5: 'mdi-language-html5',
    CSS3: 'mdi-language-css3',
    'REST API': 'mdi-api',
    React: 'mdi-react',
    Angular: 'mdi-angular',
    Redux: 'mdi-redux',
    'Responsive Design': 'mdi-responsive',
    jQuery: 'mdi-jquery',
    Datenbanken: 'mdi-database',
    Webdesign: 'mdi-web',
    JWT: 'mdi-security',
    'CI/CD': 'mdi-source-branch',
  } as const

  if (key in icons) {
    return icons[key as keyof typeof icons]
  }

  return 'mdi-code-tags'
}

function getDuration(period: string): string {
  if (period.includes('heute')) return 'Aktuell'

  const parts = period.split('–').map((p) => p.trim())
  if (parts.length !== 2) return period

  const startPart = parts[0]
  const endPart = parts[1]

  // Hier wird für TypeScript sichergestellt: keine undefined-Werte
  if (!startPart || !endPart) return period

  const startYear = Number(startPart.replace(/[^0-9]/g, ''))
  const endYear = Number(endPart.replace(/[^0-9]/g, ''))

  if (Number.isNaN(startYear) || Number.isNaN(endYear) || endYear < startYear) {
    return period
  }

  const diff = endYear - startYear || 1 // gleiches Jahr → 1 Jahr
  return `${diff} ${diff === 1 ? 'Jahr' : 'Jahre'}`
}


const EXPERIENCE_LEVELS = ['Experte', 'Fortgeschritten', 'Fortgeschritten', 'Grundlagen'] as const
const PROGRESS_VALUES = [95, 85, 80, 70] as const

function getExperienceLevel(index: number): string {
  return EXPERIENCE_LEVELS[index] ?? 'Erfahren'
}

function getProgressValue(index: number): number {
  return PROGRESS_VALUES[index] ?? 50
}
</script>

<style scoped lang="scss">
.timeline-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 24px;
  position: relative;
}

.timeline-header {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 60px;
  text-align: center;
  justify-content: center;

  @media (max-width: 600px) {
    flex-direction: column;
    gap: 16px;
  }
}

.header-icon {
  color: #667eea;
}

.header-text {
  .text-h3 {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 8px;
  }
}

.custom-timeline {
  position: relative;
  z-index: 2;

  :deep(.v-timeline-divider) {
    .v-timeline-divider__dot {
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
      border: 3px solid white;
    }
  }
}

.timeline-item {
  margin-bottom: 48px;
}

.period-card {
  position: relative;
  background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%) !important;
  border: 2px solid #e2e8f0;
  min-width: 140px;
  transition: all 0.3s ease;
  overflow: hidden;

  &:hover {
    transform: translateX(-4px);
    border-color: #667eea;
  }
}

.period-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 16px !important;
  position: relative;
  z-index: 2;
}

.period-glow {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  opacity: 0.8;
}

.experience-card {
  position: relative;
  background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%) !important;
  border: 2px solid #e2e8f0;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  overflow: hidden;
  margin-left: 24px;

  &:hover {
    transform: translateY(-8px) translateX(4px);
    border-color: #cbd5e0;
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);

    .card-glow {
      opacity: 0.6;
    }
  }
}

.card-header {
  position: relative;
  padding: 24px;
  color: white;
  overflow: hidden;
}

.header-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  opacity: 0.1;
}

.bg-dot {
  position: absolute;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.3);
  animation: float 6s ease-in-out infinite;

  &.dot-1 {
    width: 60px;
    height: 60px;
    top: -30px;
    left: -30px;
    animation-delay: 0s;
  }

  &.dot-2 {
    width: 40px;
    height: 40px;
    bottom: -20px;
    right: 10%;
    animation-delay: 2s;
  }

  &.dot-3 {
    width: 30px;
    height: 30px;
    top: 50%;
    right: -15px;
    animation-delay: 4s;
  }
}

.title-section {
  display: flex;
  align-items: center;
  gap: 16px;
  position: relative;
  z-index: 2;
}

.title-icon {
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.2));
}

.title-content {
  flex: 1;
}

.company-name {
  opacity: 0.9;
  font-weight: 500;
}

.duration-badge {
  position: relative;
  z-index: 2;
}

.duration-chip {
  backdrop-filter: blur(10px);
  background: rgba(255, 255, 255, 0.2) !important;
  font-weight: 600;
}

.card-content {
  padding: 24px;
}

.description-text {
  color: #4a5568;
  line-height: 1.6;
  margin-bottom: 20px;
  font-size: 1rem;
}

.tags-section {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 20px;
}

.tech-tag {
  backdrop-filter: blur(10px);
  background: rgba(255, 255, 255, 0.7) !important;
  border: 1px solid #e2e8f0;
  font-weight: 500;
  transition: all 0.3s ease;

  &:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }
}

.progress-section {
  margin-top: 16px;
}

.progress-label {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.progress-bar {
  border-radius: 8px;

  :deep(.v-progress-linear__determinate) {
    border-radius: 8px;
  }
}

.card-glow {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 120px;
  opacity: 0.3;
  transition: opacity 0.3s ease;
  border-radius: 0 0 50% 50%;
  transform: scale(1.2);
  transform-origin: top center;
}

.career-path {
  position: absolute;
  top: 200px;
  left: 50%;
  transform: translateX(-50%);
  height: calc(100% - 300px);
  width: 4px;
  background: linear-gradient(to bottom, #667eea, #764ba2);
  border-radius: 2px;
  z-index: 1;
  opacity: 0.1;
}

.path-line {
  position: relative;
  height: 100%;
}

.path-marker {
  position: absolute;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  left: 50%;
  transform: translateX(-50%);
  animation: bounce 2s ease-in-out infinite;
  box-shadow: 0 0 20px currentColor;

  &:nth-child(1) {
    top: 20%;
  }
  &:nth-child(2) {
    top: 50%;
  }
  &:nth-child(3) {
    top: 80%;
  }
}

@keyframes float {
  0%,
  100% {
    transform: translateY(0px) rotate(0deg);
  }
  33% {
    transform: translateY(-10px) rotate(120deg);
  }
  66% {
    transform: translateY(5px) rotate(240deg);
  }
}

@keyframes bounce {
  0%,
  100% {
    transform: translateX(-50%) scale(1);
  }
  50% {
    transform: translateX(-50%) scale(1.2);
  }
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.timeline-item {
  animation: slideIn 0.6s ease-out;
}

.timeline-item:nth-child(1) {
  animation-delay: 0.1s;
}
.timeline-item:nth-child(2) {
  animation-delay: 0.2s;
}
.timeline-item:nth-child(3) {
  animation-delay: 0.3s;
}

@media (max-width: 960px) {
  .custom-timeline {
    :deep(.v-timeline-item__body) {
      max-width: none;
    }
  }

  .experience-card {
    margin-left: 0;
    margin-top: 16px;
  }

  .period-card {
    min-width: 120px;
  }
}

@media (max-width: 600px) {
  .timeline-container {
    padding: 24px 16px;
  }

  .card-header {
    padding: 20px;
  }

  .title-section {
    flex-direction: column;
    gap: 12px;
    text-align: center;
  }

  .duration-badge {
    align-self: center;
  }

  .card-content {
    padding: 20px;
  }

  .tags-section {
    justify-content: center;
  }

  .career-path {
    display: none;
  }
}

@media (prefers-color-scheme: dark) {
  .experience-card,
  .period-card {
    background: linear-gradient(135deg, #2d3748 0%, #1a202c 100%) !important;
    border-color: #4a5568;
  }

  .description-text {
    color: #cbd5e0;
  }

  .tech-tag {
    background: rgba(45, 55, 72, 0.7) !important;
    border-color: #4a5568;
    color: #e2e8f0;
  }
}
</style>
