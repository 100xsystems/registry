---
{
  "title": "Structs",
  "description": "Fields, methods, mutation, and defaults.",
  "type": "lesson",
  "order": 11,
  "duration": "30 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define structs with typed fields",
    "Write methods on structs",
    "Use default field values"
  ],
  "knowledge_refs": [
    "zig/zig-11-structs"
  ],
  "prerequisites": [
    "zig-05-functions"
  ],
  "references": [
    {
      "title": "Zig Reference — Structs",
      "url": "https://ziglang.org/documentation/master/#struct"
    },
    {
      "title": "Zig Reference — Containers",
      "url": "https://ziglang.org/documentation/master/#Containers"
    }
  ]
}
---

# ZIG-11-STRUCTS: Structs

## Introduction

Fields, methods, mutation, and defaults. By the end of this lesson you will be able to: Define structs with typed fields; Write methods on structs; Use default field values.

## Key Concepts

### 1. Define structs with typed fields

Target: Define structs with typed fields. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```zig
// Structs: named fields with types
const std = @import("std");

const Point = struct {
    x: f64,
    y: f64,
};

pub fn main() void {
    const p = Point{ .x = 1.0, .y = 2.0 };
    std.debug.print("{d} {d}\n", .{ p.x, p.y });
}

```
### 2. Write methods on structs

Target: Write methods on structs. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```zig
// Methods are just functions whose first param is self
const std = @import("std");

const Rectangle = struct {
    width: f64,
    height: f64,

    fn area(self: Rectangle) f64 {
        return self.width * self.height;
    }
};

pub fn main() void {
    const r = Rectangle{ .width = 3.0, .height = 4.0 };
    std.debug.print("{d}\n", .{r.area()});   // 12
}

```
### 3. Use default field values

Target: Use default field values. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```zig
// Mutable structs: declare var and mutate fields
const std = @import("std");

const Counter = struct {
    value: i32,

    fn increment(self: *Counter) void {
        self.value += 1;
    }
};

pub fn main() void {
    var c = Counter{ .value = 0 };
    c.increment();
    c.increment();
    std.debug.print("{d}\n", .{c.value});   // 2
}

```
### 4. Define structs with typed fields

Target: Define structs with typed fields. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```zig
// Default field values
const std = @import("std");

const Config = struct {
    host: []const u8 = "localhost",
    port: u16 = 8080,
};

pub fn main() void {
    const cfg = Config{};
    std.debug.print("{s}:{d}\n", .{ cfg.host, cfg.port });
}

```

## Practice Questions

1. What is the key idea behind "Structs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Structs with analogies and real-world examples"
1. "Show me common mistakes beginners make with Structs"
1. "Provide advanced patterns and performance considerations for Structs"

## Key Takeaways

- Master the core ideas of Structs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
