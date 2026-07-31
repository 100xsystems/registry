---
title: "Advanced Open-Closed: Evolutionary APIs"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Design backward-compatible API evolution"
  - "Use additive change rules"
  - "Manage deprecation timelines"
  - "Keep contracts stable under growth"
prerequisites:
  []
knowledge_refs:
  - "principles/open-closed"
---

# Advanced Open-Closed: Evolutionary APIs

## Additive Evolution

A public API is closed the moment it ships: callers depend on it. Evolution rules are additive: add fields and endpoints, never remove or reinterpret. New optional fields are safe; changing a field's meaning breaks every caller.

```text
Additive API evolution rules:
  - Add new fields (optional), never remove existing ones
  - Add new endpoints, never change existing semantics
  - Unknown fields must be preserved (forward compatibility)
  - Version majors when a breaking change is unavoidable
  - Deprecate with a timeline: warn -> sunset -> remove (documented)
```

## Contracts That Last

The most successful contracts (HTTP, JSON, TCP) stayed open-closed through decades by additive evolution and tolerance: servers ignore unknown fields, clients degrade gracefully. Design your API the same way — forward compatibility is a feature.

## Practice: Evolve Without Breaking

A user API returns {id, name}. You must add email and eventually remove the deprecated phone field.

**Task 1:** Add email additively; verify old clients still parse the response.

**Task 2:** Design the phone deprecation: warn header, sunset date, migration docs.

**Task 3:** Add forward-compat handling: unknown fields preserved in proxy responses.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why removing a field is a breaking change even if you update all your own callers.

**Prompt 2 — Implementation Design:**
> Design a versioning policy for an internal API used by 40 services. What triggers a major bump, and how is the migration run?

**Prompt 3 — Boundary Testing:**
> A security fix requires changing a field's meaning (e.g., role to roles). Design the transition that stays additive.

## Key Takeaways

- APIs are closed the moment they ship
- Evolve additively; preserve unknown fields
- Deprecation is a timeline, not an event
- Forward compatibility makes contracts last

## Further Reading

- [API Evolution — Google API Design Guide](https://cloud.google.com/apis/design/compatibility)
- [Postel's Law (Be liberal in what you accept)](https://www.rfc-editor.org/rfc/rfc1122#page-18)
