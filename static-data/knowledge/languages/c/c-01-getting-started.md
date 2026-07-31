---
{
  "title": "Getting Started with C",
  "description": "Set up a C toolchain with gcc, understand compile/run, main function, and standard streams.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install gcc and compile your first C program",
    "Understand the compile pipeline (preprocess, compile, link)",
    "Use main with argc/argv",
    "Write to stdout and stderr"
  ],
  "knowledge_refs": [
    "c/c-01-getting-started"
  ],
  "prerequisites": [],
  "references": [
    {
      "title": "Beej’s Guide to C — Chapter 2",
      "url": "https://beej.us/guide/bgc/html/split/hello-world.html"
    },
    {
      "title": "learn-c.org — Hello World",
      "url": "https://learn-c.org/en/Hello%2C_World"
    },
    {
      "title": "cppreference — main function",
      "url": "https://en.cppreference.com/w/c/language/main_function"
    }
  ]
}
---

# C-01-GETTING-STARTED: Getting Started with C

## Introduction

Set up a C toolchain with gcc, understand compile/run, main function, and standard streams. By the end of this lesson you will be able to: Install gcc and compile your first C program; Understand the compile pipeline (preprocess, compile, link); Use main with argc/argv; Write to stdout and stderr.

## Key Concepts

### 1. Install gcc and compile your first C program

Target: Install gcc and compile your first C program. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```c
#include <stdio.h>

// compile: gcc -Wall -Wextra -o hello hello.c && ./hello
int main(void) {
    printf("Hello, 100X Systems!\n");
    return 0;
}
```
### 2. Understand the compile pipeline (preprocess, compile, link)

Target: Understand the compile pipeline (preprocess, compile, link). Apply the idiomatic pattern — this is how production C expresses this idea, so study the shape of the code.

```c
#include <stdio.h>

// toolchain: preprocessor -> compiler -> assembler -> linker
// gcc -E hello.c (preprocess), gcc -S (assembly), gcc -c (object)
int main(void) {
    printf("gcc -Wall -Wextra -std=c17 hello.c\n");
    return 0;
}
```
### 3. Use main with argc/argv

Target: Use main with argc/argv. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```c
#include <stdio.h>

// argc = argument count, argv = argument vector
int main(int argc, char *argv[]) {
    printf("argc = %d\n", argc);
    for (int i = 0; i < argc; i++) printf("argv[%d] = %s\n", i, argv[i]);
    return 0;
}
```
### 4. Write to stdout and stderr

Target: Write to stdout and stderr. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```c
#include <stdio.h>

int main(void) {
    // three standard streams
    fprintf(stdout, "stdout: buffered\n");
    fprintf(stderr, "stderr: unbuffered\n");
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Getting Started with C"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with C with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with C"
1. "Provide advanced patterns and performance considerations for Getting Started with C"

## Key Takeaways

- Master the core ideas of Getting Started with C through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked cppreference docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
