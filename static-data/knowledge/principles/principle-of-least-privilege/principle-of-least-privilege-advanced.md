---
title: "Advanced Least Privilege: Zero Trust and Capabilities"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Apply zero-trust principles"
  - "Use capabilities for precise grants"
  - "Design dynamic authorization"
  - "Handle privilege escalation safely"
prerequisites:
  []
knowledge_refs:
  - "principles/principle-of-least-privilege"
---

# Advanced Least Privilege: Zero Trust and Capabilities

## Zero Trust

Zero trust assumes no network zone is trusted: every request is authenticated, authorized, and encrypted, and access is granted per-request by policy — not by "inside the network". This is least privilege applied to the network: there is no implicit trust to inherit.

```text
Zero trust properties:
  - Every request authenticated (identity, not IP)
  - Every request authorized (policy engine, per request)
  - Every path encrypted; nothing trusted implicitly
  - Micro-segmentation: even lateral movement hits authorization
Capabilities: unforgeable handles that carry their own authority.
Dynamic authz: policy evaluated with context (user, device, risk,
resource sensitivity) at request time, not baked into a static role.
```

## Dynamic Authorization

Static roles oversimplify: "admin" is one key for every door. Dynamic authorization evaluates policy with context — the user, the resource sensitivity, the device, the risk score — at each request, so a high-risk session can be limited in real time without changing the role.

## Practice: Design a Zero-Trust Service

An internal admin panel currently trusts the VPN and uses one shared admin role.

**Task 1:** Design per-request authz: identity, device posture, risk score, and resource sensitivity.

**Task 2:** Replace the shared role with scoped capabilities (read-only ops, audit view, deploy).

**Task 3:** Design the escalation flow for a rare privileged action with approval and expiry.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why "trust the VPN" is least-privilege failure and what replaces it.

**Prompt 2 — Implementation Design:**
> Design an authorization service with policy-as-code, request context, and audit. What does each request carry?

**Prompt 3 — Boundary Testing:**
> A capability handle is stolen. Design the revocation that does not require reissuing everything.

## Key Takeaways

- Zero trust removes implicit network trust
- Capabilities carry precise, unforgeable authority
- Dynamic authz evaluates context at request time
- Escalation is temporary, approved, and expiring

## Further Reading

- [Zero Trust Architecture — NIST SP 800-207](https://csrc.nist.gov/publications/detail/sp/800-207/final)
- [Google BeyondCorp](https://research.google/pubs/pub43231/)
