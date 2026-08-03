---
{
  "title": "Values and Types",
  "description": "Integers, floats, bools, chars, and explicit casts.",
  "type": "lesson",
  "order": 2,
  "duration": "25 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Choose integer types with explicit sizes",
    "Work with floats and bools",
    "Cast between types with @intCast and @floatCast"
  ],
  "knowledge_refs": [
    "zig/zig-02-values-types"
  ],
  "prerequisites": [
    "zig-01-getting-started"
  ],
  "references": [
    {
      "title": "Zig Reference — Primitive Types",
      "url": "https://ziglang.org/documentation/master/#Primitive-Types"
    },
    {
      "title": "Zig Reference — Casting",
      "url": "https://ziglang.org/documentation/master/#Casting"
    }
  ]
}
---

# ZIG-02-VALUES-TYPES: Values and Types

## Introduction

Integers, floats, bools, chars, and explicit casts. By the end of this lesson you will be able to: Choose integer types with explicit sizes; Work with floats and bools; Cast between types with @intCast and @floatCast.

## Key Concepts

### 1. Choose integer types with explicit sizes

Target: Choose integer types with explicit sizes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```zig
// Integer types: signed and unsigned, sized explicitly
const std = @import("std");

pub fn main() void {
    const a: i32 = -10;      // signed 32-bit
    const b: u8 = 255;       // unsigned 8-bit (max 255)
    const c: usize = 1000;   // pointer-sized unsigned
    std.debug.print("{d} {d} {d}\n", .{ a, b, c });
}

```
### 2. Work with floats and bools

Target: Work with floats and bools. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```zig
// Floats: f16, f32, f64, f128
const std = @import("std");

pub fn main() void {
    const pi: f64 = 3.14159;
    const half: f32 = 0.5;
    std.debug.print("{d} {d}\n", .{ pi, half });
}

```
### 3. Cast between types with @intCast and @floatCast

Target: Cast between types with @intCast and @floatCast. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```zig
// Bools and char literals
const std = @import("std");

pub fn main() void {
    const ok: bool = true;
    const letter = 'a';        // a comptime_int char literal
    std.debug.print("{any} {c}\n", .{ ok, letter });
}

```
### 4. Choose integer types with explicit sizes

Target: Choose integer types with explicit sizes. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```zig
// Type coercion is explicit: use @intCast, @floatCast
const std = @import("std");

pub fn main() void {
    const small: u8 = 42;
    const big: u32 = @intCast(small);   // widening cast
    std.debug.print("{d}\n", .{big});
}

```

## Practice Questions

1. What is the key idea behind "Values and Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Values and Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Values and Types"
1. "Provide advanced patterns and performance considerations for Values and Types"

## Key Takeaways

- Master the core ideas of Values and Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
