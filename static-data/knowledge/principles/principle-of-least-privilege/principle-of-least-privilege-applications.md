---
title: "Least Privilege in Production: IAM and Service Identity"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design IAM policies with minimal scope"
  - "Use per-service identities"
  - "Apply least privilege to data access"
  - "Automate permission review"
prerequisites:
  []
knowledge_refs:
  - "principles/principle-of-least-privilege"
---

# Least Privilege in Production: IAM and Service Identity

## IAM Policies

Cloud IAM lets you grant by resource, action, and condition. A well-scoped policy allows exactly the actions on exactly the resources the service needs — never "s3:*" on "*" — with conditions (IP, time, tenant) narrowing further.

```json
// Minimal IAM: one bucket, one prefix, read-only
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["s3:GetObject"],
    "Resource": "arn:aws:s3:::reports-prod/invoices/*"
  }]
}
// Anti-pattern: "Action": "s3:*", "Resource": "*"
// A leaked key then reads AND deletes everything.
```

## Service Identity and Automation

Each service gets its own identity and short-lived credentials, never shared keys. Permission reviews are automated: unused roles are flagged, policy changes go through review, and access-reviews (who can do what) run on a schedule.

## Practice: Scrub the IAM

A legacy service holds AdministratorAccess because "it was easier".

**Task 1:** Map the service's real actions and resources; write the minimal policy.

**Task 2:** Deploy with the minimal policy in shadow mode (logs only) and verify no regressions.

**Task 3:** Set up the automated review: unused-role flags and quarterly access reviews.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why per-service identities plus short-lived credentials shrink the risk of a leaked key.

**Prompt 2 — Implementation Design:**
> Design the access-review pipeline: who reviews, what evidence, what happens to unused grants?

**Prompt 3 — Boundary Testing:**
> A service needs one admin action per quarter. Design the just-in-time escalation that expires automatically.

## Key Takeaways

- Scope IAM by resource, action, and condition
- Per-service identities with short-lived credentials
- Shadow-mode deploys make privilege reduction safe
- Automated reviews keep privilege creep out

## Further Reading

- [AWS IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Google Cloud IAM Conditions](https://cloud.google.com/iam/docs/conditions-overview)
