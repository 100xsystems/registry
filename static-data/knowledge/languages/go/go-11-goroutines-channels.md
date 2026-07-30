---
{
  "slug": "go-11-goroutines-channels",
  "title": "Goroutines and Channels",
  "description": "Launch goroutines with go keyword, create and use channels for communication, use select for multiplexing, understand goroutine scheduling and leaks.",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Launch goroutines with go keyword",
    "Create and use channels for communication",
    "Use select for multiplexing",
    "Understand goroutine scheduling and leaks"
  ],
  "knowledge_refs": ["go/go-11-goroutines-channels"],
  "prerequisites": ["GO-01"],
  "references": [
    {"title": "Go by Example: Goroutines", "url": "https://gobyexample.com/goroutines"},
    {"title": "Go by Example: Channels", "url": "https://gobyexample.com/channels"},
    {"title": "Go by Example: Select", "url": "https://gobyexample.com/select"},
    {"title": "Effective Go — Concurrency", "url": "https://go.dev/doc/effective_go#concurrency"}
  ]
}
---

# GO-11: Goroutines and Channels

## Introduction

Goroutines are lightweight threads managed by the Go runtime. They start with a tiny 2KB stack that grows and shrinks as needed. Channels are typed conduits for communication between goroutines. The Go mantra: "Do not communicate by sharing memory; instead, share memory by communicating."

## Key Concepts

### 1. Goroutines — Lightweight Threads

A goroutine is any function call prefixed with the `go` keyword. Goroutines are multiplexed onto OS threads by the Go scheduler (M:N scheduling). The main function does not wait for goroutines unless you use synchronization.

```go
package main

import (
    "fmt"
    "time"
)

func say(msg string) {
    for i := 0; i < 3; i++ {
        fmt.Println(msg)
        time.Sleep(100 * time.Millisecond)
    }
}

func main() {
    go say("hello")
    go say("world")
    time.Sleep(time.Second)
}
```

Key points: ~2KB stack vs 1MB for OS threads, work-stealing scheduler, cooperatively scheduled.

### 2. Channels — Typed Communication

Channels are typed: `chan T`, `chan<- T` (send-only), `<-chan T` (receive-only). Create with `make(chan T)`. Unbuffered channels synchronize.

```go
package main

import "fmt"

func main() {
    ch := make(chan int)
    go func() {
        ch <- 42
    }()
    val := <-ch
    fmt.Println(val)
}
```

### 3. Buffered Channels

Buffered channels have capacity: `make(chan T, capacity)`. Sends block only when buffer is full. Receives block only when buffer is empty.

```go
ch := make(chan int, 3)
ch <- 1
ch <- 2
ch <- 3
fmt.Println(<-ch) // 1
```

### 4. select — Multiplexing Channels

`select` waits on multiple channel operations. If multiple are ready, one is chosen at random. `default` makes it non-blocking.

```go
select {
case msg := <-ch1:
    fmt.Println(msg)
case msg := <-ch2:
    fmt.Println(msg)
case <-time.After(50 * time.Millisecond):
    fmt.Println("Timeout")
}
```

### 5. Goroutine Leaks and Cancellation

Goroutine leaks happen when a goroutine blocks forever. Use `context.Context` for cancellation.

```go
func worker(ctx context.Context, jobs <-chan int) {
    for {
        select {
        case job, ok := <-jobs:
            if !ok { return }
            fmt.Println("Working:", job)
        case <-ctx.Done():
            return
        }
    }
}
```

## Practice Questions

1. What is the initial stack size of a goroutine?
2. What is the difference between a buffered and unbuffered channel?
3. How does select handle multiple ready channels?
4. What causes a goroutine leak?

## LLM Prompts for Deeper Understanding

1. "Explain goroutines: lightweight scheduling, stack size, M:N scheduling"
2. "Show channel patterns: buffered, unbuffered, range, close, direction"
3. "Teach select for multiplexing, timeouts, and cancellation with context"

## Key Takeaways

- goroutines are lightweight threads (~2KB stacks)
- channels are typed conduits; make(chan T, N) for buffered
- select multiplexes channel operations; context for cancellation