#!/usr/bin/env python3
"""Deep curriculum data chunk 7: open-closed, optimistic-locking, pessimistic-locking, principle-of-least-privilege."""

TOPICS = {}


def _t(slug, topics):
    TOPICS[slug] = topics
    return topics


# ─────────────────────────────────────────────────────────────────────────────
# OPEN-CLOSED
# ─────────────────────────────────────────────────────────────────────────────
_t('open-closed', [
    {
        'title': 'Open-Closed: Extend Without Modifying',
        'desc': 'Why modules should be open for extension but closed for modification.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'State the open-closed principle',
            'Explain the risk of modifying tested code',
            'Extend behavior through interfaces and composition',
            'Recognize the modify-based anti-pattern',
        ],
        'prereqs': ['principles/dependency-inversion', 'principles/interface-segregation'],
        'sections': [
            {'heading': 'The Principle', 'paras': [
                'Open-Closed (OCP): a module should be open for extension (you can add new behavior) but closed for modification (you do not change its existing, tested code). Adding a new payment method should add a new class, not edit the switch statement.',
                'Every modification of tested code re-risks it: new bugs, new test runs, review cycles, and merge conflicts. Extension without modification keeps the stable core untouched while the system grows.',
            ], 'code': {'lang': 'java', 'body': '''
// Modify-based: every new shape edits the switch
double area(Object s) {
    if (s instanceof Circle) return pi * r * r;
    if (s instanceof Square) return side * side;
    if (s instanceof Triangle) return ...;   // edit here every time!
}

// Open-closed: new shapes implement the contract, no edits
interface Shape { double area(); }
class Circle implements Shape { public double area() { return pi*r*r; } }
// Adding a Triangle = adding a class. The area() loop never changes.'''}},
            {'heading': 'Abstraction Is the Mechanism', 'paras': [
                'Openness comes from an abstraction (interface/base) that new variants implement. The consuming code depends on the abstraction, so it stays closed while the set of variants is open. This is OCP realized through dependency inversion.',
                'The trap: abstracting too early. OCP earns its keep when variants are genuinely expected — apply it on the second concrete case, not the first.',
            ]},
        ],
        'practice': {
            'title': 'Open Up the Report Export',
            'intro': 'A report module exports CSV; you must add JSON, XML, and PDF without touching the report core.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the ExportFormat abstraction the core depends on.'},
                {'label': 'Task 2', 'text': 'Add the four exporters as implementations — zero edits to the core.'},
                {'label': 'Task 3', 'text': 'Wire the format selection at startup and explain why the core is now closed.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about when abstraction for openness is worth it and when it is premature. Start with one vs two variants.'},
            {'label': 'Compare & Contrast', 'text': 'Compare OCP with the strategy pattern and with dependency inversion. How do they relate?'},
            {'label': 'Boundary Testing', 'text': 'A new variant needs a behavior the abstraction cannot express. Design the evolution path that keeps the core closed.'},
        ],
        'takeaways': [
            'Open for extension, closed for modification',
            'Abstraction is the mechanism of openness',
            'Modifying tested code re-risks it every time',
            'Generalize on the second concrete case',
        ],
        'further': [
            {'title': 'Open-Closed Principle — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle'},
            {'title': 'SOLID — Robert C. Martin', 'url': 'https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html'},
        ],
    },
    {
        'title': 'Open-Closed in Production: Plugins and Policies',
        'desc': 'Plugin architectures, policy extension, and keeping cores stable under feature growth.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design plugin extension points',
            'Extend business policies without editing core flows',
            'Version extension points',
            'Manage the tension between openness and simplicity',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Plugin Architectures', 'paras': [
                'A plugin architecture makes the core open-closed by construction: the core defines extension points (interfaces, hooks, registries) and third parties register implementations. IDEs, browsers, and CI systems all work this way — the core stays stable while the plugin ecosystem grows.',
            ], 'code': {'lang': 'text', 'body': '''
Plugin architecture shape:
  core/          defines ExtensionPoint interfaces (never changes)
  registry/      discovers and loads implementations
  plugins/       third-party implementations of the points

Rules:
  - The core never imports a specific plugin
  - The plugin manifest declares which point it implements
  - Version the extension point (major bump = breaking)'''}},
            {'heading': 'Policy Extension', 'paras': [
                'Business rules (discounts, taxes, shipping) are the most volatile part of a system. Modeling them as strategies or rule objects — rather than if-chains in the order flow — keeps the checkout core closed while policies grow.',
            ]},
        ],
        'practice': {
            'title': 'Design the Extension Points',
            'intro': 'A checkout flow needs new payment and discount types every quarter.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the PaymentMethod and DiscountRule extension points.'},
                {'label': 'Task 2', 'text': 'Move the current variants into implementations; verify the core flow is untouched.'},
                {'label': 'Task 3', 'text': 'Define the versioning policy for the extension points and the migration path.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why versioning extension points matters and what happens when one evolves without a contract. Ask me about breaking changes.'},
            {'label': 'Implementation Design', 'text': 'Design a plugin registry with discovery, validation, and isolation. How do you prevent a bad plugin from taking down the core?'},
            {'label': 'Boundary Testing', 'text': 'A plugin needs to change core behavior, not just extend it. Design the escape hatch that does not break the closed core.'},
        ],
        'takeaways': [
            'Plugins make the core open-closed by construction',
            'Business policies belong in strategies, not if-chains',
            'Extension points need versioning',
            'Openness and simplicity are balanced by contract discipline',
        ],
        'further': [
            {'title': 'Plugin Architecture — Martin Fowler', 'url': 'https://martinfowler.com/articles/osgi.html'},
            {'title': 'Strategy Pattern — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/strategy'},
        ],
    },
    {
        'title': 'Advanced Open-Closed: Evolutionary APIs',
        'desc': 'APIs that evolve without breaking callers, and contracts that stay stable for decades.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Design backward-compatible API evolution',
            'Use additive change rules',
            'Manage deprecation timelines',
            'Keep contracts stable under growth',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Additive Evolution', 'paras': [
                'A public API is closed the moment it ships: callers depend on it. Evolution rules are additive: add fields and endpoints, never remove or reinterpret. New optional fields are safe; changing a field\'s meaning breaks every caller.',
            ], 'code': {'lang': 'text', 'body': '''
Additive API evolution rules:
  - Add new fields (optional), never remove existing ones
  - Add new endpoints, never change existing semantics
  - Unknown fields must be preserved (forward compatibility)
  - Version majors when a breaking change is unavoidable
  - Deprecate with a timeline: warn -> sunset -> remove (documented)'''}},
            {'heading': 'Contracts That Last', 'paras': [
                'The most successful contracts (HTTP, JSON, TCP) stayed open-closed through decades by additive evolution and tolerance: servers ignore unknown fields, clients degrade gracefully. Design your API the same way — forward compatibility is a feature.',
            ]},
        ],
        'practice': {
            'title': 'Evolve Without Breaking',
            'intro': 'A user API returns {id, name}. You must add email and eventually remove the deprecated phone field.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Add email additively; verify old clients still parse the response.'},
                {'label': 'Task 2', 'text': 'Design the phone deprecation: warn header, sunset date, migration docs.'},
                {'label': 'Task 3', 'text': 'Add forward-compat handling: unknown fields preserved in proxy responses.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why removing a field is a breaking change even if you update all your own callers.'},
            {'label': 'Implementation Design', 'text': 'Design a versioning policy for an internal API used by 40 services. What triggers a major bump, and how is the migration run?'},
            {'label': 'Boundary Testing', 'text': 'A security fix requires changing a field\'s meaning (e.g., role to roles). Design the transition that stays additive.'},
        ],
        'takeaways': [
            'APIs are closed the moment they ship',
            'Evolve additively; preserve unknown fields',
            'Deprecation is a timeline, not an event',
            'Forward compatibility makes contracts last',
        ],
        'further': [
            {'title': 'API Evolution — Google API Design Guide', 'url': 'https://cloud.google.com/apis/design/compatibility'},
            {'title': 'Postel\'s Law (Be liberal in what you accept)', 'url': 'https://www.rfc-editor.org/rfc/rfc1122#page-18'},
        ],
    },
    {
        'title': 'Open-Closed: Review & Mastery Quiz',
        'desc': 'Scenario questions on extension, plugins, and API evolution.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate OCP concepts',
            'Design extension points',
            'Evolve contracts additively',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: OCP means modules are open for? (A: modification / B: extension / C: deletion)',
                'Q2: The mechanism of openness is? (A: copying / B: abstraction / C: comments)',
                'Q3: Adding a payment method should ideally? (A: edit the switch / B: add a class / C: rewrite the core)',
                'Q4: True or false: removing an API field is always safe if you control the callers.',
                'Q5: Deprecation should follow? (A: a documented timeline / B: instant removal / C: silence)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A pricing engine edits a switch statement monthly. Redesign as an open-closed policy set and describe the first migration.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "I just changed the tested code, it\'s fine" is how bugs get shipped.'},
        ],
        'takeaways': [
            'Q1: B; Q2: B; Q3: B; Q4: false; Q5: A',
            'Openness is earned by abstraction, kept by contract discipline',
            'Additive evolution keeps APIs closed forever',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# OPTIMISTIC LOCKING
# ─────────────────────────────────────────────────────────────────────────────
_t('optimistic-locking', [
    {
        'title': 'Optimistic Locking: Check Before You Write',
        'desc': 'Why assuming no conflict — and verifying it at write time — scales better than locking everything.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Define optimistic locking',
            'Use version numbers to detect conflicts',
            'Handle conflict on write',
            'Compare with pessimistic locking',
        ],
        'prereqs': ['principles/consistency-pattern', 'principles/idempotency'],
        'sections': [
            {'heading': 'The Idea', 'paras': [
                'Optimistic locking lets many readers and writers proceed concurrently, assuming conflicts are rare. Each row carries a version; a write succeeds only if the version it read still matches. If it does not, the write fails with a conflict the application resolves.',
                'It trades retries (on conflict) for concurrency (always allowed). For read-heavy, low-contention data — profiles, documents, carts — it beats holding locks.',
            ], 'code': {'lang': 'sql', 'body': '''
-- Optimistic: version-guarded update
UPDATE accounts
SET balance = 100, version = version + 1
WHERE id = 42 AND version = 7;      -- only if unchanged since read

-- If 0 rows affected: someone else wrote first -> conflict
-- The app re-reads, re-applies the change, and retries.
-- Version (or updated_at) is the conflict detector.'''}},
            {'heading': 'Why Optimistic', 'paras': [
                'Pessimistic locks serialize writers and force waiting — fine for hot rows, costly when contention is low. Optimistic locking has zero lock overhead in the happy path; the cost appears only when conflicts actually happen.',
            ]},
        ],
        'practice': {
            'title': 'Detect the Conflict',
            'intro': 'Two users edit the same document concurrently; both loaded version 3.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Trace the two writes: which succeeds and what happens to the loser?'},
                {'label': 'Task 2', 'text': 'Design the conflict UX: reload, merge, or overwrite — and when each is right.'},
                {'label': 'Task 3', 'text': 'Compare with a version-less update (lost update bug). Show the difference.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why the lost-update bug disappears when a version guard is added. Start with the two-reader scenario.'},
            {'label': 'Compare & Contrast', 'text': 'Compare optimistic locking with pessimistic locking and atomic conditional updates. When is each cheapest?'},
            {'label': 'Boundary Testing', 'text': 'A long-running form holds a document open for an hour; by submit time, 20 versions have passed. Design the merge/retry path that does not frustrate the user.'},
        ],
        'takeaways': [
            'Version guards detect conflicts at write time',
            'Optimistic = no lock overhead, retry on conflict',
            'Best for read-heavy, low-contention data',
            'Conflict UX is part of the design, not an afterthought',
        ],
        'further': [
            {'title': 'Optimistic Concurrency — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Optimistic_concurrency_control'},
            {'title': 'PostgreSQL — Row-level Locks & MVCC', 'url': 'https://www.postgresql.org/docs/current/mvcc.html'},
        ],
    },
    {
        'title': 'Optimistic Locking in Production: MVCC and Retries',
        'desc': 'How databases implement it (MVCC), retry design, and version schemes that scale.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Explain MVCC as the database-level optimistic mechanism',
            'Design retry loops with bounded attempts',
            'Use updated_at vs version counters',
            'Handle partial failures in retries',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'MVCC', 'paras': [
                'Databases use Multi-Version Concurrency Control: readers see a snapshot, writers create new versions, and conflicts are detected when a transaction commits against a stale snapshot. This is optimistic concurrency at the engine level — reads never block, and write conflicts surface at commit.',
            ], 'code': {'lang': 'text', 'body': '''
MVCC in one picture:
  t0: T1 reads balance=100 (snapshot)
  t1: T2 reads balance=100 (snapshot)
  t2: T2 writes balance=90  -> new version, commits
  t3: T1 writes balance=90  -> CONFLICT (stale snapshot)
T1 must retry with the fresh version. Read-mostly workloads
never wait — that is why MVCC dominates modern databases.'''}},
            {'heading': 'Retry Design', 'paras': [
                'On conflict, the application re-reads, re-applies, and retries — with a bounded attempt count and backoff. Infinite retry on a hot row makes things worse; exponential backoff with a small max keeps the retry storm contained.',
            ]},
        ],
        'practice': {
            'title': 'Build the Retry Loop',
            'intro': 'A seat-booking flow increments booked count on a popular event.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Implement the version-guarded update with a retry loop (max 3 attempts, backoff).'},
                {'label': 'Task 2', 'text': 'Handle the terminal state: after 3 conflicts, return a friendly "seats changed" error.'},
                {'label': 'Task 3', 'text': 'Verify idempotency: a retry must not double-count a seat.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why the retry must re-read the fresh version rather than blindly retrying the stale one.'},
            {'label': 'Implementation Design', 'text': 'Design optimistic locking for a leaderboard with millions of score writes. When does optimistic locking break down, and what replaces it?'},
            {'label': 'Boundary Testing', 'text': 'A conflict occurs after a side effect (email sent) but before the write. Design the ordering that makes the retry safe.'},
        ],
        'takeaways': [
            'MVCC gives databases optimistic concurrency for free',
            'Retries must re-read and re-apply, with bounds',
            'Version counters beat timestamps for concurrent writes',
            'Side effects before writes break retry safety',
        ],
        'further': [
            {'title': 'MVCC — PostgreSQL Docs', 'url': 'https://www.postgresql.org/docs/current/mvcc.html'},
            {'title': 'Optimistic Concurrency — Microsoft Docs', 'url': 'https://learn.microsoft.com/en-us/ef/core/saving/concurrency'},
        ],
    },
    {
        'title': 'Advanced Optimistic Locking: Conflict-Free Alternatives',
        'desc': 'When optimistic locking is not enough, and CRDTs/conditionals that avoid conflicts entirely.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Recognize when optimistic locking breaks down',
            'Use atomic conditional writes where possible',
            'Apply CRDTs for conflict-free convergence',
            'Combine optimistic locking with idempotency keys',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Hot-Row Breakdown', 'paras': [
                'When a single row is written by thousands of concurrent clients (a popular counter, a seat map), conflicts approach 100% and optimistic locking degenerates into retry churn. The answer is a different data shape: shard the counter, use atomic increments, or move the hot state to a fast store with a reconciliation step.',
            ], 'code': {'lang': 'sql', 'body': '''
-- Atomic conditional: no version needed for simple guarded writes
UPDATE inventory
SET stock = stock - 1
WHERE sku = 'A1' AND stock > 0;    -- atomic guard: never oversells

-- For hot counters: shard into per-shard counters
-- UPDATE counters SET n = n + 1 WHERE shard = 1;  (then SUM over shards)
-- Atomic ops beat read-check-write on hot rows.'''}},
            {'heading': 'Conflict-Free by Design', 'paras': [
                'CRDTs eliminate conflicts for merge-friendly data (sets, counters, text): replicas diverge and merge deterministically. Pairing optimistic locking (for sequential edits) with CRDTs (for concurrent merges) covers most collaborative workloads.',
                'Idempotency keys + optimistic locking combine to make retries safe against both duplicates and lost updates.',
            ]},
        ],
        'practice': {
            'title': 'Escalate the Locking Strategy',
            'intro': 'A ticket sale: 10,000 seats, 50k concurrent requests.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Show why optimistic locking on a single seat-map row collapses.'},
                {'label': 'Task 2', 'text': 'Redesign: per-seat rows with atomic conditional update (stock>0 guard).'},
                {'label': 'Task 3', 'text': 'Add the idempotency key so retries do not double-book, and the reconciliation for partial failures.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why atomic conditional updates are optimistic locking with the check moved into the write itself.'},
            {'label': 'Implementation Design', 'text': 'Design a collaborative document: which fields use CRDTs, which use optimistic locking with conflict UI? Justify each.'},
            {'label': 'Boundary Testing', 'text': 'A distributed counter needs exact totals for billing (not approximation). Design the path from sharded counters to an exact reconciled total.'},
        ],
        'takeaways': [
            'Hot rows break optimistic locking — change the data shape',
            'Atomic conditionals move the check into the write',
            'CRDTs remove conflicts for merge-friendly data',
            'Idempotency keys make retries safe on top of locking',
        ],
        'further': [
            {'title': 'CRDTs for Collaborative Editing', 'url': 'https://hal.inria.fr/inria-00555588/document'},
            {'title': 'Atomic Ops in PostgreSQL', 'url': 'https://www.postgresql.org/docs/current/sql-update.html'},
        ],
    },
    {
        'title': 'Optimistic Locking: Review & Mastery Quiz',
        'desc': 'Scenario questions on versions, MVCC, and conflict resolution.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate locking concepts',
            'Design version guards and retries',
            'Choose escalation strategies',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Optimistic locking detects conflicts? (A: at write time / B: before reads / C: never)',
                'Q2: The conflict detector is usually? (A: a version / B: a lock / C: a queue)',
                'Q3: MVCC lets readers? (A: block writers / B: read a snapshot / C: lock rows)',
                'Q4: True or false: retries should re-read the fresh version.',
                'Q5: Hot rows under optimistic locking cause? (A: retry churn / B: less work / C: no effect)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'An e-commerce cart merges concurrent edits from two tabs. Design the version guard, the conflict UX, and the retry path.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "just update the row" silently loses data without a version guard.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: B; Q4: true; Q5: A',
            'Optimistic locking scales reads, retries on conflict',
            'Escalate to atomic ops or CRDTs when conflicts dominate',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# PESSIMISTIC LOCKING
# ─────────────────────────────────────────────────────────────────────────────
_t('pessimistic-locking', [
    {
        'title': 'Pessimistic Locking: Lock Before You Touch',
        'desc': 'Why some writes are too expensive to retry and must be serialized up front.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Define pessimistic locking',
            'Use SELECT ... FOR UPDATE style locks',
            'Explain lock scope and duration',
            'Compare with optimistic locking',
        ],
        'prereqs': ['principles/optimistic-locking', 'principles/consistency-pattern'],
        'sections': [
            {'heading': 'The Idea', 'paras': [
                'Pessimistic locking acquires the lock before the read-modify-write, so no other writer can interfere — at the cost of waiting. It is right when conflicts are frequent, retries are expensive, or the operation cannot be re-run (charging a card, transferring funds).',
                'The database form: SELECT ... FOR UPDATE locks the row until the transaction commits, serializing writers while readers continue on snapshots.',
            ], 'code': {'lang': 'sql', 'body': '''
-- Pessimistic: lock the row, then act, then commit
BEGIN;
SELECT balance FROM accounts WHERE id = 42 FOR UPDATE;
-- ... compute and write with certainty no one else moved it ...
UPDATE accounts SET balance = 90 WHERE id = 42;
COMMIT;   -- lock released

-- The FOR UPDATE lock guarantees exclusive write access
-- for the duration of the transaction.'''}},
            {'heading': 'Lock Discipline', 'paras': [
                'Lock scope must cover exactly the read-modify-write, and nothing more: acquiring early or holding long multiplies contention and can deadlock. Lock ordering (always lock resources in the same order) prevents circular waits.',
            ]},
        ],
        'practice': {
            'title': 'Lock the Seat',
            'intro': 'A booking flow must guarantee a seat stays held through the payment attempt (up to 10 minutes).',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the lock: row, scope (seat), and duration (hold period with expiry).'},
                {'label': 'Task 2', 'text': 'Trace two concurrent bookings for the same seat: who waits, who wins?'},
                {'label': 'Task 3', 'text': 'Design the hold expiry so a crashed client releases the seat automatically.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why holding a lock across a network call (payment) is dangerous and how to shorten it.'},
            {'label': 'Compare & Contrast', 'text': 'Compare pessimistic locking with optimistic locking for a bank transfer. Which fits, and why?'},
            {'label': 'Boundary Testing', 'text': 'A locked row\'s owner crashes mid-transaction. What guarantees the lock is eventually released?'},
        ],
        'takeaways': [
            'Pessimistic locking serializes writers at acquisition time',
            'Right for frequent conflicts and un-rerunnable operations',
            'Lock scope must cover exactly the read-modify-write',
            'Consistent lock ordering prevents deadlocks',
        ],
        'further': [
            {'title': 'SELECT FOR UPDATE — PostgreSQL', 'url': 'https://www.postgresql.org/docs/current/sql-select.html'},
            {'title': 'Pessimistic vs Optimistic Locking — Hibernate', 'url': 'https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#locking'},
        ],
    },
    {
        'title': 'Pessimistic Locking in Production: Distributed Locks',
        'desc': 'Locks across services and processes: Redis locks, database advisory locks, and their failure modes.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design distributed locks with leases',
            'Use advisory locks and Redis locks',
            'Handle lock expiry and fencing',
            'Avoid the lock-across-network-call trap',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Distributed Locks', 'paras': [
                'When the guarded resource spans processes, the lock lives in a shared store: a database row, a Redis SETNX with TTL, or a coordination service. The lock must expire (lease) so a crashed holder releases it — and holders must be fenced so an expired-but-still-running holder cannot write.',
            ], 'code': {'lang': 'python', 'body': '''
# Redis lock with lease (simplified, fencing omitted for brevity)
import redis, time, uuid

def acquire(client, name, ttl_ms=10_000):
    token = uuid.uuid4().hex
    ok = client.set(f'lock:{name}', token, nx=True, px=ttl_ms)
    return token if ok else None

def release(client, name, token):
    # only release if we still own it (Lua for atomicity)
    script = "if redis.call('get', KEYS[1]) == ARGV[1] " \\
             "then return redis.call('del', KEYS[1]) else return 0 end"
    client.eval(script, 1, f'lock:{name}', token)'''}},
            {'heading': 'The Trap: Network Calls Under Lock', 'paras': [
                'Holding a distributed lock across a slow external call makes the lease expire while the holder still works — then a second holder acquires the lock and both act. The fix: keep the locked section short and local, or carry a fencing token that storage validates.',
            ]},
        ],
        'practice': {
            'title': 'Design the Distributed Lock',
            'intro': 'A job scheduler must ensure only one node runs the nightly cleanup.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the lock: store, lease duration, renewal loop, and release path.'},
                {'label': 'Task 2', 'text': 'Handle the crash case: lease expires, another node acquires. What fences the old node?'},
                {'label': 'Task 3', 'text': 'Explain why the cleanup must NOT call a slow external service while holding the lock.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why a lock without a lease is a time bomb and why a lease without fencing still allows double action.'},
            {'label': 'Implementation Design', 'text': 'Design a payment double-charge guard using a distributed lock plus idempotency key. Where does the lock end and the key take over?'},
            {'label': 'Boundary Testing', 'text': 'The lock store (Redis) is down. Design the degraded mode: fail open (risky) or fail closed (safe but unavailable)?'},
        ],
        'takeaways': [
            'Distributed locks need leases and fencing',
            'Redis SETNX with TTL is a lock; the Lua release is atomic',
            'Never hold locks across slow network calls',
            'Fencing tokens make expired holders harmless',
        ],
        'further': [
            {'title': 'How to Do Distributed Locking — Kleppmann', 'url': 'https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html'},
            {'title': 'Redlock Controversy — Redis Docs', 'url': 'https://redis.io/docs/latest/develop/use/patterns/distributed-locks/'},
        ],
    },
    {
        'title': 'Advanced Pessimistic Locking: Deadlock Avoidance and Escalation',
        'desc': 'Deadlock detection, lock hierarchies, and knowing when to escalate beyond row locks.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Design lock hierarchies that prevent deadlock',
            'Handle deadlock detection and retry',
            'Choose lock granularity deliberately',
            'Escalate to serialized structures when needed',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Deadlock Avoidance', 'paras': [
                'Deadlocks happen when two transactions each hold a lock the other needs. Prevention: acquire locks in a canonical order (e.g., always account A then B, sorted by ID). Detection: databases detect wait cycles and abort one transaction, which the app must retry.',
            ], 'code': {'lang': 'text', 'body': '''
Deadlock avoidance rules:
  - Lock in a canonical order (sort resource IDs first)
  - Keep transactions short and single-purpose
  - Use NOWAIT / lock_timeout to fail fast instead of waiting forever
  - On deadlock error (40P01 in Postgres), retry the transaction

Escalation ladder:
  row lock -> table partition lock -> advisory lock -> queue/serialization
  Move up only when row-level serialization cannot do the job.'''}},
            {'heading': 'Granularity and Escalation', 'paras': [
                'Fine-grained locks (rows) maximize concurrency; coarse locks (tables, partitions) simplify but serialize. Escalate deliberately: a global sequence or a single-writer queue replaces row locking when the hot resource is a counter or a total, not a row.',
            ]},
        ],
        'practice': {
            'title': 'Eliminate the Deadlock',
            'intro': 'Transfers lock (A then B) in one code path and (B then A) in another.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Reproduce the deadlock with two concurrent transfers in opposite orders.'},
                {'label': 'Task 2', 'text': 'Fix with canonical ordering (sort account IDs before locking).'},
                {'label': 'Task 3', 'text': 'Add deadlock detection handling (retry on 40P01) and lock_timeout as a backstop.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why lock ordering prevents deadlock and why detection-with-retry is the pragmatic fallback.'},
            {'label': 'Implementation Design', 'text': 'Design a single-writer queue for a hot shared counter, and describe when it beats row locks.'},
            {'label': 'Boundary Testing', 'text': 'A transaction locks 100 rows and the lock manager starts escalating. Design the granularity policy that avoids escalation storms.'},
        ],
        'takeaways': [
            'Canonical lock ordering prevents deadlocks',
            'Detection + retry is the pragmatic backstop',
            'Granularity is a deliberate concurrency decision',
            'Escalate to serialized structures for hot shared state',
        ],
        'further': [
            {'title': 'PostgreSQL — Deadlock Handling', 'url': 'https://www.postgresql.org/docs/current/explicit-locking.html#LOCKING-DEADLOCKS'},
            {'title': 'Lock Hierarchy — Operating Systems Concepts', 'url': 'https://en.wikipedia.org/wiki/Lock_hierarchy'},
        ],
    },
    {
        'title': 'Pessimistic Locking: Review & Mastery Quiz',
        'desc': 'Scenario questions on locks, leases, and deadlocks.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate locking concepts',
            'Design safe distributed locks',
            'Prevent deadlocks',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Pessimistic locking acquires the lock? (A: after the write / B: before the read-modify-write / C: never)',
                'Q2: A distributed lock must have? (A: a lease / B: a queue / C: a cache)',
                'Q3: Deadlocks are prevented by? (A: canonical lock ordering / B: bigger locks / C: faster disks)',
                'Q4: True or false: holding a lock across a slow network call is safe with a long lease.',
                'Q5: On a deadlock error, the application should? (A: ignore / B: retry the transaction / C: crash)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A seat-hold system must guarantee exclusive holds without deadlocks. Design the lock scope, order, lease, and fencing.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "I added a lock" is only half the solution — leases and ordering are the other half.'},
        ],
        'takeaways': [
            'Q1: B; Q2: A; Q3: A; Q4: false; Q5: B',
            'Pessimistic locking serializes when it must',
            'Leases, fencing, and ordering make it safe',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# PRINCIPLE OF LEAST PRIVILEGE
# ─────────────────────────────────────────────────────────────────────────────
_t('principle-of-least-privilege', [
    {
        'title': 'Least Privilege: Grant the Minimum',
        'desc': 'Why every principal should have exactly the access it needs — no more.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Define the principle of least privilege',
            'Apply it to users, processes, and services',
            'Explain the blast-radius reduction',
            'Audit and prune excessive permissions',
        ],
        'prereqs': ['principles/information-hiding', 'principles/separation-of-concerns'],
        'sections': [
            {'heading': 'The Principle', 'paras': [
                'Least privilege: every user, service, and process gets exactly the permissions it needs to do its job, and nothing more. A report-reading service should not be able to delete records; a deploy job should not hold database admin.',
                'The payoff is blast-radius reduction: when a credential is stolen or a service is compromised, the damage is bounded by the privileges that credential held. Over-permissioned systems turn one leak into total compromise.',
            ], 'code': {'lang': 'sql', 'body': '''
-- Least privilege in the database:
-- the reporting app gets read-only; it cannot drop tables.
CREATE ROLE reporting_app LOGIN;
GRANT SELECT ON orders, customers TO reporting_app;
REVOKE ALL ON orders FROM reporting_app;   -- no UPDATE/DELETE

-- A service account should hold only what its task needs,
-- scoped to the schema it owns, never superuser.'''}},
            {'heading': 'Scoping, Not Just Roles', 'paras': [
                'Least privilege is about scope, not just "read vs write": read only the tables needed, only the rows (tenant-scoped), only the columns (no SSN on the public API), only the time (short-lived tokens). Each dimension shrinks the blast radius further.',
            ]},
        ],
        'practice': {
            'title': 'Audit the Permissions',
            'intro': 'A CI deploy token can delete any S3 bucket, and a support tool can read all customer PII.',
            'tasks': [
                {'label': 'Task 1', 'text': 'List the minimum permissions each tool actually needs.'},
                {'label': 'Task 2', 'text': 'Replace the broad grants with scoped ones (bucket prefix, tenant filter).'},
                {'label': 'Task 3', 'text': 'Design the review cadence: who audits permissions, and how often?'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why scoping columns and rows matters beyond scoping tables. Start with a leaked SSN.'},
            {'label': 'Compare & Contrast', 'text': 'Compare least privilege with defense in depth and information hiding. How do the three reinforce each other?'},
            {'label': 'Boundary Testing', 'text': 'A service legitimately needs admin for a rare migration. Design the temporary-escalation path with approval and expiry.'},
        ],
        'takeaways': [
            'Grant the minimum access, nothing more',
            'Blast radius scales with granted privilege',
            'Scope by resource, row, column, and time',
            'Temporary escalation needs approval and expiry',
        ],
        'further': [
            {'title': 'Principle of Least Privilege — OWASP', 'url': 'https://owasp.org/www-community/Access_Control'},
            {'title': 'Least Privilege — US NIST', 'url': 'https://csrc.nist.gov/glossary/term/least_privilege'},
        ],
    },
    {
        'title': 'Least Privilege in Production: IAM and Service Identity',
        'desc': 'Cloud IAM, service accounts, and role-based access that stays minimal at scale.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design IAM policies with minimal scope',
            'Use per-service identities',
            'Apply least privilege to data access',
            'Automate permission review',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'IAM Policies', 'paras': [
                'Cloud IAM lets you grant by resource, action, and condition. A well-scoped policy allows exactly the actions on exactly the resources the service needs — never "s3:*" on "*" — with conditions (IP, time, tenant) narrowing further.',
            ], 'code': {'lang': 'json', 'body': '''
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
// A leaked key then reads AND deletes everything.'''}},
            {'heading': 'Service Identity and Automation', 'paras': [
                'Each service gets its own identity and short-lived credentials, never shared keys. Permission reviews are automated: unused roles are flagged, policy changes go through review, and access-reviews (who can do what) run on a schedule.',
            ]},
        ],
        'practice': {
            'title': 'Scrub the IAM',
            'intro': 'A legacy service holds AdministratorAccess because "it was easier".',
            'tasks': [
                {'label': 'Task 1', 'text': 'Map the service\'s real actions and resources; write the minimal policy.'},
                {'label': 'Task 2', 'text': 'Deploy with the minimal policy in shadow mode (logs only) and verify no regressions.'},
                {'label': 'Task 3', 'text': 'Set up the automated review: unused-role flags and quarterly access reviews.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why per-service identities plus short-lived credentials shrink the risk of a leaked key.'},
            {'label': 'Implementation Design', 'text': 'Design the access-review pipeline: who reviews, what evidence, what happens to unused grants?'},
            {'label': 'Boundary Testing', 'text': 'A service needs one admin action per quarter. Design the just-in-time escalation that expires automatically.'},
        ],
        'takeaways': [
            'Scope IAM by resource, action, and condition',
            'Per-service identities with short-lived credentials',
            'Shadow-mode deploys make privilege reduction safe',
            'Automated reviews keep privilege creep out',
        ],
        'further': [
            {'title': 'AWS IAM Best Practices', 'url': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html'},
            {'title': 'Google Cloud IAM Conditions', 'url': 'https://cloud.google.com/iam/docs/conditions-overview'},
        ],
    },
    {
        'title': 'Advanced Least Privilege: Zero Trust and Capabilities',
        'desc': 'Zero-trust architecture, capability systems, and dynamic authorization.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Apply zero-trust principles',
            'Use capabilities for precise grants',
            'Design dynamic authorization',
            'Handle privilege escalation safely',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Zero Trust', 'paras': [
                'Zero trust assumes no network zone is trusted: every request is authenticated, authorized, and encrypted, and access is granted per-request by policy — not by "inside the network". This is least privilege applied to the network: there is no implicit trust to inherit.',
            ], 'code': {'lang': 'text', 'body': '''
Zero trust properties:
  - Every request authenticated (identity, not IP)
  - Every request authorized (policy engine, per request)
  - Every path encrypted; nothing trusted implicitly
  - Micro-segmentation: even lateral movement hits authorization
Capabilities: unforgeable handles that carry their own authority.
Dynamic authz: policy evaluated with context (user, device, risk,
resource sensitivity) at request time, not baked into a static role.'''}},
            {'heading': 'Dynamic Authorization', 'paras': [
                'Static roles oversimplify: "admin" is one key for every door. Dynamic authorization evaluates policy with context — the user, the resource sensitivity, the device, the risk score — at each request, so a high-risk session can be limited in real time without changing the role.',
            ]},
        ],
        'practice': {
            'title': 'Design a Zero-Trust Service',
            'intro': 'An internal admin panel currently trusts the VPN and uses one shared admin role.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design per-request authz: identity, device posture, risk score, and resource sensitivity.'},
                {'label': 'Task 2', 'text': 'Replace the shared role with scoped capabilities (read-only ops, audit view, deploy).'},
                {'label': 'Task 3', 'text': 'Design the escalation flow for a rare privileged action with approval and expiry.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why "trust the VPN" is least-privilege failure and what replaces it.'},
            {'label': 'Implementation Design', 'text': 'Design an authorization service with policy-as-code, request context, and audit. What does each request carry?'},
            {'label': 'Boundary Testing', 'text': 'A capability handle is stolen. Design the revocation that does not require reissuing everything.'},
        ],
        'takeaways': [
            'Zero trust removes implicit network trust',
            'Capabilities carry precise, unforgeable authority',
            'Dynamic authz evaluates context at request time',
            'Escalation is temporary, approved, and expiring',
        ],
        'further': [
            {'title': 'Zero Trust Architecture — NIST SP 800-207', 'url': 'https://csrc.nist.gov/publications/detail/sp/800-207/final'},
            {'title': 'Google BeyondCorp', 'url': 'https://research.google/pubs/pub43231/'},
        ],
    },
    {
        'title': 'Least Privilege: Review & Mastery Quiz',
        'desc': 'Scenario questions on scoping, IAM, and zero trust.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate least-privilege concepts',
            'Scope grants correctly',
            'Design zero-trust access',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Least privilege grants? (A: everything / B: the minimum needed / C: admin by default)',
                'Q2: Blast radius scales with? (A: granted privilege / B: team size / C: latency)',
                'Q3: Zero trust assumes? (A: the network is trusted / B: nothing is implicitly trusted / C: VPN is enough)',
                'Q4: True or false: short-lived credentials reduce leaked-key risk.',
                'Q5: Temporary escalation should have? (A: approval and expiry / B: no limit / C: a wiki note)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A leaked read-only reports key exposes all customer data because the reports bucket contains PII. Redesign the bucket layout and policy so a report key cannot reach PII.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "admin for everyone is simpler" is how breaches become total.'},
        ],
        'takeaways': [
            'Q1: B; Q2: A; Q3: B; Q4: true; Q5: A',
            'Scope by resource, row, column, and time',
            'Zero trust and capabilities operationalize it',
        ],
    },
])
