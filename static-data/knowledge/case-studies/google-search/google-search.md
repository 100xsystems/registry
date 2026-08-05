---
slug: google-search
title: "Google Search"
description: "How Google handles 8.5B searches/day with Caffeine indexing, PageRank, and distributed infrastructure like Spanner and BigTable."
order: 8
tags:
  - case-study
  - search
  - indexing
  - pageRank
  - distributed-systems
prerequisites: []
references:
  - title: "How Google Search Works"
    author: "Google Search Central"
    url: "https://developers.google.com/search/docs/fundamentals/how-search-works"
    type: "docs"
    description: "Official guide to Google's search infrastructure."
  - title: "Our New Search Index (Caffeine)"
    author: "Google Search Central"
    url: "https://developers.google.com/search/blog/2010/06/our-new-search-index-caffeine"
    type: "article"
    description: "Technical details of the Caffeine indexing system."
  - title: "A Guide to Google Search Ranking Systems"
    author: "Google Search Central"
    url: "https://developers.google.com/search/docs/appearance/ranking-systems-guide"
    type: "docs"
    description: "Overview of ranking systems including PageRank, RankBrain, BERT."
  - title: "PageRank Algorithm"
    author: "Wikipedia"
    url: "https://en.wikipedia.org/wiki/PageRank"
    type: "article"
    description: "Mathematical formulation and history of PageRank."
  - title: "Google Knowledge Graph"
    author: "Wikipedia"
    url: "https://en.wikipedia.org/wiki/Knowledge_Graph_(Google)"
    type: "article"
    description: "Architecture and scale of Google's knowledge base."
related_knowledge:
  - slug: case-studies-tiktok-video
    title: "TikTok Video Delivery"
    lesson_number: 6
  - slug: case-studies-twitter-newsfeed
    title: "Twitter/X News Feed"
    lesson_number: 2
knowledge_refs:
  - slug: "databases-bigtable"
    title: "BigTable"
  - slug: "databases-spanner"
    title: "Spanner"
  - slug: "patterns-mapreduce"
    title: "MapReduce"
---

# Google Search

Google Search is one of the largest distributed systems in existence, handling 8.5B searches per day (nearly 100,000 queries/second) with sub-second latencies across the entire planet.

## The Scale

- **8.5B+ searches per day** (~100K/second)
- **100 petabytes** of index storage
- **Hundreds of terabytes** of new information indexed daily
- **5 billion+ entities** in the Knowledge Graph
- **500 billion facts** in the Knowledge Graph

## The Indexing Pipeline: Caffeine

Google replaced batch indexing with **Caffeine** — a continuous, real-time streaming system:
- Processes **hundreds of thousands of pages in parallel** every second
- Ingests pages from Googlebot, processes text, images, and JavaScript (via integrated Chromium)
- Pushes updates directly to the global index without periodic rebuilds

## Ranking Algorithms

### PageRank (Link Analysis)
Models the web as a directed graph where hyperlinks are "votes of confidence":
- Random surfer model with damping factor (d ≈ 0.85)
- Computes the dominant eigenvector of the web's transition matrix
- Has evolved significantly to combat link spam

### Modern ML Systems

**RankBrain:** Deep-learning model mapping unfamiliar queries to underlying concepts.

**BERT:** Bidirectional transformer understanding contextual word combinations.

**MUM:** Multitask Unified Model for multilingual, multimodal search (image + text queries).

**SpamBrain:** AI-driven spam detection neutralizing link farms and content manipulation.

## Serving Architecture

### Two-Phase Retrieval & Scoring

**Phase 1 — Retrieval:**
- Fast lookup retrieves thousands of candidate documents from index shards
- Uses inverted indices and phrase matching

**Phase 2 — Scoring & Reranking:**
- Heavy ML pipeline evaluates candidates using hundreds of signals
- Freshness, location, PageRank, personalization, device type
- Top results selected and presented

### Infrastructure

**Borg:** Container orchestrator (predecessor to Kubernetes) running hundreds of thousands of jobs.

**BigTable:** Wide-column NoSQL store providing low-latency reads/writes for real-time indexing.

**Cloud Spanner:** Globally distributed relational database with ACID transactions using TrueTime (atomic clocks + GPS) for external consistency.

## The Knowledge Graph

Launched in 2012 to shift search from "strings to things":
- **5 billion+ entities** (people, places, concepts)
- **500 billion facts** connecting entities
- Powers instant answer boxes, knowledge panels, and voice queries
- Automatically extracts and merges facts from multiple sources

## Key Design Decisions

1. **Real-time indexing** (Caffeine) eliminated weeks-long index staleness
2. **Two-phase retrieval** separates fast candidate selection from expensive ML scoring
3. **PageRank + ML hybrid** combines link authority with semantic understanding
4. **Spanner's TrueTime** solves the global consistency problem without sacrificing availability

## Lessons Learned

- **Index freshness matters** — users want recent information
- **Link analysis is powerful but must evolve** — spam gaming is constant
- **ML augments but doesn't replace** classical algorithms
- **Global infrastructure requires hardware innovation** — atomic clocks for consistency

---

*References:*
1. Google Search Central, "How Google Search Works." [Link](https://developers.google.com/search/docs/fundamentals/how-search-works)
2. Google Search Central, "Our New Search Index (Caffeine)." [Link](https://developers.google.com/search/blog/2010/06/our-new-search-index-caffeine)
3. Google Search Central, "Guide to Google Search Ranking Systems." [Link](https://developers.google.com/search/docs/appearance/ranking-systems-guide)
4. Wikipedia, "PageRank Algorithm." [Link](https://en.wikipedia.org/wiki/PageRank)
5. Wikipedia, "Google Knowledge Graph." [Link](https://en.wikipedia.org/wiki/Knowledge_Graph_(Google))
