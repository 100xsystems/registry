---
{
  "title": "Comptime",
  "description": "Compile-time evaluation, comptime params, and introspection.",
  "type": "lesson",
  "order": 15,
  "duration": "40 min",
  "difficulty": "expert",
  "learning_objectives": [
    "Evaluate expressions at compile time",
    "Use comptime function parameters",
    "Introspect types with @TypeOf and @sizeOf"
  ],
  "knowledge_refs": [
    "zig/zig-15-comptime"
  ],
  "prerequisites": [
    "zig-06-control-flow"
  ],
  "references": [
    {
      "title": "Zig Reference — comptime",
      "url": "https://ziglang.org/documentation/master/#comptime"
    },
    {
      "title": "Zig Guide — Comptime",
      "url": "https://zig.guide/comptime/"
    }
  ]
}
---

# ZIG-15-COMPTIME: Comptime

## Introduction

Compile-time evaluation, comptime params, and introspection. By the end of this lesson you will be able to: Evaluate expressions at compile time; Use comptime function parameters; Introspect types with @TypeOf and @sizeOf.

## Key Concepts

### 1. Evaluate expressions at compile time

Target: Evaluate expressions at compile time. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```zig
// comptime: code that runs at compile time
const std = @import("std");

fn power(comptime base: i32, comptime exp: u32) i32 {
    var result: i32 = 1;
    var i: u32 = 0;
    while (i < exp) : (i += 1) {
        result *= base;
    }
    return result;
}

pub fn main() void {
    const v = comptime power(2, 10);
    std.debug.print("{d}\n", .{v});   // 1024
}

```
### 2. Use comptime function parameters

Target: Use comptime function parameters. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```zig
// comptime expressions are evaluated at build time
const std = @import("std");

const TableSize = comptime blk: {
    var size: usize = 16;
    while (size < 1000) size *= 2;
    break :blk size;
};

pub fn main() void {
    std.debug.print("{d}\n", .{TableSize});   // 1024
}

```
### 3. Introspect types with @TypeOf and @sizeOf

Target: Introspect types with @TypeOf and @sizeOf. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```zig
// @TypeOf and comptime introspection
const std = @import("std");

pub fn main() void {
    const x: u8 = 255;
    const T = @TypeOf(x);
    std.debug.print("{any}\n", .{T});   // u8
}

```
### 4. Evaluate expressions at compile time

Target: Evaluate expressions at compile time. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```zig
// inline for unrolls loops at compile time
const std = @import("std");

pub fn main() void {
    const types = [_]type{ i32, f64, bool };
    inline for (types) |T| {
        std.debug.print("{any} size {d}\n", .{ T, @sizeOf(T) });
    }
}

```

## Practice Questions

1. What is the key idea behind "Comptime"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Comptime with analogies and real-world examples"
1. "Show me common mistakes beginners make with Comptime"
1. "Provide advanced patterns and performance considerations for Comptime"

## Key Takeaways

- Master the core ideas of Comptime through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
