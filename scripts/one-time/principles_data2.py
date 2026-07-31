#!/usr/bin/env python3
"""Deep curriculum data chunk 2: bulkhead, caching, cap-theorem, circuit-breaker."""

TOPICS = {}


def _t(slug, topics):
    TOPICS[slug] = topics
    return topics


# ─────────────────────────────────────────────────────────────────────────────
# BULKHEAD
# ─────────────────────────────────────────────────────────────────────────────
_t('bulkhead', [
    {
        'title': 'Bulkheads: Isolating Failure Domains',
        'desc': 'Why one slow component should never sink the whole ship — and how to partition resources.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the bulkhead pattern as failure isolation',
            'Partition thread pools, connections, and memory',
            'Design per-dependency resource budgets',
            'Recognize shared-resource coupling in a system diagram',
        ],
        'prereqs': ['principles/circuit-breaker', 'principles/graceful-degradation'],
        'sections': [
            {'heading': 'The Shared-Pool Trap', 'paras': [
                'A single shared thread pool looks efficient: one pool for all HTTP calls, database calls, and cache calls. But when the database slows down, its queued tasks occupy every thread, and HTTP requests begin to time out — a cascade across all services.',
                'Bulkheads partition resources per dependency (or per tenant) so that one failing or slow dependency can only exhaust its own budget. The term comes from ship design: a hull is divided into compartments so a breach floods only one.',
            ], 'code': {'lang': 'java', 'body': '''
// Per-dependency thread pools instead of one shared pool
ExecutorService dbPool   = Executors.newFixedThreadPool(10);  // DB calls
ExecutorService cachePool = Executors.newFixedThreadPool(5);  // cache calls
ExecutorService httpPool  = Executors.newFixedThreadPool(20); // outbound HTTP

// A slow DB now blocks only its own 10 threads; HTTP still works
Future<Row> row = dbPool.submit(() -> db.query(sql));'''}},
            {'heading': 'Resource Budgets Per Tenant', 'paras': [
                'In multi-tenant systems, one noisy tenant can exhaust shared queues. Per-tenant semaphores, rate limits, and connection limits keep a single tenant from degrading the platform for everyone.',
                'Bulkheads do not prevent the failure; they contain it. Pair them with timeouts and circuit breakers so contained failures heal quickly.',
            ]},
        ],
        'practice': {
            'title': 'Redesign a Monolithic Pool',
            'intro': 'A service handles payments, search, and image uploads through one 100-thread pool. Search backend starts failing with 2s latency.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Split into three pools sized by expected load and SLA. Justify sizes.'},
                {'label': 'Task 2', 'text': 'Add per-pool queue bounds and rejection policy (what happens when payments pool is full?).'},
                {'label': 'Task 3', 'text': 'Add a circuit breaker around the search pool so it stops wasting threads on a dead backend.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time to help me reason about when a shared pool is acceptable and when it must be partitioned. Start with the failure cascade mechanics.'},
            {'label': 'Compare & Contrast', 'text': 'Contrast bulkheads with circuit breakers and rate limiting. Which prevents the flood, which contains the flood, and which heals the source?'},
            {'label': 'Boundary Testing', 'text': 'A bulkhead isolates per tenant but the largest tenant is 40% of traffic. Design a sizing rule that still protects small tenants during the large one\'s failure.'},
        ],
        'takeaways': [
            'Shared pools turn one slow dependency into a full outage',
            'Bulkheads partition resources so failures stay contained',
            'Pair bulkheads with timeouts and circuit breakers',
            'Per-tenant budgets protect the platform from noisy neighbors',
        ],
        'further': [
            {'title': 'Bulkhead Pattern — Microsoft Docs', 'url': 'https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead'},
            {'title': 'Release It! (Michael Nygard)', 'url': 'https://pragprog.com/titles/mnee2/release-it-second-edition/'},
        ],
    },
    {
        'title': 'Bulkheads in Production Systems',
        'desc': 'Thread pools, connection pools, and process-level isolation in real architectures.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Apply bulkheads to database and HTTP connection pools',
            'Use process/instance isolation for the strongest bulkhead',
            'Size pools from real latency and throughput data',
            'Combine bulkheads with backpressure correctly',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Connection Pools as Bulkheads', 'paras': [
                'Database connection pools are the most common bulkhead: a bounded pool per datasource. If one database dies, its pool drains (or errors fast) while other datasources keep serving.',
                'Never share one connection pool across a hot path and a batch path — the batch job will starve the hot path of connections.',
            ], 'code': {'lang': 'go', 'body': '''
// Separate pools per dependency in Go
var dbPool = make(chan struct{}, 20)      // DB: 20 concurrent
var cachePool = make(chan struct{}, 10)   // Cache: 10 concurrent

func queryDB(q string) (Row, error) {
    dbPool <- struct{}{}                  // acquire ticket
    defer func() { <-dbPool }()           // release ticket
    return db.QueryRow(q)
}'''}},
            {'heading': 'Instance-Level Bulkheads', 'paras': [
                'The strongest bulkhead is a separate process or deployment: an ML-scoring service that OOMs cannot take down the API that calls it. This trades cost for isolation.',
                'Microservices are, in part, an exercise in bulkheading at the process level — each service is a compartment with its own memory, CPU, and lifecycle.',
            ]},
        ],
        'practice': {
            'title': 'Size the Pools',
            'intro': 'You have 4 core services: checkout (60 RPS), search (200 RPS), recommendations (50 RPS), image resize (10 RPS). Each downstream call takes ~80ms p95.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Use Little\'s Law (concurrency = rate × latency) to size each pool.'},
                {'label': 'Task 2', 'text': 'Add 30% headroom and explain the trade-off between isolation and cost.'},
                {'label': 'Task 3', 'text': 'Decide which dependency deserves its own deployment and why.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why Little\'s Law dictates pool sizing and what happens when concurrency exceeds pool capacity. Ask me to compute examples.'},
            {'label': 'Implementation Design', 'text': 'Design bulkheads for a lambda/serverless architecture where there are no long-lived pools. How do you isolate there?'},
            {'label': 'Boundary Testing', 'text': 'A memory-cache failure now floods the database because the cache miss path has no pool. Where do you add the bulkhead?'},
        ],
        'takeaways': [
            'Connection pools are cheap, effective bulkheads',
            'Never share a pool between hot and batch paths',
            'Separate deployments give the strongest isolation',
            'Pool sizes come from Little\'s Law, not guesses',
        ],
        'further': [
            {'title': 'Little\'s Law and Pool Sizing', 'url': 'https://en.wikipedia.org/wiki/Little%27s_law'},
            {'title': 'Hystrix Thread Pools', 'url': 'https://github.com/Netflix/Hystrix/wiki/How-it-Works'},
        ],
    },
    {
        'title': 'Advanced Bulkheads: Semaphores, Shards, and Autonomy',
        'desc': 'Semaphore isolation, shard-level bulkheads, and designing systems that degrade autonomously.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Use semaphores for in-process isolation without queue overhead',
            'Bulkhead by shard, region, and tenant',
            'Design autonomous degradation for each compartment',
            'Avoid common bulkhead mis-sizings',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Semaphores vs Queues', 'paras': [
                'A semaphore only limits concurrency — callers that cannot acquire fail fast. A bounded queue adds waiting, which can hide failures and add latency. For low-latency paths, semaphores beat queues: fail fast and let the caller decide.',
            ], 'code': {'lang': 'java', 'body': '''
// Semaphore: fail fast instead of queueing
Semaphore searchPermits = new Semaphore(10);

Result search(String q) throws Exception {
    if (!searchPermits.tryAcquire(50, TimeUnit.MILLISECONDS)) {
        return Result.stale();   // degrade: serve cached, not queued
    }
    try {
        return searchBackend.search(q);
    } finally {
        searchPermits.release();
    }
}'''}},
            {'heading': 'Shard-Level Bulkheads', 'paras': [
                'Data-sharded systems get natural bulkheads per shard: a slow shard only hurts requests routed to it. The pattern generalizes to regions (one AZ\'s failure contained) and to leader-election scopes.',
                'Autonomy means each compartment has its own fallback: cached data, default values, or a degraded mode — so it keeps working while its neighbor recovers.',
            ]},
        ],
        'practice': {
            'title': 'Design Autonomous Degradation',
            'intro': 'A checkout service depends on payments, inventory, and promotions. Payments goes down.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define a degraded checkout mode that still works (e.g., record order, process payment later). What data does it need locally?'},
                {'label': 'Task 2', 'text': 'Draw the bulkheads and fallbacks for each dependency.'},
                {'label': 'Task 3', 'text': 'Design the recovery flow: how queued payments reconcile once the provider returns?'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why queueing inside a bulkhead defeats its purpose and when queuing is still correct.'},
            {'label': 'Implementation Design', 'text': 'Design a multi-AZ system where each AZ is a bulkhead and a full AZ loss keeps the system serving. What must be replicated per AZ?'},
            {'label': 'Boundary Testing', 'text': 'A bulkhead is sized for 10% of traffic but a viral launch sends 50% to one shard. Design overload behavior that contains the blast radius.'},
        ],
        'takeaways': [
            'Semaphores fail fast; queues hide failure with latency',
            'Shards, regions, and tenants are natural bulkheads',
            'Each compartment needs an autonomous degraded mode',
            'Sizing must include headroom for traffic skew',
        ],
        'further': [
            {'title': 'Netflix Hystrix Isolation Strategies', 'url': 'https://github.com/Netflix/Hystrix/wiki/How-it-Works#isolation'},
            {'title': 'Chaos Engineering Principles', 'url': 'https://principlesofchaos.org/'},
        ],
    },
    {
        'title': 'Bulkheads: Review & Mastery Quiz',
        'desc': 'Scenario questions on failure isolation, pool sizing, and autonomous degradation.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate isolation concepts',
            'Apply bulkhead reasoning to new systems',
            'Spot shared-resource coupling quickly',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: A slow database exhausts the shared pool. What is the first symptom? (A: DB timeouts / B: HTTP timeouts across the service / C: cache miss)',
                'Q2: What does a semaphore do that a bounded queue does not? (A: fail fast / B: buffer / C: retry)',
                'Q3: Little\'s Law states concurrency = ? (A: rate × latency / B: rate / latency / C: latency / rate)',
                'Q4: True or false: a separate deployment is a valid, strong bulkhead.',
                'Q5: The strongest protection against a noisy tenant is? (A: bigger shared pool / B: per-tenant budget / C: retries)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A recommendation service OOMs during a spike and takes down the home page. Redesign with bulkheads so the home page serves without recommendations.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "we can just add more threads to the shared pool" is a trap, using a concrete failure story.'},
        ],
        'takeaways': [
            'Q1: B; Q2: A; Q3: A; Q4: true; Q5: B',
            'Isolation is about containing, not preventing, failure',
            'Every compartment needs its own budget and fallback',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# CACHING
# ─────────────────────────────────────────────────────────────────────────────
_t('caching', [
    {
        'title': 'Caching: Speed by Storing Computed Answers',
        'desc': 'Why caching is the highest-leverage performance tool and how it can also corrupt behavior.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain cache hit rates and why they matter',
            'Choose cache placement (client, CDN, in-memory, distributed)',
            'Set TTLs and invalidation strategies',
            'Identify cache-related consistency bugs',
        ],
        'prereqs': ['principles/base', 'principles/eventual-consistency'],
        'sections': [
            {'heading': 'The Cache Hierarchy', 'paras': [
                'Caches live at every layer: browser, CDN, reverse proxy, application memory, and distributed stores like Redis. Each layer trades staleness for latency. The hottest data sits closest to the user; the source of truth sits farthest.',
                'A hit ratio of 99% for a hot endpoint means 100x fewer expensive queries — caching is usually the first and cheapest scaling lever.',
            ], 'code': {'lang': 'text', 'body': '''
latency pyramid (typical p50):
  CPU L1            ~1ns        (hardware)
  RAM               ~100ns      (in-process dict)
  Redis / Memcached ~1ms        (distributed cache)
  Database          ~5-20ms     (source of truth)
  Network + render  ~100ms+     (uncached path)'''}},
            {'heading': 'Consistency vs Speed', 'paras': [
                'Every cache introduces staleness. The engineering question is not "is it stale?" but "is the staleness bounded and acceptable?" TTLs bound staleness by time; invalidation bounds it by event; versioning bounds it by logic.',
            ]},
        ],
        'practice': {
            'title': 'Pick the Cache Layer',
            'intro': 'Profile page: 1M reads/day, read-heavy, changes rarely. Product page: changes on price updates. Checkout: must be current.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Assign a cache layer and TTL to each page type and justify.'},
                {'label': 'Task 2', 'text': 'For the product page, design cache invalidation on price change (event-based, not TTL-only).'},
                {'label': 'Task 3', 'text': 'Explain why checkout must bypass cache entirely.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about the trade-off between TTL length and consistency for a news feed. Start with hit ratio.'},
            {'label': 'Compare & Contrast', 'text': 'Compare write-through, write-around, and write-back caching for a chat application. When does each make sense?'},
            {'label': 'Boundary Testing', 'text': 'A cache stores a session token that is revoked server-side. Users stay logged in for 10 minutes. Design a revocation mechanism that does not defeat the cache.'},
        ],
        'takeaways': [
            'Caching is the cheapest way to cut latency and load',
            'Staleness is bounded by TTL, invalidation, or versioning',
            'Place caches closest to the user for hot data',
            'Never cache the write-critical path',
        ],
        'further': [
            {'title': 'Everything You Wanted to Know About Caching', 'url': 'https://aws.amazon.com/caching/'},
            {'title': 'Caching Strategies — Redis Docs', 'url': 'https://redis.io/docs/latest/develop/use/patterns/caching/'},
        ],
    },
    {
        'title': 'Caching in Production: Thundering Herds and Stampedes',
        'desc': 'Cache stampedes, stale-while-revalidate, and invalidation at scale.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Prevent cache stampedes with single-flight requests',
            'Implement stale-while-revalidate',
            'Use cache-aside correctly with locking',
            'Design multi-tier cache invalidation',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'The Stampede Problem', 'paras': [
                'When a hot key expires, thousands of concurrent requests all miss and hit the database at once — the "thundering herd." Single-flight (only one request recomputes; the rest wait for its result) turns a stampede into a single refresh.',
            ], 'code': {'lang': 'go', 'body': '''
// Single-flight: only one goroutine recomputes per key
var group singleflight.Group

func GetUser(id string) (*User, error) {
    if u, ok := cache.Get(id); ok {
        return u, nil
    }
    v, err, _ := group.Do(id, func() (any, error) {
        u, err := db.GetUser(id)   // only ONE caller hits DB
        cache.Set(id, u, ttl)
        return u, err
    })
    return v.(*User), err
}'''}},
            {'heading': 'Stale-While-Revalidate', 'paras': [
                'Serve the stale copy immediately while a background job refreshes it. Users never see a miss-latency spike, and the database sees one refresh instead of a stampede. CDNs and HTTP caches implement this with the stale-while-revalidate directive.',
            ]},
        ],
        'practice': {
            'title': 'Kill a Stampede',
            'intro': 'A leaderboard key expires every 5 minutes and its recompute takes 800ms. Under 5k QPS, the recompute phase pegs the database.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Apply single-flight and measure the DB query count before/after.'},
                {'label': 'Task 2', 'text': 'Add stale-while-revalidate with a background recompute every 60s.'},
                {'label': 'Task 3', 'text': 'Add jitter to TTLs so keys do not expire in lockstep.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why random TTL jitter alone does not fully solve a stampede and what single-flight adds.'},
            {'label': 'Implementation Design', 'text': 'Design a cache for a payment balance that must be strongly consistent with the ledger but fast. Where do you cache, and how do you invalidate?'},
            {'label': 'Boundary Testing', 'text': 'A background revalidator crashes. Design a fail-safe so stale data still gets served but the system eventually refreshes.'},
        ],
        'takeaways': [
            'Stampedes multiply one expired key into a DB outage',
            'Single-flight collapses concurrent misses into one recompute',
            'Stale-while-revalidate hides refresh latency entirely',
            'TTL jitter prevents lockstep expiry',
        ],
        'further': [
            {'title': 'Stale-While-Revalidate — MDN', 'url': 'https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control'},
            {'title': 'singleflight — Go Docs', 'url': 'https://pkg.go.dev/golang.org/x/sync/singleflight'},
        ],
    },
    {
        'title': 'Advanced Caching: Distributed Caches and Multi-Tier',
        'desc': 'Consistent hashing, cache-aside with locking, and multi-tier caches at scale.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Explain consistent hashing and hotspot avoidance',
            'Implement cache-aside with lock to avoid duplicate fills',
            'Design an L1/L2 cache hierarchy',
            'Handle cache node failure without a stampede',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Consistent Hashing', 'paras': [
                'Distributed caches place keys on nodes with consistent hashing: adding or removing a node only remaps a small fraction of keys, avoiding a full-cache stampede on resharding. Virtual nodes spread load evenly when keys cluster.',
            ], 'code': {'lang': 'python', 'body': '''
# Consistent hashing with virtual nodes (simplified)
import hashlib, bisect

class ConsistentHash:
    def __init__(self, nodes, vnodes=100):
        self.ring = []
        self.nodes = {}
        for n in nodes:
            for v in range(vnodes):
                h = int(hashlib.md5(f"{n}:{v}".encode()).hexdigest()[:8], 16)
                self.ring.append(h); self.nodes[h] = n
        self.ring.sort()

    def get_node(self, key):
        h = int(hashlib.md5(key.encode()).hexdigest()[:8], 16)
        i = bisect.bisect_right(self.ring, h) % len(self.ring)
        return self.nodes[self.ring[i]]'''}},
            {'heading': 'Cache-Aside with Lock', 'paras': [
                'Cache-aside reads: try cache, on miss load from source and populate. Without a lock, concurrent misses duplicate work (mini-stampede). A per-key lock serializes the fill while reads outside the lock still work.',
                'L1 (in-process) + L2 (distributed) caches give single-digit microsecond hits for hot keys while keeping the L2 as a safety net when a node restarts.',
            ]},
        ],
        'practice': {
            'title': 'Design a Multi-Tier Cache',
            'intro': 'A video-metadata service: 10k videos, metadata changes rarely, read QPS 100k. Six cache nodes, each with 1GB.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design L1 (in-process, 10k entries) + L2 (Redis cluster) with invalidation flow across tiers.'},
                {'label': 'Task 2', 'text': 'Handle a cache node failure: what happens to the keys it owned? Is there a stampede? How do you prevent it?'},
                {'label': 'Task 3', 'text': 'Design the write path: how does a metadata edit invalidate L1 on all servers plus L2 without missing updates?'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can derive why consistent hashing needs virtual nodes for skewed keys, and what happens without them.'},
            {'label': 'Implementation Design', 'text': 'Design a distributed cache where a single node failure must not cause a stampede. Consider backup-key routing and degraded reads.'},
            {'label': 'Boundary Testing', 'text': 'A cache stores a computed recommendation per user, but recommendations change every hour. Design a TTL + async recompute that never serves stale-for-more-than-10-min.'},
        ],
        'takeaways': [
            'Consistent hashing makes resharding cheap and non-destructive',
            'Virtual nodes fix hot-key clustering',
            'Per-key fill locks prevent duplicate work on miss',
            'Multi-tier caches trade complexity for microsecond hits',
        ],
        'further': [
            {'title': 'Consistent Hashing — Paper', 'url': 'https://dl.acm.org/doi/10.1145/258533.258642'},
            {'title': 'Cache-Aside Pattern — Microsoft Docs', 'url': 'https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside'},
        ],
    },
    {
        'title': 'Caching: Review & Mastery Quiz',
        'desc': 'Scenario questions on cache layers, stampedes, and distributed caching.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate caching concepts',
            'Apply caching reasoning to new workloads',
            'Identify cache anti-patterns',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: 99% hit ratio on a 100 QPS endpoint means how many DB queries/sec? (A: 1 / B: 99 / C: 100)',
                'Q2: A thundering herd is caused by? (A: TTL too long / B: hot key expiry with concurrent misses / C: small cache)',
                'Q3: Stale-while-revalidate serves? (A: only fresh / B: stale immediately + background refresh / C: errors)',
                'Q4: True or false: consistent hashing remaps all keys when a node joins.',
                'Q5: Which path should never be cached? (A: leaderboard / B: checkout balance / C: profile picture)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'Black Friday: a product page key expires and 50k concurrent requests stampede the database. Design the full fix (single-flight + SWR + jitter) and estimate the new DB load.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why invalidation is hard and TTL-only caching eventually bites, with a concrete example.'},
        ],
        'takeaways': [
            'Q1: A; Q2: B; Q3: B; Q4: false; Q5: B',
            'Caching multiplies capacity but introduces staleness',
            'Stampedes, not TTLs, are the usual production killer',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# CAP THEOREM
# ─────────────────────────────────────────────────────────────────────────────
_t('cap-theorem', [
    {
        'title': 'The CAP Theorem: Pick Two',
        'desc': 'Why a distributed system cannot have strong consistency and availability during a partition.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'State the CAP theorem precisely',
            'Define consistency, availability, and partition tolerance',
            'Explain what "during a partition" means',
            'Map real systems (CP/AP) onto the CAP space',
        ],
        'prereqs': ['principles/base', 'principles/quorum'],
        'sections': [
            {'heading': 'The Three Properties', 'paras': [
                'Consistency means every read returns the latest write (linearizability). Availability means every request receives a response (not necessarily the latest data). Partition tolerance means the system keeps operating when network messages are lost or delayed.',
                'During a partition, a system cannot be both fully consistent and fully available: either the minority side refuses to serve (CP, choosing consistency) or serves with possibly stale data (AP, choosing availability).',
            ], 'code': {'lang': 'text', 'body': '''
CAP during a partition (network split between A and B):
  CP choice: A serves, B returns errors/slow-down   -> consistent, not available
  AP choice: A and B both serve possibly stale data -> available, not consistent

After the partition heals, AP systems must reconcile divergent writes.'''}},
            {'heading': 'CAP Is About Partitions', 'paras': [
                'When there is no partition, a system can be both consistent and available. The theorem only forces the trade-off during a partition — so engineers design for the partition case and optimize the no-partition case.',
                'PACELC extends this: even without partitions, you choose between latency and consistency (e.g., synchronous vs asynchronous replication).',
            ]},
        ],
        'practice': {
            'title': 'Classify Real Systems',
            'intro': 'Classify each as CP or AP and justify: a primary-replica SQL database, Cassandra with quorum, a DNS system, a shopping cart.',
            'tasks': [
                {'label': 'Task 1', 'text': 'For the SQL primary-replica system, describe exactly what happens to the replica\'s reads during a split.'},
                {'label': 'Task 2', 'text': 'For Cassandra with quorum reads/writes, what does it do during a partition?'},
                {'label': 'Task 3', 'text': 'Design a cart that is AP during a partition and reconciles merges after healing. What conflicts arise?'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why "pick two" is a simplification and what PACELC adds. Start with the definition of a partition.'},
            {'label': 'Compare & Contrast', 'text': 'Compare how MongoDB (primary), Cassandra (tunable), and DynamoDB (configurable) sit on the CAP spectrum and what knobs you turn to move them.'},
            {'label': 'Boundary Testing', 'text': 'A single-node database has no partitions, so is it both C and A? What happens with two replicas and a 200ms network delay between them?'},
        ],
        'takeaways': [
            'CAP forces a choice only during a partition',
            'CP favors consistency, AP favors availability',
            'PACELC adds the latency/consistency trade-off without partitions',
            'Classify each data path, not the whole system',
        ],
        'further': [
            {'title': 'CAP Theorem — MIT Gilbert & Lynch', 'url': 'https://groups.csail.mit.edu/tds/papers/Gilbert/Brewer2.pdf'},
            {'title': 'CAP Twelve Years Later', 'url': 'https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/'},
        ],
    },
    {
        'title': 'CAP in Practice: CP and AP Systems',
        'desc': 'How real databases, key-value stores, and coordination services implement their CAP choice.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Explain quorum-based reads and writes',
            'Describe how Raft implements CP',
            'Describe how Dynamo-style systems implement AP',
            'Choose CP or AP for a given workload',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quorums: The Middle Ground', 'paras': [
                'With N replicas, require W writes and R reads such that W + R > N. Then any read sees at least one node with the latest write — quorum consistency, without waiting for all replicas. Choosing W and R tunes where you sit on the CP/AP spectrum.',
            ], 'code': {'lang': 'text', 'body': '''
Quorum math (N=3):
  W=2, R=2  -> W+R=4 > 3  : strong-ish, tolerates 1 node loss
  W=1, R=1  -> W+R=2 < 3  : AP-ish, may read stale
  W=3, R=1  -> W+R=4 > 3  : CP-ish, write needs all 3

Tune per workload: strong for payments, loose for feeds.'''}},
            {'heading': 'Raft vs Dynamo', 'paras': [
                'Raft-based systems (etcd, ZooKeeper, CockroachDB) are CP: a leader replicates writes to a majority, and the minority side of a partition refuses to elect a leader — it stops serving rather than diverge.',
                'Dynamo-style systems (Cassandra, Riak, original DynamoDB) are AP: every replica accepts writes and serves reads; conflicts are resolved later with vector clocks, timestamps, or application logic.',
            ]},
        ],
        'practice': {
            'title': 'Design the Quorum',
            'intro': 'A multi-region order service with 5 replicas. Reads must never see a lost order; writes must succeed during a single-region outage.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Choose W and R and prove W+R>5. Compute worst-case availability during a region outage.'},
                {'label': 'Task 2', 'text': 'What happens to reads if the region with the latest write is down? Is that acceptable for orders?'},
                {'label': 'Task 3', 'text': 'Redesign so writes still succeed during the outage (loosen W) and explain the new consistency risk.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why W+R>N gives quorum consistency and walk me through a W=2,R=2,N=3 read. Ask me to compute variants.'},
            {'label': 'Compare & Contrast', 'text': 'Compare how etcd (Raft) and Cassandra handle a 3-node split 2v1. Which serves reads on the minority side and why?'},
            {'label': 'Boundary Testing', 'text': 'Quorum is satisfied but a read lands on a node that missed the last write. Is that possible with W+R>N? Construct a counterexample or prove it impossible.'},
        ],
        'takeaways': [
            'W+R>N yields quorum consistency',
            'Raft systems are CP; Dynamo systems are AP',
            'Quorums tune the CP/AP trade-off per workload',
            'Multi-region quorums trade write latency for availability',
        ],
        'further': [
            {'title': 'Raft: Understandable Distributed Consensus', 'url': 'https://raft.github.io/raft.pdf'},
            {'title': 'DynamoDB Consistency Models', 'url': 'https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html'},
        ],
    },
    {
        'title': 'Advanced CAP: Linearizability, Sessions, and Reconciliation',
        'desc': 'Tight definitions of consistency, session guarantees, and conflict resolution in AP systems.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Define linearizability and serializability precisely',
            'Apply session guarantees to AP systems',
            'Design conflict resolution with version vectors',
            'Explain the read-your-writes and monotonic reads guarantees',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Linearizability and Session Guarantees', 'paras': [
                'Linearizability orders operations in real time: once a write completes, all subsequent reads see it. Fully linearizable AP systems are impossible during partitions, but session guarantees give users a weaker, useful contract: read-your-writes, monotonic reads, and monotonic writes.',
                'A read-your-writes session routes a user\'s reads to a replica that has seen their writes — cheap, and it fixes the most common user-visible consistency bug.',
            ], 'code': {'lang': 'python', 'body': '''
# Session affinity: stick a user to the replica that saw their writes
session = {}
def route_read(user_id, replica_versions):
    # pick the replica whose version >= user's last-seen write version
    want = session.get(user_id, 0)
    for replica, version in replica_versions.items():
        if version >= want:
            session[user_id] = replica   # sticky affinity
            return replica
    return min(replica_versions, key=replica_versions.get)'''}},
            {'heading': 'Version Vectors', 'paras': [
                'When two replicas diverge, version vectors tell you whether one state is newer (descendant), equal, or concurrent. Concurrent writes must be merged by application logic — that is where CRDTs and LWW registers come in.',
            ]},
        ],
        'practice': {
            'title': 'Design Conflict Resolution',
            'intro': 'An AP cart service has two replicas that each received an add-to-cart during a partition.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Use version vectors to detect the concurrent writes.'},
                {'label': 'Task 2', 'text': 'Merge the carts (union) and decide how to handle a concurrent remove of an item added on the other replica.'},
                {'label': 'Task 3', 'text': 'Add a last-writer-wins register for the cart "coupon" field and explain the clock it needs.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can distinguish linearizability from serializability and explain why AP systems give up the former but keep transactions.'},
            {'label': 'Implementation Design', 'text': 'Design session guarantees for a chat app that is otherwise AP. Which guarantees does each message need to preserve ordering of one conversation?'},
            {'label': 'Boundary Testing', 'text': 'Two users concurrently rename the same file in a distributed filesystem. Design a resolution policy and describe the user-visible result for each case.'},
        ],
        'takeaways': [
            'Linearizability is a real-time ordering; AP gives it up during partitions',
            'Session guarantees fix common user-visible bugs cheaply',
            'Version vectors distinguish causal from concurrent writes',
            'Concurrent writes need application-level merge rules',
        ],
        'further': [
            {'title': 'Linearizability — Herlihy & Wing', 'url': 'https://cs.brown.edu/~mph/HerlihyW90/p463-herlihy.pdf'},
            {'title': 'Session Guarantees for Weakly Consistent Replicated Data', 'url': 'https://www.cs.utexas.edu/users/dahlin/papers/session83.pdf'},
        ],
    },
    {
        'title': 'CAP Theorem: Review & Mastery Quiz',
        'desc': 'Scenario questions on partitions, quorums, and reconciliation.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate CAP reasoning',
            'Apply quorum math to new systems',
            'Choose consistency contracts per workload',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: During a partition, a CP system on the minority side? (A: serves stale / B: stops serving / C: serves fresh)',
                'Q2: W=2, R=2, N=3 gives? (A: quorum consistency / B: no consistency / C: linearizability always)',
                'Q3: PACELC\'s "E" stands for? (A: eventually / B: else / C: errors)',
                'Q4: True or false: a single-node DB is always both consistent and available.',
                'Q5: Session guarantee that prevents "I posted but I can\'t see it" is? (A: read-your-writes / B: monotonic reads / C: linearizability)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A multi-region payment system must never double-charge and must survive a region loss. Design the quorum and the reconciliation, and identify where you accept availability loss.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "CAP means pick two" is misleading without "during a partition" and PACELC.'},
        ],
        'takeaways': [
            'Q1: B; Q2: A; Q3: B; Q4: true (no partitions); Q5: A',
            'CAP choices are per data path and per failure mode',
            'Quorums and session guarantees are the practical tools',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# CIRCUIT BREAKER
# ─────────────────────────────────────────────────────────────────────────────
_t('circuit-breaker', [
    {
        'title': 'Circuit Breakers: Stop Calling a Dead Dependency',
        'desc': 'The pattern that fails fast instead of failing slowly, and how it prevents cascading outages.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the three circuit breaker states',
            'Describe why failing fast beats failing slowly',
            'Implement a basic circuit breaker',
            'Choose thresholds and timeouts',
        ],
        'prereqs': ['principles/bulkhead', 'principles/graceful-degradation'],
        'sections': [
            {'heading': 'The Problem: Slow Failures Cascade', 'paras': [
                'When a downstream service is down, callers that keep waiting occupy threads, connections, and queues. Their timeouts stack up, the caller\'s resources exhaust, and the failure cascades upstream — an outage that started in one service spreads to the whole platform.',
                'A circuit breaker wraps the dependency: when failures cross a threshold, the breaker "opens" and subsequent calls fail immediately (or hit a fallback) without touching the broken dependency. It gives the dependency time to recover while the caller stays healthy.',
            ], 'code': {'lang': 'python', 'body': '''
# A minimal circuit breaker (closed -> open -> half-open)
class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout_s=30):
        self.failure_threshold = failure_threshold
        self.timeout_s = timeout_s
        self.failures = 0
        self.state = 'CLOSED'
        self.opened_at = None

    def call(self, fn, fallback):
        if self.state == 'OPEN':
            if time_since(self.opened_at) > self.timeout_s:
                self.state = 'HALF_OPEN'   # try one probe call
            else:
                return fallback()          # fast fail
        try:
            result = fn()
            self.failures = 0
            self.state = 'CLOSED'
            return result
        except Exception:
            self.failures += 1
            if self.failures >= self.failure_threshold:
                self.state = 'OPEN'
                self.opened_at = now()
            return fallback()'''}},
            {'heading': 'The Three States', 'paras': [
                'CLOSED: calls go through normally, failures counted. OPEN: calls fail fast for the timeout window. HALF_OPEN: a single probe call tests recovery — success closes the breaker, failure reopens it.',
                'This state machine is what makes the pattern self-healing: it probes the dependency periodically without flooding it.',
            ]},
        ],
        'practice': {
            'title': 'Instrument a Breaker',
            'intro': 'Your service calls a payment provider. It starts returning 503s. 40% of your requests start timing out at 5s.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Set the failure threshold, timeout, and fallback (queue the payment for retry). Justify each number.'},
                {'label': 'Task 2', 'text': 'Sketch the timeline: when does the breaker open, and what do users see during OPEN?'},
                {'label': 'Task 3', 'text': 'Design the HALF_OPEN probe so it does not flood the recovering provider (one probe, then a ramp).'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time to reason about the difference between a timeout and a circuit breaker. Start with the resource cost of slow failures.'},
            {'label': 'Compare & Contrast', 'text': 'Compare circuit breakers with retries, bulkheads, and rate limiting. Which one prevents the flood, contains it, and heals the source?'},
            {'label': 'Boundary Testing', 'text': 'A breaker is closed, but the dependency returns 200s with garbage data. Your circuit is "healthy" while behavior is broken. How do you detect that failure mode?'},
        ],
        'takeaways': [
            'Slow failures are more dangerous than fast ones',
            'OPEN fails fast, giving the dependency time to recover',
            'HALF_OPEN probes recovery without flooding',
            'Breakers need health signals beyond HTTP status codes',
        ],
        'further': [
            {'title': 'Circuit Breaker Pattern — Microsoft Docs', 'url': 'https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker'},
            {'title': 'Netflix Hystrix Circuit Breaker', 'url': 'https://github.com/Netflix/Hystrix/wiki/How-it-Works'},
        ],
    },
    {
        'title': 'Circuit Breakers in Production',
        'desc': 'Real breaker implementations, fallbacks, and integrating with resilience libraries.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Configure resilience4j/resilience4j-style breakers',
            'Design meaningful fallbacks per dependency',
            'Use breaker events for alerting',
            'Avoid breaker anti-patterns (too sensitive, too slow)',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Configuring a Real Breaker', 'paras': [
                'Resilience4j (Java) and similar libraries let you configure sliding-window failure rate, minimum calls, wait duration, and call-timeout. Key tuning: minimum calls prevents a breaker opening on a single transient blip.',
            ], 'code': {'lang': 'java', 'body': '''
// resilience4j: sliding window breaker with fallback
CircuitBreakerConfig config = CircuitBreakerConfig.custom()
    .failureRateThreshold(50)                    // open at 50% failures
    .slidingWindowSize(10)                       // last 10 calls
    .minimumNumberOfCalls(5)                     // require 5 calls first
    .waitDurationInOpenState(Duration.ofSeconds(20))
    .build();
CircuitBreaker cb = CircuitBreaker.of("payments", config);

Supplier<String> safe = CircuitBreaker.decorateSupplier(cb, () ->
    paymentClient.charge(order));
String result = Try.ofSupplier(safe)
    .recover(t -> queueForRetry(order))          // fallback
    .get();'''}},
            {'heading': 'Fallbacks That Matter', 'paras': [
                'A fallback is what users actually experience: serve cached data, show degraded UI, queue the work, or return a default. A fallback that hides the failure entirely (silently dropping money) is worse than a visible error.',
            ]},
        ],
        'practice': {
            'title': 'Wire Breakers Across a Platform',
            'intro': 'Your platform calls search, recommendations, payments, and email. Each has different failure costs.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design thresholds + fallbacks per dependency (payments=queue, search=stale index, email=skip+log, recs=default).'},
                {'label': 'Task 2', 'text': 'Define alerting: which breaker openings page on-call, which just log?'},
                {'label': 'Task 3', 'text': 'Sketch a dashboard showing breaker state per dependency over time.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why minimumNumberOfCalls prevents flapping breakers and what "flapping" means.'},
            {'label': 'Implementation Design', 'text': 'Design a breaker for a batch job that retries forever. Should the job use a breaker? What does failure fast mean there?'},
            {'label': 'Boundary Testing', 'text': 'A breaker opens but the fallback itself calls the same dependency. Design the guard that prevents fallback recursion.'},
        ],
        'takeaways': [
            'Tune with failure rate + minimum calls to avoid flapping',
            'Fallbacks are the user-visible contract of a breaker',
            'Breaker events are first-class alerting signals',
            'Fallbacks must not call the broken dependency',
        ],
        'further': [
            {'title': 'Resilience4j Docs', 'url': 'https://resilience4j.readme.io/docs/circuitbreaker'},
            {'title': 'Fault Tolerance in a High Volume System (Google SRE)', 'url': 'https://sre.google/sre-book/service-level-objectives/'},
        ],
    },
    {
        'title': 'Advanced Circuit Breakers: Health Signals and Probing',
        'desc': 'Failure modes beyond status codes, adaptive probing, and breaker pools.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Detect failures invisible to status codes',
            'Implement adaptive HALF_OPEN probing',
            'Use circuit breakers in multi-node callers',
            'Combine breakers with load shedding',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Beyond Status Codes', 'paras': [
                'A dependency can return 200 with stale or corrupt data, or respond slowly without erroring. Track latency percentiles as a health signal: if p99 latency exceeds a threshold, treat the dependency as degraded and open a "latency breaker".',
            ], 'code': {'lang': 'go', 'body': '''
// Latency-based breaker: slow = unhealthy
var p99 = &slidingPercentile{window: 60, p: 0.99}

func Call(ctx context.Context, fn func() (any, error)) (any, error) {
    if p99.value() > 2*time.Second && breaker.isClosed() {
        breaker.open("latency above budget")   // slow path opens too
    }
    start := time.Now()
    v, err := fn()
    p99.add(time.Since(start))
    return v, err
}'''}},
            {'heading': 'Adaptive Probing', 'paras': [
                'Fixed HALF_OPEN probes can flood a barely-recovering dependency. Adaptive probing starts with one probe and ramps the success threshold: after a successful probe, allow a small percentage of traffic, and scale up as the dependency proves healthy.',
                'In multi-node callers, breaker state is per-node — each node independently observes and probes. Coordinate via shared state (e.g., a central health registry) only when nodes would otherwise stampede the probe.',
            ]},
        ],
        'practice': {
            'title': 'Design a Latency-Aware Breaker',
            'intro': 'A dependency degrades: p99 goes from 80ms to 4s without any error status codes.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the latency threshold and the window over which you measure p99.'},
                {'label': 'Task 2', 'text': 'Design the probe ramp: how much traffic is allowed after a successful probe?'},
                {'label': 'Task 3', 'text': 'Add a load-shedding rule: when the breaker is open AND the queue is full, reject new work at the edge.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why percentile latency is a better health signal than average latency.'},
            {'label': 'Implementation Design', 'text': 'Design a breaker that distinguishes "provider down" from "provider slow for one tenant" and opens only for the affected tenant.'},
            {'label': 'Boundary Testing', 'text': 'Every caller node opens its breaker simultaneously and all fallbacks point at the same cold cache. Design a fallback hierarchy that avoids the new stampede.'},
        ],
        'takeaways': [
            'Latency and data-quality signals catch what status codes miss',
            'Adaptive probing ramps traffic as recovery proves itself',
            'Per-node breakers avoid synchronized probe floods',
            'Breakers + load shedding give end-to-end protection',
        ],
        'further': [
            {'title': 'Latency Percentiles — Google SRE Book', 'url': 'https://sre.google/sre-book/table-of-contents/'},
            {'title': 'Finagle Resilience (Twitter)', 'url': 'https://twitter.github.io/finagle/guide/Clients.html'},
        ],
    },
    {
        'title': 'Circuit Breakers: Review & Mastery Quiz',
        'desc': 'Scenario questions on breaker states, thresholds, and fallbacks.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate breaker concepts',
            'Tune breakers for real failure modes',
            'Design effective fallbacks',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: In OPEN state, calls to the dependency? (A: proceed / B: fail fast / C: retry 3x)',
                'Q2: HALF_OPEN means? (A: probing recovery / B: permanently closed / C: degraded mode)',
                'Q3: minimumNumberOfCalls prevents? (A: flapping on a blip / B: slow starts / C: timeouts)',
                'Q4: True or false: a breaker opens based on status codes only.',
                'Q5: The user-visible contract of a breaker is its? (A: thresholds / B: fallback / C: timeout)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A dependency returns 500s for 2 minutes then recovers. Design a breaker that opens, probes once at 30s, and recovers without a stampede. What does the user see at each stage?'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why a 30s timeout alone is not enough to protect a system, using a thread-exhaustion cascade story.'},
        ],
        'takeaways': [
            'Q1: B; Q2: A; Q3: A; Q4: false; Q5: B',
            'Breakers convert slow cascades into fast, bounded failures',
            'Health signals and fallbacks determine real resilience',
        ],
    },
])
