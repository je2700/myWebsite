<template>
  <v-container class="repos-container">
    <!-- Kopfbereich -->
    <div class="header-section">
      <div class="header-content">
        <v-icon icon="mdi-github" size="48" class="header-icon" />
        <div class="header-text">
          <h1 class="text-h3 font-weight-bold">Meine Projekte</h1>
          <p class="text-subtitle-1 text-white">
            Eine Sammlung meiner Open-Source-Arbeiten und Beiträge
          </p>
        </div>
      </div>
      <div class="header-stats">
        <v-chip variant="outlined" class="stat-chip">
          <v-icon icon="mdi-source-repository" class="mr-2" />
          {{ repos.length }} Repositories
        </v-chip>
        <v-chip variant="outlined" class="stat-chip">
          <v-icon icon="mdi-star" class="mr-2" />
          {{ totalStars }} Sterne
        </v-chip>
      </div>
    </div>

    <!-- Such- & Filterbereich -->
    <v-card class="filters-card" elevation="4" rounded="xl">
      <v-card-text class="filters-content">
        <div class="filters-grid">
          <!-- Suchfeld -->
          <div class="search-field">
            <v-text-field
              v-model="q"
              density="comfortable"
              variant="outlined"
              prepend-inner-icon="mdi-magnify"
              label="Repositories durchsuchen..."
              placeholder="Suche nach Name oder Beschreibung"
              hide-details
              class="custom-search"
              clearable
            />
          </div>

          <!-- Sprachfilter -->
          <div class="filter-field">
            <v-select
              v-model="lang"
              :items="languages"
              density="comfortable"
              label="Sprache"
              variant="outlined"
              prepend-inner-icon="mdi-language"
              clearable
              hide-details
              class="custom-select"
            >
              <template v-slot:item="{ item }">
                <v-list-item>
                  <template v-slot:prepend>
                    <div 
                      class="language-dot" 
                      :style="{ backgroundColor: getLanguageColor(item.value) }"
                    ></div>
                  </template>
                  <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item>
              </template>
            </v-select>
          </div>

          <!-- Sortierfilter -->
          <div class="filter-field">
            <v-select
              v-model="sort"
              :items="sortOptions"
              item-title="title"
              item-value="value"
              density="comfortable"
              label="Sortieren nach"
              variant="outlined"
              prepend-inner-icon="mdi-sort"
              hide-details
              class="custom-select"
            />
          </div>

          <!-- Ansicht-Umschalter -->
          <div class="view-toggle">
            <v-btn-toggle
              v-model="viewMode"
              divided
              variant="outlined"
              class="view-toggle-buttons"
            >
              <v-btn :value="'grid'" size="small">
                <v-icon icon="mdi-view-grid" />
              </v-btn>
              <v-btn :value="'list'" size="small">
                <v-icon icon="mdi-view-list" />
              </v-btn>
            </v-btn-toggle>
          </div>
        </div>

        <!-- Aktive Filter -->
        <div v-if="hasActiveFilters" class="active-filters">
          <span class="text-caption text-medium-emphasis mr-2">Aktive Filter:</span>
          <v-chip
            v-if="q"
            closable
            @click:close="q = ''"
            size="small"
            variant="outlined"
            class="active-filter-chip"
          >
            Suche: "{{ q }}"
          </v-chip>
          <v-chip
            v-if="lang"
            closable
            @click:close="lang = null"
            size="small"
            variant="outlined"
            class="active-filter-chip"
          >
            Sprache: {{ lang }}
          </v-chip>
          <v-btn
            variant="text"
            size="x-small"
            @click="clearFilters"
            class="clear-all-btn"
          >
            Alle löschen
          </v-btn>
        </div>
      </v-card-text>
    </v-card>

    <!-- Ergebnisübersicht -->
    <div class="results-summary">
      <span class="text-body-2 text-white">
        Zeige {{ visible.length }} von {{ repos.length }} Repositories
      </span>
      <v-progress-linear
        v-if="loading"
        indeterminate
        color="primary"
        class="loading-bar"
      />
    </div>

    <!-- Ladezustand -->
    <div v-if="loading" class="loading-section">
      <v-row>
        <v-col 
          v-for="i in skeletonCount" 
          :key="i" 
          :cols="viewMode === 'list' ? 12 : 12"
          :md="viewMode === 'list' ? 12 : 4"
        >
          <v-skeleton-loader
            :type="viewMode === 'list' ? 'card-list-item-avatar-three-line' : 'card'"
            class="skeleton-loader"
            elevation="2"
            rounded="lg"
          />
        </v-col>
      </v-row>
    </div>

    <!-- Inhalt -->
    <div v-else class="content-section">
      <!-- Rasteransicht -->
      <v-row v-if="viewMode === 'grid'" class="repos-grid">
        <v-col cols="12" md="6" lg="4" v-for="repo in visible" :key="repo.id">
          <ProjectCard :item="repo" />
        </v-col>
      </v-row>

      <!-- Listenansicht -->
      <v-card v-else class="list-view-card" elevation="2" rounded="lg">
        <v-list class="repo-list">
          <v-list-item
            v-for="repo in visible"
            :key="repo.id"
            class="repo-list-item"
            :href="repo.html_url"
            target="_blank"
          >
            <template v-slot:prepend>
              <v-avatar color="primary" variant="tonal" size="48" class="repo-avatar">
                <v-icon icon="mdi-source-repository" />
              </v-avatar>
            </template>

            <v-list-item-title class="repo-name">
              {{ repo.name }}
            </v-list-item-title>

            <v-list-item-subtitle class="repo-description">
              {{ repo.description || 'Keine Beschreibung vorhanden' }}
            </v-list-item-subtitle>

            <template v-slot:append>
              <div class="repo-meta">
                <div class="meta-item" v-if="repo.language">
                  <div 
                    class="language-dot" 
                    :style="{ backgroundColor: getLanguageColor(repo.language) }"
                  ></div>
                  <span class="meta-text">{{ repo.language }}</span>
                </div>
                <div class="meta-item">
                  <v-icon icon="mdi-star-outline" size="16" />
                  <span class="meta-text">{{ repo.stargazers_count || 0 }}</span>
                </div>
                <div class="meta-item">
                  <v-icon icon="mdi-clock-outline" size="16" />
                  <span class="meta-text">{{ formatRelativeTime(repo.updated_at) }}</span>
                </div>
              </div>
            </template>
          </v-list-item>
        </v-list>
      </v-card>

      <!-- Leerer Zustand -->
      <v-card v-if="!visible.length && !loading" class="empty-state" elevation="2" rounded="xl">
        <v-card-text class="empty-content">
          <v-icon icon="mdi-magnify-remove" size="64" class="empty-icon" />
          <h3 class="text-h5 font-weight-bold mb-2">Keine Repositories gefunden</h3>
          <p class="text-body-1 text-medium-emphasis mb-4">
            Versuche deine Suche oder Filter anzupassen, um das Gewünschte zu finden.
          </p>
          <v-btn @click="clearFilters" variant="outlined" color="primary">
            Alle Filter löschen
          </v-btn>
        </v-card-text>
      </v-card>
    </div>
  </v-container>
</template>

<script setup lang="ts">
import { onMounted, ref, computed } from 'vue'
import ProjectCard from './ProjectCard.vue'

// Props
const props = defineProps<{
  user?: string
  limit?: number
}>()

// Username fallback (env oder prop)
const username = props.user ?? import.meta.env.VITE_GITHUB_USERNAME ?? 'je2700'
const limit = props.limit ?? 0 // 0 = alle

// Repo-Typ (nur Felder, die wir brauchen)
interface RepoItem {
  id: number
  name: string
  description?: string | null
  html_url: string
  language?: string | null
  stargazers_count?: number
  updated_at?: string
  forks_count?: number
}

// Refs
const loading = ref(true)
const repos = ref<RepoItem[]>([])
const q = ref('')
const lang = ref<string | null>(null)
const sort = ref<'updated' | 'stars'>('updated')
const viewMode = ref<'grid' | 'list'>('grid')

const sortOptions = [
  { title: 'Recently updated', value: 'updated' },
  { title: 'Most stars', value: 'stars' },
] as const

// Computed properties
const languages = computed(() => {
  const s = new Set(
    repos.value
      .map((r) => r.language)
      .filter(Boolean) as string[]
  )
  return Array.from(s).sort().map(lang => ({ 
    title: lang, 
    value: lang 
  }))
})

const totalStars = computed(() => {
  return repos.value.reduce((sum, repo) => sum + (repo.stargazers_count || 0), 0)
})

const hasActiveFilters = computed(() => {
  return !!q.value || !!lang.value
})

const skeletonCount = computed(() => {
  return viewMode.value === 'list' ? 3 : 6
})

const visible = computed(() => {
  let arr = repos.value.slice()

  if (q.value) {
    const x = q.value.toLowerCase()
    arr = arr.filter(
      (r) =>
        r.name.toLowerCase().includes(x) ||
        (r.description && r.description.toLowerCase().includes(x))
    )
  }

  if (lang.value) {
    arr = arr.filter((r) => r.language === lang.value)
  }

  if (sort.value === 'stars') {
    arr.sort((a, b) => (b.stargazers_count || 0) - (a.stargazers_count || 0))
  } else {
    arr.sort(
      (a, b) =>
        (new Date(b.updated_at || 0).getTime() || 0) -
        (new Date(a.updated_at || 0).getTime() || 0)
    )
  }

  if (limit > 0) arr = arr.slice(0, limit)

  return arr
})

// Methods
function clearFilters() {
  q.value = ''
  lang.value = null
}

function getLanguageColor(language: string | null): string {
  const colors: Record<string, string> = {
    'JavaScript': '#f7df1e',
    'TypeScript': '#3178c6',
    'Vue': '#41b883',
    'Python': '#3776ab',
    'Java': '#ed8b00',
    'C++': '#00599c',
    'Go': '#00add8',
    'Rust': '#dea584',
    'PHP': '#777bb4',
    'Ruby': '#cc342d',
    'Swift': '#fa7343',
    'Kotlin': '#7f52ff',
    'HTML': '#e34f26',
    'CSS': '#1572b6',
    'SCSS': '#c69'
  }
  return colors[language || ''] || '#6b7280'
}

function formatRelativeTime(dateString?: string): string {
  if (!dateString) return 'recently'
  
  const date = new Date(dateString)
  const now = new Date()
  const diffTime = Math.abs(now.getTime() - date.getTime())
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))
  
  if (diffDays === 1) return 'today'
  if (diffDays < 7) return `${diffDays} days ago`
  if (diffDays < 30) return `${Math.ceil(diffDays / 7)} weeks ago`
  return `${Math.ceil(diffDays / 30)} months ago`
}

// Lifecycle
onMounted(async () => {
  loading.value = true
  try {
    const res = await fetch(
      `https://api.github.com/users/${username}/repos?per_page=100&sort=updated`
    )
    if (!res.ok) throw new Error(`GitHub API error ${res.status}`)
    const data = await res.json()
    // Map nur die benötigten Felder
    repos.value = (data || []).map((r: any) => ({
      id: r.id,
      name: r.name,
      description: r.description,
      html_url: r.html_url,
      language: r.language,
      stargazers_count: r.stargazers_count,
      updated_at: r.updated_at,
      forks_count: r.forks_count,
    }))
  } catch (e) {
    console.error('Fehler beim Laden der Repos:', e)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped lang="scss">
.repos-container {
  max-width: 1400px;
  padding: 24px;
}

.header-section {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 32px;
  flex-wrap: wrap;
  gap: 24px;

  @media (max-width: 960px) {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
}

.header-content {
  display: flex;
  align-items: center;
  gap: 20px;
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

.header-stats {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.stat-chip {
  backdrop-filter: blur(10px);
  background: rgba(255, 255, 255, 0.7) !important;
  border: 1px solid #e2e8f0;
  font-weight: 600;
}

.filters-card {
  background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
  border: 1px solid #e2e8f0;
  margin-bottom: 24px;
}

.filters-content {
  padding: 24px;
}

.filters-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr auto;
  gap: 16px;
  align-items: start;

  @media (max-width: 960px) {
    grid-template-columns: 1fr 1fr;
  }

  @media (max-width: 600px) {
    grid-template-columns: 1fr;
  }
}

.search-field {
  grid-column: 1;
}

.filter-field {
  min-width: 0;
}

.view-toggle {
  display: flex;
  align-items: center;
}

.view-toggle-buttons {
  border-radius: 8px;
}

.custom-search,
.custom-select {
  :deep(.v-field) {
    background: white;
    border-radius: 12px;
  }
}

.active-filters {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid #e2e8f0;
}

.active-filter-chip {
  backdrop-filter: blur(10px);
  background: rgba(102, 126, 234, 0.1) !important;
  border-color: #667eea;
  color: #667eea;
  font-weight: 500;
}

.clear-all-btn {
  color: #667eea;
  font-weight: 500;
}

.results-summary {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.loading-bar {
  width: 200px;
}

.loading-section {
  margin-top: 16px;
}

.skeleton-loader {
  border-radius: 16px;
}

.content-section {
  min-height: 400px;
}

.repos-grid {
  gap: 24px;
}

.list-view-card {
  background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
  border: 1px solid #e2e8f0;
}

.repo-list {
  padding: 0;
}

.repo-list-item {
  border-bottom: 1px solid #e2e8f0;
  transition: all 0.3s ease;
  cursor: pointer;

  &:last-child {
    border-bottom: none;
  }

  &:hover {
    background: linear-gradient(135deg, #667eea10 0%, #764ba210 100%);
    transform: translateX(4px);
  }
}

.repo-avatar {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
}

.repo-name {
  font-weight: 600;
  font-size: 1.1rem;
  color: #1a202c;
  margin-bottom: 4px;
}

.repo-description {
  color: #4a5568;
  line-height: 1.5;
}

.repo-meta {
  display: flex;
  gap: 16px;
  align-items: center;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #718096;
  font-size: 0.875rem;
}

.meta-text {
  font-weight: 500;
}

.language-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}

.empty-state {
  background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
  border: 2px dashed #e2e8f0;
  text-align: center;
  margin-top: 48px;
}

.empty-content {
  padding: 48px 24px;
}

.empty-icon {
  color: #cbd5e0;
  margin-bottom: 16px;
}

// Animations
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.repos-grid,
.list-view-card,
.empty-state {
  animation: fadeIn 0.6s ease-out;
}

// Custom scrollbar for list view
.repo-list {
  &::-webkit-scrollbar {
    width: 6px;
  }

  &::-webkit-scrollbar-track {
    background: #f1f1f1;
    border-radius: 3px;
  }

  &::-webkit-scrollbar-thumb {
    background: #c1c1c1;
    border-radius: 3px;
  }

  &::-webkit-scrollbar-thumb:hover {
    background: #a8a8a8;
  }
}
</style>