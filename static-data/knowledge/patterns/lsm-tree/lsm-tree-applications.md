---
title: "LSM in Production: RocksDB, Cassandra, and LevelDB"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Tune memtable size and flush"
  - "Choose leveled vs size-tiered compaction"
  - "Use bloom filters to cut reads"
  - "Configure write stalls"
prerequisites:
  []
knowledge_refs:
  - "patterns/lsm-tree"
---

# LSM in Production: RocksDB, Cassandra, and LevelDB

## The Tuning Knobs

RocksDB exposes every trade: memtable size (bigger = fewer flushes, more memory), write buffer count, compaction style, bloom filter bits per key, and soft/hard write stall limits. Cassandra defaults to size-tiered and uses bloom filters per SSTable so point reads skip files entirely.

```text
Key LSM tuning decisions:
  - write_buffer_size: bigger memtable = fewer flushes = longer
    recovery after crash (memtable is replayed from the WAL)
  - max_write_buffer_number: more buffers = absorb write bursts,
    but each is memory
  - compaction_style: level vs size-tiered
  - bloom filter bits_per_key: ~10 bits = ~1% false positives;
    point reads skip non-matching SSTables entirely
  - soft_pending_compaction_bytes / hard: stall writes when
    compaction lags, trading throughput for stability
```

## Write Path and WAL

A write is ack'd after the WAL (write-ahead log) is durable, then applied to the memtable — so a crash only costs memtable contents since the last flush. WAL is sequential append; group commit batches fsyncs to amortize the cost. The read path leans on bloom filters and block caches.

## Practice: Tune for the Workload

A telemetry ingest: 200k writes/s, occasional point reads, 8GB memory budget.

**Task 1:** Size the memtable and write buffers for the burst profile.

**Task 2:** Choose compaction style and bloom filter size for the read ratio.

**Task 3:** Set the stall thresholds and simulate a compaction lag.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me the WAL role: why a crash loses only the memtable and how group commit helps.

**Prompt 2 — Implementation Design:**
> Design an LSM-backed time-series store: how are timestamps ordered, and how do range reads exploit the sort?

**Prompt 3 — Boundary Testing:**
> Compaction storms starve reads on a busy box. Design the IO budget (rate limiting compaction) that protects the read path.

## Key Takeaways

- Memtable, buffers, and compaction are the tunables
- Bloom filters make point reads skip files
- WAL durability + group commit define the write cost
- Write stalls protect stability when compaction lags

## Further Reading

- [RocksDB — Tuning Guide](https://github.com/facebook/rocksdb/wiki/RocksDB-Tuning-Guide)
- [Cassandra — Compaction](https://cassandra.apache.org/doc/stable/cassandra/operating/compaction/index.html)
