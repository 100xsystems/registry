---
slug: amazon-shopping-cart
title: "Amazon Shopping Cart"
description: "How Amazon handles flash sales, DynamoDB, and Prime Day traffic spikes with microservices and chaos engineering."
order: 7
tags:
  - case-study
  - e-commerce
  - dynamodb
  - flash-sales
  - microservices
prerequisites: []
references:
  - title: "How Amazon DynamoDB Supported ZOZOTOWN's Shopping Cart Migration"
    author: "AWS"
    url: "https://aws.amazon.com/blogs/database/how-amazon-dynamodb-supported-zozotowns-shopping-cart-migration-project/"
    type: "article"
    description: "Real-world DynamoDB migration for shopping cart workloads."
  - title: "AWS Services Scale to New Heights for Prime Day 2025"
    author: "AWS"
    url: "https://aws.amazon.com/blogs/aws/aws-services-scale-to-new-heights-for-prime-day-2025-key-metrics-and-milestones/"
    type: "article"
    description: "Key metrics and infrastructure scale during Prime Day."
  - title: "How AWS Powered Prime Day 2024"
    author: "AWS"
    url: "https://aws.amazon.com/blogs/aws/how-aws-powered-prime-day-2024-for-record-breaking-sales/"
    type: "article"
    description: "Record-breaking sales infrastructure analysis."
  - title: "Amazon Dynamo Architecture"
    author: "System Design One"
    url: "https://newsletter.systemdesign.one/p/amazon-dynamo-architecture"
    type: "article"
    description: "Technical deep dive into Dynamo's architecture."
  - title: "Can Amazon Handle Four Days of Prime Day Traffic?"
    author: "Grokking Tech Career"
    url: "https://grokkingtechcareer.substack.com/p/can-amazon-handle-four-days-of-prime"
    type: "article"
    description: "Analysis of Amazon's capacity planning and resilience."
related_knowledge:
  - slug: case-studies-uber-ride-matching
    title: "Uber Ride Matching"
    lesson_number: 9
  - slug: case-studies-netflix-streaming
    title: "Netflix Video Streaming"
    lesson_number: 5
knowledge_refs:
  - slug: "databases-dynamodb"
    title: "DynamoDB"
  - slug: "patterns-saga"
    title: "Saga Pattern"
  - slug: "patterns-circuit-breaker-pattern"
    title: "Circuit Breaker"
---

# Amazon Shopping Cart

Amazon's shopping cart and checkout system is one of the most mature distributed systems in the world, born from the very invention of DynamoDB and refined through decades of Prime Day stress tests.

## The Scale

- **Hundreds of thousands** of requests per second
- **Millions of orders per minute** during peak events
- **166 million messages/second** peak on SQS
- **Trillions** of Lambda invocations during Prime Day
- **99.999% availability** target

## The Shopping Cart Architecture

### Microservices Isolation
The cart is completely decoupled from product catalog, user profile, and payment:
- Each microservice owns its domain data exclusively
- Asynchronous processing via Kinesis and SQS
- Background workers handle inventory checks, reservation, session updates

### DynamoDB: Born from Necessity
Amazon discovered relational databases couldn't scale for cart workloads (70% simple key-value lookups). This led to **DynamoDB**:
- **Consistent hashing** for automatic partitioning
- **Single-digit millisecond latency** for cart operations
- **DAX (DynamoDB Accelerator):** In-memory write-through cache for hot keys

### Handling Flash Sales

**Shock absorbers:**
- Purchase intents funneled through status management tables and Kinesis streams
- Asynchronous processing prevents thread exhaustion

**Idempotency:**
- Conditional write expressions prevent duplicate cart additions
- Every request carries a unique idempotency token

**Graceful degradation:**
- Non-critical services (personalization, recommendations) shed or served from cache during spikes

## Payment Processing Pipeline

### Distributed Transactions with Sagas
Two-phase commits don't scale at Amazon's level. Instead:
- Asynchronous messaging between services
- Compensating transactions for rollback
- State machine trackers for orchestration
- Eventual consistency across inventory, payment, invoicing, fulfillment

### Idempotent API Design
Every payment request carries a unique token — network retries never double-charge.

## Inventory Management

### Optimistic Concurrency Control
- Items provisionally reserved with TTL expiration
- If checkout isn't completed within the window, stock returns to pool
- Dedicated inventory microservices with granular partition keys per SKU

## Prime Day: The Ultimate Stress Test

### Pre-scaling
- Historical data and predictive scaling pre-warm load balancers, databases, and CloudFront
- Custom silicon (Graviton, Trainium, Inferentia) for cost-efficient compute

### Chaos Engineering
Months before Prime Day:
- **AWS Fault Injection Service** randomly kills availability zones
- Injects network latency
- Simulates 4x normal traffic loads
- Validates self-healing capabilities

## Key Design Decisions

1. **DynamoDB was invented for this problem** — simple key-value at massive scale
2. **Sagas over 2PC** for distributed transactions at scale
3. **Idempotency everywhere** — network failures are guaranteed at scale
4. **Chaos engineering before major events** — don't wait for production failures

## Lessons Learned

- **Simple data models scale better** — 70% of cart operations are key-value lookups
- **Asynchronous processing** is essential for handling traffic spikes
- **Idempotency is non-negotiable** in payment systems
- **Chaos engineering builds confidence** — Prime Day success is earned months in advance

---

*References:*
1. AWS, "How DynamoDB Supported ZOZOTOWN's Shopping Cart." [Link](https://aws.amazon.com/blogs/database/how-amazon-dynamodb-supported-zozotowns-shopping-cart-migration-project/)
2. AWS, "Prime Day 2025 Key Metrics." [Link](https://aws.amazon.com/blogs/aws/aws-services-scale-to-new-heights-for-prime-day-2025-key-metrics-and-milestones/)
3. AWS, "How AWS Powered Prime Day 2024." [Link](https://aws.amazon.com/blogs/aws/how-aws-powered-prime-day-2024-for-record-breaking-sales/)
4. System Design One, "Amazon Dynamo Architecture." [Link](https://newsletter.systemdesign.one/p/amazon-dynamo-architecture)
5. Grokking Tech Career, "Can Amazon Handle Four Days of Prime Day Traffic?" [Link](https://grokkingtechcareer.substack.com/p/can-amazon-handle-four-days-of-prime)
