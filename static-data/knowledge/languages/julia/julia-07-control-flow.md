---
{
  "title": "Control Flow",
  "description": "if/elseif, ternary, short-circuit, and loops.",
  "type": "lesson",
  "order": 7,
  "duration": "25 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write conditional branches with if/elseif/else",
    "Use ternary operators and short-circuiting",
    "Iterate with for and while loops"
  ],
  "knowledge_refs": [
    "julia/julia-07-control-flow"
  ],
  "prerequisites": [
    "julia-01-getting-started"
  ],
  "references": [
    {
      "title": "Julia Manual — Control Flow",
      "url": "https://docs.julialang.org/en/v1/manual/control-flow/"
    },
    {
      "title": "Julia Manual — Scope of Variables (loops)",
      "url": "https://docs.julialang.org/en/v1/manual/variables-and-scoping/"
    }
  ]
}
---

# JULIA-07-CONTROL-FLOW: Control Flow

## Introduction

if/elseif, ternary, short-circuit, and loops. By the end of this lesson you will be able to: Write conditional branches with if/elseif/else; Use ternary operators and short-circuiting; Iterate with for and while loops.

## Key Concepts

### 1. Write conditional branches with if/elseif/else

Target: Write conditional branches with if/elseif/else. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```julia
# if / elseif / else
function grade(score)
    if score >= 90
        "A"
    elseif score >= 80
        "B"
    else
        "C"
    end
end
println(grade(95))         # A

```
### 2. Use ternary operators and short-circuiting

Target: Use ternary operators and short-circuiting. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```julia
# Ternary and short-circuit evaluation
x = 5
label = x > 3 ? "big" : "small"
println(label)             # big
println(x > 3 && "yes")    # "yes" — && returns last value

```
### 3. Iterate with for and while loops

Target: Iterate with for and while loops. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```julia
# for loops: ranges, arrays, and nested
total = 0
for i in 1:10
    global total += i      # `global` needed at top level (soft scope)
end
println(total)             # 55

for (i, v) in enumerate(["a", "b"])
    println("$i -> $v")
end

```
### 4. Write conditional branches with if/elseif/else

Target: Write conditional branches with if/elseif/else. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```julia
# while loops and break/continue
n = 0
while true
    global n += 1
    n >= 5 && break
end
println(n)                 # 5

for i in 1:10
    i % 2 == 0 && continue
    print(i, " ")
end
# 1 3 5 7 9

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
