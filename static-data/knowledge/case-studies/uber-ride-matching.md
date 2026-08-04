---
slug: uber-ride-matching
title: "Uber Ride Matching"
description: "How Uber matches riders to drivers in real-time using H3 geospatial indexing, surge pricing, and event-driven architecture."
order: 9
tags:
  - case-study
  - ride-sharing
  - geospatial
  - real-time
  - event-driven
prerequisites: []
references:
  - title: "H3: Uber's Hexagonal Hierarchical Spatial Index"
    author: "Uber Engineering"
    url: "https://www.uber.com/blog/h3/"
    type: "article"
    description: "Technical overview of H3 hexagonal spatial indexing."
  - title: "Uber's Real-Time Market Platform"
    author: "Uber Engineering"
    url: "https://www.uber.com/blog/real-time-market-platform/"
    type: "article"
    description: "Architecture of Uber's real-time dispatch and pricing system."
  - title: "Uber's Kafka Architecture"
    author: "Uber Engineering"
    url: "https://www.uber.com/blog/kafka/"
    type: "article"
    description: "How Uber scales Kafka for 70+ countries and 19M trips/day."
  - title: "System Design: Uber Ride Sharing"
    author: "ByteByteGo"
    url: "https://blog.bytebytego.com/p/uber-system-design"
    type: "article"
    description: "Visual breakdown of Uber's matching and dispatch architecture."
  - title: "Uber's Geospatial Data Pipeline"
    author: "Uber Engineering"
    url: "https://www.uber.com/blog/geospatial/"
    type: "article"
    description: "How Uber processes GPS data at scale for real-time tracking."
related_knowledge:
  - slug: case-studies-amazon-shopping-cart
    title: "Amazon Shopping Cart"
    lesson_number: 7
  - slug: case-studies-google-search
    title: "Google Search"
    lesson_number: 8
knowledge_refs:
  - slug: "tools-kafka"
    title: "Kafka"
  - slug: "patterns-event-driven"
    title: "Event-Driven Architecture"
  - slug: "patterns-consistent-hashing"
    title: "Consistent Hashing"
---

# Uber Ride Matching

Uber's ride-matching system solves one of the hardest real-time optimization problems: matching millions of riders to drivers across 70+ countries while dynamically pricing based on supply and demand.

## The Scale

- **19M+ trips per day**
- **70+ countries, 10,000+ cities**
- **5M+ active drivers** worldwide
- **Billions** of GPS data points daily
- **Millions** of concurrent requests

## H3: Hexagonal Spatial Indexing

Uber created **H3** to solve geospatial queries at scale:
- Earth divided into hexagonal cells (16 resolutions)
- Hexagons have uniform distance to all neighbors (unlike squares)
- Enables fast proximity queries: "Find all drivers within 2km"
- Each GPS coordinate maps to a single H3 index for efficient lookups

### Why Hexagons?
- **No edge effects:** Equal neighbor distances reduce approximation errors
- **Hierarchical:** Coarse cells for regional queries, fine cells for precise matching
- **Compact:** 64-bit integer representation fits in database indexes

## Real-Time Matching Algorithm

### The Dispatch Pipeline

1. **Rider requests ride** → GPS location captured
2. **Proximity search:** H3 finds drivers within expanding radius
3. **Scoring:** Drivers ranked by distance, rating, vehicle type, direction of travel
4. **Assignment:** Best driver notified with 15-second acceptance window
5. **Fallback:** If declined, next-best driver notified

### Matching Constraints
- Driver must be heading toward rider (not just nearby)
- Vehicle type must match rider's selection
- Driver rating must meet minimum threshold
- Real-time traffic considered for ETA accuracy

## Surge Pricing (Dynamic Pricing)

### How It Works
When demand exceeds supply in a region:
1. **Heat map analysis:** Identify high-demand zones
2. **Price multiplier calculation:** Based on supply-demand ratio
3. **Real-time adjustment:** Prices update every few minutes
4. **Incentive signaling:** Higher prices attract more drivers to the zone

### The Economics
- Surge pricing is **not** price gouging — it's a market signal
- Balances supply and demand without central coordination
- Drivers naturally gravitate toward high-surge areas
- Reduces wait times during peak demand

## GPS Data Pipeline

### Ingestion
- **Kafka:** High-throughput ingestion of GPS pings from millions of drivers
- **Geohash partitioning:** Data sharded by geographic region for locality

### Processing
- **Apache Flink:** Real-time stream processing for:
  - Driver position updates
  - ETA calculations
  - Traffic pattern analysis
  - Demand forecasting

### Storage
- **Cassandra:** Time-series storage for driver positions
- **Redis:** Hot data cache for active driver locations
- **Custom geospatial stores:** Optimized for proximity queries

## Event-Driven Architecture

Uber's backend is fully event-driven:
- **Ride events** (requested, matched, started, completed) flow through Kafka
- **Payment events** processed asynchronously after ride completion
- **Analytics events** feed real-time dashboards and ML models
- **Driver events** (online, offline, moving, idle) update availability state

## Key Design Decisions

1. **H3 hexagonal indexing** provides uniform spatial queries without edge artifacts
2. **Dynamic pricing** balances supply/demand without central coordination
3. **Event-driven architecture** enables real-time responsiveness at scale
4. **Expanding radius search** ensures matches are found even in low-supply areas

## Lessons Learned

- **Geospatial indexing is critical** for location-based services — naive approaches don't scale
- **Dynamic pricing works** when it's transparent and tied to real supply/demand
- **Event-driven beats request-response** for real-time systems
- **Graceful degradation** (expanding search radius) prevents service failures

---

*References:*
1. Uber Engineering, "H3: Uber's Hexagonal Hierarchical Spatial Index." [Link](https://www.uber.com/blog/h3/)
2. Uber Engineering, "Uber's Real-Time Market Platform." [Link](https://www.uber.com/blog/real-time-market-platform/)
3. Uber Engineering, "Uber's Kafka Architecture." [Link](https://www.uber.com/blog/kafka/)
4. ByteByteGo, "System Design: Uber Ride Sharing." [Link](https://blog.bytebytego.com/p/uber-system-design)
5. Uber Engineering, "Uber's Geospatial Data Pipeline." [Link](https://www.uber.com/blog/geospatial/)
