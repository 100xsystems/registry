---
{
  "title": "Async Patterns and Promises",
  "description": "Type async functions and Promise return types properly",
  "type": "lesson",
  "order": 15,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Type async functions and Promise return types properly",
    "Handle async error patterns with Result types",
    "Use Promise.all, allSettled, race, any with correct types",
    "Chain and compose asynchronous operations"
  ],
  "knowledge_refs": [
    "typescript/ts-15-async-promises"
  ],
  "prerequisites": [
    "TS-03",
    "TS-08"
  ],
  "references": [
    {
      "title": "TS Handbook — Promises",
      "url": "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#working-with-promises"
    },
    {
      "title": "MDN — Promise API",
      "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises"
    },
    {
      "title": "TypeScript Deep Dive — Async Patterns",
      "url": "https://basarat.gitbook.io/typescript/future-javascript/async-await"
    }
  ]
}
---

# TS-15-ASYNC-PROMISES: Async Patterns and Promises

## Introduction

TypeScript fully types async/await, Promise chains, and Promise combinators. Properly typed async code catches errors at compile time — missing awaits, incompatible Promise return types, and unhandled rejection paths become visible immediately.

## Key Concepts

### 1. Async Function Return Types

An `async` function always returns a `Promise`. TypeScript infers this automatically from the return value. You can also explicitly type the resolved value using `Promise<T>`.

```typescript
// Inferred return type
async function fetchUser(id: string) {
  const res = await fetch(`/api/users/${id}`);
  return res.json() as Promise<User>;
}
// Return type: Promise<User>

// Explicit return type — catches mistakes
async function createUser(data: CreateUserInput): Promise<User> {
  const res = await fetch('/api/users', {
    method: 'POST',
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error('Failed to create user');
  return res.json();
}

// Non-async function returning Promise
function getData(): Promise<string> {
  return Promise.resolve('data');
}
```

### 2. Promise Combinators — Typed Parallel Execution

TypeScript correctly types `Promise.all`, `Promise.allSettled`, `Promise.race`, and `Promise.any`. `Promise.all` returns a tuple type; `allSettled` discriminates between fulfilled and rejected results.

```typescript
// Promise.all — tuple return type
async function loadDashboard(): Promise<[User[], number, string]> {
  const [users, count, version] = await Promise.all([
    fetchUsers(),           // Promise<User[]>
    fetchUserCount(),       // Promise<number>
    fetchVersion(),         // Promise<string>
  ]);
  return [users, count, version];
}

// Promise.allSettled — handle partial failures
interface LoadResult {
  users?: User[];
  posts?: Post[];
  error: boolean;
}

async function loadAll(): Promise<LoadResult> {
  const results = await Promise.allSettled([
    fetchUsers(),
    fetchPosts(),
  ]);

  const [usersResult, postsResult] = results;
  return {
    users: usersResult.status === 'fulfilled' ? usersResult.value : undefined,
    posts: postsResult.status === 'fulfilled' ? postsResult.value : undefined,
    error: results.some(r => r.status === 'rejected'),
  };
}
```

### 3. Error Handling with Result Types

Instead of try/catch everywhere, use a **Result type** to make errors explicit in the type system. This pattern is common in Rust-inspired TypeScript, making error paths visible in function signatures.

```typescript
type Result<T, E = Error> =
  | { ok: true; value: T }
  | { ok: false; error: E };

async function safeFetch<T>(url: string): Promise<Result<T>> {
  try {
    const res = await fetch(url);
    if (!res.ok) {
      return { ok: false, error: new Error(`HTTP ${res.status}`) };
    }
    const data = await res.json();
    return { ok: true, value: data as T };
  } catch (err) {
    return { ok: false, error: err instanceof Error ? err : new Error('Unknown') };
  }
}

// Usage — must handle both cases
const result = await safeFetch<User[]>('/api/users');
if (result.ok) {
  console.log(result.value.length);  // narrowed to T
} else {
  console.error(result.error.message);  // narrowed to Error
}
```

### 4. Async Generators and Async Iterators

TypeScript supports **async generators** and **async iterators**. An async generator yields `Promise<T>` values and can be consumed with `for await...of`. Useful for pagination, streams, and batched processing.

```typescript
// Async generator for paginated API
async function* paginate<T>(
  url: string,
  pageSize: number = 100
): AsyncGenerator<T[], void, undefined> {
  let page = 1;
  while (true) {
    const res = await fetch(`${url}?page=${page}&limit=${pageSize}`);
    const data = await res.json();
    if (data.items.length === 0) return;
    yield data.items as T[];
    page++;
  }
}

// Consume with for await...of
async function loadAllUsers() {
  const allUsers: User[] = [];
  for await (const batch of paginate<User>('/api/users')) {
    allUsers.push(...batch);
    if (allUsers.length >= 1000) break;
  }
  return allUsers;
}
```

### 5. Async Error Boundaries and Timeouts

Type-safe error boundaries and timeout patterns prevent hanging promises and propagate errors correctly. A typed `withTimeout` wrapper makes timeout logic reusable.

```typescript
// Typed timeout wrapper
async function withTimeout<T>(
  promise: Promise<T>,
  ms: number,
  errorMsg?: string
): Promise<T> {
  const timeout = new Promise<never>((_, reject) => {
    setTimeout(() => reject(new Error(errorMsg || `Timed out after ${ms}ms`)), ms);
  });
  return Promise.race([promise, timeout]);
}

// Retry with exponential backoff
async function withRetry<T>(
  fn: () => Promise<T>,
  maxRetries: number = 3
): Promise<T> {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      return await fn();
    } catch (err) {
      if (attempt === maxRetries) throw err;
      await new Promise(resolve =>
        setTimeout(resolve, Math.min(1000 * Math.pow(2, attempt - 1), 10000))
      );
    }
  }
  throw new Error('Unreachable');
}

// Usage
const user = await withTimeout(
  withRetry(() => fetchUser('123')),
  5000,
  'Fetch user timed out'
);
```

## Practice Questions

1. What is the return type of an async function that returns `string`? What about one that throws?
1. What is the difference between `Promise.all` and `Promise.allSettled` in terms of error handling?
1. Write a typed `withRetry` function that takes a `() => Promise<T>` and retries up to 3 times.
1. How does the `Result` type pattern improve error handling compared to try/catch?

## LLM Prompts for Deeper Understanding

1. "Explain TypeScript Promise combinator types (all, allSettled, race, any) with real examples"
1. "Show me the Result type pattern for explicit error handling in TypeScript"
1. "Teach me async generator patterns for paginated API consumption in TypeScript"

## Key Takeaways

- Async functions always return `Promise<T>` — TypeScript infers `T` from the returned value
- `Promise.all` returns a tuple; `allSettled` discriminates between success and failure
- The `Result<T, E>` pattern makes error paths explicit in function signatures
