---
title: "Advanced Iterator: Internal Iteration and Parallel Traversal"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Distinguish external vs internal iteration"
  - "Parallelize iteration safely"
  - "Design iterator adapters"
  - "Reason about iterator complexity"
prerequisites:
  []
knowledge_refs:
  - "patterns/iterator"
---

# Advanced Iterator: Internal Iteration and Parallel Traversal

## External vs Internal

External iteration is caller-driven: next(), with the loop in the caller. Internal iteration is structure-driven: for_each/map, with the loop inside the collection. Internal iteration lets the collection control order, concurrency, and short-circuiting; Rust iterators and Java streams are internal with lazy adapters.

```rust
// Rust: lazy internal iteration, parallelizable with rayon
let nums: Vec<i64> = (0..1_000_000).collect();

let sum_of_squares: i64 = nums.iter()      // lazy chain
    .map(|n| n * n)
    .filter(|sq| sq % 2 == 0)
    .take(100)
    .sum();

// Parallel: same pipeline, data-parallel execution
use rayon::prelude::*;
let par_sum: i64 = nums.par_iter()
    .map(|n| n * n)
    .sum();
// The iterator abstracts both the layout AND the execution model.
```

## Parallelism and Adapters

Parallel iterators split the source, fan out, and merge — but the merge must respect ordering or document its absence. Adapters (map, filter, flat_map, take, zip) are lazy and fusion-optimizable: a compiler or runtime can collapse chains into a single pass, which is why iterator pipelines are both expressive and fast.

## Practice: Parallelize the Pipeline

A 10M-row transformation pipeline (parse, validate, enrich, aggregate) is single-threaded.

**Task 1:** Convert to a parallel iterator and measure speedup at 4 and 8 cores.

**Task 2:** Identify the order-sensitive stage and enforce ordering at the merge.

**Task 3:** Benchmark fusion: one pass vs intermediate allocations.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain the difference between caller-driven and structure-driven iteration and why the latter enables parallelism.

**Prompt 2 — Implementation Design:**
> Design a streaming ETL as iterator adapters with a bounded buffer. Where does backpressure live?

**Prompt 3 — Boundary Testing:**
> A parallel merge reorders output. Design the ordering guarantee or the documented contract when it is dropped.

## Key Takeaways

- Internal iteration moves control into the collection
- Parallel iterators split, compute, and merge
- Adapters compose lazily and fuse into one pass
- Ordering at the merge is an explicit contract

## Further Reading

- [Rust — Iterator trait](https://doc.rust-lang.org/std/iter/trait.Iterator.html)
- [Rayon — data parallelism](https://docs.rs/rayon/latest/rayon/)
