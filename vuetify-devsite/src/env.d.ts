interface ImportMetaEnv {
readonly VITE_GITHUB_USERNAME: string
readonly VITE_CONTACT_ENDPOINT?: string
}


interface ImportMeta {
readonly env: ImportMetaEnv
}