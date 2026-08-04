---
slug: building-blocks-databases
title: "Databases"
description: "SQL vs NoSQL, replication, sharding, and choosing the right database for your system design."
order: 8
tags:
  - system-design
  - building-blocks
  - databases
  - sql
  - nosql
  - replication
  - sharding
prerequisites:
  - fundamentals-scalability
references:
  - title: "Designing Data-Intensive Applications"
    author: "Martin Kleppmann"
    url: "https://dataintensive.net/"
    type: "book"
    description: "The definitive guide to database internals and distributed data."
  - title: "System Design: Database"
    author: "ByteByteGo"
    url: "https://blog.bytebytego.com/p/database"
    type: "article"
    description: "Visual guide to database choices in system design."
  - title: "SQL vs NoSQL"
    author: "AWS"
    url: "https://aws.amazon.com/nosql/ vs-sql/"
    type: "article"
    description: "Comparison of SQL and NoSQL databases."
  - title: "Database Sharding Explained"
    author: "ScyllaDB"
    url: "https://www.scylladb.com/glossary/database-sharding/"
    type: "article"
    description: "Technical deep dive on sharding strategies."
  - title: "CAP Theorem"
    author: "Wikipedia"
    url: "https://en.wikipedia.org/wiki/CAP_theorem"
    type: "article"
    description: "Formal definition and implications of CAP theorem."
related_knowledge:
  - slug: building-blocks-caching
    title: "Caching"
    lesson_number: 6
  - slug: building-blocks-message-queues
    title: "Message Queues"
    lesson_number: 7
  - slug: patterns-consistent-hashing
    title: "Consistent Hashing & Sharding"
    lesson_number: 10
knowledge_refs:
  - slug: "databases-postgresql"
    title: "PostgreSQL"
  - slug: "databases-mongodb"
    title: "MongoDB"
  - slug: "databases-cassandra"
    title: "Cassandra"
---

# Databases

Choosing the right database and understanding how to scale it is critical for system design. The SQL vs NoSQL decision, replication strategies, and sharding approaches define your system's capabilities.

## SQL vs NoSQL

### SQL (Relational)
Structured data with predefined schemas:
- **ACID:** Atomicity, Consistency, Isolation, Durability
- **Joins:** Complex queries across tables
- **Schema:** Enforced data types and relationships
- **Examples:** PostgreSQL, MySQL, SQLite

**Best for:** Financial transactions, user management, data with clear relationships.

### NoSQL (Non-Relational)
Flexible schemas for unstructured data:
- **BASE:** Basically Available, Soft state, Eventual consistency
- **No joins:** Denormalized data
- **Schema-less:** Flexible document structures
- **Examples:** MongoDB, Cassandra, Redis, DynamoDB

**Best for:** Real-time data, content management, high-write workloads, caching.

## NoSQL Database Types

| Type | Data Model | Use Case | Example |
|---|---|---|---|
| **Key-Value** | Key → Value | Caching, sessions, config | Redis, DynamoDB |
| **Document** | JSON/BSON documents | Content management, user profiles | MongoDB, CouchDB |
| **Wide-Column** | Rows with dynamic columns | Time-series, IoT, analytics | Cassandra, HBase |
| **Graph** | Nodes and edges | Social networks, recommendations | Neo4j, Neptune |

## Replication

### Leader-Follower (Primary-Replica)
One leader handles writes, followers replicate for reads:
```
Write → Leader → Follower 1 (read)
              → Follower 2 (read)
```
**Pros:** Read scaling, basic failover.
**Cons:** Write bottleneck, replication lag.

### Multi-Leader
Multiple nodes accept writes, sync with each other:
```
Write → Leader 1 ↔ Leader 2
       Leader 1 → Follower 1
       Leader 2 → Follower 2
```
**Pros:** Write scaling, geographic distribution.
**Cons:** Conflict resolution needed.

### Leaderless (Dynamo-Style)
Any node accepts reads/writes, uses quorum:
```
Write → Node 1, 2, 3 (W=2 must acknowledge)
Read → Node 1, 2, 3 (R=2 must respond, return latest)
```
**Pros:** No single point of failure, high availability.
**Cons:** Complex consistency logic.

## Sharding (Partitioning)

Splitting data across multiple databases:

### Hash-Based Sharding
```
shard = hash(key) % num_shards
```
- Even distribution
- Hard to rescale (adding shards changes all mappings)

### Range-Based Sharding
```
shard 0: keys A-M
shard 1: keys N-Z
```
- Easy range queries
- Hot spots for sequential data

### Directory-Based Sharding
Lookup service maps keys to shards:
```
key → directory → shard
```
- Flexible resharding
- Extra lookup overhead

## Choosing a Database

| Requirement | Recommended |
|---|---|
| ACID transactions | PostgreSQL, MySQL |
| High write throughput | Cassandra, DynamoDB |
| Complex relationships | PostgreSQL, Neo4j |
| Caching/sessions | Redis |
| Document storage | MongoDB |
| Time-series data | InfluxDB, TimescaleDB |
| Full-text search | Elasticsearch |

---

*References:*
1. Martin Kleppmann, *Designing Data-Intensive Applications.* [Link](https://dataintensive.net/)
2. ByteByteGo, "System Design: Database." [Link](https://blog.bytebytego.com/p/database)
3. AWS, "SQL vs NoSQL." [Link](https://aws.amazon.com/nosql/)
4. ScyllaDB, "Database Sharding Explained." [Link](https://www.scylladb.com/glossary/database-sharding/)
5. Wikipedia, "CAP Theorem." [Link](https://en.wikipedia.org/wiki/CAP_theorem)
