---
{
  "title": "Advanced Functions",
  "description": "Reuse, ... arguments, closures, and lexical scoping.",
  "type": "lesson",
  "order": 12,
  "duration": 35,
  "difficulty": "intermediate",
  "learning_objectives": [
    "Compose functions that reuse other functions",
    "Use ... to forward arguments",
    "Build closures with <<-"
  ],
  "knowledge_refs": [
    "r/r-12-functions-advanced"
  ],
  "prerequisites": [
    "r-05-functions"
  ],
  "references": [
    {
      "title": "Advanced R — Function Composition",
      "url": "https://adv-r.hadley.nz/functions.html"
    },
    {
      "title": "Advanced R — Environments",
      "url": "https://adv-r.hadley.nz/environments.html"
    }
  ]
}
---

# R-12-FUNCTIONS-ADVANCED: Advanced Functions

## Introduction

Reuse, ... arguments, closures, and lexical scoping. By the end of this lesson you will be able to: Compose functions that reuse other functions; Use ... to forward arguments; Build closures with <<-.

## Key Concepts

### 1. Compose functions that reuse other functions

Target: Compose functions that reuse other functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```r
# Writing functions that reuse other functions
power <- function(base, exp = 2) {
    base^exp
}
print(power(3))             # 9
print(power(2, 10))         # 1024

```
### 2. Use ... to forward arguments

Target: Use ... to forward arguments. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```r
# ... (dot-dot-dot): pass along extra arguments
wrapper <- function(..., prefix = "result:") {
    values <- list(...)
    paste(prefix, sum(unlist(values)))
}
print(wrapper(1, 2, 3))     # "result: 6"

```
### 3. Build closures with <<-

Target: Build closures with <<-. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```r
# Closures: functions that remember their environment
make_counter <- function() {
    count <- 0
    function() {
        count <<- count + 1   # <<- assigns in the enclosing scope
        count
    }
}
counter <- make_counter()
print(counter())            # 1
print(counter())            # 2

```
### 4. Compose functions that reuse other functions

Target: Compose functions that reuse other functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```r
# Lexical scoping: functions see their defining environment
x <- 10
f <- function() x + 5
print(f())                  # 15

y <- 1
g <- function() y
y <- 100
print(g())                  # 100 — lookup happens at call time

```

## Practice Questions

1. What is the key idea behind "Advanced Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Advanced Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Advanced Functions"
1. "Provide advanced patterns and performance considerations for Advanced Functions"

## Key Takeaways

- Master the core ideas of Advanced Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
