---
title: "LSM Trees: Writes First, Compaction Later"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the LSM structure"
  - "Describe memtable, SSTable, compaction"
  - "Understand write amplification"
  - "Know the read cost"
prerequisites:
  - "patterns/b-tree"
  - "patterns/bloom-filter"
knowledge_refs:
  - "patterns/lsm-tree"
---

# LSM Trees: Writes First, Compaction Later

## The Structure

An LSM tree keeps writes in an in-memory memtable, flushes it to immutable sorted files (SSTables), and merges files in the background. Because writes only append, they are sequential — fast on HDD and SSD. The cost moves to reads: a key may live in several files, so reads check memtable then files, newest first.

```python
# LSM essentials: memtable -> flush -> merge
class Memtable:
    def __init__(self):
        self.data = {}          # sorted structure in practice (skip list)

    def put(self, key, value):
        self.data[key] = value

    def flush(self):            # write as a sorted immutable SSTable
        sstable = SSTable(sorted(self.data.items()))
        self.data = {}
        return sstable

class LSMTree:
    def __init__(self):
        self.mem = Memtable()
        self.levels = [[]]      # level 0 newest; deeper = older/merged

    def put(self, key, value):
        self.mem.put(key, value)
        if len(self.mem.data) > 4096:     # flush on size trigger
            self.levels[0].append(self.mem.flush())

    def get(self, key):
        if key in self.mem.data: return self.mem.data[key]
        for level in self.levels:          # newest files first
            for sst in reversed(level):
                if sst.bloom.might_contain(key):
                    v = sst.get(key)
                    if v is not None: return v
        return None
```

## Compaction

Compaction merges overlapping SSTables into sorted runs and drops dead versions, reclaiming space and bounding the read amplification. Leveled compaction (RocksDB default) keeps files in strict levels for predictable reads but pays on every merge; size-tiered (Cassandra) merges similar-size runs, cheaper writes, messier reads.

## Practice: Trace the Lifecycle

A key is written, updated twice, and read — trace it through memtable and files.

**Task 1:** Trace the three versions of the key through flush and compaction.

**Task 2:** Count the files a read must check with no compaction vs after.

**Task 3:** Measure write amplification: bytes written to disk per byte of user data.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why appending beats in-place update on disk. Start with random vs sequential IO.

**Prompt 2 — Compare & Contrast:**
> Compare LSM with B-trees: write cost, read cost, space, and when each wins.

**Prompt 3 — Boundary Testing:**
> Compaction falls behind and files pile up. Design the backpressure that slows writes before space runs out.

## Key Takeaways

- LSM turns random writes into sequential appends
- Memtable + SSTables + background compaction
- Reads pay for the write win (amplification)
- Compaction strategy shapes the trade-offs

## Further Reading

- [The Log-Structured Merge-Tree — the paper](https://www.cs.umb.edu/~poneil/lsm.pdf)
- [RocksDB — wiki](https://github.com/facebook/rocksdb/wiki)
