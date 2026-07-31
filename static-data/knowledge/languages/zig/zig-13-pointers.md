---
{
  "title": "Pointers",
  "description": "Single-item pointers, const pointers, and optional pointers.",
  "type": "lesson",
  "order": 13,
  "duration": 30,
  "difficulty": "intermediate",
  "learning_objectives": [
    "Take addresses with & and dereference with .*",
    "Distinguish *T from *const T",
    "Use optional pointers ?*T"
  ],
  "knowledge_refs": [
    "zig/zig-13-pointers"
  ],
  "prerequisites": [
    "zig-03-variables"
  ],
  "references": [
    {
      "title": "Zig Reference — Pointers",
      "url": "https://ziglang.org/documentation/master/#Pointers"
    },
    {
      "title": "Zig Reference — Many-Item Pointers",
      "url": "https://ziglang.org/documentation/master/#Many-Item-Pointers"
    }
  ]
}
---

# ZIG-13-POINTERS: Pointers

## Introduction

Single-item pointers, const pointers, and optional pointers. By the end of this lesson you will be able to: Take addresses with & and dereference with .*; Distinguish *T from *const T; Use optional pointers ?*T.

## Key Concepts

### 1. Take addresses with & and dereference with .*

Target: Take addresses with & and dereference with .*. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```zig
// Pointers: & takes an address; *T is a pointer type
const std = @import("std");

pub fn main() void {
    var x: i32 = 42;
    const p: *i32 = &x;
    p.* = 43;               // dereference to write
    std.debug.print("{d}\n", .{x});   // 43
}

```
### 2. Distinguish *T from *const T

Target: Distinguish *T from *const T. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```zig
// const pointers prevent mutation
const std = @import("std");

pub fn main() void {
    const value: i32 = 10;
    const p: *const i32 = &value;
    std.debug.print("{d}\n", .{p.*});
    // p.* = 20 would fail to compile
}

```
### 3. Use optional pointers ?*T

Target: Use optional pointers ?*T. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```zig
// Many-item pointers and slices
const std = @import("std");

pub fn main() void {
    const arr = [_]i32{ 1, 2, 3 };
    const ptr: [*]const i32 = &arr;
    _ = ptr;   // used only for illustration
    const slice: []const i32 = arr[0..];
    std.debug.print("{d}\n", .{slice.len});
}

```
### 4. Take addresses with & and dereference with .*

Target: Take addresses with & and dereference with .*. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```zig
// Optional pointers: ?*T — the null-able pointer
const std = @import("std");

fn maybePtr(flag: bool) ?*const i32 {
    const value: i32 = 5;
    if (flag) return &value;
    return null;
}

pub fn main() void {
    const p = maybePtr(true) orelse return;
    std.debug.print("{d}\n", .{p.*});
}

```

## Practice Questions

1. What is the key idea behind "Pointers"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Pointers with analogies and real-world examples"
1. "Show me common mistakes beginners make with Pointers"
1. "Provide advanced patterns and performance considerations for Pointers"

## Key Takeaways

- Master the core ideas of Pointers through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
