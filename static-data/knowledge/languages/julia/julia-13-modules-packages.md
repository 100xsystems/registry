---
{
  "title": "Modules and Packages",
  "description": "Namespaces, Pkg management, import vs using.",
  "type": "lesson",
  "order": 13,
  "duration": 30,
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create and use modules with export",
    "Add and manage packages with Pkg",
    "Distinguish import from using"
  ],
  "knowledge_refs": [
    "julia/julia-13-modules-packages"
  ],
  "prerequisites": [
    "julia-05-functions"
  ],
  "references": [
    {
      "title": "Julia Manual — Modules",
      "url": "https://docs.julialang.org/en/v1/manual/modules/"
    },
    {
      "title": "Pkg — Package Manager Docs",
      "url": "https://pkgdocs.julialang.org/"
    },
    {
      "title": "Julia Manual — Code Loading",
      "url": "https://docs.julialang.org/en/v1/manual/code-loading/"
    }
  ]
}
---

# JULIA-13-MODULES-PACKAGES: Modules and Packages

## Introduction

Namespaces, Pkg management, import vs using. By the end of this lesson you will be able to: Create and use modules with export; Add and manage packages with Pkg; Distinguish import from using.

## Key Concepts

### 1. Create and use modules with export

Target: Create and use modules with export. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```julia
# Modules: namespaces for related code
module Greetings
    export hello
    hello(name) = "Hello, $name!"
    secret() = "internal only"
end

using .Greetings
println(hello("Julia"))    # Hello, Julia!

```
### 2. Add and manage packages with Pkg

Target: Add and manage packages with Pkg. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```julia
# Package management with Pkg
# using Pkg; Pkg.add("DataFrames")
# Pkg.activate("myproject")   # local environment
# Pkg.status()                # list installed packages
println("Packages live in environments, not globally")

```
### 3. Distinguish import from using

Target: Distinguish import from using. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```julia
# import vs using: qualified access
import Statistics
data = [1.0, 2.0, 3.0]
println(Statistics.mean(data))   # 2.0

```
### 4. Create and use modules with export

Target: Create and use modules with export. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```julia
# include: pull in other source files
# include("helpers.jl")       # runs that file in current scope
# The convention: one module per file for libraries
println("Modular code keeps projects navigable")

```

## Practice Questions

1. What is the key idea behind "Modules and Packages"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Modules and Packages with analogies and real-world examples"
1. "Show me common mistakes beginners make with Modules and Packages"
1. "Provide advanced patterns and performance considerations for Modules and Packages"

## Key Takeaways

- Master the core ideas of Modules and Packages through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
