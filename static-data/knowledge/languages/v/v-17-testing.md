---
{
  "title": "Testing",
  "description": "Unit tests in V.",
  "type": "lesson",
  "order": 17,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write test functions",
    "Use assert",
    "Run v test",
    "Test structs"
  ],
  "knowledge_refs": [
    "v/v-17-testing"
  ],
  "prerequisites": [
    "V-16: JSON"
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

# V-17-TESTING: Testing

## Introduction

Unit tests in V. By the end of this lesson you will be able to: Write test functions; Use assert; Run v test; Test structs.

## Key Concepts

### 1. Write test functions

Target: Write test functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```v
fn add(a int, b int) int {
	return a + b
}

fn test_add() {
	assert add(2, 3) == 5
}
```
### 2. Use assert

Target: Use assert. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```v
v test .
```
### 3. Run v test

Target: Run v test. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```v
fn test_strings() {
	assert "ab" + "cd" == "abcd"
}
```
### 4. Test structs

Target: Test structs. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```v
fn test_struct() {
	p := Person{"Ada", 36}
	assert p.age == 36
}
```

## Practice Questions

1. What is the key idea behind "Testing"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Testing with analogies and real-world examples"
1. "Show me common mistakes beginners make with Testing"
1. "Provide advanced patterns and performance considerations for Testing"

## Key Takeaways

- Master the core ideas of Testing through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
