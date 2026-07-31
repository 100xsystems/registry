---
title: "Advanced Composite: ASTs and Interpreters"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Build expression ASTs as composites"
  - "Interpret and compile ASTs recursively"
  - "Apply visitors for multiple operations"
  - "Design tree mutations safely"
prerequisites:
  []
knowledge_refs:
  - "patterns/composite"
---

# Advanced Composite: ASTs and Interpreters

## Expression Trees

An expression like (1 + 2) * 3 is a tree: a Multiply node with two children, one a binary Plus node. Evaluating and compiling are recursive walks over the composite — the interpreter pattern is composite applied to language.

```java
// Expression AST as a composite
interface Expr { int eval(); }

class Num implements Expr {
    private final int v;
    Num(int v) { this.v = v; }
    public int eval() { return v; }
}

class BinOp implements Expr {
    private final Expr l, r;
    private final char op;
    BinOp(char op, Expr l, Expr r) { this.op = op; this.l = l; this.r = r; }
    public int eval() {
        int a = l.eval(), b = r.eval();
        return switch (op) { case '+' -> a + b; case '*' -> a * b; default -> 0; };
    }
}
// (1 + 2) * 3
Expr tree = new BinOp('*', new BinOp('+', new Num(1), new Num(2)), new Num(3));
```

## Multiple Operations

An AST needs eval, print, typecheck, and optimize. Adding each as a visitor keeps the tree stable; adding a new node type touches all visitors. Choose: visitor (stable nodes, many ops) or methods (stable ops, many nodes) — the open-closed axis decides.

## Practice: Build a Mini-Interpreter

A calculator language: numbers, +, *, parentheses, and variables.

**Task 1:** Build the AST composite (Num, Var, BinOp).

**Task 2:** Add eval() with a symbol table and toPrefix() printing.

**Task 3:** Decide visitor vs methods for the next operation (typecheck) and justify.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain the visitor/methods trade-off using the expression-problem frame.

**Prompt 2 — Implementation Design:**
> Design an optimizer pass over an AST that folds constant subexpressions. Which composite walk does it need?

**Prompt 3 — Boundary Testing:**
> A huge AST (1M nodes) is evaluated recursively and overflows the stack. Design the iterative evaluation.

## Key Takeaways

- ASTs are composites — interpret and compile by walking
- Visitor vs methods is the expression problem
- Choose the axis you expect to grow
- Deep trees need iterative evaluation

## Further Reading

- [Interpreter — Refactoring Guru](https://refactoring.guru/design-patterns/interpreter)
- [Crafting Interpreters — Robert Nystrom](https://craftinginterpreters.com/)
