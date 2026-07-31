---
title: "MapReduce in Production: Hadoop and SQL Engines"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Describe Hadoop job execution"
  - "Recognize SQL compiles to map-reduce"
  - "Handle skew"
  - "Design combiners"
prerequisites:
  []
knowledge_refs:
  - "patterns/mapreduce"
---

# MapReduce in Production: Hadoop and SQL Engines

## From SQL to MapReduce

GROUP BY, COUNT, and JOIN compile to map-reduce shapes: Hive translates SQL to MR jobs; modern engines (Spark, Trino) do the same in memory. The map side pushes filters and projections; the reduce side aggregates per group. Understanding the shape lets you predict job behavior from a query.

```sql
-- This SQL compiles to a map-reduce job:
SELECT status, COUNT(*) AS cnt
FROM orders
WHERE created_at > '2026-01-01'
GROUP BY status;

-- Map phase:  for each row -> emit (status, 1), after the WHERE filter
-- Shuffle:    group all (status, 1) pairs by status
-- Reduce:     sum the counts per status
-- A JOIN compiles to a map-side emit per side + a reduce-side merge,
-- or a broadcast join when one side is small.
```

## Combiners and Skew

A combiner is a mini-reduce on the map side, shrinking the shuffle volume (sum partial counts before shipping). Skew is the killer: one key dominates (a hot word, a famous user), overloading one reducer. Salting splits hot keys across reducers, then a final pass merges.

## Practice: Tune the Job

A daily aggregation of 10B events has one hot key with 60% of the data.

**Task 1:** Add the combiner and measure shuffle bytes before/after.

**Task 2:** Design the salt-and-merge for the hot key.

**Task 3:** Predict: which phase is the bottleneck and what parallelism fixes it?

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why a combiner shrinks shuffle and why skew breaks one reducer. Ask me to trace a hot key.

**Prompt 2 — Implementation Design:**
> Design a daily recommendation aggregation with a hot user. Show the salting plan and the final merge.

**Prompt 3 — Boundary Testing:**
> A reducer task fails twice and must retry. Design the determinism that makes the retry identical.

## Key Takeaways

- SQL GROUP BY/JOIN compile to map-reduce shapes
- Combiners shrink shuffle traffic
- Key skew overloads single reducers
- Salt-and-merge tames hot keys

## Further Reading

- [Hadoop MapReduce tutorial](https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)
