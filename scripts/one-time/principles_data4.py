#!/usr/bin/env python3
"""Deep curriculum data chunk 4: dependency-inversion, dry, eventual-consistency, fail-fast."""

TOPICS = {}


def _t(slug, topics):
    TOPICS[slug] = topics
    return topics


# ─────────────────────────────────────────────────────────────────────────────
# DEPENDENCY INVERSION
# ─────────────────────────────────────────────────────────────────────────────
_t('dependency-inversion', [
    {
        'title': 'Dependency Inversion: Depend on Abstractions',
        'desc': 'Why high-level policy should never depend on low-level details, and how interfaces flip the arrow.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'State the dependency inversion principle',
            'Explain how interfaces invert dependency direction',
            'Refactor a concrete-coupling example',
            'Distinguish inversion from dependency injection',
        ],
        'prereqs': ['principles/single-responsibility', 'principles/interface-segregation'],
        'sections': [
            {'heading': 'The Principle', 'paras': [
                'Dependency Inversion (DIP): high-level modules should not depend on low-level modules; both should depend on abstractions. Abstractions should not depend on details; details should depend on abstractions.',
                'When the notification service calls EmailSender directly, the high-level policy (what to send) is welded to the low-level detail (how to send). Introduce an interface, and the policy depends on the abstraction while both email and SMS implement it.',
            ], 'code': {'lang': 'java', 'body': '''
// Before: high-level depends on low-level concrete class
class NotificationService {
    private EmailSender sender = new EmailSender();  // welded to detail
    void send(String msg) { sender.sendEmail(msg); }
}

// After: both depend on the abstraction
interface MessageSender { void send(String msg); }

class NotificationService {
    private final MessageSender sender;   // depends on abstraction
    NotificationService(MessageSender s) { this.sender = s; }
    void send(String msg) { sender.send(msg); }
}
class EmailSender implements MessageSender { public void send(String m) {} }
class SmsSender   implements MessageSender { public void send(String m) {} }'''}},
            {'heading': 'Inversion vs Injection', 'paras': [
                'Inversion is about the direction of dependency arrows. Injection (DI) is the delivery mechanism — passing the dependency in via constructor. You can invert without a framework, and you can inject without inverting. The principle is the point; the framework is optional.',
            ]},
        ],
        'practice': {
            'title': 'Invert the Reporting Stack',
            'intro': 'A ReportGenerator builds CSV rows and calls CsvWriter directly. Now you must also support JSON and PDF.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the ReportWriter interface the generator should depend on.'},
                {'label': 'Task 2', 'text': 'Implement CsvWriter, JsonWriter, PdfWriter behind it.'},
                {'label': 'Task 3', 'text': 'Wire the choice at startup (constructor injection) and explain why the generator never changes again.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why depending on an interface is not the same as depending on a base class. Start with the direction of the arrow.'},
            {'label': 'Compare & Contrast', 'text': 'Compare DIP with dependency injection frameworks (Spring, Guice). What does the framework solve, and what can you do without one?'},
            {'label': 'Boundary Testing', 'text': 'An abstraction with only one implementation and no planned second one — is it over-engineering or correct DIP? Argue both sides.'},
        ],
        'takeaways': [
            'High-level policy must not depend on low-level details',
            'Interfaces flip the dependency arrow',
            'Injection is delivery; inversion is direction',
            'One-implementation abstractions can still be justified by testability',
        ],
        'further': [
            {'title': 'Dependency Inversion Principle — Clean Code Mentor', 'url': 'https://www.clean-code-mentor.com/dependency-inversion-principle'},
            {'title': 'SOLID — Robert C. Martin', 'url': 'https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html'},
        ],
    },
    {
        'title': 'Dependency Inversion in Production: Ports and Adapters',
        'desc': 'Hexagonal architecture, testability, and keeping the domain clean of infrastructure.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Structure a service with ports and adapters',
            'Keep the domain free of framework imports',
            'Use inversion for test doubles without mocks',
            'Manage the wiring layer (composition root)',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Ports and Adapters (Hexagonal)', 'paras': [
                'Hexagonal architecture draws the application core as a hexagon: inbound ports (driven by UI/API) and outbound ports (driving database/queue/email). Adapters implement the ports at the edges. The domain core knows nothing about HTTP, SQL, or Kafka.',
            ], 'code': {'lang': 'text', 'body': '''
Hexagonal (ports & adapters):
  [HTTP adapter] -> [inbound port] -> [DOMAIN CORE] -> [outbound port] -> [Postgres adapter]
                                   -> [outbound port] -> [Kafka adapter]
The domain core imports only ports + domain types.
Test: swap adapters for in-memory fakes with zero domain changes.'''}},
            {'heading': 'Composition Root', 'paras': [
                'The composition root is the single place where concrete adapters are chosen and wired. It lives at the application edge (main, startup config), never inside the domain. This concentrates the "what implementation today" decision in one file.',
                'Inversion makes the domain testable with lightweight fakes: a fake repository implements the same port the real one does, so tests exercise the domain with no mocks, no databases, and no network.',
            ]},
        ],
        'practice': {
            'title': 'Hexagonalize a Service',
            'intro': 'A checkout service calls an HTTP payments API and writes to Postgres directly from the order logic.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the outbound ports: PaymentProvider, OrderStore.'},
                {'label': 'Task 2', 'text': 'Move HTTP and SQL calls into adapters; keep the order logic framework-free.'},
                {'label': 'Task 3', 'text': 'Write a domain test using in-memory fakes for both ports. Note what it proves that a mock-based test cannot.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why the composition root must be outside the domain and what breaks if it is not.'},
            {'label': 'Implementation Design', 'text': 'Design the ports for a notification system with email, push, and SMS providers, including retry and dead-letter semantics. Where does retry live — port or adapter?'},
            {'label': 'Boundary Testing', 'text': 'A new persistence requirement (e.g., sharding) changes the data model. How does hexagonal structure contain the blast radius?'},
        ],
        'takeaways': [
            'Ports and adapters keep infrastructure at the edges',
            'The domain core imports only ports and types',
            'The composition root concentrates wiring decisions',
            'Fakes beat mocks for testing the domain',
        ],
        'further': [
            {'title': 'Hexagonal Architecture — Alistair Cockburn', 'url': 'https://alistair.cockburn.us/hexagonal-architecture/'},
            {'title': 'Ports & Adapters — Martin Fowler', 'url': 'https://martinfowler.com/articles/hexagonal-architecture-demo.html'},
        ],
    },
    {
        'title': 'Advanced Dependency Inversion: Modules and Compile-Time Arrows',
        'desc': 'Module boundaries, preventing dependency cycles, and architecture tests that enforce the arrows.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Structure modules so arrows point inward',
            'Prevent dependency cycles with ownership rules',
            'Enforce architecture with dependency tests',
            'Apply DIP to cross-module interfaces',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Module-Level Arrows', 'paras': [
                'The same inversion applies between modules: the domain module should not depend on the infrastructure module. Put interfaces in the module that owns the policy, and let the implementation module depend on it.',
                'When module A needs data from module B, define the interface in A and implement it in B — so A stays independent and B imports A. This is how the dependency arrow flips at the module scale.',
            ], 'code': {'lang': 'text', 'body': '''
Module arrows point inward:
  domain/   (no imports of infra)  <- owns ports
  infra/    (imports domain)       <- implements ports
  app/      (imports domain + infra) <- composition root

Architecture test (pseudo):
  assert_no_import(module='domain', forbidden={'infra', 'web', 'sql'})'''}},
            {'heading': 'Enforcing with Architecture Tests', 'paras': [
                'Conventions decay without enforcement. Architecture tests (e.g., ArchUnit for Java, dependency-cruiser for JS) assert the import rules in CI: the domain module may not import infrastructure packages, and dependency cycles fail the build.',
                'These tests are cheap to write, run in seconds, and turn "keep the arrows right" from a review comment into a hard guarantee.',
            ]},
        ],
        'practice': {
            'title': 'Map and Enforce Module Dependencies',
            'intro': 'Your monorepo has 6 modules; the domain module already imports a logging library and a JSON library from the infra layer.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the allowed dependency matrix for the 6 modules.'},
                {'label': 'Task 2', 'text': 'Write the architecture test that forbids domain importing infra.'},
                {'label': 'Task 3', 'text': 'Find the existing violations and refactor two of them using interfaces.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me how to decide which module owns an interface when two modules need each other. Ask me to reason through a cycle example.'},
            {'label': 'Implementation Design', 'text': 'Design a plugin architecture where third-party plugins implement domain-defined ports. How do you load, validate, and isolate plugins?'},
            {'label': 'Boundary Testing', 'text': 'A shared util module becomes a dumping ground everyone imports. Design the dependency rule and the migration.'},
        ],
        'takeaways': [
            'Module arrows should point inward toward the domain',
            'Own the interface in the module that defines the policy',
            'Architecture tests enforce arrows in CI',
            'Plugin systems are DIP applied at the deployment level',
        ],
        'further': [
            {'title': 'ArchUnit (Java architecture tests)', 'url': 'https://www.archunit.org/'},
            {'title': 'dependency-cruiser (JS)', 'url': 'https://github.com/sverweij/dependency-cruiser'},
        ],
    },
    {
        'title': 'Dependency Inversion: Review & Mastery Quiz',
        'desc': 'Scenario questions on abstraction direction, ports, and module boundaries.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate DIP concepts',
            'Design inversion boundaries',
            'Enforce arrows with tests',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: DIP says high-level modules should depend on? (A: low-level modules / B: abstractions / C: nothing)',
                'Q2: The composition root is where you? (A: write domain logic / B: wire concrete adapters / C: define interfaces)',
                'Q3: Hexagonal architecture keeps the domain free of? (A: interfaces / B: infrastructure imports / C: tests)',
                'Q4: True or false: dependency injection frameworks are required for dependency inversion.',
                'Q5: Architecture tests are used to? (A: test UI / B: enforce import rules / C: measure performance)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A team adds a second database to a service that was written without ports. Map the refactor: which interfaces, which adapters, and what stays untouched?'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "we only ever use Postgres, so no interface needed" fails when the requirement changes.'},
        ],
        'takeaways': [
            'Q1: B; Q2: B; Q3: B; Q4: false; Q5: B',
            'Inversion is about arrows, not frameworks',
            'Enforcement in CI keeps the architecture honest',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# DRY (DON'T REPEAT YOURSELF)
# ─────────────────────────────────────────────────────────────────────────────
_t('dry', [
    {
        'title': 'DRY: Every Piece of Knowledge, Once',
        'desc': 'The difference between duplicating code and duplicating knowledge — and why the second one hurts.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Define DRY as knowledge duplication, not code duplication',
            'Identify duplicated knowledge (rules, logic, formats)',
            'Distinguish DRY from premature abstraction',
            'Refactor a repeated rule into one source of truth',
        ],
        'prereqs': ['principles/kiss', 'principles/single-responsibility'],
        'sections': [
            {'heading': 'Code vs Knowledge', 'paras': [
                'DRY is not "never copy-paste". It is: every piece of knowledge must have a single, unambiguous, authoritative representation. The same validation rule written in four places is four copies of knowledge — fixing it means fixing four files, and one will be forgotten.',
                'Two blocks that merely look similar but encode different rules are not duplicates. Forcing them together creates a coupling that is worse than the repetition.',
            ], 'code': {'lang': 'python', 'body': '''
# Duplicated knowledge: the discount rule exists twice
def cart_total(items):
    return sum(i.price * (0.9 if i.kind == 'bulk' else 1.0) for i in items)

def cart_total_for_report(items):
    # copy of the same rule, already diverging (0.85 here!)
    return sum(i.price * (0.85 if i.kind == 'bulk' else 1.0) for i in items)

# DRY: one authoritative rule
def bulk_discount(kind): return 0.9 if kind == 'bulk' else 1.0
def cart_total(items):   return sum(i.price * bulk_discount(i.kind) for i in items)
def report_total(items): return cart_total(items)  # reuses the rule'''}},
            {'heading': 'When to Extract', 'paras': [
                'Extract when a rule has multiple call sites and one source of truth matters (business rules, formats, identifiers). Do not extract two random similar snippets — that creates the "Shotgun Surgery" anti-pattern in reverse: change the abstraction, update everything.',
                'The classic heuristic: wait for the third occurrence before generalizing; the first two reveal whether the shapes actually converge.',
            ]},
        ],
        'practice': {
            'title': 'Find the Duplicated Rule',
            'intro': 'In your codebase, an email-address validation regex appears in signup, invite, and billing.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Locate every occurrence and check whether they have already drifted apart.'},
                {'label': 'Task 2', 'text': 'Extract a single validateEmail() used everywhere, with tests.'},
                {'label': 'Task 3', 'text': 'Find one "similar but different" pair and explain why merging them would be wrong.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about the difference between duplicated code and duplicated knowledge. Start with two same-shaped functions with different rules.'},
            {'label': 'Compare & Contrast', 'text': 'Compare DRY with the "rule of three" and with premature abstraction. Where does each guide you differently?'},
            {'label': 'Boundary Testing', 'text': 'A shared function is now used by 12 call sites, but two of them need slightly different behavior. Design the escape hatch that does not fork the knowledge.'},
        ],
        'takeaways': [
            'DRY targets knowledge, not code',
            'Duplicated rules drift apart silently',
            'Similar shapes with different rules are not duplicates',
            'Rule of three: extract when shapes prove they converge',
        ],
        'further': [
            {'title': 'The Pragmatic Programmer (DRY chapter)', 'url': 'https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/'},
            {'title': 'DRY vs WET — Martin Fowler', 'url': 'https://martinfowler.com/bliki/DryPrinciple.html'},
        ],
    },
    {
        'title': 'DRY in Production: Single Sources of Truth',
        'desc': 'Config, schemas, and documentation as single sources of truth across services.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Apply DRY to configuration and schemas',
            'Use generated clients to avoid duplicated contracts',
            'Keep documentation close to the code it describes',
            'Avoid over-abstraction that couples unrelated things',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Contracts and Generated Clients', 'paras': [
                'An API contract written once (OpenAPI, protobuf, GraphQL schema) and generating clients for every language is DRY at the service boundary: the wire format has one authoritative definition, and consumers cannot drift.',
            ], 'code': {'lang': 'text', 'body': '''
Single sources of truth in a platform:
  OpenAPI spec       -> generated clients (TS, Go, Java)
  protobuf .proto    -> typed messages + RPC stubs
  DB schema / migrations -> the only place the schema lives
  Feature flags      -> one registry, many consumers
Never: hand-written clients that mirror the spec.'''}},
            {'heading': 'Config and Docs', 'paras': [
                'Config duplicated across environments (dev/staging/prod values copy-pasted) drifts and causes "works on my machine" bugs. Keep one schema for config, with per-environment values in a single store.',
                'Documentation that repeats the code (e.g., a README that restates function behavior) becomes wrong the moment the code changes. Keep docs at the level of why and how-to-use, generated from code where possible.',
            ]},
        ],
        'practice': {
            'title': 'Eliminate Contract Drift',
            'intro': 'Your frontend hand-writes API client types, and the backend hand-writes the OpenAPI spec. Field renames break builds only at runtime.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Make the OpenAPI spec the single source and generate the TS client from it.'},
                {'label': 'Task 2', 'text': 'Add a CI check that fails when the spec and the backend routes diverge.'},
                {'label': 'Task 3', 'text': 'Document the workflow: how does a developer change a field end-to-end?'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why generated clients are DRY but generated code checked into repos can still drift. Ask me about regeneration workflows.'},
            {'label': 'Implementation Design', 'text': 'Design a feature-flag pipeline where the flag schema, defaults, and rollout docs are one artifact. What generates what?'},
            {'label': 'Boundary Testing', 'text': 'Two services legitimately need different shapes of the same data. Is that a DRY violation? Design the boundary between shared and owned models.'},
        ],
        'takeaways': [
            'Contracts should have one authoritative definition',
            'Generated clients prevent consumer drift',
            'Config and docs drift the same way code does',
            'Owning different shapes of shared data is legitimate',
        ],
        'further': [
            {'title': 'OpenAPI Specification', 'url': 'https://swagger.io/specification/'},
            {'title': 'Protobuf Language Guide', 'url': 'https://protobuf.dev/programming-guides/proto3/'},
        ],
    },
    {
        'title': 'Advanced DRY: Abstraction Boundaries',
        'desc': 'The failure modes of over-abstraction and how to keep shared code honest.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Recognize the "god module" failure mode',
            'Version shared abstractions safely',
            'Use dependency injection to vary behavior without forks',
            'Measure coupling to guide extraction',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'The God Module', 'paras': [
                'When too much shared code accumulates in one utils module, every change ripples through dozens of consumers. The abstraction became a coupling point: DRY bought maintenance at the price of independence.',
                'The fix is not abandoning DRY but right-sizing the boundary: group shared code by domain (shared/billing/, shared/identity/) so changes are scoped to consumers that share the domain.',
            ], 'code': {'lang': 'text', 'body': '''
Anti-pattern: src/shared/utils.ts with 40 exports used everywhere.
Better: domain-scoped sharing
  shared/billing/  (used only by billing consumers)
  shared/identity/ (used only by identity consumers)
  shared/http/     (the few things truly global)
Coupling metric to watch: fan-in per shared module.'''}},
            {'heading': 'Versioning and Variation', 'paras': [
                'Shared abstractions that must evolve use semantic versioning: consumers pin major versions, and a new major can change the abstraction without breaking everyone at once. Alternatively, strategy injection lets consumers vary behavior through an interface instead of forking the shared code.',
            ]},
        ],
        'practice': {
            'title': 'Right-Size a Shared Module',
            'intro': 'shared/utils.ts has 40 exports, 200 importers, and every change takes a week to roll out.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Measure fan-in per export; group exports by the domains that use them.'},
                {'label': 'Task 2', 'text': 'Split the module into domain-scoped packages with versioned releases.'},
                {'label': 'Task 3', 'text': 'Identify two exports that should be strategies (injected) instead of shared implementations.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can articulate when DRY and modularity conflict, and how domain-scoped sharing resolves it.'},
            {'label': 'Implementation Design', 'text': 'Design a shared currency-conversion library used by billing, payroll, and reporting. How do you version rate-source changes without breaking all three?'},
            {'label': 'Boundary Testing', 'text': 'Two consumers need subtly different semantics from a shared function. Design the option surface that covers both without a fork.'},
        ],
        'takeaways': [
            'Over-abstraction becomes a coupling point',
            'Share by domain, not by dump',
            'Version shared abstractions; pin majors',
            'Strategy injection beats forking shared code',
        ],
        'further': [
            {'title': 'The Wrong Abstraction — Sandi Metz', 'url': 'https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction'},
            {'title': 'Rule of Three — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Rule_of_three_(computer_programming)'},
        ],
    },
    {
        'title': 'DRY: Review & Mastery Quiz',
        'desc': 'Scenario questions on knowledge duplication and abstraction boundaries.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate DRY concepts',
            'Identify knowledge vs code duplication',
            'Right-size abstraction boundaries',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: DRY prohibits duplicating? (A: code / B: knowledge / C: comments)',
                'Q2: Two same-shaped functions with different rules are? (A: duplicates / B: not duplicates / C: always DRY)',
                'Q3: The "rule of three" suggests extracting after? (A: 1 use / B: 3 similar uses / C: 10 uses)',
                'Q4: True or false: generated clients eliminate contract drift.',
                'Q5: A shared utils module used by everyone is a symptom of? (A: good DRY / B: over-abstraction / C: strong typing)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A tax rule exists in the backend, a reporting job, and a frontend form. Redesign with one source of truth and describe the deployment order.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "we DRYed it too early" is a real cost, with a concrete refactor story.'},
        ],
        'takeaways': [
            'Q1: B; Q2: B; Q3: B; Q4: true; Q5: B',
            'Knowledge with one source of truth never drifts',
            'Abstractions earn their keep by reducing coupling, not lines',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# EVENTUAL CONSISTENCY
# ─────────────────────────────────────────────────────────────────────────────
_t('eventual-consistency', [
    {
        'title': 'Eventual Consistency: Converging Without Coordination',
        'desc': 'Why replicas are allowed to disagree briefly, and how they converge.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Define eventual consistency precisely',
            'Explain why it enables availability and low latency',
            'List convergence mechanisms: propagation, retries, CRDTs',
            'Describe user-visible staleness windows',
        ],
        'prereqs': ['principles/base', 'principles/consistency-pattern'],
        'sections': [
            {'heading': 'The Definition', 'paras': [
                'Eventual consistency: if no new writes occur to a replicated item, all replicas will eventually converge to the same value. The window of divergence is unbounded in theory but bounded in practice by propagation time and retry behavior.',
                'The guarantee is weak on purpose: it lets replicas serve reads and accept writes independently, which is what keeps the system available during partitions and fast in normal operation.',
            ], 'code': {'lang': 'text', 'body': '''
Eventual consistency timeline:
  t0: client writes v2 to replica A
  t1: replica B still serves v1 (stale read)
  t2: propagation delivers v2 to B
  t3: B serves v2 (converged)
Convergence is guaranteed only after writes stop.'''}},
            {'heading': 'Where It Is Safe', 'paras': [
                'Eventual consistency fits data where transient divergence is invisible or acceptable: like counts, presence, feeds, recommendations, session caches. It is dangerous for balances, inventory, and uniqueness constraints.',
            ]},
        ],
        'practice': {
            'title': 'Map the Staleness Window',
            'intro': 'A social app replicates posts across 3 regions with async propagation (~200ms).',
            'tasks': [
                {'label': 'Task 1', 'text': 'Describe the worst-case staleness for a reader in region C when a post is written in region A.'},
                {'label': 'Task 2', 'text': 'Identify which features break visibly (read-your-writes for the author) and design the session affinity fix.'},
                {'label': 'Task 3', 'text': 'List three data types that must NOT be eventually consistent here.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why "eventual" has no time bound and how systems bound it in practice. Start with propagation.'},
            {'label': 'Compare & Contrast', 'text': 'Compare eventual consistency with causal consistency and read-your-writes. Which user bugs does each one eliminate?'},
            {'label': 'Boundary Testing', 'text': 'A like counter converges eventually, but a viral post gets 10k likes/min. Describe the convergence lag and whether users notice.'},
        ],
        'takeaways': [
            'Eventual means converges when writes stop',
            'It buys availability and low write latency',
            'Staleness is bounded by propagation, not by promise',
            'Match data types to the guarantee they can tolerate',
        ],
        'further': [
            {'title': 'Eventually Consistent — Werner Vogels', 'url': 'https://www.allthingsdistributed.com/2008/12/eventually_consistent.html'},
            {'title': 'Cassandra Consistency Levels', 'url': 'https://docs.datastax.com/en/cassandra-oss/3.x/cassandra/dml/dmlConfigConsistency.html'},
        ],
    },
    {
        'title': 'Eventual Consistency in Production: Replication and Read Models',
        'desc': 'Async replication, read replicas, search indexes, and the pipelines that keep them fresh.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design async replication pipelines',
            'Use outbox patterns for reliable propagation',
            'Build read models and search indexes from events',
            'Monitor replication lag as a first-class metric',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'The Outbox Pattern', 'paras': [
                'Reliable propagation is the hard part: if you publish the event before committing the write, you may publish events for writes that roll back; if after, you may lose events on crash. The transactional outbox stores the event in the same transaction as the write, and a relay publishes it — exactly once.',
            ], 'code': {'lang': 'sql', 'body': '''
-- Transactional outbox: event written with the business data
BEGIN;
INSERT INTO orders (...) VALUES (...);
INSERT INTO outbox (id, aggregate, payload, published)
VALUES (gen_random_uuid(), 'order.created', '{"orderId": 123}', false);
COMMIT;
-- Relay (idempotent):
UPDATE outbox SET published = true
WHERE id = $1 AND published = false;   -- exactly-once guard'''}},
            {'heading': 'Read Models and Search Indexes', 'paras': [
                'Search indexes and analytics warehouses are naturally eventual: they consume events and project them into optimized shapes. The key discipline is that reads served from them are understood to be slightly behind the source of truth, and the product communicates or tolerates that.',
                'Monitor replication lag and index lag with dashboards and alerts — eventual consistency without visibility is how stale data becomes a silent production bug.',
            ]},
        ],
        'practice': {
            'title': 'Build a Reliable Sync Pipeline',
            'intro': 'Orders must appear in a search index within ~5 seconds. The current pipeline publishes events after commit and loses them on crash.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Adopt the outbox pattern and describe the crash scenarios it fixes.'},
                {'label': 'Task 2', 'text': 'Design the indexer: consume, dedupe, retry, and handle out-of-order events.'},
                {'label': 'Task 3', 'text': 'Define the lag alert (e.g., >30s index lag pages) and the replay workflow.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why the outbox must be in the same transaction as the business write. Ask me to trace the two failure orders.'},
            {'label': 'Implementation Design', 'text': 'Design a search index that must never show deleted orders. How do tombstones propagate through the pipeline?'},
            {'label': 'Boundary Testing', 'text': 'The relay publishes a duplicate event after a retry. Design idempotent consumption (dedupe key) end-to-end.'},
        ],
        'takeaways': [
            'Outbox pattern gives reliable, at-least-once propagation',
            'Consumers must be idempotent to survive retries',
            'Search/analytics are naturally eventual read models',
            'Lag is a first-class metric with alerts and replays',
        ],
        'further': [
            {'title': 'Transactional Outbox — Microservices.io', 'url': 'https://microservices.io/patterns/data/transactional-outbox.html'},
            {'title': 'Change Data Capture (Debezium)', 'url': 'https://debezium.io/'},
        ],
    },
    {
        'title': 'Advanced Eventual Consistency: Divergence and Reconciliation',
        'desc': 'Handling true conflicts, last-writer-wins hazards, and converging under partitions.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Detect and classify divergent states',
            'Design reconciliation for divergent writes',
            'Apply CRDTs where conflict resolution must be automatic',
            'Avoid LWW data loss with hybrid clocks',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Convergence vs Reconciliation', 'paras': [
                'CRDTs converge automatically: any merge order gives the same result. Non-CRDT replicas need reconciliation: detect the divergence, apply a policy (LWW, merge, conflict UI), and converge. The distinction decides whether users ever see a conflict.',
            ], 'code': {'lang': 'python', 'body': '''
# LWW with hybrid logical clock: causal-ish timestamps
import time
class HLC:
    def __init__(self):
        self.pt = 0            # physical
        self.l = 0             # logical

    def now(self):
        now = time.time_ns() // 1_000_000
        self.pt = max(self.pt, now)
        if now <= self.pt:     # same ms -> logical tick
            self.l += 1
        else:
            self.l = 0
        return self.pt, self.l

def lww_merge(a, b):  # (clock, value) pairs
    return a if a[0] >= b[0] else b   # concurrent ties -> arbitrary'''}},
            {'heading': 'When LWW Loses Data', 'paras': [
                'Last-writer-wins overwrites the whole value, so concurrent edits to different fields destroy one side\'s work. Field-level LWW (merge per field) and CRDTs (merge per element) recover most of the loss. The rule: the more concurrent editing, the finer the merge granularity must be.',
            ]},
        ],
        'practice': {
            'title': 'Choose a Convergence Strategy',
            'intro': 'A notes app: two devices edit the same note offline; both sync later.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Classify the edits: different fields (mergeable), same field (conflict), delete vs edit (tombstone needed).'},
                {'label': 'Task 2', 'text': 'Design field-level merge with an HLC and tombstones for deletes.'},
                {'label': 'Task 3', 'text': 'Decide where CRDTs are worth it vs a "conflict found — keep both" UI.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why wall-clock LWW is unsafe across nodes without synchronized clocks, and what HLC adds.'},
            {'label': 'Implementation Design', 'text': 'Design a distributed todo list where a completed item on one device and edited item on another must both survive the merge.'},
            {'label': 'Boundary Testing', 'text': 'A delete on replica A races an edit on replica B. Without tombstones the item resurrects. Design the tombstone lifecycle and its cleanup.'},
        ],
        'takeaways': [
            'CRDTs converge; non-CRDTs need reconciliation',
            'LWW at value granularity loses concurrent work',
            'Field-level and element-level merges preserve more',
            'Tombstones prevent resurrection; HLCs prevent clock lies',
        ],
        'further': [
            {'title': 'Conflict-Free Replicated Data Types', 'url': 'https://hal.inria.fr/inria-00555588/document'},
            {'title': 'Hybrid Logical Clocks', 'url': 'https://cse.buffalo.edu/tech-reports/2014-04.pdf'},
        ],
    },
    {
        'title': 'Eventual Consistency: Review & Mastery Quiz',
        'desc': 'Scenario questions on convergence, outboxes, and conflict resolution.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate eventual consistency concepts',
            'Design reliable propagation',
            'Choose conflict strategies',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Eventual consistency guarantees convergence? (A: immediately / B: after writes stop / C: never)',
                'Q2: The transactional outbox pattern guarantees? (A: exactly-once delivery / B: at-least-once with idempotent consumers / C: zero latency)',
                'Q3: A delete racing an edit needs? (A: tombstone / B: a bigger TTL / C: a lock)',
                'Q4: True or false: replication lag should be monitored like any other metric.',
                'Q5: LWW at value granularity can lose? (A: nothing / B: concurrent field edits / C: the whole database)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A multi-region cart must never lose items but tolerates slight lag. Design the read-your-writes route, the outbox, and the conflict policy.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "eventually consistent" needs bounds, alerts, and replay — not faith.'},
        ],
        'takeaways': [
            'Q1: B; Q2: B; Q3: A; Q4: true; Q5: B',
            'Convergence needs mechanisms, not promises',
            'Idempotency and tombstones make propagation safe',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# FAIL FAST
# ─────────────────────────────────────────────────────────────────────────────
_t('fail-fast', [
    {
        'title': 'Fail Fast: Surface Errors Immediately',
        'desc': 'Why discovering a problem at the exact moment it happens beats discovering it an hour later.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Define fail-fast and fail-loud',
            'Validate inputs at the boundary',
            'Use assertions for programmer assumptions',
            'Explain the cost of deferred failures',
        ],
        'prereqs': ['principles/defensive-programming', 'principles/kiss'],
        'sections': [
            {'heading': 'The Principle', 'paras': [
                'Fail fast means invalid states, bad inputs, and violated assumptions are detected at the earliest possible moment and surfaced loudly — not swallowed, logged, or deferred. A failure found now costs seconds; the same failure found in production costs an incident.',
                'The opposite is fail-late-and-silently: an invalid order ID stored as 0, a null name defaulted to "unknown", a retry loop that hides a permanent error. Each one delays the signal until the damage compounds.',
            ], 'code': {'lang': 'python', 'body': '''
# Fail fast: reject invalid input at the boundary
def create_order(user_id, items):
    if not user_id:                raise ValueError('user_id required')
    if not items:                  raise ValueError('order needs items')
    if any(i.qty <= 0 for i in items): raise ValueError('qty must be positive')
    return order_store.create(user_id, items)

# Anti-pattern: sanitize silently
def create_order(user_id, items):
    user_id = user_id or 'unknown'        # hides the bug
    items = [i for i in items if i.qty > 0]  # drops data silently
    return order_store.create(user_id, items)'''}},
            {'heading': 'Fail Fast vs Defensive', 'paras': [
                'Fail-fast and defensive programming overlap but differ in emphasis: defensive programming assumes inputs are hostile and guards broadly; fail-fast emphasizes the speed and loudness of the signal. Both agree that silent acceptance is the enemy.',
            ]},
        ],
        'practice': {
            'title': 'Audit a Silent-Failure Path',
            'intro': 'A report generator catches all exceptions, logs "error", and returns an empty report.',
            'tasks': [
                {'label': 'Task 1', 'text': 'List every place a failure is silently swallowed and what it hides.'},
                {'label': 'Task 2', 'text': 'Redesign: which failures should propagate, which should surface to the user, and which legitimately degrade?'},
                {'label': 'Task 3', 'text': 'Add monitoring that alerts on each loud failure with context.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why deferred failure is more expensive than immediate failure. Start with the debugging distance.'},
            {'label': 'Compare & Contrast', 'text': 'Contrast fail-fast with graceful degradation. When is degradation the right choice, and how do you keep it from becoming silent failure?'},
            {'label': 'Boundary Testing', 'text': 'A fail-fast assertion in a hot library crashes a production service over a benign input. Where is the right boundary between fail-fast and validate-with-fallback?'},
        ],
        'takeaways': [
            'Surface failures at the earliest, loudest moment',
            'Silent sanitization hides the bug and delays the signal',
            'Fail-fast and graceful degradation must be explicitly distinguished',
            'Alerting makes loud failures actually visible',
        ],
        'further': [
            {'title': 'Fail Fast — Martin Fowler', 'url': 'https://martinfowler.com/ieeeSoftware/failFast.pdf'},
            {'title': 'Fail Fast Principle — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Fail-fast'},
        ],
    },
    {
        'title': 'Fail Fast in Production: Validation and Startup Checks',
        'desc': 'Startup validation, config checks, and failing the deploy instead of the runtime.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Validate config and dependencies at startup',
            'Design CI checks that fail fast',
            'Use canary deploys to fail fast in production',
            'Distinguish fast failure from flapping',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Startup Validation', 'paras': [
                'A service should refuse to start rather than run in a broken state: config schema validated, required secrets present, database reachable, feature flags defined. Start-failure is loud, recoverable, and trivially visible in the deploy pipeline.',
            ], 'code': {'lang': 'go', 'body': '''
// Refuse to start on invalid config — fail fast at deploy time
type Config struct {
    DBURL      string `json:"db_url" validate:"required"`
    MaxRetries int    `json:"max_retries" validate:"gte=0,lte=5"`
}

func main() {
    cfg := loadConfig()
    if err := validate.Struct(cfg); err != nil {
        log.Fatalf("invalid config: %v", err)   // do not start broken
    }
    run(cfg)
}'''}},
            {'heading': 'Failing the Pipeline', 'paras': [
                'CI is the fastest place to fail: lint, typecheck, unit tests, contract tests, and a smoke deploy all fail in minutes, before users are involved. Production fail-fast is the canary: release to 1% of traffic, watch error rates for minutes, and roll back automatically on spikes.',
                'The trap is flapping — failing on transient blips and rolling back healthy releases. Fail-fast at the pipeline level uses thresholds, minimum sample sizes, and grace periods.',
            ]},
        ],
        'practice': {
            'title': 'Harden the Deploy Pipeline',
            'intro': 'A misconfigured flag ships to production and only breaks the checkout at 2am, three hours after deploy.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Add startup config validation so the deploy itself fails.'},
                {'label': 'Task 2', 'text': 'Design the canary: traffic %, error-rate threshold, rollback trigger, and grace period.'},
                {'label': 'Task 3', 'text': 'Add contract tests to CI that catch the drift before deploy.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why "the deploy must fail, not the service" is the goal of startup validation. Ask me to rank pipeline gates by speed.'},
            {'label': 'Implementation Design', 'text': 'Design a feature-flag rollout gate: flags validate at startup, canaries validate at 1%/10%/50%, and a broken flag rolls back automatically. What thresholds and windows?'},
            {'label': 'Boundary Testing', 'text': 'A startup check depends on a database that is legitimately down during a maintenance window. How do you fail fast without blocking maintenance?'},
        ],
        'takeaways': [
            'Fail at deploy time, not runtime',
            'CI gates and canaries are production fail-fast',
            'Avoid flapping with thresholds and grace periods',
            'Startup config validation catches the cheapest bugs',
        ],
        'further': [
            {'title': 'Twelve-Factor App — Fail Fast', 'url': 'https://12factor.net/'},
            {'title': 'Canary Deployment — Martin Fowler', 'url': 'https://martinfowler.com/bliki/CanaryRelease.html'},
        ],
    },
    {
        'title': 'Advanced Fail Fast: Timeouts, Deadlines, and Cancellation',
        'desc': 'Propagating failure through distributed calls with timeouts, deadlines, and context cancellation.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Design timeout hierarchies with bounded totals',
            'Use deadlines and context cancellation end-to-end',
            'Fail fast on budget exhaustion (load shedding)',
            'Distinguish fast-fail from silent-drop',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Deadlines That Propagate', 'paras': [
                'A single request may fan out to dozens of services. Per-call timeouts that are independent let the total budget balloon (10 calls × 500ms = 5s). Propagate a deadline: the context carries the remaining budget, and each hop checks and shrinks it.',
            ], 'code': {'lang': 'go', 'body': '''
// Deadline propagation: fail fast when the budget is spent
func HandleOrder(ctx context.Context, id string) error {
    ctx, cancel := context.WithTimeout(ctx, 2*time.Second)
    defer cancel()

    price, err := priceService.Price(ctx, id)   // inherits deadline
    if err != nil { return err }                // deadline exceeded -> fast
    inv, err := inventoryService.Check(ctx, id)
    if err != nil { return err }
    return nil
}'''}},
            {'heading': 'Budget Exhaustion Is a Fast Failure', 'paras': [
                'When the system is saturated, failing fast on new work (429/503 at the edge, queue caps, load shedding) is the correct fast failure — it protects the workers already in flight. The art is signaling it loudly (with a clear status) instead of silently dropping or queueing forever.',
            ]},
        ],
        'practice': {
            'title': 'Design the Deadline Tree',
            'intro': 'A checkout spans gateway → auth, price, inventory, payments (4 parallel calls) and has a 3s total budget.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Allocate sub-budgets so the total never exceeds 3s, including retries.'},
                {'label': 'Task 2', 'text': 'Design the cancellation flow: one slow service must not delay the others.'},
                {'label': 'Task 3', 'text': 'Define the fast-fail response when the budget is exhausted and how it differs from a silent drop.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why per-call timeouts without a shared deadline fail to bound end-to-end latency.'},
            {'label': 'Implementation Design', 'text': 'Design a retry policy that respects the deadline: how many retries fit inside the remaining budget, and when is failing fast better than retrying?'},
            {'label': 'Boundary Testing', 'text': 'A dependency returns a 503 that means "try later" versus "permanently down". Design the fast-fail distinction without two round trips.'},
        ],
        'takeaways': [
            'Propagate deadlines, not independent timeouts',
            'Budget exhaustion should fail fast and loudly',
            'Cancellation must propagate to stop wasted work',
            'Retries must fit inside the remaining budget',
        ],
        'further': [
            {'title': 'Google SRE — Handling Overload', 'url': 'https://sre.google/sre-book/handling-overload/'},
            {'title': 'gRPC Deadlines', 'url': 'https://grpc.io/docs/guides/deadlines/'},
        ],
    },
    {
        'title': 'Fail Fast: Review & Mastery Quiz',
        'desc': 'Scenario questions on loud failure, pipeline gates, and deadlines.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate fail-fast concepts',
            'Design pipeline and runtime gates',
            'Propagate deadlines correctly',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Fail fast means failures are? (A: hidden / B: surfaced early and loudly / C: retried forever)',
                'Q2: The best place to catch a config bug is? (A: production at 2am / B: startup validation / C: user reports)',
                'Q3: A propagated deadline ensures? (A: total latency stays bounded / B: no failures / C: infinite retries)',
                'Q4: True or false: silent sanitization of invalid input is a form of fail-fast.',
                'Q5: When saturated, new work should? (A: queue forever / B: fail fast with a clear status / C: drop silently)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A misconfigured service deploys and breaks 3% of checkouts. Design the canary, alert, and rollback that catch it in minutes.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why the debugging distance between a bug and its symptom is the real cost of failing late.'},
        ],
        'takeaways': [
            'Q1: B; Q2: B; Q3: A; Q4: false; Q5: B',
            'Fail at the earliest, loudest, cheapest point',
            'Deadlines and cancellation bound the blast radius',
        ],
    },
])
