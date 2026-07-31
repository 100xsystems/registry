---
{
  "title": "Make and Build Tooling",
  "description": "Makefiles, targets, automatic variables, compiler flags, sanitizers.",
  "type": "lesson",
  "order": 19,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write Makefiles with targets and deps",
    "Use automatic variables",
    "Compile with -Wall -Wextra -fsanitize",
    "Run gdb and valgrind"
  ],
  "knowledge_refs": [
    "c/c-19-build-tooling"
  ],
  "prerequisites": [
    "C-18"
  ],
  "references": [
    {
      "title": "GNU Make Manual",
      "url": "https://www.gnu.org/software/make/manual/html_node/Introduction.html"
    },
    {
      "title": "gcc Options Summary",
      "url": "https://gcc.gnu.org/onlinedocs/gcc/Option-Summary.html"
    },
    {
      "title": "Valgrind Quick Start",
      "url": "https://valgrind.org/docs/manual/quick-start.html"
    }
  ]
}
---

# C-19-BUILD-TOOLING: Make and Build Tooling

## Introduction

Makefiles, targets, automatic variables, compiler flags, sanitizers. By the end of this lesson you will be able to: Write Makefiles with targets and deps; Use automatic variables; Compile with -Wall -Wextra -fsanitize; Run gdb and valgrind.

## Key Concepts

### 1. Write Makefiles with targets and deps

Target: Write Makefiles with targets and deps. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```c
# Makefile — build automation
CC = gcc
CFLAGS = -Wall -Wextra -std=c17

app: main.o point.o
	$(CC) $(CFLAGS) -o app main.o point.o

main.o: main.c point.h
	$(CC) $(CFLAGS) -c main.c

point.o: point.c point.h
	$(CC) $(CFLAGS) -c point.c

clean:
	rm -f *.o app
```
### 2. Use automatic variables

Target: Use automatic variables. Apply the idiomatic pattern — this is how production C expresses this idea, so study the shape of the code.

```c
# Makefile with automatic variables
CC = gcc
CFLAGS = -Wall -Wextra -std=c17
SRCS = main.c point.c
OBJS = $(SRCS:.c=.o)

app: $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c point.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) app
```
### 3. Compile with -Wall -Wextra -fsanitize

Target: Compile with -Wall -Wextra -fsanitize. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```c
# compile flags you should know
# -g          : debug symbols (for gdb)
# -O2 / -O3   : optimization
# -Wall -Wextra : all warnings
# -fsanitize=address : ASan (memory errors)
# -fsanitize=undefined : UBSan (UB detection)
#
# gcc -g -O0 -fsanitize=address,undefined -o app main.c
```
### 4. Run gdb and valgrind

Target: Run gdb and valgrind. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```c
# debug with gdb
# gcc -g -o app app.c
# gdb ./app
#   (gdb) break main
#   (gdb) run
#   (gdb) next / step / print x / bt / quit
#
# valgrind for memory errors:
# valgrind --leak-check=full ./app
```

## Practice Questions

1. What is the key idea behind "Make and Build Tooling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Make and Build Tooling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Make and Build Tooling"
1. "Provide advanced patterns and performance considerations for Make and Build Tooling"

## Key Takeaways

- Master the core ideas of Make and Build Tooling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked cppreference docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
