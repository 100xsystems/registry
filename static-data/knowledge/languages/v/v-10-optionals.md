---
{
  "title": "Optionals and Results",
  "description": "Error handling with or.",
  "type": "lesson",
  "order": 10,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use ? types",
    "Handle with or",
    "Use or block",
    "Propagate errors"
  ],
  "knowledge_refs": [
    "v/v-10-optionals"
  ],
  "prerequisites": [
    "V-09: Enums"
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

# V-10-OPTIONALS: Optionals and Results

## Introduction

Error handling with or. By the end of this lesson you will be able to: Use ? types; Handle with or; Use or block; Propagate errors.

## Key Concepts

### 1. Use ? types

Target: Use ? types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```v
fn safe_div(a int, b int) ?int {
	if b == 0 {
		return error("div by zero")
	}
	return a / b
}

result := safe_div(10, 2) or { 0 }
println(result)
```
### 2. Handle with or

Target: Handle with or. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```v
fn read_file(path string) ?string {
	return os.read_file(path) or { return err }
}
```
### 3. Use or block

Target: Use or block. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```v
value := risky() or {
	println("fallback")
	-1
}
```
### 4. Propagate errors

Target: Propagate errors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```v
if r := safe_div(10, 0) {
	println(r)
} else {
	println("failed")
}
```

## Practice Questions

1. What is the key idea behind "Optionals and Results"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Optionals and Results with analogies and real-world examples"
1. "Show me common mistakes beginners make with Optionals and Results"
1. "Provide advanced patterns and performance considerations for Optionals and Results"

## Key Takeaways

- Master the core ideas of Optionals and Results through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
