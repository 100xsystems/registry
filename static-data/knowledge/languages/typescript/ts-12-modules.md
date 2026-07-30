---
{
  "title": "Modules and Namespaces",
  "description": "Use ES module import/export with type-safe patterns",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use ES module import/export with type-safe patterns",
    "Re-export and barrel modules for clean public APIs",
    "Understand namespace vs module tradeoffs",
    "Use dynamic imports for code splitting"
  ],
  "knowledge_refs": [
    "typescript/ts-12-modules"
  ],
  "prerequisites": [
    "TS-03"
  ],
  "references": [
    {
      "title": "TS Handbook — Modules",
      "url": "https://www.typescriptlang.org/docs/handbook/2/modules.html"
    },
    {
      "title": "TS Handbook — Namespaces",
      "url": "https://www.typescriptlang.org/docs/handbook/namespaces.html"
    },
    {
      "title": "TS Handbook — Dynamic Imports",
      "url": "https://www.typescriptlang.org/docs/handbook/2/modules.html#dynamic-import"
    }
  ]
}
---

# TS-12-MODULES: Modules and Namespaces

## Introduction

Modules are the standard way to organize TypeScript code. TypeScript fully supports ES modules — `import` and `export` with type-safe re-exports, barrel files, and dynamic imports. Namespaces (the old `module` keyword) are legacy but still encountered in `.d.ts` files.

## Key Concepts

### 1. Named and Default Exports

TypeScript extends ES exports with type-only exports (`export type { Foo }`). This helps bundlers eliminate unused type imports. Default exports can be named anything on import, but named exports preserve the original name.

```typescript
// types.ts
export type User = { id: string; name: string };
export type Status = 'active' | 'inactive';
// Type-only export (TS 4.5+)
export type { Admin } from './admin';

// utils.ts
export function formatDate(date: Date): string { /* ... */ }
export function parseCSV(input: string): string[] { /* ... */ }

// app.ts — import everything
import { formatDate, parseCSV } from './utils';
import type { User } from './types';  // type-only import — removed at runtime

// Default export pattern
export default class Logger {
  log(msg: string) { console.log(msg); }
}
// import Logger from './logger';  // any name works
```

### 2. Barrel Files — Clean Public APIs

Barrel files (`index.ts`) re-export from multiple modules to provide a single entry point. This hides internal file structure and simplifies imports. Be careful with barrel files in large projects as they can cause circular deps.

```typescript
// services/user.service.ts
export class UserService { /* ... */ }

// services/order.service.ts
export class OrderService { /* ... */ }

// services/index.ts (barrel)
export { UserService } from './user.service';
export { OrderService } from './order.service';
export type { User, Order } from '../types';

// consumer.ts
import { UserService, OrderService } from './services';  // clean import

// Re-export with rename
export { UserService as Users } from './user.service';
```

### 3. Dynamic Imports — Code Splitting

TypeScript fully supports dynamic `import()` expressions. The return type is `Promise<typeof module>`. Dynamic imports are key for route-based code splitting in Next.js, React lazy loading, and conditional dependencies.

```typescript
// Dynamic import for code splitting
async function loadChart(type: 'bar' | 'line') {
  if (type === 'bar') {
    const { BarChart } = await import('./charts/BarChart');
    return new BarChart();
  } else {
    const { LineChart } = await import('./charts/LineChart');
    return new LineChart();
  }
}

// Dynamic import with type
type ModuleType = typeof import('./heavy-module');
async function loadHeavy(): Promise<ModuleType> {
  return import('./heavy-module');
}

// React lazy loading pattern
const LazyComponent = React.lazy(() => import('./BigComponent'));
```

### 4. Namespaces — Legacy Organization

Before ES modules, TypeScript used `namespace` (previously `module`) to organize code. Namespaces are still in `.d.ts` files for global library declarations. Don't use them in new code — use ES modules instead.

```typescript
// Legacy namespace pattern (still found in .d.ts)
namespace MyLib {
  export interface Config {
    apiKey: string;
    endpoint: string;
  }

  export function init(config: Config): void {
    console.log(`Initializing with ${config.apiKey}`);
  }

  // Nested namespace
  export namespace Utils {
    export function formatUrl(base: string, path: string): string {
      return `${base}/${path}`;
    }
  }
}

// Usage
MyLib.init({ apiKey: 'abc', endpoint: 'https://api.example.com' });
const url = MyLib.Utils.formatUrl('https://api.example.com', 'v1/users');
```

### 5. Module Resolution Strategies

TypeScript supports two module resolution strategies: `node` (Node.js-style, looks for `node_modules`, `index.ts`) and `bundler` (TS 5.0+, more flexible for bundlers like Vite/Webpack). Use `bundler` for modern projects with `moduleResolution: "bundler"`.

```typescript
// tsconfig.json
{
  "compilerOptions": {
    "module": "ESNext",
    "moduleResolution": "bundler",  // TS 5.0+ — best for modern bundlers
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]             // path alias — must match bundler config
    }
  }
}

// With path aliases:
import { UserService } from '@/services/UserService';
// Instead of: import { UserService } from '../../../services/UserService';
```

## Practice Questions

1. What is the difference between `export type { Foo }` and `export { Foo }` when `Foo` is a type?
1. Why might barrel files cause issues in large projects? How would you mitigate this?
1. Rewrite the following namespace as ES modules: `namespace Utils { export function hash(input: string): string; }`.
1. When would you use dynamic import over static import? Give a concrete example.

## LLM Prompts for Deeper Understanding

1. "Explain TypeScript module resolution strategies: node, classic, node16, nodenext, bundler"
1. "Show me barrel file patterns in TypeScript — benefits, tradeoffs, and alternatives"
1. "Teach me dynamic import patterns for code splitting with proper error handling"

## Key Takeaways

- Use ES modules (`import`/`export`) for all new code — namespaces are legacy
- Type-only imports (`import type`) are removed at compile time for smaller bundles
- Barrel files simplify imports but can cause circular dependencies in large projects
