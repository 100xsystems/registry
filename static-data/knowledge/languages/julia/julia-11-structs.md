---
{
  "title": "Composite Types and Structs",
  "description": "Immutable and mutable structs, inner constructors.",
  "type": "lesson",
  "order": 11,
  "duration": 35,
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define immutable structs with typed fields",
    "Define mutable structs for stateful objects",
    "Write inner constructors with validation"
  ],
  "knowledge_refs": [
    "julia/julia-11-structs"
  ],
  "prerequisites": [
    "julia-06-multiple-dispatch"
  ],
  "references": [
    {
      "title": "Julia Manual — Composite Types",
      "url": "https://docs.julialang.org/en/v1/manual/types/#Composite-Types"
    },
    {
      "title": "Julia Manual — Constructors",
      "url": "https://docs.julialang.org/en/v1/manual/constructors/"
    }
  ]
}
---

# JULIA-11-STRUCTS: Composite Types and Structs

## Introduction

Immutable and mutable structs, inner constructors. By the end of this lesson you will be able to: Define immutable structs with typed fields; Define mutable structs for stateful objects; Write inner constructors with validation.

## Key Concepts

### 1. Define immutable structs with typed fields

Target: Define immutable structs with typed fields. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```julia
# Structs: immutable by default with concrete field types
struct Point
    x::Float64
    y::Float64
end

p = Point(1.0, 2.0)
println(p.x)               # 1.0

```
### 2. Define mutable structs for stateful objects

Target: Define mutable structs for stateful objects. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```julia
# Mutable structs for stateful objects
mutable struct Counter
    value::Int
end

function increment!(c::Counter)
    c.value += 1
end

c = Counter(0)
increment!(c)
increment!(c)
println(c.value)           # 2

```
### 3. Write inner constructors with validation

Target: Write inner constructors with validation. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```julia
# Default constructors and inner constructors
struct Circle
    radius::Float64
    Circle(r) = new(r)     # inner constructor validates
end

c = Circle(2.5)
println(c.radius)          # 2.5

```
### 4. Define immutable structs with typed fields

Target: Define immutable structs with typed fields. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```julia
# Field access and property mutation (immutable -> new object)
struct Rect
    w::Float64
    h::Float64
end

area(r::Rect) = r.w * r.h
r = Rect(3.0, 4.0)
println(area(r))           # 12.0

```

## Practice Questions

1. What is the key idea behind "Composite Types and Structs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Composite Types and Structs with analogies and real-world examples"
1. "Show me common mistakes beginners make with Composite Types and Structs"
1. "Provide advanced patterns and performance considerations for Composite Types and Structs"

## Key Takeaways

- Master the core ideas of Composite Types and Structs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
