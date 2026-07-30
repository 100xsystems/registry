---
{
  "title": "Getting Started with Go",
  "description": "Install Go and set up GOPATH",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install Go and set up GOPATH",
    "Understand go mod, go build, go run",
    "Write and run your first Go program",
    "Use fmt.Println for output"
  ],
  "knowledge_refs": [
    "go/go-01-getting-started"
  ],
  "prerequisites": [],
  "references": [
    {
      "title": "Go Tutorial: Getting Started",
      "url": "https://go.dev/doc/tutorial/getting-started"
    },
    {
      "title": "Go by Example: Hello World",
      "url": "https://gobyexample.com/hello-world"
    },
    {
      "title": "Effective Go",
      "url": "https://go.dev/doc/effective_go"
    },
    {
      "title": "Go Specification",
      "url": "https://go.dev/ref/spec"
    }
  ]
}
---

# GO-01-GETTING-STARTED: Getting Started with Go

## Introduction

Go is a statically typed, compiled language designed for simplicity, performance, and concurrency. Created at Google, it powers Docker, Kubernetes, Terraform, and countless CLI tools. Its philosophy: write less, build fast, ship efficiently.

## Key Concepts

### 1. Installing Go and the Toolchain

Go is a single binary download from go.dev. The toolchain includes: go run (build+run), go build (compile), go test (run tests), go fmt (format), go mod (dependencies). GOPATH is the workspace root (default ~/go).

```go
// Install Go from https://go.dev/dl/
$ go version  # go version go1.24.0 darwin/arm64

// Hello, World!
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}

// Run: go run main.go
// Build: go build -o hello main.go
```

### 2. Module System and go.mod

Every Go project starts with go mod init. go.mod defines module name, Go version, and dependencies. go.sum locks dependency checksums. Use go get to add, go mod tidy to clean up.

```go
$ mkdir myapp && cd myapp
$ go mod init example.com/myapp

// go.mod file
module example.com/myapp

go 1.24.0

require (
    github.com/google/uuid v1.6.0
)

// Add dependencies
$ go get github.com/google/uuid
$ go mod tidy  # clean up unused
```

### 3. Package Structure and Visibility

Go programs are organized in packages. Package main is the entry point. Exported names start with a capital letter (public). Lowercase names are package-private. Use import paths based on module.

```go
package main

import (
    "fmt"
    "example.com/myapp/greeting"
)

func main() {
    fmt.Println(greeting.Hello("Alice"))
}

// greeting/greeting.go
package greeting

// Hello is exported (capital letter)
func Hello(name string) string {
    return "Hello, " + name
}

// helper is package-private (lowercase)
func helper() string { return "internal" }
```

### 4. Basic Types and Variables

Go has strong typing with type inference. Declare variables with var or := (short declaration). Basic types: bool, string, int, float64, byte, rune. Zero values: 0, "", false, nil.

```go
package main
import "fmt"

func main() {
    // Type inference with :=
    name := "Alice"           // string
    age := 30                 // int
    height := 5.8             // float64
    active := true            // bool

    // Explicit var declaration
    var count int = 42
    var message string        // zero value: ""
    var total float64         // zero value: 0.0

    // Multiple declarations
    var x, y int = 1, 2
    first, second := "a", "b"

    fmt.Printf("%s is %d years old\n", name, age)
}
```

### 5. Constants and iota

Constants are declared with const, evaluated at compile time. iota generates enumerations, resetting per const block. Untyped constants have flexible type inference.

```go
package main
import "fmt"

const Pi = 3.14159
const AppName = "MyApp"

// iota enum
const (
    StatusOK = iota  // 0
    StatusWarn      // 1
    StatusError     // 2
    StatusFatal     // 3
)

// iota with expressions
const (
    _  = iota             // 0 (discard)
    KB = 1 << (10 * iota) // 1024
    MB = 1 << (10 * iota) // 1048576
    GB = 1 << (10 * iota) // 1073741824
)

func main() {
    fmt.Println(Pi, StatusOK, MB)
}
```

## Practice Questions

1. What is the difference between go run, go build, and go install?
1. How does Go determine if a name is exported (public) or unexported (private)?
1. What is the zero value of a string? What about int and bool?
1. How does iota work? What value does the first iota constant get?

## LLM Prompts for Deeper Understanding

1. "Explain Go module system: go mod init, go mod tidy, go.sum, versioning"
1. "Show Go variable declaration forms: var, :=, const, iota"
1. "Teach Go package structure: main, exported names, import paths"

## Key Takeaways

- go run executes, go build compiles, go test runs tests
- Capitalized names are exported (public); lowercase are package-private
- Constants use const keyword; iota generates sequential enum values