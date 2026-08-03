---
{
  "title": "File I/O",
  "description": "Reading, writing, and iterating with std.fs.",
  "type": "lesson",
  "order": 18,
  "duration": "30 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read files with readFileAlloc",
    "Write files with writeFile",
    "Iterate directory entries"
  ],
  "knowledge_refs": [
    "zig/zig-18-file-io"
  ],
  "prerequisites": [
    "zig-14-memory-management"
  ],
  "references": [
    {
      "title": "Zig Standard Library — std.fs",
      "url": "https://ziglang.org/documentation/master/std/#std.fs"
    },
    {
      "title": "Zig Reference — File System",
      "url": "https://ziglang.org/documentation/master/std/#root"
    }
  ]
}
---

# ZIG-18-FILE-IO: File I/O

## Introduction

Reading, writing, and iterating with std.fs. By the end of this lesson you will be able to: Read files with readFileAlloc; Write files with writeFile; Iterate directory entries.

## Key Concepts

### 1. Read files with readFileAlloc

Target: Read files with readFileAlloc. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```zig
// Reading a file requires an allocator and open options
const std = @import("std");

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    const contents = try std.fs.cwd().readFileAlloc(allocator, "data.txt", 1 << 20);
    defer allocator.free(contents);
    std.debug.print("read {d} bytes\n", .{contents.len});
}

```
### 2. Write files with writeFile

Target: Write files with writeFile. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```zig
// Writing a file
const std = @import("std");

pub fn main() !void {
    const data = "line one\nline two\n";
    try std.fs.cwd().writeFile(.{
        .sub_path = "out.txt",
        .data = data,
    });
    std.debug.print("wrote file\n", .{});
}

```
### 3. Iterate directory entries

Target: Iterate directory entries. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```zig
// Iterating over directory entries
const std = @import("std");

pub fn main() !void {
    var dir = try std.fs.cwd().openDir(".", .{ .iterate = true });
    defer dir.close();

    var it = dir.iterate();
    var count: usize = 0;
    while (try it.next()) |entry| {
        _ = entry;
        count += 1;
    }
    std.debug.print("{d} entries\n", .{count});
}

```
### 4. Read files with readFileAlloc

Target: Read files with readFileAlloc. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```zig
// std.fs.cwd() is the current working directory handle
const std = @import("std");

pub fn main() !void {
    const cwd = std.fs.cwd();
    _ = cwd;   // placeholder for file operations
    std.debug.print("cwd handle acquired\n", .{});
}

```

## Practice Questions

1. What is the key idea behind "File I/O"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain File I/O with analogies and real-world examples"
1. "Show me common mistakes beginners make with File I/O"
1. "Provide advanced patterns and performance considerations for File I/O"

## Key Takeaways

- Master the core ideas of File I/O through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
