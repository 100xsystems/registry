---
title: "Chain of Responsibility: Pass It Down the Line"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the chain intent"
  - "Build a handler chain"
  - "Understand pass-along semantics"
  - "Compare with decorator and pipeline"
prerequisites:
  - "patterns/decorator"
  - "patterns/observer"
knowledge_refs:
  - "patterns/chain-of-responsibility"
---

# Chain of Responsibility: Pass It Down the Line

## The Idea

A chain of handlers, each deciding whether it can process a request or should pass it to the next. The sender does not know which handler will act — decoupling the request from its processor.

```java
// Chain of responsibility: each handler passes or handles
abstract class Handler {
    protected Handler next;
    Handler setNext(Handler h) { this.next = h; return h; }

    public final void handle(Request r) {
        if (canHandle(r)) {
            doHandle(r);
        } else if (next != null) {
            next.handle(r);      // pass it down the line
        } else {
            throw new UnhandledRequestException(r);
        }
    }
    protected abstract boolean canHandle(Request r);
    protected abstract void doHandle(Request r);
}

// SupportTier1 -> SupportTier2 -> SupportEscalation
new SupportTier1().setNext(new SupportTier2()).setNext(new Escalation());
```

## When It Fits

Chains fit when handlers are independent, order matters, and the "who handles" decision is dynamic. Middleware pipelines, event preprocessing, and approval flows are classic chains.

## Practice: Build the Approval Chain

A purchase request: manager approves under $1k, director under $10k, CFO above.

**Task 1:** Build the three-handler chain with canHandle rules.

**Task 2:** Handle the unhandled case (negative amount) explicitly.

**Task 3:** Insert a compliance check between director and CFO without touching either.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why the sender should not know which handler acts. Start with the decoupling benefit.

**Prompt 2 — Compare & Contrast:**
> Compare chain of responsibility with decorator (adds behavior around) and pipeline (all stages run). How does the pass-along differ?

**Prompt 3 — Boundary Testing:**
> Every handler passes and the chain ends. Design the explicit terminal handler for unhandled requests.

## Key Takeaways

- Handlers pass requests they cannot process
- The sender stays decoupled from the processor
- Order matters; insert handlers without touching others
- Terminal handling prevents silent drops

## Further Reading

- [Chain of Responsibility — Refactoring Guru](https://refactoring.guru/design-patterns/chain-of-responsibility)
- [Chain of Responsibility — Wikipedia](https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern)
