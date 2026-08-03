---
{
  "title": "Tagged Types and OOP",
  "description": "Object-oriented programming in Ada.",
  "type": "lesson",
  "order": 14,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define tagged types",
    "Implement inheritance",
    "Use dispatching calls",
    "Write abstract types"
  ],
  "knowledge_refs": [
    "ada/ada-14-tagged-types"
  ],
  "prerequisites": [
    "Ada-13: Access Types and Pointers"
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

# ADA-14-TAGGED-TYPES: Tagged Types and OOP

## Introduction

Object-oriented programming in Ada. By the end of this lesson you will be able to: Define tagged types; Implement inheritance; Use dispatching calls; Write abstract types.

## Key Concepts

### 1. Define tagged types

Target: Define tagged types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ada
type Animal is tagged record
   Name : String (1 .. 20);
end record;
```
### 2. Implement inheritance

Target: Implement inheritance. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ada
type Dog is new Animal with record
   Breed : String (1 .. 20);
end record;
```
### 3. Use dispatching calls

Target: Use dispatching calls. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ada
function Sound (A : Animal) return String is
begin
   return "...";
end Sound;
```
### 4. Write abstract types

Target: Write abstract types. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ada
type Shape is abstract tagged null record;
procedure Draw (S : Shape) is abstract;
```

## Practice Questions

1. What is the key idea behind "Tagged Types and OOP"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Tagged Types and OOP with analogies and real-world examples"
1. "Show me common mistakes beginners make with Tagged Types and OOP"
1. "Provide advanced patterns and performance considerations for Tagged Types and OOP"

## Key Takeaways

- Master the core ideas of Tagged Types and OOP through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
