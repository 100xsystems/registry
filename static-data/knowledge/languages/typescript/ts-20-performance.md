---
{
  "title": "Performance and Optimization",
  "description": "Diagnose slow type-checking with the perf trace flag",
  "type": "lesson",
  "order": 20,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Diagnose slow type-checking with the perf trace flag",
    "Optimize complex types to reduce evaluation time",
    "Use interface over intersection for faster type checks",
    "Understand variance and structural checking performance"
  ],
  "knowledge_refs": [
    "typescript/ts-20-performance"
  ],
  "prerequisites": [
    "TS-08",
    "TS-10"
  ],
  "references": [
    {
      "title": "TS Wiki — Performance",
      "url": "https://github.com/microsoft/TypeScript/wiki/Performance"
    },
    {
      "title": "TS Handbook — Performance Tuning",
      "url": "https://www.typescriptlang.org/docs/handbook/performance.html"
    },
    {
      "title": "TypeScript Performance Deep Dive",
      "url": "https://blog.appsignal.com/2023/03/15/typescript-performance-tuning.html"
    }
  ]
}
---

# TS-20-PERFORMANCE: Performance and Optimization

## Introduction

TypeScript type-checking performance matters, especially in large codebases. Complex conditional types, deeply nested generics, and large unions can slow compilation significantly. Understanding how the type checker works helps you write types that compile fast.

## Key Concepts

### 1. Diagnosing Slow Types

Use `--generateTrace` and `--extendedDiagnostics` flags to find slow types. The trace output shows which files and types take longest to check. Focus optimization efforts on the top 10% of slow types.

```typescript
// tsconfig.json for performance debugging
{
  "compilerOptions": {
    "extendedDiagnostics": true,  // prints timing info on build
    "generateTrace": "trace",     // outputs trace files for chrome://tracing

    // Flags that improve speed
    "skipLibCheck": true,          // skip .d.ts checking (major speedup)
    "skipDefaultLibCheck": true,   // skip default lib checking
    "incremental": true,           // only re-check changed files
    "noEmit": true                 // no emit = faster type-checking
  }
}

// Run: tsc --generateTrace trace
// Open trace in chrome://tracing to see what's slow
```

### 2. Expensive Type Patterns to Avoid

Certain type patterns are computationally expensive for the compiler. Recursive conditional types, large discriminated unions, and deeply nested mapped types can cause exponential type evaluation.

```typescript
// BAD: Recursive conditional type (expensive)
type DeepReadonly<T> = T extends object
  ? { readonly [K in keyof T]: DeepReadonly<T[K]> }
  : T;
// TypeScript has recursion limits — use cautiously

// BETTER: Limit recursion depth
type DeepReadonly2<T, Depth extends number = 5> = Depth extends 0
  ? T
  : T extends object
  ? { readonly [K in keyof T]: DeepReadonly2<T[K], Prev[Depth]> }
  : T;

// BAD: Huge discriminated unions (1000+ members)
// Slow to narrow and compare
type AllRoutes = { path: '/users'; params: { id: string } }
  | { path: '/posts'; params: { id: string } }
  // ... 1000 more routes

// BETTER: Use interface with index signature
interface RouteMap {
  '/users': { id: string };
  '/posts': { id: string };
  // ... same 1000 entries
}
type Route<K extends keyof RouteMap> = { path: K; params: RouteMap[K] };
```

### 3. Interface vs Intersection for Performance

Interfaces are cached by TypeScript; intersection types are evaluated structurally each time. For complex type compositions, prefer interfaces with `extends` over `&` for better performance.

```typescript
// FASTER: Interface extension
type A = { a: string };
type B = { b: number };
type C = { c: boolean };

interface Fast extends A, B, C {}  // faster — cached

// SLOWER: Intersection types
type Slow = A & B & C;  // slower — evaluated each time

// For external consumers:
// Interface is better — declaration merging, cached, better error messages
interface User extends BaseUser, Timestamped, SoftDeletable {}

// But for conditional/mapped results, type is necessary:
type Result<T> = T extends string ? { value: string } : { value: number };
```

### 4. Prefer Flat Types Over Deep Nesting

Deeply nested generics cause exponential type-checking time. Flatten your types where possible, and avoid recursive mapped types on very large objects.

```typescript
// BAD: Deep nesting — slow comparison
interface User {
  profile: { address: { street: string; city: string; coordinates: { lat: number; lng: number } } };
  settings: { preferences: { notifications: { email: boolean; push: boolean } } };
  // ... more nesting
}

// BETTER: Flatten reference types
interface Coordinates { lat: number; lng: number; }
interface Address { street: string; city: string; coordinates: Coordinates; }
interface NotificationPrefs { email: boolean; push: boolean; }
interface UserPreferences { notifications: NotificationPrefs; }
interface UserProfile { address: Address; }

interface User {
  profile: UserProfile;
  settings: UserPreferences;
}

// TypeScript compares by structural identity — separate types are faster
// than inline object literals
```

### 5. Project Setup for Speed

Correct project configuration dramatically improves incremental build performance. Enable `incremental`, `skipLibCheck`, project references for monorepos, and consider `isolatedModules` for parallel builds.

```typescript
// Production-optimized tsconfig.json
{
  "compilerOptions": {
    // Speed flags
    "incremental": true,              // only rebuild changed files
    "skipLibCheck": true,             // skip .d.ts checking
    "skipDefaultLibCheck": true,      // skip default lib
    "isolatedModules": true,          // non-dependent file compilation
    "noEmit": true,                   // no emit = less work

    // Strictness
    "strict": true,

    // Modern module settings
    "module": "ESNext",
    "moduleResolution": "bundler",
    "target": "ES2022",

    // Declarations (only if needed for library)
    // "declaration": true,
    // "declarationMap": true,

    // Other
    "forceConsistentCasingInFileNames": true,
    "esModuleInterop": true,
    "resolveJsonModule": true
  },
  "include": ["src"],
  "exclude": ["node_modules", "dist", "**/*.test.ts"]
}
```

## Practice Questions

1. How does `skipLibCheck` speed up compilation? When is it unsafe to use?
1. Why are intersection types (`&`) slower than interface `extends` for large type compositions?
1. How does the `incremental` flag reduce build times? Where is the cache stored?
1. What diagnostics tool would you use to find which type in your codebase is slowest to check?

## LLM Prompts for Deeper Understanding

1. "Explain TypeScript performance optimization strategies for large codebases"
1. "Show me how to use --generateTrace to find and fix slow TypeScript types"
1. "Teach me about intersection type performance vs interface extends with benchmarks"

## Key Takeaways

- Use `--generateTrace` to find the slowest types in your codebase
- Interfaces with `extends` are faster than intersection types (`&`)
- Enable `incremental`, `skipLibCheck`, and `isolatedModules` for faster builds
