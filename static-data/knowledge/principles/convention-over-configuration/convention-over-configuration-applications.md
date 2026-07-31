---
title: "Conventions in Production: Structure and Onboarding"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design folder and naming conventions for a monorepo"
  - "Make conventions enforceable with tooling"
  - "Balance convention with flexibility for outliers"
  - "Measure onboarding time as a convention metric"
prerequisites:
  []
knowledge_refs:
  - "principles/convention-over-configuration"
---

# Conventions in Production: Structure and Onboarding

## Enforceable Conventions

Conventions enforced by tooling (linters, formatters, generators, CI checks) are the only reliable ones. A convention documented in a wiki decays; one enforced by a lint rule or a scaffolding CLI does not.

```text
Tooling that enforces convention:
  eslint + prettier        : style & patterns
  folder-lint / structure  : repo layout rules
  codegen / scaffolder     : new modules follow the template
  review bots              : flag deviations automatically
```

## The Monorepo Convention Set

A well-conventional monorepo answers instantly: where is the service, where are its tests, where do shared types live, how is it deployed. Every new module is a clone of the template, so "how do I add X?" has one answer.

The cost: outliers need justification, and structural refactors touch everything at once. Versioned conventions (a migration plan for the convention itself) keep it from fossilizing.

## Practice: Design the Module Template

Your team adds 2 new microservices per month and onboarding takes 3 weeks.

**Task 1:** Design the canonical service folder structure (src, tests, config, docs, CI).

**Task 2:** Write the scaffolding command that generates it, and the lint rules that keep it intact.

**Task 3:** Define the one-page template doc a new service must follow, and where it lives.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why "documented in the wiki" is not enough for a convention and what enforcement layers exist. Ask me to rank them by reliability.

**Prompt 2 — Implementation Design:**
> Design a versioned conventions doc: how do you propose, review, and migrate a breaking convention change across a monorepo?

**Prompt 3 — Boundary Testing:**
> One team's service needs a nonstandard structure (e.g., a long-running worker). Design the documented exception process.

## Key Takeaways

- Tooling enforcement beats documentation
- Templates make "how do I add X" have one answer
- Exceptions need a documented, reviewable process
- Conventions themselves need versioning and migration plans

## Further Reading

- [Monorepo Conventions — Nx](https://nx.dev/concepts/why-monorepos)
- [Folder Structure Best Practices](https://www.martinfowler.com/articles/web-security-basics.html)
