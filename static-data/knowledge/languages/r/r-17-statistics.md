---
{
  "title": "Statistics and Sampling",
  "description": "Sampling, distributions, summaries, and hypothesis tests.",
  "type": "lesson",
  "order": 17,
  "duration": "30 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Sample data with sample() and set.seed()",
    "Draw from random distributions",
    "Compute summary statistics and run t-tests"
  ],
  "knowledge_refs": [
    "r/r-17-statistics"
  ],
  "prerequisites": [
    "r-06-vectors-indexing"
  ],
  "references": [
    {
      "title": "R for Data Science — Distributions",
      "url": "https://r4ds.hadley.nz/"
    },
    {
      "title": "An Introduction to R — Statistical Functions",
      "url": "https://cran.r-project.org/doc/manuals/r-release/R-intro.html#Statistical-distributions"
    }
  ]
}
---

# R-17-STATISTICS: Statistics and Sampling

## Introduction

Sampling, distributions, summaries, and hypothesis tests. By the end of this lesson you will be able to: Sample data with sample() and set.seed(); Draw from random distributions; Compute summary statistics and run t-tests.

## Key Concepts

### 1. Sample data with sample() and set.seed()

Target: Sample data with sample() and set.seed(). Start with the foundations — read the runnable example carefully and trace its output before moving on.

```r
# Sampling: sample() and set.seed()
set.seed(42)
print(sample(1:10, 3))      # random sample without replacement
print(sample(1:10, 5, replace = TRUE))  # with replacement

```
### 2. Draw from random distributions

Target: Draw from random distributions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```r
# Random distributions
set.seed(1)
print(rnorm(3))             # 3 draws from N(0, 1)
print(runif(3, 0, 1))       # 3 draws from Uniform(0, 1)

```
### 3. Compute summary statistics and run t-tests

Target: Compute summary statistics and run t-tests. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```r
# Summary statistics
x <- c(1, 2, 3, 4, 100)
print(mean(x))              # 22
print(median(x))            # 3
print(sd(x))                # standard deviation
print(summary(x))           # min, quartiles, max

```
### 4. Sample data with sample() and set.seed()

Target: Sample data with sample() and set.seed(). Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```r
# Correlation and basic tests
x <- c(1, 2, 3, 4, 5)
y <- c(2, 4, 6, 8, 10)
print(cor(x, y))            # 1 — perfectly correlated
print(t.test(x, mu = 3))    # one-sample t-test

```

## Practice Questions

1. What is the key idea behind "Statistics and Sampling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Statistics and Sampling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Statistics and Sampling"
1. "Provide advanced patterns and performance considerations for Statistics and Sampling"

## Key Takeaways

- Master the core ideas of Statistics and Sampling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
