---
{
  "slug": "go-20-cli-tools",
  "title": "Building CLI Tools with flag and cobra",
  "description": "Use flag package for command-line flags, use cobra for complex CLI applications, handle os.Args and subcommands, build and cross-compile executables.",
  "type": "lesson",
  "order": 20,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use flag package for command-line flags",
    "Use cobra for complex CLI applications",
    "Handle os.Args and subcommands",
    "Build and cross-compile executables"
  ],
  "knowledge_refs": ["go/go-20-cli-tools"],
  "prerequisites": ["GO-01"],
  "references": [
    {"title": "pkg.go.dev/flag", "url": "https://pkg.go.dev/flag"},
    {"title": "Cobra Library", "url": "https://github.com/spf13/cobra"},
    {"title": "Go by Example: Command-Line Flags", "url": "https://gobyexample.com/command-line-flags"},
    {"title": "Go Blog: Cross Compilation", "url": "https://go.dev/doc/install/source#environment"}
  ]
}
---

# GO-20: Building CLI Tools with flag and cobra

## Introduction

Go is the language of choice for CLI tools (Docker, Kubernetes, Hugo, Terraform). The standard flag package handles simple flags. Cobra provides subcommands, help, and shell completion. Cross-compilation is built-in: `GOOS=linux GOARCH=amd64 go build`.

## Key Concepts

### 1. flag Package — Simple Flags

flag.String, flag.Int, flag.Bool declare flags. flag.Parse() parses os.Args. Flag types: -name, -n, --name. Use flag.Usage for custom help. Non-flag args via flag.Args().

```go
package main

import (
    "flag"
    "fmt"
)

func main() {
    name := flag.String("name", "World", "name to greet")
    count := flag.Int("count", 1, "number of times")
    verbose := flag.Bool("verbose", false, "verbose output")

    flag.Parse()

    args := flag.Args()
    fmt.Println("Extra args:", args)

    for i := 0; i < *count; i++ {
        if *verbose {
            fmt.Printf("Greeting %d of %d\n", i+1, *count)
        }
        fmt.Printf("Hello, %s!\n", *name)
    }
}

// Run: go run main.go -name=Alice -count=3 -verbose extra
```

### 2. Cobra — Advanced CLI Framework

Cobra provides commands, subcommands, flags, help, and shell completion. The root command has subcommands. Each command has a Run function. Persistent flags are available to all subcommands. Local flags are command-specific.

```go
package main

import (
    "fmt"
    "os"
    "github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{
    Use:   "app",
    Short: "App is a CLI tool",
    Run: func(cmd *cobra.Command, args []string) {
        fmt.Println("Hello from root command")
    },
}

var greetCmd = &cobra.Command{
    Use:   "greet [name]",
    Short: "Greet someone",
    Args:  cobra.MinimumNArgs(1),
    Run: func(cmd *cobra.Command, args []string) {
        name := args[0]
        uppercase, _ := cmd.Flags().GetBool("uppercase")
        if uppercase {
            name = strings.ToUpper(name)
        }
        fmt.Printf("Hello, %s!\n", name)
    },
}

func init() {
    rootCmd.AddCommand(greetCmd)
    greetCmd.Flags().BoolP("uppercase", "u", false, "uppercase output")
}

func main() {
    if err := rootCmd.Execute(); err != nil {
        fmt.Println(err)
        os.Exit(1)
    }
}
```

### 3. Environment Variables and Configuration

Use os.Getenv for environment variables. Combine with flags for flexible configuration. The standard pattern: flags override env vars override defaults. Use viper for advanced config management.

```go
package main

import (
    "flag"
    "fmt"
    "os"
)

type Config struct {
    Port    int
    DBHost  string
    DBPort  int
    Verbose bool
}

func getConfig() Config {
    cfg := Config{
        Port:    8080,       // default
        DBHost:  "localhost",
        DBPort:  5432,
        Verbose: false,
    }

    // Env vars override defaults
    if v := os.Getenv("PORT"); v != "" {
        cfg.Port, _ = strconv.Atoi(v)
    }
    if v := os.Getenv("DB_HOST"); v != "" {
        cfg.DBHost = v
    }

    // Flags override env vars
    flag.IntVar(&cfg.Port, "port", cfg.Port, "server port")
    flag.StringVar(&cfg.DBHost, "db-host", cfg.DBHost, "database host")
    flag.BoolVar(&cfg.Verbose, "verbose", cfg.Verbose, "verbose output")
    flag.Parse()

    return cfg
}
```

### 4. Cross-Compilation and Distribution

Go's cross-compilation is built-in. Set GOOS and GOARCH for different platforms. Use go build -ldflags to embed version info. CGO_ENABLED=0 for static binaries. Use GoReleaser for automated releases.

```go
// Cross-compile
$ GOOS=linux GOARCH=amd64 go build -o app-linux
$ GOOS=darwin GOARCH=amd64 go build -o app-macos
$ GOOS=windows GOARCH=amd64 go build -o app.exe

// With version info
$ go build -ldflags="-X main.Version=1.0.0 -X main.Commit=$(git rev-parse HEAD)"

// Static binary (no libc dependency)
$ CGO_ENABLED=0 go build -o app

// Build for ARM (Raspberry Pi)
$ GOOS=linux GOARCH=arm GOARM=6 go build -o app-arm

// Inside code
var (
    Version = "dev"
    Commit  = "none"
    Date    = "unknown"
)

func main() {
    fmt.Printf("Version: %s, Commit: %s, Built: %s\n", Version, Commit, Date)
}
```

### 5. CLI Best Practices: Help, Colors, Exit Codes

Good CLI tools have clear help, consistent exit codes, and progress indicators. Use os.Exit(1) for errors, 0 for success. Use ANSI colors sparingly. Check IsTerminal for color output. Use signal handling for cleanup.

```go
package main

import (
    "fmt"
    "os"
    "os/signal"
    "syscall"
    "golang.org/x/term"
)

func main() {
    // Exit codes
    if err := run(); err != nil {
        fmt.Fprintf(os.Stderr, "Error: %v\n", err)
        os.Exit(1)
    }
    os.Exit(0)
}

func isTerminal() bool {
    return term.IsTerminal(int(os.Stdout.Fd()))
}

// Color output (only in terminal)
func colorize(s string, color string) string {
    if !isTerminal() {
        return s
    }
    return color + s + "\033[0m"
}

// Graceful shutdown
func setupSignalHandler() {
    sig := make(chan os.Signal, 1)
    signal.Notify(sig, syscall.SIGINT, syscall.SIGTERM)
    go func() {
        <-sig
        fmt.Println("\nShutting down...")
        cleanup()
        os.Exit(0)
    }()
}
```

## Practice Questions

1. How do you declare a string flag with the flag package? A boolean flag?
2. What is the difference between persistent flags and local flags in Cobra?
3. How do you cross-compile a Go binary for Linux on macOS?
4. What is the standard pattern for combining flags and environment variables?
5. What exit code should a CLI tool use for errors?

## LLM Prompts for Deeper Understanding

1. "Explain flag package: flag.String, flag.Int, flag.Bool, flag.Parse, flag.Args"
2. "Show Cobra: root command, subcommands, persistent flags, Run, Args validation"
3. "Teach cross-compilation: GOOS, GOARCH, CGO_ENABLED, ldflags, static builds"

## Key Takeaways

- flag package for simple flags; Cobra for complex CLI with subcommands
- Flags override env vars override defaults pattern
- Cross-compilation: GOOS=linux GOARCH=amd64 go build
- Use os.Exit(1) for errors, os.Exit(0) for success