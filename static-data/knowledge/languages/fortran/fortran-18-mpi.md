---
{
  "title": "MPI for Distributed Computing",
  "description": "Message passing for clusters.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Initialize MPI",
    "Rank and size basics",
    "Send and receive messages",
    "Use collective operations"
  ],
  "knowledge_refs": [
    "fortran/fortran-18-mpi"
  ],
  "prerequisites": [
    "Fortran-17: Parallel Programming with OpenMP"
  ],
  "references": [
    {
      "title": "Fortran 90/95 Standard",
      "url": "https://wg5-fortran.org/",
      "description": "The official standards committee"
    },
    {
      "title": "Fortran Best Practices",
      "url": "https://fortran-lang.org/en/learn/",
      "description": "fortran-lang.org learning resources"
    },
    {
      "title": "Modern Fortran Explained",
      "url": "https://www.oxford.universitypressscholarship.com/",
      "description": "Metcalf, Reid & Cohen textbook"
    }
  ]
}
---

# FORTRAN-18-MPI: MPI for Distributed Computing

## Introduction

Message passing for clusters. By the end of this lesson you will be able to: Initialize MPI; Rank and size basics; Send and receive messages; Use collective operations.

## Key Concepts

### 1. Initialize MPI

Target: Initialize MPI. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fortran
program mpi_hello
  use mpi
  implicit none
  integer :: ierr, rank, size
  call MPI_INIT(ierr)
  call MPI_COMM_RANK(MPI_COMM_WORLD, rank, ierr)
  call MPI_COMM_SIZE(MPI_COMM_WORLD, size, ierr)
  print *, "rank", rank, "of", size
  call MPI_FINALIZE(ierr)
end program mpi_hello
```
### 2. Rank and size basics

Target: Rank and size basics. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fortran
call MPI_SEND(data, n, MPI_DOUBLE_PRECISION, 1, 0, MPI_COMM_WORLD, ierr)
```
### 3. Send and receive messages

Target: Send and receive messages. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fortran
call MPI_RECV(data, n, MPI_DOUBLE_PRECISION, 0, 0, MPI_COMM_WORLD, status, ierr)
```
### 4. Use collective operations

Target: Use collective operations. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fortran
call MPI_BARRIER(MPI_COMM_WORLD, ierr)
call MPI_BCAST(x, 1, MPI_INTEGER, 0, MPI_COMM_WORLD, ierr)
```

## Practice Questions

1. What is the key idea behind "MPI for Distributed Computing"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain MPI for Distributed Computing with analogies and real-world examples"
1. "Show me common mistakes beginners make with MPI for Distributed Computing"
1. "Provide advanced patterns and performance considerations for MPI for Distributed Computing"

## Key Takeaways

- Master the core ideas of MPI for Distributed Computing through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
