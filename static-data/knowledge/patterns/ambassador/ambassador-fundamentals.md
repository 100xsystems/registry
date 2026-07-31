---
title: "Ambassador: Offload Client-Side Plumbing"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the ambassador intent"
  - "Identify client-side concerns it offloads"
  - "Compare with proxy and sidecar"
  - "Build a basic ambassador"
prerequisites:
  - "patterns/proxy"
  - "patterns/sidecar"
  - "principles/circuit-breaker"
knowledge_refs:
  - "patterns/ambassador"
---

# Ambassador: Offload Client-Side Plumbing

## The Problem

Every client of a remote service reimplements the same plumbing: retries, timeouts, caching, circuit breaking, logging. The ambassador is a co-located helper that performs these cross-cutting concerns on the client's behalf, so the client code stays thin.

Unlike a general proxy, the ambassador is service-specific and lives with the client — often as a library or a sidecar process in the same pod.

```go
// Ambassador: wraps the remote client with resilience, transparently
type Ambassador struct {
    client  *remote.Client
    breaker *circuit.Breaker
    cache   *cache.TTL
}

func (a *Ambassador) Get(ctx context.Context, key string) (Value, error) {
    if v, ok := a.cache.Get(key); ok {           // caching for the client
        return v, nil
    }
    var v Value
    err := a.breaker.Call(func() error {         // circuit breaking
        var e error
        for attempt := 0; attempt < 3; attempt++ {   // retries
            v, e = a.client.Get(ctx, key)
            if e == nil { break }
            backoff(attempt)
        }
        return e
    })
    if err != nil { return Value{}, err }
    a.cache.Set(key, v, 5*time.Minute)
    return v, nil
}
```

## Ambassador vs Proxy vs Sidecar

A proxy sits in front of a service (server-side). An ambassador sits with the client (client-side) and does work on its behalf. A sidecar is an ambassador packaged as a separate process next to the app — same intent, deployment choice.

## Practice: Build the Ambassador

Your app calls a search API and reimplements retries and caching at every call site.

**Task 1:** Identify the cross-cutting concerns repeated across call sites.

**Task 2:** Build the ambassador encapsulating retries, caching, and circuit breaking.

**Task 3:** Rewrite call sites to use it and measure the code removed.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why client-side plumbing belongs in an ambassador rather than the business code. Start with retries.

**Prompt 2 — Compare & Contrast:**
> Compare ambassador with sidecar, proxy, and service mesh. Where does each deployment model fit?

**Prompt 3 — Boundary Testing:**
> The ambassador's circuit breaker opens and the fallback must still serve something. Design the degraded response.

## Key Takeaways

- Ambassadors offload client-side cross-cutting concerns
- Clients stay thin; resilience lives in the helper
- Sidecar is the process-deployment form
- Fallbacks inside the ambassador define degraded behavior

## Further Reading

- [Ambassador Pattern — Microsoft Docs](https://learn.microsoft.com/en-us/azure/architecture/patterns/ambassador)
- [Sidecar Pattern — Microsoft Docs](https://learn.microsoft.com/en-us/azure/architecture/patterns/sidecar)
