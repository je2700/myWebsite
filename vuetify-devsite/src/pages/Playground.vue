<template>
  <div class="playground-page">
    <!-- Hintergrund-Elemente -->
    <div class="page-background">
      <div class="bg-gradient"></div>
      <div class="floating-elements">
        <div class="element element-1">
          <v-icon icon="mdi-api" size="40" />
        </div>
        <div class="element element-2">
          <v-icon icon="mdi-code-json" size="32" />
        </div>
        <div class="element element-3">
          <v-icon icon="mdi-console" size="36" />
        </div>
        <div class="element element-4">
          <v-icon icon="mdi-server" size="38" />
        </div>
      </div>
      <div class="grid-pattern"></div>
    </div>

    <v-container class="page-container">
      <!-- Kopfbereich -->
      <div class="page-header">
        <v-card class="header-badge" variant="outlined" rounded="pill">
          <v-card-text class="badge-content">
            <v-icon icon="mdi-rocket-launch" size="20" class="mr-2" color="primary" />
            <span class="text-caption font-weight-bold">API Playground</span>
          </v-card-text>
        </v-card>

        <h1 class="page-title">
          API
          <span class="title-gradient">Playground</span>
        </h1>

        <p class="page-subtitle">
          Testen und experimentieren Sie mit REST-APIs in Echtzeit. Bauen Sie Anfragen auf, 
          inspizieren Sie Antworten und lernen Sie, wie Sie mit Webdiensten über diese interaktive Konsole interagieren.
        </p>

        <!-- Schnellstatistiken -->
        <div class="feature-highlights">
          <div class="feature-item">
            <v-icon icon="mdi-lightning-bolt" size="24" color="success" class="feature-icon" />
            <div class="feature-content">
              <div class="feature-title">Echtzeit-Tests</div>
              <div class="feature-description">Sofortige API-Antworten</div>
            </div>
          </div>
          <div class="feature-item">
            <v-icon icon="mdi-shield-check" size="24" color="primary" class="feature-icon" />
            <div class="feature-content">
              <div class="feature-title">Sichere Umgebung</div>
              <div class="feature-description">Sicherer Testbereich</div>
            </div>
          </div>
          <div class="feature-item">
            <v-icon icon="mdi-code-braces" size="24" color="warning" class="feature-icon" />
            <div class="feature-content">
              <div class="feature-title">JSON-Formatierung</div>
              <div class="feature-description">Schöne Code-Formatierung</div>
            </div>
          </div>
        </div>
      </div>

      <!-- API-Konsolen-Bereich -->
      <section class="console-section">
        <v-card class="console-container" elevation="12" rounded="xl">
          <v-card-text class="console-content">
            <!-- Abschnittskopf -->
            <div class="console-header">
              <div class="header-left">
                <v-icon icon="mdi-console-line" size="28" color="primary" class="header-icon" />
                <div class="header-text">
                  <h2 class="console-title">Interaktive API-Konsole</h2>
                  <p class="console-description">
                    Bauen Sie HTTP-Anfragen, testen Sie Endpunkte und analysieren Sie Antworten in dieser leistungsstarken Spielwiese
                  </p>
                </div>
              </div>
              <div class="header-actions">
                <v-btn
                  variant="outlined"
                  size="small"
                  @click="showExamples = !showExamples"
                  class="examples-btn"
                  rounded="lg"
                >
                  <v-icon icon="mdi-book-open" class="mr-2" />
                  {{ showExamples ? 'Ausblenden' : 'Anzeigen' }} Beispiele
                </v-btn>
              </div>
            </div>

            <!-- API-Beispiele -->
            <v-expand-transition>
              <div v-if="showExamples" class="examples-panel">
                <div class="examples-header">
                  <h3 class="examples-title">Schnellstart-Beispiele</h3>
                  <p class="examples-subtitle">
                    Probieren Sie diese vorkonfigurierten API-Beispiele aus, um zu starten
                  </p>
                </div>
                <div class="examples-grid">
                  <v-card
                    v-for="example in apiExamples"
                    :key="example.id"
                    class="example-card"
                    variant="outlined"
                    rounded="lg"
                    @click="loadExample(example)"
                    hover
                  >
                    <v-card-text class="example-content">
                      <div class="example-icon">
                        <v-icon :icon="example.icon" size="24" :color="example.color" />
                      </div>
                      <div class="example-info">
                        <div class="example-title">{{ example.title }}</div>
                        <div class="example-description">{{ example.description }}</div>
                      </div>
                      <v-icon icon="mdi-arrow-right" size="20" class="example-arrow" />
                    </v-card-text>
                  </v-card>
                </div>
              </div>
            </v-expand-transition>

            <!-- Haupt-API-Konsole -->
            <div class="api-console-wrapper">
              <slot name="api-console">
                <!-- Default ApiConsole mit direkter Anbindung an die Beispiele -->
                <ApiConsole
                  ref="apiConsoleRef"
                  @error="forwardConsoleError"
                />
              </slot>
            </div>

            <!-- Funktionen-Raster -->
            <div class="features-grid">
              <v-card class="feature-card" variant="outlined" rounded="lg">
                <v-card-text class="feature-card-content">
                  <v-icon icon="mdi-tune" size="32" color="primary" class="feature-card-icon" />
                  <h4 class="feature-card-title">Flexible Konfiguration</h4>
                  <p class="feature-card-description">
                    Passen Sie Header, Methoden und Body-Inhalte mit einer intuitiven Oberfläche an
                  </p>
                </v-card-text>
              </v-card>

              <v-card class="feature-card" variant="outlined" rounded="lg">
                <v-card-text class="feature-card-content">
                  <v-icon icon="mdi-eye" size="32" color="success" class="feature-card-icon" />
                  <h4 class="feature-card-title">Antwort-Inspektion</h4>
                  <p class="feature-card-description">
                    Detaillierte Ansicht von Statuscodes, Headern und Antwortzeiten
                  </p>
                </v-card-text>
              </v-card>

              <v-card class="feature-card" variant="outlined" rounded="lg">
                <v-card-text class="feature-card-content">
                  <v-icon icon="mdi-history" size="32" color="warning" class="feature-card-icon" />
                  <h4 class="feature-card-title">Anfragen-Verlauf</h4>
                  <p class="feature-card-description">
                    Behalten Sie Ihre API-Aufrufe im Blick und führen Sie vorherige Anfragen einfach erneut aus
                  </p>
                </v-card-text>
              </v-card>
            </div>
          </v-card-text>

          <!-- Konsolen-Dekoration -->
          <div class="console-decoration">
            <div class="decoration-dot dot-1"></div>
            <div class="decoration-dot dot-2"></div>
            <div class="decoration-dot dot-3"></div>
          </div>
        </v-card>
      </section>

      <!-- Dokumentations-Bereich -->
      <section class="documentation-section">
        <v-row>
          <v-col cols="12" md="6" class="doc-content">
            <v-card class="doc-card" variant="outlined" rounded="xl">
              <v-card-text class="doc-content-inner">
                <div class="doc-badge">
                  <v-icon icon="mdi-book" size="20" class="mr-2" color="primary" />
                  <span class="text-caption font-weight-bold">Dokumentation</span>
                </div>

                <h3 class="doc-title">API-Best Practices</h3>

                <div class="doc-tips">
                  <div class="tip-item">
                    <v-icon icon="mdi-check-circle" size="20" color="success" class="mr-2" />
                    <span>Immer Request-Payloads validieren</span>
                  </div>
                  <div class="tip-item">
                    <v-icon icon="mdi-check-circle" size="20" color="success" class="mr-2" />
                    <span>Passende HTTP-Statuscodes verwenden</span>
                  </div>
                  <div class="tip-item">
                    <v-icon icon="mdi-check-circle" size="20" color="success" class="mr-2" />
                    <span>Richtige Fehlerbehandlung implementieren</span>
                  </div>
                  <div class="tip-item">
                    <v-icon icon="mdi-check-circle" size="20" color="success" class="mr-2" />
                    <span>Aussagekräftige Antwortnachrichten einbinden</span>
                  </div>
                </div>

                <v-btn 
                  color="primary" 
                  variant="outlined" 
                  href="https://developer.mozilla.org/en-US/docs/Web/HTTP"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="doc-cta"
                  rounded="lg"
                >
                  <v-icon icon="mdi-open-in-new" class="mr-2" />
                  HTTP-Dokumentation
                </v-btn>
              </v-card-text>
            </v-card>
          </v-col>

          <v-col cols="12" md="6" class="visual-content">
            <div class="code-visual">
              <div class="code-window">
                <div class="window-header">
                  <div class="window-dots">
                    <div class="dot red"></div>
                    <div class="dot yellow"></div>
                    <div class="dot green"></div>
                  </div>
                  <div class="window-title">api-request.js</div>
                </div>
                <div class="code-content">
                  <pre class="code-block"><code>{{ formattedExampleCode }}</code></pre>
                </div>
              </div>
            </div>
          </v-col>
        </v-row>
      </section>
    </v-container>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import ApiConsole from '@/components/ApiConsole.vue'

type HttpMethod = 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE'

interface ApiExampleConfig {
  method: HttpMethod | string
  url: string
  body?: unknown
  headers?: Record<string, string>
}

interface ApiExample {
  id: number
  title: string
  description: string
  icon: string
  color: string
  config: ApiExampleConfig
}

// Konfiguration, wie sie an die ApiConsole übergeben wird
interface ConsoleExampleConfig {
  method: HttpMethod
  baseUrl: string
  path: string
  body: string
  headers?: Record<string, string>
  queryParams?: { key: string; value: string }[]
  autoSend?: boolean
}

// Typ für die ApiConsole-Instanz (via ref)
type ApiConsoleInstance = {
  applyExampleConfig?: (config: ConsoleExampleConfig) => void
}

// Props für Konfiguration
interface Props {
  initialShowExamples?: boolean
  customExamples?: ApiExample[]
}

const props = withDefaults(defineProps<Props>(), {
  initialShowExamples: true,
  customExamples: () => []
})

// Emits für Event-Kommunikation
const emit = defineEmits<{
  loadExample: [example: ApiExample]
  error: [error: Error]
}>()

const showExamples = ref(props.initialShowExamples)
const apiConsoleRef = ref<ApiConsoleInstance | null>(null)

// Default-Beispiele
const defaultExamples: ApiExample[] = [
  {
    id: 1,
    title: 'GET Request',
    description: 'Daten von JSONPlaceholder abrufen',
    icon: 'mdi-download',
    color: 'primary',
    config: {
      method: 'GET',
      url: 'https://jsonplaceholder.typicode.com/posts/1',
      body: '',
      headers: {
        'Content-Type': 'application/json'
      }
    }
  },
  {
    id: 2,
    title: 'POST Request',
    description: 'Neuen Post erstellen',
    icon: 'mdi-plus',
    color: 'success',
    config: {
      method: 'POST',
      url: 'https://jsonplaceholder.typicode.com/posts',
      body: {
        title: 'Neuer Post',
        body: 'Dies ist ein neuer Post',
        userId: 1
      },
      headers: {
        'Content-Type': 'application/json'
      }
    }
  },
  {
    id: 3,
    title: 'PUT Request',
    description: 'Existierenden Post aktualisieren',
    icon: 'mdi-pencil',
    color: 'warning',
    config: {
      method: 'PUT',
      url: 'https://jsonplaceholder.typicode.com/posts/1',
      body: {
        id: 1,
        title: 'Aktualisierter Post',
        body: 'Dieser Post wurde aktualisiert',
        userId: 1
      },
      headers: {
        'Content-Type': 'application/json'
      }
    }
  },
  {
    id: 4,
    title: 'DELETE Request',
    description: 'Post löschen',
    icon: 'mdi-delete',
    color: 'error',
    config: {
      method: 'DELETE',
      url: 'https://jsonplaceholder.typicode.com/posts/1',
      body: '',
      headers: {
        'Content-Type': 'application/json'
      }
    }
  }
]

// Beispiele (Default + optionale Custom-Beispiele), normalisiert
const apiExamples = computed<ApiExample[]>(() => {
  const source = props.customExamples.length > 0 ? props.customExamples : defaultExamples
  const validMethods: HttpMethod[] = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

  return source.map((example, index) => {
    const rawMethod = (example.config?.method || 'GET').toString().toUpperCase()
    const method: HttpMethod = validMethods.includes(rawMethod as HttpMethod)
      ? (rawMethod as HttpMethod)
      : 'GET'

    let normalizedBody = ''
    if (typeof example.config?.body === 'string') {
      normalizedBody = example.config.body
    } else if (example.config?.body != null) {
      try {
        normalizedBody = JSON.stringify(example.config.body, null, 2)
      } catch {
        normalizedBody = String(example.config.body)
      }
    }

    return {
      id: example.id ?? index,
      title: example.title || `Beispiel ${index + 1}`,
      description: example.description || '',
      icon: example.icon || 'mdi-api',
      color: example.color || 'primary',
      config: {
        method,
        url: example.config?.url || '',
        body: normalizedBody,
        headers: example.config?.headers ?? {
          'Content-Type': 'application/json'
        }
      }
    }
  })
})

// Formatiertes Beispiel für die Dokumentation
const formattedExampleCode = computed(() => {
  return `// Beispiel API Request mit Fetch
fetch('https://jsonplaceholder.typicode.com/posts/1', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
})
.then(response => {
  console.log('Status:', response.status);
  console.log('Headers:', Object.fromEntries(response.headers.entries()));
  
  if (!response.ok) {
    throw new Error(\`HTTP Error: \${response.status}\`);
  }
  
  return response.json();
})
.then(data => {
  console.log('Antwort Daten:', data);
  console.log('✅ Request erfolgreich');
})
.catch(error => {
  console.error('❌ Fehler:', error.message);
});`
})

// URL aufteilen in baseUrl, path und queryParams für die ApiConsole
function splitUrlForConsole(rawUrl: string): {
  baseUrl: string
  path: string
  queryParams: { key: string; value: string }[]
} {
  const emptyResult = {
    baseUrl: '',
    path: '',
    queryParams: [] as { key: string; value: string }[]
  }

  if (!rawUrl) return emptyResult

  try {
    const urlObj = new URL(rawUrl)
    const baseUrl = `${urlObj.protocol}//${urlObj.host}`
    const path = urlObj.pathname || '/'
    const queryParams: { key: string; value: string }[] = []

    urlObj.searchParams.forEach((value, key) => {
      queryParams.push({ key, value })
    })

    return { baseUrl, path, queryParams }
  } catch {
    // Fallback für „krumme“ URLs, ohne die Typen zu verletzen
    const parts = rawUrl.split('?')
    const withoutQuery = parts[0] ?? ''
    const queryString = parts[1] ?? ''

    const queryParams: { key: string; value: string }[] = []

    if (queryString) {
      queryString.split('&').forEach((part) => {
        if (!part) return
        const [k, v = ''] = part.split('=')
        if (!k) return
        queryParams.push({
          key: decodeURIComponent(k),
          value: decodeURIComponent(v)
        })
      })
    }

    const match = withoutQuery.match(/^(https?:\/\/[^/]+)(\/.*)?$/)

    if (match) {
      const baseUrl = match[1] ?? ''
      const path = match[2] ?? '/'
      return {
        baseUrl,
        path,
        queryParams
      }
    }

    // Fallback, falls wirklich nur „irgendwas“ drin steht
    return {
      baseUrl: withoutQuery,
      path: '',
      queryParams
    }
  }
}


// Fehler aus der ApiConsole nach außen weiterreichen
function forwardConsoleError(error: unknown) {
  const err =
    error instanceof Error
      ? error
      : new Error(String(error ?? 'Unbekannter Fehler in ApiConsole'))
  emit('error', err)
}

function loadExample(example: ApiExample) {
  try {
    if (!example?.config?.url) {
      throw new Error('Ungültige Beispiel-Konfiguration: URL fehlt')
    }
    if (!example?.config?.method) {
      throw new Error('Ungültige Beispiel-Konfiguration: HTTP-Methode fehlt')
    }

    // URL in Teile für die ApiConsole zerlegen
    const { baseUrl, path, queryParams } = splitUrlForConsole(example.config.url)

    const consoleConfig: ConsoleExampleConfig = {
      method: example.config.method as HttpMethod,
      baseUrl,
      path,
      body: (example.config.body as string) ?? '',
      headers: example.config.headers,
      queryParams,
      autoSend: true
    }

    // Event an Parent-Komponente emittieren (für eigene Konsolen-Implementierungen)
    emit('loadExample', example)

    // Default-ApiConsole direkt konfigurieren, falls vorhanden & Methode exposed
    if (apiConsoleRef.value?.applyExampleConfig) {
      apiConsoleRef.value.applyExampleConfig(consoleConfig)
    }
  } catch (error) {
    const err =
      error instanceof Error
        ? error
        : new Error('Unbekannter Fehler beim Laden des Beispiels')
    console.error('Fehler beim Laden des Beispiels:', err)
    emit('error', err)
  }
}
</script>

<style scoped lang="scss">
.playground-page {
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
  background: linear-gradient(
    135deg,
    rgba(102, 126, 234, 0.05) 0%,
    rgba(118, 75, 162, 0.03) 50%,
    transparent 100%
  );
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
  will-change: transform;

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

.feature-highlights {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
  max-width: 800px;
  margin: 0 auto;
}

.feature-item {
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

.feature-icon {
  flex-shrink: 0;
}

.feature-content {
  flex: 1;
}

.feature-title {
  font-size: 1rem;
  font-weight: 600;
  color: white;
  margin-bottom: 4px;
}

.feature-description {
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.7);
}

.console-section {
  margin-bottom: 80px;
}

.console-container {
  background: linear-gradient(
    135deg,
    rgba(255, 255, 255, 0.05) 0%,
    rgba(255, 255, 255, 0.02) 100%
  ) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  backdrop-filter: blur(20px);
  position: relative;
  overflow: hidden;
}

.console-content {
  padding: 40px !important;
  position: relative;
  z-index: 2;
}

.console-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 32px;
  flex-wrap: wrap;
  gap: 16px;
}

.header-left {
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

.console-title {
  font-size: 1.75rem;
  font-weight: 700;
  color: white;
  margin-bottom: 8px;
}

.console-description {
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.5;
  max-width: 500px;
}

.examples-btn {
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: white !important;
  background: rgba(255, 255, 255, 0.05) !important;
  font-weight: 500;

  &:hover {
    background: rgba(255, 255, 255, 0.1) !important;
  }
}

.examples-panel {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  padding: 24px;
  margin-bottom: 32px;
}

.examples-header {
  margin-bottom: 24px;
}

.examples-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: white;
  margin-bottom: 8px;
}

.examples-subtitle {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.875rem;
}

.examples-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 16px;
}

.example-card {
  background: rgba(255, 255, 255, 0.05) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  cursor: pointer;
  transition: all 0.3s ease;

  &:hover {
    background: rgba(255, 255, 255, 0.08) !important;
    border-color: rgba(255, 255, 255, 0.2) !important;
    transform: translateY(-2px);
  }
}

.example-content {
  padding: 20px !important;
  display: flex;
  align-items: center;
  gap: 16px;
  color: white;
}

.example-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.example-info {
  flex: 1;
}

.example-title {
  font-weight: 600;
  margin-bottom: 4px;
}

.example-description {
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.7);
}

.example-arrow {
  color: rgba(255, 255, 255, 0.5);
  transition: transform 0.3s ease;
}

.example-card:hover .example-arrow {
  transform: translateX(4px);
  color: rgba(255, 255, 255, 0.8);
}

.api-console-wrapper {
  margin-bottom: 40px;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
}

.feature-card {
  background: rgba(255, 255, 255, 0.03) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  transition: all 0.3s ease;

  &:hover {
    background: rgba(255, 255, 255, 0.05) !important;
    border-color: rgba(255, 255, 255, 0.2) !important;
    transform: translateY(-4px);
  }
}

.feature-card-content {
  padding: 32px !important;
  text-align: center;
  color: white;
}

.feature-card-icon {
  margin-bottom: 16px;
}

.feature-card-title {
  font-size: 1.125rem;
  font-weight: 600;
  margin-bottom: 8px;
  color: white;
}

.feature-card-description {
  color: rgba(255, 255, 255, 0.7);
  line-height: 1.5;
}

.console-decoration {
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

.documentation-section {
  margin-bottom: 40px;
}

.doc-content {
  padding: 40px 0;
}

.doc-card {
  background: linear-gradient(
    135deg,
    rgba(255, 255, 255, 0.05) 0%,
    rgba(255, 255, 255, 0.02) 100%
  ) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  backdrop-filter: blur(20px);
  height: 100%;
}

.doc-content-inner {
  padding: 40px !important;
  color: white;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.doc-badge {
  display: inline-flex;
  align-items: center;
  padding: 8px 16px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  margin-bottom: 32px;
  color: white;
}

.doc-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 24px;
  color: white;
}

.doc-tips {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 32px;
  flex: 1;
}

.tip-item {
  display: flex;
  align-items: center;
  color: rgba(255, 255, 255, 0.9);
  font-weight: 500;
}

.doc-cta {
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: white !important;
  background: rgba(255, 255, 255, 0.05) !important;
  font-weight: 500;

  &:hover {
    background: rgba(255, 255, 255, 0.1) !important;
  }
}

.visual-content {
  padding: 40px 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.code-visual {
  width: 100%;
  max-width: 500px;
}

.code-window {
  background: #1a1f35;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
}

.window-header {
  background: #2d3748;
  padding: 16px 20px;
  display: flex;
  align-items: center;
  gap: 16px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.window-dots {
  display: flex;
  gap: 8px;
}

.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;

  &.red {
    background: #f56565;
  }
  &.yellow {
    background: #ecc94b;
  }
  &.green {
    background: #48bb78;
  }
}

.window-title {
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.875rem;
  font-weight: 500;
}

.code-content {
  padding: 24px;
}

.code-block {
  margin: 0;
  color: #e2e8f0;
  font-family: 'Courier New', monospace;
  font-size: 0.875rem;
  line-height: 1.5;
  overflow-x: auto;
  white-space: pre-wrap;
  word-wrap: break-word;
}

// Animations
@keyframes float {
  0%,
  100% {
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

  .feature-highlights {
    grid-template-columns: 1fr;
    gap: 16px;
  }

  .feature-item {
    padding: 16px;
  }

  .console-content {
    padding: 32px !important;
  }

  .console-header {
    flex-direction: column;
    align-items: stretch;
  }

  .header-left {
    flex-direction: column;
    text-align: center;
  }

  .header-icon {
    align-self: center;
  }

  .examples-grid {
    grid-template-columns: 1fr;
  }

  .features-grid {
    grid-template-columns: 1fr;
  }

  .doc-content-inner {
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

  .console-title {
    font-size: 1.5rem;
  }

  .feature-card-content {
    padding: 24px !important;
  }

  .code-content {
    padding: 16px;
  }

  .code-block {
    font-size: 0.75rem;
  }

  .floating-elements .element {
    width: 60px;
    height: 60px;

    .v-icon {
      font-size: 24px;
    }
  }
}

// Reduced motion und Performance
@media (prefers-reduced-motion: reduce) {
  .floating-elements,
  .console-decoration,
  .feature-item,
  .example-card,
  .feature-card {
    animation: none;
    transition: none;
  }

  .example-card:hover,
  .feature-card:hover {
    transform: none;
  }
}

@media (prefers-reduced-performance: reduce) {
  .console-container,
  .doc-card,
  .feature-item,
  .header-badge {
    backdrop-filter: none;
  }

  .floating-elements {
    display: none;
  }
}
</style>
