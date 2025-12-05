<template>
  <div class="projects-page">
    <!-- Hintergrund-Elemente -->
    <div class="page-background">
      <div class="bg-gradient"></div>
      <div class="floating-elements">
        <div class="element element-1">
          <v-icon icon="mdi-source-branch" size="40" />
        </div>
        <div class="element element-2">
          <v-icon icon="mdi-git" size="32" />
        </div>
        <div class="element element-3">
          <v-icon icon="mdi-code-braces" size="36" />
        </div>
        <div class="element element-4">
          <v-icon icon="mdi-rocket" size="38" />
        </div>
      </div>
      <div class="grid-pattern"></div>
    </div>

    <v-container class="page-container">
      <!-- Kopfbereich -->
      <div class="page-header">
        <v-card class="header-badge" variant="outlined" rounded="pill">
          <v-card-text class="badge-content">
            <v-icon icon="mdi-code-tags" size="20" class="mr-2" color="primary" />
            <span class="text-caption font-weight-bold">Mein Portfolio</span>
          </v-card-text>
        </v-card>

        <h1 class="page-title">
          Meine
          <span class="title-gradient">Projekte</span>
        </h1>

        <p class="page-subtitle">
          Eine umfassende Sammlung meiner Open-Source-Beiträge, persönlichen Projekte 
          und gemeinsamen Arbeiten. Jedes Projekt stellt eine einzigartige Herausforderung und Lernmöglichkeit dar.
        </p>

        <!-- Portfolio-Statistiken -->
        <div class="portfolio-stats">
          <div class="stat-card">
            <div class="stat-icon">
              <v-icon icon="mdi-source-repository" size="32" color="primary" />
            </div>
            <div class="stat-content">
              <div class="stat-number">5+</div>
              <div class="stat-label">Repositorys</div>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">
              <v-icon icon="mdi-package-variant" size="32" color="secondary" />
            </div>
            <div class="stat-content">
              <div class="stat-number">5+</div>
              <div class="stat-label">Produkte</div>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">
              <v-icon icon="mdi-source-fork" size="32" color="success" />
            </div>
            <div class="stat-content">
              <div class="stat-number">5+</div>
              <div class="stat-label">Forks</div>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">
              <v-icon icon="mdi-clock" size="32" color="info" />
            </div>
            <div class="stat-content">
              <div class="stat-number">2+</div>
              <div class="stat-label">Aktive Jahre</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Projekte-Raster-Bereich -->
      <section class="projects-section">
        <v-card class="projects-container" elevation="12" rounded="xl">
          <v-card-text class="projects-content">
            <!-- Abschnittskopf -->
            <div class="section-header">
              <div class="header-main">
                <v-icon icon="mdi-view-grid" size="32" color="primary" class="header-icon" />
                <div class="header-text">
                  <h2 class="section-title">Projekt-Galerie</h2>
                  <p class="section-description">
                    Durchstöbern Sie meine vollständige Sammlung von Repositorys. Filtern Sie nach Technologie, 
                    sortieren Sie nach Beliebtheit oder suchen Sie nach bestimmten Projekten.
                  </p>
                </div>
              </div>
              <div class="header-actions">
                <v-btn
                  variant="outlined"
                  size="small"
                  :href="`https://github.com/${username}`"
                  target="_blank"
                  class="github-btn"
                  rounded="lg"
                >
                  <v-icon icon="mdi-github" class="mr-2" />
                  Auf GitHub ansehen
                </v-btn>
              </div>
            </div>

            <!-- Hervorgehobene Projekte -->
            <div class="featured-projects">
              <div class="featured-header">
                <h3 class="featured-title">
                  <v-icon icon="mdi-star" size="24" color="warning" class="mr-2" />
                  Hervorgehobene Projekte
                </h3>
                <p class="featured-subtitle">Meine beliebtesten und einflussreichsten Repositorys</p>
              </div>

              <!-- Hervorgehobene Projekte Raster -->
              <div class="featured-grid">
                <v-card
                  v-for="project in featuredProjects"
                  :key="project.id"
                  class="featured-card"
                  :href="project.url"
                  target="_blank"
                  elevation="4"
                  rounded="lg"
                  hover
                >
                  <v-card-text class="featured-card-content">
                    <div class="project-header">
                      <div class="project-icon">
                        <v-icon :icon="project.icon" size="32" :color="project.color" />
                      </div>
                      <div class="project-badge">
                        <v-chip size="x-small" :color="project.badgeColor" variant="flat">
                          Hervorgehoben
                        </v-chip>
                      </div>
                    </div>
                    <h4 class="project-title">{{ project.title }}</h4>
                    <p class="project-description">{{ project.description }}</p>
                    <div class="project-stats">
                      <div class="stat">
                        <v-icon icon="mdi-star" size="16" />
                        <span>{{ project.stars }}</span>
                      </div>
                      <div class="stat">
                        <v-icon icon="mdi-source-fork" size="16" />
                        <span>{{ project.forks }}</span>
                      </div>
                      <div class="stat">
                        <v-icon icon="mdi-circle" size="16" :color="project.languageColor" />
                        <span>{{ project.language }}</span>
                      </div>
                    </div>
                    <div class="project-tech">
                      <v-chip
                        v-for="tech in project.technologies"
                        :key="tech"
                        size="x-small"
                        variant="outlined"
                        class="tech-tag"
                      >
                        {{ tech }}
                      </v-chip>
                    </div>
                  </v-card-text>
                  <div class="featured-glow" :style="{ background: project.gradient }" />
                </v-card>
              </div>
            </div>

            <!-- Haupt-Projekte-Raster -->
            <div class="main-projects">
              <RepoGrid />
            </div>

            <!-- Call-to-Action -->
            <div class="projects-cta">
              <v-card class="cta-card" variant="outlined" rounded="lg">
                <v-card-text class="cta-content">
                  <div class="cta-icon">
                    <v-icon icon="mdi-github" size="48" color="primary" />
                  </div>
                  <h3 class="cta-title">Möchten Sie mehr sehen?</h3>
                  <p class="cta-description">
                    Erkunden Sie mein komplettes GitHub-Profil, um alle meine Repositorys, 
                    Beiträge und laufenden Projekte zu entdecken.
                  </p>
                  <v-btn 
                    color="primary" 
                    variant="flat" 
                    :href="`https://github.com/${username}`"
                    target="_blank"
                    class="cta-btn"
                    rounded="lg"
                    size="large"
                  >
                    <v-icon icon="mdi-open-in-new" class="mr-2" />
                    Mein GitHub besuchen
                  </v-btn>
                </v-card-text>
              </v-card>
            </div>
          </v-card-text>

          <!-- Container-Dekoration -->
          <div class="container-decoration">
            <div class="decoration-dot dot-1"></div>
            <div class="decoration-dot dot-2"></div>
            <div class="decoration-dot dot-3"></div>
          </div>
        </v-card>
      </section>

      <!-- Technologien-Bereich -->
      <section class="technologies-section">
        <v-row align="center">
          <v-col cols="12" md="6" class="tech-content">
            <v-card class="tech-card" variant="outlined" rounded="xl">
              <v-card-text class="tech-card-content">
                <div class="tech-badge">
                  <v-icon icon="mdi-cog" size="20" class="mr-2" color="primary" />
                  <span class="text-caption font-weight-bold">Tech-Stack</span>
                </div>

                <h3 class="tech-title">Technologien, die ich liebe</h3>

                <p class="tech-description">
                  Ich arbeite mit einer vielfältigen Auswahl an Technologien im gesamten Stack, 
                  erkunde ständig neue Tools und Frameworks, um bessere Lösungen zu entwickeln.
                </p>

                <div class="tech-stats">
                  <div class="tech-stat">
                    <div class="stat-value">100%</div>
                    <div class="stat-label">Vue 3 (Vuetify-latest)</div>
                    <v-progress-linear model-value="100" color="success" height="8" rounded />
                  </div>
                  <div class="tech-stat">
                    <div class="stat-value">85%</div>
                    <div class="stat-label">JavaScript/TypeScript & HTML5 & CSS3</div>
                    <v-progress-linear model-value="85" color="primary" height="8" rounded />
                  </div>
                  <div class="tech-stat">
                    <div class="stat-value">80%</div>
                    <div class="stat-label">Node.js & Express.js</div>
                    <v-progress-linear model-value="80" color="warning" height="8" rounded />
                  </div>
                  <div class="tech-start">
                    <div class="stat-value">75%</div>
                    <div class="stat-label">Apache-Cordova</div>
                    <v-progress-linear model-value="75" color="error" height="8" rounded />
                  </div>
                  <div class="tech-stat">
                    <div class="stat-value">70%</div>
                    <div class="stat-label">React.js & Angular.ts</div>
                    <v-progress-linear model-value="70" color="info" height="8" rounded />
                  </div>
                  <div class="tech-stat">
                    <div class="stat-value">65%</div>
                    <div class="stat-label">Datenbanken</div>
                    <v-progress-linear model-value="65" color="info" height="8" rounded />
                  </div>
                </div>
              </v-card-text>
            </v-card>
          </v-col>

          <v-col cols="12" md="6" class="tech-visual">
            <div class="tech-animation">
              <div class="orbiting-tech">
                <div class="tech-orbiter orbiter-1">
                  <v-icon icon="mdi-vuejs" size="40" color="#41b883" />
                </div>
                <div class="tech-orbiter orbiter-2">
                  <v-icon icon="mdi-nodejs" size="36" color="#68a063" />
                </div>
                <div class="tech-orbiter orbiter-3">
                  <v-icon icon="mdi-react" size="38" color="#61dafb" />
                </div>
                <div class="tech-orbiter orbiter-4">
                  <v-icon icon="mdi-language-typescript" size="34" color="#3178c6" />
                </div>
                <div class="tech-orbiter orbiter-5">
                  <v-icon icon="mdi-angular" size="36" color="#dd0031" />
                </div>
              </div>
              <div class="center-element">
                <v-icon icon="mdi-hexagon-multiple" size="64" color="primary" />
              </div>
            </div>
          </v-col>
        </v-row>
      </section>
    </v-container>
  </div>
</template>

<script setup lang="ts">
import RepoGrid from '@/components/RepoGrid.vue'

// GitHub-Benutzername
const username = 'je2700'

const featuredProjects = [
  {
    id: 1,
    title: 'je2700.github.io',
    description: 'Hauptseite - Portfolio-Website mit Vue.js und Vuetify',
    icon: 'mdi-web',
    color: '#667eea',
    badgeColor: 'primary',
    stars: 0,
    forks: 0,
    language: 'Vue.js',
    languageColor: '#41b883',
    technologies: ['Vue.js', 'Vuetify', 'TypeScript', 'Public'],
    gradient: 'linear-gradient(135deg, #667eea, #764ba2)',
    url: 'https://github.com/je2700/je2700.github.io'
  },
  {
    id: 2,
    title: 'Vue U-Bahn',
    description: 'Interaktive U-Bahn-Netzplan-Visualisierung entwickelt mit Vue.js und Vuetify',
    icon: 'mdi-vuetify',
    color: '#1867c0',
    badgeColor: 'primary',
    stars: 0,
    forks: 0,
    language: 'Vue.js',
    languageColor: '#41b883',
    technologies: ['Vue.js', 'Vuetify', 'JavaScript', 'TypeScript'],
    gradient: 'linear-gradient(135deg, #41b883, #34495e)',
    url: 'https://github.com/je2700/vue-u-bahn'
  },
  {
    id: 3,
    title: 'React Mini-Shop',
    description: 'E‑Commerce Mini-Shop Anwendung mit React und TypeScript',
    icon: 'mdi-react',
    color: '#61dafb',
    badgeColor: 'info',
    stars: 0,
    forks: 1,
    language: 'React',
    languageColor: '#61dafb',
    technologies: ['React', 'TypeScript'],
    gradient: 'linear-gradient(135deg, #61dafb, #2d79a3)',
    url: 'https://github.com/je2700/react-mini-shop'
  },
  {
    id: 4,
    title: 'Angular KPI-Cards',
    description: 'KPI-Dashboard mit ansprechenden Kartenkomponenten in Angular',
    icon: 'mdi-angular',
    color: '#e67e22',
    badgeColor: 'warning',
    stars: 0,
    forks: 1,
    language: 'Angular',
    languageColor: '#dd0031',
    technologies: ['Angular', 'TypeScript', 'Node.js'],
    gradient: 'linear-gradient(135deg, #e67e22, #d35400)',
    url: 'https://github.com/je2700/angular-kpi-cards'
  }
]
</script>

<style scoped lang="scss">
.projects-page {
  position: relative;
  min-height: 100vh;
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
  overflow: hidden;
}

.page-background {
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
    rgba(102, 126, 234, 0.05) 0%, 
    rgba(118, 75, 162, 0.03) 50%, 
    transparent 100%);
}

.floating-elements {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.element {
  position: absolute;
  width: 80px;
  height: 80px;
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(255, 255, 255, 0.3);
  animation: float 6s ease-in-out infinite;

  &.element-1 {
    top: 10%;
    left: 5%;
    animation-delay: 0s;
  }

  &.element-2 {
    top: 60%;
    left: 3%;
    animation-delay: 2s;
  }

  &.element-3 {
    bottom: 20%;
    right: 5%;
    animation-delay: 4s;
  }

  &.element-4 {
    top: 30%;
    right: 8%;
    animation-delay: 1s;
  }
}

.grid-pattern {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: 
    linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
  background-size: 50px 50px;
}

.page-container {
  position: relative;
  z-index: 2;
  padding: 40px 24px;
}

.page-header {
  text-align: center;
  margin-bottom: 80px;
}

.header-badge {
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

.page-title {
  font-size: clamp(2.5rem, 5vw, 4rem);
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

.page-subtitle {
  font-size: 1.25rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.8);
  max-width: 600px;
  margin: 0 auto 60px;
}

.portfolio-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 24px;
  max-width: 800px;
  margin: 0 auto;
}

.stat-card {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 24px;
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
  width: 60px;
  height: 60px;
  border-radius: 16px;
  background: rgba(102, 126, 234, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.stat-content {
  flex: 1;
}

.stat-number {
  font-size: 1.75rem;
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

.projects-section {
  margin-bottom: 80px;
}

.projects-container {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  backdrop-filter: blur(20px);
  position: relative;
  overflow: hidden;
}

.projects-content {
  padding: 40px !important;
  position: relative;
  z-index: 2;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 48px;
  flex-wrap: wrap;
  gap: 16px;
}

.header-main {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  flex: 1;
}

.header-icon {
  margin-top: 4px;
}

.header-text {
  flex: 1;
}

.section-title {
  font-size: 2rem;
  font-weight: 700;
  color: white;
  margin-bottom: 8px;
}

.section-description {
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.5;
  max-width: 500px;
}

.github-btn {
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: white !important;
  background: rgba(255, 255, 255, 0.05) !important;
  font-weight: 500;

  &:hover {
    background: rgba(255, 255, 255, 0.1) !important;
  }
}

.featured-projects {
  margin-bottom: 60px;
}

.featured-header {
  margin-bottom: 32px;
}

.featured-title {
  display: flex;
  align-items: center;
  font-size: 1.5rem;
  font-weight: 600;
  color: white;
  margin-bottom: 8px;
}

.featured-subtitle {
  color: rgba(255, 255, 255, 0.7);
  font-size: 1rem;
}

.featured-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
  margin-bottom: 40px;
}

.featured-card {
  background: rgba(255, 255, 255, 0.05) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  position: relative;
  overflow: hidden;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;

  &:hover {
    transform: translateY(-8px);
    border-color: rgba(255, 255, 255, 0.2) !important;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);

    .featured-glow {
      opacity: 0.6;
    }
  }
}

.featured-card-content {
  padding: 32px !important;
  position: relative;
  z-index: 2;
  color: white;
}

.project-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 16px;
}

.project-icon {
  width: 64px;
  height: 64px;
  border-radius: 16px;
  background: rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
}

.project-badge {
  flex-shrink: 0;
}

.project-title {
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 12px;
  color: white;
}

.project-description {
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.5;
  margin-bottom: 20px;
}

.project-stats {
  display: flex;
  gap: 16px;
  margin-bottom: 20px;
}

.stat {
  display: flex;
  align-items: center;
  gap: 6px;
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.875rem;
  font-weight: 500;
}

.project-tech {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tech-tag {
  backdrop-filter: blur(10px);
  background: rgba(255, 255, 255, 0.05) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  color: rgba(255, 255, 255, 0.8) !important;
  font-size: 0.7rem;
}

.featured-glow {
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

.main-projects {
  margin-bottom: 60px;
}

.projects-cta {
  text-align: center;
}

.cta-card {
  background: rgba(255, 255, 255, 0.03) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  backdrop-filter: blur(10px);
}

.cta-content {
  padding: 48px !important;
  color: white;
}

.cta-icon {
  margin-bottom: 24px;
}

.cta-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 12px;
  color: white;
}

.cta-description {
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.5;
  margin-bottom: 24px;
  max-width: 400px;
  margin-left: auto;
  margin-right: auto;
}

.cta-btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
  color: white !important;
  font-weight: 600;
  padding: 12px 32px;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
  }
}

.container-decoration {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
}

.decoration-dot {
  position: absolute;
  border-radius: 50%;
  background: rgba(102, 126, 234, 0.1);
  animation: float 4s ease-in-out infinite;

  &.dot-1 {
    width: 20px;
    height: 20px;
    top: 10%;
    right: 10%;
    animation-delay: 0s;
  }

  &.dot-2 {
    width: 12px;
    height: 12px;
    bottom: 20%;
    left: 10%;
    animation-delay: 1.5s;
  }

  &.dot-3 {
    width: 16px;
    height: 16px;
    bottom: 10%;
    right: 20%;
    animation-delay: 3s;
  }
}

.technologies-section {
  margin-bottom: 40px;
}

.tech-content {
  padding: 40px 0;
}

.tech-card {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  backdrop-filter: blur(20px);
  height: 100%;
}

.tech-card-content {
  padding: 48px !important;
  color: white;
  height: 100%;
}

.tech-badge {
  display: inline-flex;
  align-items: center;
  padding: 8px 16px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  margin-bottom: 32px;
  color: white;
}

.tech-title {
  font-size: 1.75rem;
  font-weight: 700;
  margin-bottom: 16px;
  color: white;
}

.tech-description {
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.6;
  margin-bottom: 32px;
}

.tech-stats {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.tech-stat {
  .stat-value {
    font-size: 1rem;
    font-weight: 600;
    color: white;
    margin-bottom: 8px;
  }

  .stat-label {
    font-size: 0.875rem;
    color: rgba(255, 255, 255, 0.7);
    margin-bottom: 8px;
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

.tech-orbiter {
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

  &.orbiter-1 {
    top: 10%;
    left: 50%;
    transform: translateX(-50%);
    animation-delay: 0s;
  }

  &.orbiter-2 {
    top: 50%;
    right: 10%;
    transform: translateY(-50%);
    animation-delay: 1s;
  }

  &.orbiter-3 {
    bottom: 10%;
    left: 50%;
    transform: translateX(-50%);
    animation-delay: 2s;
  }

  &.orbiter-4 {
    top: 50%;
    left: 10%;
    transform: translateY(-50%);
    animation-delay: 3s;
  }
}

.center-element {
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
  .page-container {
    padding: 32px 16px;
  }

  .page-header {
    margin-bottom: 60px;
  }

  .portfolio-stats {
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
  }

  .stat-card {
    padding: 20px;
  }

  .projects-content {
    padding: 32px !important;
  }

  .section-header {
    flex-direction: column;
    align-items: stretch;
  }

  .header-main {
    flex-direction: column;
    text-align: center;
  }

  .header-icon {
    align-self: center;
  }

  .featured-grid {
    grid-template-columns: 1fr;
  }

  .tech-card-content {
    padding: 32px !important;
  }
}

@media (max-width: 600px) {
  .page-title {
    font-size: 2rem;
  }

  .page-subtitle {
    font-size: 1.125rem;
  }

  .portfolio-stats {
    grid-template-columns: 1fr;
  }

  .section-title {
    font-size: 1.5rem;
  }

  .featured-card-content {
    padding: 24px !important;
  }

  .project-header {
    flex-direction: column;
    gap: 12px;
    align-items: flex-start;
  }

  .project-icon {
    width: 48px;
    height: 48px;
  }

  .tech-animation {
    width: 250px;
    height: 250px;
  }

  .tech-orbiter {
    width: 60px;
    height: 60px;

    .v-icon {
      font-size: 28px;
    }
  }

  .center-element {
    width: 100px;
    height: 100px;

    .v-icon {
      font-size: 48px;
    }
  }

  .floating-elements .element {
    width: 60px;
    height: 60px;

    .v-icon {
      font-size: 24px;
    }
  }
}

// Reduced motion support
@media (prefers-reduced-motion: reduce) {
  .floating-elements,
  .container-decoration,
  .orbiting-tech,
  .tech-orbiter,
  .stat-card,
  .featured-card {
    animation: none;
    transition: none;
  }

  .featured-card:hover {
    transform: none;
  }
}
</style>