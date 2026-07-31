---
title: "B-Trees in Production: Database Indexes"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Read an index scan vs sequential scan plan"
  - "Design composite B-tree indexes"
  - "Use index-only scans"
  - "Avoid index-destroying queries"
prerequisites:
  []
knowledge_refs:
  - "patterns/b-tree"
---

# B-Trees in Production: Database Indexes

## Reading the Plan

EXPLAIN shows whether the query used an index scan (B-tree descent) or a sequential scan (full table). An index scan costs ~log(n) reads; a sequential scan costs n. The optimizer picks based on selectivity — that is the planning decision.

```sql
-- Composite index: (tenant_id, status, created_at)
CREATE INDEX idx_orders_tenant_status_created
  ON orders (tenant_id, status, created_at);

-- Uses the B-tree: exact tenant, exact status, range on created_at
SELECT * FROM orders
WHERE tenant_id = 42 AND status = 'open' AND created_at > now() - '1 day';

-- Index-only scan: all columns in the index -> no table read
EXPLAIN ANALYZE SELECT tenant_id, status FROM orders
WHERE tenant_id = 42 AND status = 'open';
```

## Composite Index Design

Composite indexes work left to right: leading columns should be equality filters, trailing columns ranges. A query filtering on the second column alone cannot use the index — a classic index-destroying mistake.

## Practice: Design the Index Set

A orders table queried by: tenant+status, tenant+created_at range, and status alone.

**Task 1:** Design the minimal index set that covers the three query shapes.

**Task 2:** Use EXPLAIN ANALYZE to verify each query hits an index, not a seq scan.

**Task 3:** Find the query that cannot use an index (status alone with low selectivity) and decide: index it or accept the scan?

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why composite indexes follow left-to-right prefix rules. Ask me to design one for a real table.

**Prompt 2 — Implementation Design:**
> Design indexes for a messaging table queried by (conversation_id, created_at DESC) with a LIMIT. What does the B-tree order support?

**Prompt 3 — Boundary Testing:**
> A function on the indexed column (WHERE lower(email) = ...) kills the index. Design the expression-index fix.

## Key Takeaways

- Index scans cost log(n); seq scans cost n
- Composite indexes follow left-prefix rules
- Index-only scans skip the table entirely
- Functions on indexed columns defeat the index

## Further Reading

- [PostgreSQL — Index Types](https://www.postgresql.org/docs/current/indexes-types.html)
- [Use The Index, Luke!](https://use-the-index-luke.com/sql/where-clause)
