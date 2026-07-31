#!/usr/bin/env python3
"""Deep curriculum data chunk 3: consistency-pattern, convention-over-configuration, cqs, defensive-programming."""

TOPICS = {}


def _t(slug, topics):
    TOPICS[slug] = topics
    return topics


# ─────────────────────────────────────────────────────────────────────────────
# CONSISTENCY PATTERN
# ─────────────────────────────────────────────────────────────────────────────
_t('consistency-pattern', [
    {
        'title': 'Consistency Patterns: From Strong to Eventual',
        'desc': 'The spectrum of consistency guarantees and how to choose one per data path.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Order consistency levels from strong to eventual',
            'Define strong, causal, and eventual consistency',
            'Map workloads to appropriate consistency levels',
            'Explain the cost of stronger guarantees',
        ],
        'prereqs': ['principles/cap-theorem', 'principles/eventual-consistency'],
        'sections': [
            {'heading': 'The Consistency Spectrum', 'paras': [
                'Consistency is not binary. From strongest to weakest: linearizable (strong), sequential, causal, read-your-writes / monotonic reads, and eventual. Each step down buys availability and latency; each step up buys predictability.',
                'Strong consistency means every read sees the latest committed write, as if there were a single copy. It costs: writes must synchronize across replicas before returning.',
            ], 'code': {'lang': 'text', 'body': '''
Consistency spectrum (strong -> weak):
  Linearizable   : reads see latest write, real-time ordered
  Sequential     : operations ordered, no real-time guarantee
  Causal         : causally related writes seen in order
  Read-your-writes: you always see your own writes
  Monotonic reads: reads never go backwards in time
  Eventual       : replicas converge given quiet time'''}},
            {'heading': 'Choosing a Guarantee', 'paras': [
                'The rule: match the guarantee to the failure cost. Money and inventory need strong or quorum consistency. Feeds, counters, and profiles tolerate eventual consistency with bounded staleness.',
                'Most systems use a mix — strong for the critical path, eventual for the rest — rather than one global setting.',
            ]},
        ],
        'practice': {
            'title': 'Assign Guarantees',
            'intro': 'For each operation pick a consistency level: withdraw cash, show friend count, post a comment, decrement stock, show chat typing indicator.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Justify each choice with the worst-case user-visible failure.'},
                {'label': 'Task 2', 'text': 'For stock decrement, explain why two concurrent decrements must not oversell.'},
                {'label': 'Task 3', 'text': 'Design read-your-writes for the comment system so the author sees their own post instantly.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about the cost difference between strong and eventual consistency in a multi-region setup. Start with write latency.'},
            {'label': 'Compare & Contrast', 'text': 'Compare linearizable, causal, and eventual consistency in a collaborative editing app. Which guarantee does each CRDT provide?'},
            {'label': 'Boundary Testing', 'text': 'A system needs strong consistency only for a single key (balance). Design a hybrid that is strong for that key and eventual for everything else.'},
        ],
        'takeaways': [
            'Consistency is a spectrum, not a binary',
            'Strong guarantees cost latency and availability',
            'Match the guarantee to the failure cost per data path',
            'Hybrid systems mix levels by key or operation',
        ],
        'further': [
            {'title': 'Consistency Models — Jepsen', 'url': 'https://jepsen.io/consistency'},
            {'title': 'CAP Twelve Years Later', 'url': 'https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/'},
        ],
    },
    {
        'title': 'Consistency in Production: Quorums and Transactions',
        'desc': 'Quorum reads/writes, serializable transactions, and where they are worth the cost.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Apply quorum-based consistency to reads and writes',
            'Explain serializable transactions and their cost',
            'Design optimistic concurrency for consistency',
            'Handle cross-key consistency needs',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quorum Consistency in Practice', 'paras': [
                'With N replicas, W writes and R reads with W + R > N guarantee a read sees the latest write. This is how Dynamo-style systems provide configurable consistency: tune W and R per operation.',
            ], 'code': {'lang': 'text', 'body': '''
Quorum rules (N replicas, W writes, R reads):
  W + R > N  -> read sees latest write (quorum consistency)
  W > N/2    -> writes conflict only if concurrent (common)
  R = 1, W = N -> strong for reads, slow for writes'''}},
            {'heading': 'Serializable Transactions', 'paras': [
                'Serializable isolation makes concurrent transactions behave as if run one after another — the strongest database guarantee. It is expensive: conflict detection (locking or validation) on every transaction.',
                'Use it where money, inventory, and uniqueness rules live. Everywhere else, weaker isolation with optimistic locking is cheaper.',
            ]},
        ],
        'practice': {
            'title': 'Tune the Quorum',
            'intro': 'A 5-node cart service. Reads must never show a lost item; writes must survive a node loss.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Choose W and R with W+R>5 and W>2. Compute availability under 1-node and 2-node failure.'},
                {'label': 'Task 2', 'text': 'Explain the latency cost of W=3 writes in a 3-region deployment.'},
                {'label': 'Task 3', 'text': 'Design the read path so carts read-your-writes without global strong consistency.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why W+R>N is sufficient for a read to see the latest write, and what happens with W+R=N. Ask me to verify with small examples.'},
            {'label': 'Implementation Design', 'text': 'Design a reservation system where two users cannot book the same seat, using optimistic concurrency. Where is the conflict detected?'},
            {'label': 'Boundary Testing', 'text': 'Quorum says the latest write is visible, but the read replica is behind. Is that a contradiction? Explain with W=3, R=3, N=5.'},
        ],
        'takeaways': [
            'W+R>N is the quorum consistency condition',
            'Serializable isolation is the strongest, most expensive guarantee',
            'Optimistic concurrency trades retries for availability',
            'Tune consistency per operation, not per system',
        ],
        'further': [
            {'title': 'DynamoDB Read Consistency Options', 'url': 'https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html'},
            {'title': 'Isolation Levels — PostgreSQL Docs', 'url': 'https://www.postgresql.org/docs/current/transaction-iso.html'},
        ],
    },
    {
        'title': 'Advanced Consistency: Causal Ordering and Conflict Resolution',
        'desc': 'Causal consistency, vector clocks, and resolving concurrent writes without a single writer.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Explain causal consistency and why apps need it',
            'Use vector clocks to detect concurrent writes',
            'Design conflict resolution policies',
            'Implement last-writer-wins with correct clocks',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Causal Consistency', 'paras': [
                'Causal consistency guarantees that causally related operations are seen in the same order everywhere — the "I replied to your message, so my reply must be visible after your message" guarantee. It is stronger than eventual, cheaper than strong, and often exactly what chat and feeds need.',
                'Tracking causality is done with vector clocks: each replica maintains a counter per replica, and the full vector establishes happens-before relationships between writes.',
            ], 'code': {'lang': 'python', 'body': '''
# Vector clock: detect causality between writes
class VectorClock:
    def __init__(self, replica, counters=None):
        self.replica = replica
        self.counters = counters or {}     # replica -> logical time

    def tick(self):
        self.counters[self.replica] = self.counters.get(self.replica, 0) + 1

    def merge(self, other):
        for r, c in other.counters.items():
            self.counters[r] = max(self.counters.get(r, 0), c)

    def happens_before(self, other):
        # True if every counter <= other's and at least one <
        return all(self.counters.get(r, 0) <= other.counters.get(r, 0)
                   for r in self.counters) and \\
               any(self.counters.get(r, 0) < other.counters.get(r, 0)
                   for r in self.counters)'''.replace('\\\\', '\\')}},
            {'heading': 'Resolving Concurrent Writes', 'paras': [
                'When two writes are concurrent (neither happens-before the other), the system must pick: merge (CRDT), last-writer-wins (needs trustworthy clocks), or escalate to the application. The choice is a product decision, not a database one.',
            ]},
        ],
        'practice': {
            'title': 'Detect and Resolve Conflict',
            'intro': 'A note-taking app: the same note is edited offline on two devices, then both sync.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Use vector clocks to classify the two edits: one-after-other or concurrent?'},
                {'label': 'Task 2', 'text': 'Design a merge that keeps both edits (per-field merge) and identify which fields conflict.'},
                {'label': 'Task 3', 'text': 'Add LWW for the title field with a hybrid logical clock. Explain what breaks if clocks are not synchronized.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why wall-clock timestamps alone cannot establish causality, and what a vector clock adds.'},
            {'label': 'Implementation Design', 'text': 'Design causal delivery for a chat system: messages within a conversation must appear in causal order even across devices and offline periods.'},
            {'label': 'Boundary Testing', 'text': 'Two replicas exchange states and their vector clocks both grow unboundedly. Design a pruning strategy that does not break causality.'},
        ],
        'takeaways': [
            'Causal consistency orders causally related writes everywhere',
            'Vector clocks detect concurrency precisely',
            'Conflict resolution is a product decision',
            'LWW needs trustworthy clocks or hybrid logical clocks',
        ],
        'further': [
            {'title': 'Vector Clocks — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Vector_clock'},
            {'title': 'Hybrid Logical Clocks', 'url': 'https://cse.buffalo.edu/tech-reports/2014-04.pdf'},
        ],
    },
    {
        'title': 'Consistency Patterns: Review & Mastery Quiz',
        'desc': 'Scenario questions on the consistency spectrum, quorums, and conflict resolution.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate consistency concepts',
            'Apply guarantees to workloads',
            'Spot consistency anti-patterns',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: The strongest consistency level is? (A: eventual / B: linearizable / C: causal)',
                'Q2: W+R>N guarantees? (A: serializability / B: read sees latest write / C: no conflicts)',
                'Q3: Vector clocks detect? (A: latency / B: causality / C: partitions)',
                'Q4: True or false: stronger consistency always costs availability during partitions.',
                'Q5: A chat reply appearing before its parent message is a violation of? (A: causality / B: durability / C: idempotency)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A distributed ledger needs strict ordering for transfers but tolerates lag for balance displays. Design the consistency split and justify with failure costs.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why eventual consistency is not "wrong" but a deliberate, bounded trade-off.'},
        ],
        'takeaways': [
            'Q1: B; Q2: B; Q3: B; Q4: true; Q5: A',
            'Consistency guarantees are per-path contracts',
            'The cheapest guarantee that meets the failure cost is the right one',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# CONVENTION OVER CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────
_t('convention-over-configuration', [
    {
        'title': 'Convention over Configuration: Defaults Beat Settings',
        'desc': 'Why sensible defaults reduce decisions and make codebase navigation effortless.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Define convention over configuration',
            'List benefits: less code, faster onboarding, fewer mistakes',
            'Identify good conventions in frameworks you know',
            'Recognize when conventions become traps',
        ],
        'prereqs': ['principles/kiss', 'principles/dry'],
        'sections': [
            {'heading': 'The Principle', 'paras': [
                'Convention over configuration means the framework (or codebase) provides sensible defaults, and configuration is needed only where you deviate. Rails\' "convention over configuration", Spring Boot\'s autoconfiguration, and Next.js\' file-based routing all follow it.',
                'The result: a new engineer opening the codebase can predict where things live, because the structure follows the convention — not a sprawling config file that must be studied.',
            ], 'code': {'lang': 'text', 'body': '''
Convention examples you already use:
  Next.js    : app/route/page.tsx  -> /route (no router config)
  Rails      : POST /users maps to UsersController#create
  Spring Boot: src/main/resources/application.yml, no XML
  Testing    : *.test.ts next to source (no test config)'''}},
            {'heading': 'The Trade-Off', 'paras': [
                'Conventions reduce decisions but hide behavior: a newcomer may not know a default exists or what it does. The fix is discoverability — the convention must be documented, consistent, and overridable.',
                'A convention that requires violating it often is a bad convention. If 80% of cases deviate, invert the default.',
            ]},
        ],
        'practice': {
            'title': 'Audit Your Codebase',
            'intro': 'Look at your current project: folder structure, naming, config files, test placement.',
            'tasks': [
                {'label': 'Task 1', 'text': 'List three conventions already in use and where they are documented.'},
                {'label': 'Task 2', 'text': 'Find one place where a file had to be discovered through config rather than convention. Would a rename or move fix it?'},
                {'label': 'Task 3', 'text': 'Write a one-page conventions doc for a new teammate, covering naming, structure, and testing.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about when a framework convention helps versus hides. Start with a concrete framework default you like.'},
            {'label': 'Compare & Contrast', 'text': 'Compare Rails (convention-first) with early Java EE XML-config (config-first). What developer-experience metrics differ?'},
            {'label': 'Boundary Testing', 'text': 'A team has a strict convention but one module legitimately needs a different structure. Design the documented escape hatch that keeps the rest conventional.'},
        ],
        'takeaways': [
            'Sensible defaults remove decisions and onboarding friction',
            'Discoverability and documentation make conventions safe',
            'Bad conventions are ones you must frequently violate',
            'Escape hatches must be explicit and documented',
        ],
        'further': [
            {'title': 'Convention over Configuration — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Convention_over_configuration'},
            {'title': 'Rails Doctrine', 'url': 'https://rubyonrails.org/doctrine'},
        ],
    },
    {
        'title': 'Conventions in Production: Structure and Onboarding',
        'desc': 'How strong conventions shape large codebases, review, and team velocity.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design folder and naming conventions for a monorepo',
            'Make conventions enforceable with tooling',
            'Balance convention with flexibility for outliers',
            'Measure onboarding time as a convention metric',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Enforceable Conventions', 'paras': [
                'Conventions enforced by tooling (linters, formatters, generators, CI checks) are the only reliable ones. A convention documented in a wiki decays; one enforced by a lint rule or a scaffolding CLI does not.',
            ], 'code': {'lang': 'text', 'body': '''
Tooling that enforces convention:
  eslint + prettier        : style & patterns
  folder-lint / structure  : repo layout rules
  codegen / scaffolder     : new modules follow the template
  review bots              : flag deviations automatically'''}},
            {'heading': 'The Monorepo Convention Set', 'paras': [
                'A well-conventional monorepo answers instantly: where is the service, where are its tests, where do shared types live, how is it deployed. Every new module is a clone of the template, so "how do I add X?" has one answer.',
                'The cost: outliers need justification, and structural refactors touch everything at once. Versioned conventions (a migration plan for the convention itself) keep it from fossilizing.',
            ]},
        ],
        'practice': {
            'title': 'Design the Module Template',
            'intro': 'Your team adds 2 new microservices per month and onboarding takes 3 weeks.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the canonical service folder structure (src, tests, config, docs, CI).'},
                {'label': 'Task 2', 'text': 'Write the scaffolding command that generates it, and the lint rules that keep it intact.'},
                {'label': 'Task 3', 'text': 'Define the one-page template doc a new service must follow, and where it lives.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why "documented in the wiki" is not enough for a convention and what enforcement layers exist. Ask me to rank them by reliability.'},
            {'label': 'Implementation Design', 'text': 'Design a versioned conventions doc: how do you propose, review, and migrate a breaking convention change across a monorepo?'},
            {'label': 'Boundary Testing', 'text': 'One team\'s service needs a nonstandard structure (e.g., a long-running worker). Design the documented exception process.'},
        ],
        'takeaways': [
            'Tooling enforcement beats documentation',
            'Templates make "how do I add X" have one answer',
            'Exceptions need a documented, reviewable process',
            'Conventions themselves need versioning and migration plans',
        ],
        'further': [
            {'title': 'Monorepo Conventions — Nx', 'url': 'https://nx.dev/concepts/why-monorepos'},
            {'title': 'Folder Structure Best Practices', 'url': 'https://www.martinfowler.com/articles/web-security-basics.html'},
        ],
    },
    {
        'title': 'Advanced Convention: Domain Structure and Codegen',
        'desc': 'Domain-driven structure, code generation, and conventions that scale to hundreds of modules.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Design domain-driven folder conventions',
            'Generate boilerplate from conventions safely',
            'Version conventions as code',
            'Avoid convention traps: magic and indirection',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Domain Structure', 'paras': [
                'Organize by domain (billing/, orders/, identity/) rather than by technical layer (controllers/, services/, models/), so each feature is a self-contained unit. Within a domain, the layering convention applies uniformly.',
            ], 'code': {'lang': 'text', 'body': '''
Domain-first convention (per domain folder):
  orders/
    api/        # routes/handlers
    domain/     # entities, value objects, rules
    app/        # use cases / services
    infra/      # persistence, queues, clients
    tests/
The same shape for every domain -> predictable navigation'''}},
            {'heading': 'Codegen and Convention Versioning', 'paras': [
                'Generators turn conventions into instant, consistent artifacts: a new domain scaffolded by a CLI is identical in shape to every other. The generator IS the documented convention.',
                'Version the generator with the repo; when the convention evolves, the generator and its outputs migrate together, and CI fails on stale-shaped modules.',
            ]},
        ],
        'practice': {
            'title': 'Build the Scaffolder',
            'intro': 'Your team creates a new domain folder by hand every time, and they differ subtly.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Specify the generator inputs (domain name, entities) and outputs (all folders + skeletons).'},
                {'label': 'Task 2', 'text': 'Add a CI check that validates every domain folder matches the current template.'},
                {'label': 'Task 3', 'text': 'Design the migration path when the convention changes: rename, regenerate, or dual-run?'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can articulate when code generation helps versus when it creates a second source of truth.'},
            {'label': 'Implementation Design', 'text': 'Design a convention system for a 200-module monorepo where 10 teams contribute. How do you make conventions cross-team and enforced?'},
            {'label': 'Boundary Testing', 'text': 'A generator creates boilerplate that drifts from hand-written modules. Design a drift detector and a fix workflow.'},
        ],
        'takeaways': [
            'Domain-first structure scales to hundreds of modules',
            'Generators turn conventions into enforced artifacts',
            'Version generators and migrate outputs together',
            'CI drift checks keep convention decay out',
        ],
        'further': [
            {'title': 'Feature-Sliced Design', 'url': 'https://feature-sliced.design/'},
            {'title': 'Code Generation — AWS Amplify / Prisma Philosophy', 'url': 'https://www.prisma.io/docs'},
        ],
    },
    {
        'title': 'Convention over Configuration: Review & Mastery Quiz',
        'desc': 'Scenario questions on defaults, enforcement, and structure.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate convention concepts',
            'Design enforceable conventions',
            'Spot convention traps',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: The main benefit of convention over configuration is? (A: fewer decisions / B: more options / C: faster runtime)',
                'Q2: A convention that 80% of cases violate should be? (A: kept strict / B: inverted / C: documented more)',
                'Q3: The most reliable way to keep a convention is? (A: wiki / B: tooling enforcement / C: meetings)',
                'Q4: True or false: exceptions to conventions should be silent.',
                'Q5: Domain-first structure organizes by? (A: technical layer / B: business domain / C: team size)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'Your 50-module monorepo has drifted: five modules deviate from the template. Design a measurement, an enforcement rule, and a migration plan that does not block delivery.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why default decisions matter more than configuration flexibility for team velocity.'},
        ],
        'takeaways': [
            'Q1: A; Q2: B; Q3: B; Q4: false; Q5: B',
            'Conventions should be few, strong, and enforced',
            'Discoverability and escape hatches keep them humane',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# CQS (COMMAND QUERY SEPARATION)
# ─────────────────────────────────────────────────────────────────────────────
_t('cqs', [
    {
        'title': 'Command Query Separation: Mutations and Reads Never Mix',
        'desc': 'Why methods that both change state and return values create the worst bugs.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Define commands and queries precisely',
            'Explain why mixing them is dangerous',
            'Refactor a mixed method into command + query',
            'Identify CQS violations in real code',
        ],
        'prereqs': ['principles/single-responsibility', 'principles/separation-of-concerns'],
        'sections': [
            {'heading': 'The Rule', 'paras': [
                'CQS (Bertrand Meyer): a method is either a command that changes state and returns nothing, or a query that returns a value and changes nothing. Never both.',
                'A mixed method — "pop() returns the last element and removes it" — is a state-changing expression: callers may ignore the return (mutating) or call twice (reading), and each misuse hides a bug.',
            ], 'code': {'lang': 'java', 'body': '''
// Violation: pop() mutates AND returns — caller must know both
Item item = stack.pop();          // is item the last one? was it removed?

// CQS: command + query separated
Item peek() { return stack.get(size() - 1); }  // query: no change
void  pop() { stack.remove(size() - 1); }      // command: no return
// Usage is now explicit:
if (!stack.isEmpty()) {
    Item top = stack.peek();
    stack.pop();
}'''}},
            {'heading': 'Why It Matters', 'paras': [
                'Queries are safe to call anywhere, any number of times, in any order — they enable caching, memoization, and parallelism. Commands are the opposite: order matters, repetition matters. Mixing the two destroys the ability to reason about either.',
                'CQS is the object-level twin of the database pattern: reads and writes take different paths (CQRS) and can be scaled independently.',
            ]},
        ],
        'practice': {
            'title': 'Find and Fix Violations',
            'intro': 'Review these signatures and refactor the mixed ones: setBalance(x) returns boolean, getAndIncrement() returns int, deleteUser(id) returns User, findById(id) returns Optional.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Classify each as command, query, or mixed.'},
                {'label': 'Task 2', 'text': 'Refactor getAndIncrement() into get() + increment().'},
                {'label': 'Task 3', 'text': 'For setBalance(x) returning success, explain why throwing or returning a result object is the CQS-clean alternative.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why "returns the old value" variants are worse than plain mixed methods. Start with thread safety.'},
            {'label': 'Compare & Contrast', 'text': 'Compare CQS with CQRS (event-sourced read models). When does the object-level rule scale into the architecture-level pattern?'},
            {'label': 'Boundary Testing', 'text': 'A cache get() populates the cache on miss — it mutates internal state but returns a value. Is this a CQS violation? Argue both sides.'},
        ],
        'takeaways': [
            'Commands change state and return nothing',
            'Queries return values and change nothing',
            'Mixed methods destroy reasoning about both behaviors',
            'CQS scales into CQRS at the architecture level',
        ],
        'further': [
            {'title': 'Command Query Separation — Martin Fowler', 'url': 'https://martinfowler.com/bliki/CommandQuerySeparation.html'},
            {'title': 'CQRS — Martin Fowler', 'url': 'https://martinfowler.com/bliki/CQRS.html'},
        ],
    },
    {
        'title': 'CQS in Production: APIs and Services',
        'desc': 'Applying CQS to REST APIs, service methods, and read/write scaling.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Map HTTP methods to commands and queries',
            'Design services with explicit command and query interfaces',
            'Use read models for query-heavy paths',
            'Avoid hidden mutations in getters',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'REST as CQS', 'paras': [
                'REST already models the split: GET is a query (safe, idempotent), POST/PUT/DELETE are commands (mutating). Violations appear when a GET has side effects or a POST returns a big payload that should be a follow-up GET.',
            ], 'code': {'lang': 'text', 'body': '''
REST as CQS:
  GET    /orders/123        -> query, no side effects
  POST   /orders            -> command, returns 201 + location
  DELETE /orders/123        -> command, returns 204
Anti-pattern: GET /orders/123/refresh  (mutation via GET)
Anti-pattern: POST /orders  returning the full rendered page'''}},
            {'heading': 'Service-Level Split', 'paras': [
                'Split service methods into CommandService and QueryService. Query methods can be cached, replicated, and read-replicas can serve them; command methods take the transactional, validated path. This is CQRS in miniature, without the event-sourcing ceremony.',
            ]},
        ],
        'practice': {
            'title': 'Refactor a REST API',
            'intro': 'POST /api/login both authenticates (mutation) and returns the full user profile with 20 fields.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Redesign as POST /api/sessions returning only a token, plus GET /api/me for the profile.'},
                {'label': 'Task 2', 'text': 'List every hidden side effect in your current GET endpoints.'},
                {'label': 'Task 3', 'text': 'Decide which GET endpoints should serve from a read model and why.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why "GET that increments a counter" is a CQS violation and a caching hazard.'},
            {'label': 'Implementation Design', 'text': 'Design the command/query split for a billing service: create-invoice (command), list-invoices (query), reconcile (command). Where do read replicas fit?'},
            {'label': 'Boundary Testing', 'text': 'A command must return the ID of the created entity. How do you keep CQS clean? (return 201 + Location header, or a result record)'},
        ],
        'takeaways': [
            'GET is query; POST/PUT/DELETE are commands',
            'Explicit command/query service interfaces scale reads',
            'Read models decouple query shape from write model',
            'Return identifiers and locations, not payloads, from commands',
        ],
        'further': [
            {'title': 'REST API Design Best Practices', 'url': 'https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design'},
            {'title': 'CQRS Journey Guide', 'url': 'https://learn.microsoft.com/en-us/previous-versions/msp-n-p/jj554200(v=pandp.10)'},
        ],
    },
    {
        'title': 'Advanced CQS: CQRS and Event Sourcing',
        'desc': 'Full command/query responsibility segregation with read models and event sourcing.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Design a CQRS system with separate read and write models',
            'Explain when event sourcing complements CQRS',
            'Manage read-model consistency (eventual vs synchronous)',
            'Avoid CQRS complexity where it is not needed',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'CQRS: Separate Models', 'paras': [
                'CQRS gives commands and queries different models, storage, and scaling. Writes go to the transactional write model; reads are served by optimized read models (denormalized projections) built from the write stream.',
                'The cost: eventual consistency between write and read models, plus the machinery to project and rebuild them. Use it when read and write shapes diverge sharply or reads dominate.',
            ], 'code': {'lang': 'text', 'body': '''
CQRS topology:
  Command side:  POST /orders -> write model (normalized, transactional)
  Event stream:  order.created, order.paid, order.shipped
  Projection:    builds read model (denormalized order summaries)
  Query side:    GET /orders?status=paid -> read model (fast, shaped)
Consistency: eventual between stream and projection.'''}},
            {'heading': 'Event Sourcing', 'paras': [
                'Event sourcing stores every state change as an event (append-only) and derives current state by replay. It gives perfect audit history and makes projections trivial — at the cost of complexity, eventual read models, and schema evolution of the event stream.',
                'CQRS + event sourcing is powerful but is a heavy tool: most systems need only the service-level CQS split, not the full architecture.',
            ]},
        ],
        'practice': {
            'title': 'Design a Projection',
            'intro': 'An orders service: writes are normalized; the dashboard needs aggregated daily revenue by region.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the events and the projection that builds the daily-revenue read model.'},
                {'label': 'Task 2', 'text': 'Handle projection lag: what does the dashboard show during a replay?'},
                {'label': 'Task 3', 'text': 'Design rebuild-from-scratch for the read model after a bug in the projection.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can articulate the difference between CQS (method-level) and CQRS (architecture-level) and when each applies.'},
            {'label': 'Implementation Design', 'text': 'Design an event-sourced cart with projections for cart view, analytics, and recommendations. How do you version the events?'},
            {'label': 'Boundary Testing', 'text': 'The read model lags and a user sees a stale order status. Design a per-user read-your-writes projection or a sync boundary.'},
        ],
        'takeaways': [
            'CQRS separates read and write models end-to-end',
            'Event sourcing makes projections and audit trails natural',
            'Read models are eventually consistent with the write stream',
            'CQRS+ES is heavy — apply it only where shapes diverge',
        ],
        'further': [
            {'title': 'CQRS — Martin Fowler', 'url': 'https://martinfowler.com/bliki/CQRS.html'},
            {'title': 'Event Sourcing — Microsoft Docs', 'url': 'https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing'},
        ],
    },
    {
        'title': 'CQS: Review & Mastery Quiz',
        'desc': 'Scenario questions on command/query separation across levels.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate CQS concepts',
            'Classify APIs and methods correctly',
            'Apply CQRS where appropriate',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: A query should? (A: mutate / B: return a value without mutation / C: do both)',
                'Q2: GET /orders that deletes an order violates? (A: CQS / B: DRY / C: YAGNI)',
                'Q3: CQRS separates? (A: read and write models / B: teams / C: databases only)',
                'Q4: True or false: event sourcing stores only the latest state.',
                'Q5: A cache get() that fills the cache is? (A: always a violation / B: a defensible internal optimization / C: a command)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A reporting service runs heavy queries that slow the transactional path. Design the read-model split and its consistency story.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why hiding a mutation inside a getter is a "quiet bug factory".'},
        ],
        'takeaways': [
            'Q1: B; Q2: A; Q3: A; Q4: false; Q5: B',
            'Separation enables caching, parallelism, and independent scaling',
            'Heavy tools like CQRS+ES earn their cost only on divergent shapes',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# DEFENSIVE PROGRAMMING
# ─────────────────────────────────────────────────────────────────────────────
_t('defensive-programming', [
    {
        'title': 'Defensive Programming: Code That Survives the Unexpected',
        'desc': 'Validate inputs, fail loudly, and never trust callers or external data.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the defensive mindset',
            'Validate inputs at trust boundaries',
            'Use assertions to catch programmer errors',
            'Fail loudly instead of corrupting state',
        ],
        'prereqs': ['principles/fail-fast', 'principles/kiss'],
        'sections': [
            {'heading': 'Trust Nothing', 'paras': [
                'Defensive programming assumes inputs are hostile or broken until proven otherwise. Every boundary — API, file, network, user input — validates before use. Garbage in must produce a clear error, not a corrupt state.',
                'It is not paranoia: production bugs overwhelmingly come from unvalidated inputs meeting unwritten assumptions.',
            ], 'code': {'lang': 'python', 'body': '''
# Validate at the boundary, then trust internally
def transfer(sender, recipient, amount):
    if not isinstance(sender, str) or not sender.strip():
        raise ValueError('sender must be a non-empty string')
    if amount is None or amount <= 0:
        raise ValueError('amount must be positive')
    if amount > balance(sender):
        raise InsufficientFunds(sender)
    return execute(sender, recipient, amount)'''}},
            {'heading': 'Fail Loudly', 'paras': [
                'A silent failure (log-and-continue with wrong data) is a time bomb. Fail loudly: raise, crash, or surface the error prominently. The worst outcome is a system that looks healthy while doing the wrong thing.',
            ]},
        ],
        'practice': {
            'title': 'Harden an Endpoint',
            'intro': 'POST /users accepts JSON. Malformed bodies, negative ages, and huge payloads currently flow through.',
            'tasks': [
                {'label': 'Task 1', 'text': 'List every validation the boundary needs (schema, ranges, sizes, types).'},
                {'label': 'Task 2', 'text': 'Define the error responses (4xx with specific codes) for each violation.'},
                {'label': 'Task 3', 'text': 'Decide where you fail fast versus sanitize (e.g., trim whitespace) and justify each.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about the difference between defensive checks and over-engineering. Start with the trust boundary concept.'},
            {'label': 'Compare & Contrast', 'text': 'Contrast "fail fast" with "be liberal in what you accept". When is each correct, and how do they conflict in APIs?'},
            {'label': 'Boundary Testing', 'text': 'A parser receives a 10MB JSON with 100k keys. Design the size/depth limits and their error paths.'},
        ],
        'takeaways': [
            'Validate at every trust boundary',
            'Garbage in must produce clear errors, not corruption',
            'Silent failures are the most dangerous bugs',
            'Assert programmer assumptions; validate user input',
        ],
        'further': [
            {'title': 'Defensive Programming — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Defensive_programming'},
            {'title': 'Robustness Principle — RFC', 'url': 'https://www.rfc-editor.org/rfc/rfc1122#page-18'},
        ],
    },
    {
        'title': 'Defensive Programming in Production: Errors and Fallbacks',
        'desc': 'Error handling hierarchies, fallbacks, and protecting against cascading corruption.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design an error taxonomy for a service',
            'Build safe fallbacks that never hide corruption',
            'Protect persistent state with atomic writes',
            'Log structured context for post-mortems',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Error Taxonomy', 'paras': [
                'Classify errors: expected (validation), transient (timeouts, 503), and unexpected (bugs). Each class gets a policy: expected → 4xx with message; transient → retry with backoff; unexpected → 500, alert, and detailed logs.',
            ], 'code': {'lang': 'go', 'body': '''
// Error taxonomy drives policy
var (
    ErrInvalid = errors.New("invalid input")    // expected -> 4xx
    ErrTimeout = errors.New("upstream timeout") // transient -> retry
    ErrBroken  = errors.New("internal bug")     // unexpected -> alert
)

func handle(e error) {
    switch {
    case errors.Is(e, ErrInvalid): respond(400, e)
    case errors.Is(e, ErrTimeout): retryWithBackoff(e)
    default: alertAndLog(e)                     // never swallow
    }
}'''}},
            {'heading': 'Atomic State Changes', 'paras': [
                'When a step fails partway through a multi-step write, partial state corrupts the system. Write-then-commit (WAL, temp-file + rename, outbox pattern) ensures the visible state is always a complete state.',
            ]},
        ],
        'practice': {
            'title': 'Design the Error Policy',
            'intro': 'A sync service pulls from 3 sources and writes to a local store.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Classify failures: source timeout, schema change, disk full, record too large.'},
                {'label': 'Task 2', 'text': 'Design the atomic commit for a batch (all-or-nothing per batch, retry-able).'},
                {'label': 'Task 3', 'text': 'Define what gets logged for each class so a post-mortem is possible.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why "try/catch everything" is as harmful as "catch nothing". Ask me to rank error-handling strategies.'},
            {'label': 'Implementation Design', 'text': 'Design a fallback for a feature flag service: when it is unreachable, what do you serve — and how do you avoid serving a dangerous default?'},
            {'label': 'Boundary Testing', 'text': 'A retry loop double-applies a side effect (payment). Design idempotency keys as the defensive guard.'},
        ],
        'takeaways': [
            'Classify errors to drive policy automatically',
            'Fallbacks must never hide corruption',
            'Atomic writes prevent partial-state bugs',
            'Structured logs make unexpected errors debuggable',
        ],
        'further': [
            {'title': 'Robust Error Handling — Google Style Guide', 'url': 'https://google.github.io/styleguide/'},
            {'title': 'Error Handling in Go — The Go Blog', 'url': 'https://go.dev/blog/error-handling-and-go'},
        ],
    },
    {
        'title': 'Advanced Defensive Programming: Fuzzers and Contracts',
        'desc': 'Design-by-contract, fuzzing, and making defensive checks pay for themselves.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Apply design-by-contract with preconditions and invariants',
            'Use property-based testing and fuzzing',
            'Turn defensive checks into permanent regression tests',
            'Balance defense with performance in hot paths',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Design by Contract', 'paras': [
                'Define preconditions (what callers must provide), postconditions (what the method guarantees), and invariants (what never changes). Enforced in debug builds, they catch contract violations at the first wrong step.',
            ], 'code': {'lang': 'python', 'body': '''
# Contract enforcement with assertions (debug-only in hot paths)
def debit(account, amount):
    assert amount > 0, 'precondition: positive amount'
    assert account.is_open, 'precondition: open account'
    balance = account.balance - amount
    assert balance >= account.overdraft_limit, 'postcondition: within limit'
    account.balance = balance
    assert account.balance == expected, 'invariant: balance consistency'
    return balance'''}},
            {'heading': 'Fuzzing and Property Testing', 'paras': [
                'Fuzzing feeds random, malformed inputs to parsers and finds crashes and hangs the tests never imagined. Property-based testing asserts invariants over thousands of generated inputs — the same spirit as defensive checks, but automated and exhaustive.',
                'This is defensive programming made productive: the checks you write by hand become test oracles that keep running forever.',
            ]},
        ],
        'practice': {
            'title': 'Write a Property Test',
            'intro': 'A parseUser() function parses JSON user objects.',
            'tasks': [
                {'label': 'Task 1', 'text': 'List three invariants (e.g., id is string, age >= 0 when present, name non-empty).'},
                {'label': 'Task 2', 'text': 'Write a property test that generates 1,000 random user JSONs and asserts the invariants hold or the parse raises a clean error.'},
                {'label': 'Task 3', 'text': 'Run a quick fuzz pass over the parser and fix any crashes.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why property-based testing is stronger than example-based tests for defensive code.'},
            {'label': 'Implementation Design', 'text': 'Design a contract layer for a library: preconditions enforced in debug, elided in production. Where does each check go, and how is it logged?'},
            {'label': 'Boundary Testing', 'text': 'An invariant check in a hot loop costs 2% throughput. Decide when to keep, move, or drop it, and how to measure.'},
        ],
        'takeaways': [
            'Contracts make violations visible at the first wrong step',
            'Fuzzing finds what tests never imagine',
            'Property tests turn defensive checks into permanent oracles',
            'Hot paths trade defense against measured cost',
        ],
        'further': [
            {'title': 'Design by Contract — Eiffel (Bertrand Meyer)', 'url': 'https://www.eiffel.com/values/design-by-contract/introduction/'},
            {'title': 'Hypothesis (property-based testing)', 'url': 'https://hypothesis.readthedocs.io/'},
        ],
    },
    {
        'title': 'Defensive Programming: Review & Mastery Quiz',
        'desc': 'Scenario questions on boundaries, error policies, and contracts.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate defensive concepts',
            'Design validation and error policies',
            'Choose test oracles wisely',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: The worst failure mode in defensive programming is? (A: loud error / B: silent wrong behavior / C: fast crash)',
                'Q2: Validation belongs at? (A: everywhere / B: trust boundaries / C: the UI only)',
                'Q3: Property-based testing is stronger than example tests because it? (A: runs faster / B: covers generated inputs / C: needs no code)',
                'Q4: True or false: catch-all exception handlers are good defensive practice.',
                'Q5: An invariant that must never change is best enforced by? (A: assertion / B: documentation / C: a comment)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A config parser accepts a version field; a future version adds a field you ignore. Design the defensive check that fails loudly on unknown major versions.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "the input will always be valid because we control the caller" is a dangerous assumption.'},
        ],
        'takeaways': [
            'Q1: B; Q2: B; Q3: B; Q4: false; Q5: A',
            'Defense belongs at boundaries; assertions guard internals',
            'Automated oracles make defense permanent',
        ],
    },
])
