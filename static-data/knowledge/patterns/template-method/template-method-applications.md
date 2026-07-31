---
title: "Template Method in Production: Frameworks and Lifecycles"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Recognize IoC frameworks"
  - "Use lifecycle callbacks"
  - "Implement framework hooks"
  - "Test template subclasses"
prerequisites:
  []
knowledge_refs:
  - "patterns/template-method"
---

# Template Method in Production: Frameworks and Lifecycles

## Frameworks Are Template Methods

Every framework is a template method on a grand scale: the framework runs the flow (request handling, component lifecycle) and calls your code at the hooks. That inversion of control — the framework calls you, not the reverse — is the template method at framework scale. Your components override steps: lifecycle callbacks, request handlers, middleware.

```typescript
// A component lifecycle as a template method (framework-style)
abstract class Lifecycle {
  async run(): Promise<void> {          // fixed skeleton
    await this.onBeforeMount();
    await this.mount();
    await this.onMounted();             // hook
    await this.idle();
    await this.onBeforeUnmount();
    await this.unmount();
    await this.onUnmounted();           // hook
  }
  protected abstract mount(): Promise<void>;
  protected abstract unmount(): Promise<void>;
  protected abstract idle(): Promise<void>;
  protected async onBeforeMount(): Promise<void> {}
  protected async onMounted(): Promise<void> {}
  protected async onBeforeUnmount(): Promise<void> {}
  protected async onUnmounted(): Promise<void> {}
}
// The framework calls run(); your subclass fills mount/unmount.
// Hooks default to no-ops so subclasses override only what they
// need — the skeleton is shared, the steps are yours.
```

## Hooks and Defaults

Well-designed template methods provide sensible default steps and hooks so subclasses override the minimum. The anti-pattern: template methods that force subclasses to override steps they do not care about, or skeletons so rigid they cannot express the variation — then composition (strategy, callbacks) is the better tool.

## Practice: Implement a Lifecycle

A plugin system: plugins start, register routes, serve, and stop — with optional hooks for health and metrics.

**Task 1:** Design the plugin skeleton with abstract steps and hooks.

**Task 2:** Implement two plugins overriding the minimum.

**Task 3:** Test the flow: a failing step must run the cleanup hooks.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why every framework is a template method and what hooks are for.

**Prompt 2 — Implementation Design:**
> Design a middleware pipeline as a template method with before/after hooks per stage.

**Prompt 3 — Boundary Testing:**
> A plugin override throws mid-lifecycle. Design the base-class error handling that still unmounts cleanly.

## Key Takeaways

- Frameworks are template methods at scale
- IoC: the framework calls you at the hooks
- Sensible defaults minimize overrides
- Rigid skeletons signal composition instead

## Further Reading

- [Inversion of Control — Martin Fowler](https://martinfowler.com/bliki/InversionOfControl.html)
- [React lifecycle — docs](https://react.dev/learn/lifecycle-of-reactive-effects)
