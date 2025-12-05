// src/stores/theme.ts
import { defineStore } from 'pinia'

export const useThemeStore = defineStore('theme', {
  state: () => ({
    isDark: JSON.parse(localStorage.getItem('theme:isDark') ?? 'false') as boolean,
  }),
  actions: {
    toggle() {
      this.setDark(!this.isDark)
    },
    setDark(val: boolean) {
      this.isDark = val
      localStorage.setItem('theme:isDark', JSON.stringify(val))
    },
  },
})
