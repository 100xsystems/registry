---
{
  "slug": "go-16-json-encoding",
  "title": "JSON, Encoding, and Serialization",
  "description": "Marshal and unmarshal JSON with encoding/json, use struct tags for JSON field mapping, write custom JSON marshalers/unmarshalers, serialize other formats.",
  "type": "lesson",
  "order": 16,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Marshal and unmarshal JSON with encoding/json",
    "Use struct tags for JSON field mapping",
    "Write custom JSON marshalers/unmarshalers",
    "Serialize other formats: XML, CSV, YAML"
  ],
  "knowledge_refs": ["go/go-16-json-encoding"],
  "prerequisites": ["GO-01"],
  "references": [
    {"title": "pkg.go.dev/encoding/json", "url": "https://pkg.go.dev/encoding/json"},
    {"title": "Go by Example: JSON", "url": "https://gobyexample.com/json"},
    {"title": "Go Blog: JSON and Go", "url": "https://go.dev/blog/json"},
    {"title": "Go by Example: XML", "url": "https://gobyexample.com/xml"}
  ]
}
---

# GO-16: JSON, Encoding, and Serialization

## Introduction

encoding/json provides JSON marshal/unmarshal with struct tags. The encoder/decoder interfaces support streaming JSON from Readers/Writers. Other encoding packages: encoding/xml, encoding/csv, encoding/base64. Go's JSON handling is fast, safe, and well-integrated.

## Key Concepts

### 1. Marshal and Unmarshal

json.Marshal serializes to []byte. json.Unmarshal deserializes. Only exported fields (capitalized) are marshaled. Use json.MarshalIndent for pretty-printed output. Struct tags control field names, omitempty, and skipping.

```go
package main

import (
    "encoding/json"
    "fmt"
)

type User struct {
    Name  string `json:"name"`
    Age   int    `json:"age"`
    Email string `json:"email,omitempty"`
    Role  string `json:"-"`  // skip this field
}

func main() {
    u := User{Name: "Alice", Age: 30, Email: "a@b.com", Role: "admin"}

    // Marshal (serialize)
    jsonData, _ := json.Marshal(u)
    fmt.Println(string(jsonData))  // {"name":"Alice","age":30,"email":"a@b.com"}

    // Pretty print
    pretty, _ := json.MarshalIndent(u, "", "  ")
    fmt.Println(string(pretty))

    // Unmarshal (deserialize)
    var u2 User
    json.Unmarshal(jsonData, &u2)
    fmt.Println(u2.Name)  // Alice
}
```

### 2. Streaming JSON: Encoder/Decoder

json.NewEncoder writes JSON to a Writer. json.NewDecoder reads JSON from a Reader. Use for streaming large JSON or files. Decoder.DisallowUnknownFields() for strict parsing.

```go
package main

import (
    "encoding/json"
    "fmt"
    "io"
    "os"
)

func writeJSON(filename string, data interface{}) error {
    f, err := os.Create(filename)
    if err != nil {
        return err
    }
    defer f.Close()

    encoder := json.NewEncoder(f)
    encoder.SetIndent("", "  ")
    return encoder.Encode(data)
}

func readJSON(filename string, result interface{}) error {
    f, err := os.Open(filename)
    if err != nil {
        return err
    }
    defer f.Close()

    decoder := json.NewDecoder(f)
    return decoder.Decode(result)
}

// Decode multiple JSON objects from stream (NDJSON)
func readJSONLines(r io.Reader) ([]User, error) {
    var users []User
    decoder := json.NewDecoder(r)
    for {
        var u User
        if err := decoder.Decode(&u); err == io.EOF {
            break
        } else if err != nil {
            return nil, err
        }
        users = append(users, u)
    }
    return users, nil
}
```

### 3. Custom Marshal/Unmarshal and RawMessage

Implement json.Marshaler and json.Unmarshaler for custom types. json.RawMessage for deferred decoding. Use json.RawMessage to handle dynamic JSON fields.

```go
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

// Custom time format
type CustomTime struct {
    time.Time
}

func (ct CustomTime) MarshalJSON() ([]byte, error) {
    return json.Marshal(ct.Format("2006-01-02"))
}

func (ct *CustomTime) UnmarshalJSON(data []byte) error {
    var s string
    if err := json.Unmarshal(data, &s); err != nil {
        return err
    }
    t, err := time.Parse("2006-01-02", s)
    if err != nil {
        return err
    }
    ct.Time = t
    return nil
}

// RawMessage for dynamic fields
type FlexibleResponse struct {
    Status string          `json:"status"`
    Data   json.RawMessage `json:"data"`  // deferred decode
}

func processResponse(resp FlexibleResponse) {
    if resp.Status == "ok" {
        var users []User
        json.Unmarshal(resp.Data, &users)
        // or
        var metadata map[string]interface{}
        json.Unmarshal(resp.Data, &metadata)
    }
}
```

### 4. Other Encodings: XML, CSV, base64

encoding/xml, encoding/csv, encoding/base64 follow similar patterns. Each has marshal/unmarshal for their format. csv.NewReader/NewWriter for CSV files. base64.StdEncoding for base64 strings.

```go
package main

import (
    "encoding/csv"
    "encoding/json"
    "fmt"
    "os"
)

func readCSV(filename string) ([]map[string]string, error) {
    f, err := os.Open(filename)
    if err != nil {
        return nil, err
    }
    defer f.Close()

    reader := csv.NewReader(f)
    records, err := reader.ReadAll()
    if err != nil {
        return nil, err
    }

    headers := records[0]
    var result []map[string]string
    for _, row := range records[1:] {
        m := make(map[string]string)
        for i, h := range headers {
            m[h] = row[i]
        }
        result = append(result, m)
    }
    return result, nil
}

// YAML via external package
// import "gopkg.in/yaml.v3"
// yaml.Marshal(data) and yaml.Unmarshal(data, &target)
```

### 5. JSON Validation and Error Handling

JSON errors can be detailed. Check for syntax errors, type mismatches, and unknown fields. Use json.Valid to check if data is valid JSON before parsing.

```go
package main

import (
    "encoding/json"
    "fmt"
    "strings"
)

func safeUnmarshal(data []byte, target interface{}) error {
    decoder := json.NewDecoder(strings.NewReader(string(data)))
    decoder.DisallowUnknownFields()  // reject unknown fields

    if err := decoder.Decode(target); err != nil {
        // Check for specific error types
        switch e := err.(type) {
        case *json.SyntaxError:
            return fmt.Errorf("syntax error at offset %d: %w", e.Offset, e)
        case *json.UnmarshalTypeError:
            return fmt.Errorf("type mismatch at field %s: want %s got %s",
                e.Field, e.Type.String(), e.Value)
        default:
            return err
        }
    }
    // Check for trailing data
    if decoder.More() {
        return fmt.Errorf("unexpected trailing data")
    }
    return nil
}

func main() {
    // Validate JSON
    valid := json.Valid([]byte(`{"name":"Alice"}`))
    fmt.Println("Valid JSON:", valid)  // true
}
```

## Practice Questions

1. What struct tags does encoding/json recognize? What does omitempty do?
2. What is the difference between json.Marshal and json.NewEncoder?
3. How do you handle unknown/dynamic JSON fields?
4. How do you implement a custom JSON marshaler?
5. What does DisallowUnknownFields do? When would you use it?

## LLM Prompts for Deeper Understanding

1. "Explain JSON marshaling: struct tags, omitempty, MarshalJSON, UnmarshalJSON, RawMessage"
2. "Show streaming JSON with Encoder/Decoder for large files and NDJSON"
3. "Teach other encodings: XML, CSV, base64, YAML, and custom serialization interfaces"

## Key Takeaways

- Use json.Marshal/Unmarshal for []byte; Encoder/Decoder for streams
- Struct tags control JSON field names, omitempty, and skipping (-)
- json.RawMessage defers decoding for dynamic fields
- Other encodings (XML, CSV, base64) follow similar patterns