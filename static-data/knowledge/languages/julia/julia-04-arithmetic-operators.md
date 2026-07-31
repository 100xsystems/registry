---
{
  "title": "Arithmetic and Operators",
  "description": "Numeric operators, chained comparisons, and bitwise ops.",
  "type": "lesson",
  "order": 4,
  "duration": 25,
  "difficulty": "beginner",
  "learning_objectives": [
    "Use arithmetic, comparison, and logical operators",
    "Explain short-circuit evaluation of && and ||",
    "Apply bitwise operators to integers"
  ],
  "knowledge_refs": [
    "julia/julia-04-arithmetic-operators"
  ],
  "prerequisites": [
    "julia-02-values-types"
  ],
  "references": [
    {
      "title": "Julia Manual — Mathematical Operations",
      "url": "https://docs.julialang.org/en/v1/manual/mathematical-operations/"
    },
    {
      "title": "Julia Manual — Numeric Literal Coefficients",
      "url": "https://docs.julialang.org/en/v1/manual/mathematical-operations/#Numeric-Literal-Coefficients"
    }
  ]
}
---

# JULIA-04-ARITHMETIC-OPERATORS: Arithmetic and Operators

## Introduction

Numeric operators, chained comparisons, and bitwise ops. By the end of this lesson you will be able to: Use arithmetic, comparison, and logical operators; Explain short-circuit evaluation of && and ||; Apply bitwise operators to integers.

## Key Concepts

### 1. Use arithmetic, comparison, and logical operators

Target: Use arithmetic, comparison, and logical operators. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```julia
# Arithmetic operators
println(7 % 4)             # 3 — remainder
println(2^10)              # 1024 — power
println(div(7, 2))         # 3 — integer division
println(rem(7, 2))         # 1 — remainder

```
### 2. Explain short-circuit evaluation of && and ||

Target: Explain short-circuit evaluation of && and ||. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```julia
# Comparison and chained comparisons
println(1 < 2 < 3)         # true — chaining works natively!
println(1 == 1.0)          # true — numeric equality
println(1 === 1.0)         # false — identical types

```
### 3. Apply bitwise operators to integers

Target: Apply bitwise operators to integers. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```julia
# Logical operators: && and || short-circuit
x = nothing
y = x !== nothing && x + 1
println(y)                 # false
z = x !== nothing || "fallback"
println(z)                 # "fallback"

```
### 4. Use arithmetic, comparison, and logical operators

Target: Use arithmetic, comparison, and logical operators. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```julia
# Bitwise operations
println(0b1100 & 0b1010)   # 0b1000 = 8
println(0b1100 | 0b1010)   # 0b1110 = 14
println(0b1100 ⊻ 0b1010)   # 0b0110 = 6 (xor)
println(1 << 4)            # 16

```

## Practice Questions

1. What is the key idea behind "Arithmetic and Operators"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arithmetic and Operators with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arithmetic and Operators"
1. "Provide advanced patterns and performance considerations for Arithmetic and Operators"

## Key Takeaways

- Master the core ideas of Arithmetic and Operators through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
