---
{
  "title": "Structs and Unions",
  "description": "Struct declaration, member access, arrow operator, copies, unions.",
  "type": "lesson",
  "order": 8,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Declare and use structs",
    "Access members through pointers with ->",
    "Copy and pass structs by value",
    "Use unions for shared memory"
  ],
  "knowledge_refs": [
    "c/c-08-structs-unions"
  ],
  "prerequisites": [
    "C-07"
  ],
  "references": [
    {
      "title": "learn-c.org — Structures",
      "url": "https://learn-c.org/en/Structures"
    },
    {
      "title": "cppreference — Struct Declaration",
      "url": "https://en.cppreference.com/w/c/language/struct"
    },
    {
      "title": "cppreference — Union Declaration",
      "url": "https://en.cppreference.com/w/c/language/union"
    }
  ]
}
---

# C-08-STRUCTS-UNIONS: Structs and Unions

## Introduction

Struct declaration, member access, arrow operator, copies, unions. By the end of this lesson you will be able to: Declare and use structs; Access members through pointers with ->; Copy and pass structs by value; Use unions for shared memory.

## Key Concepts

### 1. Declare and use structs

Target: Declare and use structs. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```c
#include <stdio.h>

struct Point {
    int x;
    int y;
};

int main(void) {
    struct Point p = {3, 4};
    printf("(%d, %d)\n", p.x, p.y);
    return 0;
}
```
### 2. Access members through pointers with ->

Target: Access members through pointers with ->. Apply the idiomatic pattern — this is how production C expresses this idea, so study the shape of the code.

```c
#include <stdio.h>

struct Point { int x, y; };

int main(void) {
    // access through pointer with ->
    struct Point p = {1, 2};
    struct Point *pp = &p;
    pp->x = 99;
    printf("(%d, %d)\n", p.x, p.y);
    return 0;
}
```
### 3. Copy and pass structs by value

Target: Copy and pass structs by value. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```c
#include <stdio.h>
#include <string.h>

struct Person {
    char name[32];
    int age;
};

int main(void) {
    struct Person alice;
    strcpy(alice.name, "Alice");
    alice.age = 30;
    printf("%s %d\n", alice.name, alice.age);
    // structs are copied by value
    struct Person copy = alice;
    copy.age = 31;
    printf("%d %d\n", alice.age, copy.age);  // 30 31
    return 0;
}
```
### 4. Use unions for shared memory

Target: Use unions for shared memory. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```c
#include <stdio.h>

// union: members share the same memory
union Number {
    int i;
    float f;
};

int main(void) {
    union Number n;
    n.i = 42;
    printf("%d\n", n.i);
    n.f = 3.14f;             // overwrites the int
    printf("%f\n", n.f);
    printf("size of union: %zu\n", sizeof(n));  // size of largest member
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Structs and Unions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Structs and Unions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Structs and Unions"
1. "Provide advanced patterns and performance considerations for Structs and Unions"

## Key Takeaways

- Master the core ideas of Structs and Unions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked cppreference docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
