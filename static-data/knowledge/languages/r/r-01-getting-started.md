---
{
  "title": "Getting Started with R",
  "description": "Console, scripts, RStudio, and the R execution model.",
  "type": "lesson",
  "order": 1,
  "duration": 20,
  "difficulty": "beginner",
  "learning_objectives": [
    "Run R code in the console and from scripts",
    "Explain how R vectorizes operations",
    "Use basic assignment and print statements"
  ],
  "knowledge_refs": [
    "r/r-01-getting-started"
  ],
  "prerequisites": [],
  "references": [
    {
      "title": "The R Project — Home",
      "url": "https://www.r-project.org/"
    },
    {
      "title": "An Introduction to R — Official Manual",
      "url": "https://cran.r-project.org/doc/manuals/r-release/R-intro.html"
    },
    {
      "title": "RStudio — Free IDE",
      "url": "https://posit.co/products/open-source/rstudio/"
    }
  ]
}
---

# R-01-GETTING-STARTED: Getting Started with R

## Introduction

Console, scripts, RStudio, and the R execution model. By the end of this lesson you will be able to: Run R code in the console and from scripts; Explain how R vectorizes operations; Use basic assignment and print statements.

## Key Concepts

### 1. Run R code in the console and from scripts

Target: Run R code in the console and from scripts. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```r
# Your first R program
print("Hello, 100X Systems!")

# Run with: Rscript hello.R  ->  [1] "Hello, 100X Systems!"

```
### 2. Explain how R vectorizes operations

Target: Explain how R vectorizes operations. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```r
# The R console: RStudio IDE or the terminal
# Use <- for assignment (the R convention)
x <- 42
x               # prints the value

```
### 3. Use basic assignment and print statements

Target: Use basic assignment and print statements. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```r
# R is vectorized: operations apply to whole vectors
numbers <- c(1, 2, 3, 4, 5)
print(numbers * 2)         # [1]  2  4  6  8 10
print(sum(numbers))        # [1] 15

```
### 4. Run R code in the console and from scripts

Target: Run R code in the console and from scripts. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```r
# Scripts, the working directory, and projects
# setwd("/path/to/project")   # change working directory
# RStudio projects keep everything organized
print(getwd())             # current working directory

```

## Practice Questions

1. What is the key idea behind "Getting Started with R"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with R with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with R"
1. "Provide advanced patterns and performance considerations for Getting Started with R"

## Key Takeaways

- Master the core ideas of Getting Started with R through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
