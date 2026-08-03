---
{
  "title": "Variables",
  "description": "const vs var, mutation, and type inference.",
  "type": "lesson",
  "order": 3,
  "duration": "25 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Prefer const over var",
    "Mutate values only when needed",
    "Leverage type inference"
  ],
  "knowledge_refs": [
    "zig/zig-03-variables"
  ],
  "prerequisites": [
    "zig-02-values-types"
  ],
  "references": [
    {
      "title": "Zig Reference — Values",
      "url": "https://ziglang.org/documentation/master/#Values"
    },
    {
      "title": "Zig Reference — Variables",
      "url": "https://ziglang.org/documentation/master/#Variables"
    }
  ]
}
---

# ZIG-03-VARIABLES: Variables

## Introduction

const vs var, mutation, and type inference. By the end of this lesson you will be able to: Prefer const over var; Mutate values only when needed; Leverage type inference.

## Key Concepts

### 1. Prefer const over var

Target: Prefer const over var. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```zig
// const vs var: prefer const by default
const std = @import("std");

pub fn main() void {
    const fixed = 10;        // cannot be reassigned
    var mutable: i32 = 0;
    mutable += 5;            // var allows mutation
    std.debug.print("{d} {d}\n", .{ fixed, mutable });
}

```
### 2. Mutate values only when needed

Target: Mutate values only when needed. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```zig
// Variable shadowing is allowed and often idiomatic
const std = @import("std");

pub fn main() void {
    var x: i32 = 1;
    x = x + 1;               // mutate in place
    const y = x * 2;
    std.debug.print("{d} {d}\n", .{ x, y });
}

```
### 3. Leverage type inference

Target: Leverage type inference. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```zig
// Undefined values must be initialized before use
const std = @import("std");

pub fn main() void {
    var total: i32 = 0;      // always initialize
    for (1..6) |i| {
        total += @intCast(i);
    }
    std.debug.print("sum 1..5 = {d}\n", .{total});
}

```
### 4. Prefer const over var

Target: Prefer const over var. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```zig
// Type inference with const keeps code clean
const std = @import("std");

pub fn main() void {
    const greeting = "hello";          // *const [5:0]u8 comptime literal
    const count: u32 = 100;
    std.debug.print("{s} {d}\n", .{ greeting, count });
}

```

## Practice Questions

1. What is the key idea behind "Variables"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables"
1. "Provide advanced patterns and performance considerations for Variables"

## Key Takeaways

- Master the core ideas of Variables through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
