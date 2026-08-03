---
{
  "title": "Arrays and Maps",
  "description": "Collections.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create arrays",
    "Use array methods",
    "Use maps",
    "Iterate collections"
  ],
  "knowledge_refs": [
    "haxe/haxe-05-arrays"
  ],
  "prerequisites": [
    "Haxe-04: Functions"
  ],
  "references": [
    {
      "title": "Haxe Documentation",
      "url": "https://haxe.org/documentation/",
      "description": "Official docs"
    },
    {
      "title": "Haxe Manual",
      "url": "https://haxe.org/manual/introduction.html",
      "description": "The language manual"
    },
    {
      "title": "Haxe Cookbook",
      "url": "https://code.haxe.org/",
      "description": "Community recipes"
    }
  ]
}
---

# HAXE-05-ARRAYS: Arrays and Maps

## Introduction

Collections. By the end of this lesson you will be able to: Create arrays; Use array methods; Use maps; Iterate collections.

## Key Concepts

### 1. Create arrays

Target: Create arrays. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haxe
var nums = [1, 2, 3];
nums.push(4);
trace(nums.length);
```
### 2. Use array methods

Target: Use array methods. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haxe
var doubled = nums.map(n -> n * 2);
```
### 3. Use maps

Target: Use maps. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haxe
var ages = ["Ada" => 36];
ages["Grace"] = 85;
trace(ages["Ada"]);
```
### 4. Iterate collections

Target: Iterate collections. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haxe
for (n in nums) trace(n);
```

## Practice Questions

1. What is the key idea behind "Arrays and Maps"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arrays and Maps with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arrays and Maps"
1. "Provide advanced patterns and performance considerations for Arrays and Maps"

## Key Takeaways

- Master the core ideas of Arrays and Maps through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
