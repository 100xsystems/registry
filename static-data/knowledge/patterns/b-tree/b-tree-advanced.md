---
title: "Advanced B-Trees: Concurrency and Variants"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Explain concurrency on B-trees"
  - "Describe the B-link variant"
  - "Understand crash safety (WAL + page checksums)"
  - "Compare with LSM-trees deeply"
prerequisites:
  []
knowledge_refs:
  - "patterns/b-tree"
---

# Advanced B-Trees: Concurrency and Variants

## Concurrency

Concurrent inserts into a B-tree split nodes, and a reader mid-traversal must not see a torn state. Databases use latches (short-lived page locks), optimistic latch coupling, and B-link trees where each node points to its right sibling so a split never loses a reader.

```text
Concurrency techniques on B-trees:
  - Latch coupling: hold a node latch while acquiring the child
  - B-link: each node links to its right sibling; a reader that
    finds a split mid-traversal follows the link instead of restarting
  - Copy-on-write B-trees (LMDB style): readers see a consistent snapshot
Crash safety:
  - WAL: redo records make page changes durable and replayable
  - Page checksums: detect torn pages from partial writes
```

## B-Tree vs LSM

B-trees optimize reads (in-place, sorted, compact); LSM-trees optimize writes (append-only, batched compaction) at the cost of read amplification and space. Read-heavy OLTP prefers B-trees; write-heavy ingest prefers LSMs. Many modern stores (RocksDB) are LSM; most classic RDBMS are B-tree.

## Practice: Compare the Engines

A metrics-ingestion workload writes 100k rows/s and reads recent values.

**Task 1:** Model the write cost of a B-tree (random page writes, splits) vs an LSM (sequential appends).

**Task 2:** Model the read cost of the LSM (multi-level lookups) vs the B-tree (log n).

**Task 3:** Pick an engine and justify with the workload's write/read ratio.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why B-link trees keep readers safe during splits.

**Prompt 2 — Implementation Design:**
> Design a storage engine that serves hot recent data from an LSM and archive data from a B-tree. How do queries route?

**Prompt 3 — Boundary Testing:**
> A crash mid-split corrupts the tree. Design the WAL + recovery path that reconstructs the invariant.

## Key Takeaways

- Latches and B-links keep concurrent traversals safe
- WAL and checksums make page writes crash-safe
- B-trees read-optimized, LSM write-optimized
- Hybrid engines route by data age

## Further Reading

- [B-Link Trees — Paper](https://www.cs.cornell.edu/courses/cs4410/2016fa/slides/lecture17.pdf)
- [The Design and Implementation of InnoDB](https://dev.mysql.com/doc/refman/8.0/en/innodb-architecture.html)
