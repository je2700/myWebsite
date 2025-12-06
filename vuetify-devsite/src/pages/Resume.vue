<template>
  <div class="resume-page">
    <!-- Hintergrund-Elemente -->
    <div class="page-background">
      <div class="bg-gradient"></div>
      <div class="floating-elements">
        <div class="element element-1">
          <v-icon icon="mdi-briefcase" size="40" />
        </div>
        <div class="element element-2">
          <v-icon icon="mdi-school" size="32" />
        </div>
        <div class="element element-3">
          <v-icon icon="mdi-certificate" size="36" />
        </div>
        <div class="element element-4">
          <v-icon icon="mdi-trophy" size="38" />
        </div>
      </div>
      <div class="grid-pattern"></div>
    </div>

    <v-container class="page-container">
      <!-- Kopfbereich -->
      <div class="page-header">
        <v-card class="header-badge" variant="outlined" rounded="pill">
          <v-card-text class="badge-content">
            <v-icon icon="mdi-account-tie" size="20" class="mr-2" color="primary" />
            <span class="text-caption font-weight-bold">Beruflicher Werdegang</span>
          </v-card-text>
        </v-card>

        <h1 class="page-title">
          Mein
          <span class="title-gradient">Lebenslauf</span>
        </h1>

        <p class="page-subtitle">
          Ein umfassender Überblick über meine Berufserfahrung, Ausbildung 
          und die Reise, die meine Karriere in der Softwareentwicklung geprägt hat.
        </p>

        <!-- Schnellstatistiken -->
        <div class="resume-stats">
          <div class="stat-card">
            <div class="stat-icon">
              <v-icon icon="mdi-briefcase" size="32" color="primary" />
            </div>
            <div class="stat-content">
              <div class="stat-number">2+</div>
              <div class="stat-label">Jahre Erfahrung</div>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">
              <v-icon icon="mdi-rocket" size="32" color="warning" />
            </div>
            <div class="stat-content">
              <div class="stat-number">5+</div>
              <div class="stat-label">Projekte</div>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">
              <v-icon icon="mdi-trending-up" size="32" color="info" />
            </div>
            <div class="stat-content">
              <div class="stat-number">Entwickler</div>
              <div class="stat-label">Level</div>
            </div>
          </div>
        </div>

        <!-- Lebenslauf herunterladen -->
        <div class="download-section">
          <v-btn 
            color="primary" 
            variant="flat" 
            size="large"
            class="download-btn"
            rounded="lg"
            @click="downloadResume"
          >
            <template v-slot:prepend>
              <v-icon icon="mdi-download" />
            </template>
            Lebenslauf herunterladen (PDF)
          </v-btn>
          <div class="download-note">
            <v-icon icon="mdi-information" size="16" class="mr-1" />
            Aktualisiert Dezember 2025
          </div>
        </div>
      </div>

      <!-- Hauptinhalt -->
      <section class="resume-content">
        <v-card class="resume-container" elevation="12" rounded="xl">
          <v-card-text class="resume-card-content">
            <!-- Lebenslauf-Kopf -->
            <div class="resume-header">
              <div class="header-main">
                <v-avatar size="80" class="profile-avatar">
                  <v-icon icon="mdi-account-circle" size="80" color="white" />
                </v-avatar>
                <div class="header-info">
                  <h2 class="resume-name">Jehad Qassem</h2>
                  <p class="resume-title"> Full-Stack Entwickler</p>
                  <div class="contact-info">
                    <div class="contact-item">
                      <v-icon icon="mdi-email" size="16" />
                      <span>qassemjehad@gmail.com</span>
                    </div>
                    <div class="contact-item">
                      <v-icon icon="mdi-map-marker" size="16" />
                      <span>Berlin, Deutschland</span>
                    </div>
                  </div>
                </div>
              </div>
              <div class="header-skills">
                <v-chip
                  v-for="skill in quickSkills"
                  :key="skill"
                  size="small"
                  variant="outlined"
                  class="skill-tag"
                >
                  {{ skill }}
                </v-chip>
              </div>
            </div>

            <v-divider class="my-6" />

            <!-- Zwei-Spalten-Layout -->
            <v-row>
              <!-- Linke Spalte - Berufserfahrung -->
              <v-col cols="12" lg="8" class="experience-column">
                <div class="section-title">
                  <v-icon icon="mdi-briefcase" size="24" class="mr-2" color="primary" />
                  <h3>Berufserfahrung</h3>
                </div>
                
                <!-- Timeline-Komponente -->
                <div class="timeline-section">
                  <Timeline />
                </div>

                <!-- Fähigkeiten-Fortschritt -->
                <div class="skills-progress">
                  <div class="section-title">
                    <v-icon icon="mdi-cog" size="24" class="mr-2" color="primary" />
                    <h3>Technische Fähigkeiten</h3>
                  </div>
                  
                  <div class="progress-grid">
                    <div class="progress-item">
                      <div class="skill-info">
                        <span class="skill-name">Vue.js (Vuetify-latest)</span>
                        <span class="skill-percent">95%</span>
                      </div>
                      <v-progress-linear model-value="95" color="success" height="8" rounded />
                    </div>
                    <div class="progress-item">
                      <div class="skill-info">
                        <span class="skill-name">TypeScript</span>
                        <span class="skill-percent">90%</span>
                      </div>
                      <v-progress-linear model-value="90" color="success" height="8" rounded />
                    </div>
                    <div class="progress-item">
                      <div class="skill-info">
                        <span class="skill-name">JavaScript (ES6+) & HTML5/CSS3</span>
                        <span class="skill-percent">85%</span>
                      </div>
                      <v-progress-linear model-value="85" color="primary" height="8" rounded />
                    </div>
                    <div class="progress-item">
                      <div class="skill-info">
                        <span class="skill-name">React & Angular</span>
                        <span class="skill-percent">70%</span>
                      </div>
                      <v-progress-linear model-value="70" color="info" height="8" rounded />
                    </div>
                    <div class="progress-item">
                      <div class="skill-info">
                        <span class="skill-name">Node.js</span>
                        <span class="skill-percent">80%</span>
                      </div>
                      <v-progress-linear model-value="80" color="warning" height="8" rounded />
                    </div>
                    <div class="progress-item">
                      <div class="skill-info">
                        <span class="skill-name">PostgreSQL</span>
                        <span class="skill-percent">65%</span>
                      </div>
                      <v-progress-linear model-value="65" color="info" height="8" rounded />
                    </div>
                  </div>
                </div>
              </v-col>

              <!-- Rechte Spalte - Seitenleiste -->
              <v-col cols="12" lg="4" class="sidebar-column">
                <!-- Fernstudium -->
                <v-card class="sidebar-card education-card" variant="outlined" rounded="lg">
                  <v-card-text class="sidebar-content">
                    <div class="sidebar-title">
                      <div class="title-icon-wrapper">
                        <v-icon icon="mdi-school" size="24" color="primary" />
                      </div>
                      <h4>Fernstudium</h4>
                    </div>
                    
                    <div class="education-item">
                      <div class="edu-header">
                        <v-icon icon="mdi-calendar-range" size="18" color="primary" class="mr-2" />
                        <div class="edu-period">2022 - 2023</div>
                      </div>
                      <div class="edu-degree">
                        <v-icon icon="mdi-certificate" size="18" color="success" class="mr-2" />
                        Web-App Developer
                      </div>
                      <div class="edu-school">
                        <v-icon icon="mdi-domain" size="18" class="mr-2" />
                        SGD (Studiengemeinschaft Darmstadt)
                      </div>
                      <v-divider class="my-3" style="opacity: 0.1;" />
                      <div class="edu-highlights">
                        <div class="highlight-item">
                          <v-icon icon="mdi-check-circle" size="16" color="success" />
                          <span>Schwerpunkt Softwareentwicklung</span>
                        </div>
                        <div class="highlight-item">
                          <v-icon icon="mdi-check-circle" size="16" color="success" />
                          <span>Full-Stack Zertifizierung</span>
                        </div>
                      </div>
                    </div>
                  </v-card-text>
                </v-card>

                <!-- Zertifizierungen -->
                <v-card class="sidebar-card certificates-card" variant="outlined" rounded="lg">
                  <v-card-text class="sidebar-content">
                    <div class="sidebar-title">
                      <div class="title-icon-wrapper">
                        <v-icon icon="mdi-certificate" size="24" color="warning" />
                      </div>
                      <h4>Zertifizierungen</h4>
                    </div>
                    
                    <!-- Abschlusszeugnis -->
                    <div class="cert-item">
                      <div class="cert-header">
                        <v-icon icon="mdi-seal" size="20" color="warning" />
                        <div class="cert-name">Abschlusszeugnis</div>
                      </div>
                      <div class="cert-date-badge">
                        <v-chip size="x-small" color="warning" variant="flat">
                          <v-icon icon="mdi-calendar" size="14" class="mr-1" />
                          2023
                        </v-chip>
                      </div>
                      <v-expansion-panels variant="accordion" class="cert-expansion">
                        <v-expansion-panel>
                          <v-expansion-panel-title class="cert-toggle">
                            <span>Inhalte ansehen</span>
                            <template v-slot:actions>
                              <v-icon icon="mdi-chevron-down" />
                            </template>
                          </v-expansion-panel-title>
                          <v-expansion-panel-text class="cert-content">
                            <div class="cert-topics">
                              <div class="cert-topic">
                                <v-icon icon="mdi-check" size="14" color="success" />
                                <span>Konzepte und Werkzeuge</span>
                              </div>
                              <div class="cert-topic">
                                <v-icon icon="mdi-check" size="14" color="success" />
                                <span>Responsive Webdesign-Websites</span>
                              </div>
                              <div class="cert-topic">
                                <v-icon icon="mdi-language-javascript" size="14" color="#f7df1e" />
                                <span>JavaScript</span>
                              </div>
                              <div class="cert-topic">
                                <v-icon icon="mdi-nodejs" size="14" color="#68a063" />
                                <span>Node.js</span>
                              </div>
                              <div class="cert-topic">
                                <v-icon icon="mdi-jquery" size="14" color="#0769ad" />
                                <span>jQuery und jQuery Mobile</span>
                              </div>
                              <div class="cert-topic">
                                <v-icon icon="mdi-angular" size="14" color="#dd0031" />
                                <span>Angular</span>
                              </div>
                              <div class="cert-topic">
                                <v-icon icon="mdi-vuejs" size="14" color="#41b883" />
                                <span>Vue.js</span>
                              </div>
                              <div class="cert-topic">
                                <v-icon icon="mdi-cordova" size="14" color="#4cc2e4" />
                                <span>Apache Cordova</span>
                              </div>
                              <div class="cert-topic">
                                <v-icon icon="mdi-check" size="14" color="success" />
                                <span>Komplexere Web-Anwendungen</span>
                              </div>
                              <div class="cert-topic">
                                <v-icon icon="mdi-react" size="14" color="#61dafb" />
                                <span>Single Page Apps mit React</span>
                              </div>
                              <div class="cert-topic">
                                <v-icon icon="mdi-check" size="14" color="success" />
                                <span>Progressive Web Apps (PWA)</span>
                              </div>
                            </div>
                          </v-expansion-panel-text>
                        </v-expansion-panel>
                      </v-expansion-panels>
                    </div>

                    <!-- Zertifikat -->
                    <div class="cert-item">
                      <div class="cert-header">
                        <v-icon icon="mdi-trophy" size="20" color="primary" />
                        <div class="cert-name">Zertifikat</div>
                      </div>
                      <div class="cert-date-badge">
                        <v-chip size="x-small" color="primary" variant="flat">
                          <v-icon icon="mdi-calendar" size="14" class="mr-1" />
                          2023
                        </v-chip>
                      </div>
                      <v-expansion-panels variant="accordion" class="cert-expansion">
                        <v-expansion-panel>
                          <v-expansion-panel-title class="cert-toggle">
                            <span>Inhalte ansehen</span>
                            <template v-slot:actions>
                              <v-icon icon="mdi-chevron-down" />
                            </template>
                          </v-expansion-panel-title>
                          <v-expansion-panel-text class="cert-content">
                            <div class="cert-topics">
                              <div class="cert-topic">
                                <v-icon icon="mdi-check" size="14" color="success" />
                                <span>Konzepte und Werkzeuge</span>
                              </div>
                              <div class="cert-topic">
                                <v-icon icon="mdi-check" size="14" color="success" />
                                <span>Responsive Webdesign-Websites</span>
                              </div>
                              <div class="cert-topic">
                                <v-icon icon="mdi-language-javascript" size="14" color="#f7df1e" />
                                <span>JavaScript</span>
                              </div>
                              <div class="cert-topic">
                                <v-icon icon="mdi-nodejs" size="14" color="#68a063" />
                                <span>Node.js</span>
                              </div>
                              <div class="cert-topic">
                                <v-icon icon="mdi-jquery" size="14" color="#0769ad" />
                                <span>jQuery und jQuery Mobile</span>
                              </div>
                              <div class="cert-topic">
                                <v-icon icon="mdi-angular" size="14" color="#dd0031" />
                                <span>Angular</span>
                              </div>
                              <div class="cert-topic">
                                <v-icon icon="mdi-vuejs" size="14" color="#41b883" />
                                <span>Vue.js</span>
                              </div>
                              <div class="cert-topic">
                                <v-icon icon="mdi-cordova" size="14" color="#4cc2e4" />
                                <span>Apache Cordova</span>
                              </div>
                              <div class="cert-topic">
                                <v-icon icon="mdi-check" size="14" color="success" />
                                <span>Komplexere Web-Anwendungen</span>
                              </div>
                              <div class="cert-topic">
                                <v-icon icon="mdi-react" size="14" color="#61dafb" />
                                <span>Single Page Apps mit React</span>
                              </div>
                              <div class="cert-topic">
                                <v-icon icon="mdi-check" size="14" color="success" />
                                <span>Progressive Web Apps (PWA)</span>
                              </div>
                            </div>
                          </v-expansion-panel-text>
                        </v-expansion-panel>
                      </v-expansion-panels>
                    </div>
                  </v-card-text>
                </v-card>

                <!-- Sprachen -->
                <v-card class="sidebar-card" variant="outlined" rounded="lg">
                  <v-card-text class="sidebar-content">
                    <div class="sidebar-title">
                      <v-icon icon="mdi-translate" size="20" class="mr-2" color="primary" />
                      <h4>Sprachen</h4>
                    </div>
                    
                    <div class="language-item">
                      <span class="lang-name">Kurdisch</span>
                      <span class="lang-level">Muttersprache</span>
                    </div>
                    <div class="language-item">
                      <span class="lang-name">Deutsch</span>
                      <span class="lang-level">Fließend</span>
                    </div>
                    <div class="language-item">
                      <span class="lang-name">Arabisch</span>
                      <span class="lang-level">Fließend</span>
                    </div>
                    <div class="language-item">
                      <span class="lang-name">Englisch</span>
                      <span class="lang-level">Grundkenntnisse</span>
                    </div>
                  </v-card-text>
                </v-card>

                <!-- Interessen -->
                <v-card class="sidebar-card" variant="outlined" rounded="lg">
                  <v-card-text class="sidebar-content">
                    <div class="sidebar-title">
                      <v-icon icon="mdi-heart" size="20" class="mr-2" color="primary" />
                      <h4>Interessen</h4>
                    </div>
                    
                    <div class="interests-grid">
                      <div class="interest-item">
                        <v-icon icon="mdi-code-braces" size="20" />
                        <span>Open Source</span>
                      </div>
                      <div class="interest-item">
                        <v-icon icon="mdi-book" size="20" />
                        <span>Lesen</span>
                      </div>
                      <div class="interest-item">
                        <v-icon icon="mdi-hiking" size="20" />
                        <span>Wandern</span>
                      </div>
                      <div class="interest-item">
                        <v-icon icon="mdi-music" size="20" />
                        <span>Musik</span>
                      </div>
                    </div>
                  </v-card-text>
                </v-card>
              </v-col>
            </v-row>
          </v-card-text>

          <!-- Lebenslauf-Dekoration -->
          <div class="resume-decoration">
            <div class="decoration-dot dot-1"></div>
            <div class="decoration-dot dot-2"></div>
            <div class="decoration-dot dot-3"></div>
          </div>
        </v-card>
      </section>

      <!-- Call-to-Action -->
      <section class="resume-cta">
        <v-card class="cta-card" elevation="8" rounded="xl">
          <v-card-text class="cta-content">
            <div class="cta-icon">
              <v-icon icon="mdi-email-fast" size="48" color="primary" />
            </div>
            
            <h3 class="cta-title">
              Bereit für die
              <span class="title-gradient">Zusammenarbeit?</span>
            </h3>

            <p class="cta-description">
              Lassen Sie uns besprechen, wie ich zu Ihrem Team beitragen und Mehrwert für Ihre Projekte schaffen kann. 
              Ich bin immer offen für neue Möglichkeiten und spannende Herausforderungen.
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
              
            </div>
          </v-card-text>

          <!-- CTA-Hintergrund -->
          <div class="cta-background">
            <div class="cta-dot dot-1"></div>
            <div class="cta-dot dot-2"></div>
            <div class="cta-dot dot-3"></div>
          </div>
        </v-card>
      </section>
    </v-container>
  </div>
</template>

<script setup lang="ts">
import Timeline from '@/components/Timeline.vue'

const quickSkills = [
  'Vue.js', 'React', 'TypeScript', 'Node.js', 
  'PostgreSQL', 'Express'
]

function downloadResume() {
  // Direkter Download der PDF-Datei
  const link = document.createElement('a')
  link.href = '/lebenslauf.pdf'
  link.download = 'Lebenslauf-Jehad-Qassem.pdf'
  link.click()
}
</script>

<style scoped lang="scss">
.resume-page {
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

.resume-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 24px;
  max-width: 800px;
  margin: 0 auto 40px;
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

.download-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.download-btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
  color: white !important;
  font-weight: 600;
  padding: 12px 32px;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
  }
}

.download-note {
  display: flex;
  align-items: center;
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.875rem;
}

.resume-content {
  margin-bottom: 80px;
}

.resume-container {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  backdrop-filter: blur(20px);
  position: relative;
  overflow: hidden;
}

.resume-card-content {
  padding: 48px !important;
  position: relative;
  z-index: 2;
}

.resume-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  flex-wrap: wrap;
  gap: 24px;
}

.header-main {
  display: flex;
  align-items: flex-start;
  gap: 24px;
  flex: 1;
}

.profile-avatar {
  border: 3px solid rgba(255, 255, 255, 0.1);
  background: rgba(255, 255, 255, 0.05);
}

.header-info {
  flex: 1;
}

.resume-name {
  font-size: 2rem;
  font-weight: 700;
  color: white;
  margin-bottom: 8px;
}

.resume-title {
  font-size: 1.25rem;
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 16px;
}

.contact-info {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 8px;
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.875rem;
}

.header-skills {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  max-width: 300px;
}

.skill-tag {
  backdrop-filter: blur(10px);
  background: rgba(255, 255, 255, 0.05) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  color: rgba(255, 255, 255, 0.8) !important;
  font-size: 0.75rem;
}

.section-title {
  display: flex;
  align-items: center;
  margin-bottom: 24px;

  h3 {
    font-size: 1.5rem;
    font-weight: 600;
    color: white;
    margin: 0;
  }
}

.timeline-section {
  margin-bottom: 40px;
}

.skills-progress {
  margin-bottom: 40px;
}

.progress-grid {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.progress-item {
  .skill-info {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
  }

  .skill-name {
    font-weight: 500;
    color: white;
  }

  .skill-percent {
    font-size: 0.875rem;
    color: rgba(255, 255, 255, 0.7);
  }
}

.sidebar-column {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.sidebar-card {
  background: rgba(255, 255, 255, 0.03) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  backdrop-filter: blur(10px);
}

.sidebar-content {
  padding: 24px !important;
  color: white;
}

.sidebar-title {
  display: flex;
  align-items: center;
  margin-bottom: 20px;

  h4 {
    font-size: 1.125rem;
    font-weight: 600;
    color: white;
    margin: 0;
  }
}

.education-card {
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.08) 0%, rgba(118, 75, 162, 0.05) 100%) !important;
  border: 1px solid rgba(102, 126, 234, 0.2) !important;
}

.title-icon-wrapper {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  background: rgba(102, 126, 234, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 12px;
}

.education-item {
  margin-bottom: 0;
  padding: 16px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.05);

  .edu-header {
    display: flex;
    align-items: center;
    margin-bottom: 12px;
  }

  .edu-period {
    font-size: 0.875rem;
    color: #667eea;
    font-weight: 600;
  }

  .edu-degree {
    display: flex;
    align-items: center;
    font-size: 1.125rem;
    font-weight: 600;
    color: white;
    margin-bottom: 8px;
  }

  .edu-school {
    display: flex;
    align-items: center;
    color: rgba(255, 255, 255, 0.8);
    margin-bottom: 12px;
    font-size: 0.9rem;
  }

  .edu-highlights {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .highlight-item {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 0.875rem;
    color: rgba(255, 255, 255, 0.8);
    padding: 6px 8px;
    border-radius: 6px;
    background: rgba(255, 255, 255, 0.02);
  }
}

.certificates-card {
  background: linear-gradient(135deg, rgba(255, 193, 7, 0.05) 0%, rgba(255, 152, 0, 0.03) 100%) !important;
  border: 1px solid rgba(255, 193, 7, 0.15) !important;
}

.cert-item {
  margin-bottom: 20px;
  padding: 16px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.05);
  transition: all 0.3s ease;

  &:last-child {
    margin-bottom: 0;
  }

  &:hover {
    background: rgba(255, 255, 255, 0.04);
    border-color: rgba(255, 255, 255, 0.1);
    transform: translateY(-2px);
  }

  .cert-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 8px;
  }

  .cert-name {
    font-size: 1.125rem;
    font-weight: 600;
    color: white;
  }

  .cert-date-badge {
    margin-bottom: 12px;
  }

  .cert-expansion {
    background: transparent !important;
    box-shadow: none !important;

    .v-expansion-panel {
      background: rgba(255, 255, 255, 0.02) !important;
      border: 1px solid rgba(255, 255, 255, 0.05) !important;
      border-radius: 8px !important;
      overflow: hidden;
    }

    .cert-toggle {
      font-size: 0.875rem;
      color: rgba(255, 255, 255, 0.8);
      padding: 8px 12px;
      min-height: 36px !important;
    }

    .cert-content {
      padding: 12px !important;
    }
  }

  .cert-topics {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .cert-topic {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 0.875rem;
    color: rgba(255, 255, 255, 0.8);
    padding: 6px 10px;
    border-radius: 6px;
    background: rgba(255, 255, 255, 0.02);
    transition: all 0.2s ease;

    &:hover {
      background: rgba(255, 255, 255, 0.05);
      transform: translateX(4px);
    }
  }
}

.language-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);

  &:last-child {
    border-bottom: none;
  }

  .lang-name {
    color: white;
  }

  .lang-level {
    font-size: 0.875rem;
    color: rgba(255, 255, 255, 0.7);
  }
}

.interests-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.interest-item {
  display: flex;
  align-items: center;
  gap: 8px;
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.875rem;
}

.resume-decoration {
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

.resume-cta {
  margin-bottom: 40px;
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
    transform: translateY(-15px);
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

  .resume-stats {
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
  }

  .stat-card {
    padding: 20px;
  }

  .resume-card-content {
    padding: 32px !important;
  }

  .resume-header {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .header-main {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .contact-info {
    justify-content: center;
  }

  .header-skills {
    justify-content: center;
    max-width: none;
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
  .page-title {
    font-size: 2rem;
  }

  .page-subtitle {
    font-size: 1.125rem;
  }

  .resume-stats {
    grid-template-columns: 1fr;
  }

  .resume-name {
    font-size: 1.5rem;
  }

  .resume-title {
    font-size: 1.125rem;
  }

  .contact-info {
    flex-direction: column;
    align-items: center;
    gap: 8px;
  }

  .section-title h3 {
    font-size: 1.25rem;
  }

  .interests-grid {
    grid-template-columns: 1fr;
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
  .resume-decoration,
  .cta-background,
  .stat-card {
    animation: none;
    transition: none;
  }

  .download-btn:hover,
  .cta-btn:hover {
    transform: none;
  }
}
</style>