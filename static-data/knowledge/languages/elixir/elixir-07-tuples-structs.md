---
{
  "title": "Tuples and Structs",
  "description": "Tuples, the {:ok, _}/{:error, _} convention, and structs.",
  "type": "lesson",
  "order": 7,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use tuples",
    "Follow the ok/error convention",
    "Match tuple results",
    "Define and update structs"
  ],
  "knowledge_refs": [
    "elixir/elixir-07-tuples-structs"
  ],
  "prerequisites": [
    "ELIXIR-06"
  ],
  "references": [
    {
      "title": "Elixir — Tuples",
      "url": "https://elixir-lang.org/getting-started/basic-types.html#tuples"
    },
    {
      "title": "Elixir — Structs",
      "url": "https://elixir-lang.org/getting-started/structs.html"
    },
    {
      "title": "Elixir — Case (ok/error)",
      "url": "https://elixir-lang.org/getting-started/case-cond-and-if.html"
    }
  ]
}
---

# ELIXIR-07-TUPLES-STRUCTS: Tuples and Structs

## Introduction

Tuples, the {:ok, _}/{:error, _} convention, and structs. By the end of this lesson you will be able to: Use tuples; Follow the ok/error convention; Match tuple results; Define and update structs.

## Key Concepts

### 1. Use tuples

Target: Use tuples. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elixir
# Tuples: fixed-size containers
t = {:ok, 42}
IO.inspect(elem(t, 0))    # :ok
IO.inspect(elem(t, 1))    # 42
t2 = put_elem(t, 1, 100)
IO.inspect(t2)            # {:ok, 100}
IO.inspect(tuple_size(t)) # 2
```
### 2. Follow the ok/error convention

Target: Follow the ok/error convention. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elixir
# The {:ok, result} / {:error, reason} convention
defmodule Div do
  def divide(a, b) do
    if b == 0 do
      {:error, "division by zero"}
    else
      {:ok, a / b}
    end
  end
end

case Div.divide(10, 2) do
  {:ok, v} -> IO.puts("result: #{v}")
  {:error, msg} -> IO.puts("error: #{msg}")
end
```
### 3. Match tuple results

Target: Match tuple results. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elixir
# Pattern matching tuples with case
defmodule Result do
  def handle({:ok, value}), do: "ok: #{value}"
  def handle({:error, reason}), do: "error: #{reason}"
end

IO.puts(Result.handle({:ok, 7}))      # ok: 7
IO.puts(Result.handle({:error, :oops})) # error: oops
```
### 4. Define and update structs

Target: Define and update structs. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elixir
# Structs: maps with a shape
defmodule User do
  defstruct [:name, :age, :city]
end

u = %User{name: "Alice", age: 30}
IO.inspect(u.name)              # "Alice"
u2 = %{u | age: 31}             # update syntax
IO.inspect(u2.age)              # 31
IO.inspect(u.age)               # 30 — original unchanged
# Structs enforce their keys and provide defaults.
```

## Practice Questions

1. What is the key idea behind "Tuples and Structs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Tuples and Structs with analogies and real-world examples"
1. "Show me common mistakes beginners make with Tuples and Structs"
1. "Provide advanced patterns and performance considerations for Tuples and Structs"

## Key Takeaways

- Master the core ideas of Tuples and Structs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
