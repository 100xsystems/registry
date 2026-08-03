---
{
  "title": "CLOS: Classes and Objects",
  "description": "defclass, defmethod, and generics.",
  "type": "lesson",
  "order": 10,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define classes",
    "Create instances",
    "Define methods",
    "Use inheritance"
  ],
  "knowledge_refs": [
    "common-lisp/common-lisp-10-clos"
  ],
  "prerequisites": [
    "Common Lisp-09: List Manipulation"
  ],
  "references": [
    {
      "title": "Practical Common Lisp",
      "url": "https://gigamonkeys.com/book/",
      "description": "The classic online book"
    },
    {
      "title": "Common Lisp HyperSpec",
      "url": "http://www.lispworks.com/documentation/HyperSpec/Front/Contents.htm",
      "description": "Official standard reference"
    },
    {
      "title": "Common Lisp Cookbook",
      "url": "https://lispcookbook.github.io/cl-cookbook/",
      "description": "Community cookbook"
    }
  ]
}
---

# COMMON-LISP-10-CLOS: CLOS: Classes and Objects

## Introduction

defclass, defmethod, and generics. By the end of this lesson you will be able to: Define classes; Create instances; Define methods; Use inheritance.

## Key Concepts

### 1. Define classes

Target: Define classes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lisp
(defclass person ()
  ((name :initarg :name :accessor person-name)
   (age :initarg :age :accessor person-age)))
```
### 2. Create instances

Target: Create instances. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lisp
(make-instance 'person :name "Ada" :age 36)
```
### 3. Define methods

Target: Define methods. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lisp
(defmethod greet ((p person))
  (format t "Hi, ~a~%" (person-name p)))
```
### 4. Use inheritance

Target: Use inheritance. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lisp
(defclass developer (person)
  ((language :initarg :language :accessor dev-language)))
```

## Practice Questions

1. What is the key idea behind "CLOS: Classes and Objects"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain CLOS: Classes and Objects with analogies and real-world examples"
1. "Show me common mistakes beginners make with CLOS: Classes and Objects"
1. "Provide advanced patterns and performance considerations for CLOS: Classes and Objects"

## Key Takeaways

- Master the core ideas of CLOS: Classes and Objects through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
