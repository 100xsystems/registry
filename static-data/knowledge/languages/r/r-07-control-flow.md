---
{
  "title": "Control Flow",
  "description": "if/else, ifelse, for, and while loops.",
  "type": "lesson",
  "order": 7,
  "duration": "25 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write conditional branches",
    "Use vectorized ifelse",
    "Iterate with for and while loops"
  ],
  "knowledge_refs": [
    "r/r-07-control-flow"
  ],
  "prerequisites": [
    "r-01-getting-started"
  ],
  "references": [
    {
      "title": "An Introduction to R — Control Structures",
      "url": "https://cran.r-project.org/doc/manuals/r-release/R-intro.html#Control-statement"
    },
    {
      "title": "R for Data Science — Iteration",
      "url": "https://r4ds.hadley.nz/iteration"
    }
  ]
}
---

# R-07-CONTROL-FLOW: Control Flow

## Introduction

if/else, ifelse, for, and while loops. By the end of this lesson you will be able to: Write conditional branches; Use vectorized ifelse; Iterate with for and while loops.

## Key Concepts

### 1. Write conditional branches

Target: Write conditional branches. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```r
# if / else if / else
grade <- function(score) {
    if (score >= 90) {
        "A"
    } else if (score >= 80) {
        "B"
    } else {
        "C"
    }
}
print(grade(95))            # "A"

```
### 2. Use vectorized ifelse

Target: Use vectorized ifelse. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```r
# Vectorized conditionals: ifelse
ages <- c(10, 25, 60)
labels <- ifelse(ages >= 18, "adult", "minor")
print(labels)               # "minor" "adult" "adult"

```
### 3. Iterate with for and while loops

Target: Iterate with for and while loops. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```r
# for loops over vectors
total <- 0
for (i in 1:5) {
    total <- total + i
}
print(total)                # 15

```
### 4. Write conditional branches

Target: Write conditional branches. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```r
# while loops and next/break
n <- 0
while (n < 5) {
    n <- n + 1
    if (n == 3) next        # skip 3
    print(n)                # 1 2 4 5
}

```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
