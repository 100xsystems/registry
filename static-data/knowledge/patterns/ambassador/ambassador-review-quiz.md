---
title: "Ambassador: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate ambassador concepts"
  - "Choose deployment models"
  - "Design smart clients"
prerequisites:
  []
knowledge_refs:
  - "patterns/ambassador"
---

# Ambassador: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: An ambassador offloads? (A: server-side rendering / B: client-side plumbing / C: database writes)
- Q2: A sidecar is an ambassador? (A: in a separate process / B: in the database / C: in the UI)
- Q3: A service mesh data plane is? (A: an ambassador everywhere / B: a database / C: a UI framework)
- Q4: True or false: the app should reimplement retries at every call site.
- Q5: Smart ambassadors route based on? (A: backend health / B: user name / C: cache size)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A partner API fails often; 6 services call it. Design the ambassador strategy (library vs sidecar vs mesh) with the exact resilience settings.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why client-side resilience should be centralized, not copy-pasted.

## Key Takeaways

- Q1: B; Q2: A; Q3: A; Q4: false; Q5: A
- Ambassadors centralize client resilience
- Sidecars and meshes operationalize the pattern
