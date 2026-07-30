---
title: "Context and Cancellation"
description: "Context values, cancellation, deadlines, propagating context through goroutines, and context patterns."
type: lesson
order: 17
duration: "45 min"
difficulty: advanced
learning_objectives:
  - "Create and use context.WithCancel, WithTimeout, WithDeadline"
  - "Propagate context through function calls and goroutines"
  - "Handle graceful cancellation of concurrent operations"
  - "Store request-scoped values in context"
knowledge_refs:
  - go/go-17-context-cancellation
prerequisites:
  - "GO-12"
  - "GO-11"
references:
    - title: "Go Blog — Context"
      url: "https://go.dev/blog/context"
    - title: "Go by Example — Context"
      url: "https://gobyexample.com/context"
    - title: "Go Documentation — context package"
      url: "https://pkg.go.dev/context"
---

# GO-17-CONTEXT-CANCELLATION: Context and Cancellation

## Introduction

Context values, cancellation, deadlines, propagating context through goroutines, and context patterns.

## Learning Objectives

By the end of this lesson, you will be able to:

- Create and use context.WithCancel, WithTimeout, WithDeadline
- Propagate context through function calls and goroutines
- Handle graceful cancellation of concurrent operations
- Store request-scoped values in context

## Key Concepts

### Subtopic 1: Foundation

This section covers the foundational concepts of context and cancellation. Understanding these core ideas is essential before moving to advanced topics.

**Key points to remember:**
- Start with the basics and build up systematically
- Practice each concept with small code examples
- Refer to the linked resources for deeper dives

### Subtopic 2: Practical Application

Apply the concepts you've learned to solve real problems. Practice is essential for mastery.

**Example approach:**
1. Write small programs that exercise each concept
2. Combine concepts to solve more complex problems
3. Review and refactor your code for clarity

### Subtopic 3: Best Practices and Patterns

Learn the idiomatic patterns and best practices for this topic. Writing clean, maintainable code is a hallmark of an experienced developer.

**Guidelines:**
- Follow language conventions and style guides
- Favor clarity over cleverness
- Test your code thoroughly

## Practice Questions

1. What are the key concepts covered in this lesson?
2. Write a small program that demonstrates at least two concepts from this lesson.
3. How would you explain this topic to a fellow developer?

## LLM Prompts for Deeper Understanding

1. "Explain Context and Cancellation with analogies and examples"
2. "Show me common mistakes beginners make with context and cancellation"
3. "Provide advanced patterns and real-world use cases for context and cancellation"

## Key Takeaways

- Solidify your understanding of context and cancellation
- Practice with real code, not just theory
- Explore the reference resources for in-depth coverage

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
