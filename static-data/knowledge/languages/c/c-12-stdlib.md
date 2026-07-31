---
{
  "title": "Standard Library",
  "description": "string.h, stdlib.h, math.h, and ctype.h essentials.",
  "type": "lesson",
  "order": 12,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use string.h functions",
    "Convert strings with atoi/strtol",
    "Use math.h functions",
    "Use ctype.h character classification"
  ],
  "knowledge_refs": [
    "c/c-12-stdlib"
  ],
  "prerequisites": [
    "C-11"
  ],
  "references": [
    {
      "title": "cppreference — Standard Library Header",
      "url": "https://en.cppreference.com/w/c/header"
    },
    {
      "title": "cppreference — string.h",
      "url": "https://en.cppreference.com/w/c/string"
    },
    {
      "title": "cppreference — stdlib.h",
      "url": "https://en.cppreference.com/w/c/header/stdlib"
    }
  ]
}
---

# C-12-STDLIB: Standard Library

## Introduction

string.h, stdlib.h, math.h, and ctype.h essentials. By the end of this lesson you will be able to: Use string.h functions; Convert strings with atoi/strtol; Use math.h functions; Use ctype.h character classification.

## Key Concepts

### 1. Use string.h functions

Target: Use string.h functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char a[] = "hello";
    char b[32];
    strcpy(b, a);
    printf("%s %s\n", a, b);
    printf("compare: %d\n", strcmp("a", "b"));   // negative
    printf("find: %s\n", strchr("hello", 'l'));
    return 0;
}
```
### 2. Convert strings with atoi/strtol

Target: Convert strings with atoi/strtol. Apply the idiomatic pattern — this is how production C expresses this idea, so study the shape of the code.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    printf("%d\n", atoi("42"));       // string -> int
    printf("%.2f\n", atof("3.14159"));
    long l = strtol("0xFF", NULL, 16); // base 16 parse
    printf("%ld\n", l);               // 255
    int rand_val = rand() % 100;       // 0-99 (need srand seed)
    printf("%d\n", rand_val);
    return 0;
}
```
### 3. Use math.h functions

Target: Use math.h functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```c
#include <stdio.h>
#include <math.h>

int main(void) {
    printf("%.2f\n", sqrt(16.0));     // 4.00
    printf("%.2f\n", pow(2.0, 10.0)); // 1024.00
    printf("%.2f\n", fabs(-3.5));     // 3.50
    printf("%.2f\n", ceil(2.1));      // 3.00
    printf("%.2f\n", floor(2.9));     // 2.00
    return 0;
}
```
### 4. Use ctype.h character classification

Target: Use ctype.h character classification. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```c
#include <stdio.h>
#include <ctype.h>

int main(void) {
    printf("%d %d\n", isalpha('a'), isdigit('7'));
    printf("%c\n", toupper('a'));
    printf("%d\n", isspace(' '));
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Standard Library"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Standard Library with analogies and real-world examples"
1. "Show me common mistakes beginners make with Standard Library"
1. "Provide advanced patterns and performance considerations for Standard Library"

## Key Takeaways

- Master the core ideas of Standard Library through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked cppreference docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
