---
title: "Module Systems, Bundlers, and Build Pipelines"
description: "Deep dive into module resolution algorithms, bundler internals, tree-shaking, code splitting, and modern build tooling."
type: lesson
order: 20
duration: "60 min"
difficulty: expert
level: Expert
learning_objectives:
  - "Understand module resolution algorithms (Node.js, bundlers)"
  - "Configure bundler code splitting for optimal loading performance"
  - "Explain tree-shaking mechanics and how to ensure it works"
  - "Design efficient build pipelines with modern tooling (Vite, esbuild, Webpack)"
knowledge_refs:
  - languages/javascript/js-expert-06-module-systems-bundlers
prerequisites:
  - "JS-13: Modules and Syntax"
references:
    - title: "Node.js Documentation"
      url: "https://nodejs.org/api/packages.html"
      sections: "Packages: Modules, Exports, Imports | ECMAScript modules | Module resolution"
      description: "Official Node.js package and module documentation"
    - title: "MDN JavaScript Guide"
      url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"
      sections: "JavaScript modules"
      description: "Complete guide to ESM syntax and behavior"
    - title: "webpack Documentation"
      url: "https://webpack.js.org/concepts/"
      sections: "Code Splitting | Tree Shaking | Module Resolution"
      description: "Bundler internals and optimization strategies"
    - title: "Vite Documentation"
      url: "https://vitejs.dev/guide/"
      sections: "Features: ESM-based dev server, HMR, Build | Pre-bundling with esbuild"
      description: "Modern build tool design and optimizations"
---

# JS-20: Module Systems, Bundlers, and Build Pipelines

## Introduction

Module bundlers transform a tree of modules into optimized bundles for the browser.
Understanding how module resolution, tree-shaking, and code splitting work at a
deep level enables configuring builds for optimal performance.

## Subtopics

### 1. Module Resolution Algorithms

- **Node.js resolution**: `require("lodash")` → look in `node_modules/lodash`
  → check `package.json#exports` → fallback to `package.json#main`
- **Bundler resolution**: Additional features: alias, extensions, tsconfig paths
- **ESM resolution**: Must include file extension: `import "./foo.js"` not `"./foo"`
- **Conditional exports**: Node.js `exports` field with `import`, `require`, `node`, `browser` conditions
- *Reference:* Node.js — Packages docs | webpack — Module Resolution

### 2. Tree-Shaking

- **Static analysis**: Bundler traverses ESM import/export graph, removes unused exports
- **Dead code elimination (DCE)**: Uglify/terser further removes unreachable code
- **Side effects**: `"sideEffects": false` in package.json — tells bundler import is safe to remove
- **Barrel files**: `export * from "./module"` — can prevent tree-shaking (import directly instead)
- *Reference:* webpack — Tree Shaking | rollup.js — Tree-shaking

### 3. Code Splitting

- **Entry point splitting**: Separate bundles for different page entry points
- **Dynamic import splitting**: `import("./heavy-component.js")` — chunks created automatically
- **Shared vendor chunk**: Common dependencies extracted into vendor bundle
- **Prefetch/preload**: `<link rel="preload">` and `<link rel="prefetch">`
- *Reference:* webpack — Code Splitting | Vite — Build optimizations

### 4. Build Pipeline Design

- **esbuild**: Fast bundler written in Go — Vite uses it for pre-bundling
- **Vite**: ESM-based dev server with HMR, uses Rollup for production builds
- **webpack**: Most configurable, largest ecosystem
- **SWC**: Rust-based transpiler used as Babel replacement
- **Source maps**: `devtool` config — eval, cheap-source-map, hidden-source-map
- *Reference:* Vite docs — Features | webpack docs — Configuration

## Key Takeaways

- ESM is statically analyzable — enables tree-shaking; CommonJS is not
- Tree-shaking removes unused exports via static analysis
- Code splitting reduces initial bundle size — use dynamic imports
- Vite provides fast ESM-based dev + optimized Rollup builds for production
- Side effects flags help bundlers confidently remove unused exports
