---
title: "Hash Indexes: O(1) Point Lookups"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the hash index structure"
  - "Handle collisions"
  - "Understand the O(1) expected cost"
  - "Know when a hash index fits"
prerequisites:
  - "principles/optimistic-locking"
  - "patterns/b-tree"
knowledge_refs:
  - "patterns/hash-index"
---

# Hash Indexes: O(1) Point Lookups

## The Structure

A hash index applies a hash function to the key and uses the result as a bucket index. Point lookups (WHERE id = 42) are O(1) expected: hash, jump, scan the short bucket. Collisions — different keys in one bucket — degrade but stay near O(1) with good hashing and load factor control.

```sql
-- Hash index: exact-equality lookups only
CREATE INDEX idx_users_email_hash ON users USING hash (email);

-- Uses the hash index: hash('a@b.com') -> bucket -> row
SELECT * FROM users WHERE email = 'a@b.com';

-- Does NOT use the hash index: range/order needs order (B-tree)
SELECT * FROM users WHERE email > 'a@b.com';
SELECT * FROM users ORDER BY email;
```

## Hash vs B-Tree

Hash indexes win on exact-equality point lookups and are excellent for primary keys. They cannot do ranges, ordering, or prefix scans — those need a B-tree. In-memory tables (Postgres hash, MySQL MEMORY) also use hash structures natively.

## Practice: Pick the Index Type

A session table is queried by session_id (exact) and by user_id with a time range.

**Task 1:** Classify each query shape: point, range, or order.

**Task 2:** Choose hash vs B-tree for each and justify.

**Task 3:** Sketch the bucket layout for the hash index and the collision policy.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why a hash index cannot answer range queries. Start with the bucket math.

**Prompt 2 — Compare & Contrast:**
> Compare hash indexes, B-trees, and LSM memtables for point lookups, ranges, and writes.

**Prompt 3 — Boundary Testing:**
> A poor hash function clusters keys into one bucket. Design the load-factor trigger and rehash path.

## Key Takeaways

- Hash indexes make point lookups O(1) expected
- Collisions handled by bucket chains and load factor
- No ranges, no ordering — B-tree for those
- Perfect for primary keys and equality joins

## Further Reading

- [PostgreSQL — Hash Indexes](https://www.postgresql.org/docs/current/indexes-types.html)
- [Designing Data-Intensive Applications — Ch. 3](https://dataintensive.net/)
