#!/usr/bin/env python3
"""Deep curriculum data batch 4: flyweight, gossip, hash-index, interpreter, iterator, leader-follower."""

TOPICS = {}


def _t(slug, topics):
    TOPICS[slug] = topics
    return topics


# ─────────────────────────────────────────────────────────────────────────────
# FLYWEIGHT
# ─────────────────────────────────────────────────────────────────────────────
_t('flyweight', [
    {
        'title': 'Flyweight: Share the Repetitive State',
        'desc': 'Sharing immutable intrinsic state across thousands of objects to cut memory without changing behavior.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the flyweight intent',
            'Split intrinsic from extrinsic state',
            'Share state through a factory',
            'Measure the memory win',
        ],
        'prereqs': ['patterns/factory', 'principles/caching'],
        'sections': [
            {'heading': 'The Problem: Object Explosion', 'paras': [
                'A text editor stores a glyph object per character: 10MB of text means millions of FontGlyph objects, each carrying the same font data. The flyweight pattern separates intrinsic state (shared, immutable — the glyph shape) from extrinsic state (per-use, mutable — the position), and shares the intrinsic part.',
            ], 'code': {'lang': 'java', 'body': '''
// Intrinsic: the glyph shape — shared across all positions
final class Glyph {
    final char c; final Font font;
    Glyph(char c, Font f) { this.c = c; this.font = f; }
    void draw(int x, int y) { font.render(c, x, y); }  // extrinsic passed in
}

class GlyphFactory {
    private final Map<String, Glyph> cache = new HashMap<>();
    Glyph get(char c, Font f) {
        return cache.computeIfAbsent(c + ":" + f.id(), k -> new Glyph(c, f));
    }
}
// One Glyph per (char, font) pair — not one per character on screen'''}},
            {'heading': 'Intrinsic vs Extrinsic', 'paras': [
                'Intrinsic state never changes and is stored once. Extrinsic state changes per use and is passed in or held by the client. Getting the split wrong — sharing something mutable — silently corrupts every shared user.',
            ]},
        ],
        'practice': {
            'title': 'Share the Trees',
            'intro': 'A forest renderer creates 100,000 tree objects with 3 species; each species has a heavy mesh and texture.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Split species data (intrinsic) from position/scale (extrinsic).'},
                {'label': 'Task 2', 'text': 'Build the species factory and render 100,000 trees with 3 shared species.'},
                {'label': 'Task 3', 'text': 'Measure memory before and after; report the ratio.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about the intrinsic/extrinsic split. Start with why intrinsic state must be immutable.'},
            {'label': 'Compare & Contrast', 'text': 'Compare flyweight with the object pool. One shares identity, the other shares resources — when does each apply?'},
            {'label': 'Boundary Testing', 'text': 'A caller mutates what was supposed to be intrinsic state. Design the defensive copy or freeze that prevents corruption.'},
        ],
        'takeaways': [
            'Flyweight shares immutable intrinsic state',
            'Extrinsic state is passed per use, never stored',
            'A factory guarantees one shared instance per key',
            'The split must keep shared state immutable',
        ],
        'further': [
            {'title': 'Flyweight — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/flyweight'},
            {'title': 'Flyweight Pattern — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Flyweight_pattern'},
        ],
    },
    {
        'title': 'Flyweight in Production: Caches and Runtimes',
        'desc': 'How JVM string interning, icon caches, and game engines use flyweight at scale.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Use string interning as a flyweight',
            'Cache heavy shared assets',
            'Design key composition for the factory',
            'Avoid sharing mutable aggregates',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Interning and Asset Caches', 'paras': [
                'JVM string interning and Symbol tables are flyweights: one canonical instance per value, shared everywhere. UI frameworks cache icons and skins per theme; game engines cache meshes and textures per model. The factory key must capture every intrinsic dimension or distinct states collapse into one shared object.',
            ], 'code': {'lang': 'typescript', 'body': '''
// Asset cache as flyweight factory
const assetCache = new Map<string, Texture>();

function getTexture(name: string, mipLevels: number): Texture {
    const key = `${name}#${mipLevels}`;   // key covers ALL intrinsic dims
    let t = assetCache.get(key);
    if (!t) {
        t = loadTexture(name, mipLevels);
        assetCache.set(key, t);
    }
    return t;  // one Texture shared by every sprite that uses it
}'''}},
            {'heading': 'The Cache Is the Contract', 'paras': [
                'The flyweight factory is a cache, and caches need eviction. When memory pressure rises, the factory must either pin hot flyweights or rebuild them — a shared object cannot simply be dropped while in use. Reference counting or weak references make eviction safe.',
            ]},
        ],
        'practice': {
            'title': 'Cache the Icon Set',
            'intro': 'A UI renders 5,000 icons from 40 themes; each icon+theme pair is a heavy raster.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the factory key (icon id, theme, size, dpr).'},
                {'label': 'Task 2', 'text': 'Add a least-recently-used eviction that is safe for in-flight renders.'},
                {'label': 'Task 3', 'text': 'Measure hit rate and memory; tune the capacity.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why the factory key must cover every intrinsic dimension. Ask me what breaks when it does not.'},
            {'label': 'Implementation Design', 'text': 'Design an interning table for user IDs and profile objects in a chat app. What is shared, what is per-user, and how is eviction handled?'},
            {'label': 'Boundary Testing', 'text': 'Two threads request the same flyweight simultaneously. Design the factory concurrency (double-checked locking, or lock-free computeIfAbsent).'},
        ],
        'takeaways': [
            'Interning and asset caches are flyweights in the wild',
            'The key must cover all intrinsic dimensions',
            'Flyweight factories are caches and need eviction policies',
            'Concurrency-safe factories need careful key handling',
        ],
        'further': [
            {'title': 'String Interning — JVM', 'url': 'https://docs.oracle.com/javase/8/docs/api/java/lang/String.html#intern--'},
            {'title': 'Flyweight — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/flyweight'},
        ],
    },
    {
        'title': 'Advanced Flyweight: Pools, Weak References, and Shared Mutable State',
        'desc': 'Flyweight beyond pure sharing: pooled flyweights, weak-reference caches, and the hazards of shared mutation.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Combine flyweight with object pooling',
            'Use weak references for safe eviction',
            'Recognize shared-mutable-state hazards',
            'Design flyweights for concurrent use',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Flyweight + Pooling', 'paras': [
                'A pool is a flyweight whose instances are reusable rather than immutable: database connections, buffers, worker objects. The pool hands out an instance, the borrower returns it, and the pool resets it. The reset must fully restore the intrinsic contract or the next borrower inherits corruption.',
            ], 'code': {'lang': 'go', 'body': '''
// Pooled flyweight: reuse, reset, return
type ConnPool struct {
    idle chan *Conn
    newConn func() *Conn
}
func (p *ConnPool) Acquire() *Conn {
    select {
    case c := <-p.idle:
        c.Reset()          // full reset = intrinsic contract restored
        return c
    default:
        return p.newConn()
    }
}
func (p *ConnPool) Release(c *Conn) {
    c.Reset()
    select { case p.idle <- c: default: c.Close() }  // pool full: close
}'''}},
            {'heading': 'Weak-Reference Caches and Concurrency', 'paras': [
                'Weak-reference caches (WeakHashMap, weakref) let the GC reclaim unused flyweights — eviction without policy. The cost: a request may miss and rebuild. For concurrent use, flyweights must be safe to share: immutable fields, no internal mutable counters, or explicit synchronization.',
            ]},
        ],
        'practice': {
            'title': 'Design the Safe Pool',
            'intro': 'A request-scoped buffer pool is shared across 40 goroutines handling concurrent requests.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the pool with acquire/release and a full-reset contract.'},
                {'label': 'Task 2', 'text': 'Add the weak-reference variant and compare eviction behavior under GC.'},
                {'label': 'Task 3', 'text': 'Write the race test that proves resets and borrows never overlap.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why a pool flyweight must fully reset before reuse.'},
            {'label': 'Implementation Design', 'text': 'Design a thread-safe shared render state: immutable geometry shared, mutable transform per call. Where do the flyweight and the extrinsic state live?'},
            {'label': 'Boundary Testing', 'text': 'A borrower forgets to return a pooled object. Design the leak detection (finalizers, metrics) that surfaces it.'},
        ],
        'takeaways': [
            'Pools are reusable flyweights with a reset contract',
            'Weak references give eviction without policy',
            'Shared mutable state is the flyweight failure mode',
            'Concurrent flyweights must be immutable or synchronized',
        ],
        'further': [
            {'title': 'Object Pool — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/object-pool'},
            {'title': 'WeakHashMap — Javadoc', 'url': 'https://docs.oracle.com/javase/8/docs/api/java/util/WeakHashMap.html'},
        ],
    },
    {
        'title': 'Flyweight: Review & Mastery Quiz',
        'desc': 'Scenario questions on state splits, factories, and pools.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate flyweight concepts',
            'Split state correctly',
            'Design safe caches and pools',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Intrinsic state must be? (A: mutable / B: immutable / C: per-user)',
                'Q2: Extrinsic state is passed? (A: per use / B: once / C: never)',
                'Q3: The flyweight factory acts as a? (A: cache / B: database / C: compiler)',
                'Q4: True or false: a pool is a reusable flyweight with a reset contract.',
                'Q5: Weak-reference caches evict? (A: via GC / B: via LRU / C: never)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A chess game shows 32 pieces reused across 10,000 board cells. Design the flyweight and what the extrinsic state holds.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why sharing mutable state across objects is worse than not sharing at all.'},
        ],
        'takeaways': [
            'Q1: B; Q2: A; Q3: A; Q4: true; Q5: A',
            'Share immutable intrinsic state; pass extrinsic per use',
            'Caches and pools operationalize the pattern safely',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# GOSSIP
# ─────────────────────────────────────────────────────────────────────────────
_t('gossip', [
    {
        'title': 'Gossip Protocol: Epidemic Dissemination',
        'desc': 'Spreading state to every node with random peer exchange — like an epidemic, not a tree.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the gossip model',
            'Describe push, pull, and push-pull',
            'Analyze convergence and fan-out',
            'Use gossip for membership and state',
        ],
        'prereqs': ['patterns/paxos', 'patterns/raft'],
        'sections': [
            {'heading': 'The Model', 'paras': [
                'Each node periodically picks a random peer and exchanges summaries. Information spreads exponentially: with fan-out f per round, after t rounds roughly f^t nodes have heard it. There is no coordinator, no tree, and no single point of failure — the protocol is self-healing and eventually consistent.',
            ], 'code': {'lang': 'python', 'body': '''
# Push gossip: every round, send your state to a random peer
import random

class Node:
    def __init__(self, node_id, peers):
        self.id = node_id
        self.peers = peers          # neighbor set
        self.state = {}             # key -> (value, version)

    def round(self):
        peer = random.choice(self.peers)
        # push: send my newer entries; pull: ask for theirs
        newer = {k: v for k, v in self.state.items()
                 if self.state.get(k, (None, -1))[1] > peer.state.get(k, (None, -1))[1]}
        peer.merge(newer)
        newer_from_peer = {k: v for k, v in peer.state.items()
                           if peer.state.get(k, (None, -1))[1] > self.state.get(k, (None, -1))[1]}
        self.merge(newer_from_peer)

    def merge(self, entries):
        for k, (v, ver) in entries.items():
            if ver > self.state.get(k, (None, -1))[1]:
                self.state[k] = (v, ver)'''}},
            {'heading': 'Push, Pull, Push-Pull', 'paras': [
                'Push sends updates out; pull requests updates in; push-pull does both and converges fastest. Pull-only works when nodes are unreliable, push-only when updates are frequent. The exchange unit is a digest — checksums or version maps — so only the deltas travel.',
            ]},
        ],
        'practice': {
            'title': 'Converge the Cluster',
            'intro': 'A 100-node cluster must spread one configuration update to every node.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Simulate push gossip with fan-out 3; count rounds to full coverage.'},
                {'label': 'Task 2', 'text': 'Add pull and compare convergence on a cluster with 10% packet loss.'},
                {'label': 'Task 3', 'text': 'Design the version scheme that stops old updates from overwriting newer ones.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why gossip needs no coordinator. Start with a node failure.'},
            {'label': 'Compare & Contrast', 'text': 'Compare gossip with leader-based replication. When is epidemic dissemination the right choice?'},
            {'label': 'Boundary Testing', 'text': 'A node rejoins after a long partition with a stale state. Design the version and repair path that reconciles it.'},
        ],
        'takeaways': [
            'Gossip spreads state exponentially, coordinator-free',
            'Push, pull, and push-pull trade bandwidth for convergence',
            'Digests ensure only deltas travel',
            'Versioning prevents stale overwrites',
        ],
        'further': [
            {'title': 'Gossip Protocol — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Gossip_protocol'},
            {'title': 'SWIM: Scalable Weakly-consistent Infection-style Membership', 'url': 'https://www.cs.cornell.edu/~asdas/research/dsn02-SWIM.pdf'},
        ],
    },
    {
        'title': 'Gossip in Production: Membership and Clocks',
        'desc': 'SWIM, Cassandra, and DynamoDB — how real systems gossip about liveness and versioned state.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Describe SWIM membership',
            'Use version vectors and timestamps',
            'Handle flapping and suspicion',
            'Bound gossip bandwidth',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'SWIM Membership', 'paras': [
                'SWIM (Scalable Weakly-consistent Infection-style Membership) detects failures by pinging random nodes and asking them to ping others indirectly. A node is only marked dead after an accusation plus a confirmation round — suspicion windows absorb transient failures without flapping membership lists.',
            ], 'code': {'lang': 'go', 'body': '''
// SWIM-style membership: suspicion before removal
type Member struct {
    Addr    string
    State   MemberState   // Alive, Suspect, Dead
    Seq     uint64        // monotonically increasing membership epoch
    suspectSince time.Time
}
func (m *Member) isSuspectExpired(limit time.Duration) bool {
    return m.State == MemberStateSuspect &&
        time.Since(m.suspectSince) > limit
}
// A node is removed only after suspicion expires without ack.
// Accusations are gossiped; the accused defends by broadcasting alive.'''}},
            {'heading': 'Clocks and Versioning', 'paras': [
                'Gossiped values need causality tracking: wall clocks lie, so systems use version vectors or Lamport timestamps. When two nodes concurrently update the same key, the merge policy (last-writer-wins, or conflict resolution) must be explicit — Dynamo-style systems surface or merge conflicts deterministically.',
            ]},
        ],
        'practice': {
            'title': 'Design the Membership Layer',
            'intro': 'A 200-node cluster needs failure detection with no flapping during rolling restarts.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the suspicion window and the indirect-ping path.'},
                {'label': 'Task 2', 'text': 'Design the version vector for a replicated counter that two nodes increment concurrently.'},
                {'label': 'Task 3', 'text': 'Bound the gossip rate: how many bytes/second/node at 200 nodes, and how to cap it.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why suspicion beats instant removal for failure detection. Ask me what happens during a rolling deploy.'},
            {'label': 'Implementation Design', 'text': 'Design gossip for a 1000-node fleet with a 1MB/s/node bandwidth cap. What is gossiped, how often, and what is skipped?'},
            {'label': 'Boundary Testing', 'text': 'Two nodes increment the same counter concurrently. Design the merge (LWW vs vector-clock conflict) and the reconciliation path.'},
        ],
        'takeaways': [
            'SWIM uses suspicion and indirect pings for membership',
            'Suspicion absorbs transient failures without flapping',
            'Version vectors give causal ordering to gossiped state',
            'Gossip rate must be bounded at fleet scale',
        ],
        'further': [
            {'title': 'SWIM Paper', 'url': 'https://www.cs.cornell.edu/~asdas/research/dsn02-SWIM.pdf'},
            {'title': 'Cassandra Gossip', 'url': 'https://cassandra.apache.org/doc/stable/cassandra/architecture/gossip.html'},
        ],
    },
    {
        'title': 'Advanced Gossip: Sloppy Quorums and Anti-Entropy',
        'desc': 'Dynamo-style hinted handoff, read repair, anti-entropy, and gossip across partitions.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Explain hinted handoff',
            'Design read repair and anti-entropy',
            'Combine quorums with gossip',
            'Reconcile divergent replicas',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Sloppy Quorums and Hinted Handoff', 'paras': [
                'Dynamo-style systems accept writes on any healthy node when the home replicas are unreachable, then hand off the write later — hinted handoff. Gossip carries the hints. The trade: the system stays available under partition but trades strict consistency, relying on read repair and anti-entropy to converge afterward.',
            ], 'code': {'lang': 'go', 'body': '''
// Hinted handoff: stash for a down replica, deliver via gossip
type Hint struct {
    Key       string
    Value     []byte
    TargetID  string     // the replica that was down
    SourceID  string
}
func (n *Node) onWrite(key string, val []byte, replicas []string) {
    written := 0
    for _, r := range replicas {
        if err := n.client.Put(r, key, val); err == nil {
            written++
        } else {
            n.hints[r] = append(n.hints[r], Hint{key, val, r, n.id})
        }
    }
    if written < quorum {
        n.gossipHints()      // deliver hints when targets return
    }
}'''}},
            {'heading': 'Read Repair and Anti-Entropy', 'paras': [
                'Read repair compares replicas on every read and repairs stale ones. Anti-entropy runs continuously in the background, exchanging Merkle trees so divergent nodes find and fix differences without shipping full data. Together they pull a gossip system back to convergence after partitions.',
            ]},
        ],
        'practice': {
            'title': 'Converge After the Partition',
            'intro': 'A 5-node Dynamo-style ring splits for 5 minutes; writes land on isolated nodes via hints.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the hinted-handoff delivery and its retry policy.'},
                {'label': 'Task 2', 'text': 'Design read repair with a version comparison at read time.'},
                {'label': 'Task 3', 'text': 'Design the Merkle-tree anti-entropy that repairs the ring without a full sync.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain how hinted handoff keeps writes available during a partition and how anti-entropy heals afterward.'},
            {'label': 'Implementation Design', 'text': 'Design the merge rule for a key written on both sides of a partition with concurrent versions. Show the conflict-free or surfaced-conflict choice.'},
            {'label': 'Boundary Testing', 'text': 'A node returns from a week-long partition. Design the reconciliation that detects and repairs every divergent key.'},
        ],
        'takeaways': [
            'Hinted handoff keeps writes available through partitions',
            'Read repair fixes staleness on access',
            'Merkle anti-entropy finds divergence without full syncs',
            'Gossip systems converge but need explicit conflict policy',
        ],
        'further': [
            {'title': 'Dynamo Paper (sloppy quorums, hinted handoff)', 'url': 'https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf'},
            {'title': 'Cassandra — Read Repair', 'url': 'https://cassandra.apache.org/doc/stable/cassandra/operating/read_repair.html'},
        ],
    },
    {
        'title': 'Gossip: Review & Mastery Quiz',
        'desc': 'Scenario questions on dissemination, membership, and reconciliation.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate gossip concepts',
            'Choose dissemination strategies',
            'Design reconciliation',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Gossip spreads state? (A: via a coordinator / B: via random peer exchange / C: via a tree)',
                'Q2: The fastest-converging exchange style is? (A: push / B: pull / C: push-pull)',
                'Q3: SWIM marks a node dead only after? (A: one ping / B: suspicion + confirmation / C: admin action)',
                'Q4: True or false: hinted handoff keeps writes available during a partition.',
                'Q5: Anti-entropy uses? (A: Merkle trees / B: full copies / C: FTP)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A 500-node fleet loses 5 nodes during an upgrade. Design the gossip membership and reconciliation that keeps the fleet healthy.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why a coordinator-free epidemic protocol is more robust but eventually consistent.'},
        ],
        'takeaways': [
            'Q1: B; Q2: C; Q3: B; Q4: true; Q5: A',
            'Gossip is self-healing and coordinator-free',
            'Suspicion, hints, and anti-entropy keep it convergent',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# HASH INDEX
# ─────────────────────────────────────────────────────────────────────────────
_t('hash-index', [
    {
        'title': 'Hash Indexes: O(1) Point Lookups',
        'desc': 'Mapping a key to a fixed-size bucket so point lookups skip the scan entirely.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the hash index structure',
            'Handle collisions',
            'Understand the O(1) expected cost',
            'Know when a hash index fits',
        ],
        'prereqs': ['principles/optimistic-locking', 'patterns/b-tree'],
        'sections': [
            {'heading': 'The Structure', 'paras': [
                'A hash index applies a hash function to the key and uses the result as a bucket index. Point lookups (WHERE id = 42) are O(1) expected: hash, jump, scan the short bucket. Collisions — different keys in one bucket — degrade but stay near O(1) with good hashing and load factor control.',
            ], 'code': {'lang': 'sql', 'body': '''
-- Hash index: exact-equality lookups only
CREATE INDEX idx_users_email_hash ON users USING hash (email);

-- Uses the hash index: hash('a@b.com') -> bucket -> row
SELECT * FROM users WHERE email = 'a@b.com';

-- Does NOT use the hash index: range/order needs order (B-tree)
SELECT * FROM users WHERE email > 'a@b.com';
SELECT * FROM users ORDER BY email;'''}},
            {'heading': 'Hash vs B-Tree', 'paras': [
                'Hash indexes win on exact-equality point lookups and are excellent for primary keys. They cannot do ranges, ordering, or prefix scans — those need a B-tree. In-memory tables (Postgres hash, MySQL MEMORY) also use hash structures natively.',
            ]},
        ],
        'practice': {
            'title': 'Pick the Index Type',
            'intro': 'A session table is queried by session_id (exact) and by user_id with a time range.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Classify each query shape: point, range, or order.'},
                {'label': 'Task 2', 'text': 'Choose hash vs B-tree for each and justify.'},
                {'label': 'Task 3', 'text': 'Sketch the bucket layout for the hash index and the collision policy.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why a hash index cannot answer range queries. Start with the bucket math.'},
            {'label': 'Compare & Contrast', 'text': 'Compare hash indexes, B-trees, and LSM memtables for point lookups, ranges, and writes.'},
            {'label': 'Boundary Testing', 'text': 'A poor hash function clusters keys into one bucket. Design the load-factor trigger and rehash path.'},
        ],
        'takeaways': [
            'Hash indexes make point lookups O(1) expected',
            'Collisions handled by bucket chains and load factor',
            'No ranges, no ordering — B-tree for those',
            'Perfect for primary keys and equality joins',
        ],
        'further': [
            {'title': 'PostgreSQL — Hash Indexes', 'url': 'https://www.postgresql.org/docs/current/indexes-types.html'},
            {'title': 'Designing Data-Intensive Applications — Ch. 3', 'url': 'https://dataintensive.net/'},
        ],
    },
    {
        'title': 'Hash Indexes in Production: Partitioned Tables and Hashing Schemes',
        'desc': 'Hash-partitioned tables, consistent hashing on disk, and open addressing.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design hash partitioning',
            'Explain open addressing vs chaining',
            'Rehash without downtime',
            'Use hash joins',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Hash Partitioning', 'paras': [
                'Distributed databases partition by hash of the key so each partition holds a uniform slice: hash(key) % N routes writes and reads to one partition. The catch: adding a node rehashes nearly every key — which is why consistent hashing maps keys to a ring and only a fraction move per node.',
            ], 'code': {'lang': 'python', 'body': '''
# Consistent hashing: only a fraction of keys move on resize
import hashlib, bisect

class ConsistentHash:
    def __init__(self, vnodes=128):
        self.vnodes = vnodes
        self.ring = []       # sorted positions
        self.nodes = {}      # position -> node

    def _pos(self, key):
        return int.from_bytes(hashlib.md5(key.encode()).digest()[:8], 'big')

    def add_node(self, node):
        for i in range(self.vnodes):
            p = self._pos(f'{node}:{i}')
            bisect.insort(self.ring, p)
            self.nodes[p] = node

    def get(self, key):
        p = self._pos(key)
        i = bisect.bisect_left(self.ring, p) % len(self.ring)
        return self.nodes[self.ring[i]]

# Removing one node only remaps keys that hashed into its vnodes.'''}},
            {'heading': 'On-Disk Hashing', 'paras': [
                'Disk hash indexes use extendible or linear hashing to grow gracefully: buckets split instead of full rehash. Open addressing (probing) avoids chain pointers and is cache-friendlier in memory; chaining is simpler and resilient. Hash joins exploit exact-equality keys to pair buckets without sorting.',
            ]},
        ],
        'practice': {
            'title': 'Design the Shard Map',
            'intro': 'A 1B-row event table is sharded by event_id across 8 nodes and must grow to 12.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the hash function and vnode count for balanced shards.'},
                {'label': 'Task 2', 'text': 'Simulate the resize: how many keys move from 8 to 12 nodes with consistent hashing?'},
                {'label': 'Task 3', 'text': 'Design the routing table lookup and the dual-write during migration.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why naive mod-N hashing makes resharding painful and consistent hashing does not.'},
            {'label': 'Implementation Design', 'text': 'Design a hash-partitioned message queue: partition key, routing, and consumer assignment. What happens when a consumer dies?'},
            {'label': 'Boundary Testing', 'text': 'One shard gets 40% of traffic because keys are skewed. Design the key-salting strategy that balances load.'},
        ],
        'takeaways': [
            'Hash partitioning gives uniform data distribution',
            'Consistent hashing makes resize touch only a fraction',
            'Extendible/linear hashing grow on disk without full rehash',
            'Hash joins pair buckets without sorting',
        ],
        'further': [
            {'title': 'Consistent Hashing — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Consistent_hashing'},
            {'title': 'Cassandra — Partitioning', 'url': 'https://cassandra.apache.org/doc/stable/cassandra/architecture/partitioning.html'},
        ],
    },
    {
        'title': 'Advanced Hash Index: DynamoDB-Style and Hash-Range Keys',
        'desc': 'Composite hash-range keys, hot-key mitigation, and hash index internals under load.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Design hash-range composite keys',
            'Mitigate hot partitions',
            'Understand adaptive hashing',
            'Analyze hash index memory',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Hash-Range Keys', 'paras': [
                'DynamoDB-style tables use a hash key for partitioning and a sort key for ordering within the partition. This gives both the O(1) partition routing AND ordered access within a partition: WHERE hash = tenant AND sort BETWEEN. It is the workhorse for multi-tenant systems.',
            ], 'code': {'lang': 'python', 'body': '''
# Hash-range key design: partition by tenant, order by timestamp
#
#   partition key: tenant_id      (hash -> shard)
#   sort key:      created_at     (ordered within the shard)
#
# Query: all orders of tenant 42 in the last hour
#   WHERE tenant_id = 42 AND created_at > now() - 3600
#
# This is O(1) routing + a range scan inside one shard.
# Hot shard risk: a single huge tenant gets one shard's worth of
# throughput — hence key salting: tenant:shard, then query fan-out.'''}},
            {'heading': 'Hot Keys and Adaptive Hashing', 'paras': [
                'A single popular key (a viral post, a celebrity) concentrates traffic on one partition. Mitigations: cache the hot key in front of storage, salt the key across shards and query all, or let the system detect hot partitions and split them — adaptive hashing is the on-disk cousin that splits buckets under load.',
            ]},
        ],
        'practice': {
            'title': 'Design the Multi-Tenant Schema',
            'intro': 'A SaaS with 10,000 tenants, one with 40% of the events; queries are per-tenant time ranges.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the hash-range schema and the query shapes it serves.'},
                {'label': 'Task 2', 'text': 'Design hot-key mitigation for the 40% tenant without slowing the others.'},
                {'label': 'Task 3', 'text': 'Measure the fan-out cost of salted hot keys and tune the salt width.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why a hot key defeats a hash index and what salting does about it.'},
            {'label': 'Implementation Design', 'text': 'Design a feed system: hash key = user, sort key = timestamp, with read fan-out from followees. Where do hot users break the design?'},
            {'label': 'Boundary Testing', 'text': 'A shard fills to 90% capacity. Design the split, the routing-table update, and the dual-read window.'},
        ],
        'takeaways': [
            'Hash-range keys route by hash, order by sort key',
            'Hot keys need caching, salting, or adaptive splitting',
            'Multi-tenant schemas live or die by partition design',
            'Adaptive hashing grows buckets under load',
        ],
        'further': [
            {'title': 'DynamoDB — Partition Keys and Sort Keys', 'url': 'https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.PartitionKey.html'},
            {'title': 'Adaptive Hashing', 'url': 'https://en.wikipedia.org/wiki/Adaptive_hashing'},
        ],
    },
    {
        'title': 'Hash Indexes: Review & Mastery Quiz',
        'desc': 'Scenario questions on structure, partitioning, and hot keys.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate hash index concepts',
            'Design shards and keys',
            'Mitigate hot partitions',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: A hash index is O(1) for? (A: ranges / B: exact equality / C: ordering)',
                'Q2: Consistent hashing makes resharding touch? (A: everything / B: a fraction / C: nothing)',
                'Q3: A hot key concentrates traffic on? (A: one partition / B: all partitions / C: the coordinator)',
                'Q4: True or false: hash indexes support range scans.',
                'Q5: Hash-range keys order by? (A: hash value / B: sort key / C: arrival time)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A chat archive stores 10B messages sharded by conversation. Design the hash-range schema and the hot-conversation mitigation.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why an index choice must follow the query shape, not convention.'},
        ],
        'takeaways': [
            'Q1: B; Q2: B; Q3: A; Q4: false; Q5: B',
            'Hash for equality, B-tree for order',
            'Shard design is where hash indexes win or lose',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# INTERPRETER
# ─────────────────────────────────────────────────────────────────────────────
_t('interpreter', [
    {
        'title': 'Interpreter: A Grammar for Your Problem',
        'desc': 'Defining a language for a recurring problem and evaluating its sentences with a syntax tree.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the interpreter intent',
            'Model a grammar with an AST',
            'Evaluate expressions recursively',
            'Know when a DSL beats configuration',
        ],
        'prereqs': ['patterns/composite', 'patterns/visitor'],
        'sections': [
            {'heading': 'The Problem', 'paras': [
                'When business rules or queries recur in many shapes (filter expressions, pricing rules, search strings), hand-coding every combination is unmaintainable. The interpreter defines a small grammar, parses sentences into an abstract syntax tree, and evaluates the tree — new rules become new sentences, not new code.',
            ], 'code': {'lang': 'python', 'body': '''
# Interpreter: arithmetic expressions as an AST
class Expr:
    def eval(self, env): raise NotImplementedError

class Num(Expr):
    def __init__(self, v): self.v = v
    def eval(self, env): return self.v

class Add(Expr):
    def __init__(self, l, r): self.l, self.r = l, r
    def eval(self, env): return self.l.eval(env) + self.r.eval(env)

class Var(Expr):
    def __init__(self, name): self.name = name
    def eval(self, env): return env[self.name]

# (a + 5) + 10  ==  Add(Add(Var('a'), Num(5)), Num(10))
expr = Add(Add(Var('a'), Num(5)), Num(10))
print(expr.eval({'a': 2}))    # 17'''}},
            {'heading': 'Grammar and AST', 'paras': [
                'A grammar (E ::= E + E | number | variable) defines valid sentences; parsing turns text into the tree; evaluation walks it. The pattern shines for small, stable grammars. Large or evolving languages need a real parser generator or a full compiler pipeline instead.',
            ]},
        ],
        'practice': {
            'title': 'Build the Rule Engine',
            'intro': 'A pricing system needs rules like "if country == FR then price * 1.2" without redeploying.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the grammar for conditions and actions.'},
                {'label': 'Task 2', 'text': 'Build the parser and the AST nodes.'},
                {'label': 'Task 3', 'text': 'Evaluate a pricing rule against sample orders and add a new rule without code changes.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about how a grammar becomes an AST and the AST becomes an evaluation. Start with one operator.'},
            {'label': 'Compare & Contrast', 'text': 'Compare interpreter with strategy and with a configuration file. When is a DSL actually worth it?'},
            {'label': 'Boundary Testing', 'text': 'A rule references an unknown variable. Design the evaluation-time error and the validation pass that catches it before execution.'},
        ],
        'takeaways': [
            'Interpreter turns a grammar into an evaluable AST',
            'New behaviors become new sentences, not new code',
            'Evaluation is recursive tree walking',
            'Small stable grammars only — otherwise use a parser generator',
        ],
        'further': [
            {'title': 'Interpreter — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/interpreter'},
            {'title': 'Crafting Interpreters (free book)', 'url': 'https://craftinginterpreters.com/'},
        ],
    },
    {
        'title': 'Interpreter in Production: Query Languages and Rules Engines',
        'desc': 'Filter DSLs, search syntaxes, and workflow rules built on interpreters.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design a filter DSL',
            'Add validation and typing',
            'Sandbox the evaluator',
            'Compile hot paths',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Filter DSLs', 'paras': [
                'Products expose user-facing filter languages (Jira JQL, GitHub search, mail filters). A tokenizer + recursive-descent parser + typed evaluator is the classic interpreter pipeline. The evaluator runs against a context (the issue, the pull request) and returns a boolean — queries are data, not code.',
            ], 'code': {'lang': 'typescript', 'body': '''
// A tiny filter DSL: tag:urgent AND (priority:high OR age:old)
// Tokenize -> parse -> evaluate against a record
function evalFilter(ast: Node, ctx: Record<string, string[]>): boolean {
    switch (ast.kind) {
        case 'and': return evalFilter(ast.left, ctx) && evalFilter(ast.right, ctx);
        case 'or':  return evalFilter(ast.left, ctx) || evalFilter(ast.right, ctx);
        case 'field': {
            const vals = ctx[ast.name] ?? [];
            return ast.op === ':' ? vals.includes(ast.value) : true;
        }
    }
}
// The filter is stored as a string, parsed once, evaluated per item.
// New filter operators = new AST node + evaluator branch, both tested.'''}},
            {'heading': 'Validation and Sandboxing', 'paras': [
                'User-authored expressions must be validated before use (unknown fields, type mismatches) and evaluated safely: no side effects, bounded depth and time, and no access to the host environment. A billion-laughs-style deep expression must be depth-limited, and evaluation must be pure.',
            ]},
        ],
        'practice': {
            'title': 'Design the Search DSL',
            'intro': 'A support tool needs search like "status:open AND (assignee:me OR priority:high)".',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the grammar, tokens, and precedence.'},
                {'label': 'Task 2', 'text': 'Build the recursive-descent parser and evaluator.'},
                {'label': 'Task 3', 'text': 'Add validation (unknown fields) and depth limiting, then fuzz the parser.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me the pipeline: tokenize, parse, validate, evaluate. Ask me where each failure mode appears.'},
            {'label': 'Implementation Design', 'text': 'Design a workflow rules engine where rules are interpreted data. How do rules version, migrate, and get validated at deploy?'},
            {'label': 'Boundary Testing', 'text': 'A user submits a 10,000-token query. Design the limits (depth, tokens, time) and the error surface.'},
        ],
        'takeaways': [
            'Production interpreters power JQL-style filter DSLs',
            'Validation and sandboxing are mandatory for user input',
            'Pure evaluation keeps the interpreter safe',
            'Depth and time limits stop pathological expressions',
        ],
        'further': [
            {'title': 'Crafting Interpreters (free book)', 'url': 'https://craftinginterpreters.com/'},
            {'title': 'ANTLR (parser generator)', 'url': 'https://www.antlr.org/'},
        ],
    },
    {
        'title': 'Advanced Interpreter: Typing, Optimization, and Compilation',
        'desc': 'Static checking, tree-walking to bytecode, and JIT-style hot-path compilation.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Add a type-checking pass',
            'Compile the AST to bytecode',
            'Optimize hot evaluation paths',
            'Support incremental re-evaluation',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Beyond Tree Walking', 'paras': [
                'A plain tree-walking interpreter is simple but slow for hot paths. Compiling the AST to bytecode — linear instructions a stack machine executes — removes per-node dispatch overhead. Constant folding and common subexpression elimination shrink the instruction stream.',
            ], 'code': {'lang': 'python', 'body': '''
# Bytecode for Add(Add(Var('a'), Num(5)), Num(10))
#   LOAD_VAR a
#   PUSH 5
#   ADD
#   PUSH 10
#   ADD
# Executing a flat instruction list beats virtual dispatch on the AST.
def run(code, env):
    stack = []
    for op, arg in code:
        if op == 'LOAD_VAR': stack.append(env[arg])
        elif op == 'PUSH': stack.append(arg)
        elif op == 'ADD': stack.append(stack.pop() + stack.pop())
    return stack[0]'''}},
            {'heading': 'Typing and Incremental Evaluation', 'paras': [
                'A static pass checks types before evaluation: unknown fields, mismatched operators, impossible comparisons. Incremental evaluation re-runs only the affected sub-expressions when inputs change — the engine keeps per-node caches and invalidates along the path to the root, which matters when rules evaluate against thousands of changing records.',
            ]},
        ],
        'practice': {
            'title': 'Compile the Filter',
            'intro': 'A rules engine evaluates 1M rules/minute against streaming events and is CPU-bound.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Compile the AST to a flat instruction list and benchmark against tree walking.'},
                {'label': 'Task 2', 'text': 'Add constant folding for static sub-expressions.'},
                {'label': 'Task 3', 'text': 'Design incremental re-evaluation when only some event fields change.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why bytecode beats tree walking for hot interpreters.'},
            {'label': 'Implementation Design', 'text': 'Design a rule engine that type-checks rules at deploy time and compiles them to bytecode. What are the deploy-time checks?'},
            {'label': 'Boundary Testing', 'text': 'A rule is correct on Monday but the data schema changes Tuesday. Design the schema-versioned type check and the fail-deploy path.'},
        ],
        'takeaways': [
            'Bytecode compilation removes AST dispatch overhead',
            'Type checking moves errors from runtime to deploy',
            'Constant folding shrinks the instruction stream',
            'Incremental evaluation saves work on changing inputs',
        ],
        'further': [
            {'title': 'Crafting Interpreters — Chunks of Bytecode', 'url': 'https://craftinginterpreters.com/a-bytecode-virtual-machine.html'},
            {'title': 'Expression rules engines — Drools', 'url': 'https://www.drools.org/'},
        ],
    },
    {
        'title': 'Interpreter: Review & Mastery Quiz',
        'desc': 'Scenario questions on grammars, evaluation, and optimization.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate interpreter concepts',
            'Design DSLs and grammars',
            'Optimize evaluation',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: An interpreter evaluates? (A: a parse tree / B: compiled binaries / C: YAML only)',
                'Q2: New rules in a DSL mean? (A: new code / B: new sentences / C: new servers)',
                'Q3: User-authored expressions must be? (A: sandboxed / B: trusted / C: ignored)',
                'Q4: True or false: bytecode beats tree walking on hot paths.',
                'Q5: Type checking at parse time moves errors to? (A: deploy time / B: runtime / C: users)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A support tool needs a query language over tickets. Design the grammar, the evaluator, and the sandbox limits.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer when a DSL is worth building and when a config file is enough.'},
        ],
        'takeaways': [
            'Q1: A; Q2: B; Q3: A; Q4: true; Q5: A',
            'Interpreter = grammar + AST + evaluator',
            'Validate, sandbox, then compile hot paths',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# ITERATOR
# ─────────────────────────────────────────────────────────────────────────────
_t('iterator', [
    {
        'title': 'Iterator: Walk a Collection Without Its Layout',
        'desc': 'Sequential access to elements without exposing the underlying structure or its traversal rules.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the iterator intent',
            'Separate traversal from the collection',
            'Use lazy iteration',
            'Implement a custom iterator',
        ],
        'prereqs': ['patterns/composite', 'patterns/visitor'],
        'sections': [
            {'heading': 'The Problem', 'paras': [
                'A tree, a linked list, and a filtered view are traversed differently. If callers must know the layout to walk it, every change to the collection breaks every caller. The iterator exposes one protocol — next() / has_next() — so traversal logic lives with the collection and callers stay layout-agnostic.',
            ], 'code': {'lang': 'python', 'body': '''
# Iterator: lazy traversal with a generator
class Node:
    def __init__(self, v, left=None, right=None):
        self.v, self.left, self.right = v, left, right

def inorder(root):                      # the traversal, owned here
    if root is None:
        return
    yield from inorder(root.left)
    yield root.v
    yield from inorder(root.right)

tree = Node(2, Node(1), Node(3))
print(list(inorder(tree)))              # [1, 2, 3] — caller knows nothing'''}},
            {'heading': 'Lazy and Compositional', 'paras': [
                'Iterators are lazy: each element is produced on demand, so infinite sequences and streaming pipelines are possible. Because iterators compose (map, filter, chain), whole data pipelines become declarative — the essence of generators in Python, iterators in Rust, and streams in Java.',
            ]},
        ],
        'practice': {
            'title': 'Hide the Traversal',
            'intro': 'A document model is a tree of paragraphs and sections; the word-count tool must walk it in order.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Implement an iterator over the document tree without exposing nodes.'},
                {'label': 'Task 2', 'text': 'Add a filtered iterator (only paragraphs) by composition.'},
                {'label': 'Task 3', 'text': 'Rewrite the word-count tool to use only the iterator API.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why lazy iteration enables infinite sequences. Start with where the state lives.'},
            {'label': 'Compare & Contrast', 'text': 'Compare iterator with visitor: one walks, the other performs operations per element. When does each fit?'},
            {'label': 'Boundary Testing', 'text': 'A caller mutates the collection mid-iteration. Design the fail-fast or snapshot policy that prevents silent corruption.'},
        ],
        'takeaways': [
            'Iterators decouple traversal from collection layout',
            'Lazy generation enables streaming and infinite sequences',
            'Iterators compose into declarative pipelines',
            'Mutation during iteration needs a defined policy',
        ],
        'further': [
            {'title': 'Iterator — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/iterator'},
            {'title': 'Iterators in Python — official docs', 'url': 'https://docs.python.org/3/library/stdtypes.html#iterator-types'},
        ],
    },
    {
        'title': 'Iterator in Production: Streams, Paging, and Cursors',
        'desc': 'Database cursors, API paging, and event streams as iterators.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design cursor-based paging',
            'Stream results without loading all',
            'Handle iterator invalidation',
            'Combine iterators in pipelines',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Cursors and Paging', 'paras': [
                'Database cursors and API pagination are iterators over an implicit result set: fetch a page, get the next token, continue. Cursor-based paging (WHERE id > last_seen ORDER BY id LIMIT 50) stays stable under concurrent inserts, unlike offset paging, which skips and duplicates rows.',
            ], 'code': {'lang': 'go', 'body': '''
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
}'''}},
            {'heading': 'Streaming and Invalidation', 'paras': [
                'Streaming consumers read rows one at a time, never materializing the whole result — the iterator is a window over an open cursor. Invalidation is the classic hazard: a long-lived iterator over a changing table may see a consistent snapshot (MVCC) or fail fast (a version check on each step).',
            ]},
        ],
        'practice': {
            'title': 'Design the Pagination',
            'intro': 'A feed API returns posts ordered by created_at; users scroll for thousands of items while new posts arrive.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design cursor paging (cursor = created_at,id pair) that survives new inserts.'},
                {'label': 'Task 2', 'text': 'Implement the streaming consumer that stops at a max row count.'},
                {'label': 'Task 3', 'text': 'Test the offset-paging duplicate/skip bugs to prove the cursor design.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why cursor paging beats offset paging on a live table. Ask me to show the failing case.'},
            {'label': 'Implementation Design', 'text': 'Design a Kafka-style consumer as an iterator: position, commit, and rebalance. What does the iterator protocol look like?'},
            {'label': 'Boundary Testing', 'text': 'A page request arrives with a stale cursor from a deleted page. Design the error and the restart contract.'},
        ],
        'takeaways': [
            'Cursors make paging stable under concurrent writes',
            'Streaming iterators never materialize full results',
            'Iterator invalidation needs a defined policy',
            'Pipelines compose iterators into stages',
        ],
        'further': [
            {'title': 'PostgreSQL — Cursors', 'url': 'https://www.postgresql.org/docs/current/plpgsql-cursors.html'},
            {'title': 'REST API pagination best practices', 'url': 'https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#pagination'},
        ],
    },
    {
        'title': 'Advanced Iterator: Internal Iteration and Parallel Traversal',
        'desc': 'Internal iteration (map/filter), parallel iteration, and iterator adapters.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Distinguish external vs internal iteration',
            'Parallelize iteration safely',
            'Design iterator adapters',
            'Reason about iterator complexity',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'External vs Internal', 'paras': [
                'External iteration is caller-driven: next(), with the loop in the caller. Internal iteration is structure-driven: for_each/map, with the loop inside the collection. Internal iteration lets the collection control order, concurrency, and short-circuiting; Rust iterators and Java streams are internal with lazy adapters.',
            ], 'code': {'lang': 'rust', 'body': '''
// Rust: lazy internal iteration, parallelizable with rayon
let nums: Vec<i64> = (0..1_000_000).collect();

let sum_of_squares: i64 = nums.iter()      // lazy chain
    .map(|n| n * n)
    .filter(|sq| sq % 2 == 0)
    .take(100)
    .sum();

// Parallel: same pipeline, data-parallel execution
use rayon::prelude::*;
let par_sum: i64 = nums.par_iter()
    .map(|n| n * n)
    .sum();
// The iterator abstracts both the layout AND the execution model.'''}},
            {'heading': 'Parallelism and Adapters', 'paras': [
                'Parallel iterators split the source, fan out, and merge — but the merge must respect ordering or document its absence. Adapters (map, filter, flat_map, take, zip) are lazy and fusion-optimizable: a compiler or runtime can collapse chains into a single pass, which is why iterator pipelines are both expressive and fast.',
            ]},
        ],
        'practice': {
            'title': 'Parallelize the Pipeline',
            'intro': 'A 10M-row transformation pipeline (parse, validate, enrich, aggregate) is single-threaded.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Convert to a parallel iterator and measure speedup at 4 and 8 cores.'},
                {'label': 'Task 2', 'text': 'Identify the order-sensitive stage and enforce ordering at the merge.'},
                {'label': 'Task 3', 'text': 'Benchmark fusion: one pass vs intermediate allocations.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain the difference between caller-driven and structure-driven iteration and why the latter enables parallelism.'},
            {'label': 'Implementation Design', 'text': 'Design a streaming ETL as iterator adapters with a bounded buffer. Where does backpressure live?'},
            {'label': 'Boundary Testing', 'text': 'A parallel merge reorders output. Design the ordering guarantee or the documented contract when it is dropped.'},
        ],
        'takeaways': [
            'Internal iteration moves control into the collection',
            'Parallel iterators split, compute, and merge',
            'Adapters compose lazily and fuse into one pass',
            'Ordering at the merge is an explicit contract',
        ],
        'further': [
            {'title': 'Rust — Iterator trait', 'url': 'https://doc.rust-lang.org/std/iter/trait.Iterator.html'},
            {'title': 'Rayon — data parallelism', 'url': 'https://docs.rs/rayon/latest/rayon/'},
        ],
    },
    {
        'title': 'Iterator: Review & Mastery Quiz',
        'desc': 'Scenario questions on traversal, paging, and parallelism.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate iterator concepts',
            'Design paging and streams',
            'Parallelize pipelines',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: An iterator decouples? (A: traversal from layout / B: storage from memory / C: users from admins)',
                'Q2: Cursor paging is stable under? (A: concurrent writes / B: schema changes / C: restarts)',
                'Q3: Lazy iterators enable? (A: infinite sequences / B: eager loading / C: recursion only)',
                'Q4: True or false: internal iteration lets the collection control concurrency.',
                'Q5: Offset paging on a live table causes? (A: duplicates and skips / B: corruption / C: nothing)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A timeline API must page stably while users post constantly. Design the cursor and the iterator protocol.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why iteration logic should live with the collection, not the callers.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Iterators abstract traversal and enable streaming',
            'Cursors and parallel adapters scale them',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# LEADER-FOLLOWER
# ─────────────────────────────────────────────────────────────────────────────
_t('leader-follower', [
    {
        'title': 'Leader-Follower: One Node Writes, All Read',
        'desc': 'A single authoritative replica accepts writes; followers replicate and serve reads.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the leader-follower model',
            'Describe replication flow',
            'Understand read scaling',
            'Know the single-writer guarantee',
        ],
        'prereqs': ['patterns/replication', 'patterns/paxos'],
        'sections': [
            {'heading': 'The Model', 'paras': [
                'One leader accepts all writes and appends them to a log; followers stream the log and apply it, staying behind the leader by a replication lag. Reads can go anywhere — but reads from a follower may be stale by that lag. This is the workhorse of Postgres, MySQL, and most databases.',
            ], 'code': {'lang': 'python', 'body': '''
# Leader-follower replication: log shipping with position tracking
class Leader:
    def __init__(self):
        self.log = []                 # every write appended here
        self.position = 0

    def write(self, op):
        self.log.append(op)
        self.position += 1
        return self.position

class Follower:
    def __init__(self, leader):
        self.leader = leader
        self.applied = 0

    def poll(self):
        while self.applied < self.leader.position:   # stream the log
            op = self.leader.log[self.applied]
            self.apply(op)
            self.applied += 1

    def apply(self, op):
        print(f'follower applied: {op}')'''}},
            {'heading': 'Consistency Trade-Off', 'paras': [
                'The leader guarantees a total write order; followers are eventually consistent with it. Read-after-write needs routing: read your own writes from the leader, everything else from any replica. Replication lag breaks monotonic reads if the same user reads two followers at different positions.',
            ]},
        ],
        'practice': {
            'title': 'Route the Reads',
            'intro': 'A forum app: 95% reads, 5% writes; users must always see their own posts.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the routing rule: which reads go to the leader, which to followers?'},
                {'label': 'Task 2', 'text': 'Model the replication lag and its effect on a user reading two replicas.'},
                {'label': 'Task 3', 'text': 'Design the read-your-writes guarantee with a session pin.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about where reads go and what lag means for users. Start with read-your-writes.'},
            {'label': 'Compare & Contrast', 'text': 'Compare leader-follower with multi-leader and leaderless (quorum) replication. When is single-writer the right call?'},
            {'label': 'Boundary Testing', 'text': 'A follower lags 30 seconds and serves stale prices during a sale. Design the staleness guard (max lag routing) that protects users.'},
        ],
        'takeaways': [
            'One leader serializes writes; followers scale reads',
            'Followers replicate via a streamed log',
            'Replication lag = read staleness',
            'Read-your-writes needs session-aware routing',
        ],
        'further': [
            {'title': 'Replication — Designing Data-Intensive Applications, Ch. 5', 'url': 'https://dataintensive.net/'},
            {'title': 'PostgreSQL — Streaming Replication', 'url': 'https://www.postgresql.org/docs/current/warm-standby.html'},
        ],
    },
    {
        'title': 'Leader-Follower in Production: Failover and Lag',
        'desc': 'Automatic failover, lag monitoring, and safe promotion.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design leader failover',
            'Monitor replication lag',
            'Promote a follower safely',
            'Handle split-brain',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Failover', 'paras': [
                'When the leader dies, a follower promotes. The window between the last acked write on the old leader and the promoted follower position determines data loss — sync replication narrows it, async replication risks it. Failover must be triggered carefully: a delayed leader returning and still accepting writes splits the brain.',
            ], 'code': {'lang': 'yaml', 'body': '''
# Failover decision inputs (high-level):
#   leader_heartbeat: last seen leader heartbeat
#   follower_lag:     position delta to the candidate
#   quorum:           majority of nodes agree the leader is gone
#
# Promote only if:
#   - leader heartbeat expired > threshold
#   - candidate lag is acceptable for the data-loss budget
#   - majority quorum confirms leadership is vacant
# Split-brain guard: the old leader must fence (lose quorum) before
# the new leader accepts writes — typically via a shared lock/epoch.'''}},
            {'heading': 'Lag as a First-Class Signal', 'paras': [
                'Replication lag is the top operational risk of leader-follower. Track it per replica; route reads away from replicas past a threshold; alert when lag grows. Sync replication trades write latency for zero-loss failover; semi-sync (one sync replica) is the common middle ground.',
            ]},
        ],
        'practice': {
            'title': 'Design the Failover Runbook',
            'intro': 'A 3-node Postgres cluster with async replication must fail over in under 60 seconds.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the failure detection, the lag budget, and the promotion order.'},
                {'label': 'Task 2', 'text': 'Design the fencing that prevents the old leader from accepting writes.'},
                {'label': 'Task 3', 'text': 'Write the verification checklist for a safe promotion and the rollback path.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me the failover trade-off: async replication speed vs the loss window. Ask me to quantify it.'},
            {'label': 'Implementation Design', 'text': 'Design semi-sync replication: the leader waits for one follower before acking. What is the write latency cost and the loss guarantee?'},
            {'label': 'Boundary Testing', 'text': 'The old leader survives a partition and a new leader is promoted. Design the fencing that prevents two writers.'},
        ],
        'takeaways': [
            'Failover trades the ack window for loss risk',
            'Fencing prevents the split-brain double leader',
            'Lag must be monitored and routed around',
            'Semi-sync balances latency and durability',
        ],
        'further': [
            {'title': 'Patroni — Postgres HA', 'url': 'https://patroni.readthedocs.io/'},
            {'title': 'Replication — DDIA Ch. 5', 'url': 'https://dataintensive.net/'},
        ],
    },
    {
        'title': 'Advanced Leader-Follower: Multi-Leader and the Raft Connection',
        'desc': 'Multi-leader topologies, conflict resolution, and how Raft operationalizes leadership.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Explain multi-leader topologies',
            'Resolve concurrent writes',
            'Compare with Raft consensus',
            'Design conflict-free data models',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Multi-Leader', 'paras': [
                'Multi-leader has several leaders, each accepting writes and shipping to the others — used for multi-datacenter locality and offline-first apps. The cost is write conflicts: two leaders accept the same key concurrently. Conflict resolution (LWW, CRDTs, custom merge) must be deterministic or user-facing.',
            ], 'code': {'lang': 'typescript', 'body': '''
// LWW (last-writer-wins) merge: simple, but loses updates
function merge(a: {v: string; ts: number}, b: {v: string; ts: number}) {
    return a.ts >= b.ts ? a : b;
}
// CRDT (G-Counter): merges by taking the max of every replica counter
//   - no lost updates, no coordinator, deterministic convergence
//   - counter = [replica0, replica1, ...]; value = sum; merge = elementwise max
// Choose: LWW for logs, CRDTs for counters/sets, custom for domain merges.'''}},
            {'heading': 'Raft as Leader-Follower', 'paras': [
                'Raft is leader-follower with consensus: the leader is elected, holds a term/epoch, and replicates through a log with quorum acks. Raft solves the failover problem leader-follower leaves open — a new leader can only be elected with a majority, and old leaders are fenced by term. Most databases borrow Raft for exactly this.',
            ]},
        ],
        'practice': {
            'title': 'Choose the Topology',
            'intro': 'A notes app must work offline and sync; a billing system must never double-charge.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the offline-first multi-leader sync with a CRDT for the notes.'},
                {'label': 'Task 2', 'text': 'Design the single-leader billing path and why it must not be multi-leader.'},
                {'label': 'Task 3', 'text': 'Compare the two designs: where does conflict resolution live in each?'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why multi-leader needs conflict resolution and single-leader does not.'},
            {'label': 'Implementation Design', 'text': 'Design a shopping cart that syncs across devices with a CRDT. What is the merge rule for add and remove?'},
            {'label': 'Boundary Testing', 'text': 'LWW loses a critical update because clocks skew. Design the hybrid logical clock that fixes the ordering.'},
        ],
        'takeaways': [
            'Multi-leader adds locality at the cost of conflicts',
            'Conflict resolution must be deterministic or surfaced',
            'Raft is leader-follower made consensus-safe',
            'Some workloads must never be multi-leader',
        ],
        'further': [
            {'title': 'CRDTs — an introduction', 'url': 'https://crdt.tech/'},
            {'title': 'Raft Paper', 'url': 'https://raft.github.io/raft.pdf'},
        ],
    },
    {
        'title': 'Leader-Follower: Review & Mastery Quiz',
        'desc': 'Scenario questions on replication, failover, and conflicts.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate leader-follower concepts',
            'Design failover',
            'Resolve conflicts',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: In leader-follower, writes go to? (A: the leader / B: any follower / C: all nodes)',
                'Q2: Reads from followers may be? (A: stale / B: faster than the leader / C: impossible)',
                'Q3: Split-brain is prevented by? (A: fencing / B: backups / C: caching)',
                'Q4: True or false: multi-leader replication needs conflict resolution.',
                'Q5: Raft elects a leader with? (A: a majority quorum / B: a coin flip / C: admin action)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A global e-commerce site needs writes near users and zero double-spends. Design the hybrid: multi-leader carts, single-leader payments.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why the replication lag is the price of read scaling.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Single writer, many readers, explicit lag policy',
            'Failover and conflicts are the two hard problems',
        ],
    },
])
