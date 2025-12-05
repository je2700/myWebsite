<template>
  <div class="home-page">
    <!-- Hero-Bereich -->
    <Hero />

    <!-- Bereich: Ausgewählte Projekte -->
    <section class="featured-section">
      <!-- Hintergrundelemente -->
      <div class="section-background">
        <div class="bg-gradient"></div>
        <div class="floating-shapes">
          <div class="shape shape-1"></div>
          <div class="shape shape-2"></div>
          <div class="shape shape-3"></div>
        </div>
      </div>

      <v-container class="section-container">
        <!-- Abschnittskopf -->
        <div class="section-header">
          <v-card class="section-badge" variant="outlined" rounded="pill">
            <v-card-text class="badge-content">
              <v-icon icon="mdi-star-circle" size="20" class="mr-2" color="primary" />
              <span class="text-caption font-weight-bold">Ausgewählte Arbeiten</span>
            </v-card-text>
          </v-card>

          <h2 class="section-title">
            Meine neuesten
            <span class="title-gradient">Projekte</span>
          </h2>

          <p class="section-subtitle">
            Eine kuratierte Auswahl meiner aktuellsten Open-Source-Beiträge und persönlichen Projekte. 
            Jedes Repository repräsentiert meine Leidenschaft für sauberen Code, innovative Lösungen und kontinuierliches Lernen.
          </p>

          <!-- Schnellstatistiken -->
          <div class="quick-stats">
            <div class="stat-item">
              <div class="stat-icon">
                <v-icon icon="mdi-source-repository" size="24" color="primary" />
              </div>
              <div class="stat-info">
                <div class="stat-number">4+</div>
                <div class="stat-label">Repositories</div>
              </div>
            </div>
            <div class="stat-item">
              <div class="stat-icon">
                <v-icon icon="mdi-star" size="24" color="warning" />
              </div>
              <div class="stat-info">
                <div class="stat-number">0+</div>
                <div class="stat-label">Erhaltene Sterne</div>
              </div>
            </div>
            <div class="stat-item">
              <div class="stat-icon">
                <v-icon icon="mdi-source-branch" size="24" color="success" />
              </div>
              <div class="stat-info">
                <div class="stat-number">2+</div>
                <div class="stat-label">Forks</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Projektübersicht -->
        <div class="projects-content">
          <RepoGrid :limit="6" />

          <!-- Button: Alle ansehen -->
          <div class="view-all-section">
            <v-btn 
              color="primary" 
              variant="outlined" 
              to="/projects" 
              size="large"
              class="view-all-btn"
              rounded="lg"
            >
              <template v-slot:prepend>
                <v-icon icon="mdi-arrow-right" />
              </template>
              Alle Projekte ansehen
            </v-btn>
          </div>
        </div>
      </v-container>
    </section>

    <!-- Bereich: Fähigkeiten -->
    <section class="skills-preview">
      <v-container>
        <v-row align="center">
          <v-col cols="12" md="6" class="skills-content">
            <v-card class="skills-card" variant="outlined" rounded="xl">
              <v-card-text class="skills-card-content">
                <div class="skills-badge">
                  <v-icon icon="mdi-cog" size="20" class="mr-2" color="primary" />
                  <span class="text-caption font-weight-bold">Technologie-Stack</span>
                </div>

                <h3 class="skills-title">
                  Erstellt mit modernen
                  <span class="title-gradient">Technologien</span>
                </h3>

                <p class="skills-description">
                  Ich spezialisiere mich auf Full-Stack-Entwicklung mit modernsten Technologien, 
                  die Skalierbarkeit, Leistung und Wartbarkeit sicherstellen.
                </p>

                <div class="skills-highlights">
                  <div class="highlight-item">
                    <v-icon icon="mdi-check-circle" size="20" color="success" class="mr-2" />
                    <span>Typensichere Entwicklung</span>
                  </div>
                  <div class="highlight-item">
                    <v-icon icon="mdi-check-circle" size="20" color="success" class="mr-2" />
                    <span>Responsives Design</span>
                  </div>
                  <div class="highlight-item">
                    <v-icon icon="mdi-check-circle" size="20" color="success" class="mr-2" />
                    <span>Optimierte Performance</span>
                  </div>
                  <div class="highlight-item">
                    <v-icon icon="mdi-check-circle" size="20" color="success" class="mr-2" />
                    <span>Saubere Code-Architektur</span>
                  </div>
                </div>
              </v-card-text>
            </v-card>
          </v-col>

          <v-col cols="12" md="6" class="tech-visual">
            <div class="tech-animation">
              <div class="orbiting-tech">
                <div class="tech-item item-1">
                  <v-icon icon="mdi-vuejs" size="40" color="#41b883" />
                </div>
                <div class="tech-item item-2">
                  <v-icon icon="mdi-nodejs" size="36" color="#68a063" />
                </div>
                <div class="tech-item item-3">
                  <v-icon icon="mdi-react" size="38" color="#61dafb" />
                </div>
                <div class="tech-item item-4">
                  <v-icon icon="mdi-language-typescript" size="34" color="#3178c6" />
                </div>
                <div class="tech-item item-5">
                  <v-icon icon="mdi-database" size="36" color="#336791" />
                </div>
                <div class="tech-item item-6">
                  <v-icon icon="mdi-angular" size="34" color="#dd0031" />
                </div>
              </div>
              <div class="center-logo">
                <v-icon icon="mdi-hexagon-multiple" size="64" color="primary" />
              </div>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- CTA-Bereich -->
    <section class="cta-section">
      <v-container>
        <v-card class="cta-card" elevation="12" rounded="xl">
          <v-card-text class="cta-content">
            <div class="cta-icon">
              <v-icon icon="mdi-rocket-launch" size="48" color="primary" />
            </div>
            
            <h3 class="cta-title">
              Bereit, Ihre
              <span class="title-gradient">Ideen zum Leben zu erwecken?</span>
            </h3>

            <p class="cta-description">
              Egal Sie ein neues Projekt starten, ein bestehendes verbessern 
               möchten – ich freue mich von Ihnen zu hören.
            </p>

            <div class="cta-actions">
              <v-btn 
                color="primary" 
                size="x-large" 
                to="/contact" 
                class="cta-btn primary"
                rounded="lg"
              >
                <template v-slot:prepend>
                  <v-icon icon="mdi-email" />
                </template>
                Kontakt aufnehmen
              </v-btn>
              
              <v-btn 
                variant="outlined" 
                size="x-large" 
                to="/playground" 
                class="cta-btn secondary"
                rounded="lg"
              >
                <template v-slot:prepend>
                  <v-icon icon="mdi-console" />
                </template>
                API-Spielwiese ausprobieren
              </v-btn>
            </div>
          </v-card-text>

          <!-- CTA Hintergrundelemente -->
          <div class="cta-background">
            <div class="cta-dot dot-1"></div>
            <div class="cta-dot dot-2"></div>
            <div class="cta-dot dot-3"></div>
          </div>
        </v-card>
      </v-container>
    </section>
  </div>
</template>

<script setup lang="ts">
import Hero from '@/components/Hero.vue'
import RepoGrid from '@/components/RepoGrid.vue'
</script>

<style scoped lang="scss">
.home-page {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
}

.featured-section {
  position: relative;
  padding: 120px 0;
  overflow: hidden;
}

.section-background {
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
  height: 100%;
  background: linear-gradient(135deg, 
    rgba(102, 126, 234, 0.03) 0%, 
    rgba(118, 75, 162, 0.02) 50%, 
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
  opacity: 0.05;
  animation: float 8s ease-in-out infinite;

  &.shape-1 {
    width: 200px;
    height: 200px;
    top: 10%;
    right: 10%;
    animation-delay: 0s;
  }

  &.shape-2 {
    width: 120px;
    height: 120px;
    bottom: 20%;
    left: 5%;
    animation-delay: 3s;
  }

  &.shape-3 {
    width: 80px;
    height: 80px;
    top: 50%;
    right: 20%;
    animation-delay: 6s;
  }
}

.section-container {
  position: relative;
  z-index: 2;
}

.section-header {
  text-align: center;
  margin-bottom: 80px;
}

.section-badge {
  backdrop-filter: blur(10px);
  background: rgba(255, 255, 255, 0.05) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  display: inline-block;
  margin-bottom: 40px;
}

.badge-content {
  padding: 12px 20px !important;
  display: flex;
  align-items: center;
  color: white;
}

.section-title {
  font-size: clamp(2.5rem, 4vw, 3.5rem);
  font-weight: 800;
  line-height: 1.1;
  margin-bottom: 24px;
  color: white;
}

.title-gradient {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.section-subtitle {
  font-size: 1.25rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.8);
  max-width: 600px;
  margin: 0 auto 60px;
}

.quick-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 24px;
  max-width: 600px;
  margin: 0 auto;
}

.stat-item {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 20px;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  transition: all 0.3s ease;

  &:hover {
    transform: translateY(-4px);
    border-color: rgba(255, 255, 255, 0.2);
    background: rgba(255, 255, 255, 0.08);
  }
}

.stat-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: rgba(102, 126, 234, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.stat-info {
  flex: 1;
}

.stat-number {
  font-size: 1.5rem;
  font-weight: 800;
  color: white;
  line-height: 1;
  margin-bottom: 4px;
}

.stat-label {
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.7);
  font-weight: 500;
}

.projects-content {
  margin-bottom: 40px;
}

.view-all-section {
  text-align: center;
  margin-top: 60px;
}

.view-all-btn {
  border: 2px solid rgba(255, 255, 255, 0.2);
  color: white !important;
  background: rgba(255, 255, 255, 0.05) !important;
  font-weight: 600;
  padding: 12px 32px;

  &:hover {
    background: rgba(255, 255, 255, 0.1) !important;
    border-color: rgba(255, 255, 255, 0.3);
    transform: translateY(-2px);
  }
}

.skills-preview {
  padding: 120px 0;
  background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
}

.skills-content {
  padding: 40px 0;
}

.skills-card {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  backdrop-filter: blur(20px);
}

.skills-card-content {
  padding: 48px !important;
  color: white;
}

.skills-badge {
  display: inline-flex;
  align-items: center;
  padding: 8px 16px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  margin-bottom: 32px;
  color: white;
}

.skills-title {
  font-size: 2rem;
  font-weight: 700;
  line-height: 1.2;
  margin-bottom: 16px;
  color: white;
}

.skills-description {
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.6;
  margin-bottom: 32px;
}

.skills-highlights {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 40px;
}

.highlight-item {
  display: flex;
  align-items: center;
  color: rgba(255, 255, 255, 0.9);
  font-weight: 500;
}

.skills-cta {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
  color: white !important;
  font-weight: 600;
  padding: 12px 24px;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
  }
}

.tech-visual {
  padding: 40px 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.tech-animation {
  position: relative;
  width: 300px;
  height: 300px;
}

.orbiting-tech {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  animation: rotate 20s linear infinite;
}

.tech-item {
  position: absolute;
  width: 70px;
  height: 70px;
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  animation: float 3s ease-in-out infinite;

  &.item-1 {
    top: 10%;
    left: 50%;
    transform: translateX(-50%);
    animation-delay: 0s;
  }

  &.item-2 {
    top: 50%;
    right: 10%;
    transform: translateY(-50%);
    animation-delay: 1s;
  }

  &.item-3 {
    bottom: 10%;
    left: 50%;
    transform: translateX(-50%);
    animation-delay: 2s;
  }

  &.item-4 {
    top: 50%;
    left: 10%;
    transform: translateY(-50%);
    animation-delay: 3s;
  }
}

.center-logo {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 120px;
  height: 120px;
  border-radius: 30px;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
}

.cta-section {
  padding: 120px 0;
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
}

.cta-card {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  backdrop-filter: blur(20px);
  position: relative;
  overflow: hidden;
  text-align: center;
}

.cta-content {
  padding: 80px 48px !important;
  position: relative;
  z-index: 2;
  color: white;
}

.cta-icon {
  margin-bottom: 32px;
}

.cta-title {
  font-size: clamp(2rem, 3vw, 2.5rem);
  font-weight: 700;
  line-height: 1.2;
  margin-bottom: 16px;
  color: white;
}

.cta-description {
  font-size: 1.25rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.8);
  max-width: 500px;
  margin: 0 auto 40px;
}

.cta-actions {
  display: flex;
  gap: 16px;
  justify-content: center;
  flex-wrap: wrap;
}

.cta-btn {
  min-width: 200px;
  font-weight: 600;
  text-transform: none;

  &.primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);

    &:hover {
      transform: translateY(-3px);
      box-shadow: 0 12px 30px rgba(102, 126, 234, 0.6);
    }
  }

  &.secondary {
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

.cta-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
}

.cta-dot {
  position: absolute;
  border-radius: 50%;
  background: rgba(102, 126, 234, 0.1);
  animation: float 6s ease-in-out infinite;

  &.dot-1 {
    width: 40px;
    height: 40px;
    top: 20%;
    left: 10%;
    animation-delay: 0s;
  }

  &.dot-2 {
    width: 25px;
    height: 25px;
    bottom: 30%;
    right: 15%;
    animation-delay: 2s;
  }

  &.dot-3 {
    width: 30px;
    height: 30px;
    top: 60%;
    left: 20%;
    animation-delay: 4s;
  }
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

@keyframes rotate {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

// Responsive design
@media (max-width: 960px) {
  .featured-section,
  .skills-preview,
  .cta-section {
    padding: 80px 0;
  }

  .quick-stats {
    grid-template-columns: 1fr;
    gap: 16px;
  }

  .stat-item {
    padding: 16px;
  }

  .tech-animation {
    width: 250px;
    height: 250px;
  }

  .tech-item {
    width: 60px;
    height: 60px;

    .v-icon {
      font-size: 28px;
    }
  }

  .center-logo {
    width: 100px;
    height: 100px;

    .v-icon {
      font-size: 48px;
    }
  }

  .cta-content {
    padding: 60px 32px !important;
  }

  .cta-actions {
    flex-direction: column;
    align-items: center;
  }

  .cta-btn {
    width: 100%;
    max-width: 280px;
  }
}

@media (max-width: 600px) {
  .section-header {
    margin-bottom: 60px;
  }

  .section-title {
    font-size: 2rem;
  }

  .section-subtitle {
    font-size: 1.125rem;
  }

  .skills-card-content {
    padding: 32px !important;
  }

  .skills-title {
    font-size: 1.5rem;
  }

  .tech-animation {
    width: 200px;
    height: 200px;
  }

  .tech-item {
    width: 50px;
    height: 50px;

    .v-icon {
      font-size: 24px;
    }
  }

  .center-logo {
    width: 80px;
    height: 80px;

    .v-icon {
      font-size: 36px;
    }
  }
}

// Reduced motion support
@media (prefers-reduced-motion: reduce) {
  .floating-shapes,
  .orbiting-tech,
  .tech-item,
  .cta-dot {
    animation: none;
  }

  .stat-item:hover,
  .view-all-btn:hover,
  .skills-cta:hover,
  .cta-btn:hover {
    transform: none;
  }
}
</style>