---
title: "Interpreter: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate interpreter concepts"
  - "Design DSLs and grammars"
  - "Optimize evaluation"
prerequisites:
  []
knowledge_refs:
  - "patterns/interpreter"
---

# Interpreter: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: An interpreter evaluates? (A: a parse tree / B: compiled binaries / C: YAML only)
- Q2: New rules in a DSL mean? (A: new code / B: new sentences / C: new servers)
- Q3: User-authored expressions must be? (A: sandboxed / B: trusted / C: ignored)
- Q4: True or false: bytecode beats tree walking on hot paths.
- Q5: Type checking at parse time moves errors to? (A: deploy time / B: runtime / C: users)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A support tool needs a query language over tickets. Design the grammar, the evaluator, and the sandbox limits.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer when a DSL is worth building and when a config file is enough.

## Key Takeaways

- Q1: A; Q2: B; Q3: A; Q4: true; Q5: A
- Interpreter = grammar + AST + evaluator
- Validate, sandbox, then compile hot paths
