---
{
  "title": "Enums and Tagged Unions",
  "description": "Enums, exhaustive switch, and union(enum) payloads.",
  "type": "lesson",
  "order": 12,
  "duration": 35,
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define enums with @tagName",
    "Write exhaustive switches over enums",
    "Model alternatives with tagged unions"
  ],
  "knowledge_refs": [
    "zig/zig-12-enums-unions"
  ],
  "prerequisites": [
    "zig-06-control-flow"
  ],
  "references": [
    {
      "title": "Zig Reference — Enums",
      "url": "https://ziglang.org/documentation/master/#enum"
    },
    {
      "title": "Zig Reference — Unions",
      "url": "https://ziglang.org/documentation/master/#union"
    }
  ]
}
---

# ZIG-12-ENUMS-UNIONS: Enums and Tagged Unions

## Introduction

Enums, exhaustive switch, and union(enum) payloads. By the end of this lesson you will be able to: Define enums with @tagName; Write exhaustive switches over enums; Model alternatives with tagged unions.

## Key Concepts

### 1. Define enums with @tagName

Target: Define enums with @tagName. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```zig
// Enums: named values with optional explicit tags
const std = @import("std");

const Color = enum { red, green, blue };

pub fn main() void {
    const c = Color.green;
    std.debug.print("{s}\n", .{@tagName(c)});   // green
}

```
### 2. Write exhaustive switches over enums

Target: Write exhaustive switches over enums. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```zig
// Switch over enums is exhaustive
const std = @import("std");

const Shape = enum { circle, square, triangle };

fn describe(s: Shape) []const u8 {
    return switch (s) {
        .circle => "round",
        .square => "four sides",
        .triangle => "three sides",
    };
}

pub fn main() void {
    std.debug.print("{s}\n", .{describe(.square)});
}

```
### 3. Model alternatives with tagged unions

Target: Model alternatives with tagged unions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```zig
// Tagged unions: one payload among many
const std = @import("std");

const Value = union(enum) {
    int: i32,
    text: []const u8,
    none,
};

pub fn main() void {
    const v = Value{ .text = "hi" };
    switch (v) {
        .int => |i| std.debug.print("int {d}\n", .{i}),
        .text => |s| std.debug.print("text {s}\n", .{s}),
        .none => std.debug.print("none\n", .{}),
    }
}

```
### 4. Define enums with @tagName

Target: Define enums with @tagName. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```zig
// Enum values can carry explicit numeric tags
const std = @import("std");

const HttpStatus = enum(u16) {
    ok = 200,
    not_found = 404,
    server_error = 500,
};

pub fn main() void {
    const s = HttpStatus.not_found;
    const n: u16 = @intFromEnum(s);
    std.debug.print("{d}\n", .{n});   // 404
}

```

## Practice Questions

1. What is the key idea behind "Enums and Tagged Unions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Enums and Tagged Unions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Enums and Tagged Unions"
1. "Provide advanced patterns and performance considerations for Enums and Tagged Unions"

## Key Takeaways

- Master the core ideas of Enums and Tagged Unions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
