---
{
  "title": "Missing, Nothing, and NaN",
  "description": "Handling absent and undefined values idiomatically.",
  "type": "lesson",
  "order": 18,
  "duration": 25,
  "difficulty": "intermediate",
  "learning_objectives": [
    "Distinguish missing, nothing, and NaN",
    "Use skipmissing to clean data",
    "Apply something() for fallback values"
  ],
  "knowledge_refs": [
    "julia/julia-18-missing-nothing"
  ],
  "prerequisites": [
    "julia-02-values-types"
  ],
  "references": [
    {
      "title": "Julia Manual — Missing Values",
      "url": "https://docs.julialang.org/en/v1/manual/missing/"
    },
    {
      "title": "Julia Base — Missing Reference",
      "url": "https://docs.julialang.org/en/v1/base/base/#Base.Missing"
    }
  ]
}
---

# JULIA-18-MISSING-NOTHING: Missing, Nothing, and NaN

## Introduction

Handling absent and undefined values idiomatically. By the end of this lesson you will be able to: Distinguish missing, nothing, and NaN; Use skipmissing to clean data; Apply something() for fallback values.

## Key Concepts

### 1. Distinguish missing, nothing, and NaN

Target: Distinguish missing, nothing, and NaN. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```julia
# missing vs nothing vs NaN — three different things
println(typeof(missing))   # Missing
println(typeof(nothing))   # Nothing
println(typeof(NaN))       # Float64

# missing propagates: 1 + missing == missing
println(ismissing(1 + missing))  # true

```
### 2. Use skipmissing to clean data

Target: Use skipmissing to clean data. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```julia
# skipmissing: drop missing values from a collection
data = [1, missing, 3, missing, 5]
println(collect(skipmissing(data)))  # [1, 3, 5]
println(sum(skipmissing(data)))      # 9

```
### 3. Apply something() for fallback values

Target: Apply something() for fallback values. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```julia
# coerce with something() and fallbacks
x = nothing
println(something(x, "default"))   # "default"

y = 42
println(something(y, "default"))   # 42

```
### 4. Distinguish missing, nothing, and NaN

Target: Distinguish missing, nothing, and NaN. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```julia
# Working with missing in real data
data = [1.0, missing, 3.0]
# mean(data) errors without Statistics
using Statistics
println(mean(skipmissing(data)))    # 2.0

```

## Practice Questions

1. What is the key idea behind "Missing, Nothing, and NaN"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Missing, Nothing, and NaN with analogies and real-world examples"
1. "Show me common mistakes beginners make with Missing, Nothing, and NaN"
1. "Provide advanced patterns and performance considerations for Missing, Nothing, and NaN"

## Key Takeaways

- Master the core ideas of Missing, Nothing, and NaN through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
