---
{
  "slug": "go-17-http-server",
  "title": "HTTP Server, Client, and Middleware",
  "description": "Build HTTP servers with net/http, handle requests with ServeMux routers, make HTTP requests with http.Client, write middleware pattern.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Build HTTP servers with net/http",
    "Handle requests with ServeMux routers",
    "Make HTTP requests with http.Client",
    "Write middleware pattern"
  ],
  "knowledge_refs": ["go/go-17-http-server"],
  "prerequisites": ["GO-15"],
  "references": [
    {"title": "pkg.go.dev/net/http", "url": "https://pkg.go.dev/net/http"},
    {"title": "Go by Example: HTTP Server", "url": "https://gobyexample.com/http-server"},
    {"title": "Go by Example: HTTP Client", "url": "https://gobyexample.com/http-client"},
    {"title": "Go Blog: HTTP/2", "url": "https://go.dev/blog/http2"}
  ]
}
---

# GO-17: HTTP Server, Client, and Middleware

## Introduction

Go's net/http package provides a complete HTTP client and server in the standard library. The Handler interface and middleware pattern enable clean, composable HTTP services. Go 1.22 added enhanced routing with path parameters.

## Key Concepts

### 1. HTTP Server with http.Handler

http.Handler interface has `ServeHTTP(ResponseWriter, *Request)`. http.HandleFunc registers handler functions. http.Server configures timeouts, TLS, and address. ListenAndServe starts the server.

```go
package main

import (
    "fmt"
    "net/http"
    "time"
)

// Handler interface
type helloHandler struct{}

func (h *helloHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello, %s!", r.URL.Path[1:])
}

// Handler function
func healthHandler(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    w.WriteHeader(http.StatusOK)
    w.Write([]byte(`{"status":"ok"}`))
}

func main() {
    mux := http.NewServeMux()
    mux.Handle("/hello", &helloHandler{})
    mux.HandleFunc("/health", healthHandler)

    server := &http.Server{
        Addr:         ":8080",
        Handler:      mux,
        ReadTimeout:  10 * time.Second,
        WriteTimeout: 10 * time.Second,
        IdleTimeout:  60 * time.Second,
    }

    fmt.Println("Listening on :8080")
    server.ListenAndServe()
}
```

### 2. Request Handling: Path, Query, Headers, Body

r.URL.Path, r.URL.Query(), r.Header. r.Method, r.Body, r.Context(). ParseForm for form data. Go 1.22+ ServeMux supports path parameters with `{param}` syntax.

```go
package main

import (
    "encoding/json"
    "io"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    // Method check
    if r.Method != http.MethodGet {
        http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
        return
    }

    // Query parameters
    q := r.URL.Query()
    name := q.Get("name")

    // Path parameters (Go 1.22+)
    // mux.HandleFunc("GET /users/{id}", handler)
    // id := r.PathValue("id")

    // Headers
    contentType := r.Header.Get("Content-Type")
    _ = contentType

    // Request body
    body, _ := io.ReadAll(r.Body)
    defer r.Body.Close()

    // Response
    w.Header().Set("Content-Type", "application/json")
    w.WriteHeader(http.StatusOK)
    json.NewEncoder(w).Encode(map[string]string{
        "name": name,
        "body": string(body),
    })
}

// Go 1.22+ routing
func setupRouter() *http.ServeMux {
    mux := http.NewServeMux()
    mux.HandleFunc("GET /users/{id}", getUser)
    mux.HandleFunc("POST /users", createUser)
    mux.HandleFunc("DELETE /users/{id}", deleteUser)
    return mux
}

func getUser(w http.ResponseWriter, r *http.Request) {
    id := r.PathValue("id")
    json.NewEncoder(w).Encode(map[string]string{"id": id})
}
```

### 3. HTTP Client

http.Client manages connections, timeouts, and redirects. http.NewRequest creates requests. client.Do executes. Configure Transport for connection pooling and custom TLS. Always set timeouts.

```go
package main

import (
    "encoding/json"
    "fmt"
    "net/http"
    "time"
)

var client = &http.Client{
    Timeout: 30 * time.Second,
    Transport: &http.Transport{
        MaxIdleConns:        100,
        IdleConnTimeout:     90 * time.Second,
        DisableCompression:  false,
    },
}

func fetchUser(id string) (*User, error) {
    url := fmt.Sprintf("https://api.example.com/users/%s", id)

    req, err := http.NewRequest("GET", url, nil)
    if err != nil {
        return nil, err
    }
    req.Header.Set("Accept", "application/json")
    req.Header.Set("Authorization", "Bearer "+token)

    resp, err := client.Do(req)
    if err != nil {
        return nil, fmt.Errorf("request failed: %w", err)
    }
    defer resp.Body.Close()

    if resp.StatusCode != http.StatusOK {
        return nil, fmt.Errorf("API error: %s", resp.Status)
    }

    var user User
    if err := json.NewDecoder(resp.Body).Decode(&user); err != nil {
        return nil, err
    }
    return &user, nil
}
```

### 4. Middleware Pattern

Middleware wraps an http.Handler with additional behavior. The pattern: `func(next http.Handler) http.Handler`. Use for logging, authentication, rate limiting, CORS, request ID. Middleware composes by nesting.

```go
package main

import (
    "log"
    "net/http"
    "time"
)

func loggingMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        start := time.Now()
        next.ServeHTTP(w, r)
        log.Printf("%s %s %v", r.Method, r.URL.Path, time.Since(start))
    })
}

func corsMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        w.Header().Set("Access-Control-Allow-Origin", "*")
        w.Header().Set("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE")
        w.Header().Set("Access-Control-Allow-Headers", "Content-Type, Authorization")
        if r.Method == "OPTIONS" {
            w.WriteHeader(http.StatusOK)
            return
        }
        next.ServeHTTP(w, r)
    })
}

func recoveryMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        defer func() {
            if err := recover(); err != nil {
                log.Printf("PANIC: %v", err)
                http.Error(w, "Internal Server Error", 500)
            }
        }()
        next.ServeHTTP(w, r)
    })
}

// Chain middleware
func main() {
    mux := http.NewServeMux()
    mux.HandleFunc("/", handler)

    // Middleware applied in reverse order (last wraps first)
    wrapped := recoveryMiddleware(loggingMiddleware(corsMiddleware(mux)))
    http.ListenAndServe(":8080", wrapped)
}
```

### 5. Graceful Shutdown and Context

Use signal.NotifyContext for graceful shutdown. http.Server.Shutdown gracefully stops accepting connections. Respect in-flight requests with a context deadline.

```go
package main

import (
    "context"
    "log"
    "net/http"
    "os/signal"
    "syscall"
    "time"
)

func main() {
    ctx, stop := signal.NotifyContext(context.Background(),
        syscall.SIGINT, syscall.SIGTERM)
    defer stop()

    mux := http.NewServeMux()
    mux.HandleFunc("/", handler)

    server := &http.Server{
        Addr:    ":8080",
        Handler: mux,
    }

    // Start server in goroutine
    go func() {
        log.Println("Server starting on :8080")
        if err := server.ListenAndServe(); err != nil &&
            err != http.ErrServerClosed {
            log.Fatal(err)
        }
    }()

    <-ctx.Done()  // wait for signal
    log.Println("Shutting down...")

    shutdownCtx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
    defer cancel()

    if err := server.Shutdown(shutdownCtx); err != nil {
        log.Fatal("Shutdown error:", err)
    }
    log.Println("Server stopped")
}
```

## Practice Questions

1. What is the http.Handler interface? How does it differ from http.HandlerFunc?
2. How do you access query parameters from a request? Path parameters in Go 1.22+?
3. What is the middleware pattern in Go HTTP? How do you compose multiple middlewares?
4. Why configure http.Client timeouts? What happens without them?
5. How do you implement graceful shutdown for an HTTP server?

## LLM Prompts for Deeper Understanding

1. "Explain net/http server: Handler, ServeMux, Server config, timeouts, TLS"
2. "Show HTTP client patterns: request creation, timeout, error handling, connection pooling"
3. "Teach middleware composition: logging, auth, CORS, recovery, request ID, graceful shutdown"

## Key Takeaways

- http.Handler has ServeHTTP(w, r); http.HandleFunc for functions
- http.Client with timeouts prevents resource leaks
- Middleware wraps handlers: func(next http.Handler) http.Handler
- Go 1.22+ has enhanced routing with path parameters
- Graceful shutdown is essential for production servers