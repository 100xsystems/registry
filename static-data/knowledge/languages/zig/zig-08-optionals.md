---
{
  "title": "Optionals",
  "description": "?T, null, orelse, and if-unwrapping.",
  "type": "lesson",
  "order": 8,
  "duration": "30 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Represent absence with optional types",
    "Unwrap with orelse and if payloads",
    "Compose optionals with error unions"
  ],
  "knowledge_refs": [
    "zig/zig-08-optionals"
  ],
  "prerequisites": [
    "zig-07-errors"
  ],
  "references": [
    {
      "title": "Zig Reference — Optionals",
      "url": "https://ziglang.org/documentation/master/#Optionals"
    }
  ]
}
---

# ZIG-08-OPTIONALS: Optionals

## Introduction

?T, null, orelse, and if-unwrapping. By the end of this lesson you will be able to: Represent absence with optional types; Unwrap with orelse and if payloads; Compose optionals with error unions.

## Key Concepts

### 1. Represent absence with optional types

Target: Represent absence with optional types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```zig
// Optionals: ?T holds T or null
const std = @import("std");

pub fn main() void {
    const maybe: ?i32 = null;
    const value: ?i32 = 42;

    const a = maybe orelse 0;    // 0
    const b = value orelse 0;    // 42
    std.debug.print("{d} {d}\n", .{ a, b });
}

```
### 2. Unwrap with orelse and if payloads

Target: Unwrap with orelse and if payloads. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```zig
// Unwrap with if — the idiomatic optional pattern
const std = @import("std");

pub fn main() void {
    const maybe: ?i32 = 7;
    if (maybe) |v| {
        std.debug.print("got {d}\n", .{v});
    } else {
        std.debug.print("nothing\n", .{});
    }
}

```
### 3. Compose optionals with error unions

Target: Compose optionals with error unions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```zig
// Optionals wrap any type, including pointers
const std = @import("std");

fn find(nums: []const i32, target: i32) ?usize {
    for (nums, 0..) |n, i| {
        if (n == target) return i;
    }
    return null;
}

pub fn main() void {
    const nums = [_]i32{ 10, 20, 30 };
    const idx = find(&nums, 20) orelse 99;
    std.debug.print("{d}\n", .{idx});   // 1
}

```
### 4. Represent absence with optional types

Target: Represent absence with optional types. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```zig
// Error unions and optionals compose: !?T
const std = @import("std");

fn lookup(key: []const u8) !?i32 {
    if (key.len == 0) return error.EmptyKey;
    return null;   // valid: not found
}

pub fn main() void {
    const r = lookup("a") catch null;
    const v = r orelse -1;
    std.debug.print("{d}\n", .{v});   // -1
}

```

## Practice Questions

1. What is the key idea behind "Optionals"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Optionals with analogies and real-world examples"
1. "Show me common mistakes beginners make with Optionals"
1. "Provide advanced patterns and performance considerations for Optionals"

## Key Takeaways

- Master the core ideas of Optionals through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
