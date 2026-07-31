---
{
  "title": "Functions and the Pipe",
  "description": "Anonymous functions, captures, closures, and the pipe operator.",
  "type": "lesson",
  "order": 5,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define anonymous functions",
    "Use the capture syntax",
    "Understand closures",
    "Compose with pipes"
  ],
  "knowledge_refs": [
    "elixir/elixir-05-functions"
  ],
  "prerequisites": [
    "ELIXIR-04"
  ],
  "references": [
    {
      "title": "Elixir — Anonymous Functions",
      "url": "https://elixir-lang.org/getting-started/modules-and-functions.html#anonymous-functions"
    },
    {
      "title": "Elixir — The Pipe Operator",
      "url": "https://elixir-lang.org/getting-started/enumerables-and-streams.html#the-pipe-operator"
    },
    {
      "title": "Elixir — Captures",
      "url": "https://hexdocs.pm/elixir/Kernel.SpecialForms.html#&/1"
    }
  ]
}
---

# ELIXIR-05-FUNCTIONS: Functions and the Pipe

## Introduction

Anonymous functions, captures, closures, and the pipe operator. By the end of this lesson you will be able to: Define anonymous functions; Use the capture syntax; Understand closures; Compose with pipes.

## Key Concepts

### 1. Define anonymous functions

Target: Define anonymous functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elixir
# Anonymous functions and capture syntax
double = fn x -> x * 2 end
IO.puts(double.(4))            # 8 — note the dot for calling

square = &(&1 * &1)
IO.puts(square.(5))            # 25

# Pipes compose functions left to right:
result = 1..10
  |> Enum.map(&(&1 * &1))
  |> Enum.filter(&(&1 > 20))
  |> Enum.sum()
IO.puts(result)   # 4+9+16+25+36+49+64+81+100 = 384
```
### 2. Use the capture syntax

Target: Use the capture syntax. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elixir
# Higher-order functions: passing functions around
add_one = &(&1 + 1)
IO.inspect(Enum.map([1, 2, 3], add_one))   # [2, 3, 4]

apply_twice = fn f, x -> f.(f.(x)) end
IO.puts(apply_twice.(add_one, 5))          # 7
```
### 3. Understand closures

Target: Understand closures. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elixir
# Closures capture their environment
defmodule Counter do
  def make(start) do
    fn -> start end
  end
end

get = Counter.make(100)
IO.puts(get.())     # 100 — the closure keeps start alive

# A counter that captures and returns a tuple:
make_counter = fn ->
  count = 0
  fn -> count = count + 1; count end
end
# (In Elixir, rebinding inside the closure creates a new
#  binding each call — use Agent/Process for real state.)
```
### 4. Compose with pipes

Target: Compose with pipes. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elixir
# Function composition with the pipe operator
defmodule Pipe do
  def run do
    42
    |> Integer.to_string()
    |> String.reverse()
    |> String.to_integer()
  end
end

IO.puts(Pipe.run())  # 24
# The pipe threads the previous result as the first arg.
```

## Practice Questions

1. What is the key idea behind "Functions and the Pipe"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions and the Pipe with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions and the Pipe"
1. "Provide advanced patterns and performance considerations for Functions and the Pipe"

## Key Takeaways

- Master the core ideas of Functions and the Pipe through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
