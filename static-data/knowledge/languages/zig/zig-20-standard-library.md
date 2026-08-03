---
{
  "title": "The Standard Library",
  "description": "std.debug, std.mem, std.ArrayList, and StringHashMap.",
  "type": "lesson",
  "order": 20,
  "duration": "30 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Print and inspect with std.debug",
    "Search memory with std.mem",
    "Use ArrayList and StringHashMap"
  ],
  "knowledge_refs": [
    "zig/zig-20-standard-library"
  ],
  "prerequisites": [
    "zig-14-memory-management"
  ],
  "references": [
    {
      "title": "Zig Standard Library — Index",
      "url": "https://ziglang.org/documentation/master/std/#root"
    },
    {
      "title": "Zig Reference — std.ArrayList",
      "url": "https://ziglang.org/documentation/master/std/#std.ArrayList"
    }
  ]
}
---

# ZIG-20-STANDARD-LIBRARY: The Standard Library

## Introduction

std.debug, std.mem, std.ArrayList, and StringHashMap. By the end of this lesson you will be able to: Print and inspect with std.debug; Search memory with std.mem; Use ArrayList and StringHashMap.

## Key Concepts

### 1. Print and inspect with std.debug

Target: Print and inspect with std.debug. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```zig
// std.debug.print is the quick print; use it in main only
const std = @import("std");

pub fn main() void {
    std.debug.print("debug print\n", .{});
}

```
### 2. Search memory with std.mem

Target: Search memory with std.mem. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```zig
// std.mem: eql, startsWith, endsWith, indexOf
const std = @import("std");

pub fn main() void {
    const text = "hello world";
    const idx = std.mem.indexOf(u8, text, "world") orelse 0;
    std.debug.print("{d}\n", .{idx});   // 6
}

```
### 3. Use ArrayList and StringHashMap

Target: Use ArrayList and StringHashMap. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```zig
// std.ArrayList: the dynamic array workhorse
const std = @import("std");

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    var list = std.ArrayList(u8).init(allocator);
    defer list.deinit();
    try list.append('a');
    try list.appendSlice("bc");
    std.debug.print("{s}\n", .{list.items});   // abc
}

```
### 4. Print and inspect with std.debug

Target: Print and inspect with std.debug. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```zig
// std.StringHashMap: a ready-made hash map
const std = @import("std");

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    var map = std.StringHashMap(i32).init(allocator);
    defer map.deinit();
    try map.put("age", 36);
    const age = map.get("age") orelse 0;
    std.debug.print("{d}\n", .{age});   // 36
}

```

## Practice Questions

1. What is the key idea behind "The Standard Library"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain The Standard Library with analogies and real-world examples"
1. "Show me common mistakes beginners make with The Standard Library"
1. "Provide advanced patterns and performance considerations for The Standard Library"

## Key Takeaways

- Master the core ideas of The Standard Library through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
