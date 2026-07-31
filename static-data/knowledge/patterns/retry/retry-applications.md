---
title: "Retry in Production: SDKs, Queues, and Dead Letters"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Budget retries across services"
  - "Use delayed retry queues"
  - "Design dead-letter flows"
  - "Avoid retry storms"
prerequisites:
  []
knowledge_refs:
  - "patterns/retry"
---

# Retry in Production: SDKs, Queues, and Dead Letters

## Retry Budgets

Every service retrying its dependencies multiplies load: a single downstream failure fans out. A retry budget caps the retry rate (e.g., at most 10% of requests retried in a window); beyond it, fail fast. Budgets prevent a failing dependency from amplifying into a total outage.

```yaml
Retry budget example (rate-based):
  window: 30s
  max_retries_per_request: 3
  budget: 10% of requests may be retried in the window
  if budget exhausted: fail immediately (don't amplify the outage)

Delayed retry via queue:
  message fails -> publish to retry topic with delay (1m, 5m, 30m)
  -> consumer attempts again after the delay
  -> after N attempts -> dead-letter topic (human/automated repair)
Dead-letter handling:
  - inspect, fix the root cause, redeliver
  - or reject permanently and alert
  - monitor DLQ depth as an operational signal
```

## Queues and DLQs

Message queues retry naturally: a failed message redelivers. Delayed retries (RabbitMQ delays, SQS visibility timeout, Kafka via scheduled re-emit) space out attempts. A dead-letter queue isolates poison messages — ones that fail forever — so they stop consuming retry capacity and alert operators.

## Practice: Design the Retry Path

A webhook sender delivers 10k events/hour to partners; some partners are flaky.

**Task 1:** Design the per-partner retry policy with delays.

**Task 2:** Design the dead-letter flow and the manual re-delivery tool.

**Task 3:** Set the global retry budget so one flaky partner cannot starve the others.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why retry budgets exist: what a fan-out retry storm does to a failing dependency.

**Prompt 2 — Implementation Design:**
> Design a delayed retry pipeline with exponential delays and a DLQ. What are the delays, and who watches the DLQ?

**Prompt 3 — Boundary Testing:**
> A poison message loops for hours consuming retry capacity. Design the attempt cap and the DLQ promotion.

## Key Takeaways

- Retry budgets stop amplification
- Delayed queues space out attempts
- Dead-letter queues isolate poison messages
- DLQ depth is an operational alarm

## Further Reading

- [Retry — Google SRE workbook](https://sre.google/workbook/part-iv-practices/)
- [AWS SQS — visibility timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html)
