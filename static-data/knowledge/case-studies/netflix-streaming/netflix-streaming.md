---
slug: netflix-streaming
title: "Netflix Video Streaming"
description: "How Netflix delivers content to 250M+ subscribers using Open Connect CDN, chaos engineering, and 500+ microservices."
order: 5
tags:
  - case-study
  - streaming
  - cdn
  - chaos-engineering
  - microservices
prerequisites: []
references:
  - title: "Netflix Open Connect Program"
    author: "Netflix"
    url: "https://openconnect.netflix.com/en/"
    type: "docs"
    description: "Official documentation of Netflix's custom CDN architecture."
  - title: "Netflix TechBlog"
    author: "Netflix"
    url: "https://netflixtechblog.com/"
    type: "blog"
    description: "Engineering blog covering Netflix's technical architecture."
  - title: "CDN Netflix Tech Stack: Open Connect and Home Caching Nodes"
    author: "BlazingCDN"
    url: "https://blog.blazingcdn.com/en-us/cdn-netflix-tech-stack-open-connect-home-caching-nodes"
    type: "article"
    description: "Technical analysis of Netflix's CDN infrastructure."
  - title: "Netflix Tech Stack Explained: CDN & Microservices"
    author: "VdoCipher"
    url: "https://www.vdocipher.com/blog/netflix-tech-stack-and-architecture/"
    type: "article"
    description: "Comprehensive overview of Netflix's technology choices."
  - title: "Netflix Research - Recommendations"
    author: "Netflix"
    url: "https://research.netflix.com/research-area/recommendations"
    type: "docs"
    description: "Netflix's recommendation system research."
related_knowledge:
  - slug: case-studies-tiktok-video
    title: "TikTok Video Delivery"
    lesson_number: 6
  - slug: case-studies-amazon-shopping-cart
    title: "Amazon Shopping Cart"
    lesson_number: 7
knowledge_refs:
  - slug: "tools-aws"
    title: "AWS"
  - slug: "patterns-microservices"
    title: "Microservices"
  - slug: "tools-docker"
    title: "Docker"
---

# Netflix Video Streaming

Netflix serves 250M+ subscribers across 190+ countries, streaming billions of hours of content monthly. Their architecture is a masterclass in custom infrastructure, chaos engineering, and ML-driven personalization.

## The Scale

- **250M+ subscribers** across 190+ countries
- **500+ microservices** on AWS
- **1,000+ ISP partnerships** for content delivery
- **95%+ cache hit ratio** on Open Connect appliances
- **15% of global internet bandwidth** during peak hours

## Open Connect CDN

Unlike traditional CDNs, Netflix built **Open Connect** — a private CDN optimized exclusively for video:

### Open Connect Appliances (OCAs)
Netflix provides specialized hardware at no charge directly inside ISP headends:
- **Storage OCAs:** 36 high-density HDDs, ~90 Gbps sustained egress
- **Flash OCAs:** NVMe SSDs (500TB usable), ~160 Gbps egress

### Proactive Fill Model
OCAs don't pull content on demand. Instead:
1. Central scheduling system predicts regional viewing demand
2. Content pushed to appliances during off-peak hours
3. **Cache-hit ratios exceed 95%** — virtually zero traffic touches AWS origin during peak

### Steering Service
When a user hits play, a steering service evaluates the client's resolver IP and OCA health telemetry to generate a ranked HTTPS manifest for optimal segment retrieval.

## Content Encoding Pipeline

### Per-Title & Shot-Based Encoding
Netflix pioneered encoding optimization at the content level:
- High-action movies get higher bitrates than static dialogue scenes
- Each video analyzed and transcoded with custom recipes

### VMAF (Video Multi-Method Assessment Fusion)
Netflix developed VMAF to measure perceptual video quality accurately — the core quality gate in automated encoding pipelines.

### AV1 Codec
Deployed on supported devices for significant bitrate reductions with improved quality.

## Microservices Architecture

### Edge Layer
- **Zuul 2:** Programmable API gateway built on Netty, managing routing, security, and identity propagation

### Container Management
- **Titus:** Netflix's custom container management platform (predates Kubernetes adoption)

### Data Layer
- **EVCache:** Memcached-based distributed caching for low-latency access
- **Cassandra:** Durable high-scale data storage
- **Mantis/Keystone:** Real-time streaming data processing

### Deployment
- **Spinnaker:** Global continuous delivery across multiple AWS regions

## Chaos Engineering

Netflix pioneered the practice of proactively injecting failures:

### Chaos Monkey & Simian Army
Randomly terminates VM instances in production, forcing engineers to build stateless, self-healing applications.

### FIT (Fault Injection Testing)
Injects precise runtime errors or latency into specific service requests.

### ChAP (Chaos Automation Platform)
Automates large-scale experiments with strict safety guardrails.

## Recommendation Engine

Evolved from collaborative filtering (Cinematch) to deep learning:
- Analyzes watch history, time of day, device type, search queries
- Generates personalized rows, artwork, and ranking for every user
- Real-time inference pipelines deliver customized homepages in milliseconds

## Key Design Decisions

1. **Build your own CDN** when you're 15% of internet bandwidth
2. **Chaos engineering** isn't optional at scale — it's survival
3. **Per-content encoding** optimizes quality vs. bandwidth better than one-size-fits-all
4. **Microservices** enable independent team velocity across 500+ services

## Lessons Learned

- **Custom infrastructure wins at extreme scale** — commercial CDNs couldn't meet Netflix's specific needs
- **Chaos engineering builds resilience** — you can't wait for failures to find weaknesses
- **Personalization is a competitive moat** — ML-driven recommendations drive 80% of content watched
- **Global deployment requires tooling** — Spinnaker and Titus enable safe worldwide rollouts

---

*References:*
1. Netflix, "Open Connect Program." [Link](https://openconnect.netflix.com/en/)
2. Netflix, "TechBlog." [Link](https://netflixtechblog.com/)
3. BlazingCDN, "CDN Netflix Tech Stack." [Link](https://blog.blazingcdn.com/en-us/cdn-netflix-tech-stack-open-connect-home-caching-nodes)
4. VdoCipher, "Netflix Tech Stack Explained." [Link](https://www.vdocipher.com/blog/netflix-tech-stack-and-architecture/)
5. Netflix, "Research - Recommendations." [Link](https://research.netflix.com/research-area/recommendations)
