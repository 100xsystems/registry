---
{
  "title": "Metaprogramming",
  "description": "Symbols, expressions, macros, and code-as-data.",
  "type": "lesson",
  "order": 14,
  "duration": 40,
  "difficulty": "expert",
  "learning_objectives": [
    "Explain that Julia code is representable as data",
    "Build and evaluate expression trees",
    "Write macros that transform code at parse time"
  ],
  "knowledge_refs": [
    "julia/julia-14-metaprogramming"
  ],
  "prerequisites": [
    "julia-12-parametric-types"
  ],
  "references": [
    {
      "title": "Julia Manual — Metaprogramming",
      "url": "https://docs.julialang.org/en/v1/manual/metaprogramming/"
    },
    {
      "title": "Julia Manual — Macros",
      "url": "https://docs.julialang.org/en/v1/manual/metaprogramming/#Macros"
    },
    {
      "title": "Julia Manual — Generated Functions",
      "url": "https://docs.julialang.org/en/v1/manual/metaprogramming/#Generated-functions"
    }
  ]
}
---

# JULIA-14-METAPROGRAMMING: Metaprogramming

## Introduction

Symbols, expressions, macros, and code-as-data. By the end of this lesson you will be able to: Explain that Julia code is representable as data; Build and evaluate expression trees; Write macros that transform code at parse time.

## Key Concepts

### 1. Explain that Julia code is representable as data

Target: Explain that Julia code is representable as data. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```julia
# Symbols and expressions: code is data
s = :x
println(typeof(s))         # Symbol
expr = :(a + b)
println(expr.args)         # [:+, :a, :b] — the AST

```
### 2. Build and evaluate expression trees

Target: Build and evaluate expression trees. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```julia
# quote and eval: building expressions programmatically
ex = quote
    x = 40
    x + 2
end
println(eval(ex))          # 42

```
### 3. Write macros that transform code at parse time

Target: Write macros that transform code at parse time. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```julia
# Macros: functions on expressions, expanded at parse time
macro shout(ex)
    return :(uppercase($(esc(ex))))
end

println(@shout "hello")    # HELLO

```
### 4. Explain that Julia code is representable as data

Target: Explain that Julia code is representable as data. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```julia
# @time and @show — built-in utility macros
@show 2 + 2                # 2 + 2 = 4
@time sum(1:1_000_000)     # prints elapsed time

```

## Practice Questions

1. What is the key idea behind "Metaprogramming"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Metaprogramming with analogies and real-world examples"
1. "Show me common mistakes beginners make with Metaprogramming"
1. "Provide advanced patterns and performance considerations for Metaprogramming"

## Key Takeaways

- Master the core ideas of Metaprogramming through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
