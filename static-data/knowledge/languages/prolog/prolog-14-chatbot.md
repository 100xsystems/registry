---
{
  "title": "Expert Systems and Chatbots",
  "description": "Simple rule-based reasoning.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Design rule sets",
    "Implement diagnosis",
    "Handle unknown inputs",
    "Extend knowledge"
  ],
  "knowledge_refs": [
    "prolog/prolog-14-chatbot"
  ],
  "prerequisites": [
    "Prolog-13: DCG: Grammar Rules"
  ],
  "references": [
    {
      "title": "SWI-Prolog Documentation",
      "url": "https://www.swi-prolog.org/pldoc/",
      "description": "Official SWI-Prolog docs"
    },
    {
      "title": "Learn Prolog Now!",
      "url": "https://www.learnprolognow.org/",
      "description": "The classic free textbook"
    },
    {
      "title": "Prolog Wiki",
      "url": "https://en.wikipedia.org/wiki/Prolog",
      "description": "Overview article"
    }
  ]
}
---

# PROLOG-14-CHATBOT: Expert Systems and Chatbots

## Introduction

Simple rule-based reasoning. By the end of this lesson you will be able to: Design rule sets; Implement diagnosis; Handle unknown inputs; Extend knowledge.

## Key Concepts

### 1. Design rule sets

Target: Design rule sets. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```prolog
symptom(fever).
symptom(cough).
```
### 2. Implement diagnosis

Target: Implement diagnosis. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```prolog
disease(flu) :- symptom(fever), symptom(cough).
```
### 3. Handle unknown inputs

Target: Handle unknown inputs. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```prolog
diagnose(D) :- disease(D), write("Diagnosis: "), write(D), nl.
```
### 4. Extend knowledge

Target: Extend knowledge. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```prolog
ask(S) :-
    format("Do you have ~w? ", [S]),
    read(yes).
```

## Practice Questions

1. What is the key idea behind "Expert Systems and Chatbots"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Expert Systems and Chatbots with analogies and real-world examples"
1. "Show me common mistakes beginners make with Expert Systems and Chatbots"
1. "Provide advanced patterns and performance considerations for Expert Systems and Chatbots"

## Key Takeaways

- Master the core ideas of Expert Systems and Chatbots through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
