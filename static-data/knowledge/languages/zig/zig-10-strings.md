---
{
  "title": "Strings",
  "description": "[]const u8, literals, allocation, and comparison.",
  "type": "lesson",
  "order": 10,
  "duration": 30,
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain that strings are byte slices",
    "Build strings at runtime with ArrayList",
    "Compare and search strings with std.mem"
  ],
  "knowledge_refs": [
    "zig/zig-10-strings"
  ],
  "prerequisites": [
    "zig-09-arrays-slices"
  ],
  "references": [
    {
      "title": "Zig Guide — Strings",
      "url": "https://zig.guide/strings/"
    },
    {
      "title": "Zig Reference — Sentinel-Terminated Arrays",
      "url": "https://ziglang.org/documentation/master/#Sentinel-Terminated-Arrays"
    }
  ]
}
---

# ZIG-10-STRINGS: Strings

## Introduction

[]const u8, literals, allocation, and comparison. By the end of this lesson you will be able to: Explain that strings are byte slices; Build strings at runtime with ArrayList; Compare and search strings with std.mem.

## Key Concepts

### 1. Explain that strings are byte slices

Target: Explain that strings are byte slices. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```zig
// Strings are []const u8 in Zig
const std = @import("std");

pub fn main() void {
    const greeting: []const u8 = "hello";
    std.debug.print("{s} (len {d})\n", .{ greeting, greeting.len });
}

```
### 2. Build strings at runtime with ArrayList

Target: Build strings at runtime with ArrayList. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```zig
// String literals are null-terminated comptime values
const std = @import("std");

pub fn main() void {
    const lit = "c-string";   // *const [9:0]u8
    const slice: []const u8 = lit;
    std.debug.print("{s}\n", .{slice});
}

```
### 3. Compare and search strings with std.mem

Target: Compare and search strings with std.mem. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```zig
// Building strings at runtime needs an allocator
const std = @import("std");

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    var buf = std.ArrayList(u8).init(allocator);
    defer buf.deinit();
    try buf.appendSlice("Hello, ");
    try buf.appendSlice("Zig!");
    std.debug.print("{s}\n", .{buf.items});
}

```
### 4. Explain that strings are byte slices

Target: Explain that strings are byte slices. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```zig
// Comparing and searching strings
const std = @import("std");

pub fn main() void {
    const a = "hello";
    const b = "hello";
    const eq = std.mem.eql(u8, a, b);
    const starts = std.mem.startsWith(u8, "hello world", "hello");
    std.debug.print("{any} {any}\n", .{ eq, starts });
}

```

## Practice Questions

1. What is the key idea behind "Strings"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Strings with analogies and real-world examples"
1. "Show me common mistakes beginners make with Strings"
1. "Provide advanced patterns and performance considerations for Strings"

## Key Takeaways

- Master the core ideas of Strings through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
