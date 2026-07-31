---
{
  "title": "Real-World Pipelines",
  "description": "Text analysis, word counting, struct pipelines, and reduce.",
  "type": "lesson",
  "order": 20,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Analyse text with pipelines",
    "Count words with reduce",
    "Transform struct collections",
    "Run a running maximum"
  ],
  "knowledge_refs": [
    "elixir/elixir-20-pipelines"
  ],
  "prerequisites": [
    "ELIXIR-19"
  ],
  "references": [
    {
      "title": "Elixir — Enum.reduce",
      "url": "https://hexdocs.pm/elixir/Enum.html#reduce/3"
    },
    {
      "title": "Elixir School — Enum",
      "url": "https://elixirschool.com/en/lessons/basics/enum"
    },
    {
      "title": "Elixir — Map.update",
      "url": "https://hexdocs.pm/elixir/Map.html#update/4"
    }
  ]
}
---

# ELIXIR-20-PIPELINES: Real-World Pipelines

## Introduction

Text analysis, word counting, struct pipelines, and reduce. By the end of this lesson you will be able to: Analyse text with pipelines; Count words with reduce; Transform struct collections; Run a running maximum.

## Key Concepts

### 1. Analyse text with pipelines

Target: Analyse text with pipelines. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elixir
# The |> pipeline in real code
defmodule TextStats do
  def analyze(text) do
    text
    |> String.split()
    |> Enum.map(&String.downcase/1)
    |> Enum.frequencies()
    |> Enum.max_by(fn {_w, c} -> c end)
  end
end

IO.inspect(TextStats.analyze("the quick the brown the fox"))
# {"the", 3}
```
### 2. Count words with reduce

Target: Count words with reduce. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elixir
# Building a small CLI-ish pipeline
defmodule WordCounter do
  def run(lines) do
    lines
    |> Enum.flat_map(&String.split/1)
    |> Enum.reduce(%{}, fn word, acc ->
      Map.update(acc, word, 1, &(&1 + 1))
    end)
    |> Enum.sort_by(fn {_w, c} -> -c end)
    |> Enum.take(3)
  end
end

IO.inspect(WordCounter.run(["hi ho", "hi again", "hi"]))
# [{"hi", 3}, {"ho", 1}, {"again", 1}]
```
### 3. Transform struct collections

Target: Transform struct collections. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elixir
# Pattern: data transformation pipeline with structs
defmodule Order do
  defstruct [:id, :total]
end

orders = [
  %Order{id: 1, total: 100},
  %Order{id: 2, total: 50},
  %Order{id: 3, total: 200}
]

total =
  orders
  |> Enum.map(& &1.total)
  |> Enum.sum()

IO.puts("order total: #{total}")   # 350
```
### 4. Run a running maximum

Target: Run a running maximum. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elixir
# Guarding pipelines with Enum.reduce
defmodule RunningMax do
  def over(list) do
    list
    |> Enum.reduce(0, fn x, acc -> max(x, acc) end)
  end
end

IO.puts(RunningMax.over([3, 9, 4, 11, 2]))   # 11
# reduce threads an accumulator through the whole list.
```

## Practice Questions

1. What is the key idea behind "Real-World Pipelines"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Real-World Pipelines with analogies and real-world examples"
1. "Show me common mistakes beginners make with Real-World Pipelines"
1. "Provide advanced patterns and performance considerations for Real-World Pipelines"

## Key Takeaways

- Master the core ideas of Real-World Pipelines through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
