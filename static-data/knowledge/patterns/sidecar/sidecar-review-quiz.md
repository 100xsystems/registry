---
title: "Sidecar: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate sidecar concepts"
  - "Operate meshes"
  - "Choose shapes"
prerequisites:
  []
knowledge_refs:
  - "patterns/sidecar"
---

# Sidecar: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: A sidecar is? (A: a co-located helper process / B: a database / C: a UI)
- Q2: The app talks to the sidecar over? (A: localhost / B: the internet / C: the bus)
- Q3: A mesh sidecar adds? (A: mTLS and routing / B: storage / C: rendering)
- Q4: True or false: sidecars upgrade independently of the app.
- Q5: eBPF sidecars move work? (A: into the kernel / B: to the client / C: to the cloud)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A 30-service platform wants mTLS and canary routing without app changes. Design the mesh adoption and its rollout.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why a separate process is worth the extra ops burden.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Co-located, decoupled, independently upgradeable
- The mesh made sidecars a platform primitive
