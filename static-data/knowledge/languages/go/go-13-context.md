---
{
  "slug": "go-13-context",
  "title": "Context: Cancellation and Timeouts",
  "description": "Create contexts with Background, TODO, WithCancel. Implement timeouts and deadlines with WithTimeout. Pass request-scoped values through context. Follow context propagation conventions.",
  "type": "lesson",
  "order": 13,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create contexts with Background, TODO, WithCancel",
    "Implement timeouts and deadlines with WithTimeout",
    "Pass request-scoped values through context",
    "Follow context propagation conventions"
  ],
  "knowledge_refs": ["go/go-13-context"],
  "prerequisites": ["GO-11"],
  "references": [
    {"title": "pkg.go.dev/context", "url": "https://pkg.go.dev/context"},
    {"title": "Go Blog: Go Concurrency Patterns", "url": "https://go.dev/blog/pipelines"},
    {"title": "Go Blog: Context", "url": "https://go.dev/blog/context"},
    {"title": "Effective Go - Context", "url": "https://go.dev/doc/effective_go#context"}
  ]
}
---

# GO-13: Context: Cancellation and Timeouts

## Introduction

context.Context carries deadlines, cancellation signals, and request-scoped values across API boundaries. Every function that blocks or waits should accept a context as its first parameter. Context values are immutable — derived contexts are created for cancellation, timeouts, and values.

## Key Concepts

### 1. Context Creation: Background, TODO, WithCancel

context.Background() is the root context (never cancelled). context.TODO() when you plan to add context later. context.WithCancel(parent) returns a cancellable context and cancel function. Always defer cancel() to prevent resource leaks.

```go
package main

import (
    "context"
    "fmt"
    "time"
)

func main() {
    // Root contexts
    ctx := context.Background()
    _ = context.TODO()  // placeholder

    // WithCancel
    ctx, cancel := context.WithCancel(ctx)
    defer cancel()  // important: always call

    go func() {
        select {
        case <-time.After(5 * time.Second):
            fmt.Println("Done")
        case <-ctx.Done():
            fmt.Println("Cancelled:", ctx.Err())
        }
    }()

    cancel()  // triggers ctx.Done()
    time.Sleep(100 * time.Millisecond)
}
```

### 2. WithTimeout, WithDeadline, and WithValue

context.WithTimeout(parent, duration) cancels after duration. context.WithDeadline cancels at a specific time. context.WithValue attaches key-value pairs (only for request-scoped data, not optional parameters).

```go
package main

import (
    "context"
    "fmt"
    "time"
)

func doWork(ctx context.Context) error {
    ctx, cancel := context.WithTimeout(ctx, 2*time.Second)
    defer cancel()

    result := make(chan string, 1)
    go func() {
        time.Sleep(3 * time.Second)
        result <- "done"
    }()

    select {
    case res := <-result:
        fmt.Println("Result:", res)
        return nil
    case <-ctx.Done():
        return ctx.Err()  // context deadline exceeded
    }
}

// WithValue — request-scoped data (not for optional params)
type contextKey string

const requestIDKey contextKey = "request_id"

func WithRequestID(ctx context.Context, id string) context.Context {
    return context.WithValue(ctx, requestIDKey, id)
}

func GetRequestID(ctx context.Context) (string, bool) {
    id, ok := ctx.Value(requestIDKey).(string)
    return id, ok
}
```

### 3. Context Propagation Pattern

Pass context as the first parameter. Check ctx.Done() for cancellation. Never store context in a struct. Use context for cancellation, deadlines, and request-scoped values — not for optional parameters.

```go
package main

import "context"

// Correct: context is first parameter
func FetchData(ctx context.Context, url string) (*Response, error) {
    req, err := http.NewRequestWithContext(ctx, "GET", url, nil)
    if err != nil {
        return nil, err
    }
    return doRequest(req)
}

// WRONG: storing context in struct
type Service struct {
    ctx context.Context  // anti-pattern!
}

// Correct: context per-call
func (s *Service) DoWork(ctx context.Context) error {
    select {
    case <-ctx.Done():
        return ctx.Err()
    default:
    }
    return nil
}

// Cascading cancellation
func handleRequest(ctx context.Context, req *Request) error {
    // creates a derived context with a 5s timeout
    ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
    defer cancel()

    // passes derived context to sub-operations
    user, err := fetchUser(ctx, req.UserID)
    if err != nil {
        return err
    }
    return processUser(ctx, user)
}
```

### 4. Context in HTTP Servers and Clients

The standard library integrates context deeply. http.Request has a context. http.NewRequestWithContext creates cancellable requests. Middleware can add request-scoped values to the context.

```go
package main

import (
    "context"
    "net/http"
)

// Middleware that adds request ID to context
func RequestIDMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        id := r.Header.Get("X-Request-ID")
        if id == "" {
            id = generateID()
        }
        ctx := context.WithValue(r.Context(), requestIDKey, id)
        next.ServeHTTP(w, r.WithContext(ctx))
    })
}

// Handler using context values
func handler(w http.ResponseWriter, r *http.Request) {
    id := r.Context().Value(requestIDKey).(string)
    w.Header().Set("X-Request-ID", id)
}

// HTTP client with context
func fetchWithTimeout(ctx context.Context, url string) (*http.Response, error) {
    req, err := http.NewRequestWithContext(ctx, "GET", url, nil)
    if err != nil {
        return nil, err
    }
    return http.DefaultClient.Do(req)
}
```

### 5. Context Best Practices and Pitfalls

Context is a powerful tool but has subtleties. Always pass context as the first parameter. Never use context.Value for optional parameters. Use custom types for context keys to avoid collisions.

```go
package main

import "context"

// Custom type for context keys (prevents collisions)
type userKeyType struct{}

var userKey = userKeyType{}

func WithUser(ctx context.Context, user *User) context.Context {
    return context.WithValue(ctx, userKey, user)
}

func GetUser(ctx context.Context) (*User, bool) {
    user, ok := ctx.Value(userKey).(*User)
    return user, ok
}

// Deadlines propagate
func startTask(ctx context.Context) {
    deadline, ok := ctx.Deadline()
    if ok {
        log.Printf("Task deadline: %v", deadline)
    }
    // Derived context inherits parent deadline
    subCtx, cancel := context.WithTimeout(ctx, 1*time.Second)
    defer cancel()
    // subCtx deadline = min(parent deadline, now + 1s)
}
```

**Best practices:**
- Pass context as first parameter: `func Do(ctx context.Context, arg Arg)`
- Never store context in a struct
- Always defer cancel() after creating cancellable contexts
- Use WithValue only for request-scoped data (not for dependencies)
- Use custom types, not strings, for context keys
- Check ctx.Err() after select cases to get the cancellation reason

## Practice Questions

1. What is the difference between context.Background and context.TODO?
2. Why must you always call cancel() after creating a context with WithCancel?
3. What does ctx.Err() return after a timeout? After cancellation?
4. Why should you not store context in a struct?
5. What type should you use for context keys and why?

## LLM Prompts for Deeper Understanding

1. "Explain context: Background, TODO, WithCancel, WithTimeout, WithDeadline, WithValue"
2. "Show context propagation patterns for HTTP servers, middleware, and RPC calls"
3. "Teach context best practices: first parameter, no struct storage, custom key types"

## Key Takeaways

- context carries deadlines, cancellation, and request-scoped values
- Always defer cancel() after WithCancel/WithTimeout to prevent leaks
- Pass context as first parameter; never store in a struct
- Use custom types for context keys to prevent collisions