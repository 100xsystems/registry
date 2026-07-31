---
{
  "title": "Getting Started with Julia",
  "description": "REPL, scripts, and the Julia execution model.",
  "type": "lesson",
  "order": 1,
  "duration": 20,
  "difficulty": "beginner",
  "learning_objectives": [
    "Run Julia code in the REPL and from script files",
    "Explain how Julia JIT-compiles dynamically typed code",
    "Use basic arithmetic and function definitions"
  ],
  "knowledge_refs": [
    "julia/julia-01-getting-started"
  ],
  "prerequisites": [],
  "references": [
    {
      "title": "Julia Manual — Getting Started",
      "url": "https://docs.julialang.org/en/v1/manual/getting-started/"
    },
    {
      "title": "Julia in VS Code — docs",
      "url": "https://code.visualstudio.com/docs/languages/julia"
    },
    {
      "title": "Julia Academy — free courses",
      "url": "https://juliaacademy.com/"
    }
  ]
}
---

# JULIA-01-GETTING-STARTED: Getting Started with Julia

## Introduction

REPL, scripts, and the Julia execution model. By the end of this lesson you will be able to: Run Julia code in the REPL and from script files; Explain how Julia JIT-compiles dynamically typed code; Use basic arithmetic and function definitions.

## Key Concepts

### 1. Run Julia code in the REPL and from script files

Target: Run Julia code in the REPL and from script files. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```julia
# Your first Julia program
println("Hello, 100X Systems!")

# Run with: julia hello.jl  ->  Hello, 100X Systems!

```
### 2. Explain how Julia JIT-compiles dynamically typed code

Target: Explain how Julia JIT-compiles dynamically typed code. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```julia
# The REPL: julia  (press ) to enter package mode, ? for help)
# Arithmetic is immediate and precise by default:
println(2^10)        # 1024 — ^ is exponentiation, NOT bitwise
println(7 / 2)       # 3.5 — float division (not integer!)
println(7 ÷ 2)       # 3   — integer division

```
### 3. Use basic arithmetic and function definitions

Target: Use basic arithmetic and function definitions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```julia
# Julia is dynamically typed but JIT-compiled to native code
function greet(name)
    return "Hello, " * name * "!"
end

println(greet("Julia"))  # Hello, Julia!

```
### 4. Run Julia code in the REPL and from script files

Target: Run Julia code in the REPL and from script files. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```julia
# Scripts, packages, and one-liners
# julia -e 'println(1 + 1)'
# julia script.jl arg1 arg2
println("Startup is fast because of precompilation")

```

## Practice Questions

1. What is the key idea behind "Getting Started with Julia"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Julia with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Julia"
1. "Provide advanced patterns and performance considerations for Getting Started with Julia"

## Key Takeaways

- Master the core ideas of Getting Started with Julia through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
