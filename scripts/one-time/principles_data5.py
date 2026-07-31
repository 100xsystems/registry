#!/usr/bin/env python3
"""Deep curriculum data chunk 5: graceful-degradation, idempotency, information-hiding, interface-segregation."""

TOPICS = {}


def _t(slug, topics):
    TOPICS[slug] = topics
    return topics


# ─────────────────────────────────────────────────────────────────────────────
# GRACEFUL DEGRADATION
# ─────────────────────────────────────────────────────────────────────────────
_t('graceful-degradation', [
    {
        'title': 'Graceful Degradation: Fail Partially, Stay Useful',
        'desc': 'Designing systems that keep delivering value as components fail, instead of going fully dark.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Define graceful degradation and its goals',
            'Identify degradable and non-degradable features',
            'Design fallbacks per dependency',
            'Communicate degraded state to users',
        ],
        'prereqs': ['principles/circuit-breaker', 'principles/fail-fast'],
        'sections': [
            {'heading': 'The Idea', 'paras': [
                'Graceful degradation means when a dependency fails, the system serves the next-best experience instead of an error page. The search engine that falls back to cached results, the checkout that queues payments, the map that loads without live traffic — each is a degraded-but-useful state.',
                'The alternative is the all-or-nothing failure: one dead dependency takes down the whole page, the whole app, the whole platform. Degradation converts a full outage into a partial, honest one.',
            ], 'code': {'lang': 'typescript', 'body': '''
// Degrade: serve cached data when the live API fails
async function getFeed(): Promise<Feed> {
    try {
        const live = await fetchFeedApi();
        cache.set('feed', live, 5 * 60_000);
        return live;
    } catch {
        const cached = cache.get('feed');
        if (cached) return cached;              // degraded but useful
        return { posts: [], degraded: true };   // honest empty state
    }
}'''}},
            {'heading': 'Degradable vs Essential', 'paras': [
                'Decide per feature: what is essential (must work or fail loudly) and what is augmentative (nice-to-have, degradable)? Augmentative features get fallbacks; essential features get redundancy and alarms.',
            ]},
        ],
        'practice': {
            'title': 'Map the Degradation Plan',
            'intro': 'A news home page depends on: breaking-news API, weather widget, comments, live scores.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Classify each dependency as essential or augmentative.'},
                {'label': 'Task 2', 'text': 'Design the fallback for each augmentative one (cached copy, hide widget, show empty).'},
                {'label': 'Task 3', 'text': 'Define how the UI communicates degraded state without alarming users.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about the difference between graceful degradation and hiding failures. Start with user communication.'},
            {'label': 'Compare & Contrast', 'text': 'Compare graceful degradation with fail-fast. When is each the right primary behavior, and how do they coexist?'},
            {'label': 'Boundary Testing', 'text': 'A fallback serves stale pricing for 10 minutes during a price-API outage. Is that graceful or dangerous? Design the guard.'},
        ],
        'takeaways': [
            'Degradation converts outages into partial, honest states',
            'Classify features: essential vs augmentative',
            'Fallbacks need staleness guards to stay safe',
            'Users must see that the state is degraded',
        ],
        'further': [
            {'title': 'Graceful Degradation — Nielsen Norman Group', 'url': 'https://www.nngroup.com/articles/graceful-degradation/'},
            {'title': 'Degradation Strategies — Azure Architecture', 'url': 'https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig'},
        ],
    },
    {
        'title': 'Graceful Degradation in Production: Fallback Hierarchies',
        'desc': 'Designing fallback chains, cached responses, and degraded modes that survive real incidents.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design multi-tier fallback hierarchies',
            'Use degraded modes with explicit status',
            'Protect fallbacks from becoming the bottleneck',
            'Operate degradation with runbooks',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Fallback Hierarchies', 'paras': [
                'A fallback chain: live data → cached (fresh TTL) → cached (stale allowed) → static defaults → error. Each tier is slightly worse but still useful, and each has its own staleness and cost profile.',
            ], 'code': {'lang': 'python', 'body': '''
# Fallback hierarchy for a recommendation feed
def recommendations(user_id):
    try:
        return live_recs(user_id)              # tier 1: live
    except Timeout:
        pass
    fresh = cache.get(f'recs:{user_id}')      # tier 2: fresh cache
    if fresh is not None:
        return fresh
    stale = cache.get(f'recs:{user_id}', allow_stale=True)
    if stale is not None:
        return stale, {'degraded': 'stale'}   # tier 3: stale
    return default_recs(), {'degraded': 'default'}  # tier 4: static'''}},
            {'heading': 'Protecting the Fallback', 'paras': [
                'If a million requests all hit the same fallback at once, the fallback becomes the new outage. Cap fallback throughput (rate limits, cached responses served at the edge) so the degraded path itself cannot collapse.',
            ]},
        ],
        'practice': {
            'title': 'Design the Fallback Chain',
            'intro': 'A maps service loses its live traffic layer. Users still need directions.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the chain: live traffic → cached traffic (10 min) → traffic-free map → static "directions unavailable".'},
                {'label': 'Task 2', 'text': 'Cap the fallback tier so it does not become the bottleneck.'},
                {'label': 'Task 3', 'text': 'Write the runbook: what the on-call does when the live layer recovers (flush stale cache, verify).'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why fallbacks need their own capacity planning. Ask me to compute the fallback QPS in a degradation scenario.'},
            {'label': 'Implementation Design', 'text': 'Design a degraded checkout that queues payments and reconciles later. What does the user see, and how does recovery work?'},
            {'label': 'Boundary Testing', 'text': 'Stale data in a fallback causes a user-visible contradiction (e.g., "in stock" for a sold-out item). Design the staleness guard and the UI hint.'},
        ],
        'takeaways': [
            'Fallback hierarchies trade quality for availability',
            'Each tier needs its own staleness and cost profile',
            'Fallbacks need capacity caps or they become the outage',
            'Runbooks define recovery, not just degradation',
        ],
        'further': [
            {'title': 'Resilience Patterns — Microsoft Docs', 'url': 'https://learn.microsoft.com/en-us/azure/architecture/patterns/category/resiliency'},
            {'title': 'Chaos Engineering — Principles', 'url': 'https://principlesofchaos.org/'},
        ],
    },
    {
        'title': 'Advanced Graceful Degradation: Adaptive Quality',
        'desc': 'Dynamic resolution, adaptive compression, and quality-of-service that adjusts to load.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Design adaptive quality tiers',
            'Use client hints for progressive enhancement',
            'Apply degradation at the edge (CDN)',
            'Measure the cost of each degraded state',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Adaptive Quality', 'paras': [
                'Instead of a fixed fallback, adapt quality to load: lower image resolution, thinner payloads, fewer widgets — driven by current capacity. Video streaming (adaptive bitrate) is the canonical example; the same principle applies to APIs returning lighter response shapes under pressure.',
            ], 'code': {'lang': 'typescript', 'body': '''
// Adaptive quality: lighter responses as load rises
function responseShape(load: number) {
    if (load < 0.6) return 'full';     // all fields, images, widgets
    if (load < 0.85) return 'core';    // essential fields only
    return 'minimal';                  // id + cached text, no media
}

// Client advertises capability; server adapts
app.get('/feed', (req, res) => {
    const shape = responseShape(loadAvg());
    res.json(trim(feed, shape));
});'''}},
            {'heading': 'Edge and Client Degradation', 'paras': [
                'CDNs and service workers let degradation happen without the origin: serve cached HTML at the edge when the origin is slow, or let the client render from a cached bundle offline. Progressive enhancement is client-side degradation: the page works without JS, then upgrades.',
            ]},
        ],
        'practice': {
            'title': 'Design Adaptive Response Shapes',
            'intro': 'A video platform serves 4K streams; under load, users still need playback.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the quality ladder (4K → 1080p → 720p → audio-only) and the load thresholds for stepping down.'},
                {'label': 'Task 2', 'text': 'Design the API response-shape ladder for the recommendations endpoint.'},
                {'label': 'Task 3', 'text': 'Measure the savings: how much bandwidth and CPU each step saves, and what users lose.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why adaptive quality needs hysteresis (don\'t oscillate between tiers).'},
            {'label': 'Implementation Design', 'text': 'Design an API that returns full, core, or minimal shapes with an explicit header so clients render accordingly. What contract does the client need?'},
            {'label': 'Boundary Testing', 'text': 'A load spike triggers minimal shape, and users complain they lost the media they paid for. Design the policy that protects premium features from degradation.'},
        ],
        'takeaways': [
            'Adapt quality to capacity instead of failing',
            'Response shapes and bitrates are degradation levers',
            'Edge caching and SWR make degradation invisible',
            'Hysteresis prevents tier oscillation',
        ],
        'further': [
            {'title': 'Adaptive Bitrate Streaming — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Adaptive_bitrate_streaming'},
            {'title': 'Service Workers — MDN', 'url': 'https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API'},
        ],
    },
    {
        'title': 'Graceful Degradation: Review & Mastery Quiz',
        'desc': 'Scenario questions on fallbacks, degradation tiers, and adaptive quality.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate degradation concepts',
            'Design fallback chains',
            'Communicate degraded states honestly',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Graceful degradation turns a full outage into? (A: a silent error / B: a partial, honest state / C: a retry loop)',
                'Q2: The first tier in a fallback chain is? (A: static defaults / B: live data / C: stale cache)',
                'Q3: Fallbacks can become the new outage if? (A: uncapped / B: cached / C: tested)',
                'Q4: True or false: degraded states should be invisible to users.',
                'Q5: Adaptive quality means? (A: fixed fallback / B: quality adjusts to load / C: always full quality)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A payment provider outage hits at 2am. Design the degraded checkout, the queued-payment reconciliation, and the morning recovery runbook.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "hide the broken widget" is degradation but "return 200 with wrong data" is not.'},
        ],
        'takeaways': [
            'Q1: B; Q2: B; Q3: A; Q4: false; Q5: B',
            'Degradation must be honest and capacity-planned',
            'Quality ladders extend degradation to the premium path',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# IDEMPOTENCY
# ─────────────────────────────────────────────────────────────────────────────
_t('idempotency', [
    {
        'title': 'Idempotency: Safe to Repeat',
        'desc': 'Why "do it once, or many times — same result" is the superpower of reliable systems.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Define idempotent and non-idempotent operations',
            'Explain why retries need idempotency',
            'Recognize idempotent HTTP methods',
            'Make a non-idempotent operation idempotent',
        ],
        'prereqs': ['principles/fail-fast', 'principles/eventual-consistency'],
        'sections': [
            {'heading': 'The Definition', 'paras': [
                'An operation is idempotent if applying it multiple times has the same effect as applying it once. DELETE /orders/123 is idempotent (the order is gone either way); POST /orders is not (each POST creates another order).',
                'Idempotency is what makes retries safe. Without it, "retry after timeout" can mean "charge the customer twice".',
            ], 'code': {'lang': 'http', 'body': '''
Idempotent HTTP methods:
  GET, HEAD, PUT, DELETE, OPTIONS  -> safe to repeat
  POST, PATCH                      -> NOT idempotent by default

Fix: add an Idempotency-Key header on POSTs
  POST /orders
  Idempotency-Key: c9d3-4410-9a1f
Retrying with the same key returns the same order, never a duplicate.'''}},
            {'heading': 'Why It Matters', 'paras': [
                'Networks fail, clients time out, servers crash mid-request, retries happen. Every one of those is a chance for a duplicated side effect. Idempotency converts "I do not know if it happened" into "it does not matter — the result is the same".',
            ]},
        ],
        'practice': {
            'title': 'Classify the Operations',
            'intro': 'Classify each as idempotent or not: set the user\'s name, increment a counter, add an item to a cart, refund a charge, send an email.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Justify each classification with the "run twice" test.'},
                {'label': 'Task 2', 'text': 'For the non-idempotent ones, design the fix (idempotency key, natural key, upsert).'},
                {'label': 'Task 3', 'text': 'Explain why "add to cart" repeated twice must be a cart with two items — and how the client prevents accidental doubles.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why idempotency keys must be unique per logical operation and stable across retries.'},
            {'label': 'Compare & Contrast', 'text': 'Compare idempotency keys, unique constraints, and upserts. When is each the right mechanism for "no duplicates"?'},
            {'label': 'Boundary Testing', 'text': 'A client retries with a new key by mistake. Design the server behavior that still prevents duplicates (natural-key uniqueness as backstop).'},
        ],
        'takeaways': [
            'Idempotent = repeated application, same result',
            'Retries without idempotency duplicate side effects',
            'Idempotency keys on POSTs make them repeatable',
            'Unique constraints backstop accidental key drift',
        ],
        'further': [
            {'title': 'Idempotency — Stripe API Guide', 'url': 'https://stripe.com/docs/api/idempotent_requests'},
            {'title': 'Idempotency Key Spec — IETF Draft', 'url': 'https://datatracker.ietf.org/doc/html/draft-ietf-httpapi-idempotency-key-header'},
        ],
    },
    {
        'title': 'Idempotency in Production: Keys, Stores, and Lifecycles',
        'desc': 'Designing idempotency-key stores, retention, and end-to-end idempotent pipelines.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design an idempotency-key store',
            'Handle concurrent requests with the same key',
            'Set key retention and cleanup policies',
            'Build idempotent event consumers',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'The Key Store', 'paras': [
                'The idempotency store maps key → response (or status). A request with a seen key returns the stored response; a new key records the in-flight operation. Concurrency: two simultaneous requests with the same key must resolve to one execution — the store\'s unique constraint on the key is the lock.',
            ], 'code': {'lang': 'sql', 'body': '''
-- Idempotency store: key unique, status tracks lifecycle
CREATE TABLE idempotency (
    key        text PRIMARY KEY,
    status     text NOT NULL,              -- in_progress | done | failed
    request    jsonb,
    response   jsonb,
    created_at timestamptz DEFAULT now()
);
-- Concurrent same-key: INSERT ... ON CONFLICT (key) DO NOTHING
INSERT INTO idempotency (key, status, request)
VALUES ($1, 'in_progress', $2)
ON CONFLICT (key) DO NOTHING
RETURNING status;   -- empty = another request already owns this key'''}},
            {'heading': 'Idempotent Consumers', 'paras': [
                'Event consumers see at-least-once delivery: the same event can arrive twice. Dedupe by event ID (store seen IDs, skip repeats) or process idempotently (upserts, set semantics). Both make replay and retry safe — which every pipeline eventually needs.',
            ]},
        ],
        'practice': {
            'title': 'Design the Key Lifecycle',
            'intro': 'A payment endpoint must be idempotent, and keys can be reused after 24 hours.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the store schema, the concurrency resolution, and the 24h retention cleanup.'},
                {'label': 'Task 2', 'text': 'Define behavior: same key + same request → stored response; same key + different request → 409.'},
                {'label': 'Task 3', 'text': 'Design the event consumer dedupe and the replay workflow.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why the idempotency check and the business action must be atomic (same transaction).'},
            {'label': 'Implementation Design', 'text': 'Design an idempotent refund API: two refund requests for the same charge must produce one refund. What key, what store, what conflict behavior?'},
            {'label': 'Boundary Testing', 'text': 'The idempotency store itself fails. Design the degraded path that still prevents double charges (or makes them detectable).'},
        ],
        'takeaways': [
            'The key store\'s unique constraint resolves concurrency',
            'Key + request must be checked atomically with the action',
            'Retention policies bound the store',
            'Event dedupe makes replay safe',
        ],
        'further': [
            {'title': 'Idempotent Consumers — Microservices.io', 'url': 'https://microservices.io/patterns/communication-style/idempotent-consumer.html'},
            {'title': 'Stripe Idempotent Requests', 'url': 'https://stripe.com/docs/api/idempotent_requests'},
        ],
    },
    {
        'title': 'Advanced Idempotency: Distributed and CRDT Approaches',
        'desc': 'Idempotency across services, and convergence tools that are idempotent by construction.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Propagate idempotency keys across service boundaries',
            'Use idempotent operations (upserts, CRDTs) by design',
            'Handle exactly-once claims honestly',
            'Design reconciliation for missed dedupes',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Cross-Service Idempotency', 'paras': [
                'An order flows through gateway → orders → payments → ledger. The original idempotency key must flow with the logical operation so each hop can dedupe against its own store — a duplicate at the gateway must not become a second payment further down.',
            ], 'code': {'lang': 'text', 'body': '''
Propagate the key end-to-end:
  POST /orders  (Idempotency-Key: K)
    -> orders service stores K, emits event {key: K, ...}
    -> payments service stores K for the charge
    -> ledger service stores K for the entry
Retry at any hop reuses K; each hop dedupes independently.
Exactly-once is really: at-least-once delivery + idempotent processing.'''}},
            {'heading': 'Idempotent by Construction', 'paras': [
                'Some operations are naturally idempotent: upserts (same data written twice = one row), set adds, max/overwrite semantics, CRDT merges. Design data models around these operations and much of the retry problem disappears.',
            ]},
        ],
        'practice': {
            'title': 'Propagate the Key',
            'intro': 'A checkout spans orders, payments, and inventory services. Payment retries are double-charging.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Trace the key from the client request through all three services and their events.'},
                {'label': 'Task 2', 'text': 'Design each hop\'s dedupe store and the conflict rule (same key, different payload → 409).'},
                {'label': 'Task 3', 'text': 'Design a nightly reconciliation that finds and fixes any double charge missed by dedupe.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why "exactly-once" is usually marketing for at-least-once plus idempotency. Ask me to prove it with a crash scenario.'},
            {'label': 'Implementation Design', 'text': 'Design a distributed file sync where uploads are idempotent by content hash. How do concurrent identical uploads converge?'},
            {'label': 'Boundary Testing', 'text': 'A key expires from the store but the client still retries. Design the backstop that prevents a duplicate payment after expiry.'},
        ],
        'takeaways': [
            'Keys must propagate end-to-end with the operation',
            'At-least-once + idempotency approximates exactly-once',
            'Upserts and CRDTs are idempotent by construction',
            'Reconciliation catches what dedupe misses',
        ],
        'further': [
            {'title': 'Exactly-Once Semantics — Kafka', 'url': 'https://kafka.apache.org/documentation/#semantics'},
            {'title': 'Transactional Outbox + Idempotency', 'url': 'https://microservices.io/patterns/data/transactional-outbox.html'},
        ],
    },
    {
        'title': 'Idempotency: Review & Mastery Quiz',
        'desc': 'Scenario questions on keys, stores, and idempotent pipelines.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate idempotency concepts',
            'Design key stores and lifecycles',
            'Build idempotent pipelines',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Which HTTP method is NOT idempotent by default? (A: PUT / B: POST / C: DELETE)',
                'Q2: The idempotency store prevents duplicates via? (A: TTL / B: unique key / C: retries)',
                'Q3: Exactly-once delivery really means? (A: at-least-once + idempotent processing / B: no retries / C: no failures)',
                'Q4: True or false: an upsert is naturally idempotent.',
                'Q5: Same key + different request should return? (A: 200 / B: 409 / C: retry)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A mobile app submits an order and the connection drops; the retry must not double-charge. Design the client key generation, server store, and retention.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why idempotency is a contract between the retrier and the retried.'},
        ],
        'takeaways': [
            'Q1: B; Q2: B; Q3: A; Q4: true; Q5: B',
            'Idempotency is the foundation of safe retries',
            'Design data models to be idempotent by construction',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# INFORMATION HIDING
# ─────────────────────────────────────────────────────────────────────────────
_t('information-hiding', [
    {
        'title': 'Information Hiding: Keep Secrets from Callers',
        'desc': 'Why the shape of your internals is a promise you should never make.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Define information hiding',
            'Distinguish interface from implementation',
            'Explain why exposed internals create coupling',
            'Apply private/encapsulation in code',
        ],
        'prereqs': ['principles/separation-of-concerns', 'principles/single-responsibility'],
        'sections': [
            {'heading': 'The Principle', 'paras': [
                'Information hiding (David Parnas): every module hides a design decision behind an interface. Callers depend on the interface, never on the internals — so the internals can change freely without breaking callers.',
                'The cost of leaking internals: callers read fields, subclass internals, and depend on ordering and format details. Every change to those internals ripples into every caller. The interface is the only contract, and it should stay small and stable.',
            ], 'code': {'lang': 'java', 'body': '''
// Leaked internals: callers depend on the backing list
class ShoppingCart {
    public List<Item> items = new ArrayList<>();  // public field!
    public double total() { ... }
}
// Caller: cart.items.add(...)  -> can corrupt invariants, tied to ArrayList

// Hidden: the representation is an implementation detail
class ShoppingCart {
    private final Map<String, Item> bySku = new HashMap<>();
    public void add(Item item) { bySku.merge(item.sku(), item, Item::combine); }
    public double total() { return bySku.values().stream().mapToDouble(Item::price).sum(); }
}'''}},
            {'heading': 'Interfaces Are Promises', 'paras': [
                'A public field, a public type, a public method is a promise. The more of the module you expose, the more promises you must keep forever. Hiding information is how you keep the surface area small and the freedom to evolve large.',
            ]},
        ],
        'practice': {
            'title': 'Tighten the Surface',
            'intro': 'A DateRange class exposes start, end, and a public List<LocalDate> of every day in the range.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Identify which exposures are implementation details (the day list) versus essential (start/end).'},
                {'label': 'Task 2', 'text': 'Make the day list private and expose days() as a computed, unmodifiable view.'},
                {'label': 'Task 3', 'text': 'Change the internal representation (e.g., store as interval) and show callers did not break.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why exposing the representation (list, map, array) is worse than exposing behavior.'},
            {'label': 'Compare & Contrast', 'text': 'Compare information hiding with encapsulation and abstraction. Where do they overlap and differ?'},
            {'label': 'Boundary Testing', 'text': 'A performance tool needs deep internals. Design the deliberate, narrow escape hatch that keeps the rest hidden.'},
        ],
        'takeaways': [
            'Hide design decisions behind interfaces',
            'Exposed internals become promises you must keep',
            'Small, stable surfaces enable large internal change',
            'Narrow escape hatches beat broad exposure',
        ],
        'further': [
            {'title': 'On the Criteria for Decomposing Systems (Parnas)', 'url': 'https://www.cs.umd.edu/class/spring2003/cmsc838p/Design/criteria.pdf'},
            {'title': 'Information Hiding — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Information_hiding'},
        ],
    },
    {
        'title': 'Information Hiding in Production: Modules and Packages',
        'desc': 'Module visibility, package boundaries, and API stability in real codebases.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design package/module visibility',
            'Use exported surface areas deliberately',
            'Manage cross-module dependencies',
            'Version public APIs while hiding internals',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Module Boundaries', 'paras': [
                'At module scale, information hiding is about the exported surface: which types and functions other modules may import. A module with everything public has no boundary; a module with a deliberate public API hides its evolution.',
            ], 'code': {'lang': 'text', 'body': '''
Module surface design:
  public:   types the contract needs (Order, OrderService)
  internal: helpers, adapters, representation (never importable)
  Private-by-default languages: Rust (pub), Go (exported), Java (package-private)

Rule: if a caller imports your internals, your module has no boundary.'''}},
            {'heading': 'API Stability', 'paras': [
                'The public API is a stability contract: callers compile against it, so breaking changes cost migrations. Hiding internals means the public API can stay stable while the internals evolve freely. Semantic versioning signals when the public surface does change.',
            ]},
        ],
        'practice': {
            'title': 'Audit the Exports',
            'intro': 'A library module exports 30 symbols; only 6 are used by consumers.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Identify the 6 that form the real API and move the rest to internal visibility.'},
                {'label': 'Task 2', 'text': 'Check the exported types: do any leak internal representation (e.g., a backing collection)?'},
                {'label': 'Task 3', 'text': 'Write the public API doc: what is promised, what is internal, what is experimental.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why "everything public" in a module is an anti-pattern and how visibility keywords encode the boundary.'},
            {'label': 'Implementation Design', 'text': 'Design a module that hides its persistence (SQL) behind a repository interface. What escapes if the SQL leaks?'},
            {'label': 'Boundary Testing', 'text': 'A consumer needs one internal helper. Design the path: promote it to the public API, duplicate it, or export a narrow "experimental" surface?'},
        ],
        'takeaways': [
            'Deliberate exported surfaces create real boundaries',
            'Internals leaking into imports destroy module independence',
            'Public APIs are stability contracts',
            'Experimental surfaces accommodate rare needs',
        ],
        'further': [
            {'title': 'The API Surface — Google Style Guides', 'url': 'https://google.github.io/styleguide/'},
            {'title': 'Semantic Versioning', 'url': 'https://semver.org/'},
        ],
    },
    {
        'title': 'Advanced Information Hiding: Capabilities and Security',
        'desc': 'Capability-based design, principle of least privilege, and hiding as a security boundary.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Use capability patterns for controlled exposure',
            'Design security boundaries with hidden internals',
            'Apply least privilege with information hiding',
            'Hide errors to avoid leaking internals',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Capabilities', 'paras': [
                'A capability is an unforgeable handle that grants access — passing the handle is the authorization. Instead of a globally-visible internal, a module hands out narrow capability objects that expose exactly one action, hiding everything else.',
            ], 'code': {'lang': 'python', 'body': '''
# Capability: hand out a narrow handle, hide the rest
class Wallet:
    def __init__(self, balance):
        self._balance = balance

    def transfer_capability(self):
        # only the transfer action is exposed; balance stays hidden
        class Transfer:
            def __init__(self, w): self._w = w
            def transfer(self, to, amount):
                self._w._balance -= amount
                to._balance += amount
        return Transfer(self)

w1, w2 = Wallet(100), Wallet(0)
cap = w1.transfer_capability()   # caller holds only 'transfer'
# caller cannot read _balance or mint new money'''}},
            {'heading': 'Errors Leak Internals', 'paras': [
                'Error messages that reveal stack traces, SQL, or file paths leak internal structure to attackers. Information hiding applies to errors: the user sees a sanitized message; the operator sees the full context in logs. This is both a robustness and a security boundary.',
            ]},
        ],
        'practice': {
            'title': 'Design a Capability Surface',
            'intro': 'A document service: editors need edit, viewers need read, admins need delete.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the capability objects (read-only, editable, admin) and what each hides.'},
                {'label': 'Task 2', 'text': 'Design the error boundary: what each role sees versus what logs record.'},
                {'label': 'Task 3', 'text': 'Explain how capabilities replace global role checks for access control.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why capabilities are more precise than global permissions.'},
            {'label': 'Implementation Design', 'text': 'Design a plugin API where plugins can read data but cannot touch the core\'s internals. What capabilities do you hand out?'},
            {'label': 'Boundary Testing', 'text': 'A leaked stack trace reveals the ORM and table names. Design the sanitization layer and the operator-only log channel.'},
        ],
        'takeaways': [
            'Capabilities are unforgeable, narrow handles',
            'Least privilege is information hiding applied to access',
            'Error messages must not leak internals',
            'Hiding is a security boundary, not just a design nicety',
        ],
        'further': [
            {'title': 'Capability-Based Security — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Capability-based_security'},
            {'title': 'OWASP — Error Handling', 'url': 'https://owasp.org/www-community/Improper_Error_Handling'},
        ],
    },
    {
        'title': 'Information Hiding: Review & Mastery Quiz',
        'desc': 'Scenario questions on surfaces, modules, and capabilities.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate information hiding concepts',
            'Design module surfaces',
            'Apply hiding to security',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Callers should depend on? (A: internals / B: the interface / C: the representation)',
                'Q2: A module with everything public has? (A: a strong boundary / B: no boundary / C: fewer bugs)',
                'Q3: Capabilities are? (A: global permissions / B: unforgeable narrow handles / C: passwords)',
                'Q4: True or false: error messages should include full stack traces for users.',
                'Q5: Public API changes should follow? (A: semver / B: no rules / C: internal whims)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A service exposes its data model in the API response, and now the schema cannot evolve. Redesign the response DTO boundary and the migration.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "it\'s all public anyway" destroys the ability to change anything.'},
        ],
        'takeaways': [
            'Q1: B; Q2: B; Q3: B; Q4: false; Q5: A',
            'Boundaries are what make evolution possible',
            'Hiding is both a design tool and a security tool',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# INTERFACE SEGREGATION
# ─────────────────────────────────────────────────────────────────────────────
_t('interface-segregation', [
    {
        'title': 'Interface Segregation: Fat Interfaces Hurt Callers',
        'desc': 'Why a "kitchen sink" interface forces every implementer to carry every method.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'State the interface segregation principle',
            'Recognize fat interfaces and their costs',
            'Split interfaces by client need',
            'Apply ISP to classes and modules',
        ],
        'prereqs': ['principles/single-responsibility', 'principles/information-hiding'],
        'sections': [
            {'heading': 'The Principle', 'paras': [
                'Interface Segregation (ISP): no client should be forced to depend on methods it does not use. A fat interface — read, write, delete, audit, export, render — forces every implementer to provide everything, and every change to any method ripples through all implementers and callers.',
                'The fix is small, role-specific interfaces: a Reader, a Writer, a Deleter. Each client depends only on the interface it actually uses.',
            ], 'code': {'lang': 'java', 'body': '''
// Fat interface: every implementer must do everything
interface OrderService {
    Order get(long id);
    void create(Order o);
    void update(Order o);
    void delete(long id);
    byte[] exportCsv(List<Long> ids);
}

// Segregated by role:
interface OrderReader  { Order get(long id); }
interface OrderWriter  { void create(Order o); void update(Order o); }
interface OrderDeleter { void delete(long id); }
interface OrderExporter { byte[] exportCsv(List<Long> ids); }

// A read-only view implements only OrderReader.'''}},
            {'heading': 'Costs of Fat Interfaces', 'paras': [
                'Implementers stub unused methods (UnsupportedOperationException), callers compile against methods they never use (and depend on their stability), and the interface becomes a coupling hub that changes constantly. Small interfaces change rarely because they encode one role.',
            ]},
        ],
        'practice': {
            'title': 'Split the Monolith Interface',
            'intro': 'A UserService interface has 12 methods: auth, profile, admin, reporting, and billing concerns.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Group the methods into role interfaces by consumer (auth client, admin panel, billing).'},
                {'label': 'Task 2', 'text': 'Refactor the admin panel to depend only on its role interface.'},
                {'label': 'Task 3', 'text': 'Show how adding a method to one role interface no longer affects other consumers.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about the difference between a fat interface and a cohesive one. Start with how clients group methods.'},
            {'label': 'Compare & Contrast', 'text': 'Compare ISP with single responsibility and role interfaces (Role Interface pattern). How do they reinforce each other?'},
            {'label': 'Boundary Testing', 'text': 'Two clients genuinely share 80% of an interface\'s methods. Design the split that does not multiply interfaces pointlessly.'},
        ],
        'takeaways': [
            'Clients should depend only on interfaces they use',
            'Fat interfaces couple implementers and callers together',
            'Role interfaces change rarely and independently',
            'Group by consumer, not by shared implementation',
        ],
        'further': [
            {'title': 'Interface Segregation Principle — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Interface_segregation_principle'},
            {'title': 'Role Interface — Martin Fowler', 'url': 'https://martinfowler.com/bliki/RoleInterface.html'},
        ],
    },
    {
        'title': 'Interface Segregation in Production: APIs and Services',
        'desc': 'Segregating service APIs, DTOs, and read models by consumer need.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Segregate service interfaces by consumer',
            'Design consumer-specific DTOs',
            'Use capability views for role-based access',
            'Manage API evolution with segregation',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Consumer-Specific DTOs', 'paras': [
                'A single fat response DTO forces every consumer to receive (and depend on) fields they do not use — and leaks data they should not see. Consumer-specific DTOs (or field projections) give each caller exactly the shape it needs.',
            ], 'code': {'lang': 'typescript', 'body': '''
// Fat DTO: every consumer gets everything
interface UserResponse { id, email, passwordHash, ssn, admin, creditCard, ... }

// Segregated DTOs per consumer
interface ProfileResponse { id, name, avatar }        // public profile
interface AdminUserView  { id, email, admin, status } // admin panel
interface BillingView    { id, creditCardLast4 }      // billing

// The endpoint projects the source entity into the consumer's shape.'''}},
            {'heading': 'Role-Based Views', 'paras': [
                'Segregation doubles as a security tool: the admin-only fields simply do not exist in the public interface. This is "principle of least privilege" applied to data shapes — the code cannot leak a field it does not expose.',
            ]},
        ],
        'practice': {
            'title': 'Project the Shapes',
            'intro': 'A single /users/:id returns 25 fields to everyone, including internal flags.',
            'tasks': [
                {'label': 'Task 1', 'text': 'List the consumer groups and the exact fields each needs.'},
                {'label': 'Task 2', 'text': 'Define the DTOs and the projection logic from the source entity.'},
                {'label': 'Task 3', 'text': 'Remove the internal flags from the public path and add a test that they never serialize.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why fat response DTOs are a security and coupling problem, not just a style issue.'},
            {'label': 'Implementation Design', 'text': 'Design the read-model split for a user service: profile, admin, billing, analytics views over one source of truth.'},
            {'label': 'Boundary Testing', 'text': 'A new consumer needs 3 more fields. Design the evolution path that does not fatten the shared DTO.'},
        ],
        'takeaways': [
            'DTOs should be shaped per consumer',
            'Segregation enforces least-privilege data exposure',
            'Projections keep one source of truth with many views',
            'New consumers get new views, not fatter ones',
        ],
        'further': [
            {'title': 'DTO vs View Models — Martin Fowler', 'url': 'https://martinfowler.com/eaaCatalog/dataTransferObject.html'},
            {'title': 'GraphQL: ask for exactly what you need', 'url': 'https://graphql.org/learn/queries/'},
        ],
    },
    {
        'title': 'Advanced Interface Segregation: Role Interfaces and Adapters',
        'desc': 'Role interfaces, adapter segregation, and keeping interfaces stable as systems grow.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Apply role interface patterns at module scale',
            'Segregate adapters from core ports',
            'Design stable interfaces under growth',
            'Detect fat interfaces with tooling',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Role Interfaces at Scale', 'paras': [
                'A module that plays many roles (a user is a reader, a writer, an admin) should expose role interfaces, not one god interface. Callers depend on the role, and a type can implement several roles without any caller seeing methods it does not use.',
            ], 'code': {'lang': 'go', 'body': '''
// Go: interfaces are implicitly implemented — segregation is natural
type Reader interface { Get(id string) (*User, error) }
type Writer interface { Create(u *User) error; Update(u *User) error }
type Admin   interface { Delete(id string) error }

// The service implements all three; callers take only what they need
func handlePublic(r Reader) { /* only Get */ }
func handleAdmin(a Admin)   { /* only Delete */ }

// Fat-interface detection: an interface with many methods that
// callers use sparsely is a segregation violation waiting to happen.'''}},
            {'heading': 'Adapter Segregation', 'paras': [
                'Adapters (HTTP, SQL, queue) should implement narrow ports rather than one adapter that does everything. A Postgres adapter that implements read, write, delete, audit, and export is a fat adapter — split it so each port has a focused implementation, testable in isolation.',
            ]},
        ],
        'practice': {
            'title': 'Detect and Split',
            'intro': 'A repository interface has 15 methods used by 6 different services.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Measure per-method usage across services to find the fat core.'},
                {'label': 'Task 2', 'text': 'Split into role ports (reader, writer, deleter, auditor) and adapters.'},
                {'label': 'Task 3', 'text': 'Add a lint/architecture check that flags interfaces used by disjoint consumers.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why implicit interfaces (Go) make segregation free while explicit ones (Java) require discipline.'},
            {'label': 'Implementation Design', 'text': 'Design the port split for an event bus used by producers, consumers, and administrators. What roles exist, and what does each port promise?'},
            {'label': 'Boundary Testing', 'text': 'Two role interfaces share a method that now changes semantics. Where does the change land, and who is affected?'},
        ],
        'takeaways': [
            'Role interfaces let types play many roles cleanly',
            'Adapters should be narrow and focused',
            'Implicit interfaces reduce segregation friction',
            'Tooling can detect fat interfaces before they hurt',
        ],
        'further': [
            {'title': 'Role Interface — Martin Fowler', 'url': 'https://martinfowler.com/bliki/RoleInterface.html'},
            {'title': 'Go: Interfaces and Composition', 'url': 'https://go.dev/doc/effective_go#interfaces'},
        ],
    },
    {
        'title': 'Interface Segregation: Review & Mastery Quiz',
        'desc': 'Scenario questions on fat interfaces, DTOs, and role ports.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate ISP concepts',
            'Split interfaces by consumer',
            'Apply segregation to data exposure',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: A fat interface forces implementers to? (A: implement everything / B: hide everything / C: ignore methods)',
                'Q2: Role interfaces group methods by? (A: implementation / B: consumer role / C: database table)',
                'Q3: Consumer-specific DTOs prevent? (A: duplication / B: leaking unused fields / C: caching)',
                'Q4: True or false: implicit interfaces (Go) make segregation easier.',
                'Q5: The main cost of a fat interface is? (A: coupling / B: performance / C: memory)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A shared library interface has 18 methods used by 5 apps, each using 4-6. Plan the role split and the migration that breaks nothing.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "one interface for everything" feels convenient now and costs you every change later.'},
        ],
        'takeaways': [
            'Q1: A; Q2: B; Q3: B; Q4: true; Q5: A',
            'Segregation is coupling control at the interface level',
            'Narrow interfaces change rarely and safely',
        ],
    },
])
