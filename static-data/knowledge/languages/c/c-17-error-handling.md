---
{
  "title": "Error Handling",
  "description": "errno, perror, strerror, return codes, and setjmp/longjmp.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use errno with perror and strerror",
    "Detect math domain errors",
    "Use return-code conventions",
    "Use setjmp/longjmp for non-local errors"
  ],
  "knowledge_refs": [
    "c/c-17-error-handling"
  ],
  "prerequisites": [
    "C-16"
  ],
  "references": [
    {
      "title": "cppreference — errno",
      "url": "https://en.cppreference.com/w/c/error/errno"
    },
    {
      "title": "cppreference — perror",
      "url": "https://en.cppreference.com/w/c/io/perror"
    },
    {
      "title": "cppreference — setjmp",
      "url": "https://en.cppreference.com/w/c/program/setjmp"
    }
  ]
}
---

# C-17-ERROR-HANDLING: Error Handling

## Introduction

errno, perror, strerror, return codes, and setjmp/longjmp. By the end of this lesson you will be able to: Use errno with perror and strerror; Detect math domain errors; Use return-code conventions; Use setjmp/longjmp for non-local errors.

## Key Concepts

### 1. Use errno with perror and strerror

Target: Use errno with perror and strerror. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```c
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    FILE *f = fopen("/nonexistent/file", "r");
    if (!f) {
        printf("errno=%d %s\n", errno, strerror(errno));
        perror("fopen");
    }
    return 0;
}
```
### 2. Detect math domain errors

Target: Detect math domain errors. Apply the idiomatic pattern — this is how production C expresses this idea, so study the shape of the code.

```c
#include <stdio.h>
#include <errno.h>
#include <math.h>

int main(void) {
    errno = 0;
    double r = sqrt(-1.0);   // domain error
    if (errno == EDOM) printf("math domain error\n");
    (void)r;
    return 0;
}
```
### 3. Use return-code conventions

Target: Use return-code conventions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```c
#include <stdio.h>

// return-code convention: 0 = success, non-zero = error
int divide(int a, int b, int *out) {
    if (b == 0) return -1;
    *out = a / b;
    return 0;
}

int main(void) {
    int result;
    if (divide(10, 0, &result) != 0) {
        printf("division error\n");
        return 1;
    }
    printf("%d\n", result);
    return 0;
}
```
### 4. Use setjmp/longjmp for non-local errors

Target: Use setjmp/longjmp for non-local errors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```c
#include <stdio.h>
#include <setjmp.h>

// setjmp/longjmp: non-local goto for error handling
static jmp_buf env;

int main(void) {
    if (setjmp(env) == 0) {
        printf("about to longjmp\n");
        longjmp(env, 1);
    } else {
        printf("recovered from longjmp\n");
    }
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Error Handling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Error Handling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Error Handling"
1. "Provide advanced patterns and performance considerations for Error Handling"

## Key Takeaways

- Master the core ideas of Error Handling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked cppreference docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
