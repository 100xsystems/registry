---
{
  "title": "Control Flow",
  "description": "if/else, switch, for, while, do-while loops, and jump statements.",
  "type": "lesson",
  "order": 4,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write if/else branching logic",
    "Use switch statements",
    "Use for, while, and do-while loops",
    "Apply break and continue"
  ],
  "knowledge_refs": [
    "c/c-04-control-flow"
  ],
  "prerequisites": [
    "C-03"
  ],
  "references": [
    {
      "title": "learn-c.org — Conditions",
      "url": "https://learn-c.org/en/Conditions"
    },
    {
      "title": "learn-c.org — Loops",
      "url": "https://learn-c.org/en/Loops"
    },
    {
      "title": "cppreference — Statements",
      "url": "https://en.cppreference.com/w/c/language/statements"
    }
  ]
}
---

# C-04-CONTROL-FLOW: Control Flow

## Introduction

if/else, switch, for, while, do-while loops, and jump statements. By the end of this lesson you will be able to: Write if/else branching logic; Use switch statements; Use for, while, and do-while loops; Apply break and continue.

## Key Concepts

### 1. Write if/else branching logic

Target: Write if/else branching logic. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```c
#include <stdio.h>

int main(void) {
    int score = 85;
    if (score >= 90) printf("A\n");
    else if (score >= 80) printf("B\n");
    else printf("C\n");
    return 0;
}
```
### 2. Use switch statements

Target: Use switch statements. Apply the idiomatic pattern — this is how production C expresses this idea, so study the shape of the code.

```c
#include <stdio.h>

int main(void) {
    int day = 3;
    switch (day) {
        case 1: printf("Monday\n"); break;
        case 2: printf("Tuesday\n"); break;
        default: printf("Other\n"); break;
    }
    return 0;
}
```
### 3. Use for, while, and do-while loops

Target: Use for, while, and do-while loops. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```c
#include <stdio.h>

int main(void) {
    for (int i = 0; i < 5; i++) printf("%d ", i);  // 0 1 2 3 4
    printf("\n");
    int j = 0;
    while (j < 3) { printf("%d ", j); j++; }       // 0 1 2
    printf("\n");
    int k = 0;
    do { printf("%d ", k); k++; } while (k < 2);   // 0 1 (runs at least once)
    printf("\n");
    return 0;
}
```
### 4. Apply break and continue

Target: Apply break and continue. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```c
#include <stdio.h>

int main(void) {
    for (int i = 0; i < 10; i++) {
        if (i == 2) continue;   // skip 2
        if (i == 5) break;      // stop at 5
        printf("%d ", i);       // 0 1 3 4
    }
    printf("\n");
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked cppreference docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
