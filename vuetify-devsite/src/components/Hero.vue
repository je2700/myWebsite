<template>
  <section class="hero-section">
    <!-- Hintergrundelemente -->
    <div class="hero-background">
      <div class="bg-gradient"></div>
      <div class="floating-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
        <div class="shape shape-4"></div>
        <div class="shape shape-5"></div>
      </div>
      <div class="grid-pattern"></div>
    </div>

    <v-container class="hero-container">
      <v-row align="center" class="hero-row">
        <!-- Textbereich -->
        <v-col cols="12" md="7" class="hero-text">
          <!-- Badge -->
          <v-card class="hero-badge" variant="outlined" rounded="pill">
            <v-card-text class="badge-content">
              <v-icon icon="mdi-star-four-points" size="20" class="mr-2" color="primary" />
              <span class="text-caption font-weight-bold">Full-Stack-Entwickler</span>
            </v-card-text>
          </v-card>

          <!-- Hauptüberschrift -->
          <h1 class="hero-title">
            <span class="title-line">Digitale</span>
            <span class="title-line title-gradient">Erlebnisse</span>
            <span class="title-line">gestalten, die inspirieren</span>
          </h1>

          <!-- Untertitel -->
          <p class="hero-subtitle">
            Ich entwickle leistungsstarke Webanwendungen & APIs mit modernen Technologien. 
            Leidenschaftlich für sauberen Code, Benutzererfahrung und innovative Lösungen.
          </p>

          <!-- Statistiken -->
          <div class="hero-stats">
            <div class="stat-item">
              <div class="stat-number">5+</div>
              <div class="stat-label">Projekte</div>
            </div>
            <div class="stat-item">
              <div class="stat-number">2+</div>
              <div class="stat-label">Jahre</div>
            </div>
            <div class="stat-item">
              <div class="stat-number">100%</div>
              <div class="stat-label">Zufriedenheit</div>
            </div>
          </div>

          <!-- Tech Chips -->
          <div class="tech-section">
            <TechChips />
          </div>

          <!-- Aktionsbuttons -->
          <div class="hero-actions">
            <v-btn 
              color="primary" 
              size="x-large" 
              to="/projects" 
              class="action-btn primary-btn"
              rounded="lg"
            >
              <template v-slot:prepend>
                <v-icon icon="mdi-rocket-launch" />
              </template>
              Meine Arbeit ansehen
            </v-btn>
            
            <v-btn 
              variant="outlined" 
              size="x-large" 
              to="/playground" 
              class="action-btn secondary-btn"
              rounded="lg"
            >
              <template v-slot:prepend>
                <v-icon icon="mdi-console" />
              </template>
              API-Spielwiese
            </v-btn>
          </div>
        </v-col>

        <!-- Illustration -->
        <v-col cols="12" md="5" class="hero-visual">
          <div class="illustration-container">
            <!-- Hauptillustration -->
            <v-card class="illustration-card" elevation="12" rounded="xl">
              <v-img 
                :src="illustration" 
                class="hero-illustration"
                alt="Entwickler-Illustration"
                width="100%"
                height="100%"
              />
              
              <!-- Schwebende Elemente -->
              <div class="floating-element element-1">
                <v-icon icon="mdi-vuejs" size="32" color="#41b883" />
              </div>
              <div class="floating-element element-2">
                <v-icon icon="mdi-nodejs" size="28" color="#68a063" />
              </div>
              <div class="floating-element element-3">
                <v-icon icon="mdi-react" size="30" color="#61dafb" />
              </div>
              <div class="floating-element element-4">
                <v-icon icon="mdi-language-typescript" size="26" color="#3178c6" />
              </div>
            </v-card>

            <!-- Erfahrungs-Badge -->
            <v-card class="experience-badge" elevation="8" rounded="lg">
              <v-card-text class="experience-content">
                <div class="experience-icon">
                  <v-icon icon="mdi-trophy" size="24" color="warning" />
                </div>
                <div class="experience-text">
                  <div class="text-body-2 font-weight-bold">2+ Jahre</div>
                  <div class="text-caption text-white">Erfahrung</div>
                </div>
              </v-card-text>
            </v-card>

            <!-- Projektzähler -->
            <v-card class="project-badge" elevation="8" rounded="lg">
              <v-card-text class="project-content">
                <div class="project-number">5+</div>
                <div class="project-label">Projekte</div>
              </v-card-text>
            </v-card>
          </div>
        </v-col>
      </v-row>

      <!-- Scroll-Indikator -->
      <div class="scroll-indicator">
        <div class="scroll-text">Scrollen zum Entdecken</div>
        <div class="scroll-arrow">
          <v-icon icon="mdi-chevron-down" size="20" />
        </div>
      </div>
    </v-container>
  </section>
</template>


<script setup lang="ts">
import TechChips from '@/components/TechChips.vue'

// nutzt im Dev "/" und im Prod (GitHub Pages) automatisch "/REPO_NAME/"
const illustration = import.meta.env.BASE_URL + 'hero-dev.svg'
</script>

<style scoped lang="scss">
.hero-section {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  overflow: hidden;
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
}

.hero-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
}

.bg-gradient {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 80%;
  background: linear-gradient(135deg, 
    rgba(102, 126, 234, 0.1) 0%, 
    rgba(118, 75, 162, 0.05) 50%, 
    transparent 100%);
}

.floating-shapes {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.shape {
  position: absolute;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea, #764ba2);
  opacity: 0.1;
  animation: float 6s ease-in-out infinite;

  &.shape-1 {
    width: 120px;
    height: 120px;
    top: 10%;
    left: 10%;
    animation-delay: 0s;
  }

  &.shape-2 {
    width: 80px;
    height: 80px;
    top: 60%;
    left: 5%;
    animation-delay: 2s;
  }

  &.shape-3 {
    width: 160px;
    height: 160px;
    top: 20%;
    right: 10%;
    animation-delay: 4s;
  }

  &.shape-4 {
    width: 60px;
    height: 60px;
    bottom: 20%;
    right: 20%;
    animation-delay: 1s;
  }

  &.shape-5 {
    width: 100px;
    height: 100px;
    bottom: 10%;
    left: 20%;
    animation-delay: 3s;
  }
}

.grid-pattern {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: 
    linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
  background-size: 50px 50px;
}

.hero-container {
  position: relative;
  z-index: 2;
}

.hero-row {
  min-height: 80vh;
}

.hero-text {
  padding: 40px 0;
}

.hero-badge {
  backdrop-filter: blur(10px);
  background: rgba(255, 255, 255, 0.05) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  display: inline-block;
  margin-bottom: 32px;
}

.badge-content {
  padding: 8px 16px !important;
  display: flex;
  align-items: center;
  color: white;
}

.hero-title {
  font-size: clamp(2.5rem, 5vw, 4rem);
  font-weight: 800;
  line-height: 1.1;
  margin-bottom: 24px;
  color: white;
}

.title-line {
  display: block;
}

.title-gradient {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-subtitle {
  font-size: 1.25rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 40px;
  max-width: 600px;
}

.hero-stats {
  display: flex;
  gap: 32px;
  margin-bottom: 40px;
}

.stat-item {
  text-align: center;
}

.stat-number {
  font-size: 2rem;
  font-weight: 800;
  color: #667eea;
  line-height: 1;
  margin-bottom: 4px;
}

.stat-label {
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.7);
  font-weight: 500;
}

.tech-section {
  margin-bottom: 48px;
}

.hero-actions {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}

.action-btn {
  min-width: 160px;
  font-weight: 600;
  text-transform: none;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);

  &.primary-btn {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);

    &:hover {
      transform: translateY(-3px);
      box-shadow: 0 12px 30px rgba(102, 126, 234, 0.6);
    }
  }

  &.secondary-btn {
    border: 2px solid rgba(255, 255, 255, 0.2);
    color: white !important;
    background: rgba(255, 255, 255, 0.05) !important;

    &:hover {
      background: rgba(255, 255, 255, 0.1) !important;
      border-color: rgba(255, 255, 255, 0.3);
      transform: translateY(-2px);
    }
  }
}

.hero-visual {
  position: relative;
  padding: 40px 0;
}

.illustration-container {
  position: relative;
  max-width: 500px;
  margin: 0 auto;
}

.illustration-card {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  backdrop-filter: blur(20px);
  overflow: hidden;
}

.hero-illustration {
  border-radius: inherit;
}

.floating-element {
  position: absolute;
  width: 60px;
  height: 60px;
  border-radius: 16px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  animation: float 3s ease-in-out infinite;

  &.element-1 {
    top: 10%;
    right: 10%;
    animation-delay: 0s;
  }

  &.element-2 {
    top: 60%;
    right: 5%;
    animation-delay: 1s;
  }

  &.element-3 {
    bottom: 20%;
    left: 5%;
    animation-delay: 2s;
  }

  &.element-4 {
    bottom: 10%;
    left: 20%;
    animation-delay: 1.5s;
  }
}

.experience-badge {
  position: absolute;
  top: -20px;
  left: -20px;
  background: linear-gradient(135deg, #1e293b 0%, #334155 100%) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  backdrop-filter: blur(10px);
}

.experience-content {
  padding: 16px !important;
  display: flex;
  align-items: center;
  gap: 12px;
  color: white;
}

.experience-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: rgba(245, 158, 11, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
}

.project-badge {
  position: absolute;
  bottom: -20px;
  right: -20px;
  background: linear-gradient(135deg, #1e293b 0%, #334155 100%) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  backdrop-filter: blur(10px);
  text-align: center;
}

.project-content {
  padding: 20px 16px !important;
  color: white;
}

.project-number {
  font-size: 1.5rem;
  font-weight: 800;
  color: #667eea;
  line-height: 1;
  margin-bottom: 4px;
}

.project-label {
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.7);
}

.scroll-indicator {
  position: absolute;
  bottom: 40px;
  left: 50%;
  transform: translateX(-50%);
  text-align: center;
  color: rgba(255, 255, 255, 0.6);
  animation: bounce 2s ease-in-out infinite;
}

.scroll-text {
  font-size: 0.875rem;
  margin-bottom: 8px;
  font-weight: 500;
}

.scroll-arrow {
  color: #667eea;
}

// Animations
@keyframes float {
  0%, 100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-20px);
  }
}

@keyframes bounce {
  0%, 100% {
    transform: translateX(-50%) translateY(0);
  }
  50% {
    transform: translateX(-50%) translateY(-10px);
  }
}

// Responsive design
@media (max-width: 960px) {
  .hero-stats {
    gap: 24px;
  }

  .stat-number {
    font-size: 1.5rem;
  }

  .hero-actions {
    justify-content: center;
  }

  .floating-element {
    width: 50px;
    height: 50px;

    .v-icon {
      font-size: 24px;
    }
  }
}

@media (max-width: 600px) {
  .hero-section {
    min-height: auto;
    padding: 80px 0;
  }

  .hero-title {
    font-size: 2.5rem;
  }

  .hero-subtitle {
    font-size: 1.125rem;
  }

  .hero-stats {
    gap: 16px;
  }

  .stat-number {
    font-size: 1.25rem;
  }

  .hero-actions {
    flex-direction: column;
    align-items: center;
  }

  .action-btn {
    width: 100%;
    max-width: 280px;
  }

  .experience-badge,
  .project-badge {
    position: relative;
    top: auto;
    left: auto;
    bottom: auto;
    right: auto;
    margin: 16px auto;
    max-width: 200px;
  }

  .illustration-container {
    margin-top: 40px;
  }

  .scroll-indicator {
    position: relative;
    bottom: auto;
    margin-top: 40px;
  }
}

// Reduced motion support
@media (prefers-reduced-motion: reduce) {
  .floating-shapes,
  .floating-element,
  .scroll-indicator {
    animation: none;
  }

  .action-btn:hover {
    transform: none;
  }
}
</style>