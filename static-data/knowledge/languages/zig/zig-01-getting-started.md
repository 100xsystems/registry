---
{
  "title": "Getting Started with Zig",
  "description": "Hello world, zig run, and the build system.",
  "type": "lesson",
  "order": 1,
  "duration": "20 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Run Zig code with zig run and zig build-exe",
    "Explain how Zig compiles to native code",
    "Use std.debug.print for output"
  ],
  "knowledge_refs": [
    "zig/zig-01-getting-started"
  ],
  "prerequisites": [],
  "references": [
    {
      "title": "Zig Language Reference",
      "url": "https://ziglang.org/documentation/master/"
    },
    {
      "title": "Zig Learn — Official Guide",
      "url": "https://ziglearn.org/"
    },
    {
      "title": "Ziglang — Home",
      "url": "https://ziglang.org/"
    }
  ]
}
---

# ZIG-01-GETTING-STARTED: Getting Started with Zig

## Introduction

Hello world, zig run, and the build system. By the end of this lesson you will be able to: Run Zig code with zig run and zig build-exe; Explain how Zig compiles to native code; Use std.debug.print for output.

## Key Concepts

### 1. Run Zig code with zig run and zig build-exe

Target: Run Zig code with zig run and zig build-exe. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```zig
// Your first Zig program
const std = @import("std");

pub fn main() void {
    std.debug.print("Hello, 100X Systems!\n", .{});
}
// Run with: zig run hello.zig

```
### 2. Explain how Zig compiles to native code

Target: Explain how Zig compiles to native code. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```zig
// Zig requires you to be explicit about everything
const std = @import("std");

pub fn main() void {
    const name = "Zig";
    std.debug.print("Hello, {s}!\n", .{name});
}

```
### 3. Use std.debug.print for output

Target: Use std.debug.print for output. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```zig
// Build system: zig build-exe and zig build
// zig build-exe hello.zig   -> produces ./hello
// zig build                 -> builds with build.zig
// A build.zig file defines build steps, targets, and dependencies.

```
### 4. Run Zig code with zig run and zig build-exe

Target: Run Zig code with zig run and zig build-exe. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```zig
// Compile-time awareness from the start
const std = @import("std");

pub fn main() void {
    // The {d} format specifier prints a decimal integer
    std.debug.print("2 + 2 = {d}\n", .{2 + 2});
}

```

## Practice Questions

1. What is the key idea behind "Getting Started with Zig"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Zig with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Zig"
1. "Provide advanced patterns and performance considerations for Getting Started with Zig"

## Key Takeaways

- Master the core ideas of Getting Started with Zig through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
