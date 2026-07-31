---
title: "Advanced Template Method: Enforcing Invariants and Contracts"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Enforce step contracts"
  - "Assert invariants in the skeleton"
  - "Design hook ordering"
  - "Audit subclass behavior"
prerequisites:
  []
knowledge_refs:
  - "patterns/template-method"
---

# Advanced Template Method: Enforcing Invariants and Contracts

## Contracts in the Skeleton

The skeleton owns the contract: preconditions before each step, postconditions after, invariants across the flow. Assertions in the template method catch subclasses that violate the contract — the base class verifies, the subclass provides. Design-by-contract turns the template method into a verifiable pipeline rather than a hope.

```python
# Template method with contract enforcement
class Pipeline(ABC):
    def run(self, item):
        self._check(item, 'input')            # precondition
        cleaned = self.clean(item)
        self._check(cleaned, 'clean')         # step contract
        rows = self.transform(cleaned)
        self._check(rows, 'transform')
        self._invariant(rows)                 # invariant across flow
        return self.load(rows)

    def _check(self, value, stage):
        if value is None:
            raise ContractError(f'{stage} produced None')

    def _invariant(self, rows):
        if len(rows) != len({r.id for r in rows}):
            raise ContractError('duplicate ids after transform')

    @abstractmethod
    def clean(self, item): ...
    @abstractmethod
    def transform(self, cleaned): ...
    @abstractmethod
    def load(self, rows): ...
# Subclasses implement steps; the base enforces the contract
# between them — failure surfaces at the violating stage.
```

## Hook Ordering and Auditing

Hook ordering is part of the contract: before-hooks run in order, after-hooks in reverse, cleanups always run. Auditing the flow (logging each step and its timing) belongs in the skeleton, not the subclasses — every subclass gets observability for free.

## Practice: Harden the Skeleton

An ETL pipeline has had silent data-quality failures; the steps are subclassed by three teams.

**Task 1:** Add pre/post contracts and the flow invariant.

**Task 2:** Add step-level logging and timing to the skeleton.

**Task 3:** Verify a violating subclass fails at the stage, not downstream.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why the skeleton, not the subclasses, should own the contract.

**Prompt 2 — Implementation Design:**
> Design a validation pipeline: per-step preconditions and a cross-step invariant. Where do the assertions live?

**Prompt 3 — Boundary Testing:**
> A subclass returns valid-but-wrong data. Design the invariant that catches it at the right stage.

## Key Takeaways

- The skeleton owns pre/postconditions and invariants
- Assertions catch contract violations at the stage
- Hook ordering and cleanups are part of the contract
- Observability in the skeleton benefits every subclass

## Further Reading

- [Design by Contract — Wikipedia](https://en.wikipedia.org/wiki/Design_by_contract)
- [Template Method — Refactoring Guru](https://refactoring.guru/design-patterns/template-method)
