---
{
  "title": "Migration Patterns: JavaScript to TypeScript",
  "description": "Set up TypeScript incrementally in an existing JS project",
  "type": "lesson",
  "order": 21,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Set up TypeScript incrementally in an existing JS project",
    "Use allowJs and checkJs for gradual migration",
    "Add type declarations for untyped dependencies",
    "Migrate patterns: JSDoc to TS, CommonJS to ES modules"
  ],
  "knowledge_refs": [
    "typescript/ts-21-migration-patterns"
  ],
  "prerequisites": [
    "TS-01",
    "TS-16"
  ],
  "references": [
    {
      "title": "TS Handbook — Migrating from JS",
      "url": "https://www.typescriptlang.org/docs/handbook/migrating-from-javascript.html"
    },
    {
      "title": "TS Handbook — JSDoc Support",
      "url": "https://www.typescriptlang.org/docs/handbook/jsdoc-supported-types.html"
    },
    {
      "title": "TypeScript Migration Guide",
      "url": "https://www.typescriptlang.org/docs/handbook/declaration-files/introduction.html"
    }
  ]
}
---

# TS-21-MIGRATION-PATTERNS: Migration Patterns: JavaScript to TypeScript

## Introduction

Migrating a JavaScript codebase to TypeScript can be done incrementally without disrupting development. The key is enabling `allowJs` and `strict` gradually, converting files one at a time, and using `any` and `@ts-check` as transitional tools.

## Key Concepts

### 1. Incremental Migration with allowJs and checkJs

Start by adding a minimal `tsconfig.json` with `allowJs: true`. TypeScript will type-check `.js` files (with `checkJs: true`) and `.ts` files. Convert `.js` to `.ts` file by file. The compiler will catch cross-file type errors during migration.

```typescript
// Step 1: Add tsconfig.json to existing JS project
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "allowJs": true,          // allow .js files in compilation
    "checkJs": false,         // start false — enable later
    "strict": false,          // start loose — tighten later
    "outDir": "dist",
    "rootDir": "src",
    "noEmit": true,           // existing build handles emit
    "skipLibCheck": true
  },
  "include": ["src"]
}

// Step 2: Rename a file from .js to .ts
// fix TypeScript errors in that file

// Step 3: Enable checkJs gradually
// Add // @ts-check to .js files you want to check

// Step 4: Turn on strict incrementally:
// "noImplicitAny": true  ->  "strictNullChecks": true  ->  "strict": true
```

### 2. Using JSDoc Annotations During Migration

Before renaming to `.ts`, you can add JSDoc type annotations to `.js` files. TypeScript understands `@param`, `@returns`, `@type`, `@typedef`, and JSDoc `import()` types. This eases the transition and catches type errors early.

```typescript
// Before migration: JSDoc types in .js files
// @ts-check

/**
 * @typedef {Object} User
 * @property {string} id
 * @property {string} name
 * @property {number} age
 */

/**
 * Fetches a user by ID
 * @param {string} userId - The user's unique identifier
 * @returns {Promise<User>}
 */
async function fetchUser(userId) {
  const res = await fetch(`/api/users/${userId}`);
  /** @type {User} */
  const data = await res.json();
  return data;
}

/**
 * @param {import('express').Request} req
 * @param {import('express').Response} res
 */
function handler(req, res) {
  res.json({ ok: true });
}

// After migration to .ts — convert JSDoc to TS syntax
export async function fetchUser(userId: string): Promise<User> { ... }
```

### 3. Typing Untyped Dependencies

Many npm packages still lack TypeScript types. Create local `.d.ts` declaration files (`ambient declarations`) for untyped modules. For popular packages, install `@types/<package>` from DefinitelyTyped.

```typescript
// Option 1: Install types from DefinitelyTyped
// npm install --save-dev @types/express @types/lodash @types/node

// Option 2: Ambient declaration for untyped module
// src/types/untyped-lib.d.ts
declare module 'untyped-lib' {
  export function doSomething(input: string): number;
  export const VERSION: string;
}

// Option 3: Quick-and-dirty any declaration
declare module 'barely-typed-package';  // resolves to any

// Option 4: Augment existing module
declare module 'express' {
  interface Request {
    user?: {
      id: string;
      role: 'admin' | 'user';
    };
  }
}

// Option 5: declare global for window augmentations
declare global {
  interface Window {
    __ENV__: {
      API_URL: string;
      NODE_ENV: string;
    };
  }
}
```

### 4. Refactoring Patterns During Migration

Common patterns in JS need adjustment for TS. Use `unknown` instead of `any` for safer dynamic values. Replace `||` defaults with `??` (nullish coalescing) to handle falsy values. Use `as const` for constants. Replace `Object.create` with classes.

```typescript
// Pattern 1: Replace || with ?? (nullish coalescing)
// JS style:
const timeout = config.timeout || 3000;  // bug: 0 becomes 3000
// TS style:
const timeout = config.timeout ?? 3000;  // correct: 0 stays 0

// Pattern 2: Use unknown instead of any
// BAD:
function parse(data: any): string { return data.toString(); }
// GOOD:
function parse(data: unknown): string {
  if (typeof data === 'string') return data;
  return String(data);
}

// Pattern 3: as const for constants
export const HTTP_STATUS = {
  OK: 200,
  CREATED: 201,
  NOT_FOUND: 404,
} as const;
type HttpStatus = (typeof HTTP_STATUS)[keyof typeof HTTP_STATUS];

// Pattern 4: Type narrowing for dynamic access
function getProperty(obj: Record<string, unknown>, key: string): unknown {
  if (key in obj) return obj[key];
  return undefined;
}
```

### 5. Handling CommonJS, JSON, and Dynamic Requires

TypeScript handles CommonJS via `esModuleInterop`. JSON imports need `resolveJsonModule`. Dynamic `require()` can be typed with `import()` or ambient declarations. Configure `module` and `moduleResolution` to match your build system.

```typescript
// tsconfig.json for CommonJS migration
{
  "compilerOptions": {
    "module": "commonjs",        // output CommonJS
    "esModuleInterop": true,      // default imports from CJS
    "resolveJsonModule": true,    // import .json files
    "allowSyntheticDefaultImports": true,

    // For mixed ESM/CJS projects
    "moduleDetection": "force",
  }
}

// Importing CommonJS from TypeScript
import express from 'express';  // works with esModuleInterop

// Dynamic require
function loadModule(name: string) {
  // @ts-ignore — last resort
  const mod = require(name);
  return mod;
}

// Typed dynamic import
async function loadValidator(): Promise<typeof import('./validators')> {
  return import('./validators');
}

// JSON import
import pkg from './package.json';
console.log(pkg.version);  // typed as string
```

## Practice Questions

1. What is the migration order from JS to TS? List the key steps.
1. How does `allowJs: true` help with incremental migration?
1. What is the difference between `@ts-check` and `@ts-nocheck`? When would you use each?
1. How do you create ambient declarations for an untyped npm package? Write an example.

## LLM Prompts for Deeper Understanding

1. "Explain step-by-step migration from JavaScript to TypeScript for a 50k+ LOC codebase"
1. "Show me how to use JSDoc type annotations as a stepping stone to TypeScript migration"
1. "Teach me how to create declaration files (.d.ts) for untyped npm packages"

## Key Takeaways

- Use `allowJs`, `checkJs`, and incremental strict mode to migrate file-by-file
- JSDoc annotations bridge the gap during migration — convert to TS syntax later
- Create `.d.ts` ambient declarations for untyped npm dependencies
