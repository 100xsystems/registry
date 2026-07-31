---
title: "Advanced Adapter: Protocols and Wire-Level Adaptation"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Build adapter hierarchies for families of vendors"
  - "Translate protocols (REST, gRPC, SOAP) at the boundary"
  - "Compose adapters with decorators"
  - "Design adaptive fallbacks"
prerequisites:
  []
knowledge_refs:
  - "patterns/adapter"
---

# Advanced Adapter: Protocols and Wire-Level Adaptation

## Adapter Hierarchies

When several vendors share behavior, an abstract adapter holds the common logic and concrete adapters override the differences: AbstractPaymentAdapter implements retry, idempotency, and logging; StripeAdapter and SquareAdapter supply the wire calls.

```python
# Abstract adapter: shared cross-cutting, concrete wire calls
class AbstractPaymentAdapter(PaymentProvider):
    def __init__(self, client):
        self.client = client

    def charge(self, req):
        for attempt in retry_backoff(3):        # shared logic
            try:
                return self._do_charge(req)
            except TransientError:
                continue

    def _do_charge(self, req):                  # implemented by subclass
        raise NotImplementedError

class StripeAdapter(AbstractPaymentAdapter):
    def _do_charge(self, req):
        return self.client.charges.create(**to_stripe(req))
```

## Protocol Translation

At the network boundary, adapters translate protocols: a gRPC service wrapped so a REST client can call it, or a SOAP API exposed as JSON. The adapter handles the mechanics — framing, headers, errors — so the core stays protocol-agnostic.

## Practice: Design the Adapter Stack

Three vendors expose three different protocols (REST, gRPC, SOAP) for the same capability.

**Task 1:** Define the common interface and the shared abstract adapter.

**Task 2:** Implement one concrete adapter per protocol.

**Task 3:** Add a circuit-breaker decorator around the adapter stack and test a vendor outage.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why an abstract adapter centralizes retries while concrete adapters own wire formats.

**Prompt 2 — Implementation Design:**
> Design a protocol-translating gateway: REST in, gRPC out, with error mapping and headers. What belongs in the adapter?

**Prompt 3 — Boundary Testing:**
> One vendor is down. Design the adaptive fallback that routes to a healthy vendor through the same adapter interface.

## Key Takeaways

- Abstract adapters centralize shared cross-cutting logic
- Protocol translation belongs at the boundary
- Decorators compose around adapters for resilience
- Adapters enable adaptive multi-vendor fallback

## Further Reading

- [Anti-Corruption Layer — DDD](https://martinfowler.com/bliki/AntiCorruptionLayer.html)
- [BFF (Backend for Frontend) as Adapter](https://samnewman.io/patterns/architectural/bff/)
