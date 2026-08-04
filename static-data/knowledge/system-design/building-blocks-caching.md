---
slug: building-blocks-caching
title: "Caching"
description: "Caching strategies for reducing latency and database load — Cache-Aside, Write-Through, Write-Behind, and eviction policies."
order: 6
tags:
  - system-design
  - building-blocks
  - caching
  - redis
  - memcached
  - performance
prerequisites:
  - fundamentals-scalability
references:
  - title: "Caching Strategies and Their Use Cases"
    author: "ByteByteGo"
    url: "https://blog.bytebytego.com/p/caching-strategies"
    type: "article"
    description: "Visual guide to caching patterns and trade-offs."
  - title: "Caching at Reddit"
    author: "Reddit Engineering"
    url: "https://redditengineering.com/how-reddit-serves-more-than-a-billion-requests-an-hour/"
    type: "article"
    description: "How Reddit scales with caching at 1B+ requests/hour."
  - title: "Redis Documentation"
    author: "Redis"
    url: "https://redis.io/documentation"
    type: "docs"
    description: "Official Redis documentation for caching implementation."
  - title: "Memcached Architecture"
    author: "Memcached"
    url: "https://github.com/memcached/memcached/wiki"
    type: "docs"
    description: "Memcached architecture and deployment guide."
  - title: "CDN Caching vs Application Caching"
    author: "Cloudflare"
    url: "https://www.cloudflare.com/learning/cdn/what-is-caching/"
    type: "article"
    description: "Different levels of caching in modern systems."
related_knowledge:
  - slug: building-blocks-load-balancers
    title: "Load Balancers"
    lesson_number: 5
  - slug: building-blocks-cdn
    title: "CDNs"
    lesson_number: 9
  - slug: building-blocks-databases
    title: "Databases"
    lesson_number: 8
knowledge_refs:
  - slug: "databases-redis"
    title: "Redis"
  - slug: "patterns-caching"
    title: "Caching Patterns"
  - slug: "databases-memcached"
    title: "Memcached"
---

# Caching

Caching stores frequently accessed data in fast storage (memory) to reduce database load and response times. A well-designed cache can reduce latency from milliseconds to microseconds.

## Where to Cache

### Browser Cache
- Stores static assets (CSS, JS, images)
- Controlled by HTTP headers (Cache-Control, ETag)
- Reduces network requests entirely

### CDN Cache
- Caches static and dynamic content at edge locations
- Reduces latency by serving from nearest PoP
- Handles 60-80% of traffic for popular content

### Application Cache
- In-memory stores (Redis, Memcached) between app and database
- Reduces database queries by 90%+ for hot data
- Most impactful for system design

### Database Cache
- Query result cache, buffer pool, materialized views
- Transparent to application layer

## Caching Patterns

### Cache-Aside (Lazy Loading)
Application manages the cache explicitly:
```
1. App checks cache for data
2. Cache HIT → return cached data
3. Cache MISS → query database → store in cache → return
```
**Pros:** Only caches what's requested, resilient to cache failure.
**Cons:** Cache miss = 3 trips (cache, DB, cache write).

### Write-Through
Cache sits in front of database, writes go to both:
```
1. App writes to cache
2. Cache synchronously writes to database
3. Acknowledge to app
```
**Pros:** Cache is always consistent with database.
**Cons:** Write latency doubled, unused data may be cached.

### Write-Behind (Write-Back)
Write to cache, asynchronously flush to database:
```
1. App writes to cache
2. Acknowledge to app immediately
3. Background process writes to database
```
**Pros:** Very fast writes, reduced database load.
**Cons:** Risk of data loss if cache fails before flush.

### Read-Through
Cache automatically fetches from database on miss (app doesn't know about DB):
```
1. App reads from cache
2. Cache miss → cache fetches from DB itself
3. Cache returns data
```
**Pros:** Simpler app code.
**Cons:** Cache must know how to query DB.

## Eviction Policies

When cache is full, which items to remove?

| Policy | Description | Use Case |
|---|---|---|
| **LRU** (Least Recently Used) | Remove least recently accessed | General purpose (most common) |
| **LFU** (Least Frequently Used) | Remove least frequently accessed | Stable access patterns |
| **FIFO** (First In, First Out) | Remove oldest entries | Temporary data |
| **TTL** (Time to Live) | Expire after fixed time | Session data, tokens |

## Cache Invalidation Strategies

The hardest problem in caching: keeping cache consistent with database.

### TTL-Based
Set expiration time on cache entries:
- Simple to implement
- Stale data possible until TTL expires
- Good for data that changes infrequently

### Event-Based
Invalidate cache when data changes:
```
1. Database write occurs
2. Publish invalidation event
3. Cache listens and removes affected entries
```
- Real-time consistency
- More complex to implement
- Risk of missed events

### Version-Based
Include version in cache key:
```
cache_key = "user:123:v2"
```
- Old cache entries naturally expire
- No explicit invalidation needed
- Simple but increases cache size

## Common Pitfalls

- **Cache stampede:** Many requests hit cache simultaneously after expiration → solution: lock or probabilistic early expiration
- **Thundering herd:** Same as stampede but at application level → solution: request coalescing
- **Hot keys:** One cache entry receives disproportionate traffic → solution: replication or local caching
- **Cold cache:** Cache is empty after restart → solution: warm-up process

---

*References:*
1. ByteByteGo, "Caching Strategies." [Link](https://blog.bytebytego.com/p/caching-strategies)
2. Reddit Engineering, "How Reddit Serves 1B+ Requests/Hour." [Link](https://redditengineering.com/how-reddit-serves-more-than-a-billion-requests-an-hour/)
3. Redis, "Documentation." [Link](https://redis.io/documentation)
4. Memcached, "Architecture." [Link](https://github.com/memcached/memcached/wiki)
5. Cloudflare, "What is Caching?" [Link](https://www.cloudflare.com/learning/cdn/what-is-caching/)
