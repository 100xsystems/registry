---
title: "Advanced Information Hiding: Capabilities and Security"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Use capability patterns for controlled exposure"
  - "Design security boundaries with hidden internals"
  - "Apply least privilege with information hiding"
  - "Hide errors to avoid leaking internals"
prerequisites:
  []
knowledge_refs:
  - "principles/information-hiding"
---

# Advanced Information Hiding: Capabilities and Security

## Capabilities

A capability is an unforgeable handle that grants access — passing the handle is the authorization. Instead of a globally-visible internal, a module hands out narrow capability objects that expose exactly one action, hiding everything else.

```python
# Capability: hand out a narrow handle, hide the rest
class Wallet:
    def __init__(self, balance):
        self._balance = balance

    def transfer_capability(self):
        # only the transfer action is exposed; balance stays hidden
        class Transfer:
            def __init__(self, w): self._w = w
            def transfer(self, to, amount):
                self._w._balance -= amount
                to._balance += amount
        return Transfer(self)

w1, w2 = Wallet(100), Wallet(0)
cap = w1.transfer_capability()   # caller holds only 'transfer'
# caller cannot read _balance or mint new money
```

## Errors Leak Internals

Error messages that reveal stack traces, SQL, or file paths leak internal structure to attackers. Information hiding applies to errors: the user sees a sanitized message; the operator sees the full context in logs. This is both a robustness and a security boundary.

## Practice: Design a Capability Surface

A document service: editors need edit, viewers need read, admins need delete.

**Task 1:** Define the capability objects (read-only, editable, admin) and what each hides.

**Task 2:** Design the error boundary: what each role sees versus what logs record.

**Task 3:** Explain how capabilities replace global role checks for access control.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why capabilities are more precise than global permissions.

**Prompt 2 — Implementation Design:**
> Design a plugin API where plugins can read data but cannot touch the core's internals. What capabilities do you hand out?

**Prompt 3 — Boundary Testing:**
> A leaked stack trace reveals the ORM and table names. Design the sanitization layer and the operator-only log channel.

## Key Takeaways

- Capabilities are unforgeable, narrow handles
- Least privilege is information hiding applied to access
- Error messages must not leak internals
- Hiding is a security boundary, not just a design nicety

## Further Reading

- [Capability-Based Security — Wikipedia](https://en.wikipedia.org/wiki/Capability-based_security)
- [OWASP — Error Handling](https://owasp.org/www-community/Improper_Error_Handling)
