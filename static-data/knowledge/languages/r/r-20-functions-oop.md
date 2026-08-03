---
{
  "title": "Functional Programming and OOP",
  "description": "First-class functions, environments, S3 and S4 classes.",
  "type": "lesson",
  "order": 20,
  "duration": "40 min",
  "difficulty": "expert",
  "learning_objectives": [
    "Pass functions as arguments",
    "Use environments with local()",
    "Build S3 classes with class assignment"
  ],
  "knowledge_refs": [
    "r/r-20-functions-oop"
  ],
  "prerequisites": [
    "r-12-functions-advanced"
  ],
  "references": [
    {
      "title": "Advanced R — S3",
      "url": "https://adv-r.hadley.nz/s3.html"
    },
    {
      "title": "Advanced R — S4",
      "url": "https://adv-r.hadley.nz/s4.html"
    },
    {
      "title": "Advanced R — Functional Programming",
      "url": "https://adv-r.hadley.nz/fp.html"
    }
  ]
}
---

# R-20-FUNCTIONS-OOP: Functional Programming and OOP

## Introduction

First-class functions, environments, S3 and S4 classes. By the end of this lesson you will be able to: Pass functions as arguments; Use environments with local(); Build S3 classes with class assignment.

## Key Concepts

### 1. Pass functions as arguments

Target: Pass functions as arguments. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```r
# Functions are first-class: pass them around
apply_twice <- function(f, x) f(f(x))
print(apply_twice(function(n) n * 2, 5))  # 20

```
### 2. Use environments with local()

Target: Use environments with local(). Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```r
# Environments and scope: globalenv() and local()
x <- "global"
f <- local({
    x <- "local"
    function() x
})
print(f())                  # "local"
print(x)                    # "global" — untouched

```
### 3. Build S3 classes with class assignment

Target: Build S3 classes with class assignment. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```r
# S3 classes: R's simple OOP system
person <- function(name, age) {
    obj <- list(name = name, age = age)
    class(obj) <- "person"
    obj
}
print.person <- function(p) {
    cat(p$name, "is", p$age, "years old\n")
}
ada <- person("Ada", 36)
print(ada)                  # Ada is 36 years old

```
### 4. Pass functions as arguments

Target: Pass functions as arguments. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```r
# S4 classes: formal OOP (Bioconductor style)
# setClass("Person", slots = c(name = "character", age = "numeric"))
# ada <- new("Person", name = "Ada", age = 36)
print("S4 brings formal validation and inheritance")

```

## Practice Questions

1. What is the key idea behind "Functional Programming and OOP"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functional Programming and OOP with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functional Programming and OOP"
1. "Provide advanced patterns and performance considerations for Functional Programming and OOP"

## Key Takeaways

- Master the core ideas of Functional Programming and OOP through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
