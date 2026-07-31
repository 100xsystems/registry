---
{
  "title": "Missing Data",
  "description": "NA propagation, na.rm, and imputation strategies.",
  "type": "lesson",
  "order": 18,
  "duration": 25,
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain how NA propagates through calculations",
    "Use na.rm and complete.cases",
    "Apply basic imputation strategies"
  ],
  "knowledge_refs": [
    "r/r-18-missing-data"
  ],
  "prerequisites": [
    "r-02-values-types"
  ],
  "references": [
    {
      "title": "R for Data Science — Missing Values",
      "url": "https://r4ds.hadley.nz/missing-values"
    },
    {
      "title": "tidyr — Missing data docs",
      "url": "https://tidyr.tidyverse.org/articles/tidy-data.html"
    }
  ]
}
---

# R-18-MISSING-DATA: Missing Data

## Introduction

NA propagation, na.rm, and imputation strategies. By the end of this lesson you will be able to: Explain how NA propagates through calculations; Use na.rm and complete.cases; Apply basic imputation strategies.

## Key Concepts

### 1. Explain how NA propagates through calculations

Target: Explain how NA propagates through calculations. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```r
# NA handling: na.rm and complete.cases
data <- c(1, NA, 3, NA, 5)
print(mean(data))           # NA — propagates!
print(mean(data, na.rm = TRUE))  # 3
print(data[!is.na(data)])   # 1 3 5

```
### 2. Use na.rm and complete.cases

Target: Use na.rm and complete.cases. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```r
# na.omit drops incomplete rows
df <- data.frame(a = c(1, NA, 3), b = c("x", "y", "z"))
print(na.omit(df))          # rows 1 and 3

```
### 3. Apply basic imputation strategies

Target: Apply basic imputation strategies. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```r
# tidyr::drop_na and fill
# library(tidyr)
# df |> tidyr::drop_na()     # drop rows with any NA
# df |> tidyr::fill(col)     # forward fill
print("tidyr handles missing data elegantly")

```
### 4. Explain how NA propagates through calculations

Target: Explain how NA propagates through calculations. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```r
# impute strategies: mean replacement
values <- c(1, NA, 3)
values[is.na(values)] <- mean(values, na.rm = TRUE)
print(values)               # 1 2 3

```

## Practice Questions

1. What is the key idea behind "Missing Data"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Missing Data with analogies and real-world examples"
1. "Show me common mistakes beginners make with Missing Data"
1. "Provide advanced patterns and performance considerations for Missing Data"

## Key Takeaways

- Master the core ideas of Missing Data through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
