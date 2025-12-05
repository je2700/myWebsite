import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'


// MDI Icons (lokal installiert: npm i @mdi/font)
import '@mdi/font/css/materialdesignicons.css'


// globale Styles
import './styles/main.css'


createApp(App)
.use(createPinia())
.use(router)
.use(vuetify)
.mount('#app')