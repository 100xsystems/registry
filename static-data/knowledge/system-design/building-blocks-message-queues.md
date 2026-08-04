---
slug: building-blocks-message-queues
title: "Message Queues"
description: "Asynchronous communication between services — Kafka, RabbitMQ, SQS, and event-driven architecture."
order: 7
tags:
  - system-design
  - building-blocks
  - message-queues
  - kafka
  - event-driven
  - asynchronous
prerequisites:
  - fundamentals-scalability
references:
  - title: "Apache Kafka Documentation"
    author: "Apache"
    url: "https://kafka.apache.org/documentation/"
    type: "docs"
    description: "Official Kafka documentation."
  - title: "RabbitMQ Tutorials"
    author: "RabbitMQ"
    url: "https://www.rabbitmq.com/getstarted.html"
    type: "docs"
    description: "Official RabbitMQ tutorials and patterns."
  - title: "AWS SQS Documentation"
    author: "AWS"
    url: "https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html"
    type: "docs"
    description: "AWS Simple Queue Service documentation."
  - title: "System Design: Message Queue"
    author: "ByteByteGo"
    url: "https://blog.bytebytego.com/p/message-queue"
    type: "article"
    description: "Visual breakdown of message queue architecture."
  - title: "The Log: What every software engineer should know"
    author: "Jay Kreps"
    url: "https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying"
    type: "article"
    description: "Foundational article on event logs and streaming."
related_knowledge:
  - slug: building-blocks-databases
    title: "Databases"
    lesson_number: 8
  - slug: patterns-event-driven
    title: "Event-Driven Architecture"
    lesson_number: 11
  - slug: fundamentals-scalability
    title: "Scalability & Performance"
    lesson_number: 2
knowledge_refs:
  - slug: "tools-kafka"
    title: "Kafka"
  - slug: "tools-rabbitmq"
    title: "RabbitMQ"
  - slug: "patterns-pub-sub"
    title: "Pub/Sub"
---

# Message Queues

Message queues enable asynchronous communication between services, decoupling producers from consumers and providing resilience against traffic spikes.

## Why Message Queues?

### Synchronous vs Asynchronous

**Synchronous (without queue):**
```
User → Service A → Service B → Service C → Response
```
If Service C is slow, everything blocks.

**Asynchronous (with queue):**
```
User → Service A → Queue → Service B → Service C
                → Response (immediate)
```
Service A responds immediately. Service B processes when ready.

### Key Benefits
- **Decoupling:** Services don't need to know about each other
- **Buffering:** Absorbs traffic spikes without overwhelming consumers
- **Reliability:** Messages persist until processed
- **Scalability:** Add more consumers to increase throughput

## Queue Types

### Point-to-Point (Queue)
One message consumed by one consumer:
```
Producer → [Message] → Consumer 1
                    → Consumer 2 (different messages)
```
**Use case:** Task distribution, work queues.

### Publish-Subscribe (Topic)
One message broadcast to all subscribers:
```
Publisher → [Topic] → Subscriber 1
                   → Subscriber 2
                   → Subscriber 3
```
**Use case:** Event notifications, real-time feeds.

## Popular Message Queues

### Apache Kafka
Distributed event streaming platform:
- **High throughput:** Millions of messages/second
- **Durable:** Messages persisted to disk
- **Partitioned:** Horizontal scaling via partitions
- **Replayable:** Consumers can re-read from any offset

**Use case:** Event sourcing, log aggregation, real-time analytics.

### RabbitMQ
Traditional message broker with routing:
- **Flexible routing:** Direct, topic, fanout exchanges
- **ACK-based:** Messages acknowledged after processing
- **Lightweight:** Easier to set up than Kafka
- **Lower throughput:** Better for moderate volumes

**Use case:** Task queues, RPC, complex routing logic.

### AWS SQS
Fully managed message queue:
- **No infrastructure:** AWS handles everything
- **Standard queue:** Best-effort ordering, at-least-once delivery
- **FIFO queue:** Exactly-once processing, strict ordering
- **Auto-scaling:** Handles any volume

**Use case:** Decoupling AWS services, simple task queues.

## Message Processing Patterns

### At-Most-Once
Message delivered zero or one time:
- Fire and forget
- Risk of message loss
- Fastest processing

### At-Least-Once
Message delivered one or more times:
- Default for most systems
- Risk of duplicate processing
- Requires idempotent consumers

### Exactly-Once
Message delivered exactly one time:
- Hardest to achieve
- Requires transactional processing
- Kafka supports this with transactions

## Dead Letter Queues (DLQ)

When a message can't be processed after N retries, it moves to a DLQ:
```
Main Queue → Consumer (fails 3 times) → Dead Letter Queue
```
- Prevents poison messages from blocking the queue
- Allows manual inspection and reprocessing
- Essential for production reliability

---

*References:*
1. Apache, "Kafka Documentation." [Link](https://kafka.apache.org/documentation/)
2. RabbitMQ, "Tutorials." [Link](https://www.rabbitmq.com/getstarted.html)
3. AWS, "SQS Documentation." [Link](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
4. ByteByteGo, "System Design: Message Queue." [Link](https://blog.bytebytego.com/p/message-queue)
5. Jay Kreps, "The Log." [Link](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying)
