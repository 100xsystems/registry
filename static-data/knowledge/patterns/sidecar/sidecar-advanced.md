---
title: "Advanced Sidecar: eBPF, WASM, and Edge Sidecars"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Accelerate sidecars with eBPF"
  - "Extend sidecars with WASM"
  - "Run sidecars at the edge"
  - "Choose the sidecar shape"
prerequisites:
  []
knowledge_refs:
  - "patterns/sidecar"
---

# Advanced Sidecar: eBPF, WASM, and Edge Sidecars

## Acceleration and Extension

The sidecar hop is the mesh's main cost. eBPF moves filtering and routing into the kernel, reducing hops; WASM lets operators extend Envoy sidecars with per-tenant policy without shipping a new proxy. The sidecar is becoming a pluggable runtime, not a fixed appliance.

```text
Sidecar evolution:
  Classic: Envoy sidecar, fixed feature set, JSON config
  eBPF (Cilium, Istio ambient): move L3/L4 filtering into the
    kernel — fewer user-space hops, lower latency and CPU
  WASM: compile policy/authz filters to WASM and load them into
    the sidecar at runtime — per-tenant logic without a new build
  Ambient/zero-sidecar: a per-node shared proxy instead of
    per-pod — less overhead, coarser isolation
  Edge sidecars: the same pattern at the edge (CDN worker,
    gateway) running auth, geolocation, and transformation
The design question is always the same: what support does the
app need, and where is the right place for that hop?
```

## Choosing the Shape

Per-pod sidecar: strongest isolation, highest overhead. Per-node ambient: lower cost, coarser isolation. In-process library: lowest overhead, but language-coupled. The trade is isolation vs cost vs coupling — and the answer shifts as the platform matures.

## Practice: Choose the Data Plane

A high-QPS platform (100k RPS) finds the sidecar hop costs 10% of its latency budget.

**Task 1:** Measure the sidecar overhead on a hot path.

**Task 2:** Compare per-pod, ambient, and eBPF data planes.

**Task 3:** Pick one and justify with the isolation and latency numbers.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain the isolation-vs-overhead trade across sidecar shapes.

**Prompt 2 — Implementation Design:**
> Design a WASM authz filter for a multi-tenant gateway: how does per-tenant policy load at runtime?

**Prompt 3 — Boundary Testing:**
> An eBPF program crashes the kernel. Design the fallback to the user-space path and the rollout guard.

## Key Takeaways

- eBPF and WASM make sidecars faster and pluggable
- Ambient shapes trade isolation for overhead
- Edge sidecars apply the pattern at the edge
- Shape choice follows isolation and latency budgets

## Further Reading

- [Istio — ambient mesh](https://istio.io/latest/blog/2022/introducing-ambient-mesh/)
- [Envoy — WASM filters](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/wasm/v3/wasm)
