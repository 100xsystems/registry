---
{
  "title": "Functions",
  "description": "Explicit signatures, void returns, and function pointers.",
  "type": "lesson",
  "order": 5,
  "duration": 30,
  "difficulty": "beginner",
  "learning_objectives": [
    "Define functions with explicit return types",
    "Write void functions that produce output",
    "Pass functions as values"
  ],
  "knowledge_refs": [
    "zig/zig-05-functions"
  ],
  "prerequisites": [
    "zig-01-getting-started"
  ],
  "references": [
    {
      "title": "Zig Reference — Functions",
      "url": "https://ziglang.org/documentation/master/#Functions"
    }
  ]
}
---

# ZIG-05-FUNCTIONS: Functions

## Introduction

Explicit signatures, void returns, and function pointers. By the end of this lesson you will be able to: Define functions with explicit return types; Write void functions that produce output; Pass functions as values.

## Key Concepts

### 1. Define functions with explicit return types

Target: Define functions with explicit return types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```zig
// Functions: explicit return types, named parameters
const std = @import("std");

fn add(a: i32, b: i32) i32 {
    return a + b;
}

pub fn main() void {
    std.debug.print("{d}\n", .{add(2, 3)});   // 5
}

```
### 2. Write void functions that produce output

Target: Write void functions that produce output. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```zig
// Functions that return void and use values
const std = @import("std");

fn describe(x: i32) void {
    if (x > 0) {
        std.debug.print("positive\n", .{});
    } else {
        std.debug.print("non-positive\n", .{});
    }
}

pub fn main() void {
    describe(5);
    describe(-1);
}

```
### 3. Pass functions as values

Target: Pass functions as values. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```zig
// Nested functions are not allowed; use top-level fns
const std = @import("std");

fn square(x: i32) i32 {
    return x * x;
}

pub fn main() void {
    std.debug.print("{d}\n", .{square(square(3))});   // 81
}

```
### 4. Define functions with explicit return types

Target: Define functions with explicit return types. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```zig
// Function pointers and passing functions
const std = @import("std");

fn twice(f: *const fn (i32) i32, x: i32) i32 {
    return f(f(x));
}

fn inc(x: i32) i32 {
    return x + 1;
}

pub fn main() void {
    std.debug.print("{d}\n", .{twice(inc, 5)});   // 7
}

```

## Practice Questions

1. What is the key idea behind "Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions"
1. "Provide advanced patterns and performance considerations for Functions"

## Key Takeaways

- Master the core ideas of Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
