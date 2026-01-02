<template>
  <section class="contact-section" id="contact">
    <!-- Hintergrundelemente -->
    <div class="contact-background">
      <div class="bg-gradient"></div>
      <div class="floating-elements">
        <div class="element element-1">
          <v-icon icon="mdi-email-fast" size="40" />
        </div>
        <div class="element element-2">
          <v-icon icon="mdi-message-text" size="32" />
        </div>
        <div class="element element-3">
          <v-icon icon="mdi-chat-processing" size="36" />
        </div>
      </div>
      <div class="grid-overlay"></div>
    </div>

    <v-container class="contact-container">
      <v-row align="center" justify="center">
        <v-col cols="12" lg="10">
          <!-- Kopfbereich -->
          <div class="contact-header">
            <v-card class="contact-badge" variant="outlined" rounded="pill">
              <v-card-text class="badge-content">
                <v-icon icon="mdi-email" size="20" class="mr-2" color="primary" />
                <span class="text-caption font-weight-bold">Kontakt aufnehmen</span>
              </v-card-text>
            </v-card>

            <h2 class="contact-title">
              Lassen Sie uns etwas
              <span class="title-gradient">Großartiges</span>
              gemeinsam erschaffen
            </h2>

            <p class="contact-subtitle">
              Ich freue mich immer, neue Projekte, innovative Ideen oder mögliche Kooperationen zu besprechen.
              Ob Sie ein konkretes Projekt im Kopf haben oder einfach nur Hallo sagen möchten – ich freue mich von Ihnen zu hören.
            </p>

            <!-- Kontakt-Statistiken -->
            <div class="contact-stats">
              <div class="stat-card">
                <v-icon icon="mdi-clock-fast" size="32" color="primary" class="stat-icon" />
                <div class="stat-content">
                  <div class="stat-number">24/7</div>
                  <div class="stat-label">Ø Antwortzeit</div>
                </div>
              </div>
              <div class="stat-card">
                <v-icon icon="mdi-check-all" size="32" color="success" class="stat-icon" />
                <div class="stat-content">
                  <div class="stat-number">100%</div>
                  <div class="stat-label">Erfolgsquote</div>
                </div>
              </div>
              <div class="stat-card">
                <v-icon icon="mdi-account-multiple" size="32" color="warning" class="stat-icon" />
                <div class="stat-content">
                  <div class="stat-number">50+</div>
                  <div class="stat-label">Zufriedene Kunden</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Inhaltsbereich -->
          <v-row class="contact-content">
            <!-- Kontaktinformationen -->
            <v-col cols="12" md="5" class="contact-info">
              <v-card class="info-card" elevation="8" rounded="xl">
                <v-card-text class="info-content">
                  <h3 class="info-title">Lassen Sie uns ins Gespräch kommen</h3>
                  <p class="info-description">
                    Melden Sie sich gerne über meine E-Mail-Adresse. Ich bin jederzeit erreichbar,
                    um mögliche Kooperationen zu besprechen oder Ihre Fragen zu beantworten.
                  </p>

                  <!-- Kontaktmethoden -->
                  <div class="contact-methods">
                    <div class="contact-method">
                      <div class="method-icon">
                        <v-icon icon="mdi-email" size="24" color="primary" />
                      </div>
                      <div class="method-info">
                        <div class="method-label">E-Mail</div>

                        <!-- ✅ überall Outlook + ✨ genial: Copy-to-Clipboard + Tooltip -->
                        <div class="method-actions">
                          <a
                            :href="mailtoHref"
                            class="method-value"
                            :title="`E-Mail an ${CONTACT_EMAIL} schreiben`"
                          >
                            {{ CONTACT_EMAIL }}
                          </a>

                          <v-tooltip text="Kopieren" location="top">
                            <template #activator="{ props }">
                              <v-btn
                                v-bind="props"
                                icon
                                variant="text"
                                size="small"
                                class="copy-btn"
                                @click="copyEmail"
                                :aria-label="`E-Mail-Adresse ${CONTACT_EMAIL} kopieren`"
                              >
                                <v-icon :icon="copied ? 'mdi-check' : 'mdi-content-copy'" />
                              </v-btn>
                            </template>
                          </v-tooltip>
                        </div>

                        <div class="method-hint">
                          <v-icon icon="mdi-lightning-bolt-outline" size="16" class="mr-1" />
                          <span>{{ copied ? 'Kopiert! Jetzt einfach einfügen 🙌' : '1 Klick kopieren • 1 Klick mailen' }}</span>
                        </div>
                      </div>
                    </div>

                    <div class="contact-method">
                      <div class="method-icon">
                        <v-icon icon="mdi-map-marker" size="24" color="primary" />
                      </div>
                      <div class="method-info">
                        <div class="method-label">Standort</div>
                        <div class="method-value">Berlin, Deutschland</div>
                      </div>
                    </div>

                    <div class="contact-method">
                      <div class="method-icon">
                        <v-icon icon="mdi-clock" size="24" color="primary" />
                      </div>
                      <div class="method-info">
                        <div class="method-label">Verfügbarkeit</div>
                        <div class="method-value">Mo - Fr, 9:00 - 18:00 Uhr</div>
                      </div>
                    </div>
                  </div>

                  <!-- Social Links -->
                  <div class="social-section">
                    <div class="social-title">Folge mir</div>
                    <div class="social-links">
                      <v-btn
                        v-for="social in socialLinks"
                        :key="social.name"
                        :icon="social.icon"
                        variant="text"
                        :href="social.url"
                        target="_blank"
                        class="social-btn"
                        size="small"
                      >
                        <v-icon :icon="social.icon" size="24" />
                      </v-btn>
                    </div>
                  </div>
                </v-card-text>
              </v-card>
            </v-col>

            <!-- Kontaktformular -->
            <v-col cols="12" md="7" class="contact-form-col">
              <v-card class="form-container" elevation="12" rounded="xl">
                <v-card-text class="form-content">
                  <!-- ✨ genial: Empfänger wird als Prop weitergegeben (optional) -->
                  <ContactForm :to-email="CONTACT_EMAIL" />
                </v-card-text>

                <!-- Form-Dekoration -->
                <div class="form-decoration">
                  <div class="decoration-dot dot-1"></div>
                  <div class="decoration-dot dot-2"></div>
                  <div class="decoration-dot dot-3"></div>
                </div>
              </v-card>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>

    <!-- Snack für Copy-Feedback -->
    <v-snackbar
      v-model="copySnack"
      color="success"
      :timeout="2500"
      location="bottom"
      rounded="pill"
      elevation="12"
    >
      <v-icon icon="mdi-check-circle-outline" class="mr-2" />
      E-Mail kopiert: {{ CONTACT_EMAIL }}
    </v-snackbar>
  </section>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import ContactForm from '@/components/ContactForm.vue'

/**
 * ✅ Einmal definieren, überall nutzen
 * (So vermeidest du, dass irgendwo noch gmail “hängen bleibt”.)
 */
const CONTACT_EMAIL = 'qassemjehad@outlook.de'

const socialLinks = [
  {
    name: 'GitHub',
    icon: 'mdi-github',
    url: 'https://github.com/je2700'
  }
]

/**
 * Mailto-Link (sauber encoded + mit Betreff)
 */
const mailtoHref = computed(() => {
  const subject = 'Kontaktanfrage über die Website'
  return `mailto:${encodeURIComponent(CONTACT_EMAIL)}?subject=${encodeURIComponent(subject)}`
})

/**
 * ✨ Genial: Copy to clipboard mit Feedback
 */
const copied = ref(false)
const copySnack = ref(false)

async function copyEmail() {
  try {
    await navigator.clipboard.writeText(CONTACT_EMAIL)
    copied.value = true
    copySnack.value = true
    window.setTimeout(() => (copied.value = false), 1800)
  } catch {
    // Fallback für ältere Browser
    const ta = document.createElement('textarea')
    ta.value = CONTACT_EMAIL
    ta.setAttribute('readonly', 'true')
    ta.style.position = 'absolute'
    ta.style.left = '-9999px'
    document.body.appendChild(ta)
    ta.select()
    document.execCommand('copy')
    document.body.removeChild(ta)

    copied.value = true
    copySnack.value = true
    window.setTimeout(() => (copied.value = false), 1800)
  }
}
</script>


<style scoped lang="scss">
.contact-section {
  position: relative;
  padding: 120px 0;
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
  overflow: hidden;
}

.contact-background {
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
}

.grid-overlay {
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

.contact-container {
  position: relative;
  z-index: 2;
}

.contact-header {
  text-align: center;
  margin-bottom: 80px;
}

.contact-badge {
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

.contact-title {
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

.contact-subtitle {
  font-size: 1.25rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.8);
  max-width: 600px;
  margin: 0 auto 60px;
}

.contact-stats {
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
  flex-shrink: 0;
}

.stat-content {
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

.contact-content {
  align-items: stretch;
}

.contact-info {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.info-card {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  backdrop-filter: blur(20px);
}

.info-content {
  padding: 40px !important;
  color: white;
}

.info-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 12px;
  color: white;
}

.info-description {
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.6;
  margin-bottom: 32px;
}

.contact-methods {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 40px;
}

.contact-method {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 16px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: all 0.3s ease;

  &:hover {
    background: rgba(255, 255, 255, 0.08);
    border-color: rgba(255, 255, 255, 0.2);
    transform: translateX(4px);
  }
}

.method-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: rgba(102, 126, 234, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.method-info {
  flex: 1;
}

.method-label {
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: 4px;
}

.method-value {
  font-size: 1rem;
  font-weight: 600;
  color: white;
  text-decoration: none;
  transition: color 0.3s ease;

  &:hover {
    color: #667eea;
  }
}

.social-section {
  text-align: center;
}

.social-title {
  font-size: 1rem;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 16px;
}

.social-links {
  display: flex;
  justify-content: center;
  gap: 8px;
}

.social-btn {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.05) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  color: rgba(255, 255, 255, 0.7) !important;
  transition: all 0.3s ease;

  &:hover {
    background: rgba(255, 255, 255, 0.1) !important;
    border-color: rgba(255, 255, 255, 0.2) !important;
    color: white !important;
    transform: translateY(-2px);
  }
}

.contact-form-col {
  display: flex;
}

.form-container {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  backdrop-filter: blur(20px);
  position: relative;
  overflow: hidden;
  flex: 1;
}

.form-content {
  padding: 40px !important;
  position: relative;
  z-index: 2;
}

.form-decoration {
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
  .contact-section {
    padding: 80px 0;
  }

  .contact-stats {
    grid-template-columns: 1fr;
    gap: 16px;
  }

  .stat-card {
    padding: 20px;
  }

  .info-content,
  .form-content {
    padding: 32px !important;
  }

  .contact-method {
    padding: 12px;
  }
}

@media (max-width: 600px) {
  .contact-header {
    margin-bottom: 60px;
  }

  .contact-title {
    font-size: 2rem;
  }

  .contact-subtitle {
    font-size: 1.125rem;
  }

  .contact-stats {
    gap: 12px;
  }

  .stat-card {
    flex-direction: column;
    text-align: center;
    gap: 12px;
  }

  .info-content,
  .form-content {
    padding: 24px !important;
  }

  .contact-methods {
    gap: 16px;
  }

  .contact-method {
    flex-direction: column;
    text-align: center;
    gap: 12px;
  }

  .method-icon {
    width: 40px;
    height: 40px;
  }

  .floating-elements .element {
    width: 60px;
    height: 60px;

    .v-icon {
      font-size: 24px;
    }
  }
}

.method-actions {
  display: flex;
  align-items: center;
  gap: 6px;
}

.copy-btn {
  transform: translateY(-1px);
}

.method-hint {
  margin-top: 6px;
  display: flex;
  align-items: center;
  opacity: 0.85;
  font-size: 0.85rem;
}

// Reduced motion support
@media (prefers-reduced-motion: reduce) {
  .floating-elements,
  .form-decoration,
  .stat-card,
  .contact-method {
    animation: none;
    transition: none;
  }
}
</style>