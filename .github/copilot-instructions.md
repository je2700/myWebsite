# GitHub Copilot Instructions for the Project

## Overview
This project is a modern web application built using Vue 3 and Vuetify 3, leveraging TypeScript for type safety. The architecture is designed to be modular, with clear separation of components, pages, and layouts, facilitating maintainability and scalability.

## Architecture
- **Components**: Reusable Vue components are located in the `src/components` directory. Components are automatically imported using [unplugin-vue-components](https://github.com/unplugin/unplugin-vue-components), allowing for seamless integration without manual imports.
- **Pages**: The `src/pages` directory contains the main views of the application, each corresponding to a route defined in `src/router/index.ts`. Each page can utilize shared components and layouts.
- **Layouts**: Layouts are defined in `src/layouts` and provide a consistent structure across different pages. They wrap around page components to maintain a uniform look and feel.
- **Routing**: The application uses Vue Router for navigation, with routes defined in `src/router/index.ts`. Each route dynamically imports the corresponding page component.

## Developer Workflows
- **Building**: Use `npm run build` to compile the application for production. Ensure that environment variables are set correctly for deployment.
- **Testing**: Implement tests using a framework of your choice. Ensure that tests cover critical components and pages.
- **Debugging**: Utilize browser developer tools for debugging. Vue Devtools can be particularly helpful for inspecting component states and Vuex store.

## Project-Specific Conventions
- **Component Naming**: Components should be named using PascalCase and stored in their respective directories within `src/components`.
- **Styling**: Use scoped styles in Vue components to avoid global style conflicts. CSS animations should be defined within the component's `<style>` block.
- **State Management**: The project uses Pinia for state management, which is defined in `src/stores`. Ensure that state is managed in a modular way to promote reusability.

## Integration Points
- **External Dependencies**: The project relies on several key libraries, including Vue, Vuetify, and Pinia. Ensure that these are correctly installed and configured in `package.json`.
- **Cross-Component Communication**: Use props for parent-to-child communication and events for child-to-parent communication. For global state, utilize Pinia stores.

## Key Files and Directories
- **Main Application**: The entry point is `src/main.ts`, where the Vue app is initialized.
- **Router Configuration**: The routing logic is defined in `src/router/index.ts`.
- **Component Examples**: Refer to `src/components/TechChips.vue` and `src/components/Timeline.vue` for examples of component structure and styling.

## Conclusion
These instructions should provide a solid foundation for AI coding agents to navigate and contribute to this codebase effectively. For any unclear sections or additional details needed, please provide feedback for further refinement.