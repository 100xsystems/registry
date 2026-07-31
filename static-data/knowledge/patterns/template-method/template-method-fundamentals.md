---
title: "Template Method: A Skeleton with Hooks"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the template method intent"
  - "Define the algorithm skeleton"
  - "Override the variable steps"
  - "Keep the flow invariant"
prerequisites:
  - "patterns/strategy"
  - "principles/open-closed"
knowledge_refs:
  - "patterns/template-method"
---

# Template Method: A Skeleton with Hooks

## The Problem

Several algorithms share the same steps but differ in the details: a data importer validates, parses, stores; a report generator gathers, formats, sends. Copying the flow per class duplicates it and drifts. The template method fixes the skeleton once in a base class, and subclasses override the variable steps — the flow itself never changes.

```python
# Template method: skeleton fixed, steps overridable
from abc import ABC, abstractmethod

class DataImporter(ABC):
    def import_data(self, source):      # the template method
        data = self.validate(source)    # step 1
        rows = self.parse(data)         # step 2
        self.store(rows)                # step 3
        self.after_import()             # hook, optional

    @abstractmethod
    def validate(self, source): ...
    @abstractmethod
    def parse(self, data): ...
    @abstractmethod
    def store(self, rows): ...

    def after_import(self):             # hook: default no-op
        pass

class CsvImporter(DataImporter):
    def validate(self, s): return s if s.endswith('.csv') else error()
    def parse(self, d): return read_csv(d)
    def store(self, rows): return db.insert(rows)

class JsonImporter(DataImporter):
    def validate(self, s): return s if s.endswith('.json') else error()
    def parse(self, d): return read_json(d)
    def store(self, rows): return db.insert(rows)
# The flow (validate -> parse -> store) is written once.
```

## Template vs Strategy

Both fix a shape; they differ in mechanism. Template method uses inheritance — the subclass fills the steps of the base algorithm. Strategy uses composition — the context holds an interchangeable algorithm object. Template method is right when the steps are inherently shared; strategy when the algorithm family must swap at runtime.

## Practice: Build the Report Skeleton

Reports gather data, format it, and deliver via email, file, or dashboard — one flow, three variants.

**Task 1:** Define the template method and the abstract steps.

**Task 2:** Implement three concrete subclasses.

**Task 3:** Add a hook (e.g., notify) that defaults off and is turned on by one subclass.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why fixing the skeleton prevents duplication drift.

**Prompt 2 — Compare & Contrast:**
> Compare template method with strategy: when does inheritance beat composition and vice versa?

**Prompt 3 — Boundary Testing:**
> A subclass forgets to call a required cleanup step. Design the base-class guard that enforces it.

## Key Takeaways

- Template method fixes the algorithm skeleton
- Subclasses override the variable steps
- Hooks provide optional extension points
- The flow is written once and cannot drift

## Further Reading

- [Template Method — Refactoring Guru](https://refactoring.guru/design-patterns/template-method)
- [Template method — Wikipedia](https://en.wikipedia.org/wiki/Template_method_pattern)
