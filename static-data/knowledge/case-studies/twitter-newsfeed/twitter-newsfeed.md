---
slug: twitter-newsfeed
title: "Twitter/X News Feed"
description: "How Twitter delivers 500M+ tweets/day to hundreds of millions of users using hybrid fan-out strategies."
order: 2
tags:
  - case-study
  - social-media
  - fan-out
  - caching
  - distributed-systems
prerequisites: []
references:
  - title: "Design Twitter/X Feed: The Hardest Feed System at Scale"
    author: "ScaleDojo"
    url: "https://scaledojo.dev/blogs/design-twitterx-feed-the-hardest-feed-system-at-scale"
    type: "article"
    description: "Comprehensive breakdown of Twitter's hybrid fan-out architecture."
  - title: "Will Twitter Collapse? Examining the Resiliency of Twitter's Architecture"
    author: "Engineering Enablement"
    url: "https://engineeringenablement.substack.com/p/will-twitter-collapse-examining-the"
    type: "article"
    description: "Analysis of Twitter's architectural resilience and potential failure points."
  - title: "Introducing FlockDB"
    author: "X Engineering"
    url: "https://blog.x.com/engineering/en_us/a/2010/introducing-flockdb"
    type: "article"
    description: "Twitter's distributed graph database for social relationships."
  - title: "Processing Billions of Events in Real Time at Twitter"
    author: "X Engineering"
    url: "https://blog.x.com/engineering/en_us/topics/infrastructure/2021/processing-billions-of-events-in-real-time-at-twitter-"
    type: "article"
    description: "Real-time event processing with Kafka and Flink."
  - title: "The Distributed Database Behind Twitter"
    author: "Yugabyte"
    url: "https://www.yugabyte.com/blog/recap-the-distributed-database-behind-twitter/"
    type: "article"
    description: "Technical analysis of Manhattan, Twitter's custom key-value store."
related_knowledge:
  - slug: case-studies-whatsapp-messaging
    title: "WhatsApp Real-Time Messaging"
    lesson_number: 3
  - slug: case-studies-discord-chat
    title: "Discord Real-Time Communication"
    lesson_number: 4
knowledge_refs:
  - slug: "tools-redis"
    title: "Redis"
  - slug: "patterns-fanout"
    title: "Fan-out Pattern"
  - slug: "patterns-consistent-hashing"
    title: "Consistent Hashing"
---

# Twitter/X News Feed

Twitter's news feed is one of the most studied distributed systems architectures. Serving 500M+ tweets daily to 400M+ active users requires solving the fundamental tension between read speed and write amplification.

## The Scale

- **500M+ tweets per day** (~5,800 writes/second, peaks much higher)
- **400M+ monthly active users**
- **Sub-200ms p99 latency** for timeline loading
- **200+ billion timeline requests per day**

## The Core Problem

When a user posts a tweet, how do all their followers see it quickly?

**Option A (Fan-out-on-Write):** Push the tweet to every follower's timeline cache immediately.
- ✅ Reads are instant ($O(1)$ lookup)
- ❌ A tweet from a 100M-follower account triggers 100M cache writes

**Option B (Fan-out-on-Read):** Don't pre-compute anything. At read time, fetch the user's follows and merge their latest tweets.
- ✅ Writes are cheap
- ❌ Reads are slow (must sort thousands of tweets at read time)

## The Solution: Hybrid Fan-out

Twitter uses a **hybrid model** based on follower count:

### Regular Users (Fan-out-on-Write)
For accounts below a dynamic follower threshold:
1. User posts a tweet → stored in primary database
2. Background fan-out service fetches follower graph
3. Tweet ID pushed to every follower's timeline cache (Redis sorted set)

**Read path:** Single `ZREVRANGE` query on the sorted set → instant timeline.

### Celebrity Accounts (Fan-out-on-Read)
For accounts above the threshold (e.g., major news outlets, top celebrities):
1. Tweet stored only in the author's timeline
2. At read time, the system merges pushed timeline with live-fetched celebrity tweets

**This bounds the maximum write amplification** any single tweet can cause.

## Infrastructure

### Databases
- **Manhattan:** Custom distributed key-value store (RocksDB-based) for tweet objects, user metadata, and DMs across tens of thousands of nodes
- **FlockDB:** Distributed graph database (MySQL-backed) for the social graph (who-follows-who)

### Caching
- **Redis Sorted Sets:** Pre-computed home timelines ordered by timestamp
- **Memcached:** Raw tweet objects, user profiles, feature stores

### Real-Time Processing
- **Kafka + Flink:** Real-time event streaming for trending topics (sliding-window counts), analytics, and ML pipelines
- **Snowflake ID Generator:** Unique, time-sortable 64-bit IDs without central coordination (41 bits timestamp, 10 bits machine, 12 bits sequence)

## Key Design Decisions

1. **Hybrid fan-out** solves the celebrity problem without sacrificing read performance for regular users
2. **Sorted sets in Redis** enable O(1) timeline queries with chronological ordering
3. **Snowflake IDs** eliminate distributed ID coordination bottlenecks
4. **Separation of concerns:** Manhattan (storage), FlockDB (graph), Redis (caching), Kafka (streaming)

## Lessons Learned

- **There's no one-size-fits-all:** The hybrid approach acknowledges that different accounts have vastly different follower distributions
- **Write amplification is the enemy:** Pre-computing timelines for millions of followers per tweet is expensive but worth it for read speed
- **Distributed ID generation matters:** At Twitter's scale, even ID generation becomes a bottleneck without careful design

---

*References:*
1. ScaleDojo, "Design Twitter/X Feed: The Hardest Feed System at Scale." [Link](https://scaledojo.dev/blogs/design-twitterx-feed-the-hardest-feed-system-at-scale)
2. Engineering Enablement, "Will Twitter Collapse?" [Link](https://engineeringenablement.substack.com/p/will-twitter-collapse-examining-the)
3. X Engineering, "Introducing FlockDB." [Link](https://blog.x.com/engineering/en_us/a/2010/introducing-flockdb)
4. X Engineering, "Processing Billions of Events in Real Time." [Link](https://blog.x.com/engineering/en_us/topics/infrastructure/2021/processing-billions-of-events-in-real-time-at-twitter-)
5. Yugabyte, "The Distributed Database Behind Twitter." [Link](https://www.yugabyte.com/blog/recap-the-distributed-database-behind-twitter/)
