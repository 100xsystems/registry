---
{
  "title": "Variables and Scoping",
  "description": "Assignment, const, local vs global scope, and closures.",
  "type": "lesson",
  "order": 3,
  "duration": 25,
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare and rebind variables correctly",
    "Understand local vs global scope rules",
    "Build closures with let blocks"
  ],
  "knowledge_refs": [
    "julia/julia-03-variables-scoping"
  ],
  "prerequisites": [
    "julia-01-getting-started"
  ],
  "references": [
    {
      "title": "Julia Manual — Variables",
      "url": "https://docs.julialang.org/en/v1/manual/variables/"
    },
    {
      "title": "Julia Manual — Scope of Variables",
      "url": "https://docs.julialang.org/en/v1/manual/variables-and-scoping/"
    },
    {
      "title": "Julia Manual — Closures",
      "url": "https://docs.julialang.org/en/v1/manual/faq/"
    }
  ]
}
---

# JULIA-03-VARIABLES-SCOPING: Variables and Scoping

## Introduction

Assignment, const, local vs global scope, and closures. By the end of this lesson you will be able to: Declare and rebind variables correctly; Understand local vs global scope rules; Build closures with let blocks.

## Key Concepts

### 1. Declare and rebind variables correctly

Target: Declare and rebind variables correctly. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```julia
# Variables: convention is lowercase with underscores
name = "Ada"
age = 36
const GRAVITY = 9.81      # const cannot be rebound (warning if you try)
println(name * " is " * string(age) * " years old")

```
### 2. Understand local vs global scope rules

Target: Understand local vs global scope rules. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```julia
# Scoping: global vs local
x = 10                     # global
function f()
    y = 20                 # local
    return x + y           # global x is readable
end
println(f())               # 30

```
### 3. Build closures with let blocks

Target: Build closures with let blocks. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```julia
# Soft vs hard scope: loops introduce a new scope
sum_ = 0
for i in 1:5
    global sum_ += i       # need `global` to mutate outer var
end
println(sum_)              # 15

```
### 4. Declare and rebind variables correctly

Target: Declare and rebind variables correctly. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```julia
# let blocks create fresh local scopes
f = let
    counter = 0
    () -> (counter += 1; counter)
end
println(f())               # 1
println(f())               # 2 — closure keeps state

```

## Practice Questions

1. What is the key idea behind "Variables and Scoping"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables and Scoping with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables and Scoping"
1. "Provide advanced patterns and performance considerations for Variables and Scoping"

## Key Takeaways

- Master the core ideas of Variables and Scoping through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
