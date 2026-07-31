#!/usr/bin/env python3
"""Deep curriculum data batch 8: saga, sharding, sidecar, singleton, state, strangler-fig."""

TOPICS = {}


def _t(slug, topics):
    TOPICS[slug] = topics
    return topics


# ─────────────────────────────────────────────────────────────────────────────
# SAGA
# ─────────────────────────────────────────────────────────────────────────────
_t('saga', [
    {
        'title': 'Saga: Long-Running Transactions Without Distributed Locks',
        'desc': 'A sequence of local transactions with compensating actions — success or a full rollback.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the saga model',
            'Describe compensating transactions',
            'Compare with 2PC',
            'Design a saga flow',
        ],
        'prereqs': ['patterns/two-phase-commit', 'patterns/mediator'],
        'sections': [
            {'heading': 'The Problem', 'paras': [
                'A checkout spans inventory, payment, and shipping — three databases. A distributed transaction (2PC) needs a coordinator and holds locks across services; sagas instead break the flow into local transactions with compensating actions. If a step fails, the saga runs the compensations of the completed steps — an eventual rollback, no global locks.',
            ], 'code': {'lang': 'python', 'body': '''
# Saga: local steps + compensating actions
class OrderSaga:
    def __init__(self, inv, pay, ship):
        self.inv, self.pay, self.ship = inv, pay, ship

    def run(self, order):
        done = []
        try:
            self.inv.reserve(order)        # step 1
            done.append(lambda: self.inv.release(order))   # compensate
            self.pay.charge(order)         # step 2
            done.append(lambda: self.pay.refund(order))
            self.ship.dispatch(order)      # step 3
            done.append(lambda: self.ship.cancel(order))
            return 'success'
        except Exception as e:
            for compensate in reversed(done):   # undo, last first
                try: compensate()
                except Exception: log('compensation failed', e)
            raise e'''}},
            {'heading': 'Compensations', 'paras': [
                'A compensating action reverses the business effect of a completed step (release a reservation, refund a charge, cancel a shipment). It is not an undo of the transaction — it is a new transaction that makes the world whole again. Compensations must be idempotent and themselves reliable.',
            ]},
        ],
        'practice': {
            'title': 'Design the Checkout Saga',
            'intro': 'Checkout: reserve inventory, charge card, book shipment. A payment failure must unwind the reservation.',
            'tasks': [
                {'label': 'Task 1', 'text': 'List the steps and each compensating action.'},
                {'label': 'Task 2', 'text': 'Trace the failure at each step and the compensation order.'},
                {'label': 'Task 3', 'text': 'Make each compensation idempotent and design its retry.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why a saga needs compensations instead of a rollback. Start with two databases.'},
            {'label': 'Compare & Contrast', 'text': 'Compare saga with two-phase commit: availability, locks, and consistency.'},
            {'label': 'Boundary Testing', 'text': 'A compensation fails (the refund API is down). Design the retry and the manual-repair path.'},
        ],
        'takeaways': [
            'Sagas split long transactions into compensatable steps',
            'Compensations are new transactions, not undos',
            'No global locks — availability stays high',
            'Compensations must be idempotent and reliable',
        ],
        'further': [
            {'title': 'Saga pattern — microservices.io', 'url': 'https://microservices.io/patterns/data/saga.html'},
            {'title': 'Sagas — the original paper', 'url': 'https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf'},
        ],
    },
    {
        'title': 'Saga in Production: Orchestration and Choreography',
        'desc': 'Centralized saga coordinators vs event-driven choreography, with state machines.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Orchestrate sagas centrally',
            'Choreograph with events',
            'Persist saga state',
            'Handle partial failures',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Orchestration', 'paras': [
                'An orchestrator (Temporal, Step Functions) runs the saga as a state machine: it calls each service, records the step, and runs compensations in reverse on failure. Central orchestration makes the flow visible and resumable — the orchestrator persists state, so a crash resumes the saga mid-flight.',
            ], 'code': {'lang': 'text', 'body': '''
Orchestrated saga (state machine):
  [Reserve] -> [Charge] -> [Dispatch] -> Done
      |           |
      v           v
  [Release]    [Refund]        (compensations, run in reverse)

  The orchestrator stores each step's outcome; on a crash it
  resumes from the last recorded step. Compensations run
  exactly once (idempotent) in reverse order.

Choreographed saga (event chain):
  OrderCreated -> InventoryReserved -> PaymentCharged
    -> ShipmentDispatched
  Each service reacts to an event and emits the next; a failure
  emits a compensation event. No central state; the flow is
  implicit in the event log. Traceable, but harder to reason
  about and to resume after a crash.'''}},
            {'heading': 'Choosing', 'paras': [
                'Orchestrate when the flow is long, has many failure branches, or must be resumable. Choreograph when services must evolve independently and the happy path is linear. Hybrid: choreograph the happy path, orchestrate the compensations. The orchestration state store (a database or a workflow engine) is the saga\'s source of truth.',
            ]},
        ],
        'practice': {
            'title': 'Operationalize the Saga',
            'intro': 'A 4-step onboarding saga fails at step 3; the first two must be compensated and the flow resumed.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the orchestrated state machine with persisted state.'},
                {'label': 'Task 2', 'text': 'Design the compensation retry and the manual override.'},
                {'label': 'Task 3', 'text': 'Add the dashboard: running, failed, and compensating sagas.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why orchestration makes sagas resumable and choreography makes them decoupled.'},
            {'label': 'Implementation Design', 'text': 'Design a booking saga (hotel + flight + car) with Temporal. What are the steps, compensations, and timeouts?'},
            {'label': 'Boundary Testing', 'text': 'The orchestrator dies mid-compensation. Design the resume that completes the unwind exactly once.'},
        ],
        'takeaways': [
            'Orchestrators make sagas visible and resumable',
            'Choreography trades control for independence',
            'Persisted state is the saga source of truth',
            'Compensations must resume after crashes',
        ],
        'further': [
            {'title': 'Temporal — durable workflows', 'url': 'https://docs.temporal.io/'},
            {'title': 'AWS Step Functions — saga', 'url': 'https://docs.aws.amazon.com/step-functions/latest/dg/sample-saga.html'},
        ],
    },
    {
        'title': 'Advanced Saga: Exactly-Once Compensation and Sagas Across Partitions',
        'desc': 'Idempotent compensations, isolation levels for sagas, and sagas at scale.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Make compensations exactly-once',
            'Handle saga isolation anomalies',
            'Run sagas across partitions',
            'Design saga timeouts',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Compensation Reliability', 'paras': [
                'A compensation is itself a transaction that can fail and must be idempotent: retrying release() must not double-release. Store compensation status (pending/done) with the saga state; only mark done after the compensating transaction commits. The compensation log doubles as the audit trail.',
            ], 'code': {'lang': 'text', 'body': '''
Saga isolation problems (when steps are visible mid-saga):
  Lost update: two sagas interleave on the same resource
  Dirty read: another reader sees a step before the saga finishes
  Phantom: the saga's global effect is not atomic to others
Mitigations:
  - semantic locks: a "reserved" flag others must respect
  - reorder steps so the risky resource is touched last
  - per-saga visibility: mark in-flight sagas and treat their
    data as provisional
  - timeout: every step has a deadline; a timed-out step triggers
    compensation even without an explicit failure
These turn the saga from "best effort" into a design with
bounded, documented anomalies.'''}},
            {'heading': 'Scaling', 'paras': [
                'Sagas scale with their orchestrator: sharded state stores, per-tenant saga instances, and retry queues with backoff. Timeouts are the subtle dial — too short compensates healthy work, too long leaves stuck reservations. Saga engines provide the timeouts, retries, and resumption for free.',
            ]},
        ],
        'practice': {
            'title': 'Design for Isolation',
            'intro': 'Two users book the same hotel room concurrently; both sagas start, one must win.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the semantic lock (reserved flag) and the conflict outcome.'},
                {'label': 'Task 2', 'text': 'Design step timeouts and the compensation trigger on timeout.'},
                {'label': 'Task 3', 'text': 'Design the compensation log with exactly-once markers.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why saga isolation needs semantic locks rather than global locks.'},
            {'label': 'Implementation Design', 'text': 'Design a seat-booking saga where overselling is impossible. What order, locks, and timeouts achieve it?'},
            {'label': 'Boundary Testing', 'text': 'A timeout fires while the step actually succeeded. Design the reconciliation that detects and resolves the false compensation.'},
        ],
        'takeaways': [
            'Compensations need exactly-once markers',
            'Saga isolation uses semantic locks, not global ones',
            'Timeouts drive compensation even without failures',
            'Orchestrator state shards to scale sagas',
        ],
        'further': [
            {'title': 'Sagas — the original paper (isolation)', 'url': 'https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf'},
            {'title': 'Temporal — activities and compensations', 'url': 'https://docs.temporal.io/'},
        ],
    },
    {
        'title': 'Saga: Review & Mastery Quiz',
        'desc': 'Scenario questions on flows, orchestration, and isolation.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate saga concepts',
            'Choose orchestration',
            'Design compensations',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: A saga replaces? (A: 2PC / B: caching / C: sharding)',
                'Q2: A compensation is? (A: a new transaction / B: an undo / C: a lock)',
                'Q3: Orchestrated sagas are? (A: resumable and visible / B: faster / C: smaller)',
                'Q4: True or false: compensations must be idempotent.',
                'Q5: Saga isolation uses? (A: semantic locks / B: global locks / C: no locks)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A travel booking saga spans hotel, flight, and car. Design the steps, compensations, and timeout policy.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why compensating is different from rolling back.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Local steps plus compensations beat global locks',
            'Isolation and idempotency are the hard parts',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# SHARDING
# ─────────────────────────────────────────────────────────────────────────────
_t('sharding', [
    {
        'title': 'Sharding: Split Data to Scale',
        'desc': 'Partitioning a dataset across nodes so no single node holds it all.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the sharding model',
            'Choose a shard key',
            'Understand query routing',
            'Know the hot-shard risk',
        ],
        'prereqs': ['patterns/hash-index', 'patterns/replication'],
        'sections': [
            {'heading': 'The Model', 'paras': [
                'Sharding splits a dataset by a shard key: hash the key, route the row to its shard. No node holds everything, so capacity grows with nodes. The shard key decides everything — a good key distributes evenly and keeps related data together; a bad key concentrates traffic on one shard.',
            ], 'code': {'lang': 'text', 'body': '''
Sharding by hash of the shard key:
  shard = hash(user_id) % N

  Good shard keys:
    - high cardinality (user_id, order_id, tenant_id)
    - even distribution (uniform values)
    - query affinity (all of a user's rows in one shard)
  Bad shard keys:
    - low cardinality (status, country)
    - skewed values (one giant tenant)
  Query routing:
    - point query on shard key: one shard, fast
    - query without the key: scan every shard (scatter-gather)
  Hot shard: one key with huge traffic overwhelms its shard —
    the ceiling of the whole system.'''}},
            {'heading': 'Key Choice', 'paras': [
                'Composite keys fix many routing problems: tenant_id as the shard key routes all of a tenant\'s data to one shard (query affinity), while a secondary key orders within the shard. The cardinality and the query shapes — not fashion — pick the key.',
            ]},
        ],
        'practice': {
            'title': 'Choose the Shard Key',
            'intro': 'A messaging app: conversations, messages, users — queries are per-user and per-conversation.',
            'tasks': [
                {'label': 'Task 1', 'text': 'List the query shapes and their hot paths.'},
                {'label': 'Task 2', 'text': 'Choose the shard key with query affinity and justify.'},
                {'label': 'Task 3', 'text': 'Identify the scatter-gather queries and their cost.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why the shard key choice is the whole design. Start with a bad key.'},
            {'label': 'Compare & Contrast', 'text': 'Compare sharding with replication: one scales capacity, the other availability. When do you need both?'},
            {'label': 'Boundary Testing', 'text': 'A tenant grows to 40% of the data. Design the re-shard or the tenant split that rebalances.'},
        ],
        'takeaways': [
            'Sharding scales capacity by splitting data',
            'The shard key decides distribution and routing',
            'Query affinity keeps related data co-located',
            'Hot shards are the scaling ceiling',
        ],
        'further': [
            {'title': 'Sharding — Martin Fowler', 'url': 'https://martinfowler.com/articles/database-sharding-ballerina.html'},
            {'title': 'PostgreSQL — partitioning', 'url': 'https://www.postgresql.org/docs/current/ddl-partitioning.html'},
        ],
    },
    {
        'title': 'Sharding in Production: Vitess, Citus, and DynamoDB',
        'desc': 'How production systems shard — and how they rebalance and route.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Describe Vitess-style sharding',
            'Use range vs hash sharding',
            'Design rebalancing',
            'Route queries correctly',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Range vs Hash', 'paras': [
                'Range sharding (Citus, time-series) splits by key ranges: time ranges enable easy retention and predictable hotspots by time. Hash sharding distributes evenly but scatters ranges. The choice follows the workload: time-ordered ingestion loves range; uniform access loves hash.',
            ], 'code': {'lang': 'text', 'body': '''
Range vs hash sharding:
  Range (Citus, timeseries):
    shard = the range containing the key
    + range scans local, retention = drop whole shards
    - hot ranges (recent time) concentrate load
  Hash (Vitess, DynamoDB):
    shard = hash(key) % N
    + even distribution, no inherent hotspot
    - range queries scatter
  Rebalancing:
    - hash: consistent hashing moves a fraction on resize
    - range: split a hot range in two, migrate half
  Routing:
    - a mapping service maps key -> shard (Vitess VSchema)
    - or the client hashes locally (DynamoDB)'''}},
            {'heading': 'Operations', 'paras': [
                'Production sharding needs a routing layer (Vitess VSchema, a shard map service), rebalancing tooling, and scatter-gather for cross-shard queries. Schema changes and migrations run per shard. The hardest operational truth: resharding is a migration, not a knob — it must be planned, rehearsed, and reversible.',
            ]},
        ],
        'practice': {
            'title': 'Design the Sharded Store',
            'intro': 'A 10B-row events table, time-ordered, queried by tenant over time ranges, must grow without downtime.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Choose range vs hash for the access pattern.'},
                {'label': 'Task 2', 'text': 'Design the routing layer and the rebalance drill.'},
                {'label': 'Task 3', 'text': 'Design the retention (drop old shards) and the hot-range mitigation.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why time-series loves range sharding and what its hotspot is.'},
            {'label': 'Implementation Design', 'text': 'Design a Vitess-style setup: VSchema, shard map, and the reshard command sequence for a growing table.'},
            {'label': 'Boundary Testing', 'text': 'A shard fills to 90%. Design the split, the dual-write window, and the rollback.'},
        ],
        'takeaways': [
            'Range fits time-series; hash fits uniform access',
            'Routing layers and shard maps decouple clients',
            'Resharding is a rehearsed migration',
            'Retention drops whole shards cheaply',
        ],
        'further': [
            {'title': 'Vitess — sharding', 'url': 'https://vitess.io/docs/concepts/sharding/'},
            {'title': 'Citus — distributed tables', 'url': 'https://docs.citusdata.com/en/stable/'},
        ],
    },
    {
        'title': 'Advanced Sharding: Resharding and Cross-Shard Queries',
        'desc': 'Live resharding, distributed joins, and globally consistent operations.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Reshard without downtime',
            'Design cross-shard joins',
            'Maintain global uniqueness',
            'Distribute transactions',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Live Resharding', 'paras': [
                'Growing past the shard count demands resharding: add shards and move data. The dual-write pattern keeps it live — writes go to both old and new layouts while a backfill copies history; a cutover flips reads when the copy converges; a rollback window covers mistakes. Each phase is a state machine with checks.',
            ], 'code': {'lang': 'text', 'body': '''
Live resharding phases:
  1. Prepare: add the new shards, install the new routing rule
     (e.g., hash(key) % 8 instead of % 4)
  2. Dual-write: every write goes to the old and new shards;
     a backfill job copies historical rows (idempotent)
  3. Verify: compare row counts, checksums, and lag between
     old and new layouts
  4. Cutover: reads move to the new layout; keep the old for
     a rollback window
  5. Drain: drop the old copies and the dual-write path
Global uniqueness across shards:
  - UUIDs, or a central sequence, or per-shard ranges (id = shard*N + n)
Cross-shard transactions:
  - avoid them (design for single-shard atomicity)
  - or accept 2PC / saga semantics when unavoidable'''}},
            {'heading': 'Cross-Shard Queries', 'paras': [
                'Scatter-gather (ask every shard, merge) is the fallback for queries without the shard key — slow at scale. Distributed joins route by the join key so joined rows co-locate, or broadcast small tables. The discipline: every hot query must carry the shard key; everything else is a known cost.',
            ]},
        ],
        'practice': {
            'title': 'Plan the Reshard',
            'intro': 'A 4-shard user table must move to 8 shards with zero downtime.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the dual-write, backfill, and verify phases.'},
                {'label': 'Task 2', 'text': 'Design the cutover with a rollback window.'},
                {'label': 'Task 3', 'text': 'Audit the hot queries: which ones carry the shard key?'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why dual-write plus backfill reshares without downtime.'},
            {'label': 'Implementation Design', 'text': 'Design a globally unique ID scheme for a 64-shard system and the per-shard ordering it preserves.'},
            {'label': 'Boundary Testing', 'text': 'The backfill and dual-write diverge on one row. Design the checksum verify that catches it before cutover.'},
        ],
        'takeaways': [
            'Dual-write + backfill + verify + cutover = live reshard',
            'Hot queries must carry the shard key',
            'Scatter-gather is a known, bounded cost',
            'Global IDs need a per-shard scheme',
        ],
        'further': [
            {'title': 'Vitess — resharding', 'url': 'https://vitess.io/docs/user-guides/sharding-resharding/'},
            {'title': 'The Pathologies of Big Data (scatter-gather)', 'url': 'https://queue.acm.org/detail.cfm?id=1563874'},
        ],
    },
    {
        'title': 'Sharding: Review & Mastery Quiz',
        'desc': 'Scenario questions on keys, rebalancing, and resharding.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate sharding concepts',
            'Choose keys and layouts',
            'Plan resharding',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Sharding scales? (A: capacity / B: availability only / C: the frontend)',
                'Q2: The shard key decides? (A: distribution and routing / B: compression / C: indexing)',
                'Q3: Range sharding fits? (A: time-series / B: random access / C: graphs)',
                'Q4: True or false: resharding is a rehearsed migration.',
                'Q5: A hot shard is caused by? (A: a skewed key / B: too many shards / C: caching)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A 20B-row events table must scale and support tenant time-range queries. Design the key, the layout, and the growth plan.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why the shard key is the most important decision in the database.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Keys, layout, and rebalancing define sharding success',
            'Resharding is the migration you rehearse',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# SIDECAR
# ─────────────────────────────────────────────────────────────────────────────
_t('sidecar', [
    {
        'title': 'Sidecar: A Helper Next to Your App',
        'desc': 'Running supporting logic in a separate process co-located with the main application.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the sidecar model',
            'Co-locate without coupling',
            'Describe the communication',
            'Know the deployment',
        ],
        'prereqs': ['patterns/ambassador', 'patterns/proxy'],
        'sections': [
            {'heading': 'The Model', 'paras': [
                'A sidecar is a separate process deployed alongside the main app — same host, same lifecycle — that provides a supporting capability: logging, proxying, config reload, TLS. The app talks to the sidecar over localhost; the sidecar talks to the world. The main app stays small and language-agnostic.',
            ], 'code': {'lang': 'yaml', 'body': '''
# Kubernetes pod: app + sidecar sharing a volume and localhost
apiVersion: v1
kind: Pod
metadata:
  name: web-app
spec:
  containers:
    - name: app
      image: web-app:1.2
      volumeMounts:
        - name: logs
          mountPath: /var/log/app
    - name: log-shipper      # sidecar: supporting capability
      image: log-shipper:2.1
      volumeMounts:
        - name: logs
          mountPath: /var/log/app   # reads the app's logs
      args: ["tail", "/var/log/app/*.log"]
  volumes:
    - name: logs
      emptyDir: {}
# The app does not know the sidecar exists; the sidecar does
# not change the app's code.'''}},
            {'heading': 'Why a Process', 'paras': [
                'A separate process isolates failures, languages, and versions: the sidecar can crash and restart without touching the app, can be written in any language, and upgrades independently. The cost: another process to deploy and monitor, and the localhost hop adds a little latency.',
            ]},
        ],
        'practice': {
            'title': 'Add the Log Sidecar',
            'intro': 'A Python app writes logs; the team wants shipping, rotation, and buffering without changing the app.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the sidecar that reads, rotates, and ships the logs.'},
                {'label': 'Task 2', 'text': 'Define the localhost contract and the shared volume.'},
                {'label': 'Task 3', 'text': 'Test: the sidecar crashes and restarts; the app is unaffected.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why co-location without code coupling is the sidecar win. Start with the language barrier.'},
            {'label': 'Compare & Contrast', 'text': 'Compare sidecar with ambassador, proxy, and an in-process library. When does a process win over a library?'},
            {'label': 'Boundary Testing', 'text': 'The sidecar dies and the app must keep serving. Design the degraded mode and the alert.'},
        ],
        'takeaways': [
            'Sidecars co-locate supporting logic without coupling',
            'They isolate failures, languages, and versions',
            'Communication is localhost + shared volumes',
            'Another process means another thing to monitor',
        ],
        'further': [
            {'title': 'Sidecar pattern — Microsoft', 'url': 'https://learn.microsoft.com/en-us/azure/architecture/patterns/sidecar'},
            {'title': 'Kubernetes — multi-container pods', 'url': 'https://kubernetes.io/docs/concepts/workloads/pods/'},
        ],
    },
    {
        'title': 'Sidecar in Production: Service Mesh and Data Plane',
        'desc': 'Envoy sidecars, mTLS, and the mesh data plane as a sidecar fleet.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Describe mesh sidecars',
            'Inject mTLS and retries',
            'Operate the sidecar fleet',
            'Measure the overhead',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'The Mesh Data Plane', 'paras': [
                'Istio and Linkerd inject an Envoy sidecar into every pod. All app traffic goes through the sidecar, which adds mTLS, retries, timeouts, circuit breaking, and telemetry — platform capabilities without application changes. The sidecar becomes the universal edge for service-to-service calls.',
            ], 'code': {'lang': 'text', 'body': '''
Service mesh sidecar responsibilities (Envoy):
  - mTLS: encrypt and authenticate every service-to-service call
  - routing: version, region, and canary routing
  - resilience: retries, timeouts, circuit breaking
  - observability: traces, metrics, access logs per call
  - policy: authorization between services
  Deployment model:
    app pod -> localhost -> Envoy sidecar -> network -> peer sidecar
    -> peer app
  The app makes a plain HTTP call to localhost; everything else
  is the mesh's business.
  Cost: one more container per pod, plus ~5-15% latency from the
  two extra hops (mitigated with eBPF/gRPC optimization).'''}},
            {'heading': 'Operating the Fleet', 'paras': [
                'A sidecar fleet needs version rollout (sidecars upgrade independent of apps), config distribution (the control plane pushes routing), and health monitoring per sidecar. The mesh centralizes policy — which is its power and its blast radius: a bad mesh config breaks every service at once.',
            ]},
        ],
        'practice': {
            'title': 'Design the Mesh Rollout',
            'intro': 'A 40-service platform adopts a service mesh with canary routing and mTLS.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the sidecar injection and the rollout order.'},
                {'label': 'Task 2', 'text': 'Design the canary routing rule through the mesh.'},
                {'label': 'Task 3', 'text': 'Design the mesh outage response: what breaks if the control plane dies?'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me what the mesh sidecar adds to every call and what the app gives up.'},
            {'label': 'Implementation Design', 'text': 'Design a canary release with mesh routing: how do 5% of requests hit v2, and how is a bad v2 rolled back?'},
            {'label': 'Boundary Testing', 'text': 'A misconfigured mesh rule blackholes all traffic. Design the config validation and the emergency off-switch.'},
        ],
        'takeaways': [
            'Mesh sidecars add mTLS, routing, and resilience platform-wide',
            'Apps talk to localhost; the mesh owns the network path',
            'Sidecars upgrade independently of apps',
            'Centralized policy is power and blast radius',
        ],
        'further': [
            {'title': 'Istio — architecture', 'url': 'https://istio.io/latest/docs/ops/deployment/architecture/'},
            {'title': 'Linkerd — what is it', 'url': 'https://linkerd.io/2/what-is-linkerd/'},
        ],
    },
    {
        'title': 'Advanced Sidecar: eBPF, WASM, and Edge Sidecars',
        'desc': 'Sidecars beyond the mesh: eBPF acceleration, WASM extensions, and edge compute.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Accelerate sidecars with eBPF',
            'Extend sidecars with WASM',
            'Run sidecars at the edge',
            'Choose the sidecar shape',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Acceleration and Extension', 'paras': [
                'The sidecar hop is the mesh\'s main cost. eBPF moves filtering and routing into the kernel, reducing hops; WASM lets operators extend Envoy sidecars with per-tenant policy without shipping a new proxy. The sidecar is becoming a pluggable runtime, not a fixed appliance.',
            ], 'code': {'lang': 'text', 'body': '''
Sidecar evolution:
  Classic: Envoy sidecar, fixed feature set, JSON config
  eBPF (Cilium, Istio ambient): move L3/L4 filtering into the
    kernel — fewer user-space hops, lower latency and CPU
  WASM: compile policy/authz filters to WASM and load them into
    the sidecar at runtime — per-tenant logic without a new build
  Ambient/zero-sidecar: a per-node shared proxy instead of
    per-pod — less overhead, coarser isolation
  Edge sidecars: the same pattern at the edge (CDN worker,
    gateway) running auth, geolocation, and transformation
The design question is always the same: what support does the
app need, and where is the right place for that hop?'''}},
            {'heading': 'Choosing the Shape', 'paras': [
                'Per-pod sidecar: strongest isolation, highest overhead. Per-node ambient: lower cost, coarser isolation. In-process library: lowest overhead, but language-coupled. The trade is isolation vs cost vs coupling — and the answer shifts as the platform matures.',
            ]},
        ],
        'practice': {
            'title': 'Choose the Data Plane',
            'intro': 'A high-QPS platform (100k RPS) finds the sidecar hop costs 10% of its latency budget.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Measure the sidecar overhead on a hot path.'},
                {'label': 'Task 2', 'text': 'Compare per-pod, ambient, and eBPF data planes.'},
                {'label': 'Task 3', 'text': 'Pick one and justify with the isolation and latency numbers.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain the isolation-vs-overhead trade across sidecar shapes.'},
            {'label': 'Implementation Design', 'text': 'Design a WASM authz filter for a multi-tenant gateway: how does per-tenant policy load at runtime?'},
            {'label': 'Boundary Testing', 'text': 'An eBPF program crashes the kernel. Design the fallback to the user-space path and the rollout guard.'},
        ],
        'takeaways': [
            'eBPF and WASM make sidecars faster and pluggable',
            'Ambient shapes trade isolation for overhead',
            'Edge sidecars apply the pattern at the edge',
            'Shape choice follows isolation and latency budgets',
        ],
        'further': [
            {'title': 'Istio — ambient mesh', 'url': 'https://istio.io/latest/blog/2022/introducing-ambient-mesh/'},
            {'title': 'Envoy — WASM filters', 'url': 'https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/wasm/v3/wasm'},
        ],
    },
    {
        'title': 'Sidecar: Review & Mastery Quiz',
        'desc': 'Scenario questions on co-location, meshes, and shapes.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate sidecar concepts',
            'Operate meshes',
            'Choose shapes',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: A sidecar is? (A: a co-located helper process / B: a database / C: a UI)',
                'Q2: The app talks to the sidecar over? (A: localhost / B: the internet / C: the bus)',
                'Q3: A mesh sidecar adds? (A: mTLS and routing / B: storage / C: rendering)',
                'Q4: True or false: sidecars upgrade independently of the app.',
                'Q5: eBPF sidecars move work? (A: into the kernel / B: to the client / C: to the cloud)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A 30-service platform wants mTLS and canary routing without app changes. Design the mesh adoption and its rollout.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why a separate process is worth the extra ops burden.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Co-located, decoupled, independently upgradeable',
            'The mesh made sidecars a platform primitive',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# SINGLETON
# ─────────────────────────────────────────────────────────────────────────────
_t('singleton', [
    {
        'title': 'Singleton: One Instance, One Access Point',
        'desc': 'Ensuring a class has exactly one instance and a global access point to it.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the singleton intent',
            'Implement a singleton',
            'Make it thread-safe',
            'Recognize the drawbacks',
        ],
        'prereqs': ['patterns/factory', 'principles/separation-of-concerns'],
        'sections': [
            {'heading': 'The Intent', 'paras': [
                'Some resources must be unique: a config, a connection pool, a logger. The singleton enforces one instance and gives a global access point. The classic implementation is a private constructor plus a static instance — lazy or eager.',
            ], 'code': {'lang': 'java', 'body': '''
// Thread-safe lazy singleton: double-checked locking
class Config {
    private static volatile Config instance;

    private Config() {                 // private: no other constructors
        loadFromDisk();
    }

    static Config get() {
        Config local = instance;       // fast path, no lock
        if (local == null) {
            synchronized (Config.class) {
                local = instance;
                if (local == null) {
                    local = new Config();     // create once
                    instance = local;
                }
            }
        }
        return local;
    }
}
// Config.get() is THE single instance and access point.'''}},
            {'heading': 'Why It Is Controversial', 'paras': [
                'Singletons are global state in disguise: they hide dependencies, make testing harder (a fake needs to replace the global), and couple callers to the access point. The modern guidance: scope the instance to its lifetime (app scope via dependency injection) and inject it — the "one instance" property survives, the global access point does not.',
            ]},
        ],
        'practice': {
            'title': 'Scope the Instance',
            'intro': 'A logger is used by 200 classes; tests must capture output per test.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Implement the thread-safe singleton and note the hidden coupling.'},
                {'label': 'Task 2', 'text': 'Refactor to an injected logger scoped per app and per test.'},
                {'label': 'Task 3', 'text': 'Compare: what breaks if two instances exist in each design?'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why a global access point makes testing harder. Start with the fake.'},
            {'label': 'Compare & Contrast', 'text': 'Compare singleton with dependency injection scoping and with the registry pattern.'},
            {'label': 'Boundary Testing', 'text': 'Two threads call get() for the first time. Design the initialization that cannot create two instances.'},
        ],
        'takeaways': [
            'Singleton enforces one instance and one access point',
            'Thread safety needs careful initialization',
            'Global access is hidden coupling',
            'DI scoping keeps the single instance, drops the global',
        ],
        'further': [
            {'title': 'Singleton — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/singleton'},
            {'title': 'Singletons are pathological liars — Miško Hevery', 'url': 'https://misko.hevery.com/2008/08/17/singletons-are-pathological-liars/'},
        ],
    },
    {
        'title': 'Singleton in Production: Pools and Registries',
        'desc': 'Connection pools, caches, and registries as legitimate singletons — with injection.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Use singletons for shared resources',
            'Inject instead of import',
            'Scope to lifetimes',
            'Test with fakes',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Legitimate Singletons', 'paras': [
                'Connection pools, caches, and config are legitimate singletons: one instance shared by the whole app, never duplicated. The problem was never the single instance — it is the global access point. Inject the singleton into its consumers, and the tests inject a fake instead.',
            ], 'code': {'lang': 'typescript', 'body': '''
// Singleton scoped and injected — no global access point
export class Db {
    private static instance: Db;      // one instance, app-scoped
    static get(): Db { ... }          // used ONLY by the composition root
    query(sql: string): Result { ... }
}

// Consumers receive it:
export class OrderService {
    constructor(private db: Db) {}    // injected, testable with a fake
}
// Composition root wires it once:
const db = Db.get();
const orders = new OrderService(db);
// Only the composition root touches Db.get() — tests construct
// OrderService with an in-memory fake and never see the global.'''}},
            {'heading': 'Scoping', 'paras': [
                'Scope to the right lifetime: a connection pool is app-scoped; a request-scoped transaction context is per-request; a per-test cache is per-test. DI containers manage these lifetimes. The "singleton" pattern collapses every lifetime into global — which is exactly why it is usually a code smell in modern code.',
            ]},
        ],
        'practice': {
            'title': 'Inject the Pool',
            'intro': 'A connection pool is imported as a singleton by 50 classes; tests hit the real database.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Inject the pool through constructors everywhere it is imported.'},
                {'label': 'Task 2', 'text': 'Add the in-memory fake for tests.'},
                {'label': 'Task 3', 'text': 'Verify only the composition root calls the singleton accessor.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me the difference between a singleton instance and a global access point, and why the second is the problem.'},
            {'label': 'Implementation Design', 'text': 'Design a cache singleton that is injectable: interface, instance, and the test fake.'},
            {'label': 'Boundary Testing', 'text': 'A test leaks singleton state between cases. Design the reset hook or the per-test scoping that isolates them.'},
        ],
        'takeaways': [
            'Pools, caches, and config are legitimate singletons',
            'Inject the instance; drop the global access point',
            'Lifetimes vary: app, request, test',
            'Only the composition root touches the accessor',
        ],
        'further': [
            {'title': 'Dependency injection — Martin Fowler', 'url': 'https://martinfowler.com/articles/injection.html'},
            {'title': 'Composition root — Mark Seemann', 'url': 'https://blog.ploeh.dk/2011/07/28/CompositionRoot/'},
        ],
    },
    {
        'title': 'Advanced Singleton: Multiton and Lifecycle Managers',
        'desc': 'Multitons, managed instances, and why the pattern survives only where scoped.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Explain the multiton',
            'Manage instance lifecycles',
            'Design registries',
            'Test stateful singletons',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Multiton and Registries', 'paras': [
                'A multiton keys instances: one instance per key (one DB pool per tenant). A registry maps keys to instances with registration. Both are singletons generalized — and both belong behind a container or composition root, with explicit lifetimes, not globals.',
            ], 'code': {'lang': 'java', 'body': '''
// Multiton: one instance per key
class PoolRegistry {
    private static final Map<String, ConnectionPool> pools = new ConcurrentHashMap<>();

    static ConnectionPool poolFor(String tenant) {
        return pools.computeIfAbsent(tenant, ConnectionPool::new);
    }
}
// One pool per tenant, created on demand, shared thereafter.
// Scoped where it is needed; never a global for the app.
// The registry is the natural home: registries, factories, and
// DI containers all manage "one per X" instances — the singleton
// pattern is the degenerate case of X = app.'''}},
            {'heading': 'Lifecycle Management', 'paras': [
                'Managed instances need lifecycle: creation, warming, shutdown, and recreation on failure. A container or a registry owns the lifecycle; the pattern\'s static instance does not. Stateful singletons (caches, pools) also need reset hooks for tests — which the global access point cannot provide cleanly.',
            ]},
        ],
        'practice': {
            'title': 'Manage the Pools',
            'intro': 'A multi-tenant app needs one pool per tenant, warm on first use, drain on shutdown.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Build the registry with per-key creation.'},
                {'label': 'Task 2', 'text': 'Add lifecycle: warm, drain, and recreate on failure.'},
                {'label': 'Task 3', 'text': 'Add the test reset and verify pool state does not leak between tests.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why the multiton is a scoped singleton and who owns its lifecycle.'},
            {'label': 'Implementation Design', 'text': 'Design a connection-pool manager for 100 tenants: creation, sizing, idle eviction, and shutdown ordering.'},
            {'label': 'Boundary Testing', 'text': 'A tenant\'s pool fails open connections. Design the recreation path that warms a fresh pool without breaking in-flight requests.'},
        ],
        'takeaways': [
            'Multiton keys instances per entity',
            'Lifecycle belongs to a manager, not a static field',
            'Registries and containers own the "one per X"',
            'Test resets need explicit hooks',
        ],
        'further': [
            {'title': 'Multiton — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Multiton_pattern'},
            {'title': 'Registry — Martin Fowler', 'url': 'https://martinfowler.com/eaaCatalog/registry.html'},
        ],
    },
    {
        'title': 'Singleton: Review & Mastery Quiz',
        'desc': 'Scenario questions on instances, scoping, and lifecycles.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate singleton concepts',
            'Scope instances',
            'Manage lifecycles',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: A singleton ensures? (A: one instance / B: two instances / C: no instances)',
                'Q2: The common criticism is? (A: global access / B: speed / C: size)',
                'Q3: A multiton keeps? (A: one instance per key / B: one global / C: a queue)',
                'Q4: True or false: injection keeps the single instance without the global.',
                'Q5: Instance lifecycles belong to? (A: a manager / B: the static field / C: the client)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A multi-tenant app needs per-tenant caches with lifecycle management. Design the registry and the injection.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer when a singleton is legitimate and when it is a smell.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Single instance yes; global access no',
            'Scope and manage lifetimes explicitly',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# STATE
# ─────────────────────────────────────────────────────────────────────────────
_t('state', [
    {
        'title': 'State: Behavior That Changes with State',
        'desc': 'An object changes its behavior when its internal state changes — state as objects.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the state pattern',
            'Model states as classes',
            'Delegate behavior to state',
            'Simplify conditionals',
        ],
        'prereqs': ['patterns/strategy', 'principles/single-responsibility'],
        'sections': [
            {'heading': 'The Problem', 'paras': [
                'A network connection, an order, a document — each has states with different behavior for the same call. With if-chains, every method repeats the state checks and grows with every state and transition. The state pattern turns each state into an object; the context delegates to the current state object, which also owns its transitions.',
            ], 'code': {'lang': 'python', 'body': '''
# State pattern: each state is an object owning behavior + transitions
class Order:
    def __init__(self):
        self.state = Draft(self)          # context holds current state
    def submit(self): self.state.submit()
    def cancel(self): self.state.cancel()

class Draft:                              # state 1
    def __init__(self, order): self.order = order
    def submit(self):
        print('draft -> submitted')
        self.order.state = Submitted(self.order)   # transition here
    def cancel(self):
        print('draft cancelled')
        self.order.state = Cancelled(self.order)

class Submitted:
    def __init__(self, order): self.order = order
    def submit(self):
        raise ValueError('already submitted')     # state forbids it
    def cancel(self):
        print('submitted -> cancelled')
        self.order.state = Cancelled(self.order)

class Cancelled:
    def __init__(self, order): self.order = order
    def submit(self): raise ValueError('cancelled orders are final')
    def cancel(self): raise ValueError('already cancelled')'''}},
            {'heading': 'State vs Strategy', 'paras': [
                'Strategy swaps algorithms (a sort policy) — the context picks the strategy and keeps it. State swaps behavior because the state itself changed — the context\'s state object transitions itself. Same structure, different driver: strategy is chosen, state is entered.',
            ]},
        ],
        'practice': {
            'title': 'Model the Order Lifecycle',
            'intro': 'An order moves draft -> submitted -> paid -> shipped, with guards on every transition.',
            'tasks': [
                {'label': 'Task 1', 'text': 'List the states, the legal transitions, and the forbidden calls.'},
                {'label': 'Task 2', 'text': 'Implement the state classes and the context delegate.'},
                {'label': 'Task 3', 'text': 'Rewrite the old if-chain version and compare the growth curves.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why states should own their transitions. Start with a forbidden call.'},
            {'label': 'Compare & Contrast', 'text': 'Compare state with strategy and with a state machine table. When does the table beat the classes?'},
            {'label': 'Boundary Testing', 'text': 'A transition should be impossible but a buggy caller invokes it. Design the exception the state throws and the guard tests.'},
        ],
        'takeaways': [
            'State objects own behavior and transitions',
            'The context delegates and holds the current state',
            'It replaces growing if-chains',
            'State is entered; strategy is chosen',
        ],
        'further': [
            {'title': 'State — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/state'},
            {'title': 'State Pattern — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/State_pattern'},
        ],
    },
    {
        'title': 'State in Production: Workflows and State Machines',
        'desc': 'Order flows, document lifecycles, and state machine libraries.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design state machines',
            'Use state machine libraries',
            'Persist state',
            'Validate transitions',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'State Machines', 'paras': [
                'Production state machines centralize states, events, transitions, and guards in one declarative table — XState, Spring Statemachine, or a hand-rolled table. The table is data: auditable, testable, and documented. The state pattern classes are the OO view; the table is the operational view — same model.',
            ], 'code': {'lang': 'typescript', 'body': '''
// XState: a declarative state machine
import { createMachine, interpret } from 'xstate';

const orderMachine = createMachine({
  id: 'order',
  initial: 'draft',
  states: {
    draft:     { on: { SUBMIT: 'submitted' } },
    submitted: { on: { PAY: 'paid', CANCEL: 'cancelled' } },
    paid:      { on: { SHIP: 'shipped' } },
    shipped:   { on: { DELIVER: 'delivered' } },
    cancelled: { type: 'final' },
    delivered: { type: 'final' },
  },
});
const service = interpret(orderMachine).start();
service.send({ type: 'SUBMIT' });   // draft -> submitted
service.send({ type: 'PAY' });
// Guards (e.g., only paid orders ship) attach to transitions.
// The machine is data: it can be persisted, restored, and tested
// by walking its transition table.'''}},
            {'heading': 'Persistence', 'paras': [
                'Long-lived workflows persist the current state — the state value in a database — so a crash resumes where it stopped. The machine is deterministic: same state + same event = same transition, so restoring the state restores the behavior. Auditing records every transition.',
            ]},
        ],
        'practice': {
            'title': 'Automate the Lifecycle',
            'intro': 'A support ticket moves new -> triaged -> in_progress -> resolved -> closed, with SLA guards.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the machine: states, events, transitions, guards.'},
                {'label': 'Task 2', 'text': 'Implement it with a state machine library.'},
                {'label': 'Task 3', 'text': 'Persist the state and design the resume and audit trail.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why a declarative machine is easier to audit and test than scattered if-chains.'},
            {'label': 'Implementation Design', 'text': 'Design a state machine for a refund flow: request, review, approve/reject, issued. What are the guards?'},
            {'label': 'Boundary Testing', 'text': 'A persisted state becomes invalid after a deploy. Design the migration and the validation that rejects it.'},
        ],
        'takeaways': [
            'State machines centralize states, events, and guards',
            'The table is auditable, testable, and documented',
            'Persistence makes workflows resumable',
            'Determinism makes the machine testable',
        ],
        'further': [
            {'title': 'XState — state machines', 'url': 'https://stately.ai/docs'},
            {'title': 'Spring Statemachine', 'url': 'https://projects.spring.io/spring-statemachine/'},
        ],
    },
    {
        'title': 'Advanced State: Hierarchical and Concurrent States',
        'desc': 'Nested states, parallel regions, and statecharts.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Model hierarchical states',
            'Run parallel regions',
            'Design statecharts',
            'Handle complex workflows',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Statecharts', 'paras': [
                'Flat state machines explode with real workflows: nested substates (a connection\'s connecting/connected/retrying), parallel regions (an order being paid while being shipped), and history states. Statecharts add these — hierarchical states, orthogonal regions, and actions — which is why XState implements them.',
            ], 'code': {'lang': 'typescript', 'body': '''
// Statechart: nested + parallel regions
const machine = createMachine({
  id: 'checkout',
  initial: 'cart',
  states: {
    cart: { on: { CHECKOUT: 'processing' } },
    processing: {
      initial: 'payment',
      states: {                    // sequential substates
        payment: { on: { PAID: 'fulfillment' } },
        fulfillment: { on: { DONE: '#checkout.complete' } },
      },
    },
    complete: { type: 'final' },
  },
});
// Parallel regions (orthogonal): payment and inventory checks run
// independently; the machine only completes when BOTH regions do.
// History: a retry returns to the substate it left, not to the
// top of the parent. Statecharts make these explicit.'''}},
            {'heading': 'Complexity', 'paras': [
                'Statecharts scale to real workflows — but the lesson is the same as always: states, transitions, and guards belong in one explicit model, not scattered conditionals. When a flow grows, formalize it; when it shrinks, delete the formalism.',
            ]},
        ],
        'practice': {
            'title': 'Formalize the Deployment',
            'intro': 'A deploy flow: build (with retry substates) while config is verified (parallel), then release.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Model the nested states and the parallel regions.'},
                {'label': 'Task 2', 'text': 'Implement the statechart and walk its transition graph.'},
                {'label': 'Task 3', 'text': 'Add the history state and the retry substate.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why flat machines explode and statecharts compress them.'},
            {'label': 'Implementation Design', 'text': 'Design a statechart for a CI pipeline: build, test (parallel jobs), deploy (with rollback states). What are the regions?'},
            {'label': 'Boundary Testing', 'text': 'Two parallel regions must both finish before the parent proceeds. Design the completion guard and the timeout.'},
        ],
        'takeaways': [
            'Statecharts add hierarchy, parallelism, and history',
            'Nested substates replace state explosion',
            'Orthogonal regions model independent work',
            'Explicit models beat scattered conditionals',
        ],
        'further': [
            {'title': 'The World of Statecharts — Harel', 'url': 'https://statecharts.dev/'},
            {'title': 'XState — statechart concepts', 'url': 'https://stately.ai/docs/statecharts-overview'},
        ],
    },
    {
        'title': 'State: Review & Mastery Quiz',
        'desc': 'Scenario questions on objects, machines, and charts.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate state concepts',
            'Design machines',
            'Model complexity',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: In the state pattern, behavior lives? (A: in state objects / B: in if-chains / C: in the DB)',
                'Q2: Transitions are owned by? (A: the state objects / B: the callers / C: the cache)',
                'Q3: A state machine centralizes? (A: states, events, guards / B: money / C: logs)',
                'Q4: True or false: persisted state makes workflows resumable.',
                'Q5: Statecharts add? (A: hierarchy and parallelism / B: caching / C: sharding)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A payment flow: authorized -> captured -> settled, with a partial-refund substate. Design the machine and its guards.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why a state machine is documentation that runs.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'State as objects or as tables — explicit either way',
            'Machines audit, persist, and resume',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# STRANGLER FIG
# ─────────────────────────────────────────────────────────────────────────────
_t('strangler-fig', [
    {
        'title': 'Strangler Fig: Replace a System Slowly',
        'desc': 'Gradually replacing a legacy system with new pieces, retiring the old as you go.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the strangler pattern',
            'Route incrementally',
            'Avoid the big-bang rewrite',
            'Retire legacy pieces',
        ],
        'prereqs': ['patterns/facade', 'patterns/proxy'],
        'sections': [
            {'heading': 'The Model', 'paras': [
                'Named after the fig that grows around a host tree and eventually replaces it, the pattern builds the new system next to the old one, routes traffic over incrementally, and retires legacy pieces once the new ones carry them. No big-bang rewrite: the system is replaced feature by feature, safely.',
            ], 'code': {'lang': 'text', 'body': '''
Strangler fig flow:
  1. A facade/router sits in front of the legacy system.
  2. New capability is built in the new system behind the same
     interface.
  3. The router sends that feature's traffic to the new system.
  4. When the new system covers a legacy feature, the legacy
     implementation is retired.
  5. Eventually the router only points at the new system and
     the legacy host dies.
Rules that keep it safe:
  - the facade interface must not change during the migration
  - each feature ships with a rollback (route back to legacy)
  - legacy pieces are deleted, not abandoned (no zombie code)'''}},
            {'heading': 'Why Not Rewrite', 'paras': [
                'Big-bang rewrites fail: the legacy encodes years of hard-won behavior that a rewrite cannot reproduce at once. Strangling delivers value continuously — each feature ships, each risk is contained — and keeps the old system as the safety net until its last feature is replaced.',
            ]},
        ],
        'practice': {
            'title': 'Strangle the Monolith',
            'intro': 'A 10-year-old billing monolith: invoices move to the new service first, payments later.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the facade and the routing rule per feature.'},
                {'label': 'Task 2', 'text': 'Plan the feature order by risk and value.'},
                {'label': 'Task 3', 'text': 'Design the rollback for the first migrated feature.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why incremental replacement beats the big-bang rewrite. Start with risk.'},
            {'label': 'Compare & Contrast', 'text': 'Compare strangler with the branch-by-abstraction and the anti-corruption layer. When does each apply?'},
            {'label': 'Boundary Testing', 'text': 'A migrated feature has a subtle legacy edge case. Design the shadow-traffic comparison that catches it before cutover.'},
        ],
        'takeaways': [
            'Strangler replaces systems feature by feature',
            'A stable facade makes routing reversible',
            'Each migration ships with a rollback',
            'Retired pieces are deleted, not abandoned',
        ],
        'further': [
            {'title': 'Strangler Fig — Martin Fowler', 'url': 'https://martinfowler.com/bliki/StranglerFigApplication.html'},
            {'title': 'Strangler pattern — Microsoft', 'url': 'https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig'},
        ],
    },
    {
        'title': 'Strangler Fig in Production: APIs and Databases',
        'desc': 'Migrating APIs, databases, and monoliths with strangler techniques.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Strangle APIs incrementally',
            'Migrate databases safely',
            'Use dual writes and backfill',
            'Manage the coexistence window',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'API Strangling', 'paras': [
                'A gateway fronts both systems; routes move endpoint by endpoint. The new service implements the same contract, the gateway flips one route, and observability compares behavior. Coexistence: both systems run, sharing the database or not — the dual-write and backfill pattern migrates data while both write.',
            ], 'code': {'lang': 'text', 'body': '''
API strangling sequence:
  - gateway routes /v1/invoices -> legacy, /v1/orders -> new
  - each endpoint flips independently with a rollback
  - contract tests run against both sides during coexistence
Database migration (dual-write):
  - new schema added alongside the old
  - every write goes to both; a backfill copies history
  - reads move over when the new side is verified
  - the old column/table is dropped only after a grace window
  - change data capture (CDC) keeps both sides in sync
  The coexistence window is where incidents happen: plan the
  data sync, the rollback, and the cutover drill.'''}},
            {'heading': 'Order of Operations', 'paras': [
                'Read-only features migrate first (lowest risk), then read-write, then writes with data migration. The database is usually the last strangler target — it is the hardest to dual-run. The monolith shrinks as modules move out; the gateway grows as the routing map fills.',
            ]},
        ],
        'practice': {
            'title': 'Strangle the Checkout',
            'intro': 'A checkout API and its orders table must move out of the monolith to a new service.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the gateway routes and the migration order (reads first).'},
                {'label': 'Task 2', 'text': 'Design the dual-write, backfill, and cutover for orders.'},
                {'label': 'Task 3', 'text': 'Design the rollback: what happens if cutover fails at 90% traffic?'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why read-only features migrate first and the database migrates last.'},
            {'label': 'Implementation Design', 'text': 'Design a dual-write migration for a users table: the new table, the sync, the verify, and the drop schedule.'},
            {'label': 'Boundary Testing', 'text': 'Dual writes diverge and the new table is missing a row. Design the CDC catch-up and the verification that finds it.'},
        ],
        'takeaways': [
            'Gateways route endpoint by endpoint',
            'Databases migrate with dual writes and backfill',
            'Reads move before writes',
            'The coexistence window needs a cutover drill',
        ],
        'further': [
            {'title': 'Strangler Fig Application — Fowler', 'url': 'https://martinfowler.com/bliki/StranglerFigApplication.html'},
            {'title': 'Branch by abstraction', 'url': 'https://martinfowler.com/bliki/BranchByAbstraction.html'},
        ],
    },
    {
        'title': 'Advanced Strangler: Parallel Run and Shadow Traffic',
        'desc': 'Shadowing traffic, comparing outputs, and automated cutover decisions.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Run systems in parallel',
            'Shadow traffic to compare',
            'Automate cutover decisions',
            'Manage feature toggles',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Shadow Traffic', 'paras': [
                'Before a cutover, duplicate production traffic to the new system (shadow mode) and compare outputs — responses, errors, side effects. The comparison is the evidence the migration is safe. Discrepancies are analyzed; when the discrepancy rate drops to zero, the cutover is a formality, not a gamble.',
            ], 'code': {'lang': 'go', 'body': '''
// Shadow traffic: send a copy to the new system, compare
func (g *Gateway) Handle(w http.ResponseWriter, r *http.Request) {
    // primary: legacy (during migration) or new (after)
    res := g.primary.Handle(r)
    if g.shadowEnabled(r) {
        shadowRes := g.shadow.Handle(r)   // new system, ignored output
        go g.compare(r, res, shadowRes)   // diff in the background
    }
    write(w, res)                          // user sees the primary only
}
// compare() records: matched, mismatch, error-only-in-shadow.
// A week of zero mismatches = evidence the cutover is safe.
// Feature toggles flip routes per user/region without deploys.'''}},
            {'heading': 'Automating the Cutover', 'paras': [
                'With continuous comparison, cutover becomes a toggle flip gated by the discrepancy metric — the automation releases only when the shadow matches for the required window. Toggles give instant rollback. The discipline: every toggle has an owner, a review, and a deletion date.',
            ]},
        ],
        'practice': {
            'title': 'Gate the Cutover',
            'intro': 'A payment feature is 90% migrated; the last 10% must not regress on edge cases.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the shadow pipeline and the comparison metric.'},
                {'label': 'Task 2', 'text': 'Design the toggle and the gate: zero mismatches for 7 days.'},
                {'label': 'Task 3', 'text': 'Design the rollback toggle and the discrepancy alert.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why shadow traffic turns cutover from a gamble into evidence.'},
            {'label': 'Implementation Design', 'text': 'Design a shadow comparison for an idempotent payment API: what is compared, what is ignored, and how are mismatches triaged?'},
            {'label': 'Boundary Testing', 'text': 'Shadow traffic itself causes side effects (double side effects from the shadow system). Design the dry-run mode that prevents them.'},
        ],
        'takeaways': [
            'Shadow traffic duplicates production to compare',
            'Mismatch rates are the migration evidence',
            'Toggles make cutover and rollback instant',
            'Toggles need owners and deletion dates',
        ],
        'further': [
            {'title': 'Parallel Change — Fowler', 'url': 'https://martinfowler.com/bliki/ParallelChange.html'},
            {'title': 'Dark launch / shadow traffic', 'url': 'https://martinfowler.com/articles/feature-toggles.html'},
        ],
    },
    {
        'title': 'Strangler Fig: Review & Mastery Quiz',
        'desc': 'Scenario questions on migration, coexistence, and evidence.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate strangler concepts',
            'Plan migrations',
            'Gate cutovers',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: The strangler pattern? (A: replaces systems incrementally / B: rewrites at once / C: restart)',
                'Q2: A stable facade makes routing? (A: reversible / B: permanent / C: fast)',
                'Q3: Database migrations use? (A: dual writes and backfill / B: downtime / C: backups only)',
                'Q4: True or false: read-only features migrate first.',
                'Q5: Shadow traffic provides? (A: comparison evidence / B: revenue / C: cache)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A 15-year-old CRM must move to microservices. Design the strangler plan: order of features, the gateway, and the cutover gates.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why replacing a system is a migration, not an event.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Incremental, reversible, evidence-gated',
            'The legacy is a safety net until the last feature moves',
        ],
    },
])
