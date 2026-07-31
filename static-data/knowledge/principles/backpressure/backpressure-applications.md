---
title: "Backpressure in Real Systems"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Compare backpressure approaches across Kafka, gRPC, and HTTP/2"
  - "Explain consumer lag and its relationship to backpressure"
  - "Design a rate-aware consumer that protects its own resources"
  - "Apply backpressure to database write paths"
prerequisites:
  - "principles/backpressure/backpressure-fundamentals"
knowledge_refs:
  - "principles/backpressure"
---

# Backpressure in Real Systems

## Kafka: Poll-Based, Not Pushed

Kafka consumers pull batches with fetch requests, which gives natural backpressure: a consumer fetches only what it can process. The risk shifts to consumer lag — the distance between the committed offset and the head of the log.

When a consumer cannot keep up, lag grows. Monitoring lag is how teams detect backpressure problems before memory or disk fails.

```text
# Track lag per partition — the canonical backpressure metric
# lag = latest_offset - committed_offset
kafka-consumer-groups.sh --describe --group orders
# GROUP   TOPIC   PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG
# orders  events  0          1024            2048            1024
```

## HTTP/2 Flow Control

HTTP/2 provides per-stream flow control using WINDOW_UPDATE frames. A receiver announces how many bytes it can accept per stream and per connection, letting an overwhelmed server throttle a chatty client.

gRPC builds on HTTP/2 and inherits this: a server that is slow to respond naturally exerts backpressure on the client through the flow-control window.

## Practice: Consumer Lag Analysis

You operate a Kafka pipeline where consumer lag spikes every night during batch jobs.

**Task 1:** Describe the metrics you would collect to distinguish a slow consumer from an over-producing producer.

**Task 2:** Propose three mitigations: scale out, batch larger, or add a dead-letter path. When is each correct?

**Task 3:** Design an alert that fires 30 minutes before lag causes data loss, with a clear runbook action.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Walk me through what happens when a Kafka consumer processes a message that triggers a slow external API call. Where is the backpressure, and where is it missing?

**Prompt 2 — Compare & Contrast:**
> Contrast consumer lag in Kafka with TCP receive-window pressure. What is analogous to a zero window in Kafka?

**Prompt 3 — Boundary Testing:**
> A consumer crashes and restarts with a stale offset. It must reprocess 2M messages. How does this interact with backpressure? Design a replay that does not OOM.

## Key Takeaways

- Kafka uses pull-based consumption, making lag the key backpressure signal
- HTTP/2 flow control gives gRPC real backpressure semantics
- Always monitor consumer lag, not just throughput
- Batch size tuning is the cheapest backpressure lever

## Further Reading

- [Kafka Consumer Configuration](https://kafka.apache.org/documentation/#consumerconfigs)
- [HTTP/2 Flow Control (RFC 9113)](https://www.rfc-editor.org/rfc/rfc9113.html#name-flow-control)
