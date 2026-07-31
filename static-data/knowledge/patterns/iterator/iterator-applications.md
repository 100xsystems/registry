---
title: "Iterator in Production: Streams, Paging, and Cursors"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design cursor-based paging"
  - "Stream results without loading all"
  - "Handle iterator invalidation"
  - "Combine iterators in pipelines"
prerequisites:
  []
knowledge_refs:
  - "patterns/iterator"
---

# Iterator in Production: Streams, Paging, and Cursors

## Cursors and Paging

Database cursors and API pagination are iterators over an implicit result set: fetch a page, get the next token, continue. Cursor-based paging (WHERE id > last_seen ORDER BY id LIMIT 50) stays stable under concurrent inserts, unlike offset paging, which skips and duplicates rows.

```go
// Cursor paging: stable under concurrent writes
func ListEvents(ctx context.Context, after string, limit int) ([]Event, string, error) {
    rows, err := db.QueryContext(ctx,
        `SELECT id, body FROM events
         WHERE id > $1 ORDER BY id LIMIT $2`, after, limit)
    if err != nil { return nil, "", err }
    defer rows.Close()
    var out []Event
    for rows.Next() {
        var e Event
        rows.Scan(&e.ID, &e.Body)
        out = append(out, e)
    }
    next := ""
    if len(out) == limit { next = out[len(out)-1].ID }
    return out, next, nil   // pass next as the cursor for the next call
}
```

## Streaming and Invalidation

Streaming consumers read rows one at a time, never materializing the whole result — the iterator is a window over an open cursor. Invalidation is the classic hazard: a long-lived iterator over a changing table may see a consistent snapshot (MVCC) or fail fast (a version check on each step).

## Practice: Design the Pagination

A feed API returns posts ordered by created_at; users scroll for thousands of items while new posts arrive.

**Task 1:** Design cursor paging (cursor = created_at,id pair) that survives new inserts.

**Task 2:** Implement the streaming consumer that stops at a max row count.

**Task 3:** Test the offset-paging duplicate/skip bugs to prove the cursor design.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why cursor paging beats offset paging on a live table. Ask me to show the failing case.

**Prompt 2 — Implementation Design:**
> Design a Kafka-style consumer as an iterator: position, commit, and rebalance. What does the iterator protocol look like?

**Prompt 3 — Boundary Testing:**
> A page request arrives with a stale cursor from a deleted page. Design the error and the restart contract.

## Key Takeaways

- Cursors make paging stable under concurrent writes
- Streaming iterators never materialize full results
- Iterator invalidation needs a defined policy
- Pipelines compose iterators into stages

## Further Reading

- [PostgreSQL — Cursors](https://www.postgresql.org/docs/current/plpgsql-cursors.html)
- [REST API pagination best practices](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#pagination)
