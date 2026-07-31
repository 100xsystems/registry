#!/usr/bin/env python3
"""Deep curriculum data batch 7: proxy, publish-subscribe, raft, replication, repository, retry."""

TOPICS = {}


def _t(slug, topics):
    TOPICS[slug] = topics
    return topics


# ─────────────────────────────────────────────────────────────────────────────
# PROXY
# ─────────────────────────────────────────────────────────────────────────────
_t('proxy', [
    {
        'title': 'Proxy: Control Access Through a Stand-In',
        'desc': 'A surrogate that controls access to a real object — lazy, remote, protected, or cached.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the proxy intent',
            'Describe the proxy kinds',
            'Build a lazy proxy',
            'Distinguish proxy from adapter',
        ],
        'prereqs': ['patterns/adapter', 'patterns/decorator'],
        'sections': [
            {'heading': 'The Problem', 'paras': [
                'Sometimes the real object is expensive to create, lives on another machine, or must be protected. The proxy implements the same interface as the real object and controls access to it — the caller cannot tell the difference. The real object stays untouched.',
            ], 'code': {'lang': 'java', 'body': '''
// Proxy kinds:
//   lazy proxy   — defer creating the expensive real object
//   remote proxy — translate calls to a remote service
//   protection   — check permissions before delegating
//   cache proxy  — answer from cache when possible

interface Image { void render(); }

class HugeImage implements Image {         // expensive to load
    HugeImage(String path) { loadFromDisk(path); }
    public void render() { /* draw */ }
}

class LazyImageProxy implements Image {    // same interface
    private HugeImage real;
    private final String path;
    LazyImageProxy(String p) { this.path = p; }
    public void render() {
        if (real == null) real = new HugeImage(path);  // load on first use
        real.render();
    }
}
// The caller uses the proxy exactly like the real image.'''}},
            {'heading': 'Proxy vs Adapter vs Decorator', 'paras': [
                'A proxy has the same interface and controls access. An adapter changes the interface to fit a client. A decorator adds behavior to the same interface. Proxies and decorators look alike in structure — the intent differs: control vs enhance.',
            ]},
        ],
        'practice': {
            'title': 'Build the Lazy Proxy',
            'intro': 'A gallery loads 1,000 high-res images at startup; most are never viewed.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Implement the proxy that defers loading to first render.'},
                {'label': 'Task 2', 'text': 'Add the cache proxy on top for revisited images.'},
                {'label': 'Task 3', 'text': 'Measure startup time and memory before and after.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why the proxy must keep the same interface. Start with the caller.'},
            {'label': 'Compare & Contrast', 'text': 'Compare proxy with adapter and decorator using one example each. When do the structures differ?'},
            {'label': 'Boundary Testing', 'text': 'The remote proxy retries a call while the real object mutates. Design the idempotency guard at the boundary.'},
        ],
        'takeaways': [
            'Proxy controls access with the same interface',
            'Lazy, remote, protection, and cache kinds',
            'Intent differs from adapter (interface) and decorator (behavior)',
            'Callers never know they hold a proxy',
        ],
        'further': [
            {'title': 'Proxy — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/proxy'},
            {'title': 'Proxy Pattern — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Proxy_pattern'},
        ],
    },
    {
        'title': 'Proxy in Production: Reverse Proxies and Gateways',
        'desc': 'Nginx, API gateways, and service meshes as proxies at the network boundary.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Describe the reverse proxy',
            'Use an API gateway proxy',
            'Apply caching and routing proxies',
            'Secure through a proxy',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Reverse Proxies', 'paras': [
                'A reverse proxy sits in front of services: it terminates connections, routes requests, terminates TLS, caches responses, and load balances. Nginx and Envoy are the workhorses. The proxy owns the edge — origins stay hidden and simpler.',
            ], 'code': {'lang': 'nginx', 'body': '''
# Nginx as a reverse proxy with caching
http {
  proxy_cache_path /var/cache/nginx keys_zone=api:10m;

  server {
    listen 443 ssl;
    ssl_certificate     /etc/nginx/tls/fullchain.pem;

    location /api/ {
        proxy_pass         http://backend-svc:8080;
        proxy_cache        api;
        proxy_cache_valid  200 60s;      # cache 200s for a minute
        proxy_set_header   X-Real-IP $remote_addr;
    }
  }
}
# The proxy handles TLS, routing, and caching so the backend
# never sees raw traffic or duplicate work.'''}},
            {'heading': 'Gateways and Meshes', 'paras': [
                'An API gateway is a reverse proxy with policy: auth, rate limiting, and routing by client type. A service mesh data plane proxies every service-to-service call, adding mTLS, retries, and observability. The proxy is where cross-cutting edge concerns live.',
            ]},
        ],
        'practice': {
            'title': 'Design the Edge',
            'intro': 'An API serves mobile and web clients; it needs TLS, auth, rate limits, and caching.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Map each concern to the right proxy layer (gateway, CDN, mesh).'},
                {'label': 'Task 2', 'text': 'Configure the routing and the caching rules per client type.'},
                {'label': 'Task 3', 'text': 'Design the failure mode: gateway down vs backend down.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why the edge proxy owns TLS, caching, and routing and what the origin keeps.'},
            {'label': 'Implementation Design', 'text': 'Design an API gateway config: auth per route, rate limits per client, cache TTLs. Where do you put each rule?'},
            {'label': 'Boundary Testing', 'text': 'The gateway caches a response that later changes. Design the cache-invalidation path (purge or short TTL).'},
        ],
        'takeaways': [
            'Reverse proxies own the edge: TLS, routing, caching',
            'API gateways add policy per client',
            'Service meshes proxy service-to-service calls',
            'Cache invalidation is a gateway contract',
        ],
        'further': [
            {'title': 'Nginx — reverse proxy docs', 'url': 'https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/'},
            {'title': 'What is a Service Mesh — Istio', 'url': 'https://istio.io/latest/about/service-mesh/'},
        ],
    },
    {
        'title': 'Advanced Proxy: Virtual Proxies and Copy-on-Write',
        'desc': 'Virtual proxies, COW proxies, and dynamic proxies at scale.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Build virtual proxies',
            'Use copy-on-write proxies',
            'Generate dynamic proxies',
            'Reason about proxy overhead',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Virtual and COW Proxies', 'paras': [
                'A virtual proxy stands in for a heavy object (a full document when only metadata is needed). A copy-on-write proxy lazily copies: multiple clients share one object until one mutates — the proxy clones on first write. Both defer cost until it is actually needed.',
            ], 'code': {'lang': 'java', 'body': '''
// Dynamic proxy: java.lang.reflect.Proxy generates the proxy class
import java.lang.reflect.*;

Service svc = (Service) Proxy.newProxyInstance(
    Service.class.getClassLoader(),
    new Class[]{Service.class},
    (proxy, method, args) -> {
        long start = System.nanoTime();
        Object result = method.invoke(realService, args);   // delegate
        long ms = (System.nanoTime() - start) / 1_000_000;
        metrics.record(method.getName(), ms);               // cross-cutting
        return result;
    });
// One handler instruments every method — no per-method wrapper code.
// Dynamic proxies power AOP, mocks, and retrofits of interfaces.'''}},
            {'heading': 'Overhead', 'paras': [
                'Every proxy adds a hop: a dispatch, a check, a round trip. In hot paths, proxy chains multiply latency and complicate debugging (stack traces show proxies). The discipline: proxy at boundaries where the control is worth the hop, and measure the added latency.',
            ]},
        ],
        'practice': {
            'title': 'Design the COW Cache',
            'intro': 'A 100-client shared config object must not be copied until a client edits it.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Implement the COW proxy with copy-on-first-write.'},
                {'label': 'Task 2', 'text': 'Add the dynamic proxy that instruments every access.'},
                {'label': 'Task 3', 'text': 'Measure the proxy overhead in a hot loop and decide where to bypass it.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why a COW proxy shares until mutation and what the first writer pays.'},
            {'label': 'Implementation Design', 'text': 'Design an AOP-style metrics proxy over a repository interface. What is recorded, and how do you keep it out of hot paths?'},
            {'label': 'Boundary Testing', 'text': 'A COW proxy is written by two clients concurrently. Design the synchronization that gives each a consistent copy.'},
        ],
        'takeaways': [
            'Virtual proxies defer heavy construction',
            'COW proxies share until first mutation',
            'Dynamic proxies instrument whole interfaces',
            'Proxy hops cost latency and debug clarity',
        ],
        'further': [
            {'title': 'java.lang.reflect.Proxy — Javadoc', 'url': 'https://docs.oracle.com/javase/8/docs/api/java/lang/reflect/Proxy.html'},
            {'title': 'Lazy loading and proxies — Martin Fowler', 'url': 'https://martinfowler.com/eaaCatalog/lazyLoad.html'},
        ],
    },
    {
        'title': 'Proxy: Review & Mastery Quiz',
        'desc': 'Scenario questions on kinds, edges, and overhead.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate proxy concepts',
            'Design the edge',
            'Measure proxy cost',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: A proxy implements? (A: the same interface / B: a new interface / C: no interface)',
                'Q2: A lazy proxy defers? (A: construction / B: rendering / C: deletion)',
                'Q3: A reverse proxy terminates? (A: connections and TLS / B: the database / C: the UI)',
                'Q4: True or false: an API gateway is a reverse proxy with policy.',
                'Q5: Copy-on-write proxies copy? (A: on first mutation / B: on read / C: never)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A microservices API needs TLS, auth, rate limits, and caching at the edge. Design the proxy layers and their responsibilities.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer the difference between controlling access and changing the interface.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Proxy = same interface, controlled access',
            'The edge is where proxies earn their keep',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# PUBLISH-SUBSCRIBE
# ─────────────────────────────────────────────────────────────────────────────
_t('publish-subscribe', [
    {
        'title': 'Publish-Subscribe: Decouple Producers from Consumers',
        'desc': 'Publishers emit to topics; subscribers receive; neither knows the other.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the pub-sub model',
            'Describe topics and subscriptions',
            'Decouple producers and consumers',
            'Compare with observer',
        ],
        'prereqs': ['patterns/observer', 'patterns/mediator'],
        'sections': [
            {'heading': 'The Model', 'paras': [
                'Publishers emit messages to a named topic. The broker routes each message to every subscriber of that topic. Publishers never know subscribers; subscribers never know publishers; new parties join without touching the others. The broker mediates the decoupling.',
            ], 'code': {'lang': 'python', 'body': '''
# Pub-sub: an in-process broker decouples sides
class Broker:
    def __init__(self):
        self.topics = {}

    def publish(self, topic, message):
        for sub in self.topics.get(topic, []):
            sub.on_message(message)

    def subscribe(self, topic, subscriber):
        self.topics.setdefault(topic, []).append(subscriber)

class EmailService:
    def on_message(self, msg):
        if msg.type == 'user_signed_up':
            send_welcome(msg.email)

broker = Broker()
broker.subscribe('user_events', EmailService())
broker.publish('user_events', Message('user_signed_up', email='a@b.com'))
# The email service never imports the publisher; the publisher
# never imports the email service.'''}},
            {'heading': 'Pub-Sub vs Observer', 'paras': [
                'Observer is in-process and direct: the subject holds observer references and notifies synchronously. Pub-sub adds a broker and a topic channel: the decoupling is stronger (no direct references at all) and it works across processes, at the cost of indirection, ordering, and delivery guarantees you must choose.',
            ]},
        ],
        'practice': {
            'title': 'Wire the Events',
            'intro': 'A signup flow publishes user_signed_up; email, analytics, and the CRM consume it.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the topics and the message shape.'},
                {'label': 'Task 2', 'text': 'Wire the three subscribers and prove neither side imports the other.'},
                {'label': 'Task 3', 'text': 'Add a fourth consumer without touching the publisher or the other three.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about what the broker adds over direct observer references. Start with cross-process.'},
            {'label': 'Compare & Contrast', 'text': 'Compare pub-sub with observer and with a plain queue. When is a topic (fan-out) the right shape?'},
            {'label': 'Boundary Testing', 'text': 'A subscriber is slow and blocks the broker. Design the async delivery or the bounded queue that isolates it.'},
        ],
        'takeaways': [
            'Pub-sub decouples via a broker and topics',
            'Publishers and subscribers never meet',
            'Fan-out is the defining shape',
            'Broker indirection adds delivery and ordering choices',
        ],
        'further': [
            {'title': 'Publish–subscribe pattern — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern'},
            {'title': 'Microsoft — publisher-subscriber guidance', 'url': 'https://learn.microsoft.com/en-us/azure/architecture/patterns/publisher-subscriber'},
        ],
    },
    {
        'title': 'Pub-Sub in Production: Kafka, RabbitMQ, and Delivery Guarantees',
        'desc': 'Broker architectures, partitions, offsets, and the delivery semantics you must choose.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Describe Kafka topics and partitions',
            'Choose delivery semantics',
            'Manage consumer groups',
            'Handle ordering',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Kafka: Durable Logs as Topics', 'paras': [
                'Kafka stores a topic as a partitioned, replicated log. Each partition orders messages; consumers in a group divide partitions. Durability is the differentiator: messages persist and replay, so late subscribers read history. Ordering is per-partition, not global — a constraint every design must respect.',
            ], 'code': {'lang': 'yaml', 'body': '''
# Kafka design decisions that shape guarantees:
#   partitions:        more = more parallelism, less global order
#   replication:       >1 keeps data through broker loss
#   acks: all         wait for all replicas before acknowledging
#   consumer group:   members split partitions (not messages)
#   offsets:          committed position per consumer; replay = reset
# Delivery semantics:
#   at-most-once   consumer commits before processing
#   at-least-once  consumer processes then commits (retries dupes)
#   exactly-once   transactional produce + commit (Kafka 0.11+)
# Choose per-topic: notifications tolerate dupes; payments do not.'''}},
            {'heading': 'RabbitMQ and Fan-Out', 'paras': [
                'RabbitMQ uses exchanges and queues: exchanges route to queues (direct, topic, fan-out), consumers pull from queues. The model fits request-reply and work distribution; Kafka fits log replay and stream processing. The choice: queue semantics (each message once per queue) vs log semantics (replayable history).',
            ]},
        ],
        'practice': {
            'title': 'Choose the Broker',
            'intro': 'A platform needs: (1) every service notified of user events, (2) a work queue for image resizing, (3) replayable audit history.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Map each need to a shape: topic fan-out, queue, or log.'},
                {'label': 'Task 2', 'text': 'Choose brokers and the delivery semantics per need.'},
                {'label': 'Task 3', 'text': 'Design ordering: what is per-partition and what breaks if you need global order?'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why Kafka orders within a partition and what global order would cost.'},
            {'label': 'Implementation Design', 'text': 'Design an event pipeline: user actions into Kafka, three consumers (email, analytics, search) in separate groups. What is the topic layout?'},
            {'label': 'Boundary Testing', 'text': 'A consumer crashes after processing but before committing. Design the at-least-once retry and the idempotent consumer.'},
        ],
        'takeaways': [
            'Kafka topics are partitioned, durable logs',
            'Ordering is per-partition, not global',
            'Delivery semantics are a per-topic choice',
            'Queues distribute work; logs enable replay',
        ],
        'further': [
            {'title': 'Kafka — documentation', 'url': 'https://kafka.apache.org/documentation/'},
            {'title': 'RabbitMQ — tutorial', 'url': 'https://www.rabbitmq.com/tutorials/tutorial-one-python.html'},
        ],
    },
    {
        'title': 'Advanced Pub-Sub: Exactly-Once and Stream Processing',
        'desc': 'Transactional messaging, idempotent consumers, and stream joins.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Achieve exactly-once pipelines',
            'Make consumers idempotent',
            'Join streams correctly',
            'Handle reprocessing',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Exactly-Once', 'paras': [
                'Exactly-once in messaging means the consumer\'s side effects and the offset commit are atomic. Kafka\'s transactions write both to the log in one transaction; otherwise the consumer must be idempotent — the same message applied twice changes nothing. Idempotency keys and upserts make at-least-once behave like exactly-once.',
            ], 'code': {'lang': 'go', 'body': '''
// Idempotent consumer: the effect, not the delivery, is exactly-once
func handle(msg Event) error {
    if processed, err := store.Exists(msg.ID); err != nil {
        return err
    } else if processed {
        return nil                      // already applied: skip
    }
    if err := applyEffect(msg); err != nil {   // the real work
        return err                      // don't commit; retry later
    }
    return store.MarkProcessed(msg.ID)  // record, then commit offset
}
// A crash between applyEffect and MarkProcessed re-delivers;
// the idempotency check makes the second apply a no-op.
// Exactly-once = at-least-once delivery + idempotent effect.'''}},
            {'heading': 'Stream Processing', 'paras': [
                'Stream processors (Kafka Streams, Flink) consume topics, transform, and produce topics — pub-sub as computation. Stateful joins and aggregations use local state backed by changelog topics. Reprocessing a topic (replay from an earlier offset) is the superpower and the hazard: downstream systems must tolerate the replay.',
            ]},
        ],
        'practice': {
            'title': 'Design the Idempotent Pipeline',
            'intro': 'A payment event topic is replayed during a recovery; the ledger must not double-post.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the idempotency key and the dedupe store.'},
                {'label': 'Task 2', 'text': 'Design the streaming join: orders topic + users topic -> enriched events.'},
                {'label': 'Task 3', 'text': 'Design the replay policy: what re-runs, what is skipped, and the markers that make it safe.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why idempotent effects beat transactional magic in practice.'},
            {'label': 'Implementation Design', 'text': 'Design a streaming aggregation with changelog state: how does a consumer recover its state after a crash?'},
            {'label': 'Boundary Testing', 'text': 'A replay delivers an old event that should have been superseded. Design the version guard that drops stale application.'},
        ],
        'takeaways': [
            'Exactly-once = idempotent effects + atomic commits',
            'Kafka transactions atomicize produce and consume',
            'Stream joins need recoverable local state',
            'Replay is powerful and demands idempotency',
        ],
        'further': [
            {'title': 'Kafka — exactly-once semantics', 'url': 'https://kafka.apache.org/documentation/#semantics'},
            {'title': 'Flink — stateful stream processing', 'url': 'https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/stateful-stream-processing/'},
        ],
    },
    {
        'title': 'Publish-Subscribe: Review & Mastery Quiz',
        'desc': 'Scenario questions on decoupling, brokers, and guarantees.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate pub-sub concepts',
            'Choose brokers and semantics',
            'Design idempotent pipelines',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Pub-sub decouples via? (A: a broker and topics / B: direct references / C: shared memory)',
                'Q2: Kafka orders messages? (A: within a partition / B: globally / C: never)',
                'Q3: A consumer group splits? (A: partitions / B: messages one by one / C: the broker)',
                'Q4: True or false: at-least-once delivery can duplicate messages.',
                'Q5: Exactly-once effects come from? (A: idempotency / B: luck / C: caching)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'An order system must notify 6 services and never double-charge on replay. Design the topics, semantics, and idempotency.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "once" in distributed messaging is a choice, not a default.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Brokers decouple; semantics are yours to choose',
            'Idempotency makes at-least-once feel exactly-once',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# RAFT
# ─────────────────────────────────────────────────────────────────────────────
_t('raft', [
    {
        'title': 'Raft: Consensus Made Understandable',
        'desc': 'Leader election, log replication, and safety — the approachable consensus protocol.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the Raft roles',
            'Describe leader election',
            'Understand log replication',
            'Know the safety guarantees',
        ],
        'prereqs': ['patterns/paxos', 'principles/quorum'],
        'sections': [
            {'heading': 'The Model', 'paras': [
                'Raft splits consensus into three subproblems: leader election (nodes pick one leader), log replication (the leader appends entries and replicates to a majority), and safety (elections only produce leaders with all committed entries). Every node is a leader, follower, or candidate — the roles are explicit.',
            ], 'code': {'lang': 'text', 'body': '''
Raft fundamentals:
  Terms: time is divided into terms; each term has at most one leader.
  Election: followers with no heartbeat become candidates, request
    votes, win with a majority, and start a new term.
  Log: the leader appends client commands to its log and replicates
    entries to followers; an entry is committed once a majority
    has it on disk.
  Safety (Election Restriction): a candidate only wins if its log
    is at least as up-to-date as a majority's — so a committed
    entry can never be overwritten by a new leader.
  Fencing: a higher term from any node demotes the current leader —
    a partitioned old leader cannot keep writing.'''}},
            {'heading': 'Why Raft Exists', 'paras': [
                'Paxos was famously hard to implement correctly. Raft restructures the same guarantees into understandable pieces — explicit roles, terms, and a single leader — and it is the consensus engine behind etcd, Consul, and CockroachDB.',
            ]},
        ],
        'practice': {
            'title': 'Trace an Election',
            'intro': 'A 5-node cluster loses its leader mid-term.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Trace: heartbeat timeout -> candidate -> vote request -> majority.'},
                {'label': 'Task 2', 'text': 'Show why a candidate with an older log cannot win.'},
                {'label': 'Task 3', 'text': 'Design the split-vote tie: no majority -> timeout -> new term.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why a higher term fences the old leader. Start with the partition.'},
            {'label': 'Compare & Contrast', 'text': 'Compare Raft with Paxos: same guarantees, different structure. Where are the practical wins?'},
            {'label': 'Boundary Testing', 'text': 'Two candidates split the vote repeatedly. Design the randomized election timeout that breaks the tie.'},
        ],
        'takeaways': [
            'Raft: explicit roles, terms, and one leader',
            'Commit requires a majority on disk',
            'Election restriction protects committed entries',
            'Terms fence stale leaders',
        ],
        'further': [
            {'title': 'The Raft Paper (with animations)', 'url': 'https://raft.github.io/raft.pdf'},
            {'title': 'Raft — secret life of data', 'url': 'https://thesecretlivesofdata.com/raft/'},
        ],
    },
    {
        'title': 'Raft in Production: etcd, Consul, and CockroachDB',
        'desc': 'How real systems run Raft for config, service discovery, and storage.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Describe etcd\'s Raft use',
            'Use Raft for service discovery',
            'Replicate storage with Raft',
            'Operate Raft clusters',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'etcd and Configuration', 'paras': [
                'etcd is a Raft-replicated key-value store: Kubernetes stores cluster state in it, and the Raft log guarantees every node sees the same writes. Reads are linearizable (the leader answers) or slightly stale (any node with a consistent snapshot). The replicated log is the coordination backbone.',
            ], 'code': {'lang': 'bash', 'body': '''
# etcd: a Raft-replicated configuration store
etcdctl put /config/feature-flags '{"checkout_v2": true}'
etcdctl get /config/feature-flags --prefix

# How Raft makes this safe:
#   put -> leader appends to its log -> replicates to a majority
#   -> committed -> applied to the state machine -> answered
# A minority of down nodes does not stop writes.
# The leader holds the write path; followers replicate and serve
# consistent reads via the commit index.'''}},
            {'heading': 'Storage Replication', 'paras': [
                'CockroachDB and TiKV replicate ranges with Raft: each range is a Raft group, and writes commit only after a majority of replicas durably store the log entry. Reads go through the same consensus (or a lease) so they see committed state. Raft turns a storage engine into a replicated state machine.',
            ]},
        ],
        'practice': {
            'title': 'Operate the Cluster',
            'intro': 'A 5-node etcd cluster must survive node failures, upgrades, and network partitions.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the upgrade: one node at a time while keeping quorum.'},
                {'label': 'Task 2', 'text': 'Design the failure response: what does quorum loss look like and how do you recover?'},
                {'label': 'Task 3', 'text': 'Set the election timeouts and heartbeat for your network latency.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why Raft needs an odd number of nodes and what quorum loss means. Ask me about a 2-node cluster.'},
            {'label': 'Implementation Design', 'text': 'Design a replicated lock service on Raft: how does the lease, the fencing token, and the quorum interact?'},
            {'label': 'Boundary Testing', 'text': 'A node is slow and triggers frequent elections. Design the leader stability (pre-vote, lease) that prevents flapping.'},
        ],
        'takeaways': [
            'etcd runs Raft for Kubernetes-grade config',
            'Each storage range is its own Raft group',
            'Quorum loss stops writes, not reads from peers',
            'Election tuning keeps leaders stable',
        ],
        'further': [
            {'title': 'etcd — documentation', 'url': 'https://etcd.io/docs/'},
            {'title': 'CockroachDB — Raft', 'url': 'https://www.cockroachlabs.com/docs/stable/architecture/replication-layer.html'},
        ],
    },
    {
        'title': 'Advanced Raft: Membership Changes and Snapshots',
        'desc': 'Adding and removing nodes safely, log compaction, and read leases.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Change membership safely',
            'Compact logs with snapshots',
            'Use read leases',
            'Diagnose Raft issues',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Membership Changes', 'paras': [
                'Changing the node set mid-flight is the classic Raft hazard: the old and new configurations can each form a majority that never overlaps. Raft solves this with joint consensus — the new config commits only when both old and new majorities agree — applied as a special log entry.',
            ], 'code': {'lang': 'text', 'body': '''
Safe membership change (joint consensus):
  1. Leader appends ConfChange(NewConfig) entry.
  2. The entry commits only when BOTH the old and new
     configurations have a majority — a joint quorum.
  3. Once committed, the cluster switches to the new config
     and the old config is retired.
This prevents the split-brain window where an old-majority and
a new-majority disagree.

Log compaction:
  - The log grows forever; snapshot the state machine at an index.
  - New members receive a snapshot + tail instead of the full log.
  - InstallSnapshot replaces the follower's state and log prefix.
Read leases:
  - A leader can serve reads without a quorum round-trip within
    its election lease (it cannot be deposed during the lease).'''}},
            {'heading': 'Diagnosis', 'paras': [
                'Common Raft failures: election flapping (too short timeouts or a slow node), quorum loss (even node count or a partitioned majority), and split-brain appearance (a fenced leader still serving reads). Logs and metrics — term changes, commit index lag, leader transitions — diagnose each.',
            ]},
        ],
        'practice': {
            'title': 'Grow the Cluster',
            'intro': 'A 3-node Raft cluster must grow to 5 nodes during traffic without downtime.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the joint-consensus membership change sequence.'},
                {'label': 'Task 2', 'text': 'Design the snapshot strategy for a node added with a huge log.'},
                {'label': 'Task 3', 'text': 'Set the observability: leader changes, commit lag, snapshot traffic.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why joint consensus prevents the membership split-brain window.'},
            {'label': 'Implementation Design', 'text': 'Design a snapshot policy: when to snapshot, how install works, and how a brand-new node catches up.'},
            {'label': 'Boundary Testing', 'text': 'A leader serves reads from a stale state after a partition. Design the lease check that detects and demotes it.'},
        ],
        'takeaways': [
            'Joint consensus makes membership changes safe',
            'Snapshots bound the log and catch up new nodes',
            'Read leases avoid quorum round trips',
            'Term and lag metrics diagnose failures',
        ],
        'further': [
            {'title': 'Raft — cluster membership changes', 'url': 'https://raft.github.io/raft.pdf'},
            {'title': 'etcd — Raft internals', 'url': 'https://etcd.io/docs/v3.5/learning/raft-internals/'},
        ],
    },
    {
        'title': 'Raft: Review & Mastery Quiz',
        'desc': 'Scenario questions on roles, operations, and safety.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate Raft concepts',
            'Operate clusters',
            'Design membership',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Raft has the roles? (A: leader, follower, candidate / B: master, slave, proxy / C: writer, reader, cache)',
                'Q2: A log entry commits when? (A: a majority stores it / B: the leader stores it / C: everyone votes)',
                'Q3: A higher term? (A: fences the old leader / B: speeds writes / C: shrinks the log)',
                'Q4: True or false: Raft needs an odd number of nodes.',
                'Q5: Membership changes use? (A: joint consensus / B: a coin flip / C: DNS)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A config cluster must grow from 3 to 5 nodes live. Design the joint-consensus steps and the snapshot plan.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why Raft is Paxos restructured, not a new idea.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Explicit roles and terms make consensus implementable',
            'Safety is a matter of quorums and fencing',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# REPLICATION
# ─────────────────────────────────────────────────────────────────────────────
_t('replication', [
    {
        'title': 'Replication: Copies for Availability',
        'desc': 'Keeping identical copies of data across nodes so reads scale and failures survive.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain replication purposes',
            'Describe replication models',
            'Understand consistency trade-offs',
            'Choose replication factors',
        ],
        'prereqs': ['patterns/leader-follower', 'patterns/multi-leader'],
        'sections': [
            {'heading': 'Why Replicate', 'paras': [
                'Replication serves three goals: high availability (a node dies, others serve), read scaling (more copies, more read throughput), and latency (a copy near every region). The cost is consistency: replicas can diverge, and the replication lag decides what readers see.',
            ], 'code': {'lang': 'text', 'body': '''
Replication models:
  Single-leader: one writer, many readers (Postgres, MySQL)
    - strong write order; reads may lag
  Multi-leader: several writers, replicated between (offline-first)
    - write locality; needs conflict resolution
  Leaderless (quorum): writes go to N nodes, reads from N (Dynamo)
    - tunable consistency; needs read repair / anti-entropy
Consistency spectrum:
  Strong: reads always see the latest committed write
  Eventual: replicas converge, readers may see stale data
  Read-your-writes: your own writes are visible to you
  Monotonic: reads never go backward in time
Replication factor: the number of copies. Higher = more fault
tolerance and read capacity, but more write cost and lag risk.'''}},
            {'heading': 'Choosing a Model', 'paras': [
                'Pick single-leader when writes must be ordered and simple (most OLTP). Pick multi-leader for multi-region writes or offline apps. Pick leaderless when availability and partition tolerance beat strict ordering (carts, counters). The data\'s semantics — not fashion — choose the model.',
            ]},
        ],
        'practice': {
            'title': 'Choose the Replication',
            'intro': 'A global inventory app: writes happen in any region; double-selling must never happen.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Evaluate the three models against the write-ordering requirement.'},
                {'label': 'Task 2', 'text': 'Design the chosen model with its consistency policy.'},
                {'label': 'Task 3', 'text': 'Show the failure mode of each rejected model for this workload.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why more copies mean more consistency work. Start with a read.'},
            {'label': 'Compare & Contrast', 'text': 'Compare single-leader, multi-leader, and leaderless with one workload each. Where do the guarantees differ?'},
            {'label': 'Boundary Testing', 'text': 'A replica lags 30 seconds and a user sees their order missing. Design the read-your-writes routing that fixes it.'},
        ],
        'takeaways': [
            'Replication buys availability, reads, and locality',
            'Lag is the price; consistency policies manage it',
            'Model choice follows write semantics',
            'Replication factor tunes fault tolerance vs cost',
        ],
        'further': [
            {'title': 'Replication — DDIA Ch. 5', 'url': 'https://dataintensive.net/'},
            {'title': 'PostgreSQL — streaming replication', 'url': 'https://www.postgresql.org/docs/current/warm-standby.html'},
        ],
    },
    {
        'title': 'Replication in Production: Streams and Quorums',
        'desc': 'Log-based replication, quorum reads/writes, and operational lag management.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Replicate via logs',
            'Tune quorums',
            'Monitor replication lag',
            'Handle replica failures',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Log-Based Replication', 'paras': [
                'Modern systems replicate through logs: the leader\'s write-ahead log or a dedicated change stream (binlog, CDC) ships to replicas, which replay it. Log-based replication is decoupled from application code — triggers and dual-writes are unnecessary — and enables stream consumers (analytics, search) too.',
            ], 'code': {'lang': 'yaml', 'body': '''
Replication architecture (Postgres example):
  primary -> WAL streaming -> standby 1, standby 2
  - synchronous standby: the primary waits for one standby to
    ack before answering (zero-loss failover window)
  - asynchronous: faster writes, possible small loss on failover
  Replication slots: ensure the primary retains WAL the standby
    has not consumed yet (prevents silent divergence)
  Lag monitoring: replay_lag per standby; alert when it grows
  CDC: logical replication publishes changes as events for
    downstream systems (search index, analytics, warehouses)'''}},
            {'heading': 'Quorums', 'paras': [
                'Leaderless systems tune consistency with quorums: write to W nodes, read from R nodes, and require W + R > N to guarantee a reader sees the latest write. W=3, R=1 favors reads; W=1, R=3 favors writes. Failures below the quorum reject the operation — availability is tunable, not absolute.',
            ]},
        ],
        'practice': {
            'title': 'Operate the Replicas',
            'intro': 'A primary + 2 standbys serve 95% reads from replicas; a replica lags during nightly loads.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the lag alert and the read-routing guard.'},
                {'label': 'Task 2', 'text': 'Choose sync vs async for the loss budget.'},
                {'label': 'Task 3', 'text': 'Design the failover drill and the promotion checklist.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why W + R > N guarantees a fresh read in leaderless systems.'},
            {'label': 'Implementation Design', 'text': 'Design a CDC pipeline: database changes to a search index with lag bounds. What breaks if the index lags?'},
            {'label': 'Boundary Testing', 'text': 'A replica diverges silently (a missed WAL segment). Design the checksum/consistency check that detects and repairs it.'},
        ],
        'takeaways': [
            'Logs replicate without application coupling',
            'W + R > N is the quorum freshness rule',
            'Lag is monitored and routed around',
            'Sync vs async sets the failover loss budget',
        ],
        'further': [
            {'title': 'Dynamo — quorum replication', 'url': 'https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf'},
            {'title': 'PostgreSQL — replication', 'url': 'https://www.postgresql.org/docs/current/runtime-config-replication.html'},
        ],
    },
    {
        'title': 'Advanced Replication: Conflict Resolution and Consistency Models',
        'desc': 'Convergent state, CRDTs, and the consistency menu in depth.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Resolve replication conflicts',
            'Apply consistency models',
            'Design convergent systems',
            'Reason about availability',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'The CAP Trade', 'paras': [
                'CAP says a partition forces a choice: consistency (refuse to serve) or availability (serve possibly stale). Most systems choose availability and manage the consequences with conflict resolution and consistency policies. The practical design question is: during a partition, what do reads and writes return?',
            ], 'code': {'lang': 'python', 'body': '''
# Convergent replication: LWW vs CRDT under partition
# LWW: keep the (value, timestamp) with the highest timestamp
def lww_merge(a, b):
    return a if a[1] >= b[1] else b      # loses the older update

# CRDT G-Counter: elementwise max, value = sum — nothing is lost
def counter_merge(ca, cb):
    return [max(x, y) for x, y in zip(ca, cb)]

# Set with tombstones: adds union, removes tracked, apply both
def set_merge(sa, sb):
    adds = sa.adds | sb.adds
    removes = sa.removes | sb.removes
    return adds - removes
# Deterministic merges converge without a coordinator — the
# replication topology becomes irrelevant to correctness.'''}},
            {'heading': 'The Consistency Menu', 'paras': [
                'Beyond strong and eventual: read-your-writes, monotonic reads, bounded staleness, and causal consistency each solve a specific user-visible failure. The cheapest correct option wins — causal consistency (DynamoDB) covers most real app needs without global ordering.',
            ]},
        ],
        'practice': {
            'title': 'Design the Convergent Store',
            'intro': 'A wishlist syncs across devices; adds, removes, and reorders happen offline on every device.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the operation-based CRDTs for each operation.'},
                {'label': 'Task 2', 'text': 'Show the LWW alternative and which user-visible update it loses.'},
                {'label': 'Task 3', 'text': 'State the consistency model your design actually delivers.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why CRDT merges make the topology irrelevant.'},
            {'label': 'Implementation Design', 'text': 'Design a messaging system with causal ordering: messages within a conversation appear in cause-effect order across devices. What is the causality mechanism?'},
            {'label': 'Boundary Testing', 'text': 'A device offline for a week merges a huge backlog. Design the merge, the conflict surface, and the user-visible reconciliation.'},
        ],
        'takeaways': [
            'Partitions force consistency vs availability choices',
            'CRDTs converge deterministically under any topology',
            'The consistency menu offers cheaper correct options',
            'Causal consistency covers most app needs',
        ],
        'further': [
            {'title': 'CAP Theorem — Brewer', 'url': 'https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/'},
            {'title': 'CRDTs — crdt.tech', 'url': 'https://crdt.tech/'},
        ],
    },
    {
        'title': 'Replication: Review & Mastery Quiz',
        'desc': 'Scenario questions on models, quorums, and conflicts.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate replication concepts',
            'Tune quorums',
            'Resolve conflicts',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Replication buys? (A: availability and read scaling / B: stronger CPUs / C: smaller disks)',
                'Q2: The price of replication is? (A: lag and consistency work / B: nothing / C: speed)',
                'Q3: W + R > N guarantees? (A: a fresh read / B: no writes / C: compression)',
                'Q4: True or false: CAP forces a choice during partitions.',
                'Q5: CRDTs converge? (A: deterministically / B: randomly / C: never)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A global cart service must work during a region partition. Design the model, the quorums, and the merge.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "just add replicas" is where the real design work begins.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Replicas give availability; you pay in consistency',
            'Quorums and CRDTs manage the payment',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# REPOSITORY
# ─────────────────────────────────────────────────────────────────────────────
_t('repository', [
    {
        'title': 'Repository: Abstract the Data Layer',
        'desc': 'A collection-like interface over persistence so the domain never talks to the database.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the repository intent',
            'Hide query details',
            'Return domain objects',
            'Test with fakes',
        ],
        'prereqs': ['principles/dependency-inversion', 'patterns/factory'],
        'sections': [
            {'heading': 'The Problem', 'paras': [
                'Domain code that runs SQL directly couples business logic to the database and makes testing slow. The repository presents a collection-like interface — find(id), add(entity), remove(entity) — and hides the persistence technology behind it. The domain depends on the interface; the adapter depends on the database.',
            ], 'code': {'lang': 'typescript', 'body': '''
// Repository: the domain sees a collection, not a database
interface OrderRepository {
    findById(id: string): Order | null;
    findByCustomer(customerId: string): Order[];
    add(order: Order): void;
    remove(order: Order): void;
}

// Production adapter: SQL under the interface
class PostgresOrderRepository implements OrderRepository {
    constructor(private db: Pool) {}
    async findById(id: string) {
        const row = await this.db.query(
            'SELECT * FROM orders WHERE id = $1', [id]);
        return row.rows[0] ? Order.fromRow(row.rows[0]) : null;
    }
    // add/remove translate to INSERT/DELETE here
}

// The domain uses the interface; tests use an in-memory fake.'''}},
            {'heading': 'Repository vs DAO', 'paras': [
                'A DAO (data access object) exposes table-shaped operations: findById, insert — close to SQL. A repository speaks the domain language: findOpenOrdersFor(customer) — it returns domain objects and encapsulates the query policy. Repositories sit above DAOs and are the domain-facing contract.',
            ]},
        ],
        'practice': {
            'title': 'Wrap the Database',
            'intro': 'An order service queries SQL in 30 places; tests hit a real database.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the repository interface in domain terms.'},
                {'label': 'Task 2', 'text': 'Implement the Postgres adapter and the in-memory fake.'},
                {'label': 'Task 3', 'text': 'Migrate the 30 call sites and run the tests against the fake.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why the repository speaks the domain language rather than SQL. Start with the method names.'},
            {'label': 'Compare & Contrast', 'text': 'Compare repository with DAO and with the unit-of-work pattern. What does each layer own?'},
            {'label': 'Boundary Testing', 'text': 'A query needs a paginated, filtered shape. Design the repository method or the specification object that keeps the interface domain-friendly.'},
        ],
        'takeaways': [
            'Repository hides persistence behind a collection interface',
            'It returns domain objects and speaks domain language',
            'The domain depends on the interface, never the DB',
            'Fakes make tests fast and deterministic',
        ],
        'further': [
            {'title': 'Repository — Martin Fowler (P of EAA)', 'url': 'https://martinfowler.com/eaaCatalog/repository.html'},
            {'title': 'Repository pattern — Microsoft', 'url': 'https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/infrastructure-persistence-layer-design'},
        ],
    },
    {
        'title': 'Repository in Production: ORMs and Data Mappers',
        'desc': 'ORM repositories, query objects, and read models for reports.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Combine repositories with ORMs',
            'Design query objects',
            'Separate write and read models',
            'Avoid leaking the ORM',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'ORM Repositories', 'paras': [
                'ORMs (Hibernate, TypeORM, Prisma) provide generic repositories, but generic CRUD leaks: filters and joins leak into the domain, and N+1 query patterns appear. The fix is a domain-specific repository per aggregate that owns its query shapes, plus explicit fetching policies inside the repository.',
            ], 'code': {'lang': 'typescript', 'body': '''
// Domain repository over Prisma — the ORM stays inside
export class OrderRepository {
    constructor(private prisma: PrismaClient) {}

    async findOpenForCustomer(customerId: string): Promise<Order[]> {
        const rows = await this.prisma.order.findMany({
            where: { customerId, status: 'OPEN' },
            include: { items: true },      // fetch policy lives here
            orderBy: { createdAt: 'desc' },
        });
        return rows.map(Order.fromPrisma);
    }
    // No .findMany with raw filters escapes this class.
    // The domain never imports Prisma.'''}},
            {'heading': 'Read Models', 'paras': [
                'Writes go through repositories; heavy reports read through dedicated read models (views, projections, or a query service) that are shaped for the screen — no ORM graph walking. This is CQRS-lite: separate the write path from the read path so neither compromises the other.',
            ]},
        ],
        'practice': {
            'title': 'Harden the Repository',
            'intro': 'An order list screen triggers N+1 queries through the generic ORM repository.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Replace the generic call with a domain repository that owns the include policy.'},
                {'label': 'Task 2', 'text': 'Add the read model for the report screen.'},
                {'label': 'Task 3', 'text': 'Measure the query count before and after.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why generic ORM repositories leak queries into the domain and how owning the shapes fixes it.'},
            {'label': 'Implementation Design', 'text': 'Design a repository set for an e-commerce aggregate: order, customer, and the read model for dashboards.'},
            {'label': 'Boundary Testing', 'text': 'A developer bypasses the repository with a direct ORM call. Design the architecture test that fails the build.'},
        ],
        'takeaways': [
            'Domain-specific repositories own query shapes',
            'Fetch policies (includes) live inside the repository',
            'Read models serve reports without ORM walking',
            'Architecture tests stop repository bypasses',
        ],
        'further': [
            {'title': 'CQRS — Martin Fowler', 'url': 'https://martinfowler.com/bliki/CQRS.html'},
            {'title': 'Prisma — data modeling', 'url': 'https://www.prisma.io/docs/concepts/components/prisma-schema/data-modeling'},
        ],
    },
    {
        'title': 'Advanced Repository: Specifications and Data Mappers',
        'desc': 'Specification objects for complex queries, and mapper patterns for rich domains.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Design specification objects',
            'Build composable queries',
            'Map between models cleanly',
            'Handle transactions and units of work',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Specifications', 'paras': [
                'When repository methods multiply (findActive, findActiveInCity, findActiveInCityAfter), a specification object captures the predicate as data: repository.find(spec). Specifications compose (AND, OR, NOT) and translate to SQL or to in-memory filters — the same object works for query and test.',
            ], 'code': {'lang': 'java', 'body': '''
// Specification: predicates as data, composable
interface Spec<T> { boolean isSatisfiedBy(T t); }
class And<T> implements Spec<T> {
    private final Spec<T> a, b;
    And(Spec<T> a, Spec<T> b) { this.a = a; this.b = b; }
    public boolean isSatisfiedBy(T t) { return a.isSatisfiedBy(t) && b.isSatisfiedBy(t); }
}

class CustomerIsActive implements Spec<Customer> {
    public boolean isSatisfiedBy(Customer c) { return c.isActive(); }
}
class CustomerInCity implements Spec<Customer> {
    private final String city;
    CustomerInCity(String city) { this.city = city; }
    public boolean isSatisfiedBy(Customer c) { return c.city().equals(city); }
}
// repository.find(new And<>(new CustomerIsActive(), new CustomerInCity("NY")))
// The same Spec predicates drive the SQL translation (via a mapper)
// and the in-memory filter — one definition, two engines.'''}},
            {'heading': 'Data Mappers', 'paras': [
                'A data mapper transfers between the domain model and the database schema without either knowing the other — unlike active record, where the domain object carries its own persistence. Mappers enable rich domains at the cost of a translation layer that must stay explicit and tested.',
            ]},
        ],
        'practice': {
            'title': 'Compose the Query',
            'intro': 'A report screen needs 12 filter combinations over customers; the repository methods multiply.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the specification objects and the compositions.'},
                {'label': 'Task 2', 'text': 'Translate the specs to SQL and verify the generated queries.'},
                {'label': 'Task 3', 'text': 'Use the same specs in memory for the test fake.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why specifications stop repository-method explosion.'},
            {'label': 'Implementation Design', 'text': 'Design a filter UI backed by specifications: how do checkbox states become a composed query?'},
            {'label': 'Boundary Testing', 'text': 'A spec translates to SQL that is 10x slower than a hand-written query. Design the plan inspection or the query-object escape hatch.'},
        ],
        'takeaways': [
            'Specifications compose predicates as data',
            'One spec drives SQL and in-memory filters',
            'Data mappers decouple domain from schema',
            'Query complexity needs escape hatches',
        ],
        'further': [
            {'title': 'Specification — Martin Fowler', 'url': 'https://martinfowler.com/apsupp/spec.pdf'},
            {'title': 'Data Mapper — P of EAA', 'url': 'https://martinfowler.com/eaaCatalog/dataMapper.html'},
        ],
    },
    {
        'title': 'Repository: Review & Mastery Quiz',
        'desc': 'Scenario questions on abstractions, ORMs, and specifications.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate repository concepts',
            'Design interfaces',
            'Compose queries',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: A repository presents? (A: a collection-like interface / B: SQL directly / C: the cache)',
                'Q2: A DAO exposes? (A: table-shaped operations / B: domain language / C: the UI)',
                'Q3: Domain code should depend on? (A: the repository interface / B: the database driver / C: the ORM)',
                'Q4: True or false: specifications compose like predicates.',
                'Q5: A data mapper keeps? (A: domain and schema decoupled / B: one object / C: the DB busy)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'An order service with 30 ad-hoc queries needs a clean persistence boundary. Design the repository set and the test fakes.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why the database should be the last thing the domain knows about.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'The repository is the domain\'s door to storage',
            'Own your query shapes or they leak everywhere',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# RETRY
# ─────────────────────────────────────────────────────────────────────────────
_t('retry', [
    {
        'title': 'Retry: Try Again, Smarter',
        'desc': 'Recovering from transient failures by retrying with backoff — and knowing when to stop.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Identify transient failures',
            'Apply exponential backoff',
            'Add jitter',
            'Bound retries',
        ],
        'prereqs': ['principles/circuit-breaker', 'principles/idempotency'],
        'sections': [
            {'heading': 'The Problem', 'paras': [
                'Networks drop, services restart, locks time out — transient failures. A retry recovers many of them, but naive retries make things worse: immediate retries hammer a recovering service, and retrying non-idempotent operations double-applies effects. Retry is a policy, not a loop.',
            ], 'code': {'lang': 'go', 'body': '''
// Exponential backoff with jitter — the standard shape
func Retry(ctx context.Context, attempts int, fn func() error) error {
    for i := 0; i < attempts; i++ {
        err := fn()
        if err == nil { return nil }
        if !isTransient(err) { return err }   // permanent: stop now
        base := time.Duration(1<<i) * 100 * time.Millisecond  // 100,200,400..
        sleep := base + time.Duration(rand.Intn(100))*time.Millisecond // jitter
        select {
        case <-time.After(sleep):
        case <-ctx.Done():
            return ctx.Err()                  // honour cancellation
        }
    }
    return lastErr
}'''}},
            {'heading': 'Backoff and Jitter', 'paras': [
                'Exponential backoff doubles the wait per attempt (100ms, 200ms, 400ms...), giving a recovering service room. Jitter — a random offset — prevents thundering herd: without it, all clients retry in sync and amplify the outage. Bounded retries with a max attempt count and a deadline are mandatory.',
            ]},
        ],
        'practice': {
            'title': 'Design the Retry Policy',
            'intro': 'A checkout calls a payment API that fails transiently under load.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Classify errors: transient vs permanent. Which should never be retried?'},
                {'label': 'Task 2', 'text': 'Apply backoff with jitter and a max attempt count.'},
                {'label': 'Task 3', 'text': 'Make the operation idempotent so a retry after a timeout cannot double-charge.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why jitter matters when 100 clients retry together. Start with the herd.'},
            {'label': 'Compare & Contrast', 'text': 'Compare retry with circuit breaker and with timeouts. When does each stop the bleeding?'},
            {'label': 'Boundary Testing', 'text': 'A retry succeeds but the response is lost, so the client retries the idempotent operation. Design the idempotency key flow.'},
        ],
        'takeaways': [
            'Retry only transient failures',
            'Exponential backoff + jitter prevents herds',
            'Bound attempts and honor deadlines',
            'Idempotency makes retries safe',
        ],
        'further': [
            {'title': 'Retry pattern — Microsoft Azure', 'url': 'https://learn.microsoft.com/en-us/azure/architecture/patterns/retry'},
            {'title': 'Exponential backoff — AWS docs', 'url': 'https://docs.aws.amazon.com/general/latest/gr/api-retries.html'},
        ],
    },
    {
        'title': 'Retry in Production: SDKs, Queues, and Dead Letters',
        'desc': 'Retry budgets, delayed queues, and dead-letter handling in real systems.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Budget retries across services',
            'Use delayed retry queues',
            'Design dead-letter flows',
            'Avoid retry storms',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Retry Budgets', 'paras': [
                'Every service retrying its dependencies multiplies load: a single downstream failure fans out. A retry budget caps the retry rate (e.g., at most 10% of requests retried in a window); beyond it, fail fast. Budgets prevent a failing dependency from amplifying into a total outage.',
            ], 'code': {'lang': 'yaml', 'body': '''
Retry budget example (rate-based):
  window: 30s
  max_retries_per_request: 3
  budget: 10% of requests may be retried in the window
  if budget exhausted: fail immediately (don't amplify the outage)

Delayed retry via queue:
  message fails -> publish to retry topic with delay (1m, 5m, 30m)
  -> consumer attempts again after the delay
  -> after N attempts -> dead-letter topic (human/automated repair)
Dead-letter handling:
  - inspect, fix the root cause, redeliver
  - or reject permanently and alert
  - monitor DLQ depth as an operational signal'''}},
            {'heading': 'Queues and DLQs', 'paras': [
                'Message queues retry naturally: a failed message redelivers. Delayed retries (RabbitMQ delays, SQS visibility timeout, Kafka via scheduled re-emit) space out attempts. A dead-letter queue isolates poison messages — ones that fail forever — so they stop consuming retry capacity and alert operators.',
            ]},
        ],
        'practice': {
            'title': 'Design the Retry Path',
            'intro': 'A webhook sender delivers 10k events/hour to partners; some partners are flaky.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the per-partner retry policy with delays.'},
                {'label': 'Task 2', 'text': 'Design the dead-letter flow and the manual re-delivery tool.'},
                {'label': 'Task 3', 'text': 'Set the global retry budget so one flaky partner cannot starve the others.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why retry budgets exist: what a fan-out retry storm does to a failing dependency.'},
            {'label': 'Implementation Design', 'text': 'Design a delayed retry pipeline with exponential delays and a DLQ. What are the delays, and who watches the DLQ?'},
            {'label': 'Boundary Testing', 'text': 'A poison message loops for hours consuming retry capacity. Design the attempt cap and the DLQ promotion.'},
        ],
        'takeaways': [
            'Retry budgets stop amplification',
            'Delayed queues space out attempts',
            'Dead-letter queues isolate poison messages',
            'DLQ depth is an operational alarm',
        ],
        'further': [
            {'title': 'Retry — Google SRE workbook', 'url': 'https://sre.google/workbook/part-iv-practices/'},
            {'title': 'AWS SQS — visibility timeout', 'url': 'https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html'},
        ],
    },
    {
        'title': 'Advanced Retry: Circuit Breakers and Chaos',
        'desc': 'Integrating retries with circuit breakers, timeouts, and load shedding.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Combine retry with circuit breaking',
            'Set timeout hierarchies',
            'Shed load under pressure',
            'Test with chaos',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'The Full Stack', 'paras': [
                'Retry alone amplifies; the mature stack layers: timeout (bound the attempt), retry (recover transients), circuit breaker (stop trying when the dependency is down), and load shedding (drop work when the system is saturated). Each layer fails fast when the one below cannot recover.',
            ], 'code': {'lang': 'go', 'body': '''
// Layered resilience: timeout -> retry -> breaker -> shed
func Call(ctx context.Context) (Resp, error) {
    if shedder.ShouldDrop() {           // overload: shed now
        return Resp{}, ErrOverloaded
    }
    if !breaker.Allow() {               // circuit open: fail fast
        return Resp{}, ErrCircuitOpen
    }
    ctx, cancel := context.WithTimeout(ctx, 2*time.Second) // bound
    defer cancel()
    err := Retry(ctx, 3, func() error { return client.Do(ctx) })
    if err != nil { breaker.Fail() } else { breaker.Success() }
    return resp, err
}
// A retry only runs when the breaker is closed; an open circuit
// returns immediately instead of amplifying with more attempts.'''}},
            {'heading': 'Chaos Testing', 'paras': [
                'Retry policies rot: they work until a dependency fails in a new way. Chaos testing (inject latency, packet loss, and failures into dependencies) proves the retry stack behaves — recovery time, no amplification, budgets respected. The failure injection is a first-class test suite.',
            ]},
        ],
        'practice': {
            'title': 'Build the Stack',
            'intro': 'A search service calls an LLM API that is slow, flaky, and expensive.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Layer: timeout, retry with backoff, circuit breaker, shedder.'},
                {'label': 'Task 2', 'text': 'Set the thresholds: timeout budget, error rate to open, retry cap.'},
                {'label': 'Task 3', 'text': 'Run a chaos drill: inject 5s latency and verify the stack sheds without amplifying.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why retry without a breaker amplifies a real outage.'},
            {'label': 'Implementation Design', 'text': 'Design the timeout hierarchy for a 3-hop call: client -> gateway -> LLM. What is each timeout, and what retries run at which hop?'},
            {'label': 'Boundary Testing', 'text': 'The breaker opens during a sale and requests fail fast for minutes. Design the half-open recovery and the degraded-response fallback.'},
        ],
        'takeaways': [
            'Timeout, retry, breaker, and shedder layer together',
            'Breakers stop amplification; shedders stop saturation',
            'Chaos drills prove the stack, not just the code',
            'Half-open states test recovery safely',
        ],
        'further': [
            {'title': 'Resilience4j — the full toolkit', 'url': 'https://resilience4j.readme.io/'},
            {'title': 'Chaos Engineering — principles', 'url': 'https://principlesofchaos.org/'},
        ],
    },
    {
        'title': 'Retry: Review & Mastery Quiz',
        'desc': 'Scenario questions on policies, queues, and resilience stacks.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate retry concepts',
            'Design budgets and queues',
            'Layer resilience',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Retry only? (A: transient failures / B: all failures / C: successes)',
                'Q2: Jitter prevents? (A: thundering herds / B: retries / C: caches)',
                'Q3: A retry budget caps? (A: the retry rate / B: the database / C: memory)',
                'Q4: True or false: poison messages belong in a dead-letter queue.',
                'Q5: A circuit breaker opens when? (A: failures exceed a threshold / B: it is bored / C: memory is full)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A partner API is flaky and expensive. Design the timeout, retry, breaker, budget, and DLQ story.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why retrying without a policy is how outages become multi-hour.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Retries recover transients; policy bounds the damage',
            'Breakers, budgets, and chaos complete the stack',
        ],
    },
])
