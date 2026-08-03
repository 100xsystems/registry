---
{
  "title": "Access Types and Pointers",
  "description": "Pointers, allocation, and controlled types.",
  "type": "lesson",
  "order": 13,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Declare access types",
    "Allocate with new",
    "Dereference safely",
    "Use access parameters"
  ],
  "knowledge_refs": [
    "ada/ada-13-access-types"
  ],
  "prerequisites": [
    "Ada-12: Generics"
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

# ADA-13-ACCESS-TYPES: Access Types and Pointers

## Introduction

Pointers, allocation, and controlled types. By the end of this lesson you will be able to: Declare access types; Allocate with new; Dereference safely; Use access parameters.

## Key Concepts

### 1. Declare access types

Target: Declare access types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ada
type Node;
type Node_Access is access Node;
type Node is record
   Value : Integer;
   Next  : Node_Access;
end record;
```
### 2. Allocate with new

Target: Allocate with new. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ada
Head : Node_Access := new Node'(Value => 1, Next => null);
```
### 3. Dereference safely

Target: Dereference safely. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ada
Head.Next := new Node'(Value => 2, Next => null);
```
### 4. Use access parameters

Target: Use access parameters. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ada
procedure Show (N : not null Node_Access) is begin null; end Show;
```

## Practice Questions

1. What is the key idea behind "Access Types and Pointers"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Access Types and Pointers with analogies and real-world examples"
1. "Show me common mistakes beginners make with Access Types and Pointers"
1. "Provide advanced patterns and performance considerations for Access Types and Pointers"

## Key Takeaways

- Master the core ideas of Access Types and Pointers through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
