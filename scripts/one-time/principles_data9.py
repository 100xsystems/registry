#!/usr/bin/env python3
"""Deep curriculum data chunk 9: solid, throttling, yagni."""

TOPICS = {}


def _t(slug, topics):
    TOPICS[slug] = topics
    return topics


# ─────────────────────────────────────────────────────────────────────────────
# SOLID
# ─────────────────────────────────────────────────────────────────────────────
_t('solid', [
    {
        'title': 'SOLID: The Five Principles of Maintainable Design',
        'desc': 'The acronym that ties together the five foundation principles of object-oriented design.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'List the five SOLID principles',
            'Explain what each principle protects',
            'Recognize violations in code',
            'Apply the principles together coherently',
        ],
        'prereqs': ['principles/single-responsibility', 'principles/open-closed', 'principles/liskov-substitution', 'principles/interface-segregation', 'principles/dependency-inversion'],
        'sections': [
            {'heading': 'The Five', 'paras': [
                'SOLID is five principles that together produce code that tolerates change: Single Responsibility (one reason to change), Open-Closed (extend without modifying), Liskov Substitution (subtypes honor contracts), Interface Segregation (small role interfaces), and Dependency Inversion (depend on abstractions).',
                'They are not a checklist — they are one coherent stance: small surfaces, clear contracts, and dependency arrows that point at abstractions so the system can evolve without rippling.',
            ], 'code': {'lang': 'text', 'body': '''
SOLID in one line each:
  S - One reason to change per class
  O - Extend via new code, not edits to tested code
  L - Subtypes keep their promises
  I - Clients depend only on interfaces they use
  D - Depend on abstractions, not details

Together: a design where change is local, cheap, and safe.'''}},
            {'heading': 'The Payoff', 'paras': [
                'Each principle removes a specific class of pain: SRP removes change-conflict, OCP removes regression risk, LSP removes surprise behavior, ISP removes coupling, DIP removes direction entanglement. A system that respects them changes in small, reviewable, low-risk steps.',
            ]},
        ],
        'practice': {
            'title': 'Assess a Class Against SOLID',
            'intro': 'A 300-line PaymentProcessor that parses, validates, charges, emails, and logs, with a fat interface and concrete dependencies.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Score it against each of the five principles, with the violation named.'},
                {'label': 'Task 2', 'text': 'Refactor the two worst violations (likely S and D).'},
                {'label': 'Task 3', 'text': 'Explain how fixing one violation makes the others easier.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about how the five principles reinforce each other. Start with S and D.'},
            {'label': 'Compare & Contrast', 'text': 'Compare SOLID with GRASP and with composition-over-inheritance. Where do they converge?'},
            {'label': 'Boundary Testing', 'text': 'A codebase applies SOLID everywhere and ends up with hundreds of tiny classes. Design the judgment that keeps SOLID from over-fragmenting.'},
        ],
        'takeaways': [
            'SOLID is one stance: small surfaces, clear contracts',
            'Each principle removes a specific class of pain',
            'The principles reinforce each other',
            'Balance SOLID against simplicity — do not fragment for its own sake',
        ],
        'further': [
            {'title': 'The SOLID Principles — Robert C. Martin', 'url': 'https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html'},
            {'title': 'SOLID — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/SOLID'},
        ],
    },
    {
        'title': 'SOLID in Production: Design Reviews and Evolution',
        'desc': 'Using SOLID as a review vocabulary and evolving a legacy codebase toward it.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Use SOLID vocabulary in design reviews',
            'Prioritize violations by risk',
            'Refactor toward SOLID incrementally',
            'Keep the legacy migration safe',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Reviews in SOLID Terms', 'paras': [
                'SOLID gives review comments precision: instead of "this class is too big", say "this class has two reasons to change (SRP)" or "this switch must be edited for every new shape (OCP)". The shared vocabulary makes design discussions concrete and teachable.',
            ], 'code': {'lang': 'text', 'body': '''
Review prompts in SOLID terms:
  S: "Who else changes this class, and for what reason?"
  O: "What breaks when we add the third variant?"
  L: "Does every subclass honor the base contract?"
  I: "Does this client depend on methods it never uses?"
  D: "What concrete detail is this coupled to?"'''}},
            {'heading': 'Migration Order', 'paras': [
                'Refactoring a legacy codebase toward SOLID is a risk-ranked sequence: fix the violations causing real pain first (the god class blocking features, the fat interface forcing changes), keep behavior identical with characterization tests, and refactor in small, reviewable slices.',
            ]},
        ],
        'practice': {
            'title': 'Prioritize the Violations',
            'intro': 'A legacy billing module fails every SOLID test. New features land weekly and keep breaking.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Rank the violations by how much they block feature work.'},
                {'label': 'Task 2', 'text': 'Write characterization tests that lock current behavior before refactoring.'},
                {'label': 'Task 3', 'text': 'Plan the slice order: which class gets extracted first, and how is each step verified?'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why characterization tests are the safe foundation for SOLID refactoring. Ask me how to write one.'},
            {'label': 'Implementation Design', 'text': 'Design a weekly "design fitness" review that scores the riskiest module against SOLID and tracks the trend.'},
            {'label': 'Boundary Testing', 'text': 'A refactor toward SOLID is blocked by a shared transaction. Design the outbox-based path that unblocks it safely.'},
        ],
        'takeaways': [
            'SOLID is a precise review vocabulary',
            'Fix the violations that hurt most first',
            'Characterization tests make refactoring safe',
            'Migrate in small, verified slices',
        ],
        'further': [
            {'title': 'Working Effectively with Legacy Code', 'url': 'https://www.oreilly.com/library/view/working-effectively-with/0131177052/'},
            {'title': 'Characterization Testing — Michael Feathers', 'url': 'https://michaelfeathers.silvrback.com/characterization-testing'},
        ],
    },
    {
        'title': 'Advanced SOLID: DDD and System Design',
        'desc': 'SOLID at the architecture scale: domain models, bounded contexts, and system-level boundaries.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Apply SOLID thinking to domain models',
            'Map SOLID to bounded contexts',
            'Design system boundaries with SOLID analogies',
            'Keep architecture honest with tests',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'SOLID at the System Scale', 'paras': [
                'Every SOLID principle has a system-level twin: SRP becomes "one bounded context per service", OCP becomes "add consumers, do not edit producers", LSP becomes "implementations honor the interface contract", ISP becomes "consumer-specific read models", DIP becomes "the domain does not import infrastructure".',
            ], 'code': {'lang': 'text', 'body': '''
SOLID mapped to architecture:
  S -> bounded contexts / service ownership
  O -> event consumers attach, producers unchanged
  L -> contract-tested implementations
  I -> consumer-specific DTOs and read models
  D -> domain imports ports, not frameworks

A system designed this way changes by adding, not rewriting.'''}},
            {'heading': 'Enforcing the Architecture', 'paras': [
                'Architecture-level SOLID decays without enforcement: dependency tests, contract tests, and consumer-contract tests keep the boundaries honest. The same "test the invariants" discipline that guards a class guards a service.',
            ]},
        ],
        'practice': {
            'title': 'Map SOLID to Your System',
            'intro': 'Your platform has 12 services; one service owns payments, identity, and email.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Map each principle to a concrete violation or strength in the platform.'},
                {'label': 'Task 2', 'text': 'Design the boundary split for the multi-owner service.'},
                {'label': 'Task 3', 'text': 'Add the architecture tests that would have caught the violation.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can articulate how SOLID principles scale from a class to a bounded context.'},
            {'label': 'Implementation Design', 'text': 'Design a platform where adding a new notification channel is purely additive (OCP at the system level). What moves, what never changes?'},
            {'label': 'Boundary Testing', 'text': 'A consumer contract changes and three services break. Design the contract test + consumer-version matrix that predicts the blast radius.'},
        ],
        'takeaways': [
            'SOLID scales from classes to bounded contexts',
            'Additive change is the system-level payoff',
            'Architecture tests keep boundaries honest',
            'Contract tests predict cross-service blast radius',
        ],
        'further': [
            {'title': 'Clean Architecture — Robert C. Martin', 'url': 'https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html'},
            {'title': 'Pact — Consumer-Driven Contracts', 'url': 'https://docs.pact.io/'},
        ],
    },
    {
        'title': 'SOLID: Review & Mastery Quiz',
        'desc': 'Scenario questions on the five principles and their interactions.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate the five principles',
            'Diagnose violations precisely',
            'Apply SOLID coherently',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: The O in SOLID stands for? (A: object / B: open-closed / C: optional)',
                'Q2: "Subtypes must honor the base contract" is? (A: LSP / B: DIP / C: SRP)',
                'Q3: "Depend on abstractions, not details" is? (A: ISP / B: DIP / C: OCP)',
                'Q4: True or false: SOLID is a checklist that applies mechanically.',
                'Q5: Consumer-specific read models are ISP at? (A: class scale / B: system scale / C: no scale)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A payment flow violates all five principles. Refactor it to a SOLID design and justify each change with the principle it serves.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer how SOLID makes change cheap, using one concrete incident.'},
        ],
        'takeaways': [
            'Q1: B; Q2: A; Q3: B; Q4: false; Q5: B',
            'SOLID is a coherent stance, applied with judgment',
            'Its payoff is change that is local, cheap, and safe',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# THROTTLING
# ─────────────────────────────────────────────────────────────────────────────
_t('throttling', [
    {
        'title': 'Throttling: Slow the Flow, Don\'t Stop It',
        'desc': 'Why easing off the throttle — rather than hard-stopping — keeps systems responsive under load.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Define throttling and distinguish it from rate limiting',
            'Explain the throttling curve (slowdown, not cutoff)',
            'Apply throttling to clients and workers',
            'Return proper throttling signals',
        ],
        'prereqs': ['principles/rate-limiting', 'principles/load-shedding'],
        'sections': [
            {'heading': 'Throttling vs Rate Limiting', 'paras': [
                'Rate limiting caps the number of requests (a hard budget). Throttling controls the speed at which work proceeds — it slows the flow rather than stopping it. A throttled client gets responses, just slower; a rate-limited one gets 429s.',
                'Think of a valve versus a lock: throttling is the valve that eases pressure; rate limiting is the lock that admits a fixed number. Both protect capacity; they do it differently.',
            ], 'code': {'lang': 'python', 'body': '''
# Throttle: add delay so the flow matches capacity
import time

def throttle(request, tokens_per_sec=50):
    # delay based on how far ahead of the sustained rate we are
    gap = (1 / tokens_per_sec)
    elapsed = time.monotonic() - request.slot_started
    if elapsed < gap:
        time.sleep(gap - elapsed)       # slow down, don't reject
    return process(request)'''}},
            {'heading': 'Where Throttling Lives', 'paras': [
                'Clients throttle their own outbound calls (back off when the server is slow), workers throttle their consumption of a queue (process at a sustainable rate), and servers throttle responses to protect downstream capacity. Each layer eases the flow instead of cutting it.',
            ]},
        ],
        'practice': {
            'title': 'Design the Throttle',
            'intro': 'A batch client pulls 10k records/min from an API that can safely serve 5k/min.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the client throttle: a token bucket that shapes the pull rate.'},
                {'label': 'Task 2', 'text': 'Design the server-side signal (Retry-After on 429, and a smooth slowdown when near capacity).'},
                {'label': 'Task 3', 'text': 'Explain when throttling beats hard rate limiting for this workload.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about the difference between shaping traffic (throttle) and capping traffic (rate limit). Start with a burst.'},
            {'label': 'Compare & Contrast', 'text': 'Compare throttling with rate limiting, load shedding, and backpressure. Which is the right tool for a slow consumer?'},
            {'label': 'Boundary Testing', 'text': 'A throttled client slows down but the server is still saturated. Design the escalation from throttle to shed.'},
        ],
        'takeaways': [
            'Throttling slows the flow; rate limiting caps it',
            'The valve metaphor: ease pressure, do not cut it',
            'Clients, workers, and servers all throttle',
            'Throttle escalates to shedding when slowing is not enough',
        ],
        'further': [
            {'title': 'Traffic Shaping — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Traffic_shaping'},
            {'title': 'Retry-After header — MDN', 'url': 'https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After'},
        ],
    },
    {
        'title': 'Throttling in Production: Workers and Backoff',
        'desc': 'Worker throttling, exponential backoff, and self-protecting clients.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design worker consumption rates',
            'Implement exponential backoff with jitter',
            'Protect downstreams from bursty consumers',
            'Monitor throttling as a health signal',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Exponential Backoff', 'paras': [
                'When a downstream signals "slow down" (429, timeout, slow response), the client backs off exponentially: 1s, 2s, 4s, 8s, capped — with jitter so synchronized clients do not retry in lockstep. This is throttling as a protocol.',
            ], 'code': {'lang': 'go', 'body': '''
// Exponential backoff with jitter (AWS-style full jitter)
func backoff(attempt int) time.Duration {
    const base = time.Second
    const cap = 30 * time.Second
    exp := float64(1 << min(attempt, 30))   // 1s, 2s, 4s...
    return time.Duration(rand.Float64() * min(exp*float64(base), float64(cap)))
}
// Full jitter: random in [0, exp] prevents synchronized retry storms'''}},
            {'heading': 'Worker Throttles', 'paras': [
                'Workers that consume a queue too fast overwhelm the database or the API they call. A worker throttle — max messages per second, or adaptive to downstream latency — shapes the consumption rate to what the system can absorb.',
            ]},
        ],
        'practice': {
            'title': 'Shape the Consumer',
            'intro': 'A queue consumer calls a downstream API with a 100 QPS limit; messages arrive at 500/s.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the consumer throttle to stay under the downstream limit.'},
                {'label': 'Task 2', 'text': 'Add adaptive backoff when the downstream starts returning 429s.'},
                {'label': 'Task 3', 'text': 'Design the alert: when is sustained throttling a downstream problem, not just load?'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why full-jitter backoff prevents retry storms. Ask me to simulate five synchronized clients.'},
            {'label': 'Implementation Design', 'text': 'Design a self-protecting client: it throttles its own requests based on the server\'s latency signal. What signals does it read?'},
            {'label': 'Boundary Testing', 'text': 'A client backs off forever because the server is permanently down. Design the escalation from backoff to alert to circuit-break.'},
        ],
        'takeaways': [
            'Backoff with jitter is throttling as a protocol',
            'Workers must shape consumption to downstream capacity',
            'Sustained throttling is a downstream health signal',
            'Backoff escalates to circuit-breaking when permanent',
        ],
        'further': [
            {'title': 'Exponential Backoff And Jitter — AWS', 'url': 'https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/'},
            {'title': 'Google Cloud — Handling Throttling', 'url': 'https://cloud.google.com/storage/docs/retry-strategy'},
        ],
    },
    {
        'title': 'Advanced Throttling: Adaptive and Fair Throttles',
        'desc': 'Adaptive rates, fair throttling across consumers, and throttling that learns the system.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Design adaptive throttle rates from feedback',
            'Throttle fairly across consumers',
            'Combine throttling with backpressure',
            'Avoid throttle oscillation',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Adaptive Rates', 'paras': [
                'A fixed throttle rate is a guess; an adaptive one learns from feedback: measure downstream latency or queue depth, and raise or lower the rate smoothly (with hysteresis) to track the system\'s real capacity.',
            ], 'code': {'lang': 'go', 'body': '''
// Adaptive: track downstream p99, adjust rate with AIMD-like logic
var p99 latencyPercentile
var rate = 100.0   // requests/sec

func tick() {
    if p99.value() > 500*time.Millisecond {
        rate *= 0.8            // multiplicative decrease (smooth)
    } else if p99.value() < 200*time.Millisecond {
        rate *= 1.05           // additive increase (cautious)
    }
    rate = clamp(rate, 10, 5000)
}
// Hysteresis: thresholds far apart prevent oscillation'''}},
            {'heading': 'Fair Throttling', 'paras': [
                'When multiple consumers share a downstream, fair throttling gives each a proportional slice of the rate — a chatty consumer cannot starve the quiet ones. Per-consumer budgets with a global cap implement fairness.',
            ]},
        ],
        'practice': {
            'title': 'Design the Adaptive Fair Throttle',
            'intro': 'Ten workers consume from one API; two workers are noisy; downstream capacity fluctuates.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design per-worker budgets with a fair-share rule.'},
                {'label': 'Task 2', 'text': 'Add the adaptive rate driven by downstream p99 with hysteresis.'},
                {'label': 'Task 3', 'text': 'Design the oscillation guard and the convergence test.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why AIMD (additive increase, multiplicative decrease) is the classic safe adaptive scheme.'},
            {'label': 'Implementation Design', 'text': 'Design a throttling library clients embed: it reads server signals, shapes local rate, and reports. What is the wire protocol?'},
            {'label': 'Boundary Testing', 'text': 'Downstream p99 spikes from an unrelated tenant and your adaptive throttle overreacts. Design the signal separation.'},
        ],
        'takeaways': [
            'Adaptive rates track real capacity from feedback',
            'AIMD with hysteresis is the safe adaptive scheme',
            'Fair throttling protects quiet consumers',
            'Separate your signal from the noise of other tenants',
        ],
        'further': [
            {'title': 'AIMD Congestion Control', 'url': 'https://en.wikipedia.org/wiki/Additive_increase/multiplicative_decrease'},
            {'title': 'gRPC Adaptive Throttling', 'url': 'https://github.com/grpc/proposal/blob/master/A62-google-default-credentials.md'},
        ],
    },
    {
        'title': 'Throttling: Review & Mastery Quiz',
        'desc': 'Scenario questions on shaping, backoff, and adaptive rates.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate throttling concepts',
            'Design throttle and backoff',
            'Apply fair adaptive throttling',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Throttling differs from rate limiting by? (A: slowing instead of capping / B: stopping traffic / C: no difference)',
                'Q2: Backoff jitter prevents? (A: retry storms / B: latency / C: caching)',
                'Q3: AIMD stands for? (A: additive increase, multiplicative decrease / B: always increase, mostly decrease / C: a new metric)',
                'Q4: True or false: a fixed throttle rate needs no tuning.',
                'Q5: Fair throttling protects? (A: the noisiest consumer / B: quiet consumers / C: the edge)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A data pipeline\'s consumer is throttling against a fluctuating API. Design the adaptive fair throttle and the escalation to shedding.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "just add a sleep" and "just retry harder" are both wrong throttling.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: false; Q5: B',
            'Throttling shapes flow; backoff coordinates it',
            'Adaptive and fair variants make it production-safe',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# YAGNI
# ─────────────────────────────────────────────────────────────────────────────
_t('yagni', [
    {
        'title': 'YAGNI: You Ain\'t Gonna Need It',
        'desc': 'Why building for hypothetical futures is how codebases die, one speculative feature at a time.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Define YAGNI',
            'Recognize speculative generality',
            'Explain the carrying cost of unused code',
            'Apply the "build it when needed" discipline',
        ],
        'prereqs': ['principles/kiss', 'principles/dry'],
        'sections': [
            {'heading': 'The Principle', 'paras': [
                'YAGNI says do not build functionality you predict you will need — build it when you actually need it. Speculative features (config knobs for imagined requirements, abstraction layers for hypothetical variants, unused parameters) cost more than they ever return.',
                'The cost is not just the writing: every speculative feature must be reviewed, tested, documented, integrated, and maintained — forever. Most predicted features never arrive, and the ones that do arrive different from the prediction.',
            ], 'code': {'lang': 'python', 'body': '''
# Speculative: parameters and paths for imagined futures
def process(data, mode='fast', use_cache=False, retry_policy=None,
            notify=None, format='json'):     # 6 knobs, 1 used
    ...

# YAGNI: build what is used today
def process(data):                            # one path
    ...'''}},
            {'heading': 'YAGNI vs Preparedness', 'paras': [
                'YAGNI is not "no design" — it is "no speculative construction". Interfaces that express the real current boundary are design; interfaces that pre-empt a variant that does not exist yet are speculation. The discipline: name the concrete trigger that would justify building it.',
            ]},
        ],
        'practice': {
            'title': 'Prune the Speculation',
            'intro': 'A feature ships with an abstraction layer, a config DSL, and three unused flags "for future flexibility".',
            'tasks': [
                {'label': 'Task 1', 'text': 'List the speculative pieces and the trigger that would justify each.'},
                {'label': 'Task 2', 'text': 'Remove the pieces with no near-term trigger.'},
                {'label': 'Task 3', 'text': 'Write the team rule: what evidence justifies building ahead?'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why speculative code is not free. Start with maintenance cost.'},
            {'label': 'Compare & Contrast', 'text': 'Compare YAGNI with DRY and with "rule of three". When does DRY tempt you into YAGNI violations?'},
            {'label': 'Boundary Testing', 'text': 'An interface with one implementation is a YAGNI violation to some, sound DIP to others. Design the decision rule that resolves the debate.'},
        ],
        'takeaways': [
            'Do not build for imagined futures',
            'Speculative code carries a permanent maintenance tax',
            'Name the concrete trigger before building ahead',
            'YAGNI is discipline, not laziness',
        ],
        'further': [
            {'title': 'YAGNI — Martin Fowler', 'url': 'https://martinfowler.com/bliki/Yagni.html'},
            {'title': 'You Aren\'t Gonna Need It — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it'},
        ],
    },
    {
        'title': 'YAGNI in Production: Features and Architectures',
        'desc': 'Applying YAGNI to feature requests, frameworks, and architecture decisions.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Challenge speculative feature requests',
            'Defer framework adoption with triggers',
            'Apply YAGNI to architecture choices',
            'Communicate YAGNI without being obstructive',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Feature Requests', 'paras': [
                'Product requests often arrive with future-proofing: "build it generically so we can add X later". The YAGNI response: build the current requirement cleanly, and design the seams that make X cheap to add later — without building X.',
            ], 'code': {'lang': 'text', 'body': '''
YAGNI conversation script:
  "We should add X now because we will need it later."
  -> "What is the concrete trigger for X?"
  -> "What is the cheapest seam to add X when the trigger hits?"
  -> "Let us build the seam now and X at the trigger."
Seams = interfaces and structure that keep X cheap; X = deferred.'''}},
            {'heading': 'Framework and Architecture Decisions', 'paras': [
                'Frameworks are the biggest YAGNI temptation: adopting an orchestration platform "because we will need it" adds operational weight today for a problem that may never arrive. Defer with a trigger: adopt the framework when the problem it solves actually appears.',
            ]},
        ],
        'practice': {
            'title': 'Deflect with a Trigger',
            'intro': 'A team proposes an event-sourcing framework for a service that stores a list of settings.',
            'tasks': [
                {'label': 'Task 1', 'text': 'State the concrete trigger that would justify event sourcing.'},
                {'label': 'Task 2', 'text': 'Design the cheapest seam now (audit log, plain storage) that keeps the future option open.'},
                {'label': 'Task 3', 'text': 'Write the deferral decision in one paragraph, including the trigger and the review date.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me how to say "not yet" to a framework without being dismissed as lazy. Ask me to role-play the discussion.'},
            {'label': 'Implementation Design', 'text': 'Design the seams for a feature that will likely grow: which structure today makes growth cheap without building the growth?'},
            {'label': 'Boundary Testing', 'text': 'The trigger fires: a real second variant appears. Design the transition from the simple version to the generalized one without a rewrite.'},
        ],
        'takeaways': [
            'Build the seam, defer the speculation',
            'Frameworks are adopted on triggers, not predictions',
            'The trigger must be concrete and reviewable',
            'YAGNI conversations need a deferral script, not a veto',
        ],
        'further': [
            {'title': 'The YAGNI Trap in Architecture — ThoughtWorks', 'url': 'https://www.thoughtworks.com/insights/blog'},
            {'title': 'Deferring Decisions — ADR pattern', 'url': 'https://adr.github.io/'},
        ],
    },
    {
        'title': 'Advanced YAGNI: Options Thinking and Seams',
        'desc': 'Designing cheap options (seams) instead of building speculative futures.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Apply options thinking to design',
            'Build cheap seams that keep options open',
            'Distinguish seam from speculation',
            'Measure the cost of carrying options',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Options, Not Futures', 'paras': [
                'Financial options cost a premium and expire. Design options are the same: a cheap seam (interface, boundary, config point) that keeps a future choice open costs a little today and is worth it only if the option is plausibly exercised and cheap to keep. Every seam is also maintenance — count its premium.',
            ], 'code': {'lang': 'text', 'body': '''
Options thinking checklist for a seam:
  1. What future choice does this seam keep open?
  2. How much does the seam cost to maintain today?
  3. How plausible is the future? (evidence, not vibes)
  4. Can the seam be added later for about the same cost?
If the seam is cheap, plausible, and hard to add later -> keep it.
Otherwise -> it is speculation, not an option.'''}},
            {'heading': 'The Cost of Carrying', 'paras': [
                'Every carried option is reviewed, tested, and explained forever. The discipline is to price the premium honestly: a seam that costs more than the future it hedges is a liability. Revisit carried options on a schedule and cut the ones whose trigger keeps failing to fire.',
            ]},
        ],
        'practice': {
            'title': 'Price the Options',
            'intro': 'A service carries a plugin registry, a config DSL, and an abstraction layer — all for "future flexibility".',
            'tasks': [
                {'label': 'Task 1', 'text': 'Price each: maintenance cost today, plausibility, and cost-to-add-later.'},
                {'label': 'Task 2', 'text': 'Cut the ones that fail the checklist; keep the cheap, plausible ones.'},
                {'label': 'Task 3', 'text': 'Set the review date for the kept options and the trigger for each.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can articulate the difference between an option (priced, cheap, expiring) and speculation (free in imagination, expensive forever).'},
            {'label': 'Implementation Design', 'text': 'Design the cheapest seam that keeps a future multi-region option open, without building any multi-region machinery.'},
            {'label': 'Boundary Testing', 'text': 'A kept option is now used by one consumer and has drifted from the codebase. Design the decision: migrate it in, or cut it?'},
        ],
        'takeaways': [
            'Options cost a premium; price it honestly',
            'A cheap seam is an option; an expensive one is speculation',
            'Carried options need triggers and review dates',
            'Cut options whose triggers keep failing to fire',
        ],
        'further': [
            {'title': 'Options Thinking in Software — Martin Fowler', 'url': 'https://martinfowler.com/bliki/OptionThinking.html'},
            {'title': 'YAGNI and the Economics of Software', 'url': 'https://www.martinfowler.com/articles/is-quality-worth-cost.html'},
        ],
    },
    {
        'title': 'YAGNI: Review & Mastery Quiz',
        'desc': 'Scenario questions on speculation, triggers, and options.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate YAGNI concepts',
            'Defer speculation with triggers',
            'Price design options',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: YAGNI says build? (A: everything predicted / B: what is needed now / C: the biggest design)',
                'Q2: Speculative code costs? (A: nothing / B: a permanent maintenance tax / C: only disk)',
                'Q3: A cheap seam that keeps a future open is? (A: an option / B: speculation / C: a bug)',
                'Q4: True or false: frameworks should be adopted when the problem they solve appears.',
                'Q5: A carried option with a trigger that keeps failing should? (A: stay forever / B: be cut / C: get more code)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A team wants to build a generic template engine for one page. Design the deferral: the seam, the trigger, and the review date.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "we might need it" is the most expensive phrase in software.'},
        ],
        'takeaways': [
            'Q1: B; Q2: B; Q3: A; Q4: true; Q5: B',
            'YAGNI is options discipline: seams today, futures at the trigger',
            'Unbuilt code is the cheapest code of all',
        ],
    },
])
