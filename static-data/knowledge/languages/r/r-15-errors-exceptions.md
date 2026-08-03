---
{
  "title": "Errors and Exceptions",
  "description": "stop, warning, tryCatch, and input validation.",
  "type": "lesson",
  "order": 15,
  "duration": "30 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Raise errors and warnings with stop and warning",
    "Handle errors with tryCatch",
    "Validate inputs with stopifnot"
  ],
  "knowledge_refs": [
    "r/r-15-errors-exceptions"
  ],
  "prerequisites": [
    "r-07-control-flow"
  ],
  "references": [
    {
      "title": "Advanced R — Debugging and Exceptions",
      "url": "https://adv-r.hadley.nz/debugging.html"
    },
    {
      "title": "R Language Definition — Errors",
      "url": "https://cran.r-project.org/doc/manuals/r-release/R-lang.html#Error-handling"
    }
  ]
}
---

# R-15-ERRORS-EXCEPTIONS: Errors and Exceptions

## Introduction

stop, warning, tryCatch, and input validation. By the end of this lesson you will be able to: Raise errors and warnings with stop and warning; Handle errors with tryCatch; Validate inputs with stopifnot.

## Key Concepts

### 1. Raise errors and warnings with stop and warning

Target: Raise errors and warnings with stop and warning. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```r
# Errors and warnings: stop(), warning(), message()
check <- function(x) {
    if (x < 0) stop("x must be non-negative")
    if (x == 0) warning("x is zero")
    message("checking x = ", x)
    sqrt(x)
}
print(check(4))             # 2

```
### 2. Handle errors with tryCatch

Target: Handle errors with tryCatch. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```r
# tryCatch: R's structured exception handling
result <- tryCatch(
    expr = {
        stop("boom")
    },
    error = function(e) {
        paste("caught:", conditionMessage(e))
    },
    finally = {
        print("cleanup ran")
    }
)
print(result)               # "caught: boom"

```
### 3. Validate inputs with stopifnot

Target: Validate inputs with stopifnot. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```r
# withCallingHandlers for warnings
withCallingHandlers(
    expr = { warning("a warning"); 42 },
    warning = function(w) print(paste("warn:", conditionMessage(w)))
)

```
### 4. Raise errors and warnings with stop and warning

Target: Raise errors and warnings with stop and warning. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```r
# Validating inputs: stopifnot
require_positive <- function(x) {
    stopifnot(is.numeric(x), x > 0)
    sqrt(x)
}
print(require_positive(9))  # 3

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
