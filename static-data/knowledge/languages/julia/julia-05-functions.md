---
{
  "title": "Functions",
  "description": "Definitions, keyword arguments, anonymous functions, splatting.",
  "type": "lesson",
  "order": 5,
  "duration": "30 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define functions in one line and multi-line form",
    "Use optional and keyword arguments",
    "Write anonymous functions and do blocks"
  ],
  "knowledge_refs": [
    "julia/julia-05-functions"
  ],
  "prerequisites": [
    "julia-01-getting-started"
  ],
  "references": [
    {
      "title": "Julia Manual — Functions",
      "url": "https://docs.julialang.org/en/v1/manual/functions/"
    },
    {
      "title": "Julia Manual — Do-Block Syntax",
      "url": "https://docs.julialang.org/en/v1/manual/functions/#Do-Block-Syntax-for-Function-Arguments"
    },
    {
      "title": "Julia Manual — Varargs",
      "url": "https://docs.julialang.org/en/v1/manual/functions/#Varargs-Functions"
    }
  ]
}
---

# JULIA-05-FUNCTIONS: Functions

## Introduction

Definitions, keyword arguments, anonymous functions, splatting. By the end of this lesson you will be able to: Define functions in one line and multi-line form; Use optional and keyword arguments; Write anonymous functions and do blocks.

## Key Concepts

### 1. Define functions in one line and multi-line form

Target: Define functions in one line and multi-line form. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```julia
# Functions: the return keyword is optional (last expression wins)
add(a, b) = a + b          # one-line function definition
function mul(a, b)
    a * b                  # implicit return
end
println(add(2, 3))         # 5
println(mul(2, 3))         # 6

```
### 2. Use optional and keyword arguments

Target: Use optional and keyword arguments. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```julia
# Optional and keyword arguments
function greet(name; punctuation="!")
    return "Hello, " * name * punctuation
end
println(greet("Julia"))              # Hello, Julia!
println(greet("Julia"; punctuation="?"))  # Hello, Julia?

```
### 3. Write anonymous functions and do blocks

Target: Write anonymous functions and do blocks. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```julia
# Anonymous functions and do blocks
doubles = map(x -> x * 2, [1, 2, 3])
println(doubles)           # [2, 4, 6]

# do block = multi-line anonymous function
total = sum([1, 2, 3, 4]) do x
    x > 2 ? x : 0
end
println(total)             # 7

```
### 4. Define functions in one line and multi-line form

Target: Define functions in one line and multi-line form. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```julia
# Varargs and splatting
function total(args...)
    sum(args)
end
println(total(1, 2, 3, 4)) # 10
nums = [1, 2, 3]
println(total(nums...))    # 6 — splat a collection

```

## Practice Questions

1. What is the key idea behind "Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions"
1. "Provide advanced patterns and performance considerations for Functions"

## Key Takeaways

- Master the core ideas of Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
