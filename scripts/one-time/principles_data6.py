#!/usr/bin/env python3
"""Deep curriculum data chunk 6: kiss, leader-election, liskov-substitution, load-shedding."""

TOPICS = {}


def _t(slug, topics):
    TOPICS[slug] = topics
    return topics


# ─────────────────────────────────────────────────────────────────────────────
# KISS
# ─────────────────────────────────────────────────────────────────────────────
_t('kiss', [
    {
        'title': 'KISS: Keep It Simple, Stupid',
        'desc': 'Why simplicity is a feature and complexity is a tax you pay forever.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Define the KISS principle',
            'Recognize complexity that buys nothing',
            'Simplify a convoluted solution',
            'Explain the maintenance cost of complexity',
        ],
        'prereqs': ['principles/yagni', 'principles/dry'],
        'sections': [
            {'heading': 'The Principle', 'paras': [
                'KISS says the simplest solution that meets the requirement is the best one. Simplicity means fewer moving parts, fewer branches, fewer abstractions, fewer failure modes. Every line of complexity is code that can break, must be tested, and will be read by someone else.',
                'Complexity is a tax: it is paid at review time, test time, debugging time, onboarding time, and refactor time. The simplest design minimizes the total tax, not just today\'s code.',
            ], 'code': {'lang': 'python', 'body': '''
# Convoluted: over-abstracted for a single use
class DiscountEngine:
    def __init__(self, strategy, config_loader, cache):
        ...
    def apply(self, order):
        return self.strategy(order, self.config_loader.load(), self.cache.get())

# Simple: a function
def total_with_discount(order):
    return order.total - (order.total * 0.1 if order.coupon else 0)'''}},
            {'heading': 'Simple vs Simplistic', 'paras': [
                'Simple is not the same as simplistic. KISS does not mean ignoring requirements — it means meeting them with the least machinery. A simple solution handles the real requirements directly; a simplistic one ignores them and fails in production.',
            ]},
        ],
        'practice': {
            'title': 'Simplify a Feature',
            'intro': 'A search filter feature was built with a rule engine, plugin registry, and caching layer — for three filter types.',
            'tasks': [
                {'label': 'Task 1', 'text': 'List the machinery and what each piece actually buys for three filter types.'},
                {'label': 'Task 2', 'text': 'Rewrite it with the minimal structure that still supports the three filters.'},
                {'label': 'Task 3', 'text': 'Decide at what point (how many filter types) the rule engine becomes justified.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about the difference between "simple for the author now" and "simple for every future reader". Start with an over-engineered example.'},
            {'label': 'Compare & Contrast', 'text': 'Compare KISS with YAGNI and DRY. When do they agree, and when does DRY tempt you into complexity KISS would avoid?'},
            {'label': 'Boundary Testing', 'text': 'A simple solution needs to grow. Design the decision rule for when to generalize and how to do it without a rewrite.'},
        ],
        'takeaways': [
            'Complexity is a recurring tax, not a one-time cost',
            'The simplest solution that meets requirements wins',
            'Simple is not simplistic — requirements still count',
            'Generalize only when the pattern has proven itself',
        ],
        'further': [
            {'title': 'KISS Principle — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/KISS_principle'},
            {'title': 'Simple Made Easy — Rich Hickey', 'url': 'https://www.infoq.com/presentations/Simple-Made-Easy/'},
        ],
    },
    {
        'title': 'KISS in Production: Architecture Simplicity',
        'desc': 'Simple architectures, fewer services, and resisting complexity pressure at scale.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Question new architectural machinery',
            'Design simple, evolvable service boundaries',
            'Resist complexity pressure from tools and fashion',
            'Measure complexity cost in operations',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Machinery Has a Cost', 'paras': [
                'Every system you add — event bus, orchestration framework, feature-flag service, observability platform — adds operational surface: deployments, upgrades, incidents, and knowledge requirements. Add machinery only when the problem outgrows the simple approach, with a concrete trigger.',
            ], 'code': {'lang': 'text', 'body': '''
Complexity pressure checklist before adding machinery:
  1. What breaks today without it? (concrete failure)
  2. What is the simplest thing that fixes that?
  3. What new failures does the machinery introduce?
  4. What is the un-add trigger (when to remove it)?
If the simple answer handles it, ship the simple answer.'''}},
            {'heading': 'Fewer Services, Better Boundaries', 'paras': [
                'A microservice is a complexity purchase: you buy isolation and scaling, and pay in distributed-debugging, consistency, and operations. Most teams are better served by a modular monolith with clean internal boundaries until a scaling or autonomy trigger justifies splitting.',
            ]},
        ],
        'practice': {
            'title': 'Challenge the Architecture',
            'intro': 'A team proposes splitting a 10k-line service into 8 microservices with an event bus.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Apply the checklist: what concrete failure does the split fix?'},
                {'label': 'Task 2', 'text': 'Propose the simpler alternative (modular monolith) and compare operational costs.'},
                {'label': 'Task 3', 'text': 'Define the trigger conditions that would justify the split later.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can articulate when microservices pay for their complexity and when they do not.'},
            {'label': 'Implementation Design', 'text': 'Design a modular monolith with clean domain boundaries that could later split into services. What must be true of the boundaries now?'},
            {'label': 'Boundary Testing', 'text': 'The team already runs 30 services and the tooling handles it. Does KISS still argue for fewer? What complexity remains?'},
        ],
        'takeaways': [
            'Machinery adds operational surface every time',
            'Simple architecture defers complexity until a concrete trigger',
            'Modular monoliths beat premature microservices',
            'Complexity costs appear in operations, not code review',
        ],
        'further': [
            {'title': 'Modular Monolith — Martin Fowler', 'url': 'https://martinfowler.com/bliki/ModularMonolith.html'},
            {'title': 'Microservices — Martin Fowler', 'url': 'https://martinfowler.com/articles/microservices.html'},
        ],
    },
    {
        'title': 'Advanced KISS: Simplicity as a Design Discipline',
        'desc': 'Domain-driven simplicity, minimal APIs, and the discipline of saying no.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Apply the "one way to do it" discipline',
            'Design minimal APIs and narrow contracts',
            'Manage simplicity pressure under growth',
            'Use simplicity reviews as a gate',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'One Way to Do It', 'paras': [
                'The simplest codebases have one idiomatic way to do each thing: one way to fetch, one way to validate, one way to handle errors. Multiple parallel mechanisms (two HTTP clients, three logging styles, both sync and async paths where one suffices) multiply cognitive load and bug surface.',
            ], 'code': {'lang': 'text', 'body': '''
Simplicity review questions per change:
  - Does this add a new mechanism? (or reuse an existing one)
  - Does this add a new concept? (or use a known one)
  - Could a reader explain this in 3 sentences?
  - What existing code becomes simpler because of this?
If a change simplifies nothing and complicates something, reject it.'''}},
            {'heading': 'Saying No', 'paras': [
                'Simplicity is defended by saying no: no to speculative parameters, no to premature abstractions, no to "while we are here" features. The discipline lives in review — a change that adds machinery without simplifying anything should go back.',
                'Growth pressure is real; the answer is not "never generalize" but "generalize when the second concrete case appears, not before".',
            ]},
        ],
        'practice': {
            'title': 'Run a Simplicity Review',
            'intro': 'A PR adds a caching framework, a config DSL, and an abstraction layer to support a feature that works without them.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Apply the review questions and list what the PR simplifies.'},
                {'label': 'Task 2', 'text': 'Rewrite the feature with the existing mechanisms only.'},
                {'label': 'Task 3', 'text': 'Write the review note that explains why the machinery was cut.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me how to say no to complexity without being obstructionist. Ask me to role-play the review conversation.'},
            {'label': 'Implementation Design', 'text': 'Design the minimal API for a feature that will grow: which knobs are justified now, which are speculative?'},
            {'label': 'Boundary Testing', 'text': 'The team wants "one way to do it" but a legitimate second way exists (sync and async paths). Design the rule for when a second way is allowed.'},
        ],
        'takeaways': [
            'One idiomatic way per concern keeps codebases navigable',
            'Simplicity reviews gate complexity at the PR level',
            'Saying no protects future readers',
            'Generalize on the second concrete case, not before',
        ],
        'further': [
            {'title': 'Minimalism in Software Design', 'url': 'https://www.infoq.com/presentations/simple-made-easy/'},
            {'title': 'The Art of Code — Yegor Bugayenko', 'url': 'https://www.yegor256.com/elegant-objects.html'},
        ],
    },
    {
        'title': 'KISS: Review & Mastery Quiz',
        'desc': 'Scenario questions on simplicity, machinery, and saying no.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate simplicity concepts',
            'Challenge complexity pressure',
            'Design minimal solutions',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: KISS prefers? (A: the cleverest solution / B: the simplest that meets requirements / C: the most configurable)',
                'Q2: Complexity is best understood as? (A: a feature / B: a recurring tax / C: a sign of skill)',
                'Q3: Simple is NOT? (A: meeting requirements / B: simplistic / C: clean)',
                'Q4: True or false: machinery should be added before the problem outgrows the simple approach.',
                'Q5: A change that adds machinery without simplifying anything should? (A: merge / B: go back / C: get more tests)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A 50-line function is proposed for a rule engine and event pipeline. Redesign the minimal version and list the complexity it avoids.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "impressive" architecture is a bug, not a feature.'},
        ],
        'takeaways': [
            'Q1: B; Q2: B; Q3: B; Q4: false; Q5: B',
            'Simplicity is a discipline defended in review',
            'The cheapest solution to operate is usually the best',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# LEADER ELECTION
# ─────────────────────────────────────────────────────────────────────────────
_t('leader-election', [
    {
        'title': 'Leader Election: One Coordinator at a Time',
        'desc': 'Why distributed systems need a single decision-maker and how they choose one safely.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain why a single leader is needed',
            'Describe the leader election problem',
            'Use leases to bound leader validity',
            'Recognize split-brain risks',
        ],
        'prereqs': ['principles/quorum', 'principles/cap-theorem'],
        'sections': [
            {'heading': 'The Problem', 'paras': [
                'Many coordination tasks need exactly one actor at a time: the node that processes a partition, the node that owns a lock, the node that assigns sequence numbers. Leader election is the mechanism that picks that node and ensures there is never more than one.',
                'The danger is split-brain: two nodes both believing they are leader, both writing — divergent state that may never reconcile. Safe election must guarantee that at most one leader is active at any time, even during partitions.',
            ], 'code': {'lang': 'text', 'body': '''
Leader election requirements:
  1. Safety: at most one leader at any time (no split-brain)
  2. Liveness: if a leader fails, a new one is elected
  3. Speed: failover within a bounded window

Mechanism options:
  - Consensus (Raft): majority-based, crash-safe
  - Lease on a lock (etcd/ZooKeeper): lease = time-bounded ownership
  - Bully algorithm: highest-ID node takes over'''}},
            {'heading': 'Leases', 'paras': [
                'A lease is leadership with a time bound: the leader holds it for T seconds and must renew. If the lease expires, another node may take over. The lease bounds how long a dead leader can keep "leading" — the core protection against split-brain.',
            ]},
        ],
        'practice': {
            'title': 'Design a Lease',
            'intro': 'Two nodes serve a queue partition; exactly one may process messages at a time.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the lease: how it is acquired, its duration, and its renewal loop.'},
                {'label': 'Task 2', 'text': 'Trace a failure: leader dies mid-lease. When can the other node take over? What is the failover window?'},
                {'label': 'Task 3', 'text': 'Explain what happens if the old leader wakes up after the lease expires but still thinks it is leader.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why a lease without a clock bound is unsafe. Start with the split-brain scenario.'},
            {'label': 'Compare & Contrast', 'text': 'Compare lease-based election (etcd) with Raft consensus. When is each the right tool?'},
            {'label': 'Boundary Testing', 'text': 'A slow leader renews its lease just after the standby took over. Design the fencing that prevents both from acting.'},
        ],
        'takeaways': [
            'Exactly one leader must be active at any time',
            'Leases bound leadership by time',
            'Split-brain is the failure mode election must prevent',
            'Fencing tokens guard against zombie leaders',
        ],
        'further': [
            {'title': 'Raft Paper', 'url': 'https://raft.github.io/raft.pdf'},
            {'title': 'etcd — Lease Documentation', 'url': 'https://etcd.io/docs/v3.5/learning/why/'},
        ],
    },
    {
        'title': 'Leader Election in Production: Consensus and Coordination',
        'desc': 'Raft, ZooKeeper, etcd, and building election on real coordination services.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Explain how Raft elects a leader',
            'Use etcd/ZooKeeper for leader election',
            'Handle leader handoff gracefully',
            'Design failover with bounded downtime',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Raft Election', 'paras': [
                'Raft nodes are followers, candidates, or leader. Followers elect a leader by majority vote with randomized timeouts; the leader replicates log entries to a majority before committing. If the leader dies, followers start a new election. Safety comes from requiring a majority — two leaders cannot both have majorities.',
            ], 'code': {'lang': 'text', 'body': '''
Raft election in brief:
  1. Followers expect heartbeats; timeout triggers candidacy
  2. Candidate requests votes; majority wins
  3. Leader sends heartbeats; commits after majority ack
  4. Leader crash -> new election within one timeout window
Split-brain is impossible: two leaders would each need a majority,
and majorities always intersect.'''}},
            {'heading': 'Election on etcd/ZooKeeper', 'paras': [
                'Practical systems build election on a coordination service: contenders create an ephemeral key; the one whose create succeeds is leader. Ephemeral nodes vanish when the owner dies, triggering immediate re-election. The coordination service provides the consensus and the failure detection.',
            ]},
        ],
        'practice': {
            'title': 'Build an Election Client',
            'intro': 'Three replicas of a scheduler need a leader.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the election flow on etcd: ephemeral leader key, election loop, and lease renewal.'},
                {'label': 'Task 2', 'text': 'Handle the leader\'s graceful shutdown (release the key) vs crash (lease expiry).'},
                {'label': 'Task 3', 'text': 'Define what the new leader does on takeover: state to reload, work to resume, alerts to fire.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why randomized election timeouts prevent split-vote deadlocks in Raft. Ask me to reason through two candidates.'},
            {'label': 'Implementation Design', 'text': 'Design leader election for a single-writer database shard. What fencing token does the leader carry, and how is it checked on every write?'},
            {'label': 'Boundary Testing', 'text': 'The coordination service itself partitions. What happens to the election? Design the fail-safe behavior of the data plane.'},
        ],
        'takeaways': [
            'Raft requires a majority — split-brain becomes impossible',
            'Ephemeral keys + leases give practical election',
            'Failover downtime equals the election window',
            'Leaders need fencing tokens to be safe after failover',
        ],
        'further': [
            {'title': 'The Raft Consensus Algorithm', 'url': 'https://raft.github.io/'},
            {'title': 'ZooKeeper Leader Election Recipes', 'url': 'https://zookeeper.apache.org/doc/current/recipes.html'},
        ],
    },
    {
        'title': 'Advanced Leader Election: Fencing and Fast Failover',
        'desc': 'Fencing tokens, epoch guards, and election that scales and recovers fast.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Design fencing tokens to stop zombie leaders',
            'Use epochs for safe failover',
            'Minimize failover downtime',
            'Handle cascading elections',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Fencing Tokens', 'paras': [
                'When leadership changes, the old leader may still run for a while. Fencing: every leadership term gets a monotonically increasing token; storage only accepts writes from the current token. A zombie leader with an old token is rejected — split-brain is converted into safe rejection.',
            ], 'code': {'lang': 'text', 'body': '''
Fencing token flow:
  term 5: leader L5 writes with token 5  -> accepted
  L5 crashes; term 6: leader L6 elected, token 6
  L5 wakes and writes with token 5       -> REJECTED (stale token)

This is what makes "at most one leader" enforced by the storage,
not just by the election protocol.'''}},
            {'heading': 'Fast Failover', 'paras': [
                'Failover time = detection + election + handoff. Reduce each: tight heartbeat intervals, ready standbys with warm state, and idempotent handoff so the new leader resumes without double-processing. Balance tight detection against flapping (false failover) under network jitter.',
            ]},
        ],
        'practice': {
            'title': 'Design the Fenced Failover',
            'intro': 'A single-writer partition service: 3 nodes, storage enforces tokens.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the token generation and storage-side validation.'},
                {'label': 'Task 2', 'text': 'Trace the full failover: leader crash, election, token bump, resume. Where is downtime spent?'},
                {'label': 'Task 3', 'text': 'Design the standby warm-up so handoff is near-instant without double-processing.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why election safety alone is not enough and fencing is what protects the data.'},
            {'label': 'Implementation Design', 'text': 'Design a scheduler with 5 nodes and a 200ms failover target. What are the heartbeat, election, and handoff budgets?'},
            {'label': 'Boundary Testing', 'text': 'Network jitter causes flapping elections. Design the hysteresis that prevents thrashing leadership.'},
        ],
        'takeaways': [
            'Fencing tokens make zombie leaders harmless',
            'Epochs give every term a unique identity',
            'Failover time = detection + election + handoff',
            'Warm standbys and idempotent handoff cut downtime',
        ],
        'further': [
            {'title': 'Fencing Tokens — Martin Kleppmann', 'url': 'https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html'},
            {'title': 'Raft Leader Election Section', 'url': 'https://raft.github.io/raft.pdf'},
        ],
    },
    {
        'title': 'Leader Election: Review & Mastery Quiz',
        'desc': 'Scenario questions on leases, consensus, and fencing.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate election concepts',
            'Design safe failover',
            'Prevent split-brain',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Split-brain means? (A: two leaders acting / B: no leader / C: slow leader)',
                'Q2: A lease bounds leadership by? (A: memory / B: time / C: network)',
                'Q3: Raft requires a ___ to elect a leader. (A: majority / B: quorum of 1 / C: supermajority of 2/3)',
                'Q4: True or false: fencing tokens are rejected by storage when stale.',
                'Q5: Failover time equals? (A: detection + election + handoff / B: reboot only / C: network latency)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A single-writer service loses its leader for 30 seconds during failover. Design the pipeline that reduces this to under a second and the fencing that makes it safe.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "the old leader will just stop" is not a safe assumption.'},
        ],
        'takeaways': [
            'Q1: A; Q2: B; Q3: A; Q4: true; Q5: A',
            'Election must be safe, live, and fast',
            'Fencing is what actually protects the data',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# LISKOV SUBSTITUTION
# ─────────────────────────────────────────────────────────────────────────────
_t('liskov-substitution', [
    {
        'title': 'Liskov Substitution: Replaceable Without Surprises',
        'desc': 'Why a subclass must behave like its base class in every way callers rely on.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'State the Liskov substitution principle',
            'Identify substitution violations',
            'Recognize the is-a vs behaves-as distinction',
            'Fix inheritance design that violates LSP',
        ],
        'prereqs': ['principles/interface-segregation', 'principles/single-responsibility'],
        'sections': [
            {'heading': 'The Principle', 'paras': [
                'Liskov Substitution (LSP): if S is a subtype of T, then objects of type T may be replaced with objects of type S without altering the correctness of the program. Callers code against the base contract; every subclass must honor that contract.',
                'The classic violation: a Square extending a Rectangle. A caller widens a rectangle and expects height to stay the same; a Square silently changes both. The caller\'s assumptions about the base class break.',
            ], 'code': {'lang': 'java', 'body': '''
// Violation: Square overrides setters, breaking base-class assumptions
class Rectangle {
    void setWidth(int w)  { this.w = w; }
    void setHeight(int h) { this.h = h; }
}
class Square extends Rectangle {
    void setWidth(int w)  { super.setWidth(w); super.setHeight(w); }
    void setHeight(int h) { super.setWidth(h); super.setHeight(h); }
}
// Caller: rectangle.setWidth(5); rectangle.setHeight(10); assert h == 10
// With a Square in disguise, h becomes 5. Broken.

// Fix: separate shapes — Square and Rectangle are both shapes, not one
// a subtype of the other. Favor composition or a common Shape contract.'''}},
            {'heading': 'Contracts, Not Class Hierarchies', 'paras': [
                'LSP is about honoring contracts: preconditions not strengthened, postconditions not weakened, invariants preserved, exceptions not broadened. A subclass that throws a new checked exception, returns null where the base promised a value, or silently ignores parameters violates the contract even if it compiles.',
            ]},
        ],
        'practice': {
            'title': 'Find the Violations',
            'intro': 'Review: a Bird base class with fly() and a Penguin subclass throwing UnsupportedOperationException; a FileStorage subclass of Storage that writes to memory only.',
            'tasks': [
                {'label': 'Task 1', 'text': 'For each, state the contract violation and the caller surprise.'},
                {'label': 'Task 2', 'text': 'Redesign Penguin: an interface hierarchy (FlyingBird, SwimmingBird) instead of Bird.fly().'},
                {'label': 'Task 3', 'text': 'Redesign FileStorage: separate MemoryStorage implements the same Storage contract honestly.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about the difference between is-a (taxonomy) and behaves-as (contract). Start with Penguin.'},
            {'label': 'Compare & Contrast', 'text': 'Compare LSP violations with interface segregation: what each protects and how they interact.'},
            {'label': 'Boundary Testing', 'text': 'A subclass strengthens a precondition (rejects empty strings the base accepts). Is that always a violation? Argue with a real API.'},
        ],
        'takeaways': [
            'Subtypes must honor the base contract fully',
            'Preconditions strengthen or postconditions weaken = violation',
            'Contract-first design beats taxonomy-based inheritance',
            'Composition and interfaces prevent most LSP traps',
        ],
        'further': [
            {'title': 'The Liskov Substitution Principle (Barbara Liskov)', 'url': 'https://en.wikipedia.org/wiki/Liskov_substitution_principle'},
            {'title': 'SOLID — Robert C. Martin', 'url': 'https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html'},
        ],
    },
    {
        'title': 'LSP in Production: Interfaces and APIs',
        'desc': 'Substitution at the interface level, contracts in typed systems, and pluggable implementations.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Apply LSP to interface implementations',
            'Design contracts with pre/post conditions',
            'Test substitution behavior',
            'Avoid covariant traps',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Interface Contracts', 'paras': [
                'Every implementation of an interface promises the contract: the same behavior for the same inputs, honoring the same invariants. The repository interface promises find() never returns null on missing rows? Then every implementation — Postgres, in-memory, mock — must keep that promise.',
            ], 'code': {'lang': 'typescript', 'body': '''
// Contract: find returns undefined for missing ids, never throws
interface UserStore {
    find(id: string): Promise<User | undefined>;
}

// Postgres impl: returns undefined on empty row   -> honors contract
// Redis impl:   throws on missing key            -> VIOLATES contract
// Fake in tests: returns User({ id, ... })         -> honors contract

// Contract tests run against every implementation:
test.each(implementations)('$name find honors contract', (impl) => {
    expect(await impl.find('missing')).toBeUndefined();
});'''}},
            {'heading': 'Contract Tests', 'paras': [
                'The strongest guard for LSP is contract testing: the same test suite runs against every implementation of an interface, verifying pre/post conditions and invariants uniformly. If the mock, the real store, and the cache all pass the same suite, substitution is safe.',
            ]},
        ],
        'practice': {
            'title': 'Write the Contract Suite',
            'intro': 'A cache interface has get, set, and delete, with a documented contract.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Write the contract: what get returns for missing keys, TTL semantics, and delete idempotency.'},
                {'label': 'Task 2', 'text': 'Implement the contract test suite and run it against an in-memory and a Redis implementation.'},
                {'label': 'Task 3', 'text': 'Fix the implementation that violates the contract and document why.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why contract tests are the practical enforcement of LSP. Ask me to list the contract points of an interface you know.'},
            {'label': 'Implementation Design', 'text': 'Design a plugin API where third-party plugins must honor the contract. What tests can you run against plugins at load time?'},
            {'label': 'Boundary Testing', 'text': 'Two implementations legitimately differ in performance but not behavior. Where does that difference belong in the contract?'},
        ],
        'takeaways': [
            'Every implementation honors the same contract',
            'Contract tests run uniformly against all implementations',
            'Behavioral substitutability is what callers rely on',
            'Performance differences are not contract violations',
        ],
        'further': [
            {'title': 'Contract Testing — Pact', 'url': 'https://docs.pact.io/'},
            {'title': 'Design by Contract — Eiffel', 'url': 'https://www.eiffel.com/values/design-by-contract/introduction/'},
        ],
    },
    {
        'title': 'Advanced LSP: Variance and Behavioral Contracts',
        'desc': 'Covariance/contravariance, immutable types, and the precise rules of behavioral substitution.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Explain variance in typed systems',
            'Apply behavioral subtyping rules precisely',
            'Use immutable types to avoid substitution traps',
            'Design hierarchies that survive evolution',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Variance', 'paras': [
                'Variance governs where a subtype can appear: a List<Square> is not a List<Rectangle> (adding a Rectangle would break it). Covariance (producers) and contravariance (consumers) encode this: read-only containers can be covariant; mutable ones cannot.',
            ], 'code': {'lang': 'text', 'body': '''
Variance rules:
  Covariant  (out / +T): value only leaves -> List<out Square> is List<Rectangle>
  Contravariant (in / -T): value only enters -> Consumer<in Rectangle> is Consumer<Square>
  Invariant: mutable containers (read AND write) -> no substitution

Behavioral subtyping: subtype must
  - not strengthen preconditions
  - not weaken postconditions
  - preserve invariants
  - not broaden thrown exceptions'''}},
            {'heading': 'Immutable Design', 'paras': [
                'Immutable types sidestep most variance and substitution hazards: a read-only Square where a Rectangle is expected is safe because nothing can mutate it into a contradiction. Immutability turns many LSP traps into non-issues.',
            ]},
        ],
        'practice': {
            'title': 'Design a Variance-Safe Model',
            'intro': 'A document system: read-only views, mutable documents, and a producer of documents.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the type hierarchy so read views are covariant and writers are invariant.'},
                {'label': 'Task 2', 'text': 'Prove that a List<SpecialDoc> is not assignable to List<Doc> and explain the runtime hazard it prevents.'},
                {'label': 'Task 3', 'text': 'Refactor one mutable hierarchy to immutable value types and note what substitution guarantees you gain.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why "out" and "in" annotations encode behavioral substitution in the type system.'},
            {'label': 'Implementation Design', 'text': 'Design a collection library API with correct variance annotations and prove each with a substitution example.'},
            {'label': 'Boundary Testing', 'text': 'A subtype narrows a return type (covariant return) — is that always safe? Give the rule and a counterexample.'},
        ],
        'takeaways': [
            'Variance encodes where substitution is type-safe',
            'Behavioral subtyping rules are the semantic contract',
            'Immutability eliminates many substitution hazards',
            'Covariant returns are safe; covariant mutable containers are not',
        ],
        'further': [
            {'title': 'Variance — Kotlin Docs', 'url': 'https://kotlinlang.org/docs/generics.html#variance'},
            {'title': 'Behavioral Subtyping — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Behavioral_subtyping'},
        ],
    },
    {
        'title': 'Liskov Substitution: Review & Mastery Quiz',
        'desc': 'Scenario questions on contracts, substitution, and variance.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate LSP concepts',
            'Detect contract violations',
            'Design substitutable hierarchies',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: A subtype must honor? (A: the base contract / B: only new methods / C: nothing)',
                'Q2: Square extends Rectangle is a classic LSP violation because? (A: it changes width too / B: it is too fast / C: it is abstract)',
                'Q3: Strengthening a precondition in a subtype? (A: is safe / B: violates LSP / C: is required)',
                'Q4: True or false: contract tests should run against every implementation.',
                'Q5: A mutable List<Square> is a List<Rectangle>? (A: yes / B: no / C: maybe)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A payment provider interface has two implementations that behave differently on declined payments. Design the contract test suite that catches the difference.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "it compiles, so it is substitutable" is false.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: B; Q4: true; Q5: B',
            'Substitution is a behavioral promise, not a type label',
            'Contract tests make the promise executable',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# LOAD SHEDDING
# ─────────────────────────────────────────────────────────────────────────────
_t('load-shedding', [
    {
        'title': 'Load Shedding: Drop Work Before the System Drops',
        'desc': 'Choosing what to reject under overload so the system survives to serve the rest.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Define load shedding and its goal',
            'Distinguish shedding from failing',
            'Pick what to shed (queues, non-essential work)',
            'Signal shedding to clients',
        ],
        'prereqs': ['principles/circuit-breaker', 'principles/graceful-degradation'],
        'sections': [
            {'heading': 'The Idea', 'paras': [
                'When demand exceeds capacity, a system has three options: queue (and build latency until timeout), fail all (and take the whole service down), or shed (reject the least-valuable work and serve the rest well). Load shedding is the third: deliberate, prioritized rejection.',
                'The goal is to protect the work already in flight and the core function — a video platform under load sheds low-priority transcoding before it drops playback.',
            ], 'code': {'lang': 'python', 'body': '''
# Priority-based shedding at the edge
import time
IN_FLIGHT = 0
MAX_IN_FLIGHT = 200

def handle(request):
    global IN_FLIGHT
    if IN_FLIGHT >= MAX_IN_FLIGHT:
        if request.priority == 'critical':
            pass                    # only critical traffic gets in
        else:
            return 503_retry_after(2)   # shed: fast, explicit, retryable
    IN_FLIGHT += 1
    try:
        return process(request)
    finally:
        IN_FLIGHT -= 1'''}},
            {'heading': 'Shedding vs Failing', 'paras': [
                'Shedding is honest and explicit: reject with 429/503, a Retry-After header, and a clear reason. It tells the client "try later", so the client backs off instead of retrying harder. Shedding well is a coordination signal, not just a rejection.',
            ]},
        ],
        'practice': {
            'title': 'Pick What to Shed',
            'intro': 'A ticket site is overloaded during a flash sale. Requests: browsing, seat holds, checkout, analytics events, admin dashboard.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Rank the traffic by value and decide the shed order.'},
                {'label': 'Task 2', 'text': 'Design the response for shed traffic (status, Retry-After, message).'},
                {'label': 'Task 3', 'text': 'Decide what MUST never be shed and why (seat holds mid-checkout).'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why queueing everything is worse than shedding the least-valuable work. Start with latency cliffs.'},
            {'label': 'Compare & Contrast', 'text': 'Compare load shedding, rate limiting, and circuit breakers. When is each the right response to overload?'},
            {'label': 'Boundary Testing', 'text': 'A client ignores 503s and retries immediately. Design the backoff contract and the server-side guard.'},
        ],
        'takeaways': [
            'Shed the least-valuable work to protect the rest',
            'Explicit 429/503 with Retry-After is honest shedding',
            'Never shed in-flight critical work',
            'Shedding signals coordination to well-behaved clients',
        ],
        'further': [
            {'title': 'Handling Overload — Google SRE Book', 'url': 'https://sre.google/sre-book/handling-overload/'},
            {'title': 'Load Shedding in Envoy', 'url': 'https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/load_balancing/overload_manager'},
        ],
    },
    {
        'title': 'Load Shedding in Production: Queues and Priorities',
        'desc': 'Bounded queues, priority admission, and shedding at every layer.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design bounded queues with shed-on-full',
            'Implement priority admission control',
            'Shed at multiple layers (edge, app, worker)',
            'Monitor shedding as a signal',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Bounded Queues and Admission', 'paras': [
                'An unbounded queue is a latency bomb: work waits so long that it times out, and the queue becomes the outage. A bounded queue with shed-on-full converts overload into fast rejection. Admission control checks the queue depth and the in-flight count before accepting work.',
            ], 'code': {'lang': 'go', 'body': '''
// Admission control: shed when the system is saturated
var sem = make(chan struct{}, 100)     // 100 concurrent jobs
var queueDepth atomic.Int64

func Enqueue(job Job) error {
    if queueDepth.Load() > 50 {
        return errShedding                   // shed fast, before queueing
    }
    if len(sem) >= 100 {
        return errShedding                   // all workers busy
    }
    queueDepth.Add(1)
    sem <- struct{}{}
    go func() { defer func() { <-sem; queueDepth.Add(-1) }(); run(job) }()
    return nil
}'''}},
            {'heading': 'Shedding Layers', 'paras': [
                'Shed at the edge (CDN/load balancer rejects early), at the app (admission control), and at workers (drop lowest-priority jobs). Each layer sheds earlier and cheaper than the one below, protecting the expensive resources closest to the source of truth.',
            ]},
        ],
        'practice': {
            'title': 'Design the Shed Ladder',
            'intro': 'A search service: query API, index-refresh jobs, analytics export, and autocomplete suggestions.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define capacity budgets per layer and per work type.'},
                {'label': 'Task 2', 'text': 'Design the shed order and the responses clients see.'},
                {'label': 'Task 3', 'text': 'Define the shedding metric dashboard (shed rate, shed by type) and its alerts.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why shedding early (edge) is cheaper than shedding late (worker). Ask me to trace the cost of each.'},
            {'label': 'Implementation Design', 'text': 'Design admission control for a chat system where message delivery must never be shed but analytics may be. What budgets?'},
            {'label': 'Boundary Testing', 'text': 'The shed signal itself gets noisy and clients over-backoff. Design the jitter and the recovery ramp.'},
        ],
        'takeaways': [
            'Bounded queues + shed-on-full beat unbounded latency bombs',
            'Priority admission protects critical work',
            'Shed at every layer, cheapest first',
            'Shed rate is a first-class metric with alerts',
        ],
        'further': [
            {'title': 'Admission Control — Google SRE', 'url': 'https://sre.google/sre-book/handling-overload/'},
            {'title': 'Netflix Overload Controls', 'url': 'https://netflixtechblog.com/performance-under-load-9a8a1f4f1e9b'},
        ],
    },
    {
        'title': 'Advanced Load Shedding: Adaptive and Fair Shedding',
        'desc': 'Capacity estimation, per-tenant fairness, and shedding that adapts to real load.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Estimate capacity from signals, not guesses',
            'Implement adaptive shedding thresholds',
            'Shed fairly across tenants',
            'Prevent shed cascades',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Signal-Based Capacity', 'paras': [
                'Shedding thresholds are better derived from live signals than static guesses: CPU saturation, queue depth, request latency percentiles, and error rates. An adaptive controller raises the shed threshold as capacity proves itself and lowers it as latency climbs.',
            ], 'code': {'lang': 'go', 'body': '''
// Adaptive: shed when p99 latency exceeds the budget
var p99 latencyPercentile

func shouldShed() bool {
    return p99.value() > 500*time.Millisecond   // latency budget
        || cpu > 0.85                            // resource budget
}
// The threshold is a target, not a constant: under load it responds
// before queues grow, because latency reflects saturation early.'''}},
            {'heading': 'Fair Shedding and Cascades', 'paras': [
                'Shedding must be fair across tenants: one flood should not shed everyone. Per-tenant budgets and per-tenant shed rates isolate the noisy tenant. And shedding must not cascade — if every node sheds simultaneously and the client retries everywhere, the retry storm is the new overload.',
                'Coordination: shed responses carry Retry-After with jitter, and clients exponentially back off. Recovery ramps traffic gradually instead of reopening the floodgates.',
            ]},
        ],
        'practice': {
            'title': 'Design Fair Adaptive Shedding',
            'intro': 'A multi-tenant analytics platform: one tenant bursts 10x during their marketing campaign.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design per-tenant budgets and the fair-share shed rule.'},
                {'label': 'Task 2', 'text': 'Design the adaptive threshold from latency signals with hysteresis.'},
                {'label': 'Task 3', 'text': 'Design the recovery ramp and the client backoff contract that prevents a retry storm.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why latency percentiles signal saturation earlier than CPU or queue depth.'},
            {'label': 'Implementation Design', 'text': 'Design admission control for a system with three SLA classes (gold/silver/bronze). How does shedding respect the classes?'},
            {'label': 'Boundary Testing', 'text': 'All nodes shed at once and the fleet looks "fine" (low CPU) because work is being rejected. Design the alert that distinguishes healthy shedding from a real outage.'},
        ],
        'takeaways': [
            'Derive shed thresholds from live signals',
            'Per-tenant budgets make shedding fair',
            'Retry-After with jitter prevents retry storms',
            'Shedding must be distinguishable from outages in monitoring',
        ],
        'further': [
            {'title': 'Performance Under Load — Netflix', 'url': 'https://netflixtechblog.com/performance-under-load-9a8a1f4f1e9b'},
            {'title': 'AIMD Congestion Control (the classic adaptive scheme)', 'url': 'https://en.wikipedia.org/wiki/Additive_increase/multiplicative_decrease'},
        ],
    },
    {
        'title': 'Load Shedding: Review & Mastery Quiz',
        'desc': 'Scenario questions on shedding, admission, and fairness.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate shedding concepts',
            'Design admission control',
            'Keep shedding fair and observable',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Load shedding means? (A: queue everything / B: reject least-valuable work / C: fail all)',
                'Q2: Shed responses should include? (A: Retry-After / B: a stack trace / C: nothing)',
                'Q3: An unbounded queue under overload becomes? (A: a latency bomb / B: a cache / C: faster)',
                'Q4: True or false: shedding should be fair across tenants.',
                'Q5: The best capacity signal is? (A: a guess / B: live latency percentiles / C: ticket count)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A payment processor is overloaded at peak. Design the shed ladder that protects in-flight checkouts, rejects new low-value traffic politely, and recovers without a retry storm.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "add a bigger queue" is often the wrong answer to overload.'},
        ],
        'takeaways': [
            'Q1: B; Q2: A; Q3: A; Q4: true; Q5: B',
            'Shedding is prioritized rejection with a coordination signal',
            'Fairness and recovery ramp make it safe at scale',
        ],
    },
])
