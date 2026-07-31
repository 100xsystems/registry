#!/usr/bin/env python3
"""Generate deep ACID-format curricula for all remaining principles.

Each principle gets 4 lessons: fundamentals, applications, advanced/production,
and a review quiz — matching the approved ACID template depth.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_knowledge_lib import run_topic  # noqa: E402

PRINCIPLES = {
    'backpressure': {
        'lessons': [
            {
                'slug': 'backpressure-fundamentals',
                'title': 'Backpressure: Flow Control Fundamentals',
                'description': 'Why producers must slow down for consumers, and the mechanics of flow control.',
                'duration': '45 min', 'difficulty': 'Beginner',
                'objectives': [
                    'Explain why unbounded queues cause memory exhaustion',
                    'Define backpressure and its role in resilient systems',
                    'Identify the three flow-control strategies',
                    'Trace a slow-consumer scenario through a pipeline',
                ],
                'prereqs': ['principles/fail-fast', 'principles/rate-limiting'],
                'sections': [
                    {'heading': 'The Problem: Unbounded Buffers', 'paras': [
                        'When a producer emits faster than a consumer can process, messages pile up. Without limits, that queue grows until memory is exhausted and the process dies — taking the whole service down with it.',
                        'Backpressure is the mechanism by which a consumer signals the producer to slow down. It converts a resource-exhaustion failure into a graceful, explicit slowdown that the system can survive.',
                    ]},
                    {'heading': 'How Backpressure Works', 'paras': [
                        'There are three fundamental strategies: (1) bounded queues with blocking, (2) pull-based (reactive) demand where the consumer requests N items at a time, and (3) dropping or erroring when the buffer overflows.',
                        'The pull model is the strongest: the consumer declares exactly how much it can handle, so the producer never over-produces. This is the basis of Reactive Streams and Java Flow.',
                    ], 'code': {'lang': 'java', 'body': '''
// Reactive Streams: consumer declares demand
public final class SimpleSubscriber implements Flow.Subscriber<Integer> {
    private Flow.Subscription subscription;
    public void onSubscribe(Flow.Subscription s) {
        this.subscription = s;
        s.request(3);            // demand: 3 items at a time
    }
    public void onNext(Integer item) {
        System.out.println("got " + item);
        subscription.request(1); // one more after each
    }
    public void onError(Throwable t) { t.printStackTrace(); }
    public void onComplete() { System.out.println("done"); }
}'''}},
                ],
                'practice': {
                    'title': 'Slow Consumer Simulation',
                    'intro': 'Model a producer/consumer pair where the consumer sleeps 100ms per item and the producer bursts 10,000 items instantly.',
                    'tasks': [
                        {'label': 'Task 1', 'text': 'With an unbounded queue, record the memory growth and the time when the process dies.'},
                        {'label': 'Task 2', 'text': 'Switch to a bounded queue (capacity 100) with blocking. What happens to the producer? Is the system stable?'},
                        {'label': 'Task 3', 'text': 'Implement pull-based demand. Verify memory stays flat regardless of burst size.'},
                    ],
                },
                'prompts': [
                    {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time to help me reason about why a bounded queue with a blocking put can still deadlock a pipeline. Start with the producer thread.'},
                    {'label': 'Compare & Contrast', 'text': 'Compare backpressure in Kafka (no native backpressure), Reactive Streams, and TCP flow control. Give concrete scenarios where each fails.'},
                    {'label': 'Boundary Testing', 'text': 'What happens when a consumer requests a negative demand in a Reactive Streams implementation? What should the spec-compliant publisher do?'},
                    {'label': 'Implementation Design', 'text': 'Design a bounded async queue for a microservice that must never drop messages and never exhaust memory. Show the data structures and blocking semantics.'},
                ],
                'takeaways': [
                    'Unbounded queues convert slow consumers into OOM crashes',
                    'Pull-based demand is the strongest backpressure model',
                    'Blocking on a bounded queue is simple but can deadlock pipelines',
                    'Dropping with error signals is a valid strategy for time-sensitive data',
                ],
                'further': [
                    {'title': 'Reactive Streams Specification', 'url': 'https://www.reactive-streams.org/'},
                    {'title': 'Flow (Java) — API docs', 'url': 'https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Flow.html'},
                    {'title': 'Backpressure in Reactive Systems', 'url': 'https://www.reactivemanifesto.org/glossary#Back-Pressure'},
                ],
            },
            {
                'slug': 'backpressure-applications',
                'title': 'Backpressure in Real Systems',
                'description': 'How Kafka, gRPC, databases, and browsers actually handle flow control.',
                'duration': '60 min', 'difficulty': 'Intermediate',
                'objectives': [
                    'Compare backpressure approaches across Kafka, gRPC, and HTTP/2',
                    'Explain consumer lag and its relationship to backpressure',
                    'Design a rate-aware consumer that protects its own resources',
                    'Apply backpressure to database write paths',
                ],
                'prereqs': ['principles/backpressure/backpressure-fundamentals'],
                'sections': [
                    {'heading': 'Kafka: Poll-Based, Not Pushed', 'paras': [
                        'Kafka consumers pull batches with fetch requests, which gives natural backpressure: a consumer fetches only what it can process. The risk shifts to consumer lag — the distance between the committed offset and the head of the log.',
                        'When a consumer cannot keep up, lag grows. Monitoring lag is how teams detect backpressure problems before memory or disk fails.',
                    ], 'code': {'lang': 'text', 'body': '''
# Track lag per partition — the canonical backpressure metric
# lag = latest_offset - committed_offset
kafka-consumer-groups.sh --describe --group orders
# GROUP   TOPIC   PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG
# orders  events  0          1024            2048            1024'''}},
                    {'heading': 'HTTP/2 Flow Control', 'paras': [
                        'HTTP/2 provides per-stream flow control using WINDOW_UPDATE frames. A receiver announces how many bytes it can accept per stream and per connection, letting an overwhelmed server throttle a chatty client.',
                        'gRPC builds on HTTP/2 and inherits this: a server that is slow to respond naturally exerts backpressure on the client through the flow-control window.',
                    ]},
                ],
                'practice': {
                    'title': 'Consumer Lag Analysis',
                    'intro': 'You operate a Kafka pipeline where consumer lag spikes every night during batch jobs.',
                    'tasks': [
                        {'label': 'Task 1', 'text': 'Describe the metrics you would collect to distinguish a slow consumer from an over-producing producer.'},
                        {'label': 'Task 2', 'text': 'Propose three mitigations: scale out, batch larger, or add a dead-letter path. When is each correct?'},
                        {'label': 'Task 3', 'text': 'Design an alert that fires 30 minutes before lag causes data loss, with a clear runbook action.'},
                    ],
                },
                'prompts': [
                    {'label': 'Socratic Tutor', 'text': 'Walk me through what happens when a Kafka consumer processes a message that triggers a slow external API call. Where is the backpressure, and where is it missing?'},
                    {'label': 'Compare & Contrast', 'text': 'Contrast consumer lag in Kafka with TCP receive-window pressure. What is analogous to a zero window in Kafka?'},
                    {'label': 'Boundary Testing', 'text': 'A consumer crashes and restarts with a stale offset. It must reprocess 2M messages. How does this interact with backpressure? Design a replay that does not OOM.'},
                ],
                'takeaways': [
                    'Kafka uses pull-based consumption, making lag the key backpressure signal',
                    'HTTP/2 flow control gives gRPC real backpressure semantics',
                    'Always monitor consumer lag, not just throughput',
                    'Batch size tuning is the cheapest backpressure lever',
                ],
                'further': [
                    {'title': 'Kafka Consumer Configuration', 'url': 'https://kafka.apache.org/documentation/#consumerconfigs'},
                    {'title': 'HTTP/2 Flow Control (RFC 9113)', 'url': 'https://www.rfc-editor.org/rfc/rfc9113.html#name-flow-control'},
                ],
            },
            {
                'slug': 'backpressure-advanced',
                'title': 'Advanced Backpressure Patterns',
                'description': 'Token buckets, adaptive batching, and end-to-end flow control.',
                'duration': '75 min', 'difficulty': 'Advanced',
                'objectives': [
                    'Combine rate limiting with backpressure correctly',
                    'Build adaptive batching that responds to consumer speed',
                    'Propagate backpressure across service boundaries',
                    'Handle multi-tenant backpressure without starving tenants',
                ],
                'prereqs': ['principles/backpressure/backpressure-applications', 'principles/rate-limiting'],
                'sections': [
                    {'heading': 'Backpressure vs Rate Limiting', 'paras': [
                        'Rate limiting is producer-side: it caps how much work enters the system. Backpressure is consumer-side: it signals the producer to slow down based on actual capacity. The two are complementary — a rate limit is the safety ceiling, backpressure is the adaptive floor.',
                    ]},
                    {'heading': 'Adaptive Batching', 'paras': [
                        'An adaptive consumer measures its own processing rate and adjusts the batch size it requests. When the rate drops (GC pause, cold cache), it shrinks demand; when it rises, it grows demand. This keeps latency low and memory flat.',
                    ], 'code': {'lang': 'python', 'body': '''
# Adaptive batch sizing from measured throughput
import time

def next_batch_size(current_bps: float, target_latency_ms: int) -> int:
    # aim: batch roughly equals target_latency_ms of work
    per_item_us = 1_000_000 / max(current_bps, 1e-6)
    desired = target_latency_ms * 1000 / per_item_us
    return int(max(1, min(desired, 1000)))  # clamp 1..1000'''}},
                ],
                'practice': {
                    'title': 'End-to-End Backpressure Design',
                    'intro': 'Design flow control for: client → API gateway → worker pool → PostgreSQL.',
                    'tasks': [
                        {'label': 'Task 1', 'text': 'Decide where each layer applies pressure: client-side retry backoff, gateway request queues, worker pool bounds.'},
                        {'label': 'Task 2', 'text': 'Model the failure mode when PostgreSQL connection pool is exhausted. Does the gateway queue grow unbounded?'},
                        {'label': 'Task 3', 'text': 'Add a circuit breaker between the gateway and the worker pool. Where does it sit relative to backpressure?'},
                    ],
                },
                'prompts': [
                    {'label': 'Socratic Tutor', 'text': 'Teach me why TCP-style sliding windows are the canonical backpressure mechanism and how they map to an HTTP API that returns 429.'},
                    {'label': 'Boundary Testing', 'text': 'A single tenant floods the system. Design backpressure that degrades only that tenant while protecting others (shard-local tokens, per-tenant queues).'},
                    {'label': 'Implementation Design', 'text': 'Implement an adaptive batch consumer in Go using channels where the worker reports its processing rate back to the fetcher. Sketch the goroutines and channels.'},
                ],
                'takeaways': [
                    'Rate limiting caps entry; backpressure adapts to real capacity',
                    'Adaptive batching keeps latency bounded under load changes',
                    'Backpressure must propagate end-to-end or buffers hide the problem',
                    'Multi-tenant systems need per-tenant pressure isolation',
                ],
                'further': [
                    {'title': 'Backpressure in Reactive Manifesto', 'url': 'https://www.reactivemanifesto.org/glossary#Back-Pressure'},
                    {'title': 'Designing Data-Intensive Applications, Ch. 11', 'url': 'https://dataintensive.net/'},
                ],
            },
            {
                'slug': 'backpressure-review-quiz',
                'title': 'Backpressure: Review & Mastery Quiz',
                'description': 'Test your flow-control knowledge with scenario-based questions.',
                'duration': '30 min', 'difficulty': 'Intermediate', 'type': 'quiz',
                'objectives': [
                    'Consolidate flow-control concepts',
                    'Apply backpressure reasoning to new systems',
                    'Identify anti-patterns quickly',
                ],
                'prereqs': ['principles/backpressure/backpressure-advanced'],
                'sections': [
                    {'heading': 'Quiz', 'paras': [
                        'Answer these questions, then check against the key takeaways below.',
                    ], 'bullets': [
                        'Q1: A producer fills an unbounded queue. What is the first observable failure? (A: OOM / B: deadlock / C: 429s)',
                        'Q2: Which mechanism gives a consumer the strongest control over producer speed? (A: bounded queue / B: pull demand / C: TCP window)',
                        'Q3: In Kafka, what metric reveals a consumer falling behind? (A: fetch latency / B: consumer lag / C: record size)',
                        'Q4: True or false: HTTP/2 flow control applies per connection, not per stream.',
                        'Q5: A worker pool is at capacity and its queue is bounded. The gateway keeps sending. What should the gateway do? (A: buffer more / B: back off / C: drop silently)',
                    ]},
                ],
                'prompts': [
                    {'label': 'Scenarios', 'text': 'A video-upload pipeline buffers 5GB of frames in memory because the encoder is slow. Rewrite the design so memory stays under 200MB without dropping frames.'},
                    {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "just make the queue bigger" is rarely the right fix, using a concrete system you know.'},
                ],
                'takeaways': [
                    'A: OOM; B: pull demand; C: consumer lag; Q4: false (per stream AND connection); Q5: back off',
                    'Buffering hides problems — expose them as signals instead',
                    'Backpressure is a contract between producer and consumer',
                ],
            },
        ],
    },
}

# ─────────────────────────────────────────────────────────────────────────────
# Batch of the remaining 32 principles (compact but deep, 4 lessons each)
# ─────────────────────────────────────────────────────────────────────────────

# Simplest builder: derive from a compact spec
def build(slug, name, topics):
    """topics: list of 4 dicts each with title/desc/objs(4)/..."""
    lessons = []
    kinds = ['fundamentals', 'applications', 'advanced', 'review-quiz']
    for kind, t in zip(kinds, topics):
        lessons.append({
            'slug': f'{slug}-{kind}',
            'title': t['title'],
            'description': t['desc'],
            'duration': t.get('dur', '45 min' if kind == 'fundamentals' else ('60 min' if kind == 'applications' else '75 min')),
            'difficulty': t.get('diff', 'Beginner' if kind == 'fundamentals' else ('Intermediate' if kind in ('applications', 'review-quiz') else 'Advanced')),
            'type': 'quiz' if kind == 'review-quiz' else 'lesson',
            'objectives': t['objs'],
            'prereqs': t.get('prereqs', []),
            'sections': t.get('sections', []),
            'practice': t.get('practice'),
            'prompts': t.get('prompts', []),
            'takeaways': t.get('takeaways', []),
            'further': t.get('further', []),
        })
    return lessons


# Helper to make a section quickly
def S(heading, paras=None, code=None, bullets=None):
    d = {'heading': heading}
    if paras: d['paras'] = paras
    if code: d['code'] = code
    if bullets: d['bullets'] = bullets
    return d


def C(lang, body):
    return {'lang': lang, 'body': body}


if __name__ == '__main__':
    import importlib

    # Phase 1: backpressure (fully written above)
    run_topic('principles', 'backpressure', PRINCIPLES['backpressure']['lessons'])
    print('backpressure done')

    # Phase 2: all 32 remaining principles from the data modules
    merged = {}
    mod_names = ['principles_data'] + [f'principles_data{i}' for i in range(2, 10)]
    for mod_name in mod_names:
        mod = importlib.import_module(mod_name)
        merged.update(mod.TOPICS)
        print(f'loaded {mod_name}: {len(mod.TOPICS)} topics')

    for slug, topics in merged.items():
        lessons = build(slug, slug, topics)
        run_topic('principles', slug, lessons)

    print(f'\nTOTAL principles generated: {1 + len(merged)}')
