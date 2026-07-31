#!/usr/bin/env python3
"""Deep curriculum data for the remaining 32 principles (ACID + backpressure are done).

Each entry: TOPICS[slug] = [4 topic dicts] for fundamentals / applications /
advanced / review-quiz, consumed by gen-principles.py's build() helper.
"""

TOPICS = {}


def _t(slug, topics):
    TOPICS[slug] = topics
    return topics


# ─────────────────────────────────────────────────────────────────────────────
# BASE
# ─────────────────────────────────────────────────────────────────────────────
_t('base', [
    {
        'title': 'BASE: Eventually Consistent Distributed Systems',
        'desc': 'Why availability-first systems trade strong consistency for liveness, and what that means in practice.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Deconstruct the BASE acronym into its three properties',
            'Contrast BASE with ACID across real workloads',
            'Recognize where eventual consistency is safe',
            'Trace a read-your-writes violation scenario',
        ],
        'prereqs': ['principles/acid', 'principles/eventual-consistency'],
        'sections': [
            {'heading': 'What BASE Actually Means', 'paras': [
                'BASE stands for Basically Available, Soft state, Eventual consistency. It is the pragmatic counterweight to ACID: instead of guaranteeing consistency at every instant, the system guarantees the data will converge — eventually — while staying available.',
                'Basically Available means the system responds to every request, even if the answer is slightly stale. Soft state means replicas may be out of sync at any moment. Eventual consistency means that, given enough time without new writes, all replicas converge to the same value.',
            ], 'code': {'lang': 'text', 'body': '''
# The BASE contract in one sentence per property
Basically Available : every request gets a response (maybe stale)
Soft state          : replicas may diverge between writes
Eventual consistency: given quiet time, replicas converge'''}},
            {'heading': 'BASE vs ACID', 'paras': [
                'ACID optimizes for correctness under failure; BASE optimizes for availability and latency under scale. A bank ledger must be ACID; a social feed can be BASE.',
                'The choice is not either/or — most production systems are a blend: ACID for the money path, BASE for the recommendation path.',
            ]},
        ],
        'practice': {
            'title': 'Choose the Right Consistency Contract',
            'intro': 'For each service below, decide ACID or BASE and justify in one sentence: a shopping cart, a like counter, a banking balance, a search index, a chat presence indicator.',
            'tasks': [
                {'label': 'Task 1', 'text': 'For the like counter, design a system where the count may briefly show 1,004 instead of 1,003. What convergence mechanism fixes it?'},
                {'label': 'Task 2', 'text': 'For the banking balance, explain what breaks if you store it in a BASE store.'},
                {'label': 'Task 3', 'text': 'Draw the read-your-writes violation: user writes a post on replica A, reads on replica B, and does not see it. How long until it appears?'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about when a distributed system can be BASE for reads but ACID for writes. Start with the write path.'},
            {'label': 'Compare & Contrast', 'text': 'Compare the eventual-consistency guarantees of DynamoDB (multi-AZ, strong by default) versus Cassandra (tunable, eventual by default). When is each the right call?'},
            {'label': 'Boundary Testing', 'text': 'A BASE system serves a decrement of an inventory count. The request succeeds but the write is lost. Design a compensation mechanism that does not reintroduce a hot single-writer bottleneck.'},
        ],
        'takeaways': [
            'BASE trades strict consistency for availability and low latency',
            'Soft state means replicas are allowed to diverge',
            'Eventual consistency requires convergence, not just availability',
            'Real systems mix ACID and BASE per data path',
        ],
        'further': [
            {'title': 'Dynamo: Amazon\'s Highly Available Key-value Store', 'url': 'https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf'},
            {'title': 'CAP Theorem Explained', 'url': 'https://www.ibm.com/topics/cap-theorem'},
        ],
    },
    {
        'title': 'BASE in Production: Caches, Feeds, and Counters',
        'desc': 'How real companies ship BASE systems: cache invalidation, feed fan-out, and idempotent counters.',
        'dur': '60 min', 'diff': 'Intermediate',
        'prereqs': [],
        'objs': [
            'Design a cache with bounded staleness',
            'Build a fan-out feed that tolerates stale reads',
            'Implement an eventually consistent counter',
            'Choose reconciliation over locking where possible',
        ],
        'sections': [
            {'heading': 'Caches Are BASE', 'paras': [
                'A read-through cache is the simplest BASE system: it is basically available, holds soft state, and converges when the TTL expires or invalidation fires. The art is bounding staleness so users never notice.',
                'Use a monotonically increasing version per key; when the client sees an older version, it refreshes from the source. This converts a silent staleness bug into a visible, correctable one.',
            ], 'code': {'lang': 'python', 'body': '''
# Versioned cache entry: staleness becomes observable
import time

cache = {}  # key -> (version, value)

def put(key, value, version):
    cache[key] = (version, value, time.time())

def get(key, max_age_s=30):
    version, value, ts = cache.get(key, (0, None, 0))
    stale = (time.time() - ts) > max_age_s
    return value, version, stale'''}},
            {'heading': 'Fan-Out Feeds', 'paras': [
                'When a celebrity posts, a push fan-out writes to millions of inboxes asynchronously. Inbox reads are BASE: a follower may see the post seconds late, but the system stays available under load.',
                'Pull-based fallback (timeline assembled on read) keeps the system alive when the push pipeline lags.',
            ]},
        ],
        'practice': {
            'title': 'Stale Counters and Reconciliation',
            'intro': 'Your like counter shows slightly wrong totals because counters are updated on replicas without a central lock.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design a counter that increments locally and periodically sends deltas to a central reconciler.'},
                {'label': 'Task 2', 'text': 'What happens to the displayed count when two replicas both increment? Prove the delta-merge is commutative.'},
                {'label': 'Task 3', 'text': 'Add a nightly job that recomputes true counts from the source of truth and corrects drift.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why a TTL cache with a 60-second expiry is acceptable for a profile page but not for a payment status page. Ask me questions as you go.'},
            {'label': 'Implementation Design', 'text': 'Design a news feed that is BASE for reads but guarantees the author always sees their own post immediately (read-your-writes). Where does the read route?'},
            {'label': 'Boundary Testing', 'text': 'A caching layer serves a deleted item for 5 minutes after deletion. List every user-visible consequence and design a tombstone mechanism.'},
        ],
        'takeaways': [
            'Caches, feeds, and counters are the canonical BASE systems',
            'Versioning makes staleness observable and fixable',
            'Delta-merging counters requires commutative operations',
            'Tombstones prevent resurrecting deleted data in caches',
        ],
        'further': [
            {'title': 'Eventually Consistent — Revisited', 'url': 'https://www.allthingsdistributed.com/2008/12/eventually_consistent.html'},
            {'title': 'Designing Data-Intensive Applications', 'url': 'https://dataintensive.net/'},
        ],
    },
    {
        'title': 'Advanced BASE: CRDTs and Anti-Entropy',
        'desc': 'Conflict-free replicated data types, gossip protocols, and how systems guarantee convergence without coordination.',
        'dur': '75 min', 'diff': 'Advanced',
        'prereqs': [],
        'objs': [
            'Explain why merge functions must be commutative and associative',
            'Build a G-Counter and an OR-Set CRDT',
            'Understand gossip-based anti-entropy',
            'Apply CRDTs where locks are unacceptable',
        ],
        'sections': [
            {'heading': 'CRDTs: Convergence Without Coordination', 'paras': [
                'A CRDT is a data type whose replicas can diverge and yet merge deterministically into the same state, provided the merge operation is commutative, associative, and idempotent.',
                'The grow-only counter (G-Counter) is the simplest: each replica keeps its own per-replica count, and the total is the sum across replicas. Merging is just element-wise max.',
            ], 'code': {'lang': 'python', 'body': '''
# G-Counter: each replica owns a slot, total = sum of slots
class GCounter:
    def __init__(self, replica_id, slots=None):
        self.replica_id = replica_id
        self.slots = slots or {}  # replica -> count

    def inc(self):
        self.slots[self.replica_id] = self.slots.get(self.replica_id, 0) + 1

    def value(self):
        return sum(self.slots.values())

    def merge(self, other):
        for r, c in other.slots.items():
            self.slots[r] = max(self.slots.get(r, 0), c)

a, b = GCounter('a'), GCounter('b')
a.inc(); a.inc(); b.inc()          # divergent replicas
a.merge(b); b.merge(a)             # exchange state
assert a.value() == b.value() == 3 # converged'''}},
            {'heading': 'Anti-Entropy and Gossip', 'paras': [
                'Anti-entropy is the background process that keeps replicas converging: each replica periodically exchanges state with a random peer, merging as it goes. Gossip protocols use this to spread updates with logarithmic convergence time.',
                'CRDTs shine precisely because they make the gossip merge a pure function — no consensus, no leader, no locking.',
            ]},
        ],
        'practice': {
            'title': 'Build an OR-Set',
            'intro': 'An observed-remove set must never resurrect a removed element after a merge.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the state: a set of (element, unique-token) pairs, with add adding a token and remove adding a tombstone token.'},
                {'label': 'Task 2', 'text': 'Implement merge as the union of both states. Prove that an element removed on one replica stays removed after merge.'},
                {'label': 'Task 3', 'text': 'Extend to an LWW (last-writer-wins) register and explain the clock requirements for correctness.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why a naive set CRDT (union-based) resurrects deleted items, and what tokens fix it.'},
            {'label': 'Compare & Contrast', 'text': 'Compare CRDT convergence with Raft-based consensus. When does a system need Raft despite CRDTs existing? Give concrete systems (e.g., Redis vs Riak).'},
            {'label': 'Implementation Design', 'text': 'Design a distributed collaborative editing system (like a shared notes app) using CRDTs. How do you handle the text model, offline edits, and merge of concurrent typing?'},
        ],
        'takeaways': [
            'CRDT merges must be commutative, associative, and idempotent',
            'G-Counter converges by summing per-replica slots',
            'Tombstones prevent resurrection in observed-remove sets',
            'Gossip + CRDTs gives convergence without a leader',
        ],
        'further': [
            {'title': 'CRDTs for Mortals', 'url': 'https://medium.com/@istanbul_techie/crdts-for-mortal-developers-6dcfb10c5a7d'},
            {'title': 'The Paper: Conflict-free Replicated Data Types', 'url': 'https://hal.inria.fr/inria-00555588/document'},
        ],
    },
    {
        'title': 'BASE: Review & Mastery Quiz',
        'desc': 'Scenario questions on availability, soft state, eventual consistency, and CRDT convergence.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate the BASE mental model',
            'Apply convergence reasoning to new systems',
            'Spot anti-patterns in eventually consistent designs',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: A BASE system must guarantee what about requests? (A: strong consistency / B: a response / C: serializability)',
                'Q2: Which of these is NOT a BASE property? (A: basically available / B: soft state / C: two-phase commit)',
                'Q3: A G-Counter merge uses which operation per slot? (A: sum / B: max / C: min)',
                'Q4: True or false: a TTL cache is a form of eventual consistency.',
                'Q5: An OR-Set prevents which failure mode? (A: lost updates / B: resurrection / C: deadlock)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A gaming leaderboard shows top-100 with slight lag. Users complain their rank is wrong. Redesign to make ranks converge within 5 seconds without a global lock.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "just use ACID everywhere" is not an option at global scale, using concrete latency and availability numbers.'},
        ],
        'takeaways': [
            'Q1: B; Q2: C; Q3: B; Q4: true; Q5: B',
            'BASE is a contract about availability and eventual convergence',
            'Convergence mechanisms must be deterministic and idempotent',
        ],
    },
])
