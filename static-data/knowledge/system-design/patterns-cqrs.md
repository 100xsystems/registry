---
slug: patterns-cqrs
title: "CQRS & Event Sourcing"
description: "Separating read and write models for scalability, and storing state changes as immutable events."
order: 11
tags:
  - system-design
  - patterns
  - cqrs
  - event-sourcing
  - event-driven
  - architecture
prerequisites:
  - building-blocks-databases
  - building-blocks-message-queues
references:
  - title: "CQRS Pattern"
    author: "Microsoft Azure"
    url: "https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs"
    type: "docs"
    description: "Official Microsoft guide to CQRS pattern."
  - title: "Event Sourcing Pattern"
    author: "Microsoft Azure"
    url: "https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing"
    type: "docs"
    description: "Official Microsoft guide to Event Sourcing."
  - title: "Martin Fowler: CQRS"
    author: "Martin Fowler"
    url: "https://martinfowler.com/bliki/CQRS.html"
    type: "article"
    description: "Foundational article on CQRS by Martin Fowler."
  - title: "Event Sourcing in Practice"
    author: "EventStoreDB"
    url: "https://www.eventstore.com/event-sourcing"
    type: "article"
    description: "Practical guide to event sourcing implementation."
  - title: "System Design: CQRS"
    author: "ByteByteGo"
    url: "https://blog.bytebytego.com/p/cqrs"
    type: "article"
    description: "Visual breakdown of CQRS architecture."
related_knowledge:
  - slug: building-blocks-databases
    title: "Databases"
    lesson_number: 8
  - slug: building-blocks-message-queues
    title: "Message Queues"
    lesson_number: 7
  - slug: patterns-consistent-hashing
    title: "Consistent Hashing & Sharding"
    lesson_number: 10
knowledge_refs:
  - slug: "tools-kafka"
    title: "Kafka"
  - slug: "patterns-event-driven"
    title: "Event-Driven Architecture"
  - slug: "databases-postgresql"
    title: "PostgreSQL"
---

# CQRS & Event Sourcing

CQRS (Command Query Responsibility Segregation) separates read and write models. Event Sourcing stores state as a sequence of immutable events rather than mutable records. Together, they enable scalable, auditable, and auditable systems.

## CQRS: Separating Reads and Writes

### The Problem
In traditional architectures, the same model handles both reads and writes:
```
Request → Single Model → Single Database → Response
```
This works for simple systems but breaks when:
- Read and write patterns differ significantly
- Read traffic far exceeds write traffic
- Different scaling needs for reads vs writes

### The CQRS Solution
```
Write Path: Command → Write Model → Write Database → Event
Read Path: Query → Read Model → Read Database → Response
```

**Write side:** Optimized for consistency and validation
**Read side:** Optimized for query performance and denormalization

### When to Use CQRS
- Read/write ratios are heavily skewed (100:1 or more)
- Different data shapes needed for reads vs writes
- Multiple read models needed (search, analytics, UI)
- Complex domain logic on the write side

### When NOT to Use CQRS
- Simple CRUD applications
- Small systems with low traffic
- Team lacks distributed systems experience

## Event Sourcing: Storing Events, Not State

### Traditional Approach
Store current state:
```
Account Balance: $500
```
**Problem:** History is lost. How did we get to $500?

### Event Sourcing Approach
Store every state change:
```
Event 1: AccountCreated(amount=0)
Event 2: MoneyDeposited(amount=1000)
Event 3: MoneyWithdrawn(amount=300)
Event 4: MoneyDeposited(amount=500)
Event 5: MoneyWithdrawn(amount=700)
Current State: Derived from events = $500
```

**Benefits:**
- Complete audit trail
- Can reconstruct state at any point in time
- Debug by replaying events
- Natural fit for event-driven systems

### Projections
Derived read models built from events:
```
Events → Projection Handler → Read Model

Events: [OrderCreated, ItemAdded, ItemAdded, OrderPaid]
→ Projection: { order_id: 123, items: 2, total: $50, status: "paid" }
```

## CQRS + Event Sourcing Together

This is the most powerful combination:
```
Command → Aggregate → Event Store (append-only)
                         ↓
                    Event Bus (Kafka)
                         ↓
                    Projection 1: Search Index
                    Projection 2: Analytics DB
                    Projection 3: UI Read Model
```

**Each read model is independently scalable** and optimized for its specific query pattern.

## Trade-offs

### Benefits
- Independent scaling of reads and writes
- Complete audit trail (event sourcing)
- Multiple optimized read models
- Natural fit for distributed systems

### Costs
- Increased complexity
- Eventual consistency between write and read sides
- Event schema evolution is challenging
- Requires infrastructure for event storage and projection

---

*References:*
1. Microsoft Azure, "CQRS Pattern." [Link](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs)
2. Microsoft Azure, "Event Sourcing Pattern." [Link](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing)
3. Martin Fowler, "CQRS." [Link](https://martinfowler.com/bliki/CQRS.html)
4. EventStoreDB, "Event Sourcing in Practice." [Link](https://www.eventstore.com/event-sourcing)
5. ByteByteGo, "System Design: CQRS." [Link](https://blog.bytebytego.com/p/cqrs)
