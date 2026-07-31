---
{
  "title": "Keyword Lists, Maps, and Sets",
  "description": "Keyword lists, map vs keyword trade-offs, and MapSet.",
  "type": "lesson",
  "order": 8,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use keyword lists",
    "Manipulate keyword lists",
    "Compare maps and keyword lists",
    "Use sets"
  ],
  "knowledge_refs": [
    "elixir/elixir-08-keywords-maps-sets"
  ],
  "prerequisites": [
    "ELIXIR-07"
  ],
  "references": [
    {
      "title": "Elixir — Keyword Lists and Maps",
      "url": "https://elixir-lang.org/getting-started/keywords-and-maps.html"
    },
    {
      "title": "Elixir — MapSet",
      "url": "https://hexdocs.pm/elixir/MapSet.html"
    },
    {
      "title": "Elixir — Keyword module",
      "url": "https://hexdocs.pm/elixir/Keyword.html"
    }
  ]
}
---

# ELIXIR-08-KEYWORDS-MAPS-SETS: Keyword Lists, Maps, and Sets

## Introduction

Keyword lists, map vs keyword trade-offs, and MapSet. By the end of this lesson you will be able to: Use keyword lists; Manipulate keyword lists; Compare maps and keyword lists; Use sets.

## Key Concepts

### 1. Use keyword lists

Target: Use keyword lists. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elixir
# Keyword lists: two-element tuples, ordered, duplicates allowed
kw = [name: "Alice", age: 30]
IO.inspect(kw[:name])        # "Alice"
IO.inspect(kw[:age])         # 30
kw2 = [name: "Bob", name: "Charlie"]  # duplicates allowed
IO.inspect(kw2[:name])       # "Bob" — first match
# Keyword lists are just [name: "Alice"] == [{:name, "Alice"}]
```
### 2. Manipulate keyword lists

Target: Manipulate keyword lists. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elixir
# Keyword list operations
kw = [a: 1, b: 2]
IO.inspect(Keyword.get(kw, :a))      # 1
IO.inspect(Keyword.get(kw, :z, 99))  # 99 — default
IO.inspect(Keyword.put(kw, :c, 3))   # [a: 1, b: 2, c: 3]
IO.inspect(Keyword.keys(kw))         # [:a, :b]
IO.inspect(Keyword.values(kw))       # [1, 2]
IO.inspect(Keyword.has_key?(kw, :b)) # true
```
### 3. Compare maps and keyword lists

Target: Compare maps and keyword lists. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elixir
# Maps vs keyword lists: when to use which
map = %{name: "Alice", age: 30}        # unordered, unique keys
IO.inspect(map.name)                   # dot access
IO.inspect(map[:name])                 # bracket access
IO.inspect(Map.fetch(map, :age))       # {:ok, 30}
IO.inspect(Map.fetch(map, :nope))      # :error
# Use maps for large/lookup-heavy data; keywords for options.
```
### 4. Use sets

Target: Use sets. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elixir
# Sets
set = MapSet.new([1, 2, 3])
IO.inspect(MapSet.member?(set, 2))   # true
IO.inspect(MapSet.size(set))         # 3
set2 = MapSet.new([3, 4, 5])
IO.inspect(MapSet.union(set, set2))  # MapSet.new([1, 2, 3, 4, 5])
IO.inspect(MapSet.intersection(set, set2))  # MapSet.new([3])
IO.inspect(MapSet.difference(set, set2))    # MapSet.new([1, 2])
```

## Practice Questions

1. What is the key idea behind "Keyword Lists, Maps, and Sets"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Keyword Lists, Maps, and Sets with analogies and real-world examples"
1. "Show me common mistakes beginners make with Keyword Lists, Maps, and Sets"
1. "Provide advanced patterns and performance considerations for Keyword Lists, Maps, and Sets"

## Key Takeaways

- Master the core ideas of Keyword Lists, Maps, and Sets through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
