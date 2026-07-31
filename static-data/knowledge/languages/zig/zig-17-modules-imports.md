---
{
  "title": "Modules and Imports",
  "description": "@import, pub declarations, and build.zig wiring.",
  "type": "lesson",
  "order": 17,
  "duration": 30,
  "difficulty": "intermediate",
  "learning_objectives": [
    "Import modules with @import",
    "Expose declarations with pub",
    "Understand the build.zig file layout"
  ],
  "knowledge_refs": [
    "zig/zig-17-modules-imports"
  ],
  "prerequisites": [
    "zig-01-getting-started"
  ],
  "references": [
    {
      "title": "Zig Reference — Import",
      "url": "https://ziglang.org/documentation/master/#Import"
    },
    {
      "title": "Zig Build System — Documentation",
      "url": "https://ziglang.org/learn/build-system/"
    }
  ]
}
---

# ZIG-17-MODULES-IMPORTS: Modules and Imports

## Introduction

@import, pub declarations, and build.zig wiring. By the end of this lesson you will be able to: Import modules with @import; Expose declarations with pub; Understand the build.zig file layout.

## Key Concepts

### 1. Import modules with @import

Target: Import modules with @import. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```zig
// @import loads modules; pub exposes declarations
const std = @import("std");

pub fn main() void {
    std.debug.print("std is Zig's standard library\n", .{});
}

```
### 2. Expose declarations with pub

Target: Expose declarations with pub. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```zig
// Cross-file imports
// math.zig:
// pub fn add(a: i32, b: i32) i32 { return a + b; }
//
// main.zig:
// const math = @import("math.zig");
// const result = math.add(2, 3);

```
### 3. Understand the build.zig file layout

Target: Understand the build.zig file layout. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```zig
// pub const and pub fn create the public API
const std = @import("std");

const Greetings = struct {
    pub const DefaultName = "world";

    pub fn hello(name: []const u8) void {
        std.debug.print("Hello, {s}!\n", .{name});
    }
};

pub fn main() void {
    Greetings.hello(Greetings.DefaultName);
}

```
### 4. Import modules with @import

Target: Import modules with @import. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```zig
// build.zig wires files into build steps
// pub fn build(b: *std.Build) void {
//     const exe = b.addExecutable(.{
//         .name = "app",
//         .root_source_file = b.path("src/main.zig"),
//         .target = b.standardTargetOptions(.{}),
//     });
//     b.installArtifact(exe);
// }

```

## Practice Questions

1. What is the key idea behind "Modules and Imports"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Modules and Imports with analogies and real-world examples"
1. "Show me common mistakes beginners make with Modules and Imports"
1. "Provide advanced patterns and performance considerations for Modules and Imports"

## Key Takeaways

- Master the core ideas of Modules and Imports through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
