---
{
  "title": "Memory Management",
  "description": "Explicit allocators, defer, realloc, and arenas.",
  "type": "lesson",
  "order": 14,
  "duration": 45,
  "difficulty": "expert",
  "learning_objectives": [
    "Explain why Zig makes allocators explicit",
    "Allocate and free with allocator.alloc and free",
    "Use defer and arenas for cleanup"
  ],
  "knowledge_refs": [
    "zig/zig-14-memory-management"
  ],
  "prerequisites": [
    "zig-09-arrays-slices"
  ],
  "references": [
    {
      "title": "Zig Reference — Memory",
      "url": "https://ziglang.org/documentation/master/#Memory"
    },
    {
      "title": "Zig Guide — Memory",
      "url": "https://zig.guide/memory/"
    },
    {
      "title": "Zig Reference — defer",
      "url": "https://ziglang.org/documentation/master/#defer"
    }
  ]
}
---

# ZIG-14-MEMORY-MANAGEMENT: Memory Management

## Introduction

Explicit allocators, defer, realloc, and arenas. By the end of this lesson you will be able to: Explain why Zig makes allocators explicit; Allocate and free with allocator.alloc and free; Use defer and arenas for cleanup.

## Key Concepts

### 1. Explain why Zig makes allocators explicit

Target: Explain why Zig makes allocators explicit. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```zig
// Zig has no hidden allocator: you pass one explicitly
const std = @import("std");

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    const nums = try allocator.alloc(i32, 3);
    defer allocator.free(nums);
    nums[0] = 10;
    nums[1] = 20;
    nums[2] = 30;
    std.debug.print("{d}\n", .{nums[2]});
}

```
### 2. Allocate and free with allocator.alloc and free

Target: Allocate and free with allocator.alloc and free. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```zig
// defer frees resources when the scope exits
const std = @import("std");

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    var list = std.ArrayList(i32).init(allocator);
    defer list.deinit();
    try list.append(1);
    try list.append(2);
    std.debug.print("{d}\n", .{list.items.len});
}

```
### 3. Use defer and arenas for cleanup

Target: Use defer and arenas for cleanup. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```zig
// realloc: grow a buffer in place when possible
const std = @import("std");

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    var buf = try allocator.alloc(u8, 2);
    defer allocator.free(buf);
    buf = try allocator.realloc(buf, 8);   // may move
    buf[7] = 'x';
    std.debug.print("{d}\n", .{buf.len});
}

```
### 4. Explain why Zig makes allocators explicit

Target: Explain why Zig makes allocators explicit. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```zig
// Arena allocator: free everything at once
const std = @import("std");

pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const allocator = arena.allocator();

    _ = try allocator.alloc(u8, 1000);
    _ = try allocator.alloc(u8, 2000);
    std.debug.print("arena freed at scope exit\n", .{});
}

```

## Practice Questions

1. What is the key idea behind "Memory Management"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Memory Management with analogies and real-world examples"
1. "Show me common mistakes beginners make with Memory Management"
1. "Provide advanced patterns and performance considerations for Memory Management"

## Key Takeaways

- Master the core ideas of Memory Management through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
