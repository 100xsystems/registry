---
title: "Visitor in Production: Compilers and Analyzers"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Describe compiler visitors"
  - "Write linter visitors"
  - "Compose visitors"
  - "Handle tree context"
prerequisites:
  []
knowledge_refs:
  - "patterns/visitor"
---

# Visitor in Production: Compilers and Analyzers

## Compilers as Visitors

Every compiler, linter, and formatter walks an AST with visitors: type checking, lint rules, codegen, and formatting are separate visitors over a stable AST. ESLint's rules are visitors; Babel's transforms are visitors; so is the TypeScript checker. The AST stays stable; the toolchain's operations grow as visitors.

```javascript
// ESLint rule as a visitor — operation over a stable AST
module.exports = {
  meta: { docs: { description: 'no console.log' } },
  create(context) {
    return {
      CallExpression(node) {            // visitor for one node type
        if (node.callee.type === 'MemberExpression' &&
            node.callee.object.name === 'console' &&
            node.callee.property.name === 'log') {
          context.report({ node, message: 'no console.log' });
        }
      },
      // Add a visitor per node type per rule. The AST never
      // changes; the rule set grows as new visitors.
    };
  },
};
```

## Context and Composition

Visitors often need context: parent pointers, scope chains, import tables. A walker carries the context and passes it to visitors, or visitors thread state through the traversal. Composing visitors (run several in one pass) needs a composite visitor — itself a visitor over the same structure.

## Practice: Write the Analyzer

A linter must find unused variables and forbid arrow-function abuse in one pass.

**Task 1:** Design the visitor set and the shared context.

**Task 2:** Implement the two rules as visitors.

**Task 3:** Compose them into one pass and verify both report correctly.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why compilers are visitor ecosystems over stable ASTs.

**Prompt 2 — Implementation Design:**
> Design a formatter visitor: indent, line width, and comments over an AST. Where does the context live?

**Prompt 3 — Boundary Testing:**
> A visitor needs parent scope but the walker does not provide it. Design the context fix that does not break other visitors.

## Key Takeaways

- Compilers, linters, and formatters are visitor ecosystems
- Rules and transforms are visitors over stable ASTs
- Context (scope, parents) is threaded through the walk
- Composite visitors run several operations in one pass

## Further Reading

- [ESLint — custom rules](https://eslint.org/docs/latest/extend/custom-rules)
- [Babel — plugin handbook (visitors)](https://github.com/jamiebuilds/babel-handbook)
