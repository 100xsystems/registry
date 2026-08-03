---
{
  "title": "Operators and Expressions",
  "description": "Arithmetic, relational, and logical operators.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use arithmetic operators",
    "Compare with relational operators",
    "Combine with logical operators",
    "Control evaluation with parentheses"
  ],
  "knowledge_refs": [
    "ada/ada-04-expressions"
  ],
  "prerequisites": [
    "Ada-03: Variables and Constants"
  ],
  "references": [
    {
      "title": "Ada Reference Manual",
      "url": "https://www.adaic.org/resources/add_content/standards/",
      "description": "The official language standard"
    },
    {
      "title": "Learn Ada",
      "url": "https://learn.adacore.com/",
      "description": "AdaCore official interactive course"
    },
    {
      "title": "Ada Programming (Wikibooks)",
      "url": "https://en.wikibooks.org/wiki/Ada_Programming",
      "description": "Community textbook"
    }
  ]
}
---

# ADA-04-EXPRESSIONS: Operators and Expressions

## Introduction

Arithmetic, relational, and logical operators. By the end of this lesson you will be able to: Use arithmetic operators; Compare with relational operators; Combine with logical operators; Control evaluation with parentheses.

## Key Concepts

### 1. Use arithmetic operators

Target: Use arithmetic operators. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ada
x : Integer := 2 + 3 * 4;   -- 14

procedure Show is
begin
   null;
end Show;
```
### 2. Compare with relational operators

Target: Compare with relational operators. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ada
if a > b and c < d then
   null;
end if;
```
### 3. Combine with logical operators

Target: Combine with logical operators. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ada
odd_number : Boolean := (n mod 2) = 1;
```
### 4. Control evaluation with parentheses

Target: Control evaluation with parentheses. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ada
z : Integer := x / y;  -- integer division
divide_error : exception;
```

## Practice Questions

1. What is the key idea behind "Operators and Expressions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Operators and Expressions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Operators and Expressions"
1. "Provide advanced patterns and performance considerations for Operators and Expressions"

## Key Takeaways

- Master the core ideas of Operators and Expressions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
