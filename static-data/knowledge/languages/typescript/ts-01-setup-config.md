---
title: "TypeScript Setup and Configuration"
description: "Install TypeScript, configure tsconfig.json, understand the compilation pipeline, and set up a development workflow."
type: lesson
order: 1
duration: "45 min"
difficulty: beginner
learning_objectives:
  - "Install TypeScript and configure the compiler with tsconfig.json"
  - "Understand the TypeScript compilation pipeline — TS source to JS output"
  - "Configure key compiler options: strict, target, module, outDir"
  - "Set up a complete development workflow with watch mode and source maps"
knowledge_refs:
  - typescript/ts-01-setup-config
prerequisites:
  - "None — entry point"
references:
  - title: "TypeScript Handbook — Getting Started"
    url: "https://www.typescriptlang.org/docs/handbook/intro.html"
  - title: "TS Handbook — tsconfig.json"
    url: "https://www.typescriptlang.org/docs/handbook/tsconfig-json.html"
  - title: "TypeScript Deep Dive — Project Setup"
    url: "https://basarat.gitbook.io/typescript/getting-started"
  - title: "TS Handbook — Compiler Options"
    url: "https://www.typescriptlang.org/tsconfig/"
---

# TS-01: TypeScript Setup and Configuration

## Introduction

TypeScript is a **typed superset of JavaScript** that compiles to plain JavaScript. It adds static type checking, which catches entire classes of bugs at compile time rather than runtime. Before you can benefit from TypeScript, you need to set up your environment correctly.

## Installing TypeScript

Install TypeScript globally via npm:

```bash
npm install -g typescript
tsc --version  # Version 5.5.3 (or similar)
```

For per-project installation (recommended):

```bash
npm init -y
npm install --save-dev typescript @types/node
npx tsc --version
```

The [TypeScript Handbook's Getting Started guide](https://www.typescriptlang.org/docs/handbook/intro.html) covers installation in detail.

## Your First TypeScript File

Create a file `hello.ts`:

```typescript
function greet(name: string): string {
  return `Hello, ${name.toUpperCase()}!`;
}

console.log(greet("TypeScript"));
```

The `: string` annotation tells TypeScript that `name` must be a string and the function returns a string. Compile it:

```bash
npx tsc hello.ts
# Produces hello.js
```

The TypeScript compiler **strips the types** and produces clean JavaScript. If you pass a number to `greet()`, you get a compile-time error:

```typescript
console.log(greet(42));  // ❌ Error: Argument of type 'number' is not assignable to parameter of type 'string'
```

## Understanding tsconfig.json

The `tsconfig.json` file configures the TypeScript compiler project-wide. Create it with:

```bash
npx tsc --init
```

A typical production configuration looks like this — see the [full tsconfig reference](https://www.typescriptlang.org/tsconfig/):

```json
{
  "compilerOptions": {
    "target": "ES2022",                 // Output JS version
    "module": "Node16",                 // Module system
    "moduleResolution": "Node16",       // How modules resolve
    "strict": true,                     // Enable all strict checks
    "outDir": "./dist",                 // Output directory
    "rootDir": "./src",                 // Input directory
    "sourceMap": true,                  // Debug with original TS
    "declaration": true,                // Generate .d.ts files
    "esModuleInterop": true,            // Better CJS/ESM interop
    "skipLibCheck": true                // Speed up compilation
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

## Key Compiler Options Explained

### strict: true

This single flag enables ALL type-checking strictness flags:

```json
{
  "strict": true
  // Equivalent to enabling ALL of these:
  // strictNullChecks, strictFunctionTypes, strictBindCallApply,
  // strictPropertyInitialization, noImplicitAny,
  // noImplicitThis, alwaysStrict
}
```

Without `strictNullChecks`, `null` and `undefined` are assignable to any type — the source of countless bugs:

```typescript
// With strictNullChecks ON (recommended)
let name: string = null;  // ❌ Error: Type 'null' is not assignable to type 'string'

// Without it, this compiles fine and crashes at runtime
```

### target and module

```json
{
  "target": "ES2022",   // What JS version to emit (affects syntax transforms)
  "module": "Node16"    // What module system the output uses
}
```

- `target: "ES5"` — transforms `const` to `var`, arrow functions to regular functions, etc.
- `target: "ES2022"` — preserves modern syntax, relies on modern runtime
- `module: "Node16"` — respects `"type": "module"` in package.json

## Development Workflow

### Watch Mode

Rebuild automatically on file changes:

```bash
npx tsc --watch
```

### Source Maps

With `"sourceMap": true`, the debugger maps compiled JS back to your original TS code. Set a breakpoint in your editor and debug the `.ts` files directly.

### Using with Node.js

```json
// package.json
{
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js",
    "dev": "tsc --watch & nodemon dist/index.js"
  }
}
```

## Practice Questions

1. What does `"strict": true` actually enable? Name at least 3 individual checks.
2. Why would you set `"target": "ES5"` versus `"target": "ES2022"`?
3. Create a tsconfig.json for a library project (one that other packages will consume). What options are essential?

## Key Takeaways

- TypeScript adds static type checking on top of JavaScript
- tsconfig.json is the central configuration for any TS project
- Always enable `strict: true` for maximum safety
- Use `--watch` during development for instant feedback
