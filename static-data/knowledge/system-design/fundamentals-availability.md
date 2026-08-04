---
slug: fundamentals-availability
title: "Availability & Reliability"
description: "Understanding the nines of availability, failure modes, redundancy, and designing systems that stay online."
order: 3
tags:
  - system-design
  - fundamentals
  - availability
  - reliability
  - redundancy
  - fault-tolerance
prerequisites:
  - fundamentals-scalability
references:
  - title: "System Design Interview – An Insider's Guide"
    author: "Alex Xu"
    url: "https://bytebytego.com/"
    type: "book"
    description: "Covers availability concepts in the context of real system designs."
  - title: "Designing Data-Intensive Applications"
    author: "Martin Kleppmann"
    url: "https://dataintensive.net/"
    type: "book"
    description: "Deep dive into replication, fault tolerance, and consistency."
  - title: "Site Reliability Engineering"
    author: "Google (Beyer et al.)"
    url: "https://sre.google/sre-book/table-of-contents/"
    type: "book"
    description: "Google's approach to reliability engineering."
  - title: "The Log: What every software engineer should know"
    author: "Jay Kreps"
    url: "https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying"
    type: "article"
    description: "Foundational article on distributed system primitives."
  - title: "Chaos Engineering"
    author: "Casey Rosenthal et al. (O'Reilly)"
    url: "https://www.oreilly.com/library/view/chaos-engineering/9781492043850/"
    type: "book"
    description: "Building confidence in system behavior through controlled experiments."
related_knowledge:
  - slug: fundamentals-scalability
    title: "Scalability & Performance"
    lesson_number: 2
  - slug: patterns-circuit-breaker
    title: "Circuit Breaker & Resilience"
    lesson_number: 10
  - slug: building-blocks-databases
    title: "Databases"
    lesson_number: 9
knowledge_refs:
  - slug: "patterns-circuit-breaker-pattern"
    title: "Circuit Breaker"
  - slug: "patterns-bulkhead"
    title: "Bulkhead"
  - slug: "patterns-retry"
    title: "Retry Pattern"
---

# Availability & Reliability

Availability is the fraction of time a system is operational and accessible. Reliability is the probability that a system performs correctly over a given period. Together, they determine whether users can depend on your system.

## The Nines of Availability

| Availability | Downtime/Year | Downtime/Month | Description |
|---|---|---|---|
| 99% | 3.65 days | 7.31 hours | Two nines |
| 99.9% | 8.76 hours | 43.8 minutes | Three nines |
| 99.99% | 52.6 minutes | 4.38 minutes | Four nines |
| 99.999% | 5.26 minutes | 26.3 seconds | Five nines |

**Context:** Amazon loses ~$220,000 per minute of downtime. Google processes 8.5B searches/day — even 99.9% availability means 8.5M failed searches daily.

## Types of Failures

### Hardware Failures
- Server crashes, disk failures, network partitions
- At scale, hardware failures are **expected**, not exceptional
- Google reports ~1-2% of servers fail annually

### Software Failures
- Bugs, memory leaks, configuration errors
- Often more dangerous than hardware failures because they affect all instances simultaneously

### Network Failures
- Latency spikes, packet loss, complete partitions
- The CAP theorem forces trade-offs during network partitions

### Dependency Failures
- Third-party service outages
- Database failures
- DNS resolution failures

## Redundancy Strategies

### Active-Passive (Failover)
- Standby system takes over when primary fails
- Simple but wastes resources (standby sits idle)
- Risk of "failover gap" — time to detect and switch

### Active-Active
- Multiple systems handle traffic simultaneously
- No failover delay — if one dies, others continue
- Requires conflict resolution for writes

### Replication
- **Synchronous:** Write confirmed only after all replicas acknowledge (strong consistency, higher latency)
- **Asynchronous:** Write confirmed after primary accepts (lower latency, risk of data loss)
- **Semi-synchronous:** At least one replica confirms (balance)

## Circuit Breakers

A circuit breaker monitors failures and "trips" (opens) when failure rate exceeds a threshold:
- **Closed:** Requests pass through normally
- **Open:** All requests fail immediately (no waiting)
- **Half-Open:** After a timeout, allow a few test requests

This prevents cascade failures where one failing service brings down everything that depends on it.

## Health Checks

Regular probes to verify service health:
- **Liveness:** Is the process running?
- **Readiness:** Can the service handle traffic?
- **Startup:** Has the service finished initialization?

Load balancers use health checks to remove unhealthy instances from rotation.

## Disaster Recovery

### Recovery Time Objective (RTO)
Maximum acceptable time to restore service after failure.

### Recovery Point Objective (RPO)
Maximum acceptable data loss measured in time.

### Backup Strategies
- **Cold standby:** Backups restored manually (high RTO)
- **Warm standby:** Reduced-capacity standby always running (medium RTO)
- **Hot standby:** Full-capacity standby ready to take over (low RTO)

## Chaos Engineering

Proactively inject failures to build confidence in system resilience:
- Randomly terminate instances (Chaos Monkey)
- Inject latency between services
- Simulate network partitions
- Fill disk and exhaust memory

Netflix, Amazon, and Google run chaos experiments continuously in production.

---

*References:*
1. Alex Xu, *System Design Interview – An Insider's Guide.* [Link](https://bytebytego.com/)
2. Martin Kleppmann, *Designing Data-Intensive Applications.* [Link](https://dataintensive.net/)
3. Google, *Site Reliability Engineering.* [Link](https://sre.google/sre-book/table-of-contents/)
4. Jay Kreps, "The Log: What every software engineer should know." [Link](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying)
5. Casey Rosenthal et al., *Chaos Engineering.* [Link](https://www.oreilly.com/library/view/chaos-engineering/9781492043850/)
