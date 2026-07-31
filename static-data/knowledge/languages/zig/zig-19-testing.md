---
{
  "title": "Testing",
  "description": "test blocks, expect, expectError, and test organization.",
  "type": "lesson",
  "order": 19,
  "duration": 30,
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write test blocks run with zig test",
    "Assert with std.testing.expect",
    "Expect errors with expectError"
  ],
  "knowledge_refs": [
    "zig/zig-19-testing"
  ],
  "prerequisites": [
    "zig-07-errors"
  ],
  "references": [
    {
      "title": "Zig Reference — Testing",
      "url": "https://ziglang.org/documentation/master/#Testing"
    },
    {
      "title": "Zig Guide — Testing",
      "url": "https://zig.guide/testing/"
    }
  ]
}
---

# ZIG-19-TESTING: Testing

## Introduction

test blocks, expect, expectError, and test organization. By the end of this lesson you will be able to: Write test blocks run with zig test; Assert with std.testing.expect; Expect errors with expectError.

## Key Concepts

### 1. Write test blocks run with zig test

Target: Write test blocks run with zig test. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```zig
// test blocks compile and run with `zig test`
const std = @import("std");

fn add(a: i32, b: i32) i32 {
    return a + b;
}

test "add adds numbers" {
    try std.testing.expectEqual(@as(i32, 5), add(2, 3));
}

// Run with: zig test file.zig

```
### 2. Assert with std.testing.expect

Target: Assert with std.testing.expect. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```zig
// Testing errors with expectError
const std = @import("std");

fn divide(a: i32, b: i32) !i32 {
    if (b == 0) return error.DivisionByZero;
    return a / b;
}

test "divide by zero" {
    try std.testing.expectError(error.DivisionByZero, divide(1, 0));
}

```
### 3. Expect errors with expectError

Target: Expect errors with expectError. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```zig
// expectEqualDeep and standard testing helpers
const std = @import("std");

test "deep equality" {
    try std.testing.expectEqualDeep(&[_]i32{ 1, 2 }, &[_]i32{ 1, 2 });
    try std.testing.expect(true);
}

```
### 4. Write test blocks run with zig test

Target: Write test blocks run with zig test. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```zig
// Test organization: many small focused tests
const std = @import("std");

fn isEven(n: i32) bool {
    return n % 2 == 0;
}

test "even numbers" {
    try std.testing.expect(isEven(2));
    try std.testing.expect(isEven(100));
}

test "odd numbers" {
    try std.testing.expect(!isEven(3));
}

```

## Practice Questions

1. What is the key idea behind "Testing"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Testing with analogies and real-world examples"
1. "Show me common mistakes beginners make with Testing"
1. "Provide advanced patterns and performance considerations for Testing"

## Key Takeaways

- Master the core ideas of Testing through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
