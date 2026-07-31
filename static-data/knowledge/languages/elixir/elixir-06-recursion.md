---
{
  "title": "Recursion",
  "description": "Recursive thinking, tail calls, and building results.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Loop with recursion",
    "Use tail-call recursion",
    "Recurse over linked lists",
    "Build results recursively"
  ],
  "knowledge_refs": [
    "elixir/elixir-06-recursion"
  ],
  "prerequisites": [
    "ELIXIR-05"
  ],
  "references": [
    {
      "title": "Elixir — Recursion",
      "url": "https://elixir-lang.org/getting-started/recursion.html"
    },
    {
      "title": "Elixir — Tail Calls",
      "url": "https://hexdocs.pm/elixir/Kernel.html#def/2"
    },
    {
      "title": "Elixir School — Recursion",
      "url": "https://elixirschool.com/en/lessons/basics/collections"
    }
  ]
}
---

# ELIXIR-06-RECURSION: Recursion

## Introduction

Recursive thinking, tail calls, and building results. By the end of this lesson you will be able to: Loop with recursion; Use tail-call recursion; Recurse over linked lists; Build results recursively.

## Key Concepts

### 1. Loop with recursion

Target: Loop with recursion. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elixir
# Recursion: the Elixir way to loop
defmodule Count do
  def up_to(0), do: 0
  def up_to(n), do: n + up_to(n - 1)
end

IO.puts(Count.up_to(5))   # 15 (5+4+3+2+1+0)
```
### 2. Use tail-call recursion

Target: Use tail-call recursion. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elixir
# Tail-call recursion with an accumulator
defmodule Sum do
  def of(list), do: do_sum(list, 0)
  defp do_sum([], acc), do: acc
  defp do_sum([h | t], acc), do: do_sum(t, acc + h)
end

IO.puts(Sum.of([1, 2, 3, 4]))   # 10
# The recursive call is the LAST thing evaluated — tail call
# optimized, so deep recursion never blows the stack.
```
### 3. Recurse over linked lists

Target: Recurse over linked lists. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elixir
# Recursing over linked lists
defmodule Len do
  def of([]), do: 0
  def of([_h | t]), do: 1 + Len.of(t)
end

IO.puts(Len.of([1, 2, 3]))   # 3
# Each step peels off the head; the tail is the rest.
```
### 4. Build results recursively

Target: Build results recursively. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elixir
# List recursion building results
defmodule Evens do
  def only(list), do: collect(list, [])
  defp collect([], acc), do: Enum.reverse(acc)
  defp collect([h | t], acc) when rem(h, 2) == 0,
    do: collect(t, [h | acc])
  defp collect([_h | t], acc), do: collect(t, acc)
end

IO.inspect(Evens.only([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
```

## Practice Questions

1. What is the key idea behind "Recursion"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Recursion with analogies and real-world examples"
1. "Show me common mistakes beginners make with Recursion"
1. "Provide advanced patterns and performance considerations for Recursion"

## Key Takeaways

- Master the core ideas of Recursion through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
