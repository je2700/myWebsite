<template>
  <v-card 
    class="project-card"
    :href="cardHref" 
    target="_blank" 
    elevation="4"
    rounded="xl"
    hover
  >
    <!-- Hintergrund-Leuchteffekt -->
    <div class="card-glow" :class="glowColor"></div>
    
    <!-- Hauptinhalt -->
    <v-card-item class="card-header">
      <!-- Projekt-Icon & Titel -->
      <div class="project-header">
        <div class="project-icon">
          <v-icon :icon="projectIcon" size="32" />
        </div>
        <div class="project-title-section">
          <div class="text-h5 font-weight-bold project-name">{{ item.name }}</div>
          <div class="text-caption text-medium-emphasis project-updated">
            Aktualisiert {{ formatDate }}
          </div>
        </div>
      </div>

      <!-- Sprach-Badge -->
      <v-chip 
        v-if="item.language"
        :color="languageColor"
        variant="flat"
        size="small"
        class="language-chip"
      >
        <div class="language-dot" :style="{ backgroundColor: languageColor }"></div>
        {{ item.language }}
      </v-chip>
    </v-card-item>

    <!-- Beschreibung -->
    <v-card-text class="card-content">
      <div class="description-text">
        {{ descriptionText }}
      </div>
      
      <!-- Tech-Stack Vorschau -->
      <div v-if="techStack.length > 0" class="tech-stack">
        <v-chip
          v-for="tech in techStack"
          :key="tech"
          variant="outlined"
          size="x-small"
          class="tech-chip"
        >
          {{ tech }}
        </v-chip>
      </div>
    </v-card-text>

    <!-- Statistiken & Aktionen -->
    <v-card-actions class="card-actions">
      <!-- Statistiken -->
      <div class="project-stats">
        <div class="stat-item">
          <v-icon icon="mdi-star-outline" size="18" class="stat-icon" />
          <span class="stat-value">{{ formattedStarCount }}</span>
        </div>
        <div class="stat-item">
          <v-icon icon="mdi-source-branch" size="18" class="stat-icon" />
          <span class="stat-value">{{ forksCount }}</span>
        </div>
        <div v-if="item.language" class="stat-item">
          <div class="language-dot-small" :style="{ backgroundColor: languageColor }"></div>
          <span class="stat-value">{{ item.language }}</span>
        </div>
      </div>

      <!-- Aktionsbuttons -->
      <div class="action-buttons">
        <v-btn
          variant="outlined"
          :href="item.html_url"
          target="_blank"
          @click.stop
          size="small"
          class="action-btn code-btn"
          rounded="lg"
        >
          <template v-slot:prepend>
            <v-icon icon="mdi-github" size="18" />
          </template>
          Code
        </v-btn>
        
        <v-btn
          v-if="item.homepage && item.homepage.trim() !== ''"
          variant="flat"
          :href="item.homepage!"
          target="_blank"
          @click.stop
          size="small"
          class="action-btn live-btn"
          rounded="lg"
          :color="primaryColor"
        >
          <template v-slot:prepend>
            <v-icon icon="mdi-rocket-launch-outline" size="18" />
          </template>
          Live-Demo
        </v-btn>
      </div>
    </v-card-actions>

    <!-- Hover-Overlay -->
    <div class="card-overlay">
      <v-icon icon="mdi-arrow-top-right" size="24" class="overlay-icon" />
    </div>
  </v-card>
</template>

<script setup lang="ts">
import { computed } from 'vue'

export interface RepoItem {
  id: number
  name: string
  description?: string | null
  language?: string | null
  stargazers_count?: number
  forks_count?: number
  html_url: string
  homepage?: string | null
  updated_at?: string
  topics?: string[]
}

const props = defineProps<{ item: RepoItem }>()

// Computed properties
const descriptionText = computed(() => 
  props.item.description?.trim() || 'No description provided'
)

const formattedStarCount = computed(() => {
  const count = props.item.stargazers_count ?? 0
  return count > 1000 ? `${(count / 1000).toFixed(1)}k` : count.toString()
})

const forksCount = computed(() => props.item.forks_count ?? 0)

const cardHref = computed(() =>
  props.item.homepage && props.item.homepage.trim() !== ''
    ? props.item.homepage
    : props.item.html_url
)

const formatDate = computed(() => {
  if (!props.item.updated_at) return 'recently'
  
  const date = new Date(props.item.updated_at)
  const now = new Date()
  const diffTime = Math.abs(now.getTime() - date.getTime())
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))
  
  if (diffDays === 1) return 'today'
  if (diffDays < 7) return `${diffDays} days ago`
  if (diffDays < 30) return `${Math.ceil(diffDays / 7)} weeks ago`
  return `${Math.ceil(diffDays / 30)} months ago`
})

// Language-based styling
const languageColor = computed(() => {
  const colors: Record<string, string> = {
    'JavaScript': '#f7df1e',
    'TypeScript': '#3178c6',
    'Vue': '#41b883',
    'React': '#61dafb',
    'Angular': '#dd0031',
    'Apache Cordova': '#4cc2e4',
    'HTML': '#e34f26',
    'CSS': '#1572b6',
    'SCSS': '#c69'
  }
  return colors[props.item.language || ''] || '#6b7280'
})

const glowColor = computed(() => {
  const language = props.item.language || 'default'
  return `glow-${language.toLowerCase().replace(/[^a-z]/g, '')}`
})

const projectIcon = computed(() => {
  const icons: Record<string, string> = {
    'JavaScript': 'mdi-language-javascript',
    'TypeScript': 'mdi-language-typescript',
    'Vue': 'mdi-vuejs',
    'React': 'mdi-react',
    'Angular': 'mdi-angular',
    'Apache Cordova': 'mdi-cordova',
    'HTML': 'mdi-language-html5',
    'CSS': 'mdi-language-css3'
  }
  return icons[props.item.language || ''] || 'mdi-folder-code-outline'
})

const primaryColor = computed(() => {
  const colors: Record<string, string> = {
    'JavaScript': 'warning',
    'TypeScript': 'primary',
    'Vue': 'success',
    'React': 'info',
    'Angular': 'error',
    'Apache Cordova': 'info',
    'default': 'primary'
  }
  return colors[props.item.language || ''] || 'primary'
})

const techStack = computed(() => {
  return props.item.topics?.slice(0, 3) || []
})
</script>

<style scoped lang="scss">
.project-card {
  position: relative;
  background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
  border: 1px solid #e2e8f0;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  overflow: hidden;
  cursor: pointer;
  height: 100%;
  display: flex;
  flex-direction: column;

  &:hover {
    transform: translateY(-8px);
    border-color: #cbd5e0;
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);

    .card-glow {
      opacity: 0.6;
      transform: scale(1.1);
    }

    .card-overlay {
      opacity: 1;
      transform: translateY(0);
    }

    .project-name {
      color: #667eea;
    }
  }
}

.card-glow {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  opacity: 0.1;
  transition: all 0.4s ease;
  border-radius: 0 0 50% 50%;
  transform: scale(1);
  transform-origin: top center;

  // Language-specific glow colors
  &.glow-javascript { background: linear-gradient(135deg, #f7df1e, #f0db4f); }
  &.glow-typescript { background: linear-gradient(135deg, #3178c6, #235a97); }
  &.glow-vue { background: linear-gradient(135deg, #41b883, #34495e); }
  &.glow-python { background: linear-gradient(135deg, #3776ab, #ffd343); }
  &.glow-java { background: linear-gradient(135deg, #ed8b00, #5382a1); }
}

.card-header {
  position: relative;
  z-index: 2;
  padding: 24px 24px 16px;
}

.project-header {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  margin-bottom: 16px;
}

.project-icon {
  flex-shrink: 0;
  width: 56px;
  height: 56px;
  border-radius: 16px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.project-title-section {
  flex: 1;
  min-width: 0;
}

.project-name {
  color: #1a202c;
  transition: color 0.3s ease;
  line-height: 1.3;
  word-break: break-word;
}

.project-updated {
  margin-top: 4px;
}

.language-chip {
  backdrop-filter: blur(10px);
  background: rgba(255, 255, 255, 0.9) !important;
  border: 1px solid rgba(255, 255, 255, 0.3);
  font-weight: 600;
}

.language-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  margin-right: 6px;
}

.card-content {
  position: relative;
  z-index: 2;
  padding: 0 24px 16px;
  flex: 1;
}

.description-text {
  color: #4a5568;
  line-height: 1.6;
  margin-bottom: 16px;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.tech-stack {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.tech-chip {
  background: rgba(255, 255, 255, 0.7) !important;
  backdrop-filter: blur(10px);
  border: 1px solid #e2e8f0;
  font-size: 0.7rem;
  height: 24px;
}

.card-actions {
  position: relative;
  z-index: 2;
  padding: 16px 24px 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.project-stats {
  display: flex;
  align-items: center;
  gap: 16px;
}

.stat-item {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #718096;
  font-size: 0.875rem;
  font-weight: 500;
}

.stat-icon {
  color: #a0aec0;
}

.stat-value {
  font-size: 0.875rem;
  font-weight: 600;
}

.language-dot-small {
  width: 6px;
  height: 6px;
  border-radius: 50%;
}

.action-buttons {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.action-btn {
  flex: 1;
  min-width: 100px;
  font-weight: 600;
  text-transform: none;
  transition: all 0.3s ease;

  &:hover {
    transform: translateY(-1px);
  }
}

.code-btn {
  border-color: #e2e8f0;
  color: #4a5568;
}

.live-btn {
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
  
  &:hover {
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
  }
}

.card-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.9) 0%, rgba(118, 75, 162, 0.9) 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transform: translateY(10px);
  transition: all 0.3s ease;
  border-radius: inherit;
}

.overlay-icon {
  color: white;
  transform: scale(1.2);
}

// Responsive design
@media (max-width: 960px) {
  .project-header {
    gap: 12px;
  }
  
  .project-icon {
    width: 48px;
    height: 48px;
    
    .v-icon {
      font-size: 24px;
    }
  }
  
  .project-name {
    font-size: 1.25rem;
  }
}

@media (max-width: 600px) {
  .card-header,
  .card-content,
  .card-actions {
    padding: 20px;
  }
  
  .project-stats {
    gap: 12px;
  }
  
  .action-buttons {
    flex-direction: column;
  }
  
  .action-btn {
    min-width: auto;
  }
}

// Animation for card entrance
@keyframes cardEntrance {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.project-card {
  animation: cardEntrance 0.6s ease-out;
}
</style>