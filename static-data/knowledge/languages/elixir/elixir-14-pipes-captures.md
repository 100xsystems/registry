---
{
  "title": "Pipes and Captures",
  "description": "The pipe operator, capture syntax, and operator captures.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read pipelines left to right",
    "Chain transforms with pipes",
    "Use capture shorthand",
    "Capture operators"
  ],
  "knowledge_refs": [
    "elixir/elixir-14-pipes-captures"
  ],
  "prerequisites": [
    "ELIXIR-13"
  ],
  "references": [
    {
      "title": "Elixir — The Pipe Operator",
      "url": "https://elixir-lang.org/getting-started/enumerables-and-streams.html#the-pipe-operator"
    },
    {
      "title": "Elixir — & capture",
      "url": "https://hexdocs.pm/elixir/Kernel.SpecialForms.html#&/1"
    },
    {
      "title": "Elixir School — Pipe Operator",
      "url": "https://elixirschool.com/en/lessons/basics/pipe-operator"
    }
  ]
}
---

# ELIXIR-14-PIPES-CAPTURES: Pipes and Captures

## Introduction

The pipe operator, capture syntax, and operator captures. By the end of this lesson you will be able to: Read pipelines left to right; Chain transforms with pipes; Use capture shorthand; Capture operators.

## Key Concepts

### 1. Read pipelines left to right

Target: Read pipelines left to right. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elixir
# The pipe operator: read it left to right
"hello world"
|> String.split()
|> Enum.map(&String.capitalize/1)
|> Enum.join(" ")
|> IO.puts()
# Hello World
```
### 2. Chain transforms with pipes

Target: Chain transforms with pipes. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elixir
# Pipes with function capture and args
[1, 2, 3, 4]
|> Enum.filter(&(&1 > 2))
|> Enum.map(&(&1 * 10))
|> Enum.join(",")
|> IO.puts()
# 30,40
```
### 3. Use capture shorthand

Target: Use capture shorthand. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elixir
# Captures: &(&1 + 1) shorthand
add = &(&1 + &1)
IO.puts(add.(3))            # 6

# Named function capture with arity:
mapped = Enum.map([1, 2, 3], &Integer.to_string/1)
IO.inspect(mapped)          # ["1", "2", "3"]
```
### 4. Capture operators

Target: Capture operators. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elixir
# Operator as function captures
IO.inspect(Enum.reduce([1, 2, 3], 0, &+/2))    # 6
IO.inspect(Enum.reduce([1, 2, 3], 1, &*/2))    # 6
IO.inspect(Enum.sort([3, 1, 2], &>=/2))        # [3, 2, 1]
# &+/2 captures the + operator as a two-arg function.
```

## Practice Questions

1. What is the key idea behind "Pipes and Captures"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Pipes and Captures with analogies and real-world examples"
1. "Show me common mistakes beginners make with Pipes and Captures"
1. "Provide advanced patterns and performance considerations for Pipes and Captures"

## Key Takeaways

- Master the core ideas of Pipes and Captures through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
