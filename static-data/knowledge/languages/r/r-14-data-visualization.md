---
{
  "title": "Data Visualization",
  "description": "Base R plots, histograms, boxplots, and saving output.",
  "type": "lesson",
  "order": 14,
  "duration": 30,
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create scatterplots with plot()",
    "Build histograms and boxplots",
    "Save plots to image files"
  ],
  "knowledge_refs": [
    "r/r-14-data-visualization"
  ],
  "prerequisites": [
    "r-06-vectors-indexing"
  ],
  "references": [
    {
      "title": "An Introduction to R — Graphics",
      "url": "https://cran.r-project.org/doc/manuals/r-release/R-intro.html#Graphics"
    },
    {
      "title": "R Graphics Cookbook",
      "url": "https://r-graphics.org/"
    }
  ]
}
---

# R-14-DATA-VISUALIZATION: Data Visualization

## Introduction

Base R plots, histograms, boxplots, and saving output. By the end of this lesson you will be able to: Create scatterplots with plot(); Build histograms and boxplots; Save plots to image files.

## Key Concepts

### 1. Create scatterplots with plot()

Target: Create scatterplots with plot(). Start with the foundations — read the runnable example carefully and trace its output before moving on.

```r
# Base R plotting: the classic scatterplot
x <- 1:10
y <- x^2
plot(x, y, main = "Squares", col = "blue", pch = 19)
print("plot() opens a graphics device")

```
### 2. Build histograms and boxplots

Target: Build histograms and boxplots. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```r
# hist() for distributions
set.seed(42)
values <- rnorm(1000, mean = 0, sd = 1)
hist(values, breaks = 30, main = "Normal distribution")

```
### 3. Save plots to image files

Target: Save plots to image files. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```r
# boxplot() for comparing groups
groups <- list(a = rnorm(50), b = rnorm(50, mean = 2))
boxplot(groups, main = "Group comparison")

```
### 4. Create scatterplots with plot()

Target: Create scatterplots with plot(). Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```r
# Saving plots to files
# png("plot.png", width = 800, height = 600)
# plot(1:10, 1:10)
# dev.off()
print("dev.off() closes the graphics device")

```

## Practice Questions

1. What is the key idea behind "Data Visualization"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Data Visualization with analogies and real-world examples"
1. "Show me common mistakes beginners make with Data Visualization"
1. "Provide advanced patterns and performance considerations for Data Visualization"

## Key Takeaways

- Master the core ideas of Data Visualization through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
