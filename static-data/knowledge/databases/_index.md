---
slug: databases
title: "Databases"
description: "12 database technologies organized by type — SQL, NoSQL, key-value, document, and time-series."
order: 1
tags:
  - databases
  - sql
  - nosql
  - data-storage
---

# Databases

12 database technologies. Choose based on your data model and access patterns.

## Top 5 Must-Know Databases

1. **[PostgreSQL](/knowledge/databases/postgresql)** — Most advanced SQL database
2. **[Redis](/knowledge/databases/redis)** — In-memory cache and data structure server
3. **[MongoDB](/knowledge/databases/mongodb)** — Document database
4. **[MySQL](/knowledge/databases/mysql)** — Most popular SQL database
5. **[SQLite](/knowledge/databases/sqlite)** — Embedded database

## By Type

### Relational (SQL)
- [PostgreSQL](/knowledge/databases/postgresql) — Advanced features, JSON support, full ACID
- [MySQL](/knowledge/databases/mysql) — Popular, battle-tested
- [SQLite](/knowledge/databases/sqlite) — Embedded, zero-config
- [SQL](/knowledge/data-formats/sql) — Query language reference

### Document
- [MongoDB](/knowledge/databases/mongodb) — Flexible schema, JSON-like documents

### Key-Value
- [Redis](/knowledge/databases/redis) — In-memory, pub/sub, data structures

### Search
- [Elasticsearch](/knowledge/tools/elasticsearch) — Full-text search and analytics

### Graph
- [Neo4j](/knowledge/databases/neo4j) — Graph database for relationships

### Time-Series
- [InfluxDB](/knowledge/databases/influxdb) — Time-series data

### Wide-Column
- [Cassandra](/knowledge/databases/cassandra) — Distributed, high-availability

### NewSQL
- [CockroachDB](/knowledge/databases/cockroachdb) — Distributed SQL
- [TiDB](/knowledge/databases/tidb) — MySQL-compatible distributed SQL

## When to Use What

| Use Case | Database |
|---|---|
| Web application data | PostgreSQL |
| Session/cache | Redis |
| User-generated content | MongoDB |
| Full-text search | Elasticsearch |
| Social graph | Neo4j |
| IoT/metrics | InfluxDB |
| Mobile app | SQLite |
| High-availability writes | Cassandra |

## Related
- [System Design: Databases](/knowledge/system-design/building-blocks-databases) — How to choose and scale
- [Roadmap: Backend Engineer](/knowledge/roadmaps/backend-engineer) — Database learning path
