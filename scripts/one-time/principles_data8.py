#!/usr/bin/env python3
"""Deep curriculum data chunk 8: quorum, rate-limiting, separation-of-concerns, single-responsibility."""

TOPICS = {}


def _t(slug, topics):
    TOPICS[slug] = topics
    return topics


# ─────────────────────────────────────────────────────────────────────────────
# QUORUM
# ─────────────────────────────────────────────────────────────────────────────
_t('quorum', [
    {
        'title': 'Quorum: Majorities and Consensus',
        'desc': 'Why decisions need more than half the votes, and how quorums make distributed writes safe.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Define a quorum and why it needs a majority',
            'Explain the quorum intersection property',
            'Use read/write quorums (W + R > N)',
            'Apply quorums to replica consistency',
        ],
        'prereqs': ['principles/cap-theorem', 'principles/leader-election'],
        'sections': [
            {'heading': 'The Core Idea', 'paras': [
                'A quorum is the minimum number of nodes that must agree for a decision to hold. In a 5-node cluster, a quorum of 3 guarantees one crucial property: any two quorums intersect in at least one node. That intersection is how the system knows a later read can always see an earlier acknowledged write.',
                'The math: with N replicas, require W writes and R reads such that W + R > N. Then a read quorum and a write quorum overlap, so every consistent read sees the latest acknowledged write.',
            ], 'code': {'lang': 'text', 'body': '''
Quorum math (N = 5):
  W=3, R=3 : W+R=6 > 5 -> reads always see latest write
  W=3, R=2 : W+R=5 = 5 -> NOT guaranteed (may miss the write)
  W=2, R=2 : W+R=4 < 5 -> stale reads possible (AP-ish)

Two quorums of 3 always share at least 1 node:
  {1,2,3} and {3,4,5} intersect at 3.  That is the guarantee.'''}},
            {'heading': 'Quorum vs Consensus', 'paras': [
                'A quorum is the membership rule; consensus (Raft, Paxos) is a protocol that uses quorums to agree on a total order of operations. Quorum reads/writes give consistency; consensus gives ordering and leader election on top.',
            ]},
        ],
        'practice': {
            'title': 'Design the Quorum',
            'intro': 'A 5-node key-value store: reads must never return stale acknowledged data; writes must survive one node loss.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Pick W and R satisfying W+R>5 and W>2. Justify.'},
                {'label': 'Task 2', 'text': 'Compute availability: what happens with 2 nodes down? With 3 down?'},
                {'label': 'Task 3', 'text': 'Show why W=1, R=5 "sounds strong" but breaks the read guarantee when the write node is the read node.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why W+R>N is sufficient for the read guarantee. Start with the intersection argument.'},
            {'label': 'Compare & Contrast', 'text': 'Compare quorum reads with Raft log replication. Where does the majority do different jobs?'},
            {'label': 'Boundary Testing', 'text': 'W=3, R=3, N=5 but the write nodes and read nodes are disjoint groups (write set {1,2,3}, read set {4,5,1}). Is the guarantee intact?'},
        ],
        'takeaways': [
            'Quorums intersect — that is the consistency guarantee',
            'W+R>N is the read-your-write condition',
            'Quorums trade write latency for availability',
            'Consensus builds ordering on top of quorums',
        ],
        'further': [
            {'title': 'Raft Paper (Quorum sections)', 'url': 'https://raft.github.io/raft.pdf'},
            {'title': 'Dynamo Paper (Quorum-based replication)', 'url': 'https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf'},
        ],
    },
    {
        'title': 'Quorum in Production: Multi-AZ and Geo',
        'desc': 'Quorums across availability zones, regions, and the latency they cost.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design quorums across AZs',
            'Balance quorum size with failure tolerance',
            'Handle quorum loss (degraded mode)',
            'Measure quorum write latency',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'AZ-Aware Quorums', 'paras': [
                'A 3-replica quorum (W=2, R=2) across 3 AZs tolerates any single-AZ loss: the two remaining AZs still form a quorum. This is the standard strong-consistency deployment for managed databases.',
            ], 'code': {'lang': 'text', 'body': '''
3 AZs x 1 replica each, N=3:
  W=2, R=2 : one AZ dies -> 2 nodes remain -> quorum works
  W=3, R=1 : one AZ dies -> writes fail (no quorum) -> reads may work
  W=1, R=1 : any split -> stale reads possible (AP)

Write latency = max of the slowest node in the write quorum.
Across regions, W=2 in one region then async to the other.'''}},
            {'heading': 'Quorum Loss', 'paras': [
                'When fewer than a quorum of nodes are reachable, the system cannot safely accept writes. The correct behavior is to refuse writes (fail closed) rather than accept them without quorum and risk divergence. Reads may continue from surviving nodes if the read quorum is met.',
            ]},
        ],
        'practice': {
            'title': 'Design the Multi-AZ Quorum',
            'intro': 'A payments store must survive one AZ loss and keep reads consistent.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Pick the replica count and W/R for the requirements.'},
                {'label': 'Task 2', 'text': 'Define the fail-closed behavior when the write quorum is lost.'},
                {'label': 'Task 3', 'text': 'Estimate the write latency impact of W=2 across AZs and whether the payments SLA accepts it.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why a quorum spanning AZs is the standard strong-consistency design. Ask me to compute AZ-loss scenarios.'},
            {'label': 'Implementation Design', 'text': 'Design a multi-region order store with quorum in the primary region and async replication to a standby. What does the standby guarantee?'},
            {'label': 'Boundary Testing', 'text': 'Two of three AZs have a slow link (partition but not full loss). Quorum still meets — but latency spikes. Design the degradation signal.'},
        ],
        'takeaways': [
            '3 AZs with W=2,R=2 survive any single-AZ loss',
            'Quorum loss = fail closed, never diverge',
            'Write latency tracks the slowest quorum node',
            'Geo quorums use local quorum + async replication',
        ],
        'further': [
            {'title': 'Cassandra Tunable Consistency', 'url': 'https://docs.datastax.com/en/cassandra-oss/3.x/cassandra/dml/dmlConfigConsistency.html'},
            {'title': 'Google Spanner TrueTime & Paxos', 'url': 'https://research.google/pubs/pub45855/'},
        ],
    },
    {
        'title': 'Advanced Quorum: Flexible and Epoch Quorums',
        'desc': 'Flexible quorums, epoch-based fencing, and tuning quorums for skewed workloads.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Design flexible (asymmetric) quorums',
            'Use epochs to fence stale quorums',
            'Tune quorums per workload skew',
            'Handle quorum membership changes',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Flexible Quorums', 'paras': [
                'The read-write intersection can be split asymmetrically: reads need W nodes, writes need R nodes, with W+R>N but neither necessarily a majority. For read-heavy workloads, a flexible quorum (W=N, R=1) gives strong reads with a single-node read cost — at the price of slow writes.',
            ], 'code': {'lang': 'text', 'body': '''
Flexible quorum variants (N=5):
  Classic  : W=3, R=3  (balanced)
  Read-opt : W=4, R=2  (cheaper reads, costlier writes)
  Write-opt: W=2, R=4  (cheaper writes, costlier reads)
All satisfy W+R>5. Choose by workload skew.

Epoch fencing: when membership changes (node join/leave), start a new
epoch; old-epoch quorum decisions are rejected by storage.'''}},
            {'heading': 'Membership and Epochs', 'paras': [
                'Quorum membership changes (a node joins or is evicted) invalidate the old quorum math. Epoch-based fencing: every configuration change bumps the epoch, storage stamps accepted writes with the epoch, and nodes from the old epoch are rejected — preventing a stale majority from writing after reconfiguration.',
            ]},
        ],
        'practice': {
            'title': 'Tune and Fence',
            'intro': 'A 5-node store: reads are 20x writes, and you must add a 6th node without downtime.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Pick the flexible quorum for the read-heavy skew and justify W+R>5.'},
                {'label': 'Task 2', 'text': 'Design the membership change: new config, new epoch, and the fencing that rejects old-epoch writers.'},
                {'label': 'Task 3', 'text': 'Verify the intersection still holds with N=6 and your chosen W/R.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why flexible quorums keep the intersection property without both sides being majorities.'},
            {'label': 'Implementation Design', 'text': 'Design a config-change protocol for a quorum system: how do nodes learn the new membership safely and fence the old one?'},
            {'label': 'Boundary Testing', 'text': 'A write quorum meets but a member of it is running stale state (missed a prior write). Is that possible with W+R>N? Prove or refute.'},
        ],
        'takeaways': [
            'Flexible quorums tune cost by workload skew',
            'Epochs fence stale membership decisions',
            'Membership changes must be atomic with the new quorum math',
            'The intersection property is the invariant to preserve',
        ],
        'further': [
            {'title': 'Flexible Paxos — Quorum Flexibility', 'url': 'https://arxiv.org/abs/1608.06696'},
            {'title': 'Epoch-based Reconfiguration — Raft', 'url': 'https://raft.github.io/raft.pdf'},
        ],
    },
    {
        'title': 'Quorum: Review & Mastery Quiz',
        'desc': 'Scenario questions on quorum math, AZs, and flexible quorums.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate quorum concepts',
            'Design quorums for requirements',
            'Handle membership and loss',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: The quorum consistency condition is? (A: W+R>N / B: W+R=N / C: W>N)',
                'Q2: Two quorums always? (A: overlap / B: diverge / C: conflict)',
                'Q3: A 3-AZ, N=3, W=2,R=2 setup tolerates? (A: any single AZ loss / B: two AZ losses / C: nothing)',
                'Q4: True or false: on write-quorum loss, the system should fail closed.',
                'Q5: Epoch fencing rejects writes from? (A: old membership epochs / B: new nodes / C: reads)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A stock-trading ledger needs strong reads and low write latency. Design the quorum (N, W, R, AZ layout) and justify every number.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why quorum math is the difference between "mostly consistent" and "provably consistent".'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'The intersection property is the invariant',
            'Quorum choices are per-workload design decisions',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# RATE LIMITING
# ─────────────────────────────────────────────────────────────────────────────
_t('rate-limiting', [
    {
        'title': 'Rate Limiting: Control the Flow',
        'desc': 'Why capping request rates protects systems from spikes, abuse, and self-inflicted overload.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Define rate limiting and its goals',
            'Use fixed-window and sliding-window algorithms',
            'Return proper rate-limit responses',
            'Apply limits per user, IP, and key',
        ],
        'prereqs': ['principles/throttling', 'principles/load-shedding'],
        'sections': [
            {'heading': 'The Idea', 'paras': [
                'Rate limiting caps how many requests a client (user, IP, API key) can send in a window. It protects shared capacity from a single bursty consumer and from abusive traffic — a runaway loop, a scraper, or a DDoS-ish spike must not starve everyone else.',
                'The simplest forms: fixed window (X requests per minute, reset on the minute) and sliding window (X requests per rolling window, smoother). Token bucket generalizes both with burst control.',
            ], 'code': {'lang': 'python', 'body': '''
# Fixed window limiter (per key)
import time
WINDOW = 60
LIMIT = 30
hits = {}  # key -> (window_start, count)

def allow(key):
    now = time.time()
    start, count = hits.get(key, (now, 0))
    if now - start >= WINDOW:
        start, count = now, 0
    if count >= LIMIT:
        return False, retry_after(WINDOW - (now - start))
    hits[key] = (start, count + 1)
    return True, None'''}},
            {'heading': 'Responses That Teach', 'paras': [
                'A rate-limited request should return 429 with a Retry-After header — the client learns when to try again. Clients that honor it back off; the limit coordinates instead of just blocking. Include X-RateLimit-Limit/Remaining/Reset so clients can self-throttle.',
            ]},
        ],
        'practice': {
            'title': 'Design the Limits',
            'intro': 'A public API: anonymous users, free tier, paid tier, and an internal service.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Set rate limits per tier with justification (burst vs sustained).'},
                {'label': 'Task 2', 'text': 'Design the 429 response with Retry-After and rate-limit headers.'},
                {'label': 'Task 3', 'text': 'Decide the limit granularity: per key, per user, per IP — and why IP alone is insufficient.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about the difference between fixed-window and sliding-window limits at the window boundary.'},
            {'label': 'Compare & Contrast', 'text': 'Compare rate limiting with throttling, load shedding, and circuit breaking. Which problem does each solve?'},
            {'label': 'Boundary Testing', 'text': 'A legitimate user bursts 100 requests in one second at a limit of 60/min. Design the burst allowance (token bucket) that admits them without opening the floodgates.'},
        ],
        'takeaways': [
            'Rate limits protect shared capacity from bursts and abuse',
            '429 + Retry-After coordinates well-behaved clients',
            'Sliding windows are smoother than fixed windows',
            'Token buckets allow controlled bursts',
        ],
        'further': [
            {'title': 'Rate Limiting — MDN/Web standards', 'url': 'https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429'},
            {'title': 'An Alternative Approach to Rate Limiting (Figma)', 'url': 'https://www.figma.com/blog/an-alternative-approach-to-rate-limiting/'},
        ],
    },
    {
        'title': 'Rate Limiting in Production: Distributed Limits',
        'desc': 'Limits that work across many servers, shared counters, and edge enforcement.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design distributed rate limiters',
            'Use Redis-based counters',
            'Enforce at the edge (CDN, gateway)',
            'Handle limiter failure modes',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Distributed Counting', 'paras': [
                'With many servers behind a load balancer, per-server limits let a client get N× the budget by spreading requests. Distributed counting uses a shared store (Redis INCR with expiry, or a token-bucket service) so the limit is global.',
            ], 'code': {'lang': 'python', 'body': '''
# Redis sliding-window-ish counter (per key, per window)
import redis, time
r = redis.Redis()

def allow(key, limit, window_s):
    now = int(time.time())
    bucket = f'rl:{key}:{now // window_s}'     # fixed window in Redis
    count = r.incr(bucket)
    if count == 1:
        r.expire(bucket, window_s + 1)         # auto-cleanup
    return count <= limit, max(0, window_s - (now % window_s))'''}},
            {'heading': 'Edge Enforcement', 'paras': [
                'The cheapest place to rate-limit is the edge: CDN and gateway rules reject early, before requests consume application capacity. Layered limits — edge (coarse, per IP), gateway (per key), app (per user logic) — catch abuse at the cheapest layer.',
            ]},
        ],
        'practice': {
            'title': 'Layer the Limits',
            'intro': 'An API with 40 backend servers: clients hit 40 different IPs, so per-server limits are meaningless.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the Redis counter shared across servers with a per-key window.'},
                {'label': 'Task 2', 'text': 'Layer edge vs app limits and decide what each enforces.'},
                {'label': 'Task 3', 'text': 'Design the failure mode: Redis down. Do you fail open or closed, and what does each cost?'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why per-server limits are useless behind a load balancer and what distributed counting changes.'},
            {'label': 'Implementation Design', 'text': 'Design a token-bucket limiter as a service: the API, the state, and how clients request permits without a round trip.'},
            {'label': 'Boundary Testing', 'text': 'The limiter itself becomes the bottleneck under a flood. Design the degradation (approximate limits at the edge, exact in the app).'},
        ],
        'takeaways': [
            'Distributed counting makes limits global',
            'Redis INCR + expiry is the workhorse counter',
            'Edge enforcement is the cheapest layer',
            'Limiter failure modes need explicit fail-open/closed policy',
        ],
        'further': [
            {'title': 'Rate Limiting with Redis', 'url': 'https://redis.io/docs/latest/develop/use/patterns/rate-limiting/'},
            {'title': 'Envoy Rate Limiting Service', 'url': 'https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/other_features/global_rate_limiting'},
        ],
    },
    {
        'title': 'Advanced Rate Limiting: Token Buckets and Fairness',
        'desc': 'Token buckets, per-tenant fairness, and limits that adapt to load.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Implement a token bucket precisely',
            'Apply per-tenant fair share',
            'Design adaptive limits',
            'Avoid limit-cascades (laddering)',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Token Bucket', 'paras': [
                'The token bucket allows bursts up to capacity B while sustaining a rate R: tokens refill at R/sec, each request spends one. It is the standard for APIs that must allow bursts but not floods.',
            ], 'code': {'lang': 'python', 'body': '''
# Token bucket (per key)
import time
class TokenBucket:
    def __init__(self, rate, capacity):
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.updated = time.monotonic()

    def take(self):
        now = time.monotonic()
        self.tokens = min(self.capacity,
                          self.tokens + (now - self.updated) * self.rate)
        self.updated = now
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False'''}},
            {'heading': 'Fairness and Ladders', 'paras': [
                'Fair share: when demand exceeds capacity, give each tenant a proportional slice rather than letting the fastest client win. And watch for laddering — a client that crawls upward through tiers (IP limit, then key limit, then account limit) must hit a final cap.',
            ]},
        ],
        'practice': {
            'title': 'Design the Fair Bucket',
            'intro': 'A multi-tenant platform with 100 tenants; three tenants generate 80% of traffic.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design per-tenant token buckets with a global cap.'},
                {'label': 'Task 2', 'text': 'Define the fair-share rule when total demand exceeds capacity.'},
                {'label': 'Task 3', 'text': 'Design the anti-laddering final cap and the alert on sustained cap-hits.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why token buckets allow bursts while fixed windows cannot.'},
            {'label': 'Implementation Design', 'text': 'Design an adaptive limiter that raises limits when capacity is available and lowers them under pressure, without thrashing.'},
            {'label': 'Boundary Testing', 'text': 'A tenant bursts at exactly the bucket rate for an hour, starving others. Design the fairness override that protects the small tenants.'},
        ],
        'takeaways': [
            'Token buckets = burst capacity + sustained rate',
            'Fair share protects small tenants from big bursts',
            'Anti-laddering caps close tier-crawl loopholes',
            'Adaptive limits need hysteresis',
        ],
        'further': [
            {'title': 'Token Bucket — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Token_bucket'},
            {'title': 'Stripe Rate Limits', 'url': 'https://stripe.com/docs/rate-limits'},
        ],
    },
    {
        'title': 'Rate Limiting: Review & Mastery Quiz',
        'desc': 'Scenario questions on algorithms, distribution, and fairness.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate rate-limiting concepts',
            'Design limiter algorithms',
            'Apply fair distribution',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: The rate-limit response status is? (A: 200 / B: 429 / C: 500)',
                'Q2: A token bucket allows? (A: controlled bursts / B: no bursts / C: unlimited)',
                'Q3: Behind a load balancer, limits must be? (A: distributed / B: per server / C: disabled)',
                'Q4: True or false: Retry-After tells the client when to retry.',
                'Q5: Fair share protects? (A: the loudest tenant / B: small tenants / C: the edge)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A flash sale: 1M users hit a checkout API. Design the layered rate limits (edge, gateway, app), the token buckets, and the 429 contract.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why rate limiting is a coordination signal, not just a rejection.'},
        ],
        'takeaways': [
            'Q1: B; Q2: A; Q3: A; Q4: true; Q5: B',
            'Limits protect capacity and coordinate clients',
            'Algorithms choose the burst/smoothness trade-off',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# SEPARATION OF CONCERNS
# ─────────────────────────────────────────────────────────────────────────────
_t('separation-of-concerns', [
    {
        'title': 'Separation of Concerns: One Job per Part',
        'desc': 'Why dividing a system into focused parts makes each one simpler, testable, and replaceable.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Define separation of concerns',
            'Identify entangled concerns in code',
            'Split mixed responsibilities',
            'Explain the benefit for testing and reuse',
        ],
        'prereqs': ['principles/single-responsibility', 'principles/information-hiding'],
        'sections': [
            {'heading': 'The Principle', 'paras': [
                'Separation of concerns (Dijkstra): a system is easier to understand, test, and change when each part addresses one concern. A request handler should not also contain SQL, validation, email logic, and retry policy — each concern deserves its own place.',
                'The payoff: each piece can be tested in isolation, reused independently, and changed without touching the others. Entangled code changes ripple in every direction.',
            ], 'code': {'lang': 'python', 'body': '''
# Entangled: handler, validation, persistence, email all in one function
def signup(request):
    # validate + persist + send email + log — four concerns, one place

# Separated:
def signup(request):
    data = validate(request.body)         # validation concern
    user = users.create(data)             # persistence concern
    email.send_welcome(user)              # notification concern
    logger.info('signup', user_id=user.id)  # observability concern
    return user
# Each concern is a function with its own tests.'''}},
            {'heading': 'Concerns vs Layers', 'paras': [
                'Concerns are the "what" (validation, persistence, presentation); layers are the "where" (API, domain, infrastructure). Separation applies at both: a domain object should not know how it is stored, and an HTTP handler should not know the business rules inside the domain.',
            ]},
        ],
        'practice': {
            'title': 'Untangle the Handler',
            'intro': 'A 200-line handler validates, queries, formats, emails, and retries — all inline.',
            'tasks': [
                {'label': 'Task 1', 'text': 'List the concerns tangled in the handler.'},
                {'label': 'Task 2', 'text': 'Extract each into its own module/function with a test.'},
                {'label': 'Task 3', 'text': 'Show how the extracted validation is now reusable by another endpoint.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about the difference between separation of concerns and just "smaller functions". Start with what a concern is.'},
            {'label': 'Compare & Contrast', 'text': 'Compare separation of concerns with single responsibility and layering. Where do they overlap?'},
            {'label': 'Boundary Testing', 'text': 'Two concerns are tightly coupled by performance (validation must happen in the SQL for speed). Design the boundary that keeps them conceptually separate.'},
        ],
        'takeaways': [
            'Each part should address one concern',
            'Entangled code changes ripple everywhere',
            'Separation enables isolation, reuse, and testing',
            'Boundaries are conceptual before they are physical',
        ],
        'further': [
            {'title': 'Separation of Concerns — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Separation_of_concerns'},
            {'title': 'AOP and Cross-Cutting Concerns', 'url': 'https://en.wikipedia.org/wiki/Cross-cutting_concern'},
        ],
    },
    {
        'title': 'Separation of Concerns in Production: Layers and Modules',
        'desc': 'Clean layering, cross-cutting concerns (logging, auth), and keeping boundaries honest.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design clean layer boundaries',
            'Handle cross-cutting concerns without entanglement',
            'Prevent layer violations',
            'Keep modules independent',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Cross-Cutting Concerns', 'paras': [
                'Logging, auth, metrics, and error handling touch every layer. Entangling them into every function is duplication; the answer is middleware, decorators, or AOP that wrap the flow once. The concern stays separated — implemented once, applied everywhere.',
            ], 'code': {'lang': 'typescript', 'body': '''
// Cross-cutting concern via middleware: auth applied once
app.use('/api', authenticate);          // auth concern, one place
app.use('/api', logRequest);            // observability, one place
app.use('/api', errorBoundary);         // error handling, one place

// Handlers stay focused on business logic only:
app.get('/orders/:id', (req, res) => {
    const order = orders.get(req.params.id);
    res.json(order.toDto());
});'''}},
            {'heading': 'Enforcing Boundaries', 'paras': [
                'Layers decay without enforcement: a controller that queries the database directly is a layering violation that grows. Enforce with architecture tests (import rules), package visibility, and code review — same discipline as dependency inversion.',
            ]},
        ],
        'practice': {
            'title': 'Audit the Layers',
            'intro': 'A service where controllers query the DB, domain objects know the ORM, and email is sent from the repository.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Map every violation: where does each layer reach into another?'},
                {'label': 'Task 2', 'text': 'Refactor to clean boundaries (controller -> service -> repository -> infra).'},
                {'label': 'Task 3', 'text': 'Add the architecture test that fails on future violations.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why cross-cutting concerns should be applied once by middleware rather than repeated everywhere. Ask me to list the repeats in a typical handler.'},
            {'label': 'Implementation Design', 'text': 'Design the middleware chain for a checkout API: auth, rate limit, validation, logging, error handling. What order, and why?'},
            {'label': 'Boundary Testing', 'text': 'A legitimate query must read from a read replica — a layering exception. Design the boundary that allows it without opening the floodgates.'},
        ],
        'takeaways': [
            'Layers separate the what from the where',
            'Cross-cutting concerns belong in middleware, once',
            'Boundaries need enforcement (tests, visibility)',
            'Exceptions must be deliberate and narrow',
        ],
        'further': [
            {'title': 'Clean Architecture — Robert C. Martin', 'url': 'https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html'},
            {'title': 'Layered Architecture — Microsoft Docs', 'url': 'https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures'},
        ],
    },
    {
        'title': 'Advanced Separation of Concerns: Events and Domains',
        'desc': 'Event-driven decoupling, domain isolation, and concerns that span services.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Decouple concerns with events',
            'Design domain-event boundaries',
            'Isolate concerns across services',
            'Avoid event-driven entanglement',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Events as Decoupling', 'paras': [
                'Events let one concern (orders) announce facts without knowing who cares (inventory, email, analytics). Each consumer handles its concern independently — new consumers attach without changing the producer. This is separation of concerns across service boundaries.',
            ], 'code': {'lang': 'text', 'body': '''
Event-driven concern separation:
  orders service publishes: order.created, order.paid
  inventory service consumes: order.created  (stock concern)
  email service consumes:     order.paid     (notification concern)
  analytics consumes:         order.*        (metrics concern)

Producer knows nothing about consumers. Adding a concern =
adding a consumer, not editing the producer.'''}},
            {'heading': 'The Trap: Event Entanglement', 'paras': [
                'Events decouple producers from consumers but can couple consumers to each other if they share state or ordering expectations. The discipline: each consumer owns its concern and its read model; cross-consumer ordering assumptions are a hidden coupling.',
            ]},
        ],
        'practice': {
            'title': 'Design the Event Boundaries',
            'intro': 'A checkout publishes order.* events; three teams consume for inventory, email, and fraud.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the events and their payloads (stable, additive).'},
                {'label': 'Task 2', 'text': 'Verify no consumer depends on another consumer\'s processing order.'},
                {'label': 'Task 3', 'text': 'Design the consumer error policy: one consumer failing must not block the others.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain how events separate concerns without coupling consumers to the producer.'},
            {'label': 'Implementation Design', 'text': 'Design an outbox + event bus for a monolith splitting into services. Which concerns move to consumers first?'},
            {'label': 'Boundary Testing', 'text': 'Two consumers both update the same denormalized table — a shared concern. Design the ownership rule that prevents conflicts.'},
        ],
        'takeaways': [
            'Events let concerns attach without producer changes',
            'Each consumer owns its concern and its read model',
            'Cross-consumer ordering assumptions are hidden coupling',
            'Consumer failure isolation is part of the design',
        ],
        'further': [
            {'title': 'Domain Events — Martin Fowler', 'url': 'https://martinfowler.com/eaaDev/DomainEvent.html'},
            {'title': 'Event-Driven Architecture — AWS', 'url': 'https://aws.amazon.com/event-driven-architecture/'},
        ],
    },
    {
        'title': 'Separation of Concerns: Review & Mastery Quiz',
        'desc': 'Scenario questions on concerns, layers, and events.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate SoC concepts',
            'Separate tangled concerns',
            'Design event boundaries',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Separation of concerns divides a system by? (A: team / B: concern / C: size)',
                'Q2: Logging and auth are? (A: core concerns / B: cross-cutting concerns / C: layers)',
                'Q3: Cross-cutting concerns are best applied? (A: everywhere inline / B: once via middleware / C: never)',
                'Q4: True or false: events decouple producers from consumers.',
                'Q5: A controller querying the DB directly is? (A: a layering violation / B: best practice / C: a cache)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A payment notification handler validates, charges, emails, and updates a dashboard. Separate the concerns and design the event boundary.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "it works in one function" is not the same as "it is well-separated".'},
        ],
        'takeaways': [
            'Q1: B; Q2: B; Q3: B; Q4: true; Q5: A',
            'Separation makes each concern independently evolvable',
            'Events extend separation across services',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# SINGLE RESPONSIBILITY
# ─────────────────────────────────────────────────────────────────────────────
_t('single-responsibility', [
    {
        'title': 'Single Responsibility: One Reason to Change',
        'desc': 'Why a class with many jobs has many reasons to change — and why that is a bug.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Define single responsibility precisely',
            'Identify multiple responsibilities in a class',
            'Explain the "reasons to change" test',
            'Refactor a multi-job class',
        ],
        'prereqs': ['principles/separation-of-concerns', 'principles/information-hiding'],
        'sections': [
            {'heading': 'The Principle', 'paras': [
                'Single responsibility (SRP): a class should have one, and only one, reason to change. A class that parses, validates, persists, and emails has four reasons to change — a schema change, a validation rule change, an email template change each touch the same class, and they fight for it.',
                'The test: name the actor who asks for a change. If you can name two different actors who would change this class for different reasons, split it.',
            ], 'code': {'lang': 'java', 'body': '''
// Multiple responsibilities: parsing, validation, persistence, email
class OrderService {
    Order parse(String raw) { ... }
    void validate(Order o) { ... }
    void save(Order o) { ... }
    void sendConfirmation(Order o) { ... }
}

// One responsibility each:
class OrderParser      { Order parse(String raw) { ... } }
class OrderValidator   { void validate(Order o) { ... } }
class OrderRepository  { void save(Order o) { ... } }
class OrderMailer      { void sendConfirmation(Order o) { ... } }'''}},
            {'heading': 'Responsibility vs Single Method', 'paras': [
                'SRP is not "one method per class" — a class can have many methods serving one responsibility (a repository with find/create/delete serves persistence). The unit is the reason to change, not the line count.',
            ]},
        ],
        'practice': {
            'title': 'Split the God Class',
            'intro': 'A UserManager with 200 lines handling auth, profile, notifications, and audit.',
            'tasks': [
                {'label': 'Task 1', 'text': 'List the reasons to change and their actors (security team, product, compliance).'},
                {'label': 'Task 2', 'text': 'Split into role-focused classes with clear ownership.'},
                {'label': 'Task 3', 'text': 'Show how a security change now touches only the auth class.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about the "reasons to change" test. Start with a class you know with many jobs.'},
            {'label': 'Compare & Contrast', 'text': 'Compare SRP with separation of concerns. How are they the same idea at different scales?'},
            {'label': 'Boundary Testing', 'text': 'Two responsibilities are so small that splitting creates five tiny classes. Design the judgment call: when is a class "one responsibility" despite doing several small things?'},
        ],
        'takeaways': [
            'One reason to change per class',
            'Different actors mean different responsibilities',
            'SRP is about the unit of change, not line count',
            'Splitting isolates change and testing',
        ],
        'further': [
            {'title': 'Single Responsibility Principle — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Single-responsibility_principle'},
            {'title': 'SOLID — Robert C. Martin', 'url': 'https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html'},
        ],
    },
    {
        'title': 'Single Responsibility in Production: Services and Modules',
        'desc': 'Responsibility boundaries in services, modules, and teams.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design responsibility boundaries for services',
            'Align module ownership with change actors',
            'Prevent responsibility creep',
            'Balance granularity with operational cost',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Service Responsibility', 'paras': [
                'A microservice is a single responsibility with an owner: the payments service owns payment state, the identity service owns identity. The boundary is drawn where the reason to change diverges — two teams changing one service for different reasons is the service-level SRP violation.',
            ], 'code': {'lang': 'text', 'body': '''
Service responsibility test:
  - Who changes this service? (one team/actor = good)
  - Why do they change it? (one reason family = good)
  - Does another actor's change block this service's deploy?
If two actors must coordinate on every change, the service
has two responsibilities: split the boundary.'''}},
            {'heading': 'Responsibility Creep', 'paras': [
                'Services accumulate jobs over time ("it is easy to add here"). Responsibility creep shows up as a service that owns data it does not produce, sends emails it has no business sending, and blocks on concerns outside its domain. Regular ownership audits prune the creep.',
            ]},
        ],
        'practice': {
            'title': 'Audit the Services',
            'intro': 'A "user service" now handles auth, profiles, billing addresses, and marketing consent.',
            'tasks': [
                {'label': 'Task 1', 'text': 'List the responsibilities and their change actors.'},
                {'label': 'Task 2', 'text': 'Propose the boundary split (identity vs billing vs marketing) and what moves.'},
                {'label': 'Task 3', 'text': 'Decide whether to split now or extract modules first, with the triggers for each.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why service boundaries should follow change actors, not data ownership alone.'},
            {'label': 'Implementation Design', 'text': 'Design the extraction of billing from a user service: data migration, event contract, and deploy order.'},
            {'label': 'Boundary Testing', 'text': 'Two responsibilities genuinely share a transaction (profile + billing in one checkout). Design the boundary that respects the transaction.'},
        ],
        'takeaways': [
            'Service boundaries follow change actors',
            'Two actors coordinating on every change = split',
            'Responsibility creep is a creeping tax',
            'Extract in steps, not big-bang splits',
        ],
        'further': [
            {'title': 'Microservices Boundaries — Martin Fowler', 'url': 'https://martinfowler.com/articles/microservices.html'},
            {'title': 'DDD Bounded Contexts', 'url': 'https://martinfowler.com/bliki/BoundedContext.html'},
        ],
    },
    {
        'title': 'Advanced Single Responsibility: Transactions and Bounded Contexts',
        'desc': 'When responsibilities must cooperate, and domain boundaries that stay honest under transactions.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Handle cross-responsibility transactions',
            'Design bounded contexts with clean translations',
            'Use outboxes to keep boundaries without breaking transactions',
            'Detect boundary rot with dependency analysis',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'The Transaction Trap', 'paras': [
                'The strongest argument against splitting: "they share a transaction." But a single database transaction spanning two responsibilities is a coupling — the fix is the transactional outbox: each responsibility owns its writes, and the event that needs the other side is published atomically with its own write.',
            ], 'code': {'lang': 'text', 'body': '''
Keeping boundaries with a transaction:
  checkout creates order + publishes order.created
  -> one transaction, outbox table, relay publishes
  billing consumes order.created -> owns its ledger (separate tx)
  inventory consumes order.created -> owns its stock (separate tx)
No distributed transaction; each responsibility keeps its boundary.
Saga/compensation handles multi-step failures.'''}},
            {'heading': 'Bounded Contexts', 'paras': [
                'DDD bounded contexts give each responsibility its own model and language: "customer" in sales differs from "customer" in support. The boundary includes a translation layer (anti-corruption layer) so neither model leaks into the other.',
            ]},
        ],
        'practice': {
            'title': 'Redesign the Shared Transaction',
            'intro': 'Order creation writes orders + decrements inventory + charges payment in one transaction.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Identify the responsibilities entangled by the transaction.'},
                {'label': 'Task 2', 'text': 'Redesign with outbox + consumers, keeping atomicity per responsibility.'},
                {'label': 'Task 3', 'text': 'Design the compensation (saga) for the failure order: charge ok, stock failed.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why a shared transaction is a boundary violation even when it works.'},
            {'label': 'Implementation Design', 'text': 'Design the anti-corruption layer between sales "customer" and support "customer" models.'},
            {'label': 'Boundary Testing', 'text': 'A saga step is not idempotent. Design the idempotency guard that keeps the saga safe.'},
        ],
        'takeaways': [
            'Shared transactions are the boundary-violation trap',
            'Outbox + consumers keep atomicity per responsibility',
            'Bounded contexts need translation layers',
            'Sagas need idempotent steps',
        ],
        'further': [
            {'title': 'Bounded Context — Martin Fowler', 'url': 'https://martinfowler.com/bliki/BoundedContext.html'},
            {'title': 'Saga Pattern — Microservices.io', 'url': 'https://microservices.io/patterns/data/saga.html'},
        ],
    },
    {
        'title': 'Single Responsibility: Review & Mastery Quiz',
        'desc': 'Scenario questions on reasons to change, services, and boundaries.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate SRP concepts',
            'Detect multi-responsibility classes',
            'Design honest boundaries',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: SRP means one? (A: method / B: reason to change / C: file)',
                'Q2: A repository with find/create/delete has? (A: three responsibilities / B: one responsibility (persistence) / C: no responsibility)',
                'Q3: Two actors changing one service means? (A: good / B: split the boundary / C: merge teams)',
                'Q4: True or false: a shared database transaction across responsibilities is a coupling.',
                'Q5: The outbox pattern preserves? (A: one giant transaction / B: per-responsibility atomicity / C: nothing)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A "notification service" now owns templates, sends, retries, and unsubscribe. Redesign the responsibility split and the interface between them.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "it is one class, it is simpler" fails the moment two actors want different changes.'},
        ],
        'takeaways': [
            'Q1: B; Q2: B; Q3: B; Q4: true; Q5: B',
            'The reason to change is the unit of responsibility',
            'Boundaries survive transactions via outbox and sagas',
        ],
    },
])
