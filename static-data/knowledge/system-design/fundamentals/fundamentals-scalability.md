---
slug: fundamentals-scalability
title: "Scalability & Performance"
description: "Understanding vertical vs horizontal scaling, performance metrics, and designing systems that grow with demand."
order: 2
tags:
  - system-design
  - fundamentals
  - scalability
  - performance
  - latency
  - throughput
prerequisites: []
references:
  - title: "System Design Interview – An Insider's Guide"
    author: "Alex Xu"
    url: "https://bytebytego.com/"
    type: "book"
    description: "Foundational text on system design with scalability as the core theme."
  - title: "Designing Data-Intensive Applications"
    author: "Martin Kleppmann"
    url: "https://dataintensive.net/"
    type: "book"
    description: "Definitive guide to distributed systems and data scalability."
  - title: "System Design Roadmap"
    author: "roadmap.sh"
    url: "https://roadmap.sh/system-design"
    type: "docs"
    description: "Visual roadmap covering scalability concepts step by step."
  - title: "High Scalability Blog"
    author: "Todd Hoff"
    url: "http://highscalability.com/"
    type: "blog"
    description: "Real-world architecture case studies and scaling strategies."
  - title: "The Art of Scalability"
    author: "Martin Abbott & Michael Fisher"
    url: "https://www.amazon.com/Art-Scalability-Scalable-Architecture-Processes/dp/0134037311"
    type: "book"
    description: "Comprehensive guide to scaling people, processes, and technology."
related_knowledge:
  - slug: fundamentals-availability
    title: "Availability & Reliability"
    lesson_number: 3
  - slug: fundamentals-estimation
    title: "Back-of-the-Envelope Estimation"
    lesson_number: 4
  - slug: building-blocks-load-balancers
    title: "Load Balancers"
    lesson_number: 5
knowledge_refs:
  - slug: "patterns-consistent-hashing"
    title: "Consistent Hashing"
  - slug: "patterns-circuit-breaker-pattern"
    title: "Circuit Breaker"
  - slug: "databases-redis"
    title: "Redis"
---

# Scalability & Performance

Scalability is the ability of a system to handle increased load by adding resources. Understanding when and how to scale is the foundation of system design.

## Vertical vs. Horizontal Scaling

### Vertical Scaling (Scale Up)
Adding more resources to a single machine:
- Upgrade CPU, RAM, or disk
- Simple to implement — no code changes
- Has physical limits (max server size)
- Single point of failure

**When to use:** Early-stage startups, databases that are hard to shard, workloads that require strong consistency.

### Horizontal Scaling (Scale Out)
Adding more machines to distribute load:
- Stateless application servers behind a load balancer
- Database sharding across multiple nodes
- No theoretical upper limit
- Requires distributed system design

**When to use:** High-traffic web applications, systems requiring high availability, workloads with predictable growth.

## Performance Metrics

### Latency
Time to process a single request:
- **p50 (median):** 50% of requests complete within this time
- **p95:** 95% of requests complete within this time
- **p99:** 99% of requests complete within this time
- **p999:** The "tail latency" that affects your most demanding users

**Why p99 matters more than average:** At scale, even 1% of slow requests affects millions of users. Google found that a 100ms latency increase decreased revenue by 1%.

### Throughput
Total work completed per unit time:
- **QPS (Queries Per Second):** How many requests your system handles
- **RPS (Requests Per Second):** Same concept, different terminology
- **Bandwidth:** Data transferred per second (bits/second)

### The Latency-Throughput Trade-off
Often, optimizing for one hurts the other:
- **Batch processing:** High throughput, high latency
- **Real-time processing:** Low latency, potentially lower throughput
- **Caching:** Low latency for reads, but adds complexity

## Common Bottlenecks

### Database Bottlenecks
- Too many reads hitting a single database
- Complex joins across large tables
- Write-heavy workloads overwhelming a single leader

**Solutions:** Read replicas, sharding, caching, connection pooling

### Application Bottlenecks
- Synchronous calls to external services
- CPU-intensive computations blocking request handling
- Memory pressure from large object allocations

**Solutions:** Async processing, connection pooling, horizontal scaling

### Network Bottlenecks
- Insufficient bandwidth for data transfer
- High latency between services
- DNS resolution delays

**Solutions:** CDN, connection keep-alive, geographic distribution

## Designing for Scalability

### Stateless Services
Keep no session state in application servers — store it in external stores (Redis, database). This enables any server to handle any request.

### Asynchronous Processing
Move slow operations to background queues:
- Email sending
- Image processing
- Report generation
- Analytics events

### Database Design
- **Normalize for writes, denormalize for reads**
- **Partition by access pattern** — shard by the most common query
- **Use indexes strategically** — they speed up reads but slow down writes

### Caching Strategy
Cache frequently accessed, rarely changing data:
- User profiles
- Product catalogs
- Configuration data
- API responses

## Key Numbers to Remember

| Metric | Value |
|---|---|
| L1 cache reference | 0.5 ns |
| L2 cache reference | 7 ns |
| Main memory reference | 100 ns |
| SSD random read (4KB) | 150 μs |
| HDD seek | 10 ms |
| Same-datacenter round trip | 0.5 ms |
| Cross-continent round trip | 150 ms |

---

*References:*
1. Alex Xu, *System Design Interview – An Insider's Guide.* [Link](https://bytebytego.com/)
2. Martin Kleppmann, *Designing Data-Intensive Applications.* [Link](https://dataintensive.net/)
3. roadmap.sh, "System Design Roadmap." [Link](https://roadmap.sh/system-design)
4. High Scalability Blog. [Link](http://highscalability.com/)
5. Martin Abbott & Michael Fisher, *The Art of Scalability.* [Link](https://www.amazon.com/Art-Scalability-Scalable-Architecture-Processes/dp/0134037311)
