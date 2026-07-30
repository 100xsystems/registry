---
{
  "slug": "go-19-modules-packages",
  "title": "Modules, Packages, and Dependency Management",
  "description": "Create and publish Go modules, manage versions with go mod and semantic versioning, use workspaces for multi-module projects, vendor dependencies.",
  "type": "lesson",
  "order": 19,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create and publish Go modules",
    "Manage versions with go mod and semantic versioning",
    "Use workspaces for multi-module projects",
    "Vendor dependencies"
  ],
  "knowledge_refs": ["go/go-19-modules-packages"],
  "prerequisites": ["GO-01"],
  "references": [
    {"title": "Go Modules Reference", "url": "https://go.dev/doc/modules/managing-dependencies"},
    {"title": "Go Blog: Module Mirror", "url": "https://go.dev/blog/module-mirror"},
    {"title": "Go Blog: Module Versioning", "url": "https://go.dev/blog/module-compatibility"},
    {"title": "Go Workspaces", "url": "https://go.dev/doc/tutorial/workspaces"}
  ]
}
---

# GO-19: Modules, Packages, and Dependency Management

## Introduction

Go modules are the standard dependency management system. go.mod defines the module and dependencies. Semantic import versioning ensures compatibility. The Go module proxy and checksum database provide reliable, secure dependency resolution.

## Key Concepts

### 1. Module Creation and Publishing

go mod init creates a module. Package paths are derived from the module path. Go uses semantic versioning (v1.2.3). Tag releases with git tags. Publish by pushing to VCS (GitHub, etc.). The module path typically matches the repository URL.

```go
// Creating a module
$ mkdir mylib && cd mylib
$ go mod init github.com/100xsystems/mylib

// go.mod
module github.com/100xsystems/mylib

go 1.24.0

// Exported function (capital letter)
// hello.go
package mylib

func Hello(name string) string {
    return "Hello, " + name
}

// Tag and publish
$ git tag v1.0.0
$ git push origin v1.0.0
```

### 2. Version Management

go get adds/updates dependencies. @latest, @v1.2.3, @commit. go mod tidy removes unused dependencies. go mod verify checks checksums. go.sum locks dependency hashes. Direct and indirect dependencies are tracked.

```go
// Add dependencies
$ go get github.com/google/uuid@latest
$ go get github.com/google/uuid@v1.6.0  // specific version
$ go get github.com/google/uuid@abc123  // commit hash

// Maintenance
$ go mod tidy   // add missing, remove unused
$ go mod verify // verify checksums

// Local development
// go.mod
replace github.com/100xsystems/mylib => ../mylib-local

// Exclude a version
// go.mod
exclude github.com/old/lib v1.0.0

// Retract a version (v1.0.0 has a bug)
// go.mod
retract v1.0.0  // Go will warn users not to use this version
```

### 3. Workspaces (Go 1.18+)

Workspaces let you develop multiple modules locally without replace directives. go work init creates a workspace. go work use adds local modules. go.work file coordinates all modules. Run build/test commands from the workspace root.

```go
// Create workspace
$ mkdir workspace && cd workspace
$ go work init ./module-a ./module-b

// go.work
go 1.24.0

use (
    ./module-a
    ./module-b
)

replace (
    example.com/mylib => ./local-mylib
)

// Workspace commands
$ go build ./...
$ go test ./...
$ go work use ./new-module  // add another module
$ go work edit -dropuse ./old-module  // remove a module
```

### 4. Internal Packages and Best Practices

internal packages are only importable by sibling packages. Avoid init() in libraries. Use semantic versioning tags. Keep backwards compatibility within major versions. Use v2, v3, etc. for breaking changes.

```go
// Internal package — only accessible within module
// myapp/internal/auth/
// Only myapp packages can import internal/auth

import "myapp/internal/auth"  // OK
import "other/internal/auth"  // ERROR: not accessible

// Best practices
// 1. Use semantic versioning (v1.2.3)
// 2. Maintain backward compatibility within major version
// 3. Run go mod tidy before committing
// 4. Pin dependencies with go.sum
// 5. Use go mod vendor for reproducible builds
// 6. Avoid init() functions in library packages
// 7. Use internal packages to hide implementation details

// Breaking changes = new major version
// module github.com/user/mod/v2
// import "github.com/user/mod/v2"
```

### 5. Module Proxy and Checksum Database

Go uses a module proxy (default: proxy.golang.org) for faster, reliable downloads. The checksum database (sum.golang.org) ensures module integrity. GONOSUMCHECK bypasses the database for private modules. GOPRIVATE controls proxy behavior.

```go
// Environment variables
// GOPROXY=https://proxy.golang.org,direct  // default
// GONOSUMCHECK=github.com/private/*        // skip checksum for private modules
// GOPRIVATE=github.com/private/*           // skip proxy and checksum
// GOFLAGS=-mod=vendor                      // use vendor directory

// Vendoring
$ go mod vendor  // copies dependencies to vendor/
$ go build -mod=vendor  // build from vendor/

// Private modules
$ go env -w GOPRIVATE=github.com/mycompany/*
$ go env -w GONOSUMCHECK=github.com/mycompany/*
```

## Practice Questions

1. What does go mod init do? What does go mod tidy do?
2. How do you add a specific version of a dependency?
3. What is the difference between go mod tidy and go mod verify?
4. What are Go workspaces used for? How do they differ from replace directives?
5. What is an internal package? How does it restrict imports?

## LLM Prompts for Deeper Understanding

1. "Explain Go module system: go.mod, go.sum, versioning, publishing, semantic import versioning"
2. "Show workspaces for multi-module local development vs replace directives"
3. "Teach internal packages, vendor, module proxy, checksum database, and private modules"

## Key Takeaways

- go mod init creates modules; go get adds dependencies
- Semantic versioning (v1.2.3) with git tags for releases
- Workspaces (Go 1.18+) manage multiple local modules without replace
- internal packages are only accessible by sibling packages
- Use go mod vendor for reproducible builds