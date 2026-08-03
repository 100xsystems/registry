---
{
  "title": "The Tidyverse",
  "description": "dplyr, ggplot2, readr, and tidyr — the modern R.",
  "type": "lesson",
  "order": 13,
  "duration": "30 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Install and load the tidyverse",
    "Use dplyr verbs with the pipe operator",
    "Explain the grammar of graphics in ggplot2"
  ],
  "knowledge_refs": [
    "r/r-13-tidyverse"
  ],
  "prerequisites": [
    "r-09-lists-data-frames"
  ],
  "references": [
    {
      "title": "Tidyverse — Main Site",
      "url": "https://www.tidyverse.org/"
    },
    {
      "title": "R for Data Science — Whole book",
      "url": "https://r4ds.hadley.nz/"
    },
    {
      "title": "dplyr — Documentation",
      "url": "https://dplyr.tidyverse.org/"
    },
    {
      "title": "ggplot2 — Documentation",
      "url": "https://ggplot2.tidyverse.org/"
    }
  ]
}
---

# R-13-TIDYVERSE: The Tidyverse

## Introduction

dplyr, ggplot2, readr, and tidyr — the modern R. By the end of this lesson you will be able to: Install and load the tidyverse; Use dplyr verbs with the pipe operator; Explain the grammar of graphics in ggplot2.

## Key Concepts

### 1. Install and load the tidyverse

Target: Install and load the tidyverse. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```r
# tidyverse: the modern R ecosystem
# install.packages("tidyverse")
# library(tidyverse)
# dplyr verbs: filter, select, mutate, arrange, summarize
print("tidyverse = ggplot2 + dplyr + tidyr + ...")

```
### 2. Use dplyr verbs with the pipe operator

Target: Use dplyr verbs with the pipe operator. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```r
# dplyr pipeline with the pipe operator |>
data <- data.frame(name = c("Ada", "Grace", "Linus"),
                   age = c(36, 85, 55))
result <- data |>
    dplyr::filter(age > 40) |>
    dplyr::select(name)
print(result)               # Grace, Linus

```
### 3. Explain the grammar of graphics in ggplot2

Target: Explain the grammar of graphics in ggplot2. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```r
# ggplot2: grammar of graphics
# library(ggplot2)
# ggplot(data, aes(x = age)) +
#   geom_histogram(bins = 10) +
#   labs(title = "Age distribution")
print("ggplot2 builds plots layer by layer")

```
### 4. Install and load the tidyverse

Target: Install and load the tidyverse. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```r
# readr and tidyr: reading and reshaping data
# library(readr); df <- read_csv("data.csv")
# library(tidyr); tidyr::pivot_longer(df, cols = c(a, b))
print("readr reads CSVs fast; tidyr reshapes tables")

```

## Practice Questions

1. What is the key idea behind "The Tidyverse"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain The Tidyverse with analogies and real-world examples"
1. "Show me common mistakes beginners make with The Tidyverse"
1. "Provide advanced patterns and performance considerations for The Tidyverse"

## Key Takeaways

- Master the core ideas of The Tidyverse through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
