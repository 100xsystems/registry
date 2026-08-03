---
{
  "title": "Variables and Scoping",
  "description": "Assignment, object names, environments, and existence checks.",
  "type": "lesson",
  "order": 3,
  "duration": "25 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Assign values with <- and =",
    "List and remove objects with ls() and rm()",
    "Explain that everything in R is an object"
  ],
  "knowledge_refs": [
    "r/r-03-variables-scoping"
  ],
  "prerequisites": [
    "r-01-getting-started"
  ],
  "references": [
    {
      "title": "Advanced R — Names and Values",
      "url": "https://adv-r.hadley.nz/names-values.html"
    },
    {
      "title": "Advanced R — Environments",
      "url": "https://adv-r.hadley.nz/environments.html"
    }
  ]
}
---

# R-03-VARIABLES-SCOPING: Variables and Scoping

## Introduction

Assignment, object names, environments, and existence checks. By the end of this lesson you will be able to: Assign values with <- and =; List and remove objects with ls() and rm(); Explain that everything in R is an object.

## Key Concepts

### 1. Assign values with <- and =

Target: Assign values with <- and =. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```r
# Assignment: <- is idiomatic, = also works
x <- 10
y = 20
print(x + y)                # 30

```
### 2. List and remove objects with ls() and rm()

Target: List and remove objects with ls() and rm(). Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```r
# Object names: letters, digits, dots, underscores
my_variable <- 1
my.var <- 2
print(my_variable + my.var) # 3

```
### 3. Explain that everything in R is an object

Target: Explain that everything in R is an object. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```r
# Environment: ls() lists objects, rm() removes them
a <- 1
b <- 2
print(ls())                 # "a" "b"
rm(a)
print(exists("a"))          # FALSE

```
### 4. Assign values with <- and =

Target: Assign values with <- and =. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```r
# Everything in R is an object — even functions
f <- function(x) x * 2
print(f)                    # prints the function body
print(is.function(f))       # TRUE

```

## Practice Questions

1. What is the key idea behind "Variables and Scoping"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables and Scoping with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables and Scoping"
1. "Provide advanced patterns and performance considerations for Variables and Scoping"

## Key Takeaways

- Master the core ideas of Variables and Scoping through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
