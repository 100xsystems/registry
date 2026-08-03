---
{
  "title": "Arrays",
  "description": "Dynamic arrays.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create arrays",
    "Append elements",
    "Iterate arrays",
    "Use array methods"
  ],
  "knowledge_refs": [
    "v/v-05-arrays"
  ],
  "prerequisites": [
    "V-04: Functions"
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

# V-05-ARRAYS: Arrays

## Introduction

Dynamic arrays. By the end of this lesson you will be able to: Create arrays; Append elements; Iterate arrays; Use array methods.

## Key Concepts

### 1. Create arrays

Target: Create arrays. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```v
mut nums := [1, 2, 3]
nums << 4
println(nums)
```
### 2. Append elements

Target: Append elements. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```v
nums := [1, 2, 3, 4]
println(nums.filter(fn (n int) bool { return n % 2 == 0 }))
```
### 3. Iterate arrays

Target: Iterate arrays. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```v
for n in nums {
	println(n)
}
```
### 4. Use array methods

Target: Use array methods. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```v
println(nums.len)
println(nums[1..3])
```

## Practice Questions

1. What is the key idea behind "Arrays"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arrays with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arrays"
1. "Provide advanced patterns and performance considerations for Arrays"

## Key Takeaways

- Master the core ideas of Arrays through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
