---
{
  "title": "Arrays",
  "description": "Vectors, comprehensions, broadcasting, and matrices.",
  "type": "lesson",
  "order": 9,
  "duration": 35,
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create and index arrays (1-based indexing!)",
    "Write array comprehensions with filters",
    "Apply functions elementwise with broadcasting"
  ],
  "knowledge_refs": [
    "julia/julia-09-arrays"
  ],
  "prerequisites": [
    "julia-02-values-types"
  ],
  "references": [
    {
      "title": "Julia Manual — Arrays",
      "url": "https://docs.julialang.org/en/v1/manual/arrays/"
    },
    {
      "title": "Julia Manual — Broadcasting",
      "url": "https://docs.julialang.org/en/v1/manual/arrays/#Broadcasting"
    },
    {
      "title": "Julia Manual — Array Comprehensions",
      "url": "https://docs.julialang.org/en/v1/manual/arrays/#Comprehensions"
    }
  ]
}
---

# JULIA-09-ARRAYS: Arrays

## Introduction

Vectors, comprehensions, broadcasting, and matrices. By the end of this lesson you will be able to: Create and index arrays (1-based indexing!); Write array comprehensions with filters; Apply functions elementwise with broadcasting.

## Key Concepts

### 1. Create and index arrays (1-based indexing!)

Target: Create and index arrays (1-based indexing!). Start with the foundations — read the runnable example carefully and trace its output before moving on.

```julia
# Arrays: homogeneous, 1-based indexed, column-major
v = [10, 20, 30]
println(v[1])              # 10 — indexing starts at 1!
println(v[end])            # 30
println(length(v))         # 3

```
### 2. Write array comprehensions with filters

Target: Write array comprehensions with filters. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```julia
# Comprehensions and generator expressions
squares = [x^2 for x in 1:5]
println(squares)           # [1, 4, 9, 16, 25]

even_squares = [x^2 for x in 1:10 if iseven(x)]
println(even_squares)      # [4, 16, 36, 64, 100]

```
### 3. Apply functions elementwise with broadcasting

Target: Apply functions elementwise with broadcasting. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```julia
# Broadcasting: the dot applies a function elementwise
nums = [1, 2, 3]
println(nums .+ 10)        # [11, 12, 13]
println(sin.(nums))        # elementwise sin

# .= mutates in place
nums .= nums .* 2
println(nums)              # [2, 4, 6]

```
### 4. Create and index arrays (1-based indexing!)

Target: Create and index arrays (1-based indexing!). Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```julia
# Matrices: 2D arrays
M = [1 2; 3 4]             # 2x2 matrix
println(M[1, 2])           # 2 — row 1, col 2
println(size(M))           # (2, 2)
println(M')                # adjoint (transpose for reals)

```

## Practice Questions

1. What is the key idea behind "Arrays"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arrays with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arrays"
1. "Provide advanced patterns and performance considerations for Arrays"

## Key Takeaways

- Master the core ideas of Arrays through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
