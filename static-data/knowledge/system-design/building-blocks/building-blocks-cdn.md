---
slug: building-blocks-cdn
title: "CDNs"
description: "Content Delivery Networks — how edge caching reduces latency and handles global traffic at scale."
order: 9
tags:
  - system-design
  - building-blocks
  - cdn
  - edge-caching
  - global-delivery
prerequisites:
  - fundamentals-scalability
  - building-blocks-caching
references:
  - title: "What is a CDN?"
    author: "Cloudflare"
    url: "https://www.cloudflare.com/learning/cdn/what-is-a-cdn/"
    type: "article"
    description: "Comprehensive CDN explanation with diagrams."
  - title: "Netflix Open Connect"
    author: "Netflix"
    url: "https://openconnect.netflix.com/en/"
    type: "docs"
    description: "How Netflix built a custom CDN for video delivery."
  - title: "How CDNs Work"
    author: "AWS CloudFront"
    url: "https://docs.aws.amazon.com/cloudfront/latest/guide/Introduction.html"
    type: "docs"
    description: "AWS CloudFront CDN architecture."
  - title: "System Design: CDN"
    author: "ByteByteGo"
    url: "https://blog.bytebytego.com/p/cdn"
    type: "article"
    description: "Visual breakdown of CDN architecture."
  - title: "Akamai: How CDNs Work"
    author: "Akamai"
    url: "https://www.akamai.com/learn/cdn/cdn-what-is-a-cdn"
    type: "article"
    description: "Enterprise CDN architecture explanation."
related_knowledge:
  - slug: building-blocks-caching
    title: "Caching"
    lesson_number: 6
  - slug: building-blocks-load-balancers
    title: "Load Balancers"
    lesson_number: 5
  - slug: case-studies-netflix-streaming
    title: "Netflix Video Streaming"
    lesson_number: 5
knowledge_refs:
  - slug: "tools-cloudflare"
    title: "Cloudflare"
  - slug: "tools-aws"
    title: "AWS"
  - slug: "patterns-caching"
    title: "Caching"
---

# CDNs (Content Delivery Networks)

A CDN distributes content across globally distributed edge servers, serving users from the nearest location. CDNs reduce latency, absorb traffic spikes, and reduce origin server load.

## How CDNs Work

### Request Flow
```
User (Tokyo) → DNS → CDN Edge (Tokyo PoP) → Cache HIT → Return content
                                          → Cache MISS → Fetch from Origin → Cache → Return
```

### Push vs Pull CDNs

**Push CDN:**
- You push content to CDN edge servers
- Good for content you control (blog posts, product images)
- Requires you to manage content distribution

**Pull CDN:**
- CDN fetches content on first request, caches for future
- Good for dynamic content or content you don't control
- Simpler setup, but first request hits origin

## CDN Caching Levels

### Edge Cache
- Closest to the user (city/region level)
- Lowest latency
- Limited storage

### Mid-Tier Cache
- Regional aggregation point
- Higher storage than edge
- Reduces origin load

### Origin Cache
- Your own caching layer (Redis, Varnish)
- Final fallback before database
- Highest storage

## When to Use CDNs

### Static Assets (Best Use Case)
- Images, CSS, JavaScript
- Video files, documents
- Software downloads

### Dynamic Content (Growing Use Case)
- API responses with caching headers
- Personalized content (with edge compute)
- A/B testing at the edge

### When NOT to Use CDN
- Highly personalized, real-time data
- Small-scale applications (overhead not worth it)
- Content that changes every second

## Major CDN Providers

| Provider | Strengths | Scale |
|---|---|---|
| **Cloudflare** | Free tier, security, edge compute | 300+ cities |
| **AWS CloudFront** | AWS integration, Lambda@Edge | 450+ PoPs |
| **Akamai** | Enterprise, largest network | 4,100+ PoPs |
| **Fastly** | Real-time purge, edge compute | 90+ PoPs |
| **CloudFront** | Video streaming | Global |

## Custom CDNs

At extreme scale, companies build their own:
- **Netflix Open Connect:** Custom appliances in ISP headends
- **Google Global Cache:** Caches YouTube content inside ISPs
- **TikTok BytePlus CDN:** 1,300+ proprietary PoPs

## CDN Performance Metrics

- **Cache hit ratio:** % of requests served from cache (target: 95%+)
- **Time to first byte (TTFB):** Latency for the first byte of response
- **Edge latency:** How quickly the nearest PoP responds
- **Origin offload:** % of traffic absorbed by CDN (target: 80%+)

---

*References:*
1. Cloudflare, "What is a CDN?" [Link](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)
2. Netflix, "Open Connect." [Link](https://openconnect.netflix.com/en/)
3. AWS, "CloudFront." [Link](https://docs.aws.amazon.com/cloudfront/latest/guide/Introduction.html)
4. ByteByteGo, "System Design: CDN." [Link](https://blog.bytebytego.com/p/cdn)
5. Akamai, "How CDNs Work." [Link](https://www.akamai.com/learn/cdn/cdn-what-is-a-cdn)
