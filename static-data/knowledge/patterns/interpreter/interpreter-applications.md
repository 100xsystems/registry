---
title: "Interpreter in Production: Query Languages and Rules Engines"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design a filter DSL"
  - "Add validation and typing"
  - "Sandbox the evaluator"
  - "Compile hot paths"
prerequisites:
  []
knowledge_refs:
  - "patterns/interpreter"
---

# Interpreter in Production: Query Languages and Rules Engines

## Filter DSLs

Products expose user-facing filter languages (Jira JQL, GitHub search, mail filters). A tokenizer + recursive-descent parser + typed evaluator is the classic interpreter pipeline. The evaluator runs against a context (the issue, the pull request) and returns a boolean — queries are data, not code.

```typescript
// A tiny filter DSL: tag:urgent AND (priority:high OR age:old)
// Tokenize -> parse -> evaluate against a record
function evalFilter(ast: Node, ctx: Record<string, string[]>): boolean {
    switch (ast.kind) {
        case 'and': return evalFilter(ast.left, ctx) && evalFilter(ast.right, ctx);
        case 'or':  return evalFilter(ast.left, ctx) || evalFilter(ast.right, ctx);
        case 'field': {
            const vals = ctx[ast.name] ?? [];
            return ast.op === ':' ? vals.includes(ast.value) : true;
        }
    }
}
// The filter is stored as a string, parsed once, evaluated per item.
// New filter operators = new AST node + evaluator branch, both tested.
```

## Validation and Sandboxing

User-authored expressions must be validated before use (unknown fields, type mismatches) and evaluated safely: no side effects, bounded depth and time, and no access to the host environment. A billion-laughs-style deep expression must be depth-limited, and evaluation must be pure.

## Practice: Design the Search DSL

A support tool needs search like "status:open AND (assignee:me OR priority:high)".

**Task 1:** Define the grammar, tokens, and precedence.

**Task 2:** Build the recursive-descent parser and evaluator.

**Task 3:** Add validation (unknown fields) and depth limiting, then fuzz the parser.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me the pipeline: tokenize, parse, validate, evaluate. Ask me where each failure mode appears.

**Prompt 2 — Implementation Design:**
> Design a workflow rules engine where rules are interpreted data. How do rules version, migrate, and get validated at deploy?

**Prompt 3 — Boundary Testing:**
> A user submits a 10,000-token query. Design the limits (depth, tokens, time) and the error surface.

## Key Takeaways

- Production interpreters power JQL-style filter DSLs
- Validation and sandboxing are mandatory for user input
- Pure evaluation keeps the interpreter safe
- Depth and time limits stop pathological expressions

## Further Reading

- [Crafting Interpreters (free book)](https://craftinginterpreters.com/)
- [ANTLR (parser generator)](https://www.antlr.org/)
