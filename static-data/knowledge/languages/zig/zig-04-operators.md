---
{
  "title": "Operators",
  "description": "Arithmetic, division semantics, bitwise, and logic.",
  "type": "lesson",
  "order": 4,
  "duration": "25 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use arithmetic operators on integers and floats",
    "Explain division semantics by type",
    "Apply bitwise and logical operators"
  ],
  "knowledge_refs": [
    "zig/zig-04-operators"
  ],
  "prerequisites": [
    "zig-02-values-types"
  ],
  "references": [
    {
      "title": "Zig Reference — Operators",
      "url": "https://ziglang.org/documentation/master/#Operators"
    },
    {
      "title": "Zig Reference — Assignment",
      "url": "https://ziglang.org/documentation/master/#Assignment"
    }
  ]
}
---

# ZIG-04-OPERATORS: Operators

## Introduction

Arithmetic, division semantics, bitwise, and logic. By the end of this lesson you will be able to: Use arithmetic operators on integers and floats; Explain division semantics by type; Apply bitwise and logical operators.

## Key Concepts

### 1. Use arithmetic operators on integers and floats

Target: Use arithmetic operators on integers and floats. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```zig
// Arithmetic operators
const std = @import("std");

pub fn main() void {
    const a: i32 = 7;
    std.debug.print("{d}\n", .{a + 3});   // 10
    std.debug.print("{d}\n", .{a - 2});   // 5
    std.debug.print("{d}\n", .{a * 2});   // 14
    std.debug.print("{d}\n", .{a / 2});   // 3 — integer division
    std.debug.print("{d}\n", .{a % 4});   // 3 — modulo
}

```
### 2. Explain division semantics by type

Target: Explain division semantics by type. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```zig
// Division semantics differ by type
const std = @import("std");

pub fn main() void {
    const int_div = 7 / 2;       // 3 (i32 comptime)
    const float_div = @as(f64, 7) / 2.0;  // 3.5
    std.debug.print("{d} {d}\n", .{ int_div, float_div });
}

```
### 3. Apply bitwise and logical operators

Target: Apply bitwise and logical operators. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```zig
// Bitwise operators
const std = @import("std");

pub fn main() void {
    const a: u8 = 0b1100;
    const b: u8 = 0b1010;
    std.debug.print("{b}\n", .{a & b});   // 1000
    std.debug.print("{b}\n", .{a | b});   // 1110
    std.debug.print("{b}\n", .{a ^ b});   // 0110 (xor)
    std.debug.print("{b}\n", .{a << 1});  // 11000
}

```
### 4. Use arithmetic operators on integers and floats

Target: Use arithmetic operators on integers and floats. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```zig
// Comparison and logical operators
const std = @import("std");

pub fn main() void {
    const x: i32 = 5;
    std.debug.print("{any} {any}\n", .{ x < 10, x >= 3 });
    std.debug.print("{any}\n", .{x > 0 and x < 10});   // true
    std.debug.print("{any}\n", .{x < 0 or x == 5});    // true
    std.debug.print("{any}\n", .{!(x == 0)});          // true
}

```

## Practice Questions

1. What is the key idea behind "Operators"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Operators with analogies and real-world examples"
1. "Show me common mistakes beginners make with Operators"
1. "Provide advanced patterns and performance considerations for Operators"

## Key Takeaways

- Master the core ideas of Operators through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
