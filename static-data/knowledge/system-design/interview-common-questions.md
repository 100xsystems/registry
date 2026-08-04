---
slug: interview-common-questions
title: "Common Design Questions"
description: "The most frequently asked system design interview questions with key concepts and approaches."
order: 15
tags:
  - system-design
  - interview
  - questions
  - practice
  - preparation
prerequisites:
  - interview-framework
references:
  - title: "System Design Interview – An Insider's Guide (Volumes 1 & 2)"
    author: "Alex Xu"
    url: "https://bytebytego.com/"
    type: "book"
    description: "20+ system design questions with detailed solutions."
  - title: "Grokking the System Design Interview"
    author: "Design Gurus"
    url: "https://www.designgurus.io/course/grokking-the-system-design-interview"
    type: "course"
    description: "60+ system design problems with structured solutions."
  - title: "Hello Interview: System Design Questions"
    author: "Hello Interview"
    url: "https://www.hellointerview.com/learn/system-design/in-a-hurry"
    type: "article"
    description: "Curated list of most common system design questions."
  - title: "ByteByteGo: System Design Questions"
    author: "ByteByteGo"
    url: "https://blog.bytebytego.com/p/system-design-questions"
    type: "article"
    description: "Visual breakdown of common system design problems."
  - title: "System Design Primer"
    author: "Donne Martin (GitHub)"
    url: "https://github.com/donnemartin/system-design-primer"
    type: "article"
    description: "Open-source system design study guide."
related_knowledge:
  - slug: interview-framework
    title: "The 4-Step Framework"
    lesson_number: 14
  - slug: interview-trade-offs
    title: "Trade-off Analysis"
    lesson_number: 16
  - slug: case-studies
    title: "System Design Case Studies"
    lesson_number: 1
knowledge_refs:
  - slug: "building-blocks-caching"
    title: "Caching"
  - slug: "building-blocks-databases"
    title: "Databases"
  - slug: "building-blocks-message-queues"
    title: "Message Queues"
---

# Common Design Questions

These are the most frequently asked system design interview questions, grouped by category. Each includes key concepts to discuss and common approaches.

## Social & Messaging

### Design a URL Shortener
**Key concepts:** Hashing, base62 encoding, database design, caching, analytics
**Approach:** Hash URL → store mapping → return short URL. Use counters for unique IDs.

### Design a News Feed
**Key concepts:** Fan-out (push vs pull), caching, ranking, real-time updates
**Approach:** Hybrid fan-out (push for regular users, pull for celebrities). Cache feeds in Redis.

### Design a Chat System
**Key concepts:** WebSockets, message ordering, offline storage, encryption
**Approach:** WebSocket connections, message queue for offline users, message IDs for ordering.

### Design Instagram/TikTok
**Key concepts:** Image/video storage, CDN, feed generation, recommendation engine
**Approach:** Object storage (S3) + CDN for media. ML pipeline for recommendations.

## Infrastructure

### Design a Rate Limiter
**Key concepts:** Token bucket, sliding window, distributed counting, Redis
**Approach:** Token bucket algorithm with Redis for distributed state. Return 429 with Retry-After.

### Design a Key-Value Store
**Key concepts:** Consistent hashing, replication, conflict resolution, Merkle trees
**Approach:** Consistent hashing ring, vector clocks for conflict detection, gossip protocol.

### Design a Web Crawler
**Key concepts:** BFS traversal, URL frontier, politeness, deduplication
**Approach:** URL queue + worker pool. Respect robots.txt, rate limit per domain.

### Design a Notification System
**Key concepts:** Message queues, multi-channel (push/SMS/email), prioritization
**Approach:** Event-driven pipeline with separate queues per channel. Priority queue for urgent notifications.

## Data-Intensive

### Design a Search Autocomplete
**Key concepts:** Trie data structure, frequency counting, real-time updates
**Approach:** Trie with frequency counts at each node. Update frequencies periodically.

### Design a Web Analytics System
**Key concepts:** Event ingestion, time-series data, aggregation, sampling
**Approach:** Kafka for ingestion, Flink for real-time aggregation, ClickHouse for storage.

### Design a Metrics Monitoring System
**Key concepts:** Time-series databases, aggregation, alerting, dashboards
**Approach:** Collectors → Kafka → Time-series DB (InfluxDB/Prometheus) → Alerting rules.

### Design a Distributed Cache
**Key concepts:** Consistent hashing, cache invalidation, replication, eviction
**Approach:** Consistent hashing for distribution. LRU eviction. Replication for fault tolerance.

## Location-Based

### Design Google Maps
**Key concepts:** Geospatial indexing (H3, Quadtree), routing algorithms, real-time traffic
**Approach:** Graph-based routing with A* algorithm. H3 for spatial queries. Real-time traffic from user GPS.

### Design Uber/Lyft
**Key concepts:** Geospatial indexing, matching algorithm, surge pricing, real-time tracking
**Approach:** H3 hexagonal grid for proximity search. Dynamic pricing based on supply/demand.

## Storage & Files

### Design Google Drive/Dropbox
**Key concepts:** File chunking, sync protocol, conflict resolution, metadata
**Approach:** Block-level sync with Merkle trees for change detection. Operational transforms for conflicts.

### Design a Distributed File System
**Key concepts:** Chunking, replication, metadata service, consistency
**Approach:** GFS/HDFS-style: chunk servers for data, master for metadata, 3x replication.

## Video & Streaming

### Design YouTube/Netflix
**Key concepts:** Video encoding, CDN, adaptive streaming, recommendations
**Approach:** Multi-bitrate encoding, CDN for delivery (Open Connect for Netflix), ML recommendations.

---

*References:*
1. Alex Xu, *System Design Interview (Volumes 1 & 2).* [Link](https://bytebytego.com/)
2. Design Gurus, "Grokking the System Design Interview." [Link](https://www.designgurus.io/course/grokking-the-system-design-interview)
3. Hello Interview, "System Design Questions." [Link](https://www.hellointerview.com/learn/system-design/in-a-hurry)
4. ByteByteGo, "System Design Questions." [Link](https://blog.bytebytego.com/p/system-design-questions)
5. Donne Martin, "System Design Primer." [Link](https://github.com/donnemartin/system-design-primer)
