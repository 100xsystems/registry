---
{
  "title": "Pattern Matching in Depth",
  "description": "Function-head matching, guards, pinning, and list patterns.",
  "type": "lesson",
  "order": 9,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Match in function heads",
    "Write guards",
    "Pin values with ^",
    "Match list shapes"
  ],
  "knowledge_refs": [
    "elixir/elixir-09-pattern-matching"
  ],
  "prerequisites": [
    "ELIXIR-08"
  ],
  "references": [
    {
      "title": "Elixir — Pattern Matching",
      "url": "https://elixir-lang.org/getting-started/pattern-matching.html"
    },
    {
      "title": "Elixir — Guards reference",
      "url": "https://hexdocs.pm/elixir/guards.html"
    },
    {
      "title": "Elixir — Multi-clause functions",
      "url": "https://elixir-lang.org/getting-started/modules-and-functions.html#default-arguments"
    }
  ]
}
---

# ELIXIR-09-PATTERN-MATCHING: Pattern Matching in Depth

## Introduction

Function-head matching, guards, pinning, and list patterns. By the end of this lesson you will be able to: Match in function heads; Write guards; Pin values with ^; Match list shapes.

## Key Concepts

### 1. Match in function heads

Target: Match in function heads. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elixir
# Pattern matching in function heads
defmodule Greet do
  def hello(%{name: name}), do: "Hello, #{name}!"
  def hello(_), do: "Hello, stranger!"
end

IO.puts(Greet.hello(%{name: "Alice"}))   # Hello, Alice!
IO.puts(Greet.hello(%{}))                # Hello, stranger!
```
### 2. Write guards

Target: Write guards. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elixir
# Guards: validating function arguments
defmodule Age do
  def classify(n) when is_integer(n) and n >= 18, do: "adult"
  def classify(n) when is_integer(n), do: "minor"
  def classify(_), do: "not a number"
end

IO.puts(Age.classify(21))   # adult
IO.puts(Age.classify(10))   # minor
IO.puts(Age.classify("x"))  # not a number
```
### 3. Pin values with ^

Target: Pin values with ^. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elixir
# Pinning with ^: matching existing values
x = 10
case 10 do
  ^x -> "matches the pinned value"
  _ -> "no match"
end
# Without ^, x would be REBOUND inside the clause.
```
### 4. Match list shapes

Target: Match list shapes. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elixir
# Match on list shapes
defmodule Listy do
  def describe([]), do: "empty"
  def describe([x]), do: "one element: #{x}"
  def describe([x | rest]), do: "#{x} plus #{length(rest)} more"
end

IO.puts(Listy.describe([]))          # empty
IO.puts(Listy.describe([42]))        # one element: 42
IO.puts(Listy.describe([1, 2, 3]))   # 1 plus 2 more
```

## Practice Questions

1. What is the key idea behind "Pattern Matching in Depth"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Pattern Matching in Depth with analogies and real-world examples"
1. "Show me common mistakes beginners make with Pattern Matching in Depth"
1. "Provide advanced patterns and performance considerations for Pattern Matching in Depth"

## Key Takeaways

- Master the core ideas of Pattern Matching in Depth through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
