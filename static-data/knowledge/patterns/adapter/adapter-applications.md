---
title: "Adapter in Production: Third-Party Integration"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Isolate vendor SDKs behind adapters"
  - "Translate data models at the boundary"
  - "Handle version and breaking changes"
  - "Test integrations without the vendor"
prerequisites:
  []
knowledge_refs:
  - "patterns/adapter"
---

# Adapter in Production: Third-Party Integration

## Vendor Isolation

Direct vendor-SDK calls scattered through the codebase make upgrades and vendor swaps terrifying. One adapter per vendor concentrates the SDK dependency: the rest of the codebase depends on your interface, so a vendor change touches one file.

```go
// Vendor isolated behind one adapter
type PaymentProvider interface {
    Charge(ctx context.Context, req ChargeRequest) (ChargeResult, error)
    Refund(ctx context.Context, id string, amount int64) error
}

// StripeAdapter and SquareAdapter both implement PaymentProvider.
// The checkout code depends on the interface, never on a vendor SDK.
// Vendor SDK upgrade or swap = touch one adapter file.
```

## Model Translation

Adapters translate between your domain model and the vendor model at the boundary: your Money{amount, currency} becomes the vendor's {amount_cents, currency_code}. The translation — including rounding, timezones, and enums — lives in one place with tests.

## Practice: Isolate the Email Vendor

Email sending is called from 30 places directly on the vendor SDK. A new vendor must be supported.

**Task 1:** Define the EmailSender interface your app needs.

**Task 2:** Write the adapter for the current vendor and the new one.

**Task 3:** Migrate the 30 call sites to the interface and delete the direct SDK usage.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why adapter isolation makes vendor upgrades a one-file change. Ask me what breaks if it is not isolated.

**Prompt 2 — Implementation Design:**
> Design a payment adapter with idempotency keys and retries inside the adapter. What does the app's interface look like?

**Prompt 3 — Boundary Testing:**
> The vendor changes a field meaning silently. Design the adapter's defensive validation and the contract test against the live vendor.

## Key Takeaways

- One adapter per vendor concentrates SDK risk
- Model translation lives at the boundary, tested
- The app depends on your interface, not the vendor
- Contract tests catch silent vendor changes

## Further Reading

- [Anti-Corruption Layer — DDD](https://martinfowler.com/bliki/AntiCorruptionLayer.html)
- [Vendor Lock-In Mitigation — Martin Fowler](https://martinfowler.com/bliki/SoftwareLockIn.html)
