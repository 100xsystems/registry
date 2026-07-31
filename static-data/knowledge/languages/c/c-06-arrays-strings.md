---
{
  "title": "Arrays and Strings",
  "description": "One and multi-dimensional arrays, null-terminated strings, string.h.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare and iterate arrays",
    "Work with C strings and string.h",
    "Use multi-dimensional arrays",
    "Understand array decay to pointers"
  ],
  "knowledge_refs": [
    "c/c-06-arrays-strings"
  ],
  "prerequisites": [
    "C-05"
  ],
  "references": [
    {
      "title": "learn-c.org — Arrays",
      "url": "https://learn-c.org/en/Arrays"
    },
    {
      "title": "learn-c.org — Strings",
      "url": "https://learn-c.org/en/Strings"
    },
    {
      "title": "cppreference — String Functions",
      "url": "https://en.cppreference.com/w/c/string/byte"
    }
  ]
}
---

# C-06-ARRAYS-STRINGS: Arrays and Strings

## Introduction

One and multi-dimensional arrays, null-terminated strings, string.h. By the end of this lesson you will be able to: Declare and iterate arrays; Work with C strings and string.h; Use multi-dimensional arrays; Understand array decay to pointers.

## Key Concepts

### 1. Declare and iterate arrays

Target: Declare and iterate arrays. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```c
#include <stdio.h>

int main(void) {
    int nums[5] = {1, 2, 3, 4, 5};
    for (int i = 0; i < 5; i++) printf("%d ", nums[i]);
    printf("\n");
    printf("nums[0]=%d size=%zu\n", nums[0], sizeof(nums) / sizeof(nums[0]));
    return 0;
}
```
### 2. Work with C strings and string.h

Target: Work with C strings and string.h. Apply the idiomatic pattern — this is how production C expresses this idea, so study the shape of the code.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    // C strings are null-terminated char arrays
    char msg[] = "hello";
    printf("%s len=%zu\n", msg, strlen(msg));   // hello len=5
    char buf[32];
    strcpy(buf, "world");
    strcat(buf, "!");
    printf("%s\n", buf);                        // world!
    return 0;
}
```
### 3. Use multi-dimensional arrays

Target: Use multi-dimensional arrays. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```c
#include <stdio.h>

int main(void) {
    // 2D arrays: row-major
    int grid[2][3] = {{1, 2, 3}, {4, 5, 6}};
    for (int r = 0; r < 2; r++)
        for (int c = 0; c < 3; c++)
            printf("%d ", grid[r][c]);
    printf("\n");
    printf("grid[1][0] = %d\n", grid[1][0]);   // 4
    return 0;
}
```
### 4. Understand array decay to pointers

Target: Understand array decay to pointers. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```c
#include <stdio.h>

int main(void) {
    // strings are arrays of char: iterate safely
    char *name = "100x";
    for (int i = 0; name[i] != '\0'; i++) putchar(name[i]);
    printf("\n");
    // array decay: name in an expression is &name[0]
    printf("pointer to first char: %c\n", *name);
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Arrays and Strings"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arrays and Strings with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arrays and Strings"
1. "Provide advanced patterns and performance considerations for Arrays and Strings"

## Key Takeaways

- Master the core ideas of Arrays and Strings through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked cppreference docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
