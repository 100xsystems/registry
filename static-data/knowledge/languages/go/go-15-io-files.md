---
{
  "slug": "go-15-io-files",
  "title": "I/O: Readers, Writers, and File Operations",
  "description": "Use io.Reader and io.Writer interfaces, work with files via os package, use bufio for buffered I/O, use io.Copy, io.MultiReader, io.TeeReader.",
  "type": "lesson",
  "order": 15,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use io.Reader and io.Writer interfaces",
    "Work with files via os package",
    "Use bufio for buffered I/O",
    "Use io.Copy, io.MultiReader, io.TeeReader"
  ],
  "knowledge_refs": ["go/go-15-io-files"],
  "prerequisites": ["GO-01"],
  "references": [
    {"title": "pkg.go.dev/io", "url": "https://pkg.go.dev/io"},
    {"title": "pkg.go.dev/os", "url": "https://pkg.go.dev/os"},
    {"title": "pkg.go.dev/bufio", "url": "https://pkg.go.dev/bufio"},
    {"title": "Go by Example: Reading Files", "url": "https://gobyexample.com/reading-files"}
  ]
}
---

# GO-15: I/O: Readers, Writers, and File Operations

## Introduction

Go's I/O model is based on the io.Reader and io.Writer interfaces. These simple interfaces compose to create powerful data pipelines. The os package handles file operations; bufio adds buffering. This composable design is one of Go's most elegant features.

## Key Concepts

### 1. io.Reader and io.Writer Interfaces

io.Reader has `Read(p []byte) (n int, err error)`. io.Writer has `Write(p []byte) (n int, err error)`. io.Closer has `Close() error`. These interfaces power all I/O in Go — files, networks, compression, encryption.

```go
package main

import (
    "fmt"
    "io"
    "strings"
)

func main() {
    r := strings.NewReader("Hello, World!")
    buf := make([]byte, 5)

    for {
        n, err := r.Read(buf)
        if err == io.EOF {
            break
        }
        fmt.Printf("Read %d bytes: %s\n", n, buf[:n])
    }

    // Custom Writer
    type LogWriter struct {
        Writer io.Writer
    }

    func (lw *LogWriter) Write(p []byte) (int, error) {
        fmt.Printf("Writing %d bytes\n", len(p))
        return lw.Writer.Write(p)
    }
}
```

### 2. File Operations with os Package

os.Open, os.Create, os.ReadFile, os.WriteFile. os.File implements Reader/Writer. Stat gets file info. os.ReadDir lists directory entries. File permissions are Unix-style octal.

```go
package main

import (
    "fmt"
    "os"
)

func main() {
    // Read entire file
    data, err := os.ReadFile("input.txt")
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    fmt.Println(string(data))

    // Write entire file
    err = os.WriteFile("output.txt", []byte("Hello"), 0644)

    // Open for reading/writing
    f, err := os.OpenFile("data.txt", os.O_RDWR|os.O_CREATE, 0644)
    defer f.Close()

    // File info
    info, _ := f.Stat()
    fmt.Println("Size:", info.Size())
    fmt.Println("Mode:", info.Mode())
    fmt.Println("ModTime:", info.ModTime())

    // Read directory (Go 1.16+)
    entries, _ := os.ReadDir(".")
    for _, entry := range entries {
        fmt.Println(entry.Name(), entry.IsDir())
    }
}
```

### 3. bufio — Buffered I/O

bufio provides buffered Readers and Writers. bufio.Scanner reads lines/words/tokens. bufio.Reader for small reads. bufio.Writer for buffered writes. Always call Flush() on buffered writers.

```go
package main

import (
    "bufio"
    "fmt"
    "os"
)

// Scanner for line-by-line reading
func readLines(filename string) ([]string, error) {
    f, err := os.Open(filename)
    if err != nil {
        return nil, err
    }
    defer f.Close()

    var lines []string
    scanner := bufio.NewScanner(f)
    for scanner.Scan() {
        lines = append(lines, scanner.Text())
    }
    return lines, scanner.Err()
}

// Buffered Writer
func writeBuffered(filename, content string) error {
    f, err := os.Create(filename)
    if err != nil {
        return err
    }
    defer f.Close()

    w := bufio.NewWriter(f)
    w.WriteString(content)
    return w.Flush()  // important: flush buffer to file
}

// Custom scanner split function
func scanWords(data []byte, atEOF bool) (advance int, token []byte, err error) {
    // skip leading spaces
    start := 0
    for start < len(data) && data[start] == ' ' {
        start++
    }
    // scan until next space
    for i := start; i < len(data); i++ {
        if data[i] == ' ' {
            return i, data[start:i], nil
        }
    }
    if atEOF && len(data) > start {
        return len(data), data[start:], nil
    }
    return start, nil, nil
}
```

### 4. io Composition: Copy, MultiReader, TeeReader

io.Copy streams from Reader to Writer. io.MultiReader chains readers. io.TeeReader duplicates reads to a Writer. io.LimitReader limits bytes read. io.Pipe for in-memory streaming.

```go
package main

import (
    "bytes"
    "fmt"
    "io"
    "os"
    "strings"
)

func main() {
    // io.Copy — stream from reader to writer
    r := strings.NewReader("Hello, World!")
    n, err := io.Copy(os.Stdout, r)
    fmt.Printf("\nCopied %d bytes\n", n)

    // io.MultiReader — chain readers
    r1 := strings.NewReader("Hello, ")
    r2 := strings.NewReader("World!")
    combined := io.MultiReader(r1, r2)
    io.Copy(os.Stdout, combined)

    // io.TeeReader — duplicate reads
    var buf bytes.Buffer
    src := strings.NewReader("Data")
    tee := io.TeeReader(src, &buf)
    io.Copy(os.Stdout, tee)  // prints "Data"
    fmt.Println(buf.String())  // also "Data"

    // io.LimitReader — limit bytes read
    limited := io.LimitReader(strings.NewReader("Hello World"), 5)
    io.Copy(os.Stdout, limited)  // prints "Hello"
}
```

### 5. Compression and Encoding with io

The io interfaces compose with compression, encryption, and encoding packages. gzip, zlib, base64 all implement Reader/Writer patterns.

```go
package main

import (
    "bytes"
    "compress/gzip"
    "encoding/base64"
    "fmt"
    "io"
    "os"
)

// Gzip compression
func compress(data []byte) (*bytes.Buffer, error) {
    var buf bytes.Buffer
    w := gzip.NewWriter(&buf)
    _, err := w.Write(data)
    if err != nil {
        return nil, err
    }
    w.Close()
    return &buf, nil
}

func decompress(r io.Reader) ([]byte, error) {
    gr, err := gzip.NewReader(r)
    if err != nil {
        return nil, err
    }
    defer gr.Close()
    return io.ReadAll(gr)
}

// Base64 encoding
func encodeBase64(r io.Reader) string {
    encoded := &bytes.Buffer{}
    encoder := base64.NewEncoder(base64.StdEncoding, encoded)
    io.Copy(encoder, r)
    encoder.Close()
    return encoded.String()
}

// io.Pipe for in-memory streaming
func pipeExample() {
    pr, pw := io.Pipe()
    go func() {
        defer pw.Close()
        json.NewEncoder(pw).Encode(map[string]string{"key": "value"})
    }()
    io.Copy(os.Stdout, pr)  // prints JSON
}
```

## Practice Questions

1. What is the signature of io.Reader.Read? What signals EOF?
2. What is the difference between os.ReadFile and os.Open? When would you use each?
3. Why must you call Flush() on a bufio.Writer? What happens if you don't?
4. What does io.Copy do? How does it use Reader and Writer?
5. How do io.MultiReader and io.TeeReader differ?

## LLM Prompts for Deeper Understanding

1. "Explain io.Reader and io.Writer interfaces with composition patterns and examples"
2. "Show file operations: os.ReadFile, os.WriteFile, os.Open, os.OpenFile, os.ReadDir"
3. "Teach io.Copy, MultiReader, TeeReader, PipeReader, LimitReader, and compression wrappers"

## Key Takeaways

- io.Reader and io.Writer are the foundation of all I/O in Go
- bufio.Scanner for line-by-line reading; bufio.Writer.Flush() required
- io.Copy streams from any Reader to any Writer
- io interfaces compose with compression, encryption, and encoding packages