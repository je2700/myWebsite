<template>
  <v-card class="contact-card" elevation="8" rounded="xl">
    <!-- Kopfbereich -->
    <div class="card-header">
      <v-icon icon="mdi-email-send-outline" size="48" class="header-icon" />
      <div class="header-text">
        <div class="text-h4 font-weight-bold">Kontakt aufnehmen</div>
        <div class="text-subtitle-1 text-white">
          Lassen Sie uns gemeinsam etwas Großartiges erschaffen
        </div>
      </div>
      <div class="header-decoration">
        <div class="decoration-dot dot-1"></div>
        <div class="decoration-dot dot-2"></div>
        <div class="decoration-dot dot-3"></div>
      </div>
    </div>

    <v-divider class="mx-6" />

    <!-- Formularbereich -->
    <v-card-text class="form-content">
      <v-form @submit.prevent="onSubmit" v-model="valid" class="contact-form">
        <!-- Namensfeld -->
        <v-card variant="outlined" class="input-card" rounded="lg">
          <v-card-text class="pa-4">
            <div class="input-header">
              <v-icon icon="mdi-account-outline" size="20" class="mr-2" color="primary" />
              <span class="text-subtitle-2 font-weight-medium">Ihr Name</span>
            </div>
            <v-text-field 
              v-model="name"
              variant="plain"
              placeholder="*Geben Sie Ihren vollständigen Namen ein"
              hide-details
              class="custom-text-field"
              :disabled="loading"
            />
          </v-card-text>
          <v-card-actions v-if="showErrors && nameError" class="error-message pt-0">
            <v-icon icon="mdi-alert-circle-outline" size="16" class="mr-1" />
            <span class="text-caption">{{ nameError }}</span>
          </v-card-actions>
        </v-card>

        <!-- E-Mail-Feld -->
        <v-card variant="outlined" class="input-card" rounded="lg">
          <v-card-text class="pa-4">
            <div class="input-header">
              <v-icon icon="mdi-email-outline" size="20" class="mr-2" color="primary" />
              <span class="text-subtitle-2 font-weight-medium">E-Mail-Adresse</span>
            </div>
            <v-text-field 
              v-model="email"
              type="email"
              variant="plain"
              placeholder="*Ihre.email@beispiel.com"
              hide-details
              class="custom-text-field"
              :disabled="loading"
            />
          </v-card-text>
          <v-card-actions v-if="showErrors && emailError" class="error-message pt-0">
            <v-icon icon="mdi-alert-circle-outline" size="16" class="mr-1" />
            <span class="text-caption">{{ emailError }}</span>
          </v-card-actions>
        </v-card>

        <!-- Nachrichtenfeld -->
        <v-card variant="outlined" class="input-card message-card" rounded="lg">
          <v-card-text class="pa-4">
            <div class="input-header">
              <v-icon icon="mdi-message-text-outline" size="20" class="mr-2" color="primary" />
              <span class="text-subtitle-2 font-weight-medium">Ihre Nachricht</span>
            </div>
            <v-textarea
              v-model="message"
              variant="plain"
              placeholder="*Erzählen Sie mir von Ihrem Projekt, Ihren Ideen oder sagen Sie einfach Hallo..."
              rows="6"
              auto-grow
              hide-details
              class="custom-textarea"
              :disabled="loading"
            />
          </v-card-text>
          <v-card-actions v-if="showErrors && messageError" class="error-message pt-0">
            <v-icon icon="mdi-alert-circle-outline" size="16" class="mr-1" />
            <span class="text-caption">{{ messageError }}</span>
          </v-card-actions>
        </v-card>

        <!-- Zeichenzähler -->
        <div class="character-counter">
          <span class="text-caption" :class="(message?.length || 0) > 500 ? 'text-error' : 'text-disabled'">
            {{ message?.length || 0 }}/500
          </span>
        </div>

        <!-- Aktionsbuttons -->
        <div class="action-buttons">
          <v-btn
            color="primary"
            type="submit"
            :loading="loading"
            :disabled="loading"
            size="x-large"
            class="submit-btn"
            rounded="lg"
          >
            <template v-slot:prepend>
              <v-icon :icon="loading ? 'mdi-loading mdi-spin' : 'mdi-send'" />
            </template>
            {{ loading ? 'Wird gesendet...' : 'Nachricht senden' }}
          </v-btn>

          <v-btn
            type="reset"
            variant="outlined"
            @click="reset"
            :disabled="loading"
            size="x-large"
            class="reset-btn"
            rounded="lg"
          >
            <v-icon icon="mdi-autorenew" class="mr-2" />
            Zurücksetzen
          </v-btn>
        </div>
      </v-form>
    </v-card-text>
  </v-card>

  <!-- Erfolgs-/Fehlerbenachrichtigung -->
  <v-snackbar
    v-model="snack.show"
    :color="snack.error ? 'error' : 'success'"
    :timeout="5000"
    location="top"
    elevation="24"
    rounded="pill"
    class="notification-snackbar"
  >
    <div class="snackbar-content">
      <v-icon
        :icon="snack.error ? 'mdi-alert-circle-outline' : 'mdi-check-circle-outline'"
        class="mr-3"
        size="24"
      />
      <span class="snackbar-text">{{ snack.text }}</span>
    </div>
    <template v-slot:actions>
      <v-btn
        icon
        variant="text"
        @click="snack.show = false"
        :color="snack.error ? 'white' : 'white'"
      >
        <v-icon icon="mdi-close" />
      </v-btn>
    </template>
  </v-snackbar>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'

const name = ref('')
const email = ref('')
const message = ref('')
const loading = ref(false)
const valid = ref(false)
const showErrors = ref(false)
const snack = ref({ show: false, text: '', error: false })

// Computed properties for validation
const nameError = computed(() => {
  if (!name.value) return 'Name ist erforderlich'
  if (name.value.length < 2) return 'Name muss mindestens 2 Zeichen lang sein'
  return ''
})

const emailError = computed(() => {
  if (!email.value) return 'E-Mail ist erforderlich'
  if (!/.+@.+\..+/.test(email.value)) return 'Bitte geben Sie eine gültige E-Mail-Adresse ein'
  return ''
})

const messageError = computed(() => {
  if (!message.value) return 'Nachricht ist erforderlich'
  if (message.value.length < 10) return 'Nachricht muss mindestens 10 Zeichen lang sein'
  if (message.value.length > 500) return 'Nachricht darf maximal 500 Zeichen lang sein'
  return ''
})

// Check if there are any errors
const hasErrors = computed(() => {
  return !!nameError.value || !!emailError.value || !!messageError.value
})

// Update valid based on all errors
const checkValidity = () => {
  valid.value = !nameError.value && !emailError.value && !messageError.value
}

// Watch for changes and update validity
watch([name, email, message], checkValidity, { immediate: true })

function reset() {
  name.value = ''
  email.value = ''
  message.value = ''
  showErrors.value = false
}

async function onSubmit() {
  // Show all errors immediately when submit is clicked
  showErrors.value = true
  
  // Check if form has any validation errors
  if (hasErrors.value) {
    snack.value = {
      show: true,
      text: '❌ Bitte füllen Sie alle Pflichtfelder korrekt aus',
      error: true
    }
    return
  }
  
  loading.value = true
  
  const endpoint = import.meta.env.VITE_CONTACT_ENDPOINT
  const formData = {
    name: name.value,
    email: email.value,
    message: message.value,
    timestamp: new Date().toISOString()
  }

  try {
    if (endpoint) {
      const response = await fetch(endpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify(formData)
      })

      if (!response.ok) {
        throw new Error(`Server antwortete mit Status ${response.status}`)
      }

      snack.value = {
        show: true,
        text: '🎉 Vielen Dank! Ihre Nachricht wurde erfolgreich gesendet.',
        error: false
      }
    } else {
      // Fallback: mailto opens email client
      const mailtoBody = `Name: ${formData.name}\nE-Mail: ${formData.email}\n\nNachricht:\n${formData.message}`
      window.location.href = `mailto:${encodeURIComponent('qassemjehad@gmail.com')}?subject=${encodeURIComponent('Neue Kontaktanfrage')}&body=${encodeURIComponent(mailtoBody)}`
      
      snack.value = {
        show: true,
        text: '📧 E-Mail-Client wird geöffnet...',
        error: false
      }
    }
    
    reset()
  } catch (e: any) {
    console.error('Contact form error:', e)
    snack.value = {
      show: true,
      text: `❌ Senden fehlgeschlagen: ${e?.message ?? 'Bitte versuchen Sie es erneut oder senden Sie uns direkt eine E-Mail.'}`,
      error: true
    }
  } finally {
    loading.value = false
  }
}
</script>

<style scoped lang="scss">
.contact-card {
  background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
  border: 1px solid #e2e8f0;
  overflow: hidden;
  position: relative;

  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
    background-size: 200% 100%;
    animation: shimmer 3s ease-in-out infinite;
  }
}

.card-header {
  position: relative;
  padding: 32px 32px 24px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  overflow: hidden;

  .header-icon {
    position: absolute;
    top: 24px;
    right: 24px;
    color: #e2e8f0;
    opacity: 0.1;
    transform: scale(2);
  }

  .header-text {
    position: relative;
    z-index: 2;
  }

  .header-decoration {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    pointer-events: none;
  }

  .decoration-dot {
    position: absolute;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.1);
    animation: float 6s ease-in-out infinite;

    &.dot-1 {
      width: 80px;
      height: 80px;
      top: -40px;
      left: -40px;
      animation-delay: 0s;
    }

    &.dot-2 {
      width: 120px;
      height: 120px;
      bottom: -60px;
      right: 10%;
      animation-delay: 2s;
    }

    &.dot-3 {
      width: 60px;
      height: 60px;
      top: 50%;
      right: -30px;
      animation-delay: 4s;
    }
  }
}

.form-content {
  padding: 32px;
}

.contact-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.input-card {
  border: 2px solid #e2e8f0;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  background: white;

  &:hover {
    border-color: #cbd5e0;
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
  }

  &:focus-within {
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
  }

  &.message-card {
    min-height: 200px;
  }
}

.input-header {
  display: flex;
  align-items: center;
  margin-bottom: 12px;
}

.custom-text-field,
.custom-textarea {
  :deep(.v-field) {
    padding: 0;
    background: transparent;

    .v-field__input {
      padding-top: 16px;
      min-height: auto;
      font-size: 16px;
      color: #2d3748;

      &::placeholder {
        color: #a0aec0;
      }
    }
  }
}

.error-message {
  background: #fed7d7;
  border-top: 1px solid #feb2b2;
  color: #c53030;
  padding: 8px 16px;
  animation: slideDown 0.3s ease-out;
}

.character-counter {
  text-align: right;
  margin-top: -12px;
}

.action-buttons {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 16px;
  margin-top: 24px;

  @media (max-width: 600px) {
    grid-template-columns: 1fr;
  }
}

.submit-btn {
  height: 56px;
  font-weight: 600;
  font-size: 16px;
  text-transform: none;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  transition: all 0.3s ease;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 30px rgba(102, 126, 234, 0.4);
  }

  &:disabled {
    transform: none;
    box-shadow: none;
  }
}

.reset-btn {
  height: 56px;
  font-weight: 500;
  font-size: 16px;
  text-transform: none;
  border: 2px solid #e2e8f0;
  color: #4a5568;

  &:hover {
    border-color: #667eea;
    color: #667eea;
    background: rgba(102, 126, 234, 0.05);
  }
}

.notification-snackbar {
  :deep(.v-snackbar__content) {
    padding: 16px 20px;
  }
}

.snackbar-content {
  display: flex;
  align-items: center;
}

.snackbar-text {
  font-weight: 500;
  font-size: 14px;
}

// Animations
@keyframes shimmer {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

@keyframes float {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  33% { transform: translateY(-10px) rotate(120deg); }
  66% { transform: translateY(5px) rotate(240deg); }
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

// Loading animation
:deep(.v-btn--loading) {
  .v-icon {
    animation: spin 1s linear infinite;
  }
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

// Responsive design
@media (max-width: 960px) {
  .card-header {
    padding: 24px 24px 20px;
    
    .text-h4 {
      font-size: 1.75rem;
    }
  }
  
  .form-content {
    padding: 24px;
  }
}

@media (max-width: 600px) {
  .contact-card {
    margin: 8px;
  }
  
  .card-header {
    padding: 20px 20px 16px;
    
    .text-h4 {
      font-size: 1.5rem;
    }
  }
  
  .form-content {
    padding: 20px;
  }
  
  .action-buttons {
    gap: 12px;
  }
  
  .submit-btn,
  .reset-btn {
    height: 48px;
    font-size: 14px;
  }
}
</style>