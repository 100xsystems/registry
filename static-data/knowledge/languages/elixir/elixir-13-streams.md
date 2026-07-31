---
{
  "title": "Streams and Lazy Evaluation",
  "description": "Lazy enumerables, infinite streams, and streaming files.",
  "type": "lesson",
  "order": 13,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Build lazy streams",
    "Iterate infinite data",
    "Cycle and repeat values",
    "Stream files line by line"
  ],
  "knowledge_refs": [
    "elixir/elixir-13-streams"
  ],
  "prerequisites": [
    "ELIXIR-12"
  ],
  "references": [
    {
      "title": "Elixir — Enumerables and Streams",
      "url": "https://elixir-lang.org/getting-started/enumerables-and-streams.html"
    },
    {
      "title": "Elixir — Stream module",
      "url": "https://hexdocs.pm/elixir/Stream.html"
    },
    {
      "title": "Elixir School — Streams",
      "url": "https://elixirschool.com/en/lessons/basics/enum"
    }
  ]
}
---

# ELIXIR-13-STREAMS: Streams and Lazy Evaluation

## Introduction

Lazy enumerables, infinite streams, and streaming files. By the end of this lesson you will be able to: Build lazy streams; Iterate infinite data; Cycle and repeat values; Stream files line by line.

## Key Concepts

### 1. Build lazy streams

Target: Build lazy streams. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elixir
# Streams: lazy, composable enumerables
stream = 1..10_000_000
  |> Stream.map(&(&1 * &1))
  |> Stream.filter(&(&1 > 1_000_000))

IO.inspect(Enum.take(stream, 3))   # [1002001, 1008016, 1014049]
# Streams compute on demand — no intermediate lists.
```
### 2. Iterate infinite data

Target: Iterate infinite data. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elixir
# Streams for infinite data
natural = Stream.iterate(1, &(&1 + 1))
IO.inspect(Enum.take(natural, 5))   # [1, 2, 3, 4, 5]

# Fibonacci as a stream:
fibs = Stream.unfold({0, 1}, fn {a, b} -> {a, {b, a + b}} end)
IO.inspect(Enum.take(fibs, 8))      # [0, 1, 1, 2, 3, 5, 8, 13]
```
### 3. Cycle and repeat values

Target: Cycle and repeat values. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elixir
# Stream.cycle and Stream.repeatedly
cycled = Stream.cycle(["a", "b"])
IO.inspect(Enum.take(cycled, 5))   # ["a", "b", "a", "b", "a"]

repeated = Stream.repeatedly(fn -> :rand.uniform(100) end)
IO.inspect(Enum.take(repeated, 3))  # three random numbers
```
### 4. Stream files line by line

Target: Stream files line by line. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elixir
# Streaming file processing
# Reads lines lazily from a file, transforms, writes out:
result =
  "data.txt"
  |> File.stream!()
  |> Stream.map(&String.trim/1)
  |> Stream.reject(&(&1 == ""))
  |> Enum.count()

IO.puts("non-empty lines: #{result}")
# Without Stream, the whole file would load into memory.
```

## Practice Questions

1. What is the key idea behind "Streams and Lazy Evaluation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Streams and Lazy Evaluation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Streams and Lazy Evaluation"
1. "Provide advanced patterns and performance considerations for Streams and Lazy Evaluation"

## Key Takeaways

- Master the core ideas of Streams and Lazy Evaluation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
