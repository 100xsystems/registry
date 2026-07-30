---
{
  "slug": "go-12-sync-package",
  "title": "sync Package: Mutex, WaitGroup, Once, Pool",
  "description": "Use sync.Mutex and RWMutex for thread safety, sync.WaitGroup for goroutine coordination, sync.Once for one-time initialization, sync.Pool for object reuse.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use sync.Mutex and RWMutex for thread safety",
    "Use sync.WaitGroup for goroutine coordination",
    "Use sync.Once for one-time initialization",
    "Use sync.Pool for object reuse"
  ],
  "knowledge_refs": ["go/go-12-sync-package"],
  "prerequisites": ["GO-11"],
  "references": [
    {"title": "pkg.go.dev/sync", "url": "https://pkg.go.dev/sync"},
    {"title": "Go by Example: Mutexes", "url": "https://gobyexample.com/mutexes"},
    {"title": "Go by Example: WaitGroups", "url": "https://gobyexample.com/waitgroups"},
    {"title": "Effective Go - sync", "url": "https://go.dev/doc/effective_go#sync"}
  ]
}
---

# GO-12: sync Package: Mutex, WaitGroup, Once, Pool

## Introduction

The sync package provides basic synchronization primitives. Mutex for mutual exclusion, RWMutex for read-heavy workloads, WaitGroup for goroutine coordination, Once for one-time initialization, and Pool for reusable object caches. Never copy a sync value — pass by pointer.

## Key Concepts

### 1. sync.Mutex and sync.RWMutex

Mutex provides mutual exclusion via Lock/Unlock. RWMutex allows multiple readers or one writer. Always use defer for unlock. Keep critical sections small. RWMutex is faster for read-heavy workloads (80%+ reads).

```go
package main

import (
    "fmt"
    "sync"
)

type SafeCounter struct {
    mu    sync.Mutex
    value int
}

func (c *SafeCounter) Increment() {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.value++
}

func (c *SafeCounter) Value() int {
    c.mu.Lock()
    defer c.mu.Unlock()
    return c.value
}

// RWMutex - multiple readers, single writer
type SafeCache struct {
    mu   sync.RWMutex
    data map[string]string
}

func (c *SafeCache) Get(key string) (string, bool) {
    c.mu.RLock()
    defer c.mu.RUnlock()
    val, ok := c.data[key]
    return val, ok
}

func (c *SafeCache) Set(key, value string) {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.data[key] = value
}
```

**Mutex best practices:**
- Always use `defer` for unlock — prevents deadlocks on panic
- Keep locked regions as small as possible
- Document what the mutex protects
- Never copy a mutex — use `*sync.Mutex` if passing around
- Consider `RWMutex` only when reads significantly outnumber writes

### 2. sync.WaitGroup — Wait for Goroutines

WaitGroup waits for a collection of goroutines. `Add(n)` before launching. `Done()` in each goroutine (often via defer). `Wait()` blocks until all Done(). Never copy a WaitGroup — pass by pointer.

```go
package main

import (
    "fmt"
    "sync"
)

func main() {
    var wg sync.WaitGroup
    urls := []string{"a.com", "b.com", "c.com"}

    for _, url := range urls {
        wg.Add(1)
        go func(u string) {
            defer wg.Done()
            fetch(u)
        }(url)
    }

    wg.Wait()
    fmt.Println("All requests completed")
}

// Fan-out with bounded parallelism
func processInParallel(items []int, workers int) {
    var wg sync.WaitGroup
    sem := make(chan struct{}, workers)

    for _, item := range items {
        wg.Add(1)
        go func(val int) {
            defer wg.Done()
            sem <- struct{}{}  // acquire
            defer func() { <-sem }()  // release
            process(val)
        }(item)
    }
    wg.Wait()
}
```

**WaitGroup patterns:**
- Call `Add` before starting the goroutine, not inside it
- Use `defer wg.Done()` in each goroutine
- Combine with a semaphore channel for bounded parallelism
- WaitGroup can be reused after all Done() calls complete

### 3. sync.Once and sync.OnceFunc

sync.Once ensures a function is executed only once, even across goroutines. `Do()` blocks until the function completes. `sync.OnceFunc` (Go 1.21+) returns a reusable wrapper function.

```go
package main

import (
    "fmt"
    "sync"
)

var (
    config *Config
    once   sync.Once
)

func GetConfig() *Config {
    once.Do(func() {
        fmt.Println("Loading config once")
        config = loadConfig()
    })
    return config
}

// sync.OnceFunc (Go 1.21+)
var loadConfigOnce = sync.OnceFunc(func() {
    fmt.Println("Loading once")
    config = loadConfig()
})

func GetConfigV2() *Config {
    loadConfigOnce()
    return config
}

// sync.OnceValue (Go 1.21+)
var getConfigOnce = sync.OnceValue(func() *Config {
    return loadConfig()
})

func GetConfigV3() *Config {
    return getConfigOnce()
}
```

### 4. sync.Pool — Object Reuse

sync.Pool reuses allocated objects to reduce GC pressure. `Get()` returns an arbitrary value (or calls New). `Put()` returns objects to the pool. Items in the pool can be GC'd at any time. Best for temporary objects like buffers.

```go
package main

import (
    "bytes"
    "fmt"
    "sync"
)

var bufferPool = sync.Pool{
    New: func() interface{} {
        return new(bytes.Buffer)
    },
}

func writeToBuffer(data string) string {
    buf := bufferPool.Get().(*bytes.Buffer)
    buf.Reset()
    defer bufferPool.Put(buf)

    buf.WriteString(data)
    return buf.String()
}

// Pool for structs
var userPool = sync.Pool{
    New: func() interface{} {
        return &User{}
    },
}

func AcquireUser() *User {
    return userPool.Get().(*User)
}

func ReleaseUser(u *User) {
    u.Reset()
    userPool.Put(u)
}
```

**Pool guidelines:**
- Pool is best for buffers and temporary objects
- Objects in Pool can be silently removed by GC
- Never assume Pool.Get() returns your Put() object
- Always reset objects before reuse
- Profile before using Pool — it adds complexity

### 5. sync.Cond — Condition Variable

sync.Cond provides a condition variable for goroutines that wait for a signal. Less commonly used than channels, but useful for broadcasting events to multiple goroutines.

```go
package main

import (
    "fmt"
    "sync"
)

type Queue struct {
    items []int
    cond  *sync.Cond
}

func NewQueue() *Queue {
    return &Queue{
        cond: sync.NewCond(&sync.Mutex{}),
    }
}

func (q *Queue) Put(item int) {
    q.cond.L.Lock()
    defer q.cond.L.Unlock()
    q.items = append(q.items, item)
    q.cond.Signal()  // wake one waiter
}

func (q *Queue) Get() int {
    q.cond.L.Lock()
    defer q.cond.L.Unlock()
    for len(q.items) == 0 {
        q.cond.Wait()  // releases lock, waits, re-acquires
    }
    item := q.items[0]
    q.items = q.items[1:]
    return item
}
```

## Practice Questions

1. What is the difference between Mutex and RWMutex? When would you use each?
2. Why should you always defer Unlock() after Lock()?
3. What happens if you call WaitGroup.Add() after the goroutines have started?
4. What is sync.Pool used for? When should you use it?
5. What is the difference between sync.Once and sync.OnceFunc?

## LLM Prompts for Deeper Understanding

1. "Explain sync.Mutex and RWMutex with lock/unlock/defer patterns and best practices"
2. "Show sync.WaitGroup for fan-out/worker patterns with bounded parallelism"
3. "Teach sync.Once for lazy initialization and sync.Pool for object reuse and GC pressure"

## Key Takeaways

- Use RWMutex for read-heavy workloads, Mutex for write-heavy
- WaitGroup coordinates goroutine completion; always defer Done()
- Pool reduces GC pressure by reusing temporary objects
- Never copy a sync value — always pass by pointer