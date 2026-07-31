---
title: "Proxy in Production: Reverse Proxies and Gateways"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Describe the reverse proxy"
  - "Use an API gateway proxy"
  - "Apply caching and routing proxies"
  - "Secure through a proxy"
prerequisites:
  []
knowledge_refs:
  - "patterns/proxy"
---

# Proxy in Production: Reverse Proxies and Gateways

## Reverse Proxies

A reverse proxy sits in front of services: it terminates connections, routes requests, terminates TLS, caches responses, and load balances. Nginx and Envoy are the workhorses. The proxy owns the edge — origins stay hidden and simpler.

```nginx
# Nginx as a reverse proxy with caching
http {
  proxy_cache_path /var/cache/nginx keys_zone=api:10m;

  server {
    listen 443 ssl;
    ssl_certificate     /etc/nginx/tls/fullchain.pem;

    location /api/ {
        proxy_pass         http://backend-svc:8080;
        proxy_cache        api;
        proxy_cache_valid  200 60s;      # cache 200s for a minute
        proxy_set_header   X-Real-IP $remote_addr;
    }
  }
}
# The proxy handles TLS, routing, and caching so the backend
# never sees raw traffic or duplicate work.
```

## Gateways and Meshes

An API gateway is a reverse proxy with policy: auth, rate limiting, and routing by client type. A service mesh data plane proxies every service-to-service call, adding mTLS, retries, and observability. The proxy is where cross-cutting edge concerns live.

## Practice: Design the Edge

An API serves mobile and web clients; it needs TLS, auth, rate limits, and caching.

**Task 1:** Map each concern to the right proxy layer (gateway, CDN, mesh).

**Task 2:** Configure the routing and the caching rules per client type.

**Task 3:** Design the failure mode: gateway down vs backend down.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why the edge proxy owns TLS, caching, and routing and what the origin keeps.

**Prompt 2 — Implementation Design:**
> Design an API gateway config: auth per route, rate limits per client, cache TTLs. Where do you put each rule?

**Prompt 3 — Boundary Testing:**
> The gateway caches a response that later changes. Design the cache-invalidation path (purge or short TTL).

## Key Takeaways

- Reverse proxies own the edge: TLS, routing, caching
- API gateways add policy per client
- Service meshes proxy service-to-service calls
- Cache invalidation is a gateway contract

## Further Reading

- [Nginx — reverse proxy docs](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/)
- [What is a Service Mesh — Istio](https://istio.io/latest/about/service-mesh/)
