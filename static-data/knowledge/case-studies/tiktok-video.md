---
slug: tiktok-video
title: "TikTok Video Delivery"
description: "How TikTok's AI-powered recommendation engine and video pipeline serve 1B+ users with personalized content."
order: 6
tags:
  - case-study
  - video
  - recommendation-engine
  - machine-learning
  - cdn
prerequisites: []
references:
  - title: "Monolith: Real-Time Recommendation System with Collisionless Embedding Table"
    author: "J. Liu et al. (ByteDance/VLDB)"
    url: "https://arxiv.org/abs/2209.07663"
    type: "paper"
    description: "ByteDance's real-time ML architecture for recommendations."
  - title: "ByteDance Processes Billions of Daily Videos on AWS Inferentia2"
    author: "AWS ML Blog"
    url: "https://aws.amazon.com/blogs/machine-learning/bytedance-processes-billions-of-daily-videos-using-their-multimodal-video-understanding-models-on-aws-inferentia2/"
    type: "article"
    description: "Large-scale multimodal AI pipelines and hardware acceleration."
  - title: "ByteGraph: A High-Performance Distributed Graph Database at ByteDance"
    author: "C. Li et al."
    url: "https://www.vldb.org/pvldb/"
    type: "paper"
    description: "Social graph partitioning and low-latency traversal storage."
  - title: "System Design: TikTok Architecture"
    author: "System Design Handbook"
    url: "https://systemdesign.one/"
    type: "article"
    description: "Multi-tier CDN caching and transcoding architecture analysis."
  - title: "TikTok's Recommendation Algorithm Explained"
    author: "ByteByteGo"
    url: "https://blog.bytebytego.com/p/tiktoks-recommendation-algorithm"
    type: "article"
    description: "Visual breakdown of TikTok's For You Page algorithm."
related_knowledge:
  - slug: case-studies-netflix-streaming
    title: "Netflix Video Streaming"
    lesson_number: 5
  - slug: case-studies-google-search
    title: "Google Search"
    lesson_number: 8
knowledge_refs:
  - slug: "ai-ml-recommendation-systems"
    title: "Recommendation Systems"
  - slug: "tools-kafka"
    title: "Kafka"
  - slug: "patterns-event-driven"
    title: "Event-Driven Architecture"
---

# TikTok Video Delivery

TikTok's "For You" feed is an industry benchmark in AI-powered personalization, serving 1B+ users with a recommendation engine that learns from every interaction in real-time.

## The Scale

- **1B+ monthly active users**
- **Tens of millions** of daily video uploads
- **1,300+ CDN PoPs** globally
- **Sub-300ms** time-to-first-frame
- **Petabytes** of video processed daily

## Recommendation Engine

### Two-Stage Pipeline

**1. Candidate Generation (Retrieval):**
- Narrows billions of videos to hundreds of candidates
- Uses Approximate Nearest Neighbor (ANN) vector searches
- Deep retrieval models based on user/item embeddings

**2. Fine Ranking:**
- Deep neural networks evaluate hundreds of real-time features
- Watch time, completion rate, skips, sound usage, shares
- Outputs final ranked list for the For You Page

### Monolith: Real-Time Training

Unlike traditional batch-trained models, ByteDance's **Monolith** enables near real-time online training:
- User interactions stream via Kafka/Flink
- Gradients computed and model parameters updated on the fly
- **Collisionless embedding tables** using Cuckoo Hashing prevent popular items from overwriting rare ones
- **Expirable embeddings** automatically purge stale data

### Incremental Sync
Sparse embedding tables (hundreds of GB) are synced incrementally from training servers to live inference servers without taking the system offline.

## Video Processing Pipeline

### Upload & Encoding
1. Client performs chunked, resumable upload to regional edge servers
2. Instant low-resolution preview generated for immediate playback
3. Heavy transcoding and AI moderation occur asynchronously

### Codecs
- H.264, HEVC/H.265, AV1 for standard delivery
- **BVC2.0 (ByteVC):** Proprietary codec with exceptional compression efficiency

### AI Video Understanding
Multimodal LLMs on AWS Inferentia2 process billions of videos daily for:
- Content moderation and safety filtering
- Feature extraction (semantic embeddings like "dance" or "tutorial")

## CDN Strategy

### Multi-CDN + Private Edge
Mix of commercial CDNs and proprietary BytePlus CDN (1,300+ PoPs):
- **Hot/Cold tiering:** Trending videos on SSD-backed edge nodes; long-tail on cold storage
- **Predictive cache warming:** When videos show viral indicators, edge nodes preemptively replicate across regions

## Real-Time Feature Pipeline

- **Event streaming:** User actions flow through Kafka/ByteMQ
- **Stream processing:** Apache Flink joins real-time interactions with static metadata
- **Log-odds correction:** Prevents distributional bias from negative sampling

## Key Design Decisions

1. **Real-time model training** gives TikTok a competitive edge in personalization
2. **Collisionless embeddings** prevent the "popularity bias" problem in recommendations
3. **Predictive cache warming** reduces latency for viral content
4. **AI-first video processing** automates moderation at scale

## Lessons Learned

- **Real-time ML beats batch ML** for recommendation quality
- **Embedding table design** is critical — hash collisions silently degrade recommendations
- **CDN tiering** balances cost and performance for petabyte-scale content
- **Multimodal AI** is essential for content understanding at scale

---

*References:*
1. J. Liu et al., "Monolith: Real-Time Recommendation System," VLDB 2022. [Link](https://arxiv.org/abs/2209.07663)
2. AWS ML Blog, "ByteDance Processes Billions of Daily Videos." [Link](https://aws.amazon.com/blogs/machine-learning/bytedance-processes-billions-of-daily-videos-using-their-multimodal-video-understanding-models-on-aws-inferentia2/)
3. C. Li et al., "ByteGraph: Distributed Graph Database at ByteDance." [Link](https://www.vldb.org/pvldb/)
4. System Design Handbook, "TikTok Architecture." [Link](https://systemdesign.one/)
5. ByteByteGo, "TikTok's Recommendation Algorithm Explained." [Link](https://blog.bytebytego.com/p/tiktoks-recommendation-algorithm)
