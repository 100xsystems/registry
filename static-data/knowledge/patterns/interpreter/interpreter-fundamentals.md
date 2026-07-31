---
title: "Interpreter: A Grammar for Your Problem"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the interpreter intent"
  - "Model a grammar with an AST"
  - "Evaluate expressions recursively"
  - "Know when a DSL beats configuration"
prerequisites:
  - "patterns/composite"
  - "patterns/visitor"
knowledge_refs:
  - "patterns/interpreter"
---

# Interpreter: A Grammar for Your Problem

## The Problem

When business rules or queries recur in many shapes (filter expressions, pricing rules, search strings), hand-coding every combination is unmaintainable. The interpreter defines a small grammar, parses sentences into an abstract syntax tree, and evaluates the tree — new rules become new sentences, not new code.

```python
# Interpreter: arithmetic expressions as an AST
class Expr:
    def eval(self, env): raise NotImplementedError

class Num(Expr):
    def __init__(self, v): self.v = v
    def eval(self, env): return self.v

class Add(Expr):
    def __init__(self, l, r): self.l, self.r = l, r
    def eval(self, env): return self.l.eval(env) + self.r.eval(env)

class Var(Expr):
    def __init__(self, name): self.name = name
    def eval(self, env): return env[self.name]

# (a + 5) + 10  ==  Add(Add(Var('a'), Num(5)), Num(10))
expr = Add(Add(Var('a'), Num(5)), Num(10))
print(expr.eval({'a': 2}))    # 17
```

## Grammar and AST

A grammar (E ::= E + E | number | variable) defines valid sentences; parsing turns text into the tree; evaluation walks it. The pattern shines for small, stable grammars. Large or evolving languages need a real parser generator or a full compiler pipeline instead.

## Practice: Build the Rule Engine

A pricing system needs rules like "if country == FR then price * 1.2" without redeploying.

**Task 1:** Define the grammar for conditions and actions.

**Task 2:** Build the parser and the AST nodes.

**Task 3:** Evaluate a pricing rule against sample orders and add a new rule without code changes.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about how a grammar becomes an AST and the AST becomes an evaluation. Start with one operator.

**Prompt 2 — Compare & Contrast:**
> Compare interpreter with strategy and with a configuration file. When is a DSL actually worth it?

**Prompt 3 — Boundary Testing:**
> A rule references an unknown variable. Design the evaluation-time error and the validation pass that catches it before execution.

## Key Takeaways

- Interpreter turns a grammar into an evaluable AST
- New behaviors become new sentences, not new code
- Evaluation is recursive tree walking
- Small stable grammars only — otherwise use a parser generator

## Further Reading

- [Interpreter — Refactoring Guru](https://refactoring.guru/design-patterns/interpreter)
- [Crafting Interpreters (free book)](https://craftinginterpreters.com/)
