<template>
  <v-container class="container">
    <v-card class="main-card" elevation="4" rounded="xl">
      <!-- Header mit Titel und Status -->
      <v-card-title class="card-header">
        <div class="d-flex align-center justify-space-between w-100">
          <div class="d-flex align-center">
            <v-icon icon="mdi-api" color="primary" size="32" class="mr-3" />
            <div>
              <div class="text-h5 font-weight-bold">API-Client</div>
              <div class="text-caption text-white">
                Testen Sie Ihre REST-Endpunkte
              </div>
            </div>
          </div>
          <v-chip
            :color="statusColor"
            variant="flat"
            size="small"
            class="status-chip"
          >
            <v-icon :icon="statusIcon" class="mr-1" size="16" />
            {{ statusText }}
          </v-chip>
        </div>
      </v-card-title>

      <v-divider class="mx-4" />

      <!-- Anfrage-Konfiguration -->
      <v-card-text class="request-section">
        <!-- URL-Zeile -->
        <div class="url-row mb-6">
          <v-select
            v-model="method"
            :items="methods"
            density="comfortable"
            variant="outlined"
            class="method-select"
            :color="methodColor"
            hide-details
          >
            <template v-slot:selection="{ item }">
              <v-chip
                :color="methodColor"
                variant="flat"
                size="small"
                class="font-weight-bold"
              >
                {{ item.title }}
              </v-chip>
            </template>
          </v-select>

          <v-text-field
            v-model="baseUrl"
            density="comfortable"
            variant="outlined"
            placeholder="http://localhost:3000"
            hide-details
            class="base-url-field"
          />

          <v-text-field
            v-model="path"
            density="comfortable"
            variant="outlined"
            placeholder="/api/health"
            hide-details
            class="path-field"
          />
        </div>

        <!-- Query-Parameter (vor allem für GET/DELETE nützlich) -->
        <div v-if="method === 'GET' || method === 'DELETE'" class="mt-4">
          <div class="d-flex align-center justify-space-between mb-2">
            <span class="text-subtitle-2 font-weight-medium">
              Query-Parameter
            </span>
            <v-btn
              size="x-small"
              variant="text"
              prepend-icon="mdi-plus"
              @click="addQueryParam"
            >
              Hinzufügen
            </v-btn>
          </div>

          <div
            class="query-row"
            v-for="(p, i) in queryParams"
            :key="i"
          >
            <v-text-field
              v-model="p.key"
              density="comfortable"
              variant="outlined"
              placeholder="key"
              hide-details
            />
            <v-text-field
              v-model="p.value"
              density="comfortable"
              variant="outlined"
              placeholder="value"
              hide-details
            />
            <v-btn
              icon="mdi-close"
              size="small"
              variant="text"
              @click="removeQueryParam(i)"
            />
          </div>

          <div class="mt-2 text-caption text-grey-darken-1">
            Effektive URL:
            <code>{{ finalUrl }}</code>
          </div>
        </div>

        <!-- Body-Editor -->
        <v-card
          v-if="showBody"
          variant="outlined"
          class="body-editor-card mb-4"
        >
          <v-card-title class="body-header py-2">
            <span class="text-subtitle-2 font-weight-medium">
              Anfrage-Body
            </span>
            <v-spacer />
            <v-btn
              size="small"
              variant="text"
              @click="prettyPrint"
              prepend-icon="mdi-code-json"
              class="text-caption"
            >
              Formatieren
            </v-btn>
          </v-card-title>
          <v-card-text class="pa-0">
            <v-textarea
              v-model="body"
              variant="plain"
              rows="8"
              placeholder='{"key": "value"}'
              class="body-textarea"
              hide-details
              auto-grow
            />
          </v-card-text>
        </v-card>

        <!-- Aktionen -->
        <div class="action-buttons">
          <v-btn
            color="primary"
            @click="send"
            prepend-icon="mdi-send"
            size="large"
            :loading="loading"
            class="send-btn"
          >
            Anfrage senden
          </v-btn>
          <v-btn
            variant="outlined"
            @click="clearAll"
            prepend-icon="mdi-broom"
            size="large"
          >
            Leeren
          </v-btn>
        </div>
      </v-card-text>

      <!-- Antwort-Bereich -->
      <v-divider />

      <v-card-text class="response-section">
        <div class="d-flex align-center justify-space-between mb-3">
          <div class="text-subtitle-1 font-weight-bold">Antwort</div>
          <div class="d-flex ga-2">
            <v-btn
              size="small"
              variant="text"
              @click="copyResponse"
              prepend-icon="mdi-content-copy"
            >
              Kopieren
            </v-btn>
            <v-btn
              size="small"
              variant="text"
              @click="toggleTheme"
              :prepend-icon="themeIcon"
            >
              Design
            </v-btn>
          </div>
        </div>

        <v-card
          variant="outlined"
          class="response-card"
          :class="{ 'error-card': hasError }"
        >
          <!-- Meta-Informationen zur Antwort -->
          <div v-if="responseMeta" class="response-meta">
            <v-chip
              size="small"
              :color="hasError ? 'error' : 'success'"
              variant="flat"
            >
              {{ responseMeta.status }} {{ responseMeta.statusText }}
            </v-chip>
            <v-chip
              v-if="responseMeta.responseTime"
              size="small"
              variant="outlined"
            >
              {{ responseMeta.responseTime }}
            </v-chip>
            <v-chip
              v-if="responseMeta.headers?.['content-type']"
              size="small"
              variant="outlined"
            >
              {{ responseMeta.headers['content-type'] }}
            </v-chip>
          </div>

          <div class="response-content">
            <pre :class="['response-pre', theme]">{{ displayBody }}</pre>
          </div>
        </v-card>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'

type HttpMethod = 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE'

interface ApiResponse {
  status: number
  statusText: string
  ok: boolean
  responseTime: string
  headers: Record<string, string>
  data: any
}

interface QueryParam {
  key: string
  value: string
}

const baseUrl = ref('http://localhost:3000')

const methods = [
  { title: 'GET', value: 'GET', color: 'success' },
  { title: 'POST', value: 'POST', color: 'primary' },
  { title: 'PUT', value: 'PUT', color: 'warning' },
  { title: 'PATCH', value: 'PATCH', color: 'info' },
  { title: 'DELETE', value: 'DELETE', color: 'error' }
] as const

const method = ref<HttpMethod>('GET')
const path = ref('/api/health')
const body = ref('')

const initialResult =
  '// No request sent yet\n// Click "Send Request" to test your API'
const result = ref<string>(initialResult)

const loading = ref(false)
const theme = ref<'dark' | 'light'>('dark')

// Query-Parameter
const queryParams = ref<QueryParam[]>([{ key: '', value: '' }])

function addQueryParam() {
  queryParams.value.push({ key: '', value: '' })
}

function removeQueryParam(index: number) {
  if (queryParams.value.length === 1) {
    // Immer mindestens eine Zeile behalten
    queryParams.value[0] = { key: '', value: '' }
    return
  }
  queryParams.value.splice(index, 1)
}

const finalUrl = computed(() => {
  try {
    const url = new URL(path.value || '/', baseUrl.value)
    queryParams.value
      .filter((p) => p.key.trim() !== '')
      .forEach((p) => url.searchParams.append(p.key.trim(), p.value))
    return url.toString()
  } catch {
    // Fallback: naive Zusammenfügung
    const base = (baseUrl.value || '').replace(/\/$/, '')
    const p = path.value || ''
    const queryString = queryParams.value
      .filter((q) => q.key.trim() !== '')
      .map(
        (q) =>
          `${encodeURIComponent(q.key.trim())}=${encodeURIComponent(q.value)}`
      )
      .join('&')
    return base + p + (queryString ? `?${queryString}` : '')
  }
})

// Sichtbarkeit Body-Editor
const showBody = computed(
  () => method.value !== 'GET' && method.value !== 'DELETE'
)

// Methoden-Farbgebung
const methodColor = computed(
  () => methods.find((m) => m.value === method.value)?.color || 'primary'
)

// Status-Handling
const lastOk = ref<boolean | null>(null)

const hasError = computed(() => lastOk.value === false)

const statusText = computed(() =>
  loading.value ? 'Lädt...' : hasError.value ? 'Fehler' : 'Bereit'
)
const statusIcon = computed(() =>
  loading.value
    ? 'mdi-loading'
    : hasError.value
      ? 'mdi-alert-circle'
      : 'mdi-check-circle'
)
const statusColor = computed(() =>
  loading.value ? 'warning' : hasError.value ? 'error' : 'success'
)

// Theme
const themeIcon = computed(() =>
  theme.value === 'dark' ? 'mdi-weather-sunny' : 'mdi-weather-night'
)

function toggleTheme() {
  theme.value = theme.value === 'dark' ? 'light' : 'dark'
  try {
    localStorage.setItem('api-client-theme', theme.value)
  } catch {
    // ignore
  }
}

// Antwort-Meta aus dem JSON im result extrahieren
const responseMeta = computed<ApiResponse | null>(() => {
  try {
    const parsed = JSON.parse(result.value) as ApiResponse
    if (
      parsed &&
      typeof parsed === 'object' &&
      'status' in parsed &&
      'responseTime' in parsed
    ) {
      return parsed
    }
    return null
  } catch {
    return null
  }
})

// Anzeige-Body: nur der eigentliche Body, nicht die Meta-Daten
const displayBody = computed(() => {
  const meta = responseMeta.value
  if (meta) {
    const data = meta.data
    if (data == null) {
      return '// No body returned'
    }
    if (typeof data === 'string') {
      return data
    }
    try {
      return JSON.stringify(data, null, 2)
    } catch {
      return String(data)
    }
  }

  return result.value
})

function copyResponse() {
  const meta = responseMeta.value
  const textToCopy = meta
    ? JSON.stringify(meta, null, 2)
    : result.value

  navigator.clipboard.writeText(textToCopy).catch(() => {
    // optional: Fehlerhandling bei fehlender Clipboard-API
  })
}

function clearAll() {
  body.value = ''
  path.value = ''
  queryParams.value = [{ key: '', value: '' }]
  result.value = initialResult
  lastOk.value = null
}

function prettyPrint() {
  if (!body.value.trim()) return
  try {
    const parsed = JSON.parse(body.value)
    body.value = JSON.stringify(parsed, null, 2)
  } catch {
    // ignore invalid JSON
  }
}

async function send(): Promise<void> {
  loading.value = true

  try {
    const url = new URL(path.value || '/', baseUrl.value)

    // Query-Parameter anhängen
    queryParams.value
      .filter((p) => p.key.trim() !== '')
      .forEach((p) => url.searchParams.append(p.key.trim(), p.value))

    const headers: Record<string, string> = {}
    const opts: RequestInit = {
      method: method.value,
      headers
    }

    // Body nur wenn sinnvoll
    if (method.value !== 'GET' && method.value !== 'DELETE' && body.value) {
      try {
        const parsed = JSON.parse(body.value)
        opts.body = JSON.stringify(parsed)
        headers['Content-Type'] = 'application/json'
      } catch {
        opts.body = body.value
        headers['Content-Type'] = 'text/plain'
      }
    }

    const startTime = Date.now()
    const r = await fetch(url.toString(), opts)
    const responseTime = Date.now() - startTime

    const text = await r.text()
    let json: any = null

    try {
      const contentType = r.headers.get('content-type') || ''
      if (text && contentType.includes('application/json')) {
        json = JSON.parse(text)
      }
    } catch {
      json = null
    }

    const res: ApiResponse = {
      status: r.status,
      statusText: r.statusText,
      ok: r.ok,
      responseTime: `${responseTime}ms`,
      headers: Object.fromEntries(r.headers.entries()),
      data: json ?? (text || null)
    }

    lastOk.value = r.ok
    result.value = JSON.stringify(res, null, 2)
  } catch (e: any) {
    lastOk.value = false
    result.value = `// Error: ${e?.message ?? String(e)}`
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  // Theme aus localStorage laden
  try {
    const savedTheme = localStorage.getItem('api-client-theme')
    if (savedTheme === 'dark' || savedTheme === 'light') {
      theme.value = savedTheme
    }
  } catch {
    // ignore
  }
})
</script>

<style scoped>
.container {
  max-width: 1200px;
  padding: 20px;
}

.main-card {
  background: linear-gradient(145deg, #ffffff 0%, #f8fafc 100%);
  border: 1px solid #e2e8f0;
}

.card-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 20px 24px;
}

.status-chip {
  background: rgba(255, 255, 255, 0.2) !important;
  backdrop-filter: blur(10px);
  color: white;
}

.request-section {
  padding: 24px;
}

.url-row {
  display: grid;
  grid-template-columns: 120px 1fr 2fr;
  gap: 12px;
  align-items: start;
}

@media (max-width: 768px) {
  .url-row {
    grid-template-columns: 1fr;
  }
}

.method-select {
  min-width: 120px;
}

.body-editor-card {
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  overflow: hidden;
}

.body-header {
  background: #f8fafc;
  border-bottom: 1px solid #e2e8f0;
}

.body-textarea {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, 'Roboto Mono',
    'Courier New', monospace;
  font-size: 14px;
  line-height: 1.5;
  padding: 16px;
}

.body-textarea :deep(textarea) {
  padding-top: 17px;
}

.action-buttons {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.send-btn {
  min-width: 160px;
}

/* Query-Parameter */
.query-row {
  display: grid;
  grid-template-columns: 1fr 1fr auto;
  gap: 8px;
  align-items: center;
  margin-bottom: 6px;
}

.response-section {
  padding: 24px;
}

.response-card {
  border-radius: 12px;
  overflow: hidden;
  transition: all 0.3s ease;
}

.response-card.error-card {
  border-color: #feb2b2;
  background: #fff5f5;
}

.response-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding: 12px 16px 0;
}

.response-content {
  max-height: 400px;
  overflow: auto;
}

.response-pre {
  margin: 0;
  padding: 20px;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, 'Roboto Mono',
    'Courier New', monospace;
  font-size: 13px;
  line-height: 1.5;
  border-radius: 8px;
}

.response-pre.dark {
  background: #1a202c;
  color: #e2e8f0;
}

.response-pre.light {
  background: #f7fafc;
  color: #2d3748;
  border: 1px solid #e2e8f0;
}

/* Custom scrollbar */
.response-content::-webkit-scrollbar {
  width: 8px;
}

.response-content::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 4px;
}

.response-content::-webkit-scrollbar-thumb {
  background: #c1c1c1;
  border-radius: 4px;
}

.response-content::-webkit-scrollbar-thumb:hover {
  background: #a8a8a8;
}

/* Loading animation */
.v-btn--loading .v-icon {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

/* Hover effects */
.v-card {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.v-card:hover {
  transform: translateY(-2px);
}
</style>
