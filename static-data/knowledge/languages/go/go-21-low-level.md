---
{
  "slug": "go-21-low-level",
  "title": "Low-Level Programming, unsafe, and CGo",
  "description": "Use the unsafe package for low-level memory manipulation, call C code with cgo, understand Go's memory model and garbage collector, perform system calls.",
  "type": "lesson",
  "order": 21,
  "duration": "75 min",
  "difficulty": "expert",
  "learning_objectives": [
    "Use unsafe package for low-level memory operations",
    "Call C code with cgo",
    "Understand Go's memory model and GC",
    "Perform system calls"
  ],
  "knowledge_refs": ["go/go-21-low-level"],
  "prerequisites": ["GO-08"],
  "references": [
    {"title": "pkg.go.dev/unsafe", "url": "https://pkg.go.dev/unsafe"},
    {"title": "pkg.go.dev/cgo", "url": "https://pkg.go.dev/cmd/cgo"},
    {"title": "Go Blog: Go Memory Model", "url": "https://go.dev/ref/mem"},
    {"title": "Go Blog: GC", "url": "https://go.dev/blog/gc-guide"}
  ]
}
---

# GO-21: Low-Level Programming, unsafe, and CGo

## Introduction

Go provides high-level abstractions, but low-level access is available through the unsafe package, cgo for C interop, and direct system calls. These are advanced techniques for performance-critical code, hardware interaction, and system programming.

## Key Concepts

### 1. unsafe Package: Pointer Arithmetic

unsafe.Pointer allows conversion between different pointer types. uintptr is an integer representation of a pointer. Use with extreme caution: the GC doesn't track uintptr values. The pointer safety rules protect against memory corruption.

```go
package main

import (
    "fmt"
    "unsafe"
)

func main() {
    var x int64 = 42
    p := unsafe.Pointer(&x)

    // Convert to different pointer type
    var b *byte = (*byte)(p)
    fmt.Println("First byte:", *b)

    // Pointer arithmetic
    p = unsafe.Pointer(uintptr(p) + unsafe.Sizeof(byte(0)))
    var b2 *byte = (*byte)(p)
    fmt.Println("Second byte:", *b2)

    // Size of types
    fmt.Println("int64 size:", unsafe.Sizeof(int64(0)))
    fmt.Println("string size:", unsafe.Sizeof(""))
    fmt.Println("struct size:", unsafe.Sizeof(User{}))
    fmt.Println("slice size:", unsafe.Sizeof([]byte{}))

    // Offset of struct fields
    type T struct {
        a byte  // offset 0
        b int64 // offset 8 (aligned)
        c byte  // offset 16
    }
    fmt.Println("T size:", unsafe.Sizeof(T{}))
    fmt.Println("T.b offset:", unsafe.Offsetof(T{}.b))
}
```

### 2. CGo — Calling C from Go

cgo allows Go programs to call C code. Use `import "C"` with a special comment. Cgo is not free — it has overhead. Build with CGO_ENABLED=1. Use for system libraries, performance-critical code, or legacy C code.

```go
// #include <stdio.h>
// #include <stdlib.h>
// #include <string.h>
//
// void hello(const char* name) {
//     printf("Hello, %s!\n", name);
// }
//
// int add(int a, int b) {
//     return a + b;
// }
import "C"

import (
    "fmt"
    "unsafe"
)

func main() {
    // Call C function
    C.hello(C.CString("World"))
    sum := C.add(1, 2)
    fmt.Println("Sum:", sum)

    // C string to Go string
    cStr := C.CString("Hello")
    defer C.free(unsafe.Pointer(cStr))
    goStr := C.GoString(cStr)
    fmt.Println(goStr)

    // Go string to C string (NUL-terminated)
    msg := "Go string"
    cMsg := C.CString(msg)
    defer C.free(unsafe.Pointer(cMsg))
    C.hello(cMsg)
}

// Build: CGO_ENABLED=1 go build
// Cross-compile with C requires cross-compiler toolchain
```

### 3. Go Memory Model and GC

Go uses a concurrent, tri-color, mark-sweep garbage collector. The GC runs concurrently with the program. GC pauses are typically <1ms. The memory model defines happens-before relationships for concurrent operations.

```go
package main

import (
    "fmt"
    "runtime"
    "runtime/debug"
    "time"
)

func main() {
    // GC configuration
    debug.SetGCPercent(100)  // default: trigger when heap grows 100%
    debug.SetMemoryLimit(1 * 1024 * 1024 * 1024)  // 1GB soft limit

    // Force GC
    runtime.GC()

    // GC stats
    var stats debug.GCStats
    debug.ReadGCStats(&stats)
    fmt.Printf("GC runs: %d, pause: %v\n", stats.NumGC, stats.Pause[0])

    // Memory stats
    var m runtime.MemStats
    runtime.ReadMemStats(&m)
    fmt.Printf("Alloc: %d MiB, TotalAlloc: %d MiB, Sys: %d MiB\n",
        m.Alloc/1024/1024, m.TotalAlloc/1024/1024, m.Sys/1024/1024)
    fmt.Printf("Heap: %d MiB, Stack: %d MiB, GC: %d\n",
        m.HeapAlloc/1024/1024, m.StackInuse/1024/1024, m.NumGC)

    // Escape analysis: variables that escape to heap
    // go build -gcflags=-m
    // Variables that can't be stack-allocated go to heap
}
```

### 4. System Calls and OS Interaction

Go's syscall package provides low-level OS interface. Use golang.org/x/sys for platform-specific functionality. Direct syscalls are faster than cgo but platform-specific. The os package wraps syscalls for portability.

```go
package main

import (
    "fmt"
    "golang.org/x/sys/unix"
    "os"
    "syscall"
)

func main() {
    // Direct syscall (Linux)
    fd, err := syscall.Open("file.txt", syscall.O_RDONLY, 0)
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    defer syscall.Close(fd)

    // Using golang.org/x/sys/unix (Linux)
    var stat unix.Stat_t
    if err := unix.Stat("file.txt", &stat); err != nil {
        fmt.Println("Error:", err)
        return
    }
    fmt.Printf("Inode: %d, Size: %d, Permissions: %o\n",
        stat.Ino, stat.Size, stat.Mode)

    // Epoll (Linux) for efficient I/O
    epfd, _ := unix.EpollCreate1(0)
    event := &unix.EpollEvent{
        Events: unix.EPOLLIN,
        Fd:     int32(fd),
    }
    unix.EpollCtl(epfd, unix.EPOLL_CTL_ADD, fd, event)

    // Signal handling
    sigs := make(chan os.Signal, 1)
    signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)
    go func() {
        <-sigs
        cleanup()
        os.Exit(0)
    }()
}
```

### 5. Profiling and Optimization

Use pprof for CPU and memory profiling. The testing package has built-in benchmarking. Use go test -bench and go test -cpuprofile. The runtime/pprof package enables programmatic profiling.

```go
package main

import (
    "os"
    "runtime/pprof"
    "runtime/trace"
)

func main() {
    // CPU profiling
    cpuFile, _ := os.Create("cpu.prof")
    defer cpuFile.Close()
    pprof.StartCPUProfile(cpuFile)
    defer pprof.StopCPUProfile()

    // Memory profiling
    memFile, _ := os.Create("mem.prof")
    defer memFile.Close()
    pprof.WriteHeapProfile(memFile)

    // Trace (for goroutine scheduling analysis)
    traceFile, _ := os.Create("trace.out")
    defer traceFile.Close()
    trace.Start(traceFile)
    defer trace.Stop()

    // Run your program
    doWork()

    // Analyze: go tool pprof cpu.prof
    // Analyze: go tool trace trace.out
    // Web UI: go tool pprof -http=:8080 cpu.prof
}

// Optimization techniques
// 1. Use sync.Pool for temporary objects
// 2. Pre-allocate slices with make([]T, 0, capacity)
// 3. Use strings.Builder instead of string concatenation
// 4. Avoid defer in hot paths
// 5. Use array instead of slice for small fixed-size collections
// 6. Use go test -bench=. -benchmem for benchmarks
// 7. Use go build -gcflags=-m for escape analysis
```

## Practice Questions

1. What is the difference between unsafe.Pointer and uintptr?
2. What are the overheads of cgo? When should you use it?
3. How does Go's garbage collector work? What is the typical pause time?
4. What is the relationship between syscall and golang.org/x/sys?
5. How do you profile CPU and memory usage in a Go program?

## LLM Prompts for Deeper Understanding

1. "Explain unsafe package: unsafe.Pointer, uintptr, Sizeof, Offsetof, pointer safety rules"
2. "Show cgo: import C, C.CString, C.GoString, calling C functions, freeing memory"
3. "Teach Go memory model, GC, profiling with pprof, escape analysis, optimization"

## Key Takeaways

- unsafe.Pointer enables low-level memory access; use with extreme caution
- cgo calls C from Go but has overhead; use for system libraries
- Go's GC is concurrent with sub-millisecond pauses
- Profiling with pprof is essential for performance optimization
- Prefer the os package over direct syscalls for portability