---
{
  "title": "File I/O",
  "description": "fopen, fprintf/fscanf, fgets, binary I/O, fseek, and error handling.",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Open files with fopen and modes",
    "Read lines with fgets",
    "Read formatted data with fscanf",
    "Do binary I/O with fwrite/fread and fseek"
  ],
  "knowledge_refs": [
    "c/c-11-file-io"
  ],
  "prerequisites": [
    "C-10"
  ],
  "references": [
    {
      "title": "learn-c.org — File I/O",
      "url": "https://learn-c.org/en/File_I/O"
    },
    {
      "title": "cppreference — fopen",
      "url": "https://en.cppreference.com/w/c/io/fopen"
    },
    {
      "title": "cppreference — Input/Output Functions",
      "url": "https://en.cppreference.com/w/c/io"
    }
  ]
}
---

# C-11-FILE-IO: File I/O

## Introduction

fopen, fprintf/fscanf, fgets, binary I/O, fseek, and error handling. By the end of this lesson you will be able to: Open files with fopen and modes; Read lines with fgets; Read formatted data with fscanf; Do binary I/O with fwrite/fread and fseek.

## Key Concepts

### 1. Open files with fopen and modes

Target: Open files with fopen and modes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```c
#include <stdio.h>

int main(void) {
    FILE *f = fopen("/tmp/notes.txt", "w");   // "r", "w", "a", "rb"...
    if (!f) { perror("fopen"); return 1; }
    fprintf(f, "hello file\n");
    fclose(f);
    return 0;
}
```
### 2. Read lines with fgets

Target: Read lines with fgets. Apply the idiomatic pattern — this is how production C expresses this idea, so study the shape of the code.

```c
#include <stdio.h>

int main(void) {
    FILE *f = fopen("/tmp/notes.txt", "r");
    if (!f) return 1;
    char line[128];
    while (fgets(line, sizeof(line), f)) printf("%s", line);
    fclose(f);
    return 0;
}
```
### 3. Read formatted data with fscanf

Target: Read formatted data with fscanf. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```c
#include <stdio.h>

int main(void) {
    // fscanf: formatted reading (careful with %s overflow!)
    FILE *f = fopen("/tmp/data.txt", "w+");
    if (!f) return 1;
    fprintf(f, "100 Alice\n");
    rewind(f);
    int id;
    char name[32];
    fscanf(f, "%d %31s", &id, name);
    printf("%d %s\n", id, name);
    fclose(f);
    return 0;
}
```
### 4. Do binary I/O with fwrite/fread and fseek

Target: Do binary I/O with fwrite/fread and fseek. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```c
#include <stdio.h>

int main(void) {
    // binary I/O + random access
    FILE *f = fopen("/tmp/bin.dat", "wb+");
    int data[4] = {1, 2, 3, 4};
    fwrite(data, sizeof(int), 4, f);
    fseek(f, 2 * sizeof(int), SEEK_SET);   // jump to index 2
    int x;
    fread(&x, sizeof(int), 1, f);
    printf("%d\n", x);   // 3
    fclose(f);
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "File I/O"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain File I/O with analogies and real-world examples"
1. "Show me common mistakes beginners make with File I/O"
1. "Provide advanced patterns and performance considerations for File I/O"

## Key Takeaways

- Master the core ideas of File I/O through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked cppreference docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
