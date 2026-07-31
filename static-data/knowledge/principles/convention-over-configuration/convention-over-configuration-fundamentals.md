---
title: "Convention over Configuration: Defaults Beat Settings"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Define convention over configuration"
  - "List benefits: less code, faster onboarding, fewer mistakes"
  - "Identify good conventions in frameworks you know"
  - "Recognize when conventions become traps"
prerequisites:
  - "principles/kiss"
  - "principles/dry"
knowledge_refs:
  - "principles/convention-over-configuration"
---

# Convention over Configuration: Defaults Beat Settings

## The Principle

Convention over configuration means the framework (or codebase) provides sensible defaults, and configuration is needed only where you deviate. Rails' "convention over configuration", Spring Boot's autoconfiguration, and Next.js' file-based routing all follow it.

The result: a new engineer opening the codebase can predict where things live, because the structure follows the convention — not a sprawling config file that must be studied.

```text
Convention examples you already use:
  Next.js    : app/route/page.tsx  -> /route (no router config)
  Rails      : POST /users maps to UsersController#create
  Spring Boot: src/main/resources/application.yml, no XML
  Testing    : *.test.ts next to source (no test config)
```

## The Trade-Off

Conventions reduce decisions but hide behavior: a newcomer may not know a default exists or what it does. The fix is discoverability — the convention must be documented, consistent, and overridable.

A convention that requires violating it often is a bad convention. If 80% of cases deviate, invert the default.

## Practice: Audit Your Codebase

Look at your current project: folder structure, naming, config files, test placement.

**Task 1:** List three conventions already in use and where they are documented.

**Task 2:** Find one place where a file had to be discovered through config rather than convention. Would a rename or move fix it?

**Task 3:** Write a one-page conventions doc for a new teammate, covering naming, structure, and testing.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about when a framework convention helps versus hides. Start with a concrete framework default you like.

**Prompt 2 — Compare & Contrast:**
> Compare Rails (convention-first) with early Java EE XML-config (config-first). What developer-experience metrics differ?

**Prompt 3 — Boundary Testing:**
> A team has a strict convention but one module legitimately needs a different structure. Design the documented escape hatch that keeps the rest conventional.

## Key Takeaways

- Sensible defaults remove decisions and onboarding friction
- Discoverability and documentation make conventions safe
- Bad conventions are ones you must frequently violate
- Escape hatches must be explicit and documented

## Further Reading

- [Convention over Configuration — Wikipedia](https://en.wikipedia.org/wiki/Convention_over_configuration)
- [Rails Doctrine](https://rubyonrails.org/doctrine)
