---
title: "Advanced LSM: Merge Policies and Range Reads"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Compare leveled and size-tiered deeply"
  - "Design range read merging"
  - "Exploit LSM for time-ordered data"
  - "Analyze amplification costs"
prerequisites:
  []
knowledge_refs:
  - "patterns/lsm-tree"
---

# Advanced LSM: Merge Policies and Range Reads

## Leveled vs Size-Tiered

Leveled compaction keeps one sorted run per level with exponentially growing sizes; reads touch at most one file per level — predictable. Size-tiered merges runs of similar size; writes are cheaper but a read may scan many files. Cassandra and HBase differ exactly here, and the choice is workload-shaped.

```text
Compaction styles compared:
  Leveled (RocksDB default):
    - each level has one sorted run; reads hit <= one file/level
    - write amplification higher (every write merged many times)
    - predictable read latency, compact space
  Size-tiered (Cassandra default):
    - merge runs of similar size; fewer merges -> lower write amp
    - reads may scan many overlapping files
    - better for write-heavy, read-light, or time-series
  Time-series twist: range-merge on time-ordered keys, compact old
  runs rarely — hot recent data compact, cold history untouched
```

## Range Reads and Time-Series

Range reads merge across files like a k-way merge, streaming rows in order. Time-series workloads shine: writes are time-ordered appends, hot recent data lives in the memtable and first files, and old history stays compacted and rarely touched — LSM is the natural shape for metrics and logs.

## Practice: Design the Merge Strategy

A metrics store ingests 1M points/s, keeps 90 days, reads last-hour ranges heavily.

**Task 1:** Choose the compaction style for the hot-recent/cold-history split.

**Task 2:** Design the range read that merges memtable + recent files + compacted history.

**Task 3:** Compute write and read amplification for the chosen layout.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain the write-amplification vs read-predictability trade between the two compaction styles.

**Prompt 2 — Implementation Design:**
> Design a log store: partition by time, LSM per partition, and the retention compaction that drops old partitions.

**Prompt 3 — Boundary Testing:**
> A time-series key skews: one hot series grows the level 0 files. Design the split or priority that isolates the hot series.

## Key Takeaways

- Leveled: predictable reads, higher write amplification
- Size-tiered: cheaper writes, messy reads
- Range reads are k-way merges across files
- Time-series is LSM's natural workload

## Further Reading

- [RocksDB — Compaction](https://github.com/facebook/rocksdb/wiki/Compaction)
- [HBase — compaction](https://hbase.apache.org/book.html#_compaction)
