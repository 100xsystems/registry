---
{
  "slug": "go-14-testing",
  "title": "Testing: testing Package and Table-Driven Tests",
  "description": "Write unit tests with testing.T, use table-driven tests, write benchmarks with testing.B, use go test flags and coverage.",
  "type": "lesson",
  "order": 14,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write unit tests with testing.T",
    "Use table-driven tests",
    "Write benchmarks with testing.B",
    "Use go test flags and coverage"
  ],
  "knowledge_refs": ["go/go-14-testing"],
  "prerequisites": ["GO-01"],
  "references": [
    {"title": "pkg.go.dev/testing", "url": "https://pkg.go.dev/testing"},
    {"title": "Go by Example: Testing", "url": "https://gobyexample.com/testing"},
    {"title": "Go Blog: Test Coverage", "url": "https://go.dev/blog/cover"},
    {"title": "Effective Go - Testing", "url": "https://go.dev/doc/effective_go#testing"}
  ]
}
---

# GO-14: Testing: testing Package and Table-Driven Tests

## Introduction

Go has a built-in testing package with support for unit tests, benchmarks, and fuzzing. Table-driven tests are the idiomatic Go pattern. `go test` runs tests, `-bench` runs benchmarks, `-cover` measures coverage. The testing package is lightweight but powerful.

## Key Concepts

### 1. Unit Tests and Test Functions

Test functions are named TestXxx(t *testing.T). Run with `go test ./...` or `go test -v`. Use t.Error for non-fatal failures, t.Fatal for fatal failures. Helper functions with t.Helper() for cleaner stack traces.

```go
package main

import "testing"

func TestAdd(t *testing.T) {
    result := Add(2, 3)
    if result != 5 {
        t.Errorf("Add(2, 3) = %d; want 5", result)
    }
}

// Helper function with t.Helper()
func assertEqual(t *testing.T, got, want int) {
    t.Helper()  // mark as helper
    if got != want {
        t.Errorf("got %d; want %d", got, want)
    }
}

func TestAddWithHelper(t *testing.T) {
    assertEqual(t, Add(2, 3), 5)
    assertEqual(t, Add(-1, 1), 0)
}

// Run: go test -v ./...
// Run single: go test -v -run TestAdd
```

### 2. Table-Driven Tests

Table-driven tests define a struct slice of test cases. Each case has name, input, expected. Subtests with t.Run(name, func(t *testing.T) {}) enable parallel execution, selective running, and independent failure reporting.

```go
package main

import "testing"

func TestDivide(t *testing.T) {
    tests := []struct {
        name    string
        a, b    int
        want    int
        wantErr bool
    }{
        {name: "positive", a: 10, b: 2, want: 5},
        {name: "by zero",  a: 1, b: 0, wantErr: true},
        {name: "negative", a: -6, b: 3, want: -2},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got, err := Divide(tt.a, tt.b)
            if tt.wantErr {
                if err == nil {
                    t.Error("expected error")
                }
                return
            }
            if got != tt.want {
                t.Errorf("got %d; want %d", got, tt.want)
            }
        })
    }
}

// Parallel subtests
func TestParallel(t *testing.T) {
    tests := []struct {
        name string
        val  int
    }{
        {name: "case1", val: 1},
        {name: "case2", val: 2},
    }
    for _, tt := range tests {
        tt := tt  // capture range variable
        t.Run(tt.name, func(t *testing.T) {
            t.Parallel()
            // test with tt.val
        })
    }
}
```

### 3. Benchmarks and Coverage

Benchmark functions are named BenchmarkXxx(b *testing.B). b.N is adjusted by the framework. Run with `-bench=. -benchmem` for allocation stats. `go test -cover` for coverage measurement.

```go
package main

import "testing"

func BenchmarkStringConcat(b *testing.B) {
    for i := 0; i < b.N; i++ {
        _ = ConcatStrings("Hello", "World")
    }
}

func BenchmarkStringBuilder(b *testing.B) {
    b.ReportAllocs()  // report allocation stats
    for i := 0; i < b.N; i++ {
        _ = BuildString("Hello", "World")
    }
}

// Reset timer before setup
func BenchmarkWithSetup(b *testing.B) {
    data := expensiveSetup()
    b.ResetTimer()  // exclude setup time

    for i := 0; i < b.N; i++ {
        process(data)
    }
}

// Run: go test -bench=. -benchmem
// Coverage: go test -cover
// go test -coverprofile=coverage.out
// go tool cover -html=coverage.out
```

### 4. Test Fixtures and Setup/Teardown

Use TestMain(m *testing.M) for per-package setup/teardown. t.Cleanup registers cleanup functions. t.TempDir creates auto-cleaned temp directories. Subtests can run in parallel with t.Parallel().

```go
package main

import (
    "os"
    "testing"
)

func TestMain(m *testing.M) {
    // Setup
    setupDB()

    // Run tests
    code := m.Run()

    // Teardown
    teardownDB()
    os.Exit(code)
}

// t.Cleanup for per-test cleanup
func TestWithFile(t *testing.T) {
    file := createTempFile(t)
    t.Cleanup(func() {
        os.Remove(file)
    })
}

// t.TempDir - auto-cleaned temp directory
func TestTempDir(t *testing.T) {
    dir := t.TempDir()  // auto-removed after test
    _ = dir
}

// Fuzzing (Go 1.18+)
func FuzzReverse(f *testing.F) {
    seeds := []string{"hello", "world", "123"}
    for _, s := range seeds {
        f.Add(s)
    }
    f.Fuzz(func(t *testing.T, s string) {
        reversed := Reverse(s)
        double := Reverse(reversed)
        if s != double {
            t.Errorf("Double reverse failed: %q -> %q -> %q", s, reversed, double)
        }
    })
}
```

### 5. Mocking and Test Doubles

Go interfaces make mocking natural. Create mock implementations for testing. Use interfaces to decouple your code. The testify library provides assert/require helpers, but the standard library is sufficient.

```go
package main

// Interface for mocking
type DataStore interface {
    Get(id string) (*User, error)
    Save(u *User) error
}

// Mock implementation
type mockStore struct {
    users map[string]*User
}

func (m *mockStore) Get(id string) (*User, error) {
    u, ok := m.users[id]
    if !ok {
        return nil, ErrNotFound
    }
    return u, nil
}

func (m *mockStore) Save(u *User) error {
    m.users[u.ID] = u
    return nil
}

func TestGetUser(t *testing.T) {
    store := &mockStore{users: map[string]*User{
        "1": {ID: "1", Name: "Alice"},
    }}

    svc := NewUserService(store)
    user, err := svc.GetUser("1")
    if err != nil {
        t.Fatal(err)
    }
    if user.Name != "Alice" {
        t.Errorf("got %s; want Alice", user.Name)
    }
}
```

## Practice Questions

1. What is the signature of a Go test function? How do you run it?
2. How do table-driven tests work with subtests? Why use t.Run?
3. What is the difference between t.Error and t.Fatal?
4. How do you run benchmarks in Go? What does b.N represent?
5. What is TestMain used for? How do you register cleanup functions?

## LLM Prompts for Deeper Understanding

1. "Explain Go testing: TestXxx, t.Error, t.Fatal, t.Helper, table-driven tests with subtests"
2. "Show benchmarks with b.N, b.ReportAllocs, b.ResetTimer, and the -benchmem flag"
3. "Teach TestMain, t.Cleanup, t.TempDir, fuzzing, and test coverage measurement"

## Key Takeaways

- Test functions: func TestXxx(t *testing.T); run with go test -v
- Table-driven tests with subtests (t.Run) are the idiomatic Go pattern
- go test -bench=. -benchmem for benchmarks; -cover for coverage
- Use interfaces for mocking; testify is optional but helpful