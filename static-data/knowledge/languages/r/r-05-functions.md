---
{
  "title": "Functions",
  "description": "Definitions, defaults, return values, and anonymous functions.",
  "type": "lesson",
  "order": 5,
  "duration": "30 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define functions with default arguments",
    "Use explicit and implicit return values",
    "Write anonymous functions with lapply"
  ],
  "knowledge_refs": [
    "r/r-05-functions"
  ],
  "prerequisites": [
    "r-01-getting-started"
  ],
  "references": [
    {
      "title": "Advanced R — Functions",
      "url": "https://adv-r.hadley.nz/functions.html"
    },
    {
      "title": "R Language Definition — Functions",
      "url": "https://cran.r-project.org/doc/manuals/r-release/R-lang.html#Functions"
    }
  ]
}
---

# R-05-FUNCTIONS: Functions

## Introduction

Definitions, defaults, return values, and anonymous functions. By the end of this lesson you will be able to: Define functions with default arguments; Use explicit and implicit return values; Write anonymous functions with lapply.

## Key Concepts

### 1. Define functions with default arguments

Target: Define functions with default arguments. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```r
# Functions: last expression is the return value
square <- function(x) {
    x^2
}
print(square(5))            # 25

```
### 2. Use explicit and implicit return values

Target: Use explicit and implicit return values. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```r
# Explicit return() and early exits
classify <- function(n) {
    if (n < 0) return("negative")
    if (n == 0) return("zero")
    "positive"
}
print(classify(-5))         # "negative"
print(classify(3))          # "positive"

```
### 3. Write anonymous functions with lapply

Target: Write anonymous functions with lapply. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```r
# Default arguments
greet <- function(name = "world") {
    paste("Hello,", name, "!")
}
print(greet())              # "Hello, world !"
print(greet("R"))           # "Hello, R !"

```
### 4. Define functions with default arguments

Target: Define functions with default arguments. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```r
# Anonymous functions and lapply
squares <- lapply(c(1, 2, 3), function(x) x^2)
print(unlist(squares))      # 1 4 9

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
