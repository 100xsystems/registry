---
{
  "title": "Collections and Enum",
  "description": "Enum, lists, maps, and comprehensions.",
  "type": "lesson",
  "order": 4,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Transform collections with Enum",
    "Build and manipulate lists",
    "Work with maps",
    "Write list comprehensions"
  ],
  "knowledge_refs": [
    "elixir/elixir-04-enumerable"
  ],
  "prerequisites": [
    "ELIXIR-03"
  ],
  "references": [
    {
      "title": "Elixir — Enum module",
      "url": "https://hexdocs.pm/elixir/Enum.html"
    },
    {
      "title": "Elixir — Lists and Tuples",
      "url": "https://elixir-lang.org/getting-started/basic-types.html#linked-lists"
    },
    {
      "title": "Elixir — Comprehensions",
      "url": "https://elixir-lang.org/getting-started/comprehensions.html"
    }
  ]
}
---

# ELIXIR-04-ENUMERABLE: Collections and Enum

## Introduction

Enum, lists, maps, and comprehensions. By the end of this lesson you will be able to: Transform collections with Enum; Build and manipulate lists; Work with maps; Write list comprehensions.

## Key Concepts

### 1. Transform collections with Enum

Target: Transform collections with Enum. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elixir
# Enum: the bread-and-butter of collections
IO.inspect(Enum.map([1, 2, 3], &(&1 * 2)))        # [2, 4, 6]
IO.inspect(Enum.filter([1, 2, 3, 4], &(&1 > 2)))  # [3, 4]
IO.inspect(Enum.reduce([1, 2, 3], 0, &(&1 + &2))) # 6
IO.inspect(Enum.sum([1, 2, 3]))                   # 6
```
### 2. Build and manipulate lists

Target: Build and manipulate lists. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elixir
# List operations
list = [3, 1, 2]
IO.inspect(Enum.sort(list))            # [1, 2, 3]
IO.inspect(Enum.reverse(list))         # [2, 1, 3]
IO.inspect(Enum.max(list))             # 3
IO.inspect(Enum.min(list))             # 1
IO.inspect(length(list))               # 3
IO.inspect([1, 2] ++ [3, 4])           # [1, 2, 3, 4]
IO.inspect([1, 2, 3] -- [2])           # [1, 3]
```
### 3. Work with maps

Target: Work with maps. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elixir
# Map operations
m = %{name: "Alice", age: 30}
IO.inspect(m[:name])           # Alice — access syntax
IO.inspect(Map.get(m, :age))   # 30
m2 = Map.put(m, :city, "NYC")  # new map, m unchanged
IO.inspect(Map.keys(m2))       # [:name, :age, :city]
IO.inspect(Map.has_key?(m, :name))  # true
```
### 4. Write list comprehensions

Target: Write list comprehensions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elixir
# Comprehensions
squares = for n <- 1..5, do: n * n
IO.inspect(squares)   # [1, 4, 9, 16, 25]

even_squares = for n <- 1..10, rem(n, 2) == 0, do: n * n
IO.inspect(even_squares)  # [4, 16, 36, 64, 100]

pairs = for a <- [1, 2], b <- ["x", "y"], do: {a, b}
IO.inspect(pairs)
# [{1, "x"}, {1, "y"}, {2, "x"}, {2, "y"}]
```

## Practice Questions

1. What is the key idea behind "Collections and Enum"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Collections and Enum with analogies and real-world examples"
1. "Show me common mistakes beginners make with Collections and Enum"
1. "Provide advanced patterns and performance considerations for Collections and Enum"

## Key Takeaways

- Master the core ideas of Collections and Enum through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
