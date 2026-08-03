---
{
  "title": "Arrays and Slices",
  "description": "Fixed arrays, runtime slices, and bounds checking.",
  "type": "lesson",
  "order": 9,
  "duration": "30 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create fixed-length arrays",
    "Slice arrays for views",
    "Explain mandatory bounds checking"
  ],
  "knowledge_refs": [
    "zig/zig-09-arrays-slices"
  ],
  "prerequisites": [
    "zig-02-values-types"
  ],
  "references": [
    {
      "title": "Zig Reference — Arrays",
      "url": "https://ziglang.org/documentation/master/#Arrays"
    },
    {
      "title": "Zig Reference — Slices",
      "url": "https://ziglang.org/documentation/master/#Slices"
    }
  ]
}
---

# ZIG-09-ARRAYS-SLICES: Arrays and Slices

## Introduction

Fixed arrays, runtime slices, and bounds checking. By the end of this lesson you will be able to: Create fixed-length arrays; Slice arrays for views; Explain mandatory bounds checking.

## Key Concepts

### 1. Create fixed-length arrays

Target: Create fixed-length arrays. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```zig
// Arrays have fixed length; slices are views
const std = @import("std");

pub fn main() void {
    const arr = [_]i32{ 1, 2, 3, 4, 5 };
    const slice: []const i32 = arr[0..3];   // 1 2 3
    std.debug.print("{d}\n", .{slice.len});
}

```
### 2. Slice arrays for views

Target: Slice arrays for views. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```zig
// Bounds checking is mandatory at runtime
const std = @import("std");

pub fn main() void {
    const arr = [_]i32{ 1, 2, 3 };
    const idx: usize = 1;
    // arr[idx] panics if idx >= arr.len — no silent UB
    std.debug.print("{d}\n", .{arr[idx]});
}

```
### 3. Explain mandatory bounds checking

Target: Explain mandatory bounds checking. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```zig
// Slicing with comptime-known bounds when possible
const std = @import("std");

pub fn main() void {
    const data = "hello world";
    const first5 = data[0..5];
    std.debug.print("{s}\n", .{first5});   // hello
}

```
### 4. Create fixed-length arrays

Target: Create fixed-length arrays. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```zig
// Copying with std.mem.copyForwards
const std = @import("std");

pub fn main() void {
    var dest = [_]i32{ 0, 0, 0, 0, 0 };
    const src = [_]i32{ 7, 8, 9 };
    @memcpy(dest[0..3], &src);
    std.debug.print("{d} {d} {d}\n", .{ dest[0], dest[1], dest[2] });
}

```

## Practice Questions

1. What is the key idea behind "Arrays and Slices"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arrays and Slices with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arrays and Slices"
1. "Provide advanced patterns and performance considerations for Arrays and Slices"

## Key Takeaways

- Master the core ideas of Arrays and Slices through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
