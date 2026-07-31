---
{
  "title": "Getting Started with Elixir",
  "description": "Installation, IEx, modules, functions, and pattern matching basics.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write and run your first Elixir program",
    "Explore interactively with IEx",
    "Define modules and functions",
    "Match values with the = operator"
  ],
  "knowledge_refs": [
    "elixir/elixir-01-getting-started"
  ],
  "prerequisites": [],
  "references": [
    {
      "title": "Elixir — Getting Started",
      "url": "https://elixir-lang.org/getting-started/introduction.html"
    },
    {
      "title": "Elixir — Installation",
      "url": "https://elixir-lang.org/install.html"
    },
    {
      "title": "Elixir — IEx",
      "url": "https://hexdocs.pm/iex/IEx.html"
    }
  ]
}
---

# ELIXIR-01-GETTING-STARTED: Getting Started with Elixir

## Introduction

Installation, IEx, modules, functions, and pattern matching basics. By the end of this lesson you will be able to: Write and run your first Elixir program; Explore interactively with IEx; Define modules and functions; Match values with the = operator.

## Key Concepts

### 1. Write and run your first Elixir program

Target: Write and run your first Elixir program. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elixir
# Your first Elixir program
defmodule Hello do
  def world do
    IO.puts("Hello, 100X Systems!")
  end
end

Hello.world()
# run: elixir hello.exs  ->  Hello, 100X Systems!
```
### 2. Explore interactively with IEx

Target: Explore interactively with IEx. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elixir
# IEx interactive shell and basic expressions
# iex> 1 + 2
# 3
# iex> "Elixir" |> String.upcase()
# "ELIXIR"
IO.puts(Enum.map(1..5, &(&1 * &1)) |> Enum.join(", "))
# 1, 4, 9, 16, 25
```
### 3. Define modules and functions

Target: Define modules and functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elixir
# Modules, functions, and the dot syntax
defmodule Math do
  def add(a, b), do: a + b
  def multiply(a, b), do: a * b
end

IO.puts(Math.add(3, 4))       # 7
IO.puts(Math.multiply(3, 4))  # 12
```
### 4. Match values with the = operator

Target: Match values with the = operator. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elixir
# Pattern matching basics with =
{a, b, c} = {:ok, 42, "hello"}
IO.puts("#{a} #{b} #{c}")
# {:ok, 42, "hello"} destructured in one expression.
# The = operator is a match, not an assignment.
```

## Practice Questions

1. What is the key idea behind "Getting Started with Elixir"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Elixir with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Elixir"
1. "Provide advanced patterns and performance considerations for Getting Started with Elixir"

## Key Takeaways

- Master the core ideas of Getting Started with Elixir through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
