---
title: "Advanced Ambassador: Smart Clients and Fallback Routing"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Build a smart client with adaptive routing"
  - "Add capability negotiation to the ambassador"
  - "Design multi-provider fallback routing"
  - "Keep ambassador state consistent"
prerequisites:
  []
knowledge_refs:
  - "patterns/ambassador"
---

# Advanced Ambassador: Smart Clients and Fallback Routing

## Smart Clients

An advanced ambassador measures backend health (latency, error rate) and routes requests adaptively: healthy instances get traffic, degraded ones get drained, and a region-wide failure triggers cross-region routing. This is client-side load balancing as an ambassador concern.

```go
// Adaptive routing in the ambassador: prefer healthy backends
func (a *Ambassador) pickBackend() *Backend {
    var best *Backend
    for _, b := range a.backends {
        if b.score() < threshold && (best == nil || b.score() > best.score()) {
            best = b
        }
    }
    if best == nil { return a.fallbackBackend() }  // cross-region fallback
    return best
}
```

## Capability Negotiation

Backends differ in capabilities (one supports bulk ops, another does not). The ambassador negotiates at connect time and exposes only what the chosen backend supports — the app sees one interface, the ambassador adapts to reality.

## Practice: Design the Smart Ambassador

Three backend clusters serve one API; one cluster degrades during a sale.

**Task 1:** Design the health scoring and the routing rule.

**Task 2:** Add the cross-region fallback with the capacity guard.

**Task 3:** Design the observability: routing decisions, drained backends, and fallback events.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain how an ambassador does client-side load balancing without the app knowing.

**Prompt 2 — Implementation Design:**
> Design capability negotiation between an app and a storage backend with two feature levels. What happens at connect, and what at runtime?

**Prompt 3 — Boundary Testing:**
> All backends degrade at once. Design the ambassador's final fallback and the alert that fires.

## Key Takeaways

- Smart ambassadors route around unhealthy backends
- Capability negotiation keeps one interface, many realities
- Cross-region fallback needs capacity guards
- Ambassador decisions must be observable

## Further Reading

- [Client-Side Load Balancing — Finagle](https://twitter.github.io/finagle/guide/Clients.html)
- [Envoy Upstream Selection](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/load_balancing/overview)
