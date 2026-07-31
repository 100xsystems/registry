---
{
  "title": "Values, Types, and Immutability",
  "description": "Immutable data, atoms, strings, numbers, and booleans.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Explain immutability and rebinding",
    "Use atoms, strings, and numbers",
    "Perform arithmetic and division",
    "Manipulate strings"
  ],
  "knowledge_refs": [
    "elixir/elixir-02-values-types"
  ],
  "prerequisites": [
    "ELIXIR-01"
  ],
  "references": [
    {
      "title": "Elixir — Basic Types",
      "url": "https://elixir-lang.org/getting-started/basic-types.html"
    },
    {
      "title": "Elixir — Strings",
      "url": "https://elixir-lang.org/getting-started/basic-types.html#strings"
    },
    {
      "title": "Elixir — Operators",
      "url": "https://hexdocs.pm/elixir/operators.html"
    }
  ]
}
---

# ELIXIR-02-VALUES-TYPES: Values, Types, and Immutability

## Introduction

Immutable data, atoms, strings, numbers, and booleans. By the end of this lesson you will be able to: Explain immutability and rebinding; Use atoms, strings, and numbers; Perform arithmetic and division; Manipulate strings.

## Key Concepts

### 1. Explain immutability and rebinding

Target: Explain immutability and rebinding. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elixir
# Immutable values: rebinding vs mutation
x = 1
x = x + 1            # rebinding — a NEW binding, x is never mutated
IO.puts(x)           # 2

list = [1, 2, 3]
new_list = [0 | list]        # prepend, original untouched
IO.inspect(list)             # [1, 2, 3]
IO.inspect(new_list)         # [0, 1, 2, 3]
# Everything is immutable; "changes" produce new values.
```
### 2. Use atoms, strings, and numbers

Target: Use atoms, strings, and numbers. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elixir
# Data types: atoms, strings, numbers, booleans
IO.inspect(:ok)                    # atom
IO.inspect("double quoted")        # binary string
IO.inspect('single quoted')        # charlist (list of codepoints)
IO.inspect(42)                     # integer
IO.inspect(3.14)                   # float
IO.inspect(true)                   # boolean (an atom)
IO.inspect(nil)                    # nil (an atom)
# Atoms are constants whose name is their value.
```
### 3. Perform arithmetic and division

Target: Perform arithmetic and division. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elixir
# Arithmetic and division
IO.inspect(10 / 2)     # 5.0 — always returns a float
IO.inspect(div(10, 3)) # 3 — integer division
IO.inspect(rem(10, 3)) # 1 — remainder
IO.inspect(10 ** 2)    # 100 — exponentiation
```
### 4. Manipulate strings

Target: Manipulate strings. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elixir
# String basics: interpolation and concatenation
name = "Elixir"
IO.puts("Hello, #{name}!")        # interpolation
IO.puts("a" <> "b")               # concatenation -> "ab"
IO.puts(String.length("héllo"))   # 5 — counts graphemes
IO.puts(String.upcase("hello"))   # HELLO
# Strings are UTF-8 binaries, not arrays of bytes.
```

## Practice Questions

1. What is the key idea behind "Values, Types, and Immutability"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Values, Types, and Immutability with analogies and real-world examples"
1. "Show me common mistakes beginners make with Values, Types, and Immutability"
1. "Provide advanced patterns and performance considerations for Values, Types, and Immutability"

## Key Takeaways

- Master the core ideas of Values, Types, and Immutability through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
