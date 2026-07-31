---
{
  "title": "Modules and Functions",
  "description": "Public/private functions, defaults, clauses, import, alias.",
  "type": "lesson",
  "order": 15,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Structure modules",
    "Use default arguments",
    "Write multi-clause functions",
    "Import and alias modules"
  ],
  "knowledge_refs": [
    "elixir/elixir-15-modules"
  ],
  "prerequisites": [
    "ELIXIR-14"
  ],
  "references": [
    {
      "title": "Elixir — Modules",
      "url": "https://elixir-lang.org/getting-started/modules-and-functions.html"
    },
    {
      "title": "Elixir — import/alias/require",
      "url": "https://elixir-lang.org/getting-started/alias-require-and-import.html"
    },
    {
      "title": "Elixir — defp",
      "url": "https://hexdocs.pm/elixir/Kernel.html#defp/2"
    }
  ]
}
---

# ELIXIR-15-MODULES: Modules and Functions

## Introduction

Public/private functions, defaults, clauses, import, alias. By the end of this lesson you will be able to: Structure modules; Use default arguments; Write multi-clause functions; Import and alias modules.

## Key Concepts

### 1. Structure modules

Target: Structure modules. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elixir
# Modules, public/private functions
defmodule Calc do
  def add(a, b), do: a + b        # public
  defp secret, do: :hidden        # private

  def double(x), do: x * 2
end

IO.puts(Calc.add(2, 3))
IO.puts(Calc.double(4))
# Calc.secret() would raise UndefinedFunctionError.
```
### 2. Use default arguments

Target: Use default arguments. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elixir
# Function default arguments
defmodule Greet do
  def hello(name, greeting \ "Hello") do
    "#{greeting}, #{name}!"
  end
end

IO.puts(Greet.hello("Alice"))            # Hello, Alice!
IO.puts(Greet.hello("Bob", "Hey"))       # Hey, Bob!
# Defaults must be defined in a header clause.
```
### 3. Write multi-clause functions

Target: Write multi-clause functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elixir
# Multi-clause functions with different arities
defmodule Shape do
  def area({:square, s}), do: s * s
  def area({:rect, w, h}), do: w * h
  def area({:circle, r}), do: 3.14159 * r * r
end

IO.puts(Shape.area({:square, 4}))   # 16
IO.puts(Shape.area({:circle, 2}))   # 12.56636
```
### 4. Import and alias modules

Target: Import and alias modules. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elixir
# Import, alias, and require
import Enum, only: [map: 2, sum: 1]
alias MyApp.Utils.Helper, as: H

IO.inspect(map([1, 2], &(&1 * 2)))   # [2, 4]
IO.inspect(sum([1, 2, 3]))           # 6

# Aliasing lets you reference H instead of the full name.
```

## Practice Questions

1. What is the key idea behind "Modules and Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Modules and Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Modules and Functions"
1. "Provide advanced patterns and performance considerations for Modules and Functions"

## Key Takeaways

- Master the core ideas of Modules and Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
