---
{
  "title": "Linked Lists and Data Structures",
  "description": "Struct nodes, linked lists, traversal, free, and reusable patterns.",
  "type": "lesson",
  "order": 15,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Build singly linked list nodes",
    "Push and traverse linked lists",
    "Free lists safely",
    "Design reusable container patterns"
  ],
  "knowledge_refs": [
    "c/c-15-data-structures"
  ],
  "prerequisites": [
    "C-14"
  ],
  "references": [
    {
      "title": "learn-c.org — Linked Lists",
      "url": "https://learn-c.org/en/Linked_lists"
    },
    {
      "title": "cppreference — Struct Pointer Members",
      "url": "https://en.cppreference.com/w/c/language/struct"
    },
    {
      "title": "Wikipedia — Linked List",
      "url": "https://en.wikipedia.org/wiki/Linked_list"
    }
  ]
}
---

# C-15-DATA-STRUCTURES: Linked Lists and Data Structures

## Introduction

Struct nodes, linked lists, traversal, free, and reusable patterns. By the end of this lesson you will be able to: Build singly linked list nodes; Push and traverse linked lists; Free lists safely; Design reusable container patterns.

## Key Concepts

### 1. Build singly linked list nodes

Target: Build singly linked list nodes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```c
#include <stdio.h>
#include <stdlib.h>

// singly linked list node
struct Node {
    int data;
    struct Node *next;
};

int main(void) {
    struct Node *head = malloc(sizeof(struct Node));
    head->data = 1;
    head->next = NULL;
    printf("%d\n", head->data);
    free(head);
    return 0;
}
```
### 2. Push and traverse linked lists

Target: Push and traverse linked lists. Apply the idiomatic pattern — this is how production C expresses this idea, so study the shape of the code.

```c
#include <stdio.h>
#include <stdlib.h>

struct Node { int data; struct Node *next; };

// push to front
struct Node *push(struct Node *head, int val) {
    struct Node *n = malloc(sizeof(struct Node));
    n->data = val;
    n->next = head;
    return n;
}

int main(void) {
    struct Node *head = NULL;
    head = push(head, 3);
    head = push(head, 2);
    head = push(head, 1);
    for (struct Node *p = head; p; p = p->next) printf("%d ", p->data);
    printf("\n");   // 1 2 3
    return 0;
}
```
### 3. Free lists safely

Target: Free lists safely. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```c
#include <stdio.h>
#include <stdlib.h>

// traversal with free (always free every node)
struct Node { int data; struct Node *next; };

void free_list(struct Node *head) {
    while (head) {
        struct Node *tmp = head;
        head = head->next;
        free(tmp);
    }
}

int main(void) {
    // build tiny list inline
    struct Node *a = malloc(sizeof(*a));
    struct Node *b = malloc(sizeof(*b));
    a->data = 1; a->next = b;
    b->data = 2; b->next = NULL;
    free_list(a);
    printf("freed\n");
    return 0;
}
```
### 4. Design reusable container patterns

Target: Design reusable container patterns. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```c
#include <stdio.h>
#include <stdlib.h>

// generic stack of void * — reusable data structure
struct Stack {
    void **items;
    int top;
    int cap;
};

struct Stack *stack_new(int cap) {
    struct Stack *s = malloc(sizeof(*s));
    s->items = malloc(cap * sizeof(void *));
    s->top = 0;
    s->cap = cap;
    return s;
}

void stack_push(struct Stack *s, void *v) {
    s->items[s->top++] = v;
}

void *stack_pop(struct Stack *s) {
    return s->top ? s->items[--s->top] : NULL;
}

int main(void) {
    struct Stack *s = stack_new(4);
    int a = 1, b = 2;
    stack_push(s, &a);
    stack_push(s, &b);
    printf("%d %d\n", *(int *)stack_pop(s), *(int *)stack_pop(s));  // 2 1
    free(s->items);
    free(s);
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Linked Lists and Data Structures"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Linked Lists and Data Structures with analogies and real-world examples"
1. "Show me common mistakes beginners make with Linked Lists and Data Structures"
1. "Provide advanced patterns and performance considerations for Linked Lists and Data Structures"

## Key Takeaways

- Master the core ideas of Linked Lists and Data Structures through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked cppreference docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
