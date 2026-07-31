---
title: "MapReduce: Parallelize Batch by Divide and Conquer"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the map-reduce model"
  - "Describe shuffle and group"
  - "Identify map-reduce workloads"
  - "Write a word-count job"
prerequisites:
  - "patterns/iterator"
  - "principles/fail-fast"
knowledge_refs:
  - "patterns/mapreduce"
---

# MapReduce: Parallelize Batch by Divide and Conquer

## The Model

MapReduce runs in three phases: map (each input record produces key-value pairs, in parallel), shuffle (pairs are grouped by key and routed), and reduce (each group is processed by one reduce task, in parallel). The framework hides distribution, failure, and scheduling — the programmer writes two pure functions.

```python
# Word count: the canonical MapReduce
def map_fn(line):
    for word in line.split():
        yield (word.lower(), 1)

def reduce_fn(word, counts):
    yield (word, sum(counts))

# Framework: partition -> shuffle by key -> group -> reduce per key
def run_mapreduce(lines, n_reducers):
    mapped = []
    for line in lines:                       # map phase, parallelizable
        mapped.extend(map_fn(line))
    groups = {}
    for key, val in mapped:                  # shuffle + group by hash
        groups.setdefault(hash(key) % n_reducers, []).append((key, val))
    return {k: v for g in groups.values()
            for k, v in reduce_fn(g[0][0], (v for _, v in g))}
```

## Why Map and Reduce Are Pure

Map and reduce functions must be pure — no shared state, deterministic output — because the framework may retry any task on another node. Purity is what makes failure recovery trivial: re-run the task. Side effects and hidden orderings are the classic MapReduce bugs.

## Practice: Count the Log Lines

A 100GB log must be summarized by error type across 20 machines.

**Task 1:** Define map (extract type) and reduce (count) functions.

**Task 2:** Design the partitioning so counts are correct regardless of retries.

**Task 3:** Identify the phase that must be pure and why.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why pure functions make retries safe. Start with a crashed task.

**Prompt 2 — Compare & Contrast:**
> Compare MapReduce with streaming (Kafka) and with SQL GROUP BY. When is batch the right tool?

**Prompt 3 — Boundary Testing:**
> A reduce task sees keys in different order after a retry. Design the deterministic grouping that keeps output identical.

## Key Takeaways

- Map + shuffle + reduce parallelizes batch data
- Pure functions make failure recovery trivial
- The framework hides distribution and scheduling
- Determinism across retries is mandatory

## Further Reading

- [MapReduce — the paper](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf)
- [MapReduce — Wikipedia](https://en.wikipedia.org/wiki/MapReduce)
