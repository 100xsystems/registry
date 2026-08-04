---
slug: patterns-api-gateway
title: "API Gateway & Rate Limiting"
description: "Single entry point for APIs, request routing, authentication, rate limiting, and API management."
order: 13
tags:
  - system-design
  - patterns
  - api-gateway
  - rate-limiting
  - authentication
  - microservices
prerequisites:
  - building-blocks-load-balancers
  - fundamentals-scalability
references:
  - title: "API Gateway Pattern"
    author: "Microsoft Azure"
    url: "https://learn.microsoft.com/en-us/azure/architecture/patterns/gateway-routing"
    type: "docs"
    description: "Official Microsoft guide to API gateway patterns."
  - title: "System Design: Rate Limiter"
    author: "ByteByteGo"
    url: "https://blog.bytebytego.com/p/rate-limiter"
    type: "article"
    description: "Comprehensive rate limiting strategies."
  - title: "Kong API Gateway Documentation"
    author: "Kong"
    url: "https://docs.konghq.com/gateway/"
    type: "docs"
    description: "Open-source API gateway documentation."
  - title: "AWS API Gateway Documentation"
    author: "AWS"
    url: "https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html"
    type: "docs"
    description: "AWS managed API gateway."
  - title: "Rate Limiting Algorithms"
    author: "Cloudflare"
    url: "https://www.cloudflare.com/learning/bots/what-is-rate-limiting/"
    type: "article"
    description: "Different rate limiting algorithms explained."
related_knowledge:
  - slug: building-blocks-load-balancers
    title: "Load Balancers"
    lesson_number: 5
  - slug: patterns-circuit-breaker
    title: "Circuit Breaker & Resilience"
    lesson_number: 12
  - slug: fundamentals-scalability
    title: "Scalability & Performance"
    lesson_number: 2
knowledge_refs:
  - slug: "tools-nginx"
    title: "NGINX"
  - slug: "tools-aws"
    title: "AWS"
  - slug: "patterns-authentication"
    title: "Authentication"
---

# API Gateway & Rate Limiting

An API Gateway is the single entry point for all client requests, providing routing, authentication, rate limiting, and other cross-cutting concerns. Rate limiting protects services from overload.

## API Gateway Responsibilities

### Request Routing
Direct requests to the appropriate microservice:
```
Client → API Gateway
        → /users → User Service
        → /orders → Order Service
        → /payments → Payment Service
```

### Authentication & Authorization
Verify identity and permissions before forwarding:
```
Client → Gateway → Validate JWT → Check permissions → Forward to service
```

### Rate Limiting
Control request frequency per client/user/IP.

### Request/Response Transformation
- Add/remove headers
- Protocol translation (REST → gRPC)
- Response aggregation (BFF pattern)

### SSL Termination
Handle TLS encryption/decryption once at the gateway.

## Rate Limiting Algorithms

### Token Bucket
Tokens added at fixed rate, each request consumes one:
```
Bucket: [token] [token] [token] [token]
Request → consumes token → allowed
Empty bucket → rejected
```
**Pros:** Allows bursts, smooth rate limiting.

### Fixed Window Counter
Count requests in fixed time windows:
```
Window: [1 minute]
Counter: 0/100
Request → increment → allowed if < 100
Window resets → counter resets
```
**Pros:** Simple. **Cons:** Boundary burst problem (100 requests at 11:59:59 + 100 at 12:00:00 = 200 in 2 seconds).

### Sliding Window Log
Store timestamp of each request, count within window:
```
Log: [12:00:01, 12:00:15, 12:00:30, ...]
Count requests in last 60 seconds → allow if < 100
```
**Pros:** Accurate. **Cons:** Memory intensive.

### Sliding Window Counter
Combines fixed window with proportional weighting:
```
Current window: 80 requests
Previous window: 60 requests
Weighted count = 80 + 60 × (elapsed/60) = 80 + 60 × 0.5 = 110
```
**Pros:** Accurate, memory efficient.

## Rate Limiting Responses

When limit exceeded, return clear information:
```http
HTTP/1.1 429 Too Many Requests
Retry-After: 30
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1640000060
```

## Distributed Rate Limiting

At scale, rate limiting must work across multiple gateway instances:

### Centralized Counter (Redis)
```
INCR rate:user:123
EXPIRE rate:user:123 60
```
Simple but single point of failure.

### Local + Sync
Each gateway tracks locally, periodically syncs:
- Fast local checks
- Eventual consistency for global limits

### Consistent Hashing
Route same user to same gateway:
- Natural local rate limiting
- No cross-instance coordination needed

## Popular API Gateways

| Gateway | Type | Features |
|---|---|---|
| **Kong** | Open-source | Plugin ecosystem, OAuth, rate limiting |
| **AWS API Gateway** | Managed | Lambda integration, throttling |
| **Envoy** | Open-source | Service mesh, L7 proxy |
| **NGINX** | Open-source | Reverse proxy, load balancing |
| **Apigee** | Google | Enterprise API management |

---

*References:*
1. Microsoft Azure, "API Gateway Pattern." [Link](https://learn.microsoft.com/en-us/azure/architecture/patterns/gateway-routing)
2. ByteByteGo, "System Design: Rate Limiter." [Link](https://blog.bytebytego.com/p/rate-limiter)
3. Kong, "API Gateway Documentation." [Link](https://docs.konghq.com/gateway/)
4. AWS, "API Gateway." [Link](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
5. Cloudflare, "Rate Limiting Algorithms." [Link](https://www.cloudflare.com/learning/bots/what-is-rate-limiting/)
