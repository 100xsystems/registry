---
{
  "title": "Errors",
  "description": "Error unions, try, catch, and propagation.",
  "type": "lesson",
  "order": 7,
  "duration": 35,
  "difficulty": "intermediate",
  "learning_objectives": [
    "Return errors from functions with !T",
    "Propagate errors with try",
    "Handle errors with catch blocks"
  ],
  "knowledge_refs": [
    "zig/zig-07-errors"
  ],
  "prerequisites": [
    "zig-05-functions"
  ],
  "references": [
    {
      "title": "Zig Reference — Errors",
      "url": "https://ziglang.org/documentation/master/#Errors"
    },
    {
      "title": "Zig Guide — Error Handling",
      "url": "https://zig.guide/error-handling/"
    }
  ]
}
---

# ZIG-07-ERRORS: Errors

## Introduction

Error unions, try, catch, and propagation. By the end of this lesson you will be able to: Return errors from functions with !T; Propagate errors with try; Handle errors with catch blocks.

## Key Concepts

### 1. Return errors from functions with !T

Target: Return errors from functions with !T. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```zig
// Error unions: return error.NAME or a value
const std = @import("std");

fn safeDivide(a: i32, b: i32) !i32 {
    if (b == 0) return error.DivisionByZero;
    return a / b;
}

pub fn main() void {
    const result = safeDivide(10, 2) catch |err| {
        std.debug.print("error: {s}\n", .{@errorName(err)});
        return;
    };
    std.debug.print("{d}\n", .{result});
}

```
### 2. Propagate errors with try

Target: Propagate errors with try. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```zig
// try: propagate errors to the caller
const std = @import("std");

fn inner() !i32 {
    return error.NotReady;
}

fn outer() !i32 {
    const value = try inner();   // propagates the error
    return value + 1;
}

pub fn main() void {
    const r = outer() catch |err| {
        std.debug.print("caught {s}\n", .{@errorName(err)});
        return;
    };
    std.debug.print("{d}\n", .{r});
}

```
### 3. Handle errors with catch blocks

Target: Handle errors with catch blocks. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```zig
// Global error sets and error unions as values
const std = @import("std");

const MyError = error{ OutOfRange, BadInput };

fn validate(n: i32) MyError!i32 {
    if (n < 0) return error.BadInput;
    if (n > 100) return error.OutOfRange;
    return n;
}

pub fn main() void {
    const r = validate(-1) catch |err| {
        std.debug.print("{s}\n", .{@errorName(err)});
        return;
    };
    std.debug.print("{d}\n", .{r});
}

```
### 4. Return errors from functions with !T

Target: Return errors from functions with !T. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```zig
// Error handling with orelse-style fallbacks
const std = @import("std");

fn parseNumber(s: []const u8) !i32 {
    return std.fmt.parseInt(i32, s, 10);
}

pub fn main() void {
    const a = parseNumber("42") catch 0;
    const b = parseNumber("nope") catch 0;
    std.debug.print("{d} {d}\n", .{ a, b });   // 42 0
}

```

## Practice Questions

1. What is the key idea behind "Errors"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Errors with analogies and real-world examples"
1. "Show me common mistakes beginners make with Errors"
1. "Provide advanced patterns and performance considerations for Errors"

## Key Takeaways

- Master the core ideas of Errors through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
