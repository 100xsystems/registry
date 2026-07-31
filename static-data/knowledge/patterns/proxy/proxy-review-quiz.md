---
title: "Proxy: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate proxy concepts"
  - "Design the edge"
  - "Measure proxy cost"
prerequisites:
  []
knowledge_refs:
  - "patterns/proxy"
---

# Proxy: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: A proxy implements? (A: the same interface / B: a new interface / C: no interface)
- Q2: A lazy proxy defers? (A: construction / B: rendering / C: deletion)
- Q3: A reverse proxy terminates? (A: connections and TLS / B: the database / C: the UI)
- Q4: True or false: an API gateway is a reverse proxy with policy.
- Q5: Copy-on-write proxies copy? (A: on first mutation / B: on read / C: never)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A microservices API needs TLS, auth, rate limits, and caching at the edge. Design the proxy layers and their responsibilities.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer the difference between controlling access and changing the interface.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Proxy = same interface, controlled access
- The edge is where proxies earn their keep
