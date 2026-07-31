---
{
  "title": "Tuples, NamedTuples, and Dictionaries",
  "description": "Immutable tuples, keyed maps, and sets.",
  "type": "lesson",
  "order": 10,
  "duration": 30,
  "difficulty": "beginner",
  "learning_objectives": [
    "Create and destructure tuples",
    "Use NamedTuples for labeled data",
    "Work with Dicts and Sets"
  ],
  "knowledge_refs": [
    "julia/julia-10-tuples-dicts"
  ],
  "prerequisites": [
    "julia-09-arrays"
  ],
  "references": [
    {
      "title": "Julia Manual — Composite Types (Tuple)",
      "url": "https://docs.julialang.org/en/v1/manual/types/#Composite-Types"
    },
    {
      "title": "Julia Standard Library — Dict",
      "url": "https://docs.julialang.org/en/v1/base/collections/"
    }
  ]
}
---

# JULIA-10-TUPLES-DICTS: Tuples, NamedTuples, and Dictionaries

## Introduction

Immutable tuples, keyed maps, and sets. By the end of this lesson you will be able to: Create and destructure tuples; Use NamedTuples for labeled data; Work with Dicts and Sets.

## Key Concepts

### 1. Create and destructure tuples

Target: Create and destructure tuples. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```julia
# Tuples: immutable, heterogeneous
t = (1, "two", 3.0)
println(t[1])              # 1
a, b, c = t                # destructuring
println("$a $b $c")        # 1 two 3.0

```
### 2. Use NamedTuples for labeled data

Target: Use NamedTuples for labeled data. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```julia
# NamedTuples: tuples with named fields
person = (name="Ada", age=36)
println(person.name)       # Ada
println(person.age)        # 36

```
### 3. Work with Dicts and Sets

Target: Work with Dicts and Sets. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```julia
# Dictionaries: mutable key-value maps
d = Dict("a" => 1, "b" => 2)
d["c"] = 3
println(keys(d))           # collection of keys
println(haskey(d, "a"))    # true
println(get(d, "z", 0))    # 0 — default value

```
### 4. Create and destructure tuples

Target: Create and destructure tuples. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```julia
# Sets and push!/pop! for mutable collections
s = Set([1, 2, 2, 3])
println(s)                 # Set([2, 3, 1]) — duplicates removed

stack = Int[]
push!(stack, 1, 2, 3)
println(pop!(stack))       # 3
println(stack)             # [1, 2]

```

## Practice Questions

1. What is the key idea behind "Tuples, NamedTuples, and Dictionaries"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Tuples, NamedTuples, and Dictionaries with analogies and real-world examples"
1. "Show me common mistakes beginners make with Tuples, NamedTuples, and Dictionaries"
1. "Provide advanced patterns and performance considerations for Tuples, NamedTuples, and Dictionaries"

## Key Takeaways

- Master the core ideas of Tuples, NamedTuples, and Dictionaries through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
