#!/usr/bin/env python3
"""Deep curriculum data batch 3: cqrs, decorator, event-sourcing, facade, factory, fanout."""

TOPICS = {}


def _t(slug, topics):
    TOPICS[slug] = topics
    return topics


# ─────────────────────────────────────────────────────────────────────────────
# CQRS
# ─────────────────────────────────────────────────────────────────────────────
_t('cqrs', [
    {
        'title': 'CQRS: Separate Commands from Queries',
        'desc': 'Using different models for writes and reads so each can be optimized independently.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the CQRS intent',
            'Separate command and query models',
            'Understand when the split pays off',
            'Compare with CQS at the method level',
        ],
        'prereqs': ['principles/cqs', 'patterns/repository'],
        'sections': [
            {'heading': 'The Idea', 'paras': [
                'CQRS splits the data path: commands (writes) go to a transactional write model; queries (reads) are served by optimized read models. They may even be different databases — the write model normalized, the read model denormalized for the exact query shapes.',
                'The cost is eventual consistency between the models, so CQRS pays off when reads and writes have sharply different shapes, volumes, or scaling needs.',
            ], 'code': {'lang': 'text', 'body': '''
CQRS topology:
  POST /orders   -> CommandService -> write model (normalized, transactional)
  OrderCreated   -> event -> projector -> read model (denormalized)
  GET /orders    -> QueryService  -> read model (fast, query-shaped)

  Consistency: eventual between write model and read model.
  Payoff: scale reads independently; shape reads for the UI.'''}},
            {'heading': 'CQS vs CQRS', 'paras': [
                'CQS is method-level: commands return nothing, queries mutate nothing. CQRS is architecture-level: commands and queries have separate models, stores, and often separate services. CQRS is CQS taken to the data-model scale.',
            ]},
        ],
        'practice': {
            'title': 'Split the Models',
            'intro': 'An orders service: writes are complex; the dashboard queries aggregate by region and status.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the command model (normalized, transactional).'},
                {'label': 'Task 2', 'text': 'Design the read model (denormalized dashboard rows).'},
                {'label': 'Task 3', 'text': 'Decide the synchronization: synchronous projection or event-driven, and the lag each accepts.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why CQRS trades consistency for read/write independence. Start with the projection lag.'},
            {'label': 'Compare & Contrast', 'text': 'Compare CQRS with a plain repository over one database. What concrete problem does the split solve?'},
            {'label': 'Boundary Testing', 'text': 'A user reads a just-created order and the read model lags. Design the read-your-writes path.'},
        ],
        'takeaways': [
            'Commands and queries get separate models',
            'Read models are shaped for query patterns',
            'Consistency between models is eventual',
            'CQRS pays off when read/write shapes diverge',
        ],
        'further': [
            {'title': 'CQRS — Martin Fowler', 'url': 'https://martinfowler.com/bliki/CQRS.html'},
            {'title': 'CQRS Journey — Microsoft', 'url': 'https://learn.microsoft.com/en-us/previous-versions/msp-n-p/jj554200(v=pandp.10)'},
        ],
    },
    {
        'title': 'CQRS in Production: Projections and Read Models',
        'desc': 'Building projections, managing lag, and scaling reads independently.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design event-driven projections',
            'Rebuild read models from scratch',
            'Handle projection failures',
            'Scale reads with read replicas',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Projections', 'paras': [
                'A projector consumes the write stream and builds read models. The projection is idempotent: replaying the stream reconstructs the model exactly, so a failed projector restarts from its last checkpoint and rebuilds only the gap.',
            ], 'code': {'lang': 'go', 'body': '''
// Idempotent projector: replay-safe read model builder
func project(ctx context.Context, events <-chan Event) error {
    for ev := range events {
        switch e := ev.(type) {
        case OrderCreated:
            // upsert: same event replayed = same row (idempotent)
            upsertOrderSummary(ctx, e.OrderID, e.Region, e.Amount)
        case OrderPaid:
            markPaid(ctx, e.OrderID, e.PaidAt)
        }
        checkpoint(ev.Sequence)   // resume from here after a crash
    }
    return nil
}'''}},
            {'heading': 'Rebuild and Lag', 'paras': [
                'Read models can be rebuilt from the entire stream when the projection schema changes. Lag is monitored: a stale read model silently serves old data, so lag alerts are the CQRS equivalent of a health check.',
            ]},
        ],
        'practice': {
            'title': 'Design the Projection Pipeline',
            'intro': 'A reporting read model aggregates orders by region and hour.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the projector, its checkpointing, and idempotent upserts.'},
                {'label': 'Task 2', 'text': 'Design the full rebuild when the aggregation schema changes.'},
                {'label': 'Task 3', 'text': 'Set the lag alert and the degraded-read response during a rebuild.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why projections must be idempotent and checkpointed. Ask me to trace a crash mid-project.'},
            {'label': 'Implementation Design', 'text': 'Design a read model for search: orders indexed by status, region, and SKU. What is the projection and its lag budget?'},
            {'label': 'Boundary Testing', 'text': 'The event stream has a gap from an upstream outage. Design the reconciliation that fills the gap.'},
        ],
        'takeaways': [
            'Projections are idempotent and checkpointed',
            'Full rebuilds are a first-class operation',
            'Lag is monitored like any health metric',
            'Read models scale independently of writes',
        ],
        'further': [
            {'title': 'Event Sourcing + CQRS — Martin Fowler', 'url': 'https://martinfowler.com/eaaDev/EventSourcing.html'},
            {'title': 'Change Data Capture (Debezium)', 'url': 'https://debezium.io/'},
        ],
    },
    {
        'title': 'Advanced CQRS: Event Sourcing and Sagas',
        'desc': 'Event-sourced write models, saga orchestration, and consistency management.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Combine CQRS with event sourcing',
            'Orchestrate sagas across command sides',
            'Manage schema evolution of events',
            'Choose CQRS complexity deliberately',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Event-Sourced Write Model', 'paras': [
                'The command side can be event-sourced: every command produces an event appended to the log, and aggregate state is derived by replay. The events ARE the write model — perfect audit, easy projections, no lost updates.',
            ], 'code': {'lang': 'text', 'body': '''
Event-sourced command side:
  Command: PlaceOrder{id, items, region}
  -> validates against derived state
  -> appends OrderCreated{id, items, region}   (the only truth)
  -> state = fold(replay(events))
  Query side: projections consume the same events.

Sagas: each step is a command on its own aggregate;
failures emit compensating commands.'''}},
            {'heading': 'The Cost-Benefit', 'paras': [
                'CQRS + event sourcing is powerful and heavy: event versioning, replay infrastructure, projection management, and eventual consistency everywhere. The discipline: start with a plain repository; adopt CQRS when read/write divergence or scaling demands it; adopt event sourcing when the audit/rebuild story is worth the machinery.',
            ]},
        ],
        'practice': {
            'title': 'Design the Saga + Projection',
            'intro': 'An order saga spans orders, payments, and inventory; the dashboard needs aggregates.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the saga: commands per aggregate and compensating commands on failure.'},
                {'label': 'Task 2', 'text': 'Design the projection that builds dashboard aggregates from saga events.'},
                {'label': 'Task 3', 'text': 'Version the events so a schema change replays cleanly.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can articulate when event sourcing earns its cost and when it is ceremony.'},
            {'label': 'Implementation Design', 'text': 'Design a saga with compensating commands for a payment flow. What happens at each failure point?'},
            {'label': 'Boundary Testing', 'text': 'A projection and a saga consume the same event and both fail. Design the isolation so one does not block the other.'},
        ],
        'takeaways': [
            'Events are the write model; state is derived',
            'Sagas coordinate commands with compensations',
            'Event versioning keeps replays faithful',
            'Adopt the machinery on demonstrated need',
        ],
        'further': [
            {'title': 'Event Sourcing — Microsoft Docs', 'url': 'https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing'},
            {'title': 'Saga — Microservices.io', 'url': 'https://microservices.io/patterns/data/saga.html'},
        ],
    },
    {
        'title': 'CQRS: Review & Mastery Quiz',
        'desc': 'Scenario questions on split models, projections, and event sourcing.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate CQRS concepts',
            'Design projections',
            'Choose complexity deliberately',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: CQRS gives commands and queries? (A: separate models / B: one model / C: no models)',
                'Q2: Consistency between write and read models is? (A: eventual / B: immediate / C: absent)',
                'Q3: Projections must be? (A: idempotent / B: random / C: fast only)',
                'Q4: True or false: CQS is the method-level version of CQRS.',
                'Q5: Event sourcing stores? (A: events as truth / B: only state / C: only queries)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A social feed: writes are simple, reads are complex joins. Design the CQRS split, the projection, and the lag budget.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why CQRS is a trade-off, not a default.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'CQRS buys read/write independence at consistency cost',
            'Projections and lag management are the operational core',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# DECORATOR
# ─────────────────────────────────────────────────────────────────────────────
_t('decorator', [
    {
        'title': 'Decorator: Add Behavior Without Changing the Class',
        'desc': 'Wrapping an object with new capabilities while keeping the same interface.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the decorator intent',
            'Wrap objects with added behavior',
            'Compose multiple decorators',
            'Compare with inheritance',
        ],
        'prereqs': ['patterns/composite', 'patterns/adapter'],
        'sections': [
            {'heading': 'The Idea', 'paras': [
                'A decorator wraps an object and adds behavior, implementing the same interface. A coffee: an espresso wrapped by Milk decorator wrapped by Whip decorator. Each layer adds cost/behavior without touching the base class — decorators compose at runtime.',
            ], 'code': {'lang': 'java', 'body': '''
// Decorator: wrap with behavior, same interface
interface Coffee { double cost(); String description(); }

class Espresso implements Coffee {
    public double cost() { return 1.50; }
    public String description() { return "espresso"; }
}

class WithMilk implements Coffee {
    private final Coffee base;
    WithMilk(Coffee base) { this.base = base; }
    public double cost() { return base.cost() + 0.30; }
    public String description() { return base.description() + " + milk"; }
}

Coffee c = new WithMilk(new Espresso());   // compose at runtime
// New toppings = new decorator classes; the base never changes.'''}},
            {'heading': 'Why Not Inheritance', 'paras': [
                'Inheritance for every combination explodes (EspressoMilkWhip, LatteCaramelNoWhip...). Decorators compose the pieces at runtime — the number of classes is the number of toppings, not the number of combinations.',
            ]},
        ],
        'practice': {
            'title': 'Decorate the Stream',
            'intro': 'A text stream needs encryption, compression, and buffering — in any combination.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the Stream interface (read/write).'},
                {'label': 'Task 2', 'text': 'Implement FileStream plus EncryptedStream, CompressedStream, BufferedStream decorators.'},
                {'label': 'Task 3', 'text': 'Compose a compressed+encrypted stream and show the layer order matters.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why decorators beat inheritance for combinatorial behavior. Start with the class count.'},
            {'label': 'Compare & Contrast', 'text': 'Compare decorator with adapter (interface change), proxy (access control), and composite (trees).'},
            {'label': 'Boundary Testing', 'text': 'Two decorators conflict (encrypt after compress vs compress after encrypt). Design the ordering rule or the guard.'},
        ],
        'takeaways': [
            'Decorators add behavior via wrapping',
            'Composition beats inheritance for combinations',
            'Layer order is part of the behavior',
            'The interface stays unchanged',
        ],
        'further': [
            {'title': 'Decorator — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/decorator'},
            {'title': 'Decorator Pattern — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Decorator_pattern'},
        ],
    },
    {
        'title': 'Decorator in Production: Middleware and Observability',
        'desc': 'Decorators for logging, caching, and retries around services.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Wrap services with cross-cutting decorators',
            'Compose observability stacks',
            'Keep decorators interchangeable',
            'Test decorated stacks',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Service Decorators', 'paras': [
                'A repository interface decorated with a CacheDecorator, a MetricsDecorator, and a RetryDecorator gives every capability without touching the repository — or the callers. Cross-cutting concerns become composable layers.',
            ], 'code': {'lang': 'java', 'body': '''
// Service decorators: stack cross-cutting concerns
interface UserRepo {
    Optional<User> find(String id);
}

class CacheDecorator implements UserRepo {
    private final UserRepo inner;
    CacheDecorator(UserRepo inner) { this.inner = inner; }
    public Optional<User> find(String id) {
        // cache-first; fall back to inner on miss
        return cached(id).or(() -> inner.find(id));
    }
}

UserRepo repo = new MetricsDecorator(
                    new CacheDecorator(
                    new RetryDecorator(
                        new DbUserRepo())));   // stack order = behavior'''}},
            {'heading': 'Interchangeable Stacks', 'paras': [
                'Because decorators implement the same interface, stacks are interchangeable: tests use an in-memory repo with no decorators, production stacks them all. The composition root decides the stack; the application never knows.',
            ]},
        ],
        'practice': {
            'title': 'Stack the Decorators',
            'intro': 'A payment client needs retries, circuit breaking, metrics, and logging.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Implement the four decorators over the PaymentClient interface.'},
                {'label': 'Task 2', 'text': 'Decide the stack order and justify (metrics outermost, retries inside circuit breaker?).'},
                {'label': 'Task 3', 'text': 'Show the test stack (no decorators) and the prod stack (all four) share the same interface.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why decorator order changes behavior (retry inside vs outside a circuit breaker). Ask me to pick the right order.'},
            {'label': 'Implementation Design', 'text': 'Design an observability decorator that measures latency, counts errors, and propagates trace IDs. What does it add to the interface?'},
            {'label': 'Boundary Testing', 'text': 'A decorator swallows an exception to return a fallback. Design the flag that keeps the original error observable.'},
        ],
        'takeaways': [
            'Cross-cutting concerns become composable layers',
            'Stack order is behavior — choose deliberately',
            'The composition root chooses the stack',
            'Test stacks and prod stacks share the interface',
        ],
        'further': [
            {'title': 'Decorator Pattern — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/decorator'},
            {'title': 'Fault Tolerance with Decorators (Resilience4j)', 'url': 'https://resilience4j.readme.io/'},
        ],
    },
    {
        'title': 'Advanced Decorator: Dynamic and Transactional Wrapping',
        'desc': 'Runtime-assembled decorator stacks and transactional wrappers.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Assemble decorator stacks dynamically',
            'Wrap transactions and sessions',
            'Manage decorator state and identity',
            'Avoid decorator over-wrapping',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Dynamic Stacks', 'paras': [
                'Feature flags and tenant configs can assemble different decorator stacks per request: tenant A gets caching + metrics, tenant B gets metrics only. A stack factory builds the chain per context at the composition root.',
            ], 'code': {'lang': 'python', 'body': '''
# Dynamic stack assembly per tenant
def build_repo(tenant):
    repo = DbUserRepo()
    if tenant.cache_enabled:
        repo = CacheDecorator(repo)
    if tenant.trace_enabled:
        repo = TraceDecorator(repo)
    repo = MetricsDecorator(repo)     # metrics always
    return repo

# Flags change stacks live without touching callers.'''}},
            {'heading': 'Transactional Decorators', 'paras': [
                'A transactional decorator wraps a method so it joins or starts a transaction, commits on success, rolls back on failure — leaving the business method free of transaction code. Nested decorators must cooperate (join the outer transaction, not nest blindly).',
            ]},
        ],
        'practice': {
            'title': 'Design the Dynamic Stack',
            'intro': 'A multi-tenant repo with per-tenant caching and tracing flags.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Build the stack factory keyed by tenant config.'},
                {'label': 'Task 2', 'text': 'Add the transactional decorator with correct join semantics.'},
                {'label': 'Task 3', 'text': 'Design the identity problem: a decorated object compared by identity breaks. Document the fix (compare by interface semantics).'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why transactional decorators must join, not nest.'},
            {'label': 'Implementation Design', 'text': 'Design a session decorator that opens, commits, and closes around a unit of work. Where does it sit in the stack?'},
            {'label': 'Boundary Testing', 'text': 'Ten decorators deep hides a buggy middle layer. Design the observability (stack trace per layer) that finds it.'},
        ],
        'takeaways': [
            'Stack factories assemble decorators per context',
            'Transactional decorators must join, not nest',
            'Identity comparisons break under wrapping',
            'Observable layers keep deep stacks debuggable',
        ],
        'further': [
            {'title': 'Spring @Transactional (the classic transactional decorator)', 'url': 'https://docs.spring.io/spring-framework/reference/data-access/transaction/'},
            {'title': 'Decorator — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/decorator'},
        ],
    },
    {
        'title': 'Decorator: Review & Mastery Quiz',
        'desc': 'Scenario questions on wrapping, stacking, and composition.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate decorator concepts',
            'Compose behavior stacks',
            'Choose stack order',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: A decorator? (A: wraps and adds behavior / B: changes the interface / C: creates objects)',
                'Q2: Decorators beat inheritance for? (A: combinations / B: speed / C: memory)',
                'Q3: Stack order matters because it? (A: changes behavior / B: never matters / C: is cosmetic)',
                'Q4: True or false: decorators must preserve the interface.',
                'Q5: An adapter differs from a decorator by? (A: changing the interface / B: adding behavior / C: being faster)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'An HTTP client needs logging, retry, and timeout decorators. Stack them, justify the order, and show the undecorated test version.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why decorators keep cross-cutting code out of business classes.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Decorators compose behavior at runtime',
            'Order, identity, and observability are the care points',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# EVENT SOURCING
# ─────────────────────────────────────────────────────────────────────────────
_t('event-sourcing', [
    {
        'title': 'Event Sourcing: The Log Is the Truth',
        'desc': 'Storing every state change as an event and deriving state by replay.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain event sourcing',
            'Derive state by replaying events',
            'List the audit and rebuild benefits',
            'Understand the costs',
        ],
        'prereqs': ['principles/cqs', 'patterns/cqrs'],
        'sections': [
            {'heading': 'The Idea', 'paras': [
                'Instead of storing the current state, store every event that changed it: OrderCreated, OrderPaid, OrderShipped. Current state is derived by replaying events. The event log is the only source of truth — it cannot be lost and it records exactly what happened.',
            ], 'code': {'lang': 'python', 'body': '''
# Event sourcing: state = fold over events
def apply(state, event):
    if event.type == 'created':   return {**state, 'id': event.id, 'status': 'created'}
    if event.type == 'paid':      return {**state, 'status': 'paid', 'paid_at': event.at}
    if event.type == 'shipped':   return {**state, 'status': 'shipped'}
    return state

def rebuild(events):
    state = {}
    for e in sorted(events, key=lambda x: x.sequence):
        state = apply(state, e)
    return state

# Audit: every change is in the log. Rebuild: replay from scratch.'''}},
            {'heading': 'Benefits and Costs', 'paras': [
                'Benefits: perfect audit trail, full history, rebuildable state, projections for any view, and no lost updates (concurrent writes append). Costs: replay infrastructure, event versioning, eventual projections, and a learning curve.',
            ]},
        ],
        'practice': {
            'title': 'Model the Ledger',
            'intro': 'A bank account: deposit, withdraw, and freeze events.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the events and the apply() fold.'},
                {'label': 'Task 2', 'text': 'Rebuild the balance from a 1,000-event log and verify.'},
                {'label': 'Task 3', 'text': 'Show the audit answer: "what happened to this account, in order?"'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why the event log beats stored state for audit. Start with what "what happened" requires.'},
            {'label': 'Compare & Contrast', 'text': 'Compare event sourcing with a plain update-in-place store and with command sourcing.'},
            {'label': 'Boundary Testing', 'text': 'A buggy old event is replayed after a rule change. Design the versioning that keeps replays faithful.'},
        ],
        'takeaways': [
            'The event log is the source of truth',
            'State is derived by replay',
            'Audit and rebuild come free',
            'Versioning and snapshots manage the costs',
        ],
        'further': [
            {'title': 'Event Sourcing — Martin Fowler', 'url': 'https://martinfowler.com/eaaDev/EventSourcing.html'},
            {'title': 'Event Sourcing — Microsoft Docs', 'url': 'https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing'},
        ],
    },
    {
        'title': 'Event Sourcing in Production: Streams and Snapshots',
        'desc': 'Event stores, snapshots, and versioned streams at scale.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Store events in streams',
            'Use snapshots to bound replay cost',
            'Version events for schema evolution',
            'Concurrently append without conflicts',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Streams and Snapshots', 'paras': [
                'Events live in per-aggregate streams (Kafka, EventStore, or a table). Replaying a 10-year stream is slow, so snapshots store periodic state: rebuild loads the last snapshot, then replays only the events after it.',
            ], 'code': {'lang': 'sql', 'body': '''
-- Events table with a version per aggregate
CREATE TABLE events (
    aggregate_id uuid,
    sequence    bigint,
    type        text,
    payload     jsonb,
    created_at  timestamptz,
    PRIMARY KEY (aggregate_id, sequence)
);
-- Snapshot table: state at a sequence, to bound replay
CREATE TABLE snapshots (
    aggregate_id uuid PRIMARY KEY,
    at_sequence bigint,
    state jsonb
);
-- Rebuild: load snapshot at seq N, replay events > N.'''}},
            {'heading': 'Versioning and Appends', 'paras': [
                'Events evolve: an old OrderCreated lacks a field new code expects. Version events (v1, v2) and let the fold handle each version. Concurrent appends are safe because appends are additive — no overwrite conflicts, only ordering.',
            ]},
        ],
        'practice': {
            'title': 'Design the Stream Store',
            'intro': 'A 10M-event order stream; reads must be fast and audits complete.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the events + snapshots schema and the rebuild algorithm.'},
                {'label': 'Task 2', 'text': 'Version the OrderCreated event and migrate the fold.'},
                {'label': 'Task 3', 'text': 'Design the snapshot cadence: every N events, or on demand, and why.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why snapshots are the scalability lever for event sourcing. Ask me to compute the replay savings.'},
            {'label': 'Implementation Design', 'text': 'Design a versioned event stream with upcaster functions for a payroll system. What happens to old payouts?'},
            {'label': 'Boundary Testing', 'text': 'Two snapshots disagree with the event log. Design the verification (replay diff) that detects drift.'},
        ],
        'takeaways': [
            'Streams hold per-aggregate event sequences',
            'Snapshots bound replay cost',
            'Versioning keeps old events replayable',
            'Append-only means concurrency is safe',
        ],
        'further': [
            {'title': 'EventStoreDB', 'url': 'https://www.eventstore.com/'},
            {'title': 'Kafka as an Event Store', 'url': 'https://kafka.apache.org/documentation/'},
        ],
    },
    {
        'title': 'Advanced Event Sourcing: Projections and Sagas',
        'desc': 'Projections over streams, sagas coordinated by events, and the full picture.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Build projections from event streams',
            'Orchestrate sagas with events',
            'Handle event-driven consistency',
            'Operate event sourcing safely',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Projections as Views', 'paras': [
                'Every read model is a projection over the stream: a balance, a dashboard, a search index. Projections are idempotent functions of the stream, rebuildable at any time — event sourcing makes the read side a pure derived concern.',
            ], 'code': {'lang': 'go', 'body': '''
// Projection: pure function of the stream -> rebuildable views
func projectBalance(events []Event) Balance {
    var b Balance
    for _, e := range events {
        switch e.Type {
        case "deposit":  b.Amount += e.Amount
        case "withdraw": b.Amount -= e.Amount
        }
    }
    return b
}
// Same function builds the current balance or the balance at any past
// point — cut the stream at sequence N and replay.'''}},
            {'heading': 'Sagas and the Danger Zone', 'paras': [
                'A saga listens to events and issues commands: OrderCreated triggers the ChargeAccount command; PaymentSucceeded triggers ShipOrder. Failures produce compensating commands. The danger: saga logic distributed across many consumers becomes hard to reason about — centralize orchestration deliberately.',
            ]},
        ],
        'practice': {
            'title': 'Design the Saga + Projection',
            'intro': 'An order saga: create order, charge, reserve inventory, ship; the dashboard needs live totals.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the events and the saga state machine (which event triggers which command).'},
                {'label': 'Task 2', 'text': 'Design the compensation for each failure point.'},
                {'label': 'Task 3', 'text': 'Build the dashboard projection and its rebuild-from-scratch path.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why sagas need idempotent commands and compensations.'},
            {'label': 'Implementation Design', 'text': 'Design a saga as a state machine: events in, commands out, timeouts for stuck states. Where do timeouts live?'},
            {'label': 'Boundary Testing', 'text': 'An event arrives out of order after a partition. Design the saga handling for gaps and duplicates.'},
        ],
        'takeaways': [
            'Read models are projections — pure and rebuildable',
            'Sagas coordinate via events with compensations',
            'Orchestration centralization keeps sagas sane',
            'Out-of-order and duplicate events need explicit handling',
        ],
        'further': [
            {'title': 'Saga — Microservices.io', 'url': 'https://microservices.io/patterns/data/saga.html'},
            {'title': 'Eventuate Tram (saga framework)', 'url': 'https://eventuate.io/'},
        ],
    },
    {
        'title': 'Event Sourcing: Review & Mastery Quiz',
        'desc': 'Scenario questions on the log, snapshots, and projections.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate event sourcing concepts',
            'Design streams and snapshots',
            'Build projections',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: In event sourcing, the truth is? (A: the current state / B: the event log / C: the cache)',
                'Q2: State is derived by? (A: replay / B: guessing / C: caching)',
                'Q3: Snapshots bound? (A: replay cost / B: storage / C: nothing)',
                'Q4: True or false: appends are safe from conflicts.',
                'Q5: Read models are? (A: projections / B: the write truth / C: backups)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A compliance system must prove the full history of a loan. Design the event store, the snapshot strategy, and the audit query.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why the event log is more truthful than stored state.'},
        ],
        'takeaways': [
            'Q1: B; Q2: A; Q3: A; Q4: true; Q5: A',
            'The log never lies — state is derived',
            'Snapshots, versioning, and projections make it scale',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# FACADE
# ─────────────────────────────────────────────────────────────────────────────
_t('facade', [
    {
        'title': 'Facade: One Simple Door to a Complex System',
        'desc': 'Providing a simple interface over a complex subsystem.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the facade intent',
            'Simplify a complex subsystem',
            'Keep the subsystem untouched',
            'Distinguish from adapter',
        ],
        'prereqs': ['patterns/adapter', 'patterns/singleton'],
        'sections': [
            {'heading': 'The Idea', 'paras': [
                'A subsystem has many moving parts: an order flow touches inventory, billing, shipping, and notifications. A facade offers one simple method — placeOrder() — that coordinates them. Callers see one door; the subsystem stays intact behind it.',
            ], 'code': {'lang': 'java', 'body': '''
// Facade: one simple API over a complex subsystem
class OrderFacade {
    private final Inventory inv;
    private final Billing billing;
    private final Shipping ship;

    OrderFacade(Inventory i, Billing b, Shipping s) { ... }

    public OrderResult placeOrder(Cart cart, Payment pmt) {
        if (!inv.reserve(cart)) return OrderResult.outOfStock();
        ChargeResult ch = billing.charge(pmt, cart.total());
        if (!ch.ok) { inv.release(cart); return OrderResult.chargeFailed(); }
        String tracking = ship.schedule(cart);
        return OrderResult.ok(tracking);
    }
}
// Callers never touch inventory, billing, or shipping.'''}},
            {'heading': 'Facade vs Adapter', 'paras': [
                'An adapter translates an interface so two things can talk. A facade simplifies a subsystem for its callers — the intent is convenience and decoupling, not interface compatibility.',
            ]},
        ],
        'practice': {
            'title': 'Facade the Checkout',
            'intro': 'Checkout currently calls 5 subsystems in sequence with error handling at the call site.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Identify the 5 subsystems and their interactions.'},
                {'label': 'Task 2', 'text': 'Design the facade method with its result type and error paths.'},
                {'label': 'Task 3', 'text': 'Move the orchestration into the facade and show callers simplify.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why a facade reduces caller coupling without hiding capability. Start with the result type.'},
            {'label': 'Compare & Contrast', 'text': 'Compare facade with adapter and with the mediator pattern. When is each the right simplification?'},
            {'label': 'Boundary Testing', 'text': 'A caller legitimately needs a subsystem detail the facade hides. Design the escape hatch that does not defeat the facade.'},
        ],
        'takeaways': [
            'Facades simplify complex subsystems',
            'The subsystem stays intact behind the door',
            'Callers decouple from subsystem internals',
            'Facade simplifies; adapter translates; mediator coordinates peers',
        ],
        'further': [
            {'title': 'Facade — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/facade'},
            {'title': 'Facade Pattern — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Facade_pattern'},
        ],
    },
    {
        'title': 'Facade in Production: SDKs and Libraries',
        'desc': 'The public API of an SDK as a facade over internal modules.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design SDK public facades',
            'Keep internals replaceable',
            'Version the facade surface',
            'Test through the facade',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'SDK Facades', 'paras': [
                'A good SDK exposes a small facade and hides the engine: the client calls client.send(message) and never sees connection pools, retries, and serialization. The facade is the versioned public surface; internals can change freely beneath it.',
            ], 'code': {'lang': 'typescript', 'body': '''
// SDK facade: the only public surface
export class Client {
    private readonly conn: ConnectionManager;
    private readonly serializer: Serializer;

    constructor(opts: ClientOptions) {   // options are the DSL
        this.conn = new ConnectionManager(opts);
        this.serializer = new Serializer(opts.format);
    }

    async send(msg: Message): Promise<MessageId> {
        const wire = this.serializer.serialize(msg);
        const id = await this.conn.send(wire);   // retries inside
        return id;
    }
}
// Internal modules are never exported. The facade IS the API.'''}},
            {'heading': 'Testing Through the Facade', 'paras': [
                'Integration tests drive the SDK through the facade — the same path users take. The facade also gives a natural seam for contract tests: the public surface is the contract, and internals are free to change.',
            ]},
        ],
        'practice': {
            'title': 'Design the SDK Surface',
            'intro': 'A metrics SDK: users need sendMetric, flush, and shutdown — nothing else.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the facade class and its options type.'},
                {'label': 'Task 2', 'text': 'Hide the batching, retry, and serialization internals behind it.'},
                {'label': 'Task 3', 'text': 'Write the facade contract test and the internal refactor that proves internals are replaceable.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why the facade is the versioned contract of an SDK and internals are free to evolve.'},
            {'label': 'Implementation Design', 'text': 'Design a library that hides a web socket layer behind a chat.send() facade. What does the facade promise?'},
            {'label': 'Boundary Testing', 'text': 'A power user needs a knob the facade hides. Design the advanced-options surface that does not break the facade.'},
        ],
        'takeaways': [
            'The facade is the SDK\'s versioned public surface',
            'Internals evolve freely beneath it',
            'Options types are the configuration DSL',
            'Contract tests pin the public surface',
        ],
        'further': [
            {'title': 'API Design — Google API Design Guide', 'url': 'https://cloud.google.com/apis/design'},
            {'title': 'Semantic Versioning for SDKs', 'url': 'https://semver.org/'},
        ],
    },
    {
        'title': 'Advanced Facade: Bounded Facades and Fragile Foundations',
        'desc': 'Multiple facades per subsystem, and keeping facades from hiding too much.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Design multiple facades per audience',
            'Balance hiding with capability',
            'Keep facades thin and honest',
            'Evolve facades safely',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Facades per Audience', 'paras': [
                'Different callers need different simplifications of the same subsystem: an admin facade (reconfigure, inspect), an operator facade (metrics, drain), and a user facade (use). Each facade is a role-shaped door — the interface segregation principle applied to facades.',
            ], 'code': {'lang': 'text', 'body': '''
Facades per audience over one engine:
  UserFacade:     start, pause, stop            (the product)
  OperatorFacade: status, drain, metrics        (the SRE)
  AdminFacade:    configure, migrate, snapshot  (the admin)
Each facade is thin: it delegates to the engine, never re-implements.
Thin facades stay honest; thick ones become new subsystems.'''}},
            {'heading': 'The Fragile Foundation', 'paras': [
                'A facade that hides error modes can become a fragile foundation: callers never see failures until they burst through. Facades should return explicit result types, surface retryable states, and never swallow errors silently — the door must be honest about what is behind it.',
            ]},
        ],
        'practice': {
            'title': 'Design the Facade Set',
            'intro': 'A video pipeline has user, operator, and admin audiences.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the three facades and what each exposes.'},
                {'label': 'Task 2', 'text': 'Verify each facade stays thin (delegates, never re-implements).'},
                {'label': 'Task 3', 'text': 'Design the error surface: what each audience can observe and what is always logged.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can articulate when one facade is enough and when per-audience facades pay off.'},
            {'label': 'Implementation Design', 'text': 'Design a facade that never hides failures: explicit result types and observable states. What does the caller\'s error handling look like?'},
            {'label': 'Boundary Testing', 'text': 'A facade hides a subsystem swap behind it. Design the versioning that keeps the swap invisible to callers.'},
        ],
        'takeaways': [
            'Per-audience facades shape the same engine',
            'Thin facades delegate; thick ones become subsystems',
            'Honest facades never swallow errors',
            'The facade can hide swaps, not failures',
        ],
        'further': [
            {'title': 'Facade — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/facade'},
            {'title': 'Interface Segregation + Facade', 'url': 'https://martinfowler.com/bliki/RoleInterface.html'},
        ],
    },
    {
        'title': 'Facade: Review & Mastery Quiz',
        'desc': 'Scenario questions on simplification, audiences, and honesty.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate facade concepts',
            'Design thin facades',
            'Keep doors honest',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: A facade provides? (A: a simple interface over a complex subsystem / B: a translation layer / C: a cache)',
                'Q2: The subsystem behind a facade? (A: stays intact / B: is rewritten / C: disappears)',
                'Q3: A facade differs from an adapter by? (A: simplifying vs translating / B: being faster / C: using threads)',
                'Q4: True or false: facades should swallow errors silently.',
                'Q5: Per-audience facades are? (A: role-shaped doors / B: copies / C: singletons)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A checkout subsystem has 6 classes and error-prone orchestration. Design the facade, its result types, and the caller\'s new simplicity.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why a facade that hides failures is a fragile foundation.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: false; Q5: A',
            'Facades simplify and decouple',
            'Thin, honest facades are the sustainable ones',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# FACTORY (FACTORY METHOD)
# ─────────────────────────────────────────────────────────────────────────────
_t('factory', [
    {
        'title': 'Factory Method: Let Subclasses Create',
        'desc': 'Deferring object creation to subclasses through one overridable method.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the factory method intent',
            'Defer creation to subclasses',
            'Compare with abstract factory and simple factory',
            'Apply the new keyword rule',
        ],
        'prereqs': ['patterns/abstract-factory', 'patterns/singleton'],
        'sections': [
            {'heading': 'The Idea', 'paras': [
                'The factory method lets a class delegate creation to subclasses: the base defines create() abstractly, each subclass returns its own product. Callers depend on the base class; the "which product" decision moves to the subclass.',
            ], 'code': {'lang': 'java', 'body': '''
// Factory method: creation is a subclass decision
abstract class Dialog {
    abstract Button createButton();          // the factory method

    void render() {
        Button b = createButton();           // polymorphic creation
        b.onClick(() -> System.out.println("clicked"));
        b.render();
    }
}

class WebDialog extends Dialog {
    Button createButton() { return new HtmlButton(); }
}
class MobileDialog extends Dialog {
    Button createButton() { return new TouchButton(); }
}
// render() works for any subclass; creation stays in the subclass.'''}},
            {'heading': 'The new-Keyword Rule', 'paras': [
                'Direct new in business code couples the caller to a concrete class. Factory methods and injected factories localize creation so the caller depends on abstractions. The rule: put new behind a factory when the concrete choice should vary.',
            ]},
        ],
        'practice': {
            'title': 'Defer the Parser Choice',
            'intro': 'An importer parses JSON, CSV, or XML based on the file type.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the Parser interface and the three implementations.'},
                {'label': 'Task 2', 'text': 'Design the factory method on the importer (or a ParserFactory) that returns the right parser.'},
                {'label': 'Task 3', 'text': 'Add a fourth format with zero changes to the import flow.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about the difference between a factory method (overridable) and a simple factory (a function with a switch).'},
            {'label': 'Compare & Contrast', 'text': 'Compare factory method with abstract factory and with dependency injection.'},
            {'label': 'Boundary Testing', 'text': 'The factory returns a product that needs different setup per subtype. Design the factory that handles divergent construction.'},
        ],
        'takeaways': [
            'Factory methods defer creation to subclasses',
            'Callers depend on abstractions, not concretes',
            'The new keyword hides behind factories',
            'Adding a product = adding a subclass',
        ],
        'further': [
            {'title': 'Factory Method — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/factory-method'},
            {'title': 'Factory Method — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Factory_method_pattern'},
        ],
    },
    {
        'title': 'Factory in Production: DI and Parsers',
        'desc': 'Factories in dependency injection, parser selection, and provider choice.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Use factories with DI containers',
            'Select implementations by context',
            'Test factory output',
            'Avoid factory misuse',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Factories and DI', 'paras': [
                'DI containers provide singletons; factories provide context-dependent instances. A factory that receives the container and builds the right implementation per request (per tenant, per format) combines the two cleanly.',
            ], 'code': {'lang': 'java', 'body': '''
// Factory injected by the container, produces per-context products
@Singleton
class PaymentFactory {
    private final Map<String, Provider> providers;   // injected set

    PaymentFactory(List<Provider> all) {
        this.providers = all.stream()
            .collect(toMap(Provider::name, p -> p));
    }

    Provider forCurrency(String currency) {
        return providers.getOrDefault(currency, providers.get("default"));
    }
}'''}},
            {'heading': 'Misuse', 'paras': [
                'Factories are misused when they replace a plain constructor for no varying reason, or when they grow into god-objects that construct everything. The smell: a factory with a parameter that switches on every product type — that is a simple factory that should be a registry or config.',
            ]},
        ],
        'practice': {
            'title': 'Build the Context Factory',
            'intro': 'A notification service chooses email, SMS, or push by the user\'s channel preference.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the Channel interface and three implementations.'},
                {'label': 'Task 2', 'text': 'Build the factory that selects by preference with a default fallback.'},
                {'label': 'Task 3', 'text': 'Add a fourth channel (WhatsApp) with zero changes to the sender flow.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me when a factory is justified versus a direct constructor. Ask me to apply the "does the choice vary?" test.'},
            {'label': 'Implementation Design', 'text': 'Design a DI-registered factory for per-tenant storage. Where does the tenant context come from?'},
            {'label': 'Boundary Testing', 'text': 'The factory returns a product with an unsatisfied dependency. Design the startup validation that catches it.'},
        ],
        'takeaways': [
            'Factories combine with DI for context-dependent instances',
            'Selection by key with a default is the common shape',
            'The "does the choice vary?" test gates factory use',
            'Factory registries beat god-factories',
        ],
        'further': [
            {'title': 'Factory Method — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/factory-method'},
            {'title': 'Dependency Injection — Martin Fowler', 'url': 'https://martinfowler.com/articles/injection.html'},
        ],
    },
    {
        'title': 'Advanced Factory: Abstract Factories and Registries',
        'desc': 'Factories of factories, and registries that keep creation open-closed.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Compose factories hierarchically',
            'Build registries for open-closed creation',
            'Handle factory lifecycle',
            'Test factory hierarchies',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Hierarchies and Registries', 'paras': [
                'A registry of factories keeps creation open-closed: register(Key, Factory) at startup; new creators join by registration. A factory of factories (abstract factory) produces related products; the registry selects which family.',
            ], 'code': {'lang': 'python', 'body': '''
# Registry of factories: open-closed creation
class CreatorRegistry:
    def __init__(self):
        self.creators = {}

    def register(self, key, creator):
        self.creators[key] = creator

    def create(self, key, *args):
        if key not in self.creators:
            raise UnknownCreator(key)
        return self.creators[key](*args)

# Startup: register all known creators
registry.register('json', JsonParser.create)
registry.register('csv', CsvParser.create)
# New parser -> one registration line, core untouched.'''}},
            {'heading': 'Lifecycle and Testing', 'paras': [
                'Factories that hold resources (connection pools, clients) need lifecycle management: create, validate, and dispose hooks. Testing factory hierarchies uses a fake factory registered under the same key — the registry makes the swap trivial.',
            ]},
        ],
        'practice': {
            'title': 'Design the Creator Registry',
            'intro': 'A platform parses 6 formats and must add more without touching the core.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Build the registry and register six creators at startup.'},
                {'label': 'Task 2', 'text': 'Add a validation pass (each creator produces a working product).'},
                {'label': 'Task 3', 'text': 'Add lifecycle hooks (dispose) and the fake-factory test strategy.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain how a registry implements open-closed for creation.'},
            {'label': 'Implementation Design', 'text': 'Design a plugin loader where plugins register their creators on load. How do you validate and isolate a bad plugin?'},
            {'label': 'Boundary Testing', 'text': 'Two creators register the same key. Design the conflict policy (reject, last-wins, or namespace).'},
        ],
        'takeaways': [
            'Registries keep creation open-closed',
            'Startup validation catches bad creators early',
            'Lifecycle hooks manage factory resources',
            'Fake factories under the same key make testing trivial',
        ],
        'further': [
            {'title': 'Registry — Martin Fowler', 'url': 'https://martinfowler.com/eaaCatalog/registry.html'},
            {'title': 'Plugin Architecture', 'url': 'https://martinfowler.com/articles/osgi.html'},
        ],
    },
    {
        'title': 'Factory: Review & Mastery Quiz',
        'desc': 'Scenario questions on deferring creation, registries, and DI.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate factory concepts',
            'Design creation boundaries',
            'Keep creation open-closed',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: A factory method defers creation to? (A: subclasses / B: the caller / C: the database)',
                'Q2: The "does the choice vary?" test decides? (A: whether a factory is justified / B: the database / C: the UI)',
                'Q3: A registry keeps creation? (A: open for extension / B: fixed / C: hidden)',
                'Q4: True or false: direct new in business code couples callers to concretes.',
                'Q5: A factory that switches on every product type is a smell of? (A: god-factory / B: good design / C: DI)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'An exporter supports 5 formats with per-format options. Design the creation boundary: factory method, registry, or DI — and justify.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why creation belongs behind a boundary when the choice varies.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Factories localize the varying creation decision',
            'Registries make creation open for extension',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# FANOUT
# ─────────────────────────────────────────────────────────────────────────────
_t('fanout', [
    {
        'title': 'Fanout: One Write, Many Readers',
        'desc': 'Broadcasting a single event to many consumers efficiently.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the fanout intent',
            'Push vs pull fanout',
            'Compare with publish-subscribe',
            'Identify fanout in feeds and events',
        ],
        'prereqs': ['patterns/publish-subscribe', 'patterns/sharding'],
        'sections': [
            {'heading': 'The Idea', 'paras': [
                'Fanout delivers one write to many destinations: a celebrity post to a million inboxes, a config change to every node, an event to every subscriber. The two shapes are push (write to each destination) and pull (readers fetch and merge).',
            ], 'code': {'lang': 'text', 'body': '''
Fanout shapes:
  Push:  author posts -> write to 1M inboxes (fast reads, heavy writes)
  Pull:  author posts -> one timeline; readers fetch + merge (light writes)
  Hybrid: push to active readers, pull for the long tail

Real systems:
  Kafka: topic partitions broadcast to consumer groups
  Redis: pub/sub broadcasts to live subscribers
  Social feeds: push fanout with pull fallback'''}},
            {'heading': 'The Fanout Challenge', 'paras': [
                'The difficulty is scale and latency: a million-inbox write is a million writes. Fanout design balances write amplification against read latency — push makes reads instant and writes heavy; pull makes writes light and reads slower.',
            ]},
        ],
        'practice': {
            'title': 'Design the Feed Fanout',
            'intro': 'A social app: 1M users, celebrities post hourly, followers read on demand.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design push fanout: the writer fan-out job, batching, and retries.'},
                {'label': 'Task 2', 'text': 'Design the pull fallback for inactive users.'},
                {'label': 'Task 3', 'text': 'Compare write amplification and read latency for push vs pull vs hybrid.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about the trade-off between push and pull fanout. Start with read latency.'},
            {'label': 'Compare & Contrast', 'text': 'Compare fanout with publish-subscribe and with the observer pattern. When is each the right shape?'},
            {'label': 'Boundary Testing', 'text': 'A celebrity with 10M followers posts at peak. Design the fanout that does not collapse the write path.'},
        ],
        'takeaways': [
            'Fanout delivers one write to many readers',
            'Push = instant reads, heavy writes; pull = the reverse',
            'Hybrid fanout balances active and inactive readers',
            'Scale design is the whole game',
        ],
        'further': [
            {'title': 'Fanout on Twitter — InfoQ', 'url': 'https://www.infoq.com/presentations/ebay-fanout/'},
            {'title': 'Designing a News Feed (System Design Primer)', 'url': 'https://github.com/donnemartin/system-design-primer'},
        ],
    },
    {
        'title': 'Fanout in Production: Feeds and Event Buses',
        'desc': 'Timeline fanout, Kafka partitions, and broadcast at scale.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design timeline fanout',
            'Use Kafka-style partitioned fanout',
            'Handle fanout failures partially',
            'Monitor fanout lag',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Partitioned Fanout', 'paras': [
                'Kafka fanout: a topic has partitions; each message goes to one partition, and each consumer group reads all partitions. Fan-out to N consumer groups is inherent — every group reads every message. Within a group, partitions split the work.',
            ], 'code': {'lang': 'text', 'body': '''
Kafka fanout model:
  topic "user.events" (8 partitions)
  consumer group "analytics"  -> reads ALL events (fanout to group)
  consumer group "notify"     -> reads ALL events (independent fanout)
  consumer group "search"     -> reads ALL events
Each group is a fanout destination; partitions parallelize within.

Ordering guarantee: per partition, per key (e.g., per user).'''}},
            {'heading': 'Partial Failure', 'paras': [
                'A fanout to 100 destinations should not fail all when one is slow: per-destination queues, dead-letter paths, and independent retry budgets keep one bad consumer from blocking the broadcast. Fanout lag per destination is the monitoring unit.',
            ]},
        ],
        'practice': {
            'title': 'Design the Broadcast Pipeline',
            'intro': 'A config change must reach 500 services; three are slow.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the broadcast: per-service queues, timeouts, and retries.'},
                {'label': 'Task 2', 'text': 'Design the partial-failure policy: slow services lag, others proceed.'},
                {'label': 'Task 3', 'text': 'Design the lag dashboard and the "which services have not applied" query.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why fanout destinations need independent failure budgets. Ask me to trace one slow consumer.'},
            {'label': 'Implementation Design', 'text': 'Design a feature-flag broadcast to 500 nodes with per-node ack and timeout. What guarantees can you honestly make?'},
            {'label': 'Boundary Testing', 'text': 'A destination is down for an hour and misses the broadcast. Design the catch-up (replay or version check).'},
        ],
        'takeaways': [
            'Partitioned topics fan out per consumer group',
            'Per-destination budgets isolate slow consumers',
            'Fanout lag is the monitoring unit',
            'Down destinations need catch-up paths',
        ],
        'further': [
            {'title': 'Kafka Documentation', 'url': 'https://kafka.apache.org/documentation/'},
            {'title': 'Google Pub/Sub Fanout', 'url': 'https://cloud.google.com/pubsub/docs/fanout'},
        ],
    },
    {
        'title': 'Advanced Fanout: Hybrid and Adaptive Fanout',
        'desc': 'Hybrid push/pull, adaptive fanout, and fanout at internet scale.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Design hybrid fanout with pull fallback',
            'Adapt fanout to reader activity',
            'Fan out across regions',
            'Avoid fanout storms',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Hybrid Fanout', 'paras': [
                'The production shape: push to active readers (small inboxes), pull for inactive and long-tail users, with a merge on read. Activity-based classification decides who gets pushed — usually a recency threshold (active in N days).',
            ], 'code': {'lang': 'text', 'body': '''
Hybrid fanout algorithm:
  author posts post P
  for each follower F:
    if active(F): push P into F.inbox     # small set, fast
    else:         append P to F.pending    # lazy, merged on read
  read(F): merge(F.inbox, F.pending, author timelines)

  Adaptive: an inactive user who reads becomes active -> start pushing.
  A user inactive for 90 days stops receiving pushes.'''}},
            {'heading': 'Regional and Storm Control', 'paras': [
                'Cross-region fanout replicates the write, not a million messages: the post travels once; each region fans out locally. Storm control: fanout jobs are bounded (batches, queues), backpressure on the writer, and shedding of the lowest-priority destinations under load.',
            ]},
        ],
        'practice': {
            'title': 'Design the Hybrid Fanout',
            'intro': 'A video platform: 10M followers total, 5% active daily.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the active/inactive split and the threshold.'},
                {'label': 'Task 2', 'text': 'Design the merge-on-read for pull users.'},
                {'label': 'Task 3', 'text': "Design the regional replication and the fanout job's backpressure and shedding."},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why hybrid fanout is the standard production answer.'},
            {'label': 'Implementation Design', 'text': 'Design the fanout job with batch processing and backpressure: how does it survive a 10M-follower post?'},
            {'label': 'Boundary Testing', 'text': 'A follower list changes mid-fanout. Design the snapshot semantics (fan out to the follower set at publish time).'},
        ],
        'takeaways': [
            'Hybrid = push active + pull long tail',
            'Activity thresholds drive the split',
            'Regional fanout replicates once, fans out locally',
            'Bounded jobs and backpressure prevent storms',
        ],
        'further': [
            {'title': 'Timeline Architecture (System Design)', 'url': 'https://github.com/donnemartin/system-design-primer#design-a-social-media-feed'},
            {'title': 'Batching at Scale — Google SRE', 'url': 'https://sre.google/sre-book/'},
        ],
    },
    {
        'title': 'Fanout: Review & Mastery Quiz',
        'desc': 'Scenario questions on push/pull, partitions, and hybrids.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate fanout concepts',
            'Design feed fanout',
            'Handle scale and failure',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Push fanout makes reads? (A: instant / B: slow / C: impossible)',
                'Q2: Pull fanout makes writes? (A: light / B: heavy / C: nil)',
                'Q3: In Kafka, each consumer group reads? (A: all messages / B: one message / C: nothing)',
                'Q4: True or false: one slow fanout destination should block the broadcast.',
                'Q5: Hybrid fanout pushes to? (A: active readers / B: everyone / C: nobody)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A messaging platform must deliver a viral post to 5M followers under 5s. Design the fanout: push/pull split, batching, regional, and the failure budgets.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why a million-inbox write needs fanout design, not a for loop.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: false; Q5: A',
            'Fanout is write-amplification vs read-latency',
            'Hybrid and partitioned fanout handle the scale',
        ],
    },
])
