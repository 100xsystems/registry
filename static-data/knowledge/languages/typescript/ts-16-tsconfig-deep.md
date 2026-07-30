---
{
  "title": "tsconfig.json Deep Dive",
  "description": "Configure strict mode and its component flags",
  "type": "lesson",
  "order": 16,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Configure strict mode and its component flags",
    "Manage module resolution, target, and lib settings",
    "Use project references for monorepo build performance",
    "Configure path aliases, type roots, and declaration outputs"
  ],
  "knowledge_refs": [
    "typescript/ts-16-tsconfig-deep"
  ],
  "prerequisites": [
    "TS-12"
  ],
  "references": [
    {
      "title": "TS Handbook — tsconfig",
      "url": "https://www.typescriptlang.org/docs/handbook/tsconfig-json.html"
    },
    {
      "title": "TS Handbook — Compiler Options",
      "url": "https://www.typescriptlang.org/tsconfig"
    },
    {
      "title": "TS Handbook — Project References",
      "url": "https://www.typescriptlang.org/docs/handbook/project-references.html"
    }
  ]
}
---

# TS-16-TSCONFIG-DEEP: tsconfig.json Deep Dive

## Introduction

The `tsconfig.json` file controls every aspect of TypeScript compilation. Understanding its options — especially `strict`, `moduleResolution`, `target`, and project references — is essential for configuring TypeScript projects correctly.

## Key Concepts

### 1. Strict Mode and Its Components

`strict: true` enables a suite of type-checking flags that catch common bugs. Each flag can be individually disabled, but in new projects, keep them all enabled. The most impactful flags are `noImplicitAny`, `strictNullChecks`, and `noUncheckedIndexedAccess`.

```typescript
// tsconfig.json
{
  "compilerOptions": {
    "strict": true,
    // Equivalent to enabling all of these:
    // "noImplicitAny": true,         - error on implicit any
    // "strictNullChecks": true,      - null/undefined are distinct
    // "strictFunctionTypes": true,   - bivariant param checking
    // "strictBindCallApply": true,   - correct bind/call/apply types
    // "strictPropertyInitialization": true - constructor must init props
    // "noImplicitThis": true,        - this used without context
    // "alwaysStrict": true           - 'use strict' in output

    // Additional useful flags beyond strict:
    "noUncheckedIndexedAccess": true,  // adds | undefined to index access
    "noUnusedLocals": true,            // error on unused variables
    "noUnusedParameters": true,        // error on unused params
    "exactOptionalPropertyTypes": true, // strict optional handling
    "forceConsistentCasingInFileNames": true,
    "skipLibCheck": true               // skip .d.ts checking (faster)
  }
}
```

### 2. target, lib, and module Resolution

`target` sets the output JS version; `lib` specifies which type definitions are available (DOM, ES2023, etc.); `module` and `moduleResolution` control how imports are resolved. For modern projects use `ESNext` for both `module` and `target`, with `bundler` resolution.

```typescript
{
  "compilerOptions": {
    "target": "ES2022",              // output language version
    "lib": ["ES2022", "DOM", "DOM.Iterable"],  // type definitions
    "module": "ESNext",              // module system in output
    "moduleResolution": "bundler",   // TS 5+ — works with Vite/Webpack
    "moduleDetection": "force",      // every file is a module

    // For Node.js projects
    // "module": "NodeNext",
    // "moduleResolution": "NodeNext",

    "allowImportingTsExtensions": true, // import .ts files (with bundler)
    "resolveJsonModule": true,         // import .json files
    "isolatedModules": true,           // every file is a separate module
    "esModuleInterop": true,           // default imports from CJS
    "verbatimModuleSyntax": true       // type imports/exports must use 'type'
  }
}
```

### 3. Path Aliases and Base URL

Path aliases (`@/` to `src/`) clean up relative imports. They require matching configuration in the bundler (Webpack `resolve.alias`, Vite `resolve.alias`, or Next.js `compilerOptions.paths`).

```typescript
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],               // import { User } from '@/models/User'
      "@components/*": ["src/components/*"],
      "@utils/*": ["src/utils/*"],
      "@lib/*": ["src/lib/*"]
    },
    "rootDir": "src",                 // source root
    "outDir": "dist",                  // output directory
    "declaration": true,               // generate .d.ts files
    "declarationMap": true,            // source maps for .d.ts
    "sourceMap": true                   // .js.map files
  },
  "include": ["src"],
  "exclude": ["node_modules", "dist"]
}
```

### 4. Project References — Monorepo Performance

Project references split a large codebase into smaller projects that build independently. TypeScript only rebuilds changed projects — dramatically faster for monorepos. Each subproject has its own `tsconfig.json` with `composite: true`.

```typescript
// Root tsconfig.json (solutions file)
{
  "compilerOptions": {
    "composite": true,
    "declaration": true,
    "declarationMap": true
  },
  "references": [
    { "path": "packages/core" },
    { "path": "packages/utils" },
    { "path": "packages/api" },
    { "path": "packages/app" }
  ]
}

// packages/core/tsconfig.json
{
  "compilerOptions": {
    "composite": true,
    "rootDir": "src",
    "outDir": "dist",
    "declaration": true
  },
  "include": ["src"]
}

// packages/api/tsconfig.json
{
  "compilerOptions": {
    "composite": true,
    "rootDir": "src",
    "outDir": "dist"
  },
  "include": ["src"],
  "references": [
    { "path": "../core" },
    { "path": "../utils" }
  ]
}
```

### 5. Type Roots and Declaration Files

`typeRoots` controls where TypeScript looks for type definitions (`.d.ts` files). `types` restricts which `@types/*` packages are auto-included. `declaration` and `declarationMap` are critical for library authors.

```typescript
{
  "compilerOptions": {
    // Type roots — where to find .d.ts files
    "typeRoots": ["./node_modules/@types", "./typings"],

    // Only include these @types packages
    "types": ["node", "express"],

    // Library output config
    "declaration": true,         // generate .d.ts
    "declarationMap": true,     // source maps for decls
    "emitDeclarationOnly": true, // only .d.ts, no JS output

    // Use when bundler handles JS compilation
    "noEmit": true               // type-check only, no JS output
  }
}

// Global .d.ts file (e.g., typings/env.d.ts)
declare namespace NodeJS {
  interface ProcessEnv {
    NODE_ENV: 'development' | 'production';
    API_KEY: string;
    DATABASE_URL: string;
  }
}

// Module augmentation in .d.ts
declare module 'some-lib' {
  interface Options {
    timeout?: number;
    retries?: number;
  }
}
```

## Practice Questions

1. What specific checks does `strict: true` enable? Name at least 5.
1. What is the difference between `moduleResolution: "node"` and `"bundler"`? When would you use each?
1. How do project references improve build performance in monorepos?
1. Why would a library author set `declaration: true` and `declarationMap: true`?

## LLM Prompts for Deeper Understanding

1. "Explain all tsconfig strict mode flags and what each one catches"
1. "Show me how to set up project references for a TypeScript monorepo with 5+ packages"
1. "Teach me about moduleResolution strategies: node, node16, nodenext, and bundler"

## Key Takeaways

- `strict: true` enables 8 individual strictness flags that catch common bugs
- Path aliases with `baseUrl` + `paths` clean up imports, but must match bundler config
- Project references split monorepo builds into independently-compiled units for speed
