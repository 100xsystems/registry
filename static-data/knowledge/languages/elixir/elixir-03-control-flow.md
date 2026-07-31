---
{
  "title": "Control Flow",
  "description": "case, cond, if/unless, and pattern-matched function clauses.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Match with case and guards",
    "Chain conditions with cond",
    "Use if and unless",
    "Write multi-clause functions"
  ],
  "knowledge_refs": [
    "elixir/elixir-03-control-flow"
  ],
  "prerequisites": [
    "ELIXIR-02"
  ],
  "references": [
    {
      "title": "Elixir — case, cond, if",
      "url": "https://elixir-lang.org/getting-started/case-cond-and-if.html"
    },
    {
      "title": "Elixir — Pattern Matching",
      "url": "https://elixir-lang.org/getting-started/pattern-matching.html"
    },
    {
      "title": "Elixir — Guards",
      "url": "https://hexdocs.pm/elixir/guards.html"
    }
  ]
}
---

# ELIXIR-03-CONTROL-FLOW: Control Flow

## Introduction

case, cond, if/unless, and pattern-matched function clauses. By the end of this lesson you will be able to: Match with case and guards; Chain conditions with cond; Use if and unless; Write multi-clause functions.

## Key Concepts

### 1. Match with case and guards

Target: Match with case and guards. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elixir
# case: pattern matching with guards
defmodule Describe do
  def of(x) do
    case x do
      0 -> "zero"
      n when n < 0 -> "negative"
      n when n > 0 -> "positive"
      _ -> "unknown"
    end
  end
end

IO.puts(Describe.of(-5))  # negative
```
### 2. Chain conditions with cond

Target: Chain conditions with cond. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elixir
# cond: the else-if chain
defmodule Rating do
  def label(score) do
    cond do
      score >= 90 -> "excellent"
      score >= 70 -> "good"
      score >= 50 -> "fair"
      true -> "poor"
    end
  end
end

IO.puts(Rating.label(85))  # good
```
### 3. Use if and unless

Target: Use if and unless. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elixir
# if / unless
if true do
  IO.puts("if runs")
end

unless false do
  IO.puts("unless runs when false")
end

# if is a macro returning a value:
result = if 1 + 1 == 2, do: "math works", else: "broken"
IO.puts(result)
```
### 4. Write multi-clause functions

Target: Write multi-clause functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elixir
# Multiple function clauses via pattern matching
defmodule Fact do
  def of(0), do: 1
  def of(n) when n > 0, do: n * of(n - 1)
end

IO.puts(Fact.of(5))   # 120
# The first matching clause wins — no if/else needed.
```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
