import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import { aliases, mdi } from 'vuetify/iconsets/mdi'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'


const light = {
  dark: false,
  colors: {
    background: '#FFFFFF',
    surface: '#FFFFFF',
    primary: '#6C5CE7',
    secondary: '#00D1B2',
    info: '#209CEE',
    success: '#23D160',
    warning: '#FFDD57',
    error: '#FF3860',
  },
}


const dark = {
  dark: true,
  colors: {
    background: '#0E1016',
    surface: '#151924',
    primary: '#A29BFE',
    secondary: '#00E5C6',
  },
}


export default createVuetify({
  components,
  directives,
  theme: {
    defaultTheme: 'light',
    themes: { light, dark },
  },
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: { mdi },
  },
})