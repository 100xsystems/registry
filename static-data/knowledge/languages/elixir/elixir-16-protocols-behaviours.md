---
{
  "title": "Protocols and Behaviours",
  "description": "Protocols for polymorphism, behaviours as interfaces.",
  "type": "lesson",
  "order": 16,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define protocols",
    "Implement protocols for structs",
    "Use behaviours",
    "Extend built-in protocols"
  ],
  "knowledge_refs": [
    "elixir/elixir-16-protocols-behaviours"
  ],
  "prerequisites": [
    "ELIXIR-15"
  ],
  "references": [
    {
      "title": "Elixir — Protocols",
      "url": "https://elixir-lang.org/getting-started/protocols.html"
    },
    {
      "title": "Elixir — Behaviours",
      "url": "https://elixir-lang.org/getting-started/modules-and-functions.html#behaviours"
    },
    {
      "title": "Elixir — String.Chars",
      "url": "https://hexdocs.pm/elixir/String.Chars.html"
    }
  ]
}
---

# ELIXIR-16-PROTOCOLS-BEHAVIOURS: Protocols and Behaviours

## Introduction

Protocols for polymorphism, behaviours as interfaces. By the end of this lesson you will be able to: Define protocols; Implement protocols for structs; Use behaviours; Extend built-in protocols.

## Key Concepts

### 1. Define protocols

Target: Define protocols. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elixir
# Protocols: polymorphism without inheritance
defprotocol Size do
  def size(data)
end

defimpl Size, for: List do
  def size(list), do: length(list)
end

defimpl Size, for: Map do
  def size(map), do: map_size(map)
end

defimpl Size, for: BitString do
  def size(str), do: String.length(str)
end

IO.puts(Size.size([1, 2, 3]))    # 3
IO.puts(Size.size(%{a: 1}))      # 1
IO.puts(Size.size("hello"))      # 5
# Protocols dispatch on the data type.
```
### 2. Implement protocols for structs

Target: Implement protocols for structs. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elixir
# Implementing a protocol for your own struct
defprotocol Greet do
  def hello(entity)
end

defmodule Human do
  defstruct [:name]
end

defimpl Greet, for: Human do
  def hello(%Human{name: n}), do: "Hello, #{n}!"
end

IO.puts(Greet.hello(%Human{name: "Alice"}))
# New types can implement the protocol without editing it.
```
### 3. Use behaviours

Target: Use behaviours. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elixir
# Behaviours: interfaces for modules
defmodule Worker do
  @callback perform(args :: term) :: term
  @optional_callbacks perform: 1
end

defmodule MyWorker do
  @behaviour Worker

  @impl Worker
  def perform(input), do: {:processed, input}
end

IO.inspect(MyWorker.perform(:data))
# @impl raises a warning if the callback signature drifts.
```
### 4. Extend built-in protocols

Target: Extend built-in protocols. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elixir
# The String.Chars protocol: to_string
IO.puts(to_string(42))          # "42"
IO.puts("#{42}")                # uses String.Chars

defmodule Point do
  defstruct [:x, :y]
  defimpl String.Chars do
    def to_string(%Point{x: x, y: y}), do: "Point(#{x}, #{y})"
  end
end

IO.puts("#{struct(Point, x: 1, y: 2)}")   # Point(1, 2)
```

## Practice Questions

1. What is the key idea behind "Protocols and Behaviours"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Protocols and Behaviours with analogies and real-world examples"
1. "Show me common mistakes beginners make with Protocols and Behaviours"
1. "Provide advanced patterns and performance considerations for Protocols and Behaviours"

## Key Takeaways

- Master the core ideas of Protocols and Behaviours through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
