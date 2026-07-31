---
title: "Ambassador in Production: Sidecars and Meshes"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Deploy an ambassador as a sidecar"
  - "Understand mesh proxies as ambassadors"
  - "Version the ambassador with the client"
  - "Monitor ambassador health"
prerequisites:
  []
knowledge_refs:
  - "patterns/ambassador"
---

# Ambassador in Production: Sidecars and Meshes

## Sidecar Deployment

The ambassador as a sidecar container runs in the same pod as the app, sharing localhost. The app calls the sidecar; the sidecar talks to the remote service with all the resilience logic. Language-independent, hot-updatable without rebuilding the app.

```yaml
# Sidecar ambassador in a Kubernetes pod
containers:
  - name: app
    image: my-app
    command: ["/app", "--search=http://localhost:9090"]
  - name: ambassador
    image: search-ambassador:1.4   # retries, circuit breaker, cache
    ports:
      - containerPort: 9090        # app calls localhost:9090
# Update the ambassador image without rebuilding the app.
```

## Service Mesh as Ambassador

A service mesh data plane (Envoy, Linkerd) is an ambassador deployed everywhere: it injects retries, timeouts, mTLS, and circuit breaking into every service-to-service call without application changes. The mesh centralizes the ambassador pattern across the platform.

## Practice: Choose the Deployment

Your platform has 12 services calling a flaky partner API.

**Task 1:** Compare: in-process library ambassador vs sidecar vs mesh proxy.

**Task 2:** Pick one for the flaky partner and justify with update and isolation needs.

**Task 3:** Design the monitoring: how do you see ambassador retry and breaker events per service?

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me the trade-offs between an in-process ambassador and a sidecar process. Ask me about updates and failure modes.

**Prompt 2 — Implementation Design:**
> Design a mesh proxy configuration for a partner API: retries, timeout budget, circuit breaker, and observability. What are the exact settings?

**Prompt 3 — Boundary Testing:**
> The sidecar crashes but the app is fine. Design the degraded mode (fail open, direct call) and its alert.

## Key Takeaways

- Sidecars deploy ambassadors without app rebuilds
- Service meshes centralize the pattern platform-wide
- Ambassador updates are independent of the app
- Ambassador health is a first-class signal

## Further Reading

- [Sidecar Pattern — Microsoft Docs](https://learn.microsoft.com/en-us/azure/architecture/patterns/sidecar)
- [What is a Service Mesh — Istio](https://istio.io/latest/about/service-mesh/)
