<template>
  <div class="tech-stack-container">
    <!-- Kopfbereich -->
    <div class="tech-header">
      <v-icon icon="mdi-cog-outline" size="32" class="header-icon" />
      <div class="header-text">
        <h2 class="text-h4 font-weight-bold">Technologie-Stack</h2>
        <p class="text-subtitle-1 text-white">
          Technologien, mit denen ich arbeite und die ich liebe
        </p>
      </div>
    </div>

    <!-- Tech Chips -->
    <div class="tech-chips-grid">
      <v-card
        v-for="t in tech"
        :key="t"
        class="tech-card"
        :class="`tech-${t.toLowerCase().replace(/[^a-z]/g, '')}`"
        variant="outlined"
        rounded="xl"
        hover
        @click="onTechClick(t)"
      >
        <v-card-text class="tech-card-content">
          <!-- Icon -->
          <div class="tech-icon-wrapper">
            <v-icon :icon="icons[t] ?? 'mdi-code-tags'" size="28" class="tech-icon" />
            <div class="tech-glow" />
          </div>

          <!-- Name -->
          <div class="tech-name">{{ t }}</div>

          <!-- Hover-Pfeil -->
          <v-icon icon="mdi-arrow-right" size="20" class="tech-arrow" />
        </v-card-text>

        <!-- Hintergrundmuster -->
        <div class="tech-pattern">
          <div class="pattern-dot dot-1"></div>
          <div class="pattern-dot dot-2"></div>
          <div class="pattern-dot dot-3"></div>
        </div>
      </v-card>
    </div>

    <!-- Ausgewählte Technologie-Info -->
    <v-expand-transition>
      <v-card 
        v-if="selectedTech" 
        class="selected-tech-card"
        elevation="8"
        rounded="xl"
      >
        <v-card-text class="selected-tech-content">
          <div class="selected-tech-header">
            <div class="selected-tech-icon">
              <v-icon :icon="icons[selectedTech] ?? 'mdi-code-tags'" size="32" />
            </div>
            <div class="selected-tech-info">
              <h3 class="text-h5 font-weight-bold">{{ selectedTech }}</h3>
              <p class="text-body-1 text-medium-emphasis">
                {{ techDescriptions[selectedTech] || 'Eine Technologie, mit der ich gerne arbeite' }}
              </p>
            </div>
            <v-btn
              icon
              variant="text"
              @click="selectedTech = null"
              class="close-btn"
            >
              <v-icon icon="mdi-close" />
            </v-btn>
          </div>
          
          <v-divider class="my-4" />
          
          <div class="tech-details">
            <div class="detail-item">
              <v-icon icon="mdi-star-outline" class="mr-2" color="primary" />
              <span>Erfahren</span>
            </div>
            <div class="detail-item">
              <v-icon icon="mdi-clock-outline" class="mr-2" color="primary" />
              <span>{{ experienceLevel[selectedTech] || '2+ Jahre' }}</span>
            </div>
            <div class="detail-item">
              <v-icon icon="mdi-heart-outline" class="mr-2" color="primary" />
              <span>{{ techLove[selectedTech] || 'Arbeite sehr gerne damit' }}</span>
            </div>
          </div>
        </v-card-text>
      </v-card>
    </v-expand-transition>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const tech = ['Node.js', 'Express.js', 'Vue.js', 'React.js', 'Angular', 'Cordova', 'TypeScript', 'PostgreSQL']

const icons: Record<string, string> = {
  'Node.js': 'mdi-nodejs',
  'Express.js': 'mdi-cloud-outline',
  'Vue.js': 'mdi-vuejs',
  'React.js': 'mdi-react',
  'Angular': 'mdi-angular',
  'Cordova': 'mdi-cellphone-cog',
  'TypeScript': 'mdi-language-typescript',
  'PostgreSQL': 'mdi-database'
}

const techDescriptions: Record<string, string> = {
   "Node.js": "JavaScript-Laufzeitumgebung, die auf der V8-Engine von Chrome basiert und skalierbare serverseitige Anwendungen ermöglicht",
  "Express.js": "Minimales und flexibles Node.js-Webanwendungs-Framework zum Erstellen von APIs und Web-Apps",
  "Vue.js": "Progressives JavaScript-Framework zum Erstellen von Benutzeroberflächen und Single-Page-Anwendungen",
  "React.js": "Bibliothek zum Erstellen von Benutzeroberflächen mit wiederverwendbaren Komponenten und virtuellem DOM",
  "Angular": "TypeScript-basiertes Framework von Google zur Entwicklung strukturierter Single-Page-Webanwendungen mit Komponenten, Modulen und Services.",
  "Cordova": "Framework zum Erstellen von mobilen Apps mit HTML, CSS und JavaScript",
  "TypeScript": "Typisierte Obermenge von JavaScript, die in reines JavaScript kompiliert wird",
  "PostgreSQL": "Relationale Datenbank für moderne Anwendungen"
}

const experienceLevel: Record<string, string> = {
  "Node.js": "1+ Jahre",
  "Express.js": "1+ Jahre",
  "Vue.js": "1+ Jahre",
  "React.js": "1+ Jahre",
  "Angular": "1+ Jahre",
  "TypeScript": "1+ Jahre",
  "PostgreSQL": "1+ Jahre",
  "Cordova": "1+ Jahre"
}

const techLove: Record<string, string> = {
 'Node.js': 'Liebe das Ökosystem',
 'Vue.js': 'Lieblings-Framework',
 'TypeScript': 'Kann ohne Typen nicht leben',
 'PostgreSQL': 'Flexibel und skalierbar',
 'Cordova': 'Mobile Apps mit Webtechnologien'
}

const selectedTech = ref<string | null>(null)

function onTechClick(tech: string) {
  selectedTech.value = selectedTech.value === tech ? null : tech
}
</script>

<style scoped lang="scss">
.tech-stack-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 24px;
}

.tech-header {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 48px;
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
  .text-h4 {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 8px;
  }
}

.tech-chips-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
  margin-bottom: 32px;

  @media (max-width: 600px) {
    grid-template-columns: 1fr;
  }
}

.tech-card {
  position: relative;
  background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%) !important;
  border: 2px solid #e2e8f0;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
  overflow: hidden;

  &:hover {
    transform: translateY(-8px);
    border-color: #667eea;
    box-shadow: 0 20px 40px rgba(102, 126, 234, 0.15);

    .tech-arrow {
      opacity: 1;
      transform: translateX(4px);
    }

    .tech-glow {
      opacity: 1;
      transform: scale(1.1);
    }
  }
}

.tech-card-content {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 24px;
  position: relative;
  z-index: 2;
}

.tech-icon-wrapper {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 60px;
  height: 60px;
  border-radius: 16px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  flex-shrink: 0;
}

.tech-glow {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(circle at center, rgba(255, 255, 255, 0.4) 0%, transparent 70%);
  border-radius: 16px;
  opacity: 0;
  transform: scale(0.8);
  transition: all 0.3s ease;
}

.tech-name {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1a202c;
  flex: 1;
}

.tech-arrow {
  color: #667eea;
  opacity: 0;
  transform: translateX(0);
  transition: all 0.3s ease;
}

.tech-pattern {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  opacity: 0.1;
}

.pattern-dot {
  position: absolute;
  border-radius: 50%;
  background: #667eea;
  animation: float 6s ease-in-out infinite;

  &.dot-1 {
    width: 20px;
    height: 20px;
    top: 20px;
    right: 20px;
    animation-delay: 0s;
  }

  &.dot-2 {
    width: 12px;
    height: 12px;
    bottom: 30px;
    left: 30px;
    animation-delay: 2s;
  }

  &.dot-3 {
    width: 16px;
    height: 16px;
    bottom: 20px;
    right: 40px;
    animation-delay: 4s;
  }
}

// Technology-specific styles
.tech-nodejs {
  border-color: #68a063;
  
  .tech-icon-wrapper {
    background: linear-gradient(135deg, #68a063 0%, #3c873a 100%);
  }
  
  &:hover {
    border-color: #68a063;
    box-shadow: 0 20px 40px rgba(104, 160, 99, 0.15);
  }
}

.tech-vuejs {
  border-color: #41b883;
  
  .tech-icon-wrapper {
    background: linear-gradient(135deg, #41b883 0%, #34495e 100%);
  }
  
  &:hover {
    border-color: #41b883;
    box-shadow: 0 20px 40px rgba(65, 184, 131, 0.15);
  }
}

.tech-reactjs {
  border-color: #61dafb;
  
  .tech-icon-wrapper {
    background: linear-gradient(135deg, #61dafb 0%, #2d79a3 100%);
  }
  
  &:hover {
    border-color: #61dafb;
    box-shadow: 0 20px 40px rgba(97, 218, 251, 0.15);
  }
}

.tech-angular {
  border-color: #dd0031;
  
  .tech-icon-wrapper {
    background: linear-gradient(135deg, #dd0031 0%, #c3002f 100%);
  }
  
  &:hover {
    border-color: #dd0031;
    box-shadow: 0 20px 40px rgba(221, 0, 49, 0.15);
  }
}

.tech-typescript {
  border-color: #3178c6;
  
  .tech-icon-wrapper {
    background: linear-gradient(135deg, #3178c6 0%, #235a97 100%);
  }
  
  &:hover {
    border-color: #3178c6;
    box-shadow: 0 20px 40px rgba(49, 120, 198, 0.15);
  }
}

.tech-mongodb {
  border-color: #47a248;
  
  .tech-icon-wrapper {
    background: linear-gradient(135deg, #47a248 0%, #3d8b3d 100%);
  }
  
  &:hover {
    border-color: #47a248;
    box-shadow: 0 20px 40px rgba(71, 162, 72, 0.15);
  }
}

.selected-tech-card {
  background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%) !important;
  border: 2px solid #667eea;
  margin-top: 24px;
}

.selected-tech-content {
  padding: 32px;
}

.selected-tech-header {
  display: flex;
  align-items: flex-start;
  gap: 20px;
}

.selected-tech-icon {
  width: 64px;
  height: 64px;
  border-radius: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.selected-tech-info {
  flex: 1;
}

.close-btn {
  align-self: flex-start;
}

.tech-details {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
}

.detail-item {
  display: flex;
  align-items: center;
  padding: 12px 16px;
  background: rgba(102, 126, 234, 0.05);
  border-radius: 12px;
  border: 1px solid rgba(102, 126, 234, 0.1);
  font-weight: 500;
  color: #4a5568;
}

// Animations
@keyframes float {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  33% { transform: translateY(-10px) rotate(120deg); }
  66% { transform: translateY(5px) rotate(240deg); }
}

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

.tech-card {
  animation: fadeInUp 0.6s ease-out;
}

.tech-card:nth-child(2) { animation-delay: 0.1s; }
.tech-card:nth-child(3) { animation-delay: 0.2s; }
.tech-card:nth-child(4) { animation-delay: 0.3s; }
.tech-card:nth-child(5) { animation-delay: 0.4s; }
.tech-card:nth-child(6) { animation-delay: 0.5s; }
.tech-card:nth-child(7) { animation-delay: 0.6s; }
.tech-card:nth-child(8) { animation-delay: 0.7s; }
.tech-card:nth-child(9) { animation-delay: 0.8s; }

// Responsive design
@media (max-width: 960px) {
  .tech-chips-grid {
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  }
  
  .selected-tech-header {
    flex-direction: column;
    text-align: center;
    gap: 16px;
  }
  
  .selected-tech-icon {
    align-self: center;
  }
  
  .close-btn {
    align-self: center;
  }
}

@media (max-width: 600px) {
  .tech-stack-container {
    padding: 24px 16px;
  }
  
  .tech-card-content {
    padding: 20px;
  }
  
  .tech-icon-wrapper {
    width: 50px;
    height: 50px;
    
    .v-icon {
      font-size: 24px;
    }
  }
  
  .tech-name {
    font-size: 1.1rem;
  }
  
  .selected-tech-content {
    padding: 24px;
  }
  
  .tech-details {
    grid-template-columns: 1fr;
  }
}
</style>