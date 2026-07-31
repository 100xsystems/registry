---
title: "Least Privilege: Grant the Minimum"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Define the principle of least privilege"
  - "Apply it to users, processes, and services"
  - "Explain the blast-radius reduction"
  - "Audit and prune excessive permissions"
prerequisites:
  - "principles/information-hiding"
  - "principles/separation-of-concerns"
knowledge_refs:
  - "principles/principle-of-least-privilege"
---

# Least Privilege: Grant the Minimum

## The Principle

Least privilege: every user, service, and process gets exactly the permissions it needs to do its job, and nothing more. A report-reading service should not be able to delete records; a deploy job should not hold database admin.

The payoff is blast-radius reduction: when a credential is stolen or a service is compromised, the damage is bounded by the privileges that credential held. Over-permissioned systems turn one leak into total compromise.

```sql
-- Least privilege in the database:
-- the reporting app gets read-only; it cannot drop tables.
CREATE ROLE reporting_app LOGIN;
GRANT SELECT ON orders, customers TO reporting_app;
REVOKE ALL ON orders FROM reporting_app;   -- no UPDATE/DELETE

-- A service account should hold only what its task needs,
-- scoped to the schema it owns, never superuser.
```

## Scoping, Not Just Roles

Least privilege is about scope, not just "read vs write": read only the tables needed, only the rows (tenant-scoped), only the columns (no SSN on the public API), only the time (short-lived tokens). Each dimension shrinks the blast radius further.

## Practice: Audit the Permissions

A CI deploy token can delete any S3 bucket, and a support tool can read all customer PII.

**Task 1:** List the minimum permissions each tool actually needs.

**Task 2:** Replace the broad grants with scoped ones (bucket prefix, tenant filter).

**Task 3:** Design the review cadence: who audits permissions, and how often?

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why scoping columns and rows matters beyond scoping tables. Start with a leaked SSN.

**Prompt 2 — Compare & Contrast:**
> Compare least privilege with defense in depth and information hiding. How do the three reinforce each other?

**Prompt 3 — Boundary Testing:**
> A service legitimately needs admin for a rare migration. Design the temporary-escalation path with approval and expiry.

## Key Takeaways

- Grant the minimum access, nothing more
- Blast radius scales with granted privilege
- Scope by resource, row, column, and time
- Temporary escalation needs approval and expiry

## Further Reading

- [Principle of Least Privilege — OWASP](https://owasp.org/www-community/Access_Control)
- [Least Privilege — US NIST](https://csrc.nist.gov/glossary/term/least_privilege)
