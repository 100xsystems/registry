---
slug: building-blocks-load-balancers
title: "Load Balancers"
description: "How load balancers distribute traffic across servers — Layer 4 vs Layer 7, algorithms, and health checks."
order: 5
tags:
  - system-design
  - building-blocks
  - load-balancers
  - networking
  - high-availability
prerequisites:
  - fundamentals-scalability
references:
  - title: "System Design Interview – An Insider's Guide"
    author: "Alex Xu"
    url: "https://bytebytego.com/"
    type: "book"
    description: "Load balancer concepts in the context of system design."
  - title: "NGINX Load Balancing Guide"
    author: "NGINX"
    url: "https://www.nginx.com/resources/glossary/load-balancing/"
    type: "docs"
    description: "Practical guide to load balancing algorithms and configuration."
  - title: "AWS Elastic Load Balancing"
    author: "AWS"
    url: "https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html"
    type: "docs"
    description: "How AWS implements load balancing at scale."
  - title: "Envoy Proxy Architecture"
    author: "Envoy"
    url: "https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/arch_overview"
    type: "docs"
    description: "Modern service mesh load balancing architecture."
  - title: "System Design: Load Balancer"
    author: "ByteByteGo"
    url: "https://blog.bytebytego.com/p/load-balancer"
    type: "article"
    description: "Visual breakdown of load balancing strategies."
related_knowledge:
  - slug: building-blocks-caching
    title: "Caching"
    lesson_number: 6
  - slug: building-blocks-cdn
    title: "CDNs"
    lesson_number: 9
  - slug: fundamentals-scalability
    title: "Scalability & Performance"
    lesson_number: 2
knowledge_refs:
  - slug: "patterns-consistent-hashing"
    title: "Consistent Hashing"
  - slug: "tools-nginx"
    title: "NGINX"
  - slug: "tools-aws"
    title: "AWS"
---

# Load Balancers

A load balancer distributes incoming traffic across multiple servers, ensuring no single server is overwhelmed and providing high availability through redundancy.

## Layer 4 vs Layer 7 Load Balancing

### Layer 4 (Transport Layer)
Routes based on IP address and TCP/UDP port:
- **Fast:** No inspection of request content
- **Simple:** Just forwards packets
- **Use case:** Database connections, gaming servers, TCP-based protocols

### Layer 7 (Application Layer)
Routes based on HTTP headers, URLs, cookies, or content:
- **Smart:** Can route based on request content
- **SSL termination:** Handles encryption/decryption once
- **Use case:** Web applications, API routing, content-based routing

## Load Balancing Algorithms

### Round Robin
Distributes requests sequentially across servers:
```
Request 1 → Server A
Request 2 → Server B
Request 3 → Server C
Request 4 → Server A (wraps around)
```
**Pros:** Simple, even distribution. **Cons:** Ignores server load.

### Least Connections
Routes to the server with fewest active connections:
```
Server A: 5 connections → Next request goes here
Server B: 12 connections
Server C: 8 connections
```
**Pros:** Adapts to server load. **Cons:** Requires tracking connection counts.

### IP Hash
Uses client IP to consistently route to the same server:
```
hash(client_ip) % num_servers → server_index
```
**Pros:** Session affinity without sticky sessions. **Cons:** Uneven distribution if IP distribution is skewed.

### Weighted Round Robin
Servers get proportional traffic based on capacity:
```
Server A (8 cores): weight 4 → 40% of traffic
Server B (4 cores): weight 2 → 20% of traffic
Server C (4 cores): weight 2 → 20% of traffic
Server D (2 cores): weight 1 → 10% of traffic
```

### Least Response Time
Routes to the server with lowest latency and fewest connections:
**Pros:** Best user experience. **Cons:** More complex to implement.

## Health Checks

Load balancers continuously probe servers to detect failures:
- **TCP check:** Is the port open?
- **HTTP check:** Does `/health` return 200?
- **Custom check:** Does the service respond correctly?

Unhealthy servers are removed from rotation until they recover.

## Load Balancer Architecture

### Single Load Balancer
Simple but single point of failure:
```
Client → LB → [Server A, Server B, Server C]
```

### Redundant Load Balancers
Active-passive or active-active pairs:
```
Client → LB1 (active) → Servers
       → LB2 (passive) → (takes over if LB1 fails)
```

### Multi-Tier Load Balancing
DNS-level → Global LB → Regional LB → Application servers:
```
Client → DNS → Global LB (geographic routing)
             → Regional LB1 → App Servers (US-East)
             → Regional LB2 → App Servers (EU-West)
```

## Common Load Balancers

| Tool | Type | Use Case |
|---|---|---|
| **NGINX** | Layer 7 | Web applications, reverse proxy |
| **HAProxy** | Layer 4/7 | High-performance TCP/HTTP |
| **AWS ALB** | Layer 7 | Managed HTTP/HTTPS |
| **AWS NLB** | Layer 4 | Managed TCP/UDP |
| **Envoy** | Layer 7 | Service mesh, microservices |
| **Cloudflare** | Layer 7 | Global CDN + load balancing |

---

*References:*
1. Alex Xu, *System Design Interview.* [Link](https://bytebytego.com/)
2. NGINX, "Load Balancing Guide." [Link](https://www.nginx.com/resources/glossary/load-balancing/)
3. AWS, "Elastic Load Balancing." [Link](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)
4. Envoy, "Architecture Overview." [Link](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/arch_overview)
5. ByteByteGo, "System Design: Load Balancer." [Link](https://blog.bytebytego.com/p/load-balancer)
