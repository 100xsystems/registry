---
{
  "slug": "go-18-reflection-generics",
  "title": "Reflection and Generics (Go 1.18+)",
  "description": "Use reflect package for runtime type inspection, write generic functions with type parameters, use constraints for type bounds, understand type inference and instantiation.",
  "type": "lesson",
  "order": 18,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use reflect package for runtime type inspection",
    "Write generic functions with type parameters",
    "Use constraints for type bounds",
    "Understand type inference and instantiation"
  ],
  "knowledge_refs": ["go/go-18-reflection-generics"],
  "prerequisites": ["GO-04"],
  "references": [
    {"title": "pkg.go.dev/reflect", "url": "https://pkg.go.dev/reflect"},
    {"title": "Go by Example: Generics", "url": "https://gobyexample.com/generics"},
    {"title": "Go Blog: Generics", "url": "https://go.dev/blog/generics"},
    {"title": "Go 1.18 Release Notes", "url": "https://go.dev/doc/go1.18"}
  ]
}
---

# GO-18: Reflection and Generics (Go 1.18+)

## Introduction

Reflection (reflect) inspects types at runtime. Generics (Go 1.18+) enable polymorphic functions and types. Generics are preferred over reflection for type-safe, performant code. Reflection is for special cases like JSON encoding, ORMs, and serialization.

## Key Concepts

### 1. Reflection Basics: Type and Value

reflect.TypeOf(v) returns the type. reflect.ValueOf(v) returns the value. Kind returns the underlying kind (struct, slice, etc.). Use reflect.Indirect to dereference pointers. NumField and Field for struct field iteration.

```go
package main

import (
    "fmt"
    "reflect"
)

func inspect(v interface{}) {
    t := reflect.TypeOf(v)
    val := reflect.ValueOf(v)

    fmt.Println("Type:", t.Name())
    fmt.Println("Kind:", t.Kind())
    fmt.Println("Value:", val.Interface())

    // Dereference pointer
    if t.Kind() == reflect.Ptr {
        val = reflect.Indirect(val)
        t = val.Type()
    }

    // Iterate struct fields
    if t.Kind() == reflect.Struct {
        for i := 0; i < t.NumField(); i++ {
            field := t.Field(i)
            fmt.Printf("  %s: %v (tag: %s)\n", field.Name,
                val.Field(i), field.Tag.Get("json"))
        }
    }
}

func main() {
    inspect(User{Name: "Alice", Age: 30})
}
```

### 2. Modifying Values with Reflection

Use reflect.Value.Elem() to get the element a pointer points to. Call SetInt, SetString, SetField to modify values. CanAddr checks if the value is addressable. Panics if not addressable.

```go
package main

import (
    "fmt"
    "reflect"
)

func setField(obj interface{}, name string, value interface{}) {
    val := reflect.ValueOf(obj)
    if val.Kind() != reflect.Ptr {
        fmt.Println("must be pointer to modify")
        return
    }

    elem := val.Elem()
    field := elem.FieldByName(name)
    if !field.IsValid() {
        fmt.Println("field not found:", name)
        return
    }

    if field.CanSet() {
        switch field.Kind() {
        case reflect.String:
            field.SetString(value.(string))
        case reflect.Int, reflect.Int64:
            field.SetInt(int64(value.(int)))
        case reflect.Float64:
            field.SetFloat(value.(float64))
        case reflect.Bool:
            field.SetBool(value.(bool))
        }
    }
}

u := &User{}
setField(u, "Name", "Alice")
fmt.Println(u.Name)  // Alice
```

### 3. Generics: Type Parameters

Generic functions use `[T any]` syntax. Type parameters go before function parameters. Multiple type parameters: `[T, U any]`. Type inference from arguments. The `comparable` built-in constraint allows == and !=.

```go
package main

import "fmt"

// Generic function
func Identity[T any](value T) T {
    return value
}

// Generic function with comparable
func Contains[T comparable](slice []T, target T) bool {
    for _, item := range slice {
        if item == target {
            return true
        }
    }
    return false
}

// Multiple type parameters
func Pair[T, U any](a T, b U) (T, U) {
    return a, b
}

// Type inference
func main() {
    s := Identity("hello")  // T inferred as string
    n := Identity(42)       // T inferred as int

    fmt.Println(Contains([]string{"a", "b"}, "a"))  // true
    fmt.Println(Contains([]int{1, 2, 3}, 4))        // false

    fmt.Println(Pair("key", 42))  // T=string, U=int
}
```

### 4. Generic Types and Constraints

Generic types: `type Stack[T any] struct {}`. Custom constraints: `type Number interface { ~int | ~float64 }`. Use ~ to allow types with the same underlying type. The constraints package provides common constraints.

```go
package main

import (
    "fmt"
)

// Generic type
type Stack[T any] struct {
    items []T
}

func (s *Stack[T]) Push(item T) {
    s.items = append(s.items, item)
}

func (s *Stack[T]) Pop() (T, bool) {
    if len(s.items) == 0 {
        var zero T
        return zero, false
    }
    item := s.items[len(s.items)-1]
    s.items = s.items[:len(s.items)-1]
    return item, true
}

// Custom constraint
type Number interface {
    ~int | ~float64 | ~float32
}

func Sum[T Number](values []T) T {
    var sum T
    for _, v := range values {
        sum += v
    }
    return sum
}

// Interface constraint
type Stringer interface {
    String() string
}

func Print[T Stringer](v T) {
    fmt.Println(v.String())
}
```

### 5. Generics vs Reflection: When to Use Each

| Aspect | Generics | Reflection |
|--------|----------|------------|
| Type safety | Compile-time | Runtime (panics) |
| Performance | Zero overhead | Slow (allocations) |
| Use case | Data structures, algorithms | Serialization, ORMs |
| Example | Stack[T], Map[K,V] | JSON marshal, SQL scan |

```go
package main

import (
    "encoding/json"
    "fmt"
    "reflect"
)

// Generics: type-safe, zero overhead
func Filter[T any](items []T, pred func(T) bool) []T {
    var result []T
    for _, item := range items {
        if pred(item) {
            result = append(result, item)
        }
    }
    return result
}

// Reflection: necessary for dynamic types
func toJSON(v interface{}) (string, error) {
    data, err := json.Marshal(v)
    return string(data), err
}

// Reflection: check if type implements interface
func implementsStringer(v interface{}) bool {
    type stringer interface{ String() string }
    _, ok := v.(stringer)
    return ok
}

// Reflection: dynamic field access
func getField(v interface{}, name string) (interface{}, error) {
    val := reflect.ValueOf(v)
    if val.Kind() == reflect.Ptr {
        val = val.Elem()
    }
    field := val.FieldByName(name)
    if !field.IsValid() {
        return nil, fmt.Errorf("field %s not found", name)
    }
    return field.Interface(), nil
}
```

## Practice Questions

1. What is the difference between reflect.Type and reflect.Value?
2. How do you modify a struct field via reflection? What must be true?
3. What is the syntax for a generic function in Go? What does comparable do?
4. What is the ~ operator in type constraints?
5. When should you use generics vs reflection?

## LLM Prompts for Deeper Understanding

1. "Explain reflect: Type, Value, Kind, Elem, SetInt, SetString, NumField, FieldByName"
2. "Show generics: type parameters, constraints, comparable, custom constraints, ~ operator"
3. "Teach generics vs reflection: when to use each, performance implications, type safety"

## Key Takeaways

- reflect.TypeOf/ValueOf for runtime type inspection; Kind for underlying type
- Generics use [T any] syntax; type inference from arguments
- comparable is a built-in constraint; custom constraints use ~ for underlying types
- Prefer generics over reflection for type safety and performance