---
{
  "title": "Errors and Exceptions",
  "description": "try/catch/finally, throw, and error handling patterns.",
  "type": "lesson",
  "order": 15,
  "duration": "30 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use try/catch/finally blocks correctly",
    "Throw typed exceptions with throw()",
    "Build safe wrappers around fallible code"
  ],
  "knowledge_refs": [
    "julia/julia-15-errors-exceptions"
  ],
  "prerequisites": [
    "julia-07-control-flow"
  ],
  "references": [
    {
      "title": "Julia Manual — Control Flow (try/catch)",
      "url": "https://docs.julialang.org/en/v1/manual/control-flow/#Exception-Handling"
    },
    {
      "title": "Julia Base — Exceptions Reference",
      "url": "https://docs.julialang.org/en/v1/base/base/#Exceptions"
    }
  ]
}
---

# JULIA-15-ERRORS-EXCEPTIONS: Errors and Exceptions

## Introduction

try/catch/finally, throw, and error handling patterns. By the end of this lesson you will be able to: Use try/catch/finally blocks correctly; Throw typed exceptions with throw(); Build safe wrappers around fallible code.

## Key Concepts

### 1. Use try/catch/finally blocks correctly

Target: Use try/catch/finally blocks correctly. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```julia
# try/catch/finally for graceful error handling
try
    error("something broke")
catch e
    println("caught: ", e) # caught: ErrorException("something broke")
finally
    println("cleanup ran")
end

```
### 2. Throw typed exceptions with throw()

Target: Throw typed exceptions with throw(). Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```julia
# throw to raise your own exceptions
function check_age(age)
    age < 0 && throw(ArgumentError("age cannot be negative"))
    return "ok"
end

println(check_age(30))     # ok
# check_age(-1) throws ArgumentError

```
### 3. Build safe wrappers around fallible code

Target: Build safe wrappers around fallible code. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```julia
# Capturing exception details with `catch e`
try
    x = 1 + "a"            # MethodError
catch e
    println(typeof(e))     # MethodError
    println(e.f)           # +  (the failing function)
end

```
### 4. Use try/catch/finally blocks correctly

Target: Use try/catch/finally blocks correctly. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```julia
# Errors are values-like: use try/catch to build safe wrappers
function safe_sqrt(x)
    try
        sqrt(x)
    catch
        NaN
    end
end

println(safe_sqrt(-1.0))   # NaN
println(safe_sqrt(9.0))    # 3.0

```

## Practice Questions

1. What is the key idea behind "Errors and Exceptions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Errors and Exceptions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Errors and Exceptions"
1. "Provide advanced patterns and performance considerations for Errors and Exceptions"

## Key Takeaways

- Master the core ideas of Errors and Exceptions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
