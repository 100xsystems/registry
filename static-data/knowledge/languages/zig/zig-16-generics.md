---
{
  "title": "Generics",
  "description": "Generic functions and data structures via comptime T.",
  "type": "lesson",
  "order": 16,
  "duration": "40 min",
  "difficulty": "expert",
  "learning_objectives": [
    "Parameterize functions with comptime types",
    "Build generic structs",
    "Reuse std.ArrayList and friends"
  ],
  "knowledge_refs": [
    "zig/zig-16-generics"
  ],
  "prerequisites": [
    "zig-15-comptime"
  ],
  "references": [
    {
      "title": "Zig Guide — Comptime and Generics",
      "url": "https://zig.guide/comptime/"
    },
    {
      "title": "Zig Reference — Generic Data Structures",
      "url": "https://ziglang.org/documentation/master/#Generic-Data-Structures"
    }
  ]
}
---

# ZIG-16-GENERICS: Generics

## Introduction

Generic functions and data structures via comptime T. By the end of this lesson you will be able to: Parameterize functions with comptime types; Build generic structs; Reuse std.ArrayList and friends.

## Key Concepts

### 1. Parameterize functions with comptime types

Target: Parameterize functions with comptime types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```zig
// Generic functions via comptime type parameters
const std = @import("std");

fn maxOf(comptime T: type, a: T, b: T) T {
    return if (a > b) a else b;
}

pub fn main() void {
    std.debug.print("{d}\n", .{maxOf(i32, 3, 7)});
    std.debug.print("{d}\n", .{maxOf(f64, 2.5, 1.5)});
}

```
### 2. Build generic structs

Target: Build generic structs. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```zig
// Generic data structures
const std = @import("std");

fn Stack(comptime T: type) type {
    return struct {
        items: []T,
        len: usize = 0,

        fn push(self: *@This(), item: T) void {
            self.items[self.len] = item;
            self.len += 1;
        }
    };
}

pub fn main() void {
    var arr = [_]i32{ 0, 0, 0 };
    var stack = Stack(i32){ .items = &arr };
    stack.push(42);
    std.debug.print("{d}\n", .{stack.len});
}

```
### 3. Reuse std.ArrayList and friends

Target: Reuse std.ArrayList and friends. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```zig
// Generic over the element type with constraints
const std = @import("std");

fn sum(comptime T: type, items: []const T) T {
    var total: T = 0;
    for (items) |it| {
        total += it;
    }
    return total;
}

pub fn main() void {
    const ints = [_]i32{ 1, 2, 3, 4 };
    const floats = [_]f64{ 0.5, 1.5 };
    std.debug.print("{d} {d}\n", .{ sum(i32, &ints), sum(f64, &floats) });
}

```
### 4. Parameterize functions with comptime types

Target: Parameterize functions with comptime types. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```zig
// std.ArrayList is a ready-made generic
const std = @import("std");

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    var list = std.ArrayList(i32).init(allocator);
    defer list.deinit();
    try list.appendSlice(&[_]i32{ 1, 2, 3 });
    std.debug.print("{d}\n", .{list.items.len});   // 3
}

```

## Practice Questions

1. What is the key idea behind "Generics"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Generics with analogies and real-world examples"
1. "Show me common mistakes beginners make with Generics"
1. "Provide advanced patterns and performance considerations for Generics"

## Key Takeaways

- Master the core ideas of Generics through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
