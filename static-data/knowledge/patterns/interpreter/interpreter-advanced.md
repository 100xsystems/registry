---
title: "Advanced Interpreter: Typing, Optimization, and Compilation"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Add a type-checking pass"
  - "Compile the AST to bytecode"
  - "Optimize hot evaluation paths"
  - "Support incremental re-evaluation"
prerequisites:
  []
knowledge_refs:
  - "patterns/interpreter"
---

# Advanced Interpreter: Typing, Optimization, and Compilation

## Beyond Tree Walking

A plain tree-walking interpreter is simple but slow for hot paths. Compiling the AST to bytecode — linear instructions a stack machine executes — removes per-node dispatch overhead. Constant folding and common subexpression elimination shrink the instruction stream.

```python
# Bytecode for Add(Add(Var('a'), Num(5)), Num(10))
#   LOAD_VAR a
#   PUSH 5
#   ADD
#   PUSH 10
#   ADD
# Executing a flat instruction list beats virtual dispatch on the AST.
def run(code, env):
    stack = []
    for op, arg in code:
        if op == 'LOAD_VAR': stack.append(env[arg])
        elif op == 'PUSH': stack.append(arg)
        elif op == 'ADD': stack.append(stack.pop() + stack.pop())
    return stack[0]
```

## Typing and Incremental Evaluation

A static pass checks types before evaluation: unknown fields, mismatched operators, impossible comparisons. Incremental evaluation re-runs only the affected sub-expressions when inputs change — the engine keeps per-node caches and invalidates along the path to the root, which matters when rules evaluate against thousands of changing records.

## Practice: Compile the Filter

A rules engine evaluates 1M rules/minute against streaming events and is CPU-bound.

**Task 1:** Compile the AST to a flat instruction list and benchmark against tree walking.

**Task 2:** Add constant folding for static sub-expressions.

**Task 3:** Design incremental re-evaluation when only some event fields change.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why bytecode beats tree walking for hot interpreters.

**Prompt 2 — Implementation Design:**
> Design a rule engine that type-checks rules at deploy time and compiles them to bytecode. What are the deploy-time checks?

**Prompt 3 — Boundary Testing:**
> A rule is correct on Monday but the data schema changes Tuesday. Design the schema-versioned type check and the fail-deploy path.

## Key Takeaways

- Bytecode compilation removes AST dispatch overhead
- Type checking moves errors from runtime to deploy
- Constant folding shrinks the instruction stream
- Incremental evaluation saves work on changing inputs

## Further Reading

- [Crafting Interpreters — Chunks of Bytecode](https://craftinginterpreters.com/a-bytecode-virtual-machine.html)
- [Expression rules engines — Drools](https://www.drools.org/)
