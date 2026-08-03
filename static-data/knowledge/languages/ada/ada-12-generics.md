---
{
  "title": "Generics",
  "description": "Generic subprograms and packages for reuse.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write generic functions",
    "Write generic packages",
    "Instantiate generics",
    "Constrain with generic formal types"
  ],
  "knowledge_refs": [
    "ada/ada-12-generics"
  ],
  "prerequisites": [
    "Ada-11: Packages and Visibility"
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

# ADA-12-GENERICS: Generics

## Introduction

Generic subprograms and packages for reuse. By the end of this lesson you will be able to: Write generic functions; Write generic packages; Instantiate generics; Constrain with generic formal types.

## Key Concepts

### 1. Write generic functions

Target: Write generic functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ada
generic
   type T is private;
function Identity (X : T) return T;
```
### 2. Write generic packages

Target: Write generic packages. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ada
function Identity is new Identity (Integer);
```
### 3. Instantiate generics

Target: Instantiate generics. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ada
generic
   type Element is private;
package Stack is
   procedure Push (E : Element);
end Stack;
```
### 4. Constrain with generic formal types

Target: Constrain with generic formal types. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ada
generic
   type Index is (<>);
   type Vector is array (Index range <>) of Integer;
package Stats is
   function Sum (V : Vector) return Integer;
end Stats;
```

## Practice Questions

1. What is the key idea behind "Generics"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Generics with analogies and real-world examples"
1. "Show me common mistakes beginners make with Generics"
1. "Provide advanced patterns and performance considerations for Generics"

## Key Takeaways

- Master the core ideas of Generics through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
