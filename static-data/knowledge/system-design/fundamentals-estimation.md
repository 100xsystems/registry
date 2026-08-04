---
slug: fundamentals-estimation
title: "Back-of-the-Envelope Estimation"
description: "Quick estimation techniques for QPS, storage, bandwidth, and compute requirements during system design."
order: 4
tags:
  - system-design
  - fundamentals
  - estimation
  - capacity-planning
  - back-of-envelope
prerequisites:
  - fundamentals-scalability
references:
  - title: "Back-of-the-Envelope Estimation"
    author: "ByteByteGo"
    url: "https://bytebytego.com/courses/system-design-interview/back-of-the-envelope-estimation"
    type: "course"
    description: "Comprehensive estimation course with examples."
  - title: "Capacity Estimation Worksheet"
    author: "Design Gurus"
    url: "https://designgurus.substack.com/p/the-5-step-capacity-estimation-worksheet"
    type: "article"
    description: "5-step worksheet for capacity estimation."
  - title: "System Design Interview Fundamentals: Mastering Estimation"
    author: "Hello Interview"
    url: "https://www.hellointerview.com/blog/mastering-estimation"
    type: "article"
    description: "Practical estimation fundamentals for interviews."
  - title: "Back of the Envelope"
    author: "System Design One"
    url: "https://systemdesign.one/back-of-the-envelope/"
    type: "article"
    description: "Deep dive on capacity planning formulas."
  - title: "System Design Estimation (Part 1)"
    author: "Karn Prem"
    url: "https://medium.com/@karnprem/system-design-estimation-part-1-30b92cbb42cc"
    type: "article"
    description: "Core formulas for system design estimation."
related_knowledge:
  - slug: fundamentals-scalability
    title: "Scalability & Performance"
    lesson_number: 2
  - slug: building-blocks-databases
    title: "Databases"
    lesson_number: 9
  - slug: interview-framework
    title: "The 4-Step Framework"
    lesson_number: 14
knowledge_refs:
  - slug: "databases-redis"
    title: "Redis"
  - slug: "tools-aws"
    title: "AWS"
  - slug: "patterns-caching"
    title: "Caching"
---

# Back-of-the-Envelope Estimation

Quick estimation is essential for system design — it prevents you from building systems that are either wildly over-provisioned or woefully under-capacity. These techniques help you make informed decisions in minutes.

## Key Numbers to Memorize

### Latency (Jeff Dean's Numbers)
| Operation | Latency |
|---|---|
| L1 cache reference | 0.5 ns |
| L2 cache reference | 7 ns |
| Main memory reference | 100 ns |
| SSD random read (4KB) | 150 μs |
| SSD sequential read (1MB) | 1 ms |
| HDD seek | 10 ms |
| HDD sequential read (1MB) | 30 ms |
| Same-datacenter round trip | 0.5 ms |
| Cross-continent round trip | 150 ms |

### Storage Reference
| Object | Size |
|---|---|
| UTF-8 character | 1 byte |
| Integer/timestamp | 4-8 bytes |
| Tweet/message | 200-500 bytes |
| Thumbnail image | 50-100 KB |
| High-res photo | 1-2 MB |
| 1-minute video (HD) | 50 MB |
| 2-hour movie | 1-4 GB |

### Availability Nines
| Availability | Downtime/Year |
|---|---|
| 99% | 3.65 days |
| 99.9% | 8.76 hours |
| 99.99% | 52.6 minutes |
| 99.999% | 5.26 minutes |

## Estimation Formulas

### QPS (Queries Per Second)

**Average QPS:**
```
QPS_avg = (DAU × Actions per User per Day) / 86,400
```

**Peak QPS:**
```
QPS_peak = QPS_avg × Multiplier
```

Multipliers:
- SaaS apps: 2x
- Consumer apps: 3-5x
- Flash sales: 10-100x

**Example:** Twitter has 200M DAU, each posts 2 tweets/day:
```
QPS_avg = (200M × 2) / 86,400 ≈ 4,630 QPS
QPS_peak = 4,630 × 3 ≈ 14,000 QPS
```

### Storage

**Total storage:**
```
Storage = Daily New Data × 365 × Retention Years × (1 + Replication Factor)
```

Add 20-30% for indexes and metadata.

**Example:** 1M new photos/day, 2MB each, 3-year retention, 3x replication:
```
Storage = 1M × 2MB × 365 × 3 × (1 + 3) × 1.25 ≈ 10.95 TB
```

### Bandwidth

**Bandwidth = QPS × Average Request/Response Size**

**Example:** 10,000 QPS, 5KB average response:
```
Bandwidth = 10,000 × 5KB = 50 MB/s = 400 Mbps
```

**Remember:** Storage is measured in bytes, network in bits. Multiply by 8 to convert.

### Compute

**Servers needed:**
```
Servers = (QPS_peak × Request Latency in seconds) / Target CPU Utilization
```

Target utilization: 70% (leave headroom for spikes).

**Example:** 10,000 QPS, 50ms latency, 70% utilization:
```
Servers = (10,000 × 0.05) / 0.7 ≈ 715 cores
```

## Estimation Framework

1. **Clarify requirements** — What are we estimating? For what time period?
2. **Make assumptions** — State your assumptions clearly
3. **Calculate baseline** — Use the formulas above
4. **Apply safety margin** — Add 2-3x for peak load
5. **Sanity check** — Does the result make sense?

## Common Pitfalls

- **Ignoring peak load** — Average QPS is not enough; plan for 3-5x peaks
- **Forgetting replication** — 3x replication means 3x storage
- **Confusing bytes and bits** — Network bandwidth is in bits, storage in bytes
- **Not accounting for growth** — Plan for 2-3 years ahead, not just today

---

*References:*
1. ByteByteGo, "Back-of-the-Envelope Estimation." [Link](https://bytebytego.com/courses/system-design-interview/back-of-the-envelope-estimation)
2. Design Gurus, "Capacity Estimation Worksheet." [Link](https://designgurus.substack.com/p/the-5-step-capacity-estimation-worksheet)
3. Hello Interview, "Mastering Estimation." [Link](https://www.hellointerview.com/blog/mastering-estimation)
4. System Design One, "Back of the Envelope." [Link](https://systemdesign.one/back-of-the-envelope/)
5. Karn Prem, "System Design Estimation (Part 1)." [Link](https://medium.com/@karnprem/system-design-estimation-part-1-30b92cbb42cc)
