---
title: "Backpressure: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate flow-control concepts"
  - "Apply backpressure reasoning to new systems"
  - "Identify anti-patterns quickly"
prerequisites:
  - "principles/backpressure/backpressure-advanced"
knowledge_refs:
  - "principles/backpressure"
---

# Backpressure: Review & Mastery Quiz

## Quiz

Answer these questions, then check against the key takeaways below.

- Q1: A producer fills an unbounded queue. What is the first observable failure? (A: OOM / B: deadlock / C: 429s)
- Q2: Which mechanism gives a consumer the strongest control over producer speed? (A: bounded queue / B: pull demand / C: TCP window)
- Q3: In Kafka, what metric reveals a consumer falling behind? (A: fetch latency / B: consumer lag / C: record size)
- Q4: True or false: HTTP/2 flow control applies per connection, not per stream.
- Q5: A worker pool is at capacity and its queue is bounded. The gateway keeps sending. What should the gateway do? (A: buffer more / B: back off / C: drop silently)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A video-upload pipeline buffers 5GB of frames in memory because the encoder is slow. Rewrite the design so memory stays under 200MB without dropping frames.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "just make the queue bigger" is rarely the right fix, using a concrete system you know.

## Key Takeaways

- A: OOM; B: pull demand; C: consumer lag; Q4: false (per stream AND connection); Q5: back off
- Buffering hides problems — expose them as signals instead
- Backpressure is a contract between producer and consumer
