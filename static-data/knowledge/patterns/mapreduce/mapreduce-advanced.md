---
title: "Advanced MapReduce: Iterative and Incremental Jobs"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Express iterative algorithms"
  - "Design incremental updates"
  - "Avoid recomputing everything"
  - "Choose engine for the job"
prerequisites:
  []
knowledge_refs:
  - "patterns/mapreduce"
---

# Advanced MapReduce: Iterative and Incremental Jobs

## Iteration Is the Pain Point

PageRank and k-means iterate: each pass needs the previous output as input, and naive MapReduce re-reads and re-shuffles the entire dataset every iteration. Systems like Spark cache RDDs in memory to keep iteration fast, and Pregel (vertex-centric) specializes graph iteration. The lesson: know your iteration pattern before choosing the engine.

```scala
// Spark: cache keeps iterative algorithms fast
val links = sc.textFile("links.tsv")
    .map(parse).distinct().groupByKey().cache()   // cached across iters

var ranks = links.mapValues(_ => 1.0)
for (i <- 1 to 10) {                              // iterative loop
  val contribs = links.join(ranks).values.flatMap {
    case (urls, rank) => urls.map(url => (url, rank / urls.size))
  }
  ranks = contribs.reduceByKey(_ + _).mapValues(0.15 + 0.85 * _)
}
// Without the cache(), every iteration re-reads and re-shuffles
// the whole graph from disk.
```

## Incremental Aggregation

When inputs change by a fraction, full recompute is wasteful. Incremental pipelines (Lambda/Kappa) keep base aggregates and apply deltas; streaming stages (Kafka Streams, Flink) maintain rolling windows as the map-reduce shape runs continuously. Materialized views in warehouses do this declaratively.

## Practice: Iterate Without Recomputation

A PageRank job over a 10B-edge graph runs nightly and the edges change 2% per day.

**Task 1:** Design the cached iteration and count the bytes saved.

**Task 2:** Design the incremental delta path for the 2% change.

**Task 3:** Choose the engine (Spark vs Flink vs warehouse SQL) and justify with the update pattern.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why iteration without caching re-reads the world every pass.

**Prompt 2 — Implementation Design:**
> Design a streaming map-reduce for real-time per-user aggregations with exactly-once semantics. Where do the windows live?

**Prompt 3 — Boundary Testing:**
> A delta arrives out of order. Design the watermark or the idempotent apply that keeps the aggregate correct.

## Key Takeaways

- Iteration without caching is re-reading the world
- Engine choice follows the iteration pattern
- Deltas beat full recompute for slowly changing data
- Streaming runs the map-reduce shape continuously

## Further Reading

- [Spark — RDD programming guide](https://spark.apache.org/docs/latest/rdd-programming-guide.html)
- [Pregel — Google paper](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/37252.pdf)
