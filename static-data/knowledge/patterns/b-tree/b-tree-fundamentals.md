---
title: "B-Trees: The Database Index Workhorse"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the B-tree structure"
  - "Understand the branching factor"
  - "Trace a lookup, insert, and split"
  - "Explain why B-trees beat binary trees on disk"
prerequisites:
  - "patterns/hash-index"
  - "principles/caching"
knowledge_refs:
  - "patterns/b-tree"
---

# B-Trees: The Database Index Workhorse

## The Structure

A B-tree is a balanced multi-way tree: every node holds up to B keys, every internal node has up to B+1 children, and all leaves sit at the same depth. The branching factor (B, often hundreds) keeps the tree short — a 4-level B-tree can index billions of keys.

On disk, each node is one page read. A binary tree would need ~30 disk reads to find a key among a billion; a B-tree needs ~4. That is the entire reason databases use B-trees.

```text
B-tree shape (branching factor 4, leaves at same depth):
            [  17 |  52 ]
           /     |      \
    [3|9|11]  [23|31|41]  [61|77|83]
      |   |      |   |       |   |
     leaf leaf  leaf leaf   leaf leaf

Lookup: 3-4 page reads for billions of keys (vs ~30 for binary).
```

## Ordered and Range-Friendly

Because keys stay sorted, B-trees support range scans (WHERE id BETWEEN 10 AND 20), ordered iteration, and prefix matching — things hash indexes cannot do. This is why B-trees are the default index for most databases.

## Practice: Trace the Operations

A B-tree with branching factor 3 stores integers. Insert 25 into a full leaf [20, 23, 27].

**Task 1:** Trace the split: which key promotes to the parent, and how the leaf divides?

**Task 2:** Trace a range scan [23, 41] through the tree — which nodes are visited?

**Task 3:** Estimate the tree height for 1 billion keys at branching factor 200 and justify the disk reads.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why branching factor matters more than tree cleverness on disk. Start with page reads.

**Prompt 2 — Compare & Contrast:**
> Compare B-trees with LSM-trees for write-heavy vs read-heavy workloads. When is each the right choice?

**Prompt 3 — Boundary Testing:**
> A B-tree index becomes fragmented with random inserts. Design the page-fill heuristics (like the 2/3 fill rule) that delay splits.

## Key Takeaways

- B-trees are balanced, multi-way, disk-aware trees
- Branching factor keeps height logarithmic in page reads
- Sorted keys enable range scans and prefixes
- One node = one page read is the design constraint

## Further Reading

- [B-Tree — Wikipedia](https://en.wikipedia.org/wiki/B-tree)
- [Use The Index, Luke!](https://use-the-index-luke.com/)
