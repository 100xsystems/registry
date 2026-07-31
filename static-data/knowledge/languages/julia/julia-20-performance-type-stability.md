---
{
  "title": "Performance and Type Stability",
  "description": "Type stability, @code_warntype, and allocation-free code.",
  "type": "lesson",
  "order": 20,
  "duration": 40,
  "difficulty": "expert",
  "learning_objectives": [
    "Explain why type stability drives performance",
    "Use @code_warntype and @time to diagnose hotspots",
    "Avoid Union return types and global scope in hot loops"
  ],
  "knowledge_refs": [
    "julia/julia-20-performance-type-stability"
  ],
  "prerequisites": [
    "julia-12-parametric-types"
  ],
  "references": [
    {
      "title": "Julia Manual — Performance Tips",
      "url": "https://docs.julialang.org/en/v1/manual/performance-tips/"
    },
    {
      "title": "Julia Manual — @code_warntype",
      "url": "https://docs.julialang.org/en/v1/base/base/#Base.@code_warntype"
    },
    {
      "title": "BenchmarkTools.jl",
      "url": "https://github.com/JuliaCI/BenchmarkTools.jl"
    }
  ]
}
---

# JULIA-20-PERFORMANCE-TYPE-STABILITY: Performance and Type Stability

## Introduction

Type stability, @code_warntype, and allocation-free code. By the end of this lesson you will be able to: Explain why type stability drives performance; Use @code_warntype and @time to diagnose hotspots; Avoid Union return types and global scope in hot loops.

## Key Concepts

### 1. Explain why type stability drives performance

Target: Explain why type stability drives performance. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```julia
# Performance: type stability matters
function sum_positive(xs)
    s = 0                  # annotate for stability: s = 0.0
    for x in xs
        x > 0 && (s += x)
    end
    s
end
println(sum_positive([1, -2, 3]))  # 4

```
### 2. Use @code_warntype and @time to diagnose hotspots

Target: Use @code_warntype and @time to diagnose hotspots. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```julia
# @code_warntype reveals type instability
function unstable(x)
    x > 0 ? 1 : 1.0        # Union{Int64, Float64} — boxed!
end

# @code_warntype unstable(1)
println("Avoid Union return types for hot loops")

```
### 3. Avoid Union return types and global scope in hot loops

Target: Avoid Union return types and global scope in hot loops. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```julia
# @time and @btime for measuring performance
using Printf
@time sum(1:1_000_000)     # prints allocation + time

# @btime from BenchmarkTools is even better:
# using BenchmarkTools; @btime sum(1:1_000_000)

```
### 4. Explain why type stability drives performance

Target: Explain why type stability drives performance. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```julia
# The performance mantra: global scope is slow
function fast(xs)
    s = 0.0
    for x in xs
        s += x
    end
    s
end
println(fast(1.0:1_000_000.0))  # 5.000005e11

```

## Practice Questions

1. What is the key idea behind "Performance and Type Stability"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Performance and Type Stability with analogies and real-world examples"
1. "Show me common mistakes beginners make with Performance and Type Stability"
1. "Provide advanced patterns and performance considerations for Performance and Type Stability"

## Key Takeaways

- Master the core ideas of Performance and Type Stability through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
