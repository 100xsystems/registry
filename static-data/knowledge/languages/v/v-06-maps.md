---
{
  "title": "Maps",
  "description": "Key-value storage.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create maps",
    "Insert and get",
    "Iterate entries",
    "Check existence"
  ],
  "knowledge_refs": [
    "v/v-06-maps"
  ],
  "prerequisites": [
    "V-05: Arrays"
  ],
  "references": [
    {
      "title": "V Documentation",
      "url": "https://docs.vlang.io/",
      "description": "Official docs"
    },
    {
      "title": "V Manual",
      "url": "https://docs.vlang.io/introduction.html",
      "description": "Language manual"
    },
    {
      "title": "V Language GitHub",
      "url": "https://github.com/vlang/v",
      "description": "Source code"
    }
  ]
}
---

# V-06-MAPS: Maps

## Introduction

Key-value storage. By the end of this lesson you will be able to: Create maps; Insert and get; Iterate entries; Check existence.

## Key Concepts

### 1. Create maps

Target: Create maps. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```v
mut ages := map[string]int{}
ages["Ada"] = 36
println(ages["Ada"])
```
### 2. Insert and get

Target: Insert and get. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```v
ages := {"Ada": 36, "Grace": 85}
println(ages.keys())
```
### 3. Iterate entries

Target: Iterate entries. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```v
for name, age in ages {
	println("$name: $age")
}
```
### 4. Check existence

Target: Check existence. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```v
if "Ada" in ages {
	println("found")
}
```

## Practice Questions

1. What is the key idea behind "Maps"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Maps with analogies and real-world examples"
1. "Show me common mistakes beginners make with Maps"
1. "Provide advanced patterns and performance considerations for Maps"

## Key Takeaways

- Master the core ideas of Maps through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
