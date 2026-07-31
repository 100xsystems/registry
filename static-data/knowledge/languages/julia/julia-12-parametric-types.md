---
{
  "title": "Abstract and Parametric Types",
  "description": "Type parameters, unions, and the type hierarchy.",
  "type": "lesson",
  "order": 12,
  "duration": 35,
  "difficulty": "intermediate",
  "learning_objectives": [
    "Parameterize structs with type variables",
    "Use Union types to allow multiple types",
    "Navigate the type hierarchy with <:"
  ],
  "knowledge_refs": [
    "julia/julia-12-parametric-types"
  ],
  "prerequisites": [
    "julia-11-structs"
  ],
  "references": [
    {
      "title": "Julia Manual — Parametric Types",
      "url": "https://docs.julialang.org/en/v1/manual/types/#Parametric-Types"
    },
    {
      "title": "Julia Manual — UnionAll Types",
      "url": "https://docs.julialang.org/en/v1/manual/types/#UnionAll-Types"
    }
  ]
}
---

# JULIA-12-PARAMETRIC-TYPES: Abstract and Parametric Types

## Introduction

Type parameters, unions, and the type hierarchy. By the end of this lesson you will be able to: Parameterize structs with type variables; Use Union types to allow multiple types; Navigate the type hierarchy with <:.

## Key Concepts

### 1. Parameterize structs with type variables

Target: Parameterize structs with type variables. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```julia
# Parametric types: parameterize on the element type
struct Box{T}
    contents::T
end

b1 = Box(42)               # Box{Int64}
b2 = Box("hi")             # Box{String}
println(b1.contents)       # 42

```
### 2. Use Union types to allow multiple types

Target: Use Union types to allow multiple types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```julia
# Union types and Any
x::Union{Int, String} = 42
println(x)                 # 42
y::Any = "anything"
println(y)                 # anything

```
### 3. Navigate the type hierarchy with <:

Target: Navigate the type hierarchy with <:. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```julia
# Type hierarchy: Int <: Signed <: Integer <: Real <: Number
println(Int <: Integer)    # true
println(Integer <: Real)   # true
println(Real <: Number)    # true

```
### 4. Parameterize structs with type variables

Target: Parameterize structs with type variables. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```julia
# Type annotations give performance AND safety
function scale(x::Float64, k::Float64)
    x * k
end

println(scale(2.0, 3.0))   # 6.0
# scale(2, 3) would throw MethodError — that is a feature!

```

## Practice Questions

1. What is the key idea behind "Abstract and Parametric Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Abstract and Parametric Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Abstract and Parametric Types"
1. "Provide advanced patterns and performance considerations for Abstract and Parametric Types"

## Key Takeaways

- Master the core ideas of Abstract and Parametric Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
