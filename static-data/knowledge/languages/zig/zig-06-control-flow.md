---
{
  "title": "Control Flow",
  "description": "if expressions, switch, for, and while loops.",
  "type": "lesson",
  "order": 6,
  "duration": 30,
  "difficulty": "beginner",
  "learning_objectives": [
    "Use if and switch as expressions",
    "Iterate with for over slices and ranges",
    "Control loops with continue and break"
  ],
  "knowledge_refs": [
    "zig/zig-06-control-flow"
  ],
  "prerequisites": [
    "zig-01-getting-started"
  ],
  "references": [
    {
      "title": "Zig Reference — If",
      "url": "https://ziglang.org/documentation/master/#If"
    },
    {
      "title": "Zig Reference — Switch",
      "url": "https://ziglang.org/documentation/master/#Switch"
    },
    {
      "title": "Zig Reference — Loops",
      "url": "https://ziglang.org/documentation/master/#While"
    }
  ]
}
---

# ZIG-06-CONTROL-FLOW: Control Flow

## Introduction

if expressions, switch, for, and while loops. By the end of this lesson you will be able to: Use if and switch as expressions; Iterate with for over slices and ranges; Control loops with continue and break.

## Key Concepts

### 1. Use if and switch as expressions

Target: Use if and switch as expressions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```zig
// if is an expression in Zig
const std = @import("std");

pub fn main() void {
    const x: i32 = 10;
    const label = if (x > 5) "big" else "small";
    std.debug.print("{s}\n", .{label});   // big
}

```
### 2. Iterate with for over slices and ranges

Target: Iterate with for over slices and ranges. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```zig
// switch expressions — exhaustive by default
const std = @import("std");

fn day_name(d: u8) []const u8 {
    return switch (d) {
        1 => "Monday",
        2 => "Tuesday",
        3 => "Wednesday",
        else => "another day",
    };
}

pub fn main() void {
    std.debug.print("{s}\n", .{day_name(2)});
}

```
### 3. Control loops with continue and break

Target: Control loops with continue and break. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```zig
// for loops over slices and ranges
const std = @import("std");

pub fn main() void {
    const nums = [_]i32{ 1, 2, 3, 4, 5 };
    var total: i32 = 0;
    for (nums) |n| {
        total += n;
    }
    std.debug.print("{d}\n", .{total});   // 15
}

```
### 4. Use if and switch as expressions

Target: Use if and switch as expressions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```zig
// while loops with continue and break
const std = @import("std");

pub fn main() void {
    var i: u32 = 0;
    var total: u32 = 0;
    while (i < 10) : (i += 1) {
        if (i == 3) continue;
        if (i == 7) break;
        total += i;
    }
    std.debug.print("{d}\n", .{total});   // 0+1+2+4+5+6 = 18
}

```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
