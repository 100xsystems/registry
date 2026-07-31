#!/usr/bin/env python3
"""Deep curriculum data batch 2: builder, chain-of-responsibility, circuit-breaker-pattern, command, composite, consistent-hashing."""

TOPICS = {}


def _t(slug, topics):
    TOPICS[slug] = topics
    return topics


# ─────────────────────────────────────────────────────────────────────────────
# BUILDER
# ─────────────────────────────────────────────────────────────────────────────
_t('builder', [
    {
        'title': 'Builder: Construct Complex Objects Step by Step',
        'desc': 'Separating the construction of a complex object from its representation.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the builder intent',
            'Use fluent builders for many-parameter objects',
            'Enforce valid intermediate states',
            'Compare with constructors and factories',
        ],
        'prereqs': ['patterns/factory', 'patterns/abstract-factory'],
        'sections': [
            {'heading': 'The Problem: Telescoping Constructors', 'paras': [
                'An object with 10 optional parameters needs either a constructor with 10 arguments (unreadable, easy to mix up) or a constellation of overloads. The builder constructs the object step by step, naming each setting, and produces the finished product at build() time.',
            ], 'code': {'lang': 'java', 'body': '''
// Builder: fluent, named, validated construction
public class Request {
    public static class Builder {
        private String method = "GET";
        private String url;
        private Map<String, String> headers = new HashMap<>();
        private byte[] body;

        public Builder url(String u) { this.url = u; return this; }
        public Builder method(String m) { this.method = m; return this; }
        public Builder header(String k, String v) { headers.put(k, v); return this; }
        public Builder body(byte[] b) { this.body = b; return this; }

        public Request build() {
            if (url == null) throw new IllegalStateException("url required");
            return new Request(method, url, headers, body);
        }
    }
}

Request r = new Request.Builder()
    .url("https://api.example.com/orders")
    .method("POST")
    .header("Authorization", token)
    .body(json)
    .build();'''}},
            {'heading': 'Validation at Build Time', 'paras': [
                'The builder enforces invariants at build(): required fields present, combinations valid. Intermediate states (half-configured) cannot escape because the object is immutable once built.',
            ]},
        ],
        'practice': {
            'title': 'Build the Query Object',
            'intro': 'A search query has 8 optional filters; call sites currently pass 8-positional-argument constructors.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the builder with fluent setters and build-time validation.'},
                {'label': 'Task 2', 'text': 'Enforce one invalid combination at build() (e.g., limit without sort).'},
                {'label': 'Task 3', 'text': 'Make the built object immutable and show two call sites.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about when a builder beats a well-named constructor. Start with parameter count.'},
            {'label': 'Compare & Contrast', 'text': 'Compare builder with factory and with named parameters (Python kwargs). When is each simpler?'},
            {'label': 'Boundary Testing', 'text': 'A builder method can be called twice with conflicting values. Design the "last wins" or "reject" policy.'},
        ],
        'takeaways': [
            'Builders name each step of complex construction',
            'Build-time validation catches bad combos early',
            'Built objects stay immutable',
            'Use them when constructors get unreadable',
        ],
        'further': [
            {'title': 'Builder — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/builder'},
            {'title': 'Builder Pattern — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Builder_pattern'},
        ],
    },
    {
        'title': 'Builder in Production: Configuration and DSLs',
        'desc': 'Fluent config, test fixtures, and domain-specific languages built on builders.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design fluent configuration builders',
            'Build test fixtures with builders',
            'Compose builders for nested objects',
            'Keep builders honest with defaults',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Configuration DSLs', 'paras': [
                'Server configs, client options, and pipeline definitions read beautifully as builders: the fluent chain reads like a specification, and build() validates the whole thing before anything runs.',
            ], 'code': {'lang': 'typescript', 'body': '''
// Fluent config builder: the code reads like a spec
const server = Server.builder()
    .port(8080)
    .maxConnections(10_000)
    .timeoutMs(5_000)
    .enableTls(cert, key)
    .onStartup(registerHealthCheck)
    .build();
// build() validates: port range, tls requires cert+key, etc.'''}},
            {'heading': 'Fixture Builders', 'paras': [
                'Test fixtures built with builders stay readable as they grow: user.withRole("admin").withEmail(...).build() — each test states only the fields it cares about, and the builder fills safe defaults for the rest. When the entity gains a field, the builder\'s default keeps every test compiling.',
            ]},
        ],
        'practice': {
            'title': 'Build the Fixture Builder',
            'intro': 'An Order entity with 12 fields; every test constructs one by hand with positional args.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the builder with sensible defaults for all fields.'},
                {'label': 'Task 2', 'text': 'Rewrite 10 existing test constructions with the builder — measure the readability change.'},
                {'label': 'Task 3', 'text': 'Add a new field and show no test breaks.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why fixture builders with defaults keep tests compiling when entities grow.'},
            {'label': 'Implementation Design', 'text': 'Design a nested builder (Order -> OrderItem list) with a fluent addItem(). How does the child builder participate?'},
            {'label': 'Boundary Testing', 'text': 'A default value in the builder hides a required semantic. Design the build-time validation that catches it.'},
        ],
        'takeaways': [
            'Config and pipeline builders read like specifications',
            'Fixture builders keep tests readable and resilient',
            'Defaults plus build-time validation is the balance',
            'Nested builders compose fluent hierarchies',
        ],
        'further': [
            {'title': 'Fluent Interface — Martin Fowler', 'url': 'https://martinfowler.com/bliki/FluentInterface.html'},
            {'title': 'Test Fixture Builders', 'url': 'https://www.martinfowler.com/bliki/ObjectMother.html'},
        ],
    },
    {
        'title': 'Advanced Builder: Immutability and Validation Pipelines',
        'desc': 'Immutable products, staged builders, and builders as validation pipelines.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Guarantee immutability of built products',
            'Design staged builders (type-safe steps)',
            'Chain validations through the builder',
            'Measure builder overhead',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Staged Builders', 'paras': [
                'A staged builder makes illegal states unrepresentable: the first stage returns a type that only exposes the next legal step. A request builder can enforce "url first, then method, then optional headers, then build" in the type system — the compiler rejects invalid orders.',
            ], 'code': {'lang': 'typescript', 'body': '''
// Staged builder: type system enforces the order of steps
interface HasUrl { withMethod(m: string): HasMethod; }
interface HasMethod { withHeader(k: string, v: string): HasMethod; build(): Request; }

class RequestBuilder implements HasUrl, HasMethod {
    private url = "";
    private method = "GET";
    constructor() {}

    withUrl(u: string): HasMethod { this.url = u; return this; }
    withMethod(m: string): HasMethod { this.method = m; return this; }
    withHeader(k: string, v: string): HasMethod { return this; }
    build(): Request { return new Request(this.url, this.method); }
}

// new RequestBuilder().withMethod("POST").withUrl(u) // compile error: url first'''.replace('\\\\', '\\')}},
            {'heading': 'Validation Pipelines', 'paras': [
                'The builder can carry a validation pipeline: each withX registers a check, and build() runs them all in order, collecting errors instead of failing on the first. This turns the builder into a form-validation engine with a single error-reporting surface.',
            ]},
        ],
        'practice': {
            'title': 'Design the Staged Builder',
            'intro': 'A payment request builder must enforce: amount first, currency second, then optional fields, then build.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the staged types so the compiler enforces the order.'},
                {'label': 'Task 2', 'text': 'Add a validation pipeline that collects all errors at build().'},
                {'label': 'Task 3', 'text': 'Verify the built object is deeply immutable (no setters, defensive copies).'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain how staged builders make illegal states unrepresentable.'},
            {'label': 'Implementation Design', 'text': 'Design a request-validator builder for an API gateway: stages for auth, body, params, with error aggregation.'},
            {'label': 'Boundary Testing', 'text': 'A builder with 20 stages becomes unusable. Design the line between staged safety and pragmatic flexibility.'},
        ],
        'takeaways': [
            'Staged builders encode legal orders in types',
            'Validation pipelines aggregate errors at build()',
            'Immutability is the contract of a built product',
            'Stages should not multiply past usefulness',
        ],
        'further': [
            {'title': 'Typestate Pattern (staged builders)', 'url': 'https://en.wikipedia.org/wiki/Typestate'},
            {'title': 'Immutability in Java — Effective Java Item 17', 'url': 'https://www.oreilly.com/library/view/effective-java-3rd/9780134686097/'},
        ],
    },
    {
        'title': 'Builder: Review & Mastery Quiz',
        'desc': 'Scenario questions on fluent construction, fixtures, and staging.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate builder concepts',
            'Design fluent APIs',
            'Enforce validity at build time',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: The builder solves? (A: complex construction / B: slow queries / C: caching)',
                'Q2: Validation should happen? (A: at build() / B: never / C: in the caller)',
                'Q3: A staged builder enforces? (A: legal step order / B: faster build / C: smaller memory)',
                'Q4: True or false: built objects should be immutable.',
                'Q5: Fixture builders keep tests compiling by? (A: safe defaults / B: removing fields / C: mocking)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'An HTTP client constructor takes 9 positional args and callers keep mixing them up. Design the builder and migrate three call sites.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why named builder steps beat positional constructors for readability.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Builders name construction and validate at the end',
            'Stages and immutability make them safe',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# CHAIN OF RESPONSIBILITY
# ─────────────────────────────────────────────────────────────────────────────
_t('chain-of-responsibility', [
    {
        'title': 'Chain of Responsibility: Pass It Down the Line',
        'desc': 'Giving multiple handlers a chance to process a request, each passing it on if it cannot.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the chain intent',
            'Build a handler chain',
            'Understand pass-along semantics',
            'Compare with decorator and pipeline',
        ],
        'prereqs': ['patterns/decorator', 'patterns/observer'],
        'sections': [
            {'heading': 'The Idea', 'paras': [
                'A chain of handlers, each deciding whether it can process a request or should pass it to the next. The sender does not know which handler will act — decoupling the request from its processor.',
            ], 'code': {'lang': 'java', 'body': '''
// Chain of responsibility: each handler passes or handles
abstract class Handler {
    protected Handler next;
    Handler setNext(Handler h) { this.next = h; return h; }

    public final void handle(Request r) {
        if (canHandle(r)) {
            doHandle(r);
        } else if (next != null) {
            next.handle(r);      // pass it down the line
        } else {
            throw new UnhandledRequestException(r);
        }
    }
    protected abstract boolean canHandle(Request r);
    protected abstract void doHandle(Request r);
}

// SupportTier1 -> SupportTier2 -> SupportEscalation
new SupportTier1().setNext(new SupportTier2()).setNext(new Escalation());'''}},
            {'heading': 'When It Fits', 'paras': [
                'Chains fit when handlers are independent, order matters, and the "who handles" decision is dynamic. Middleware pipelines, event preprocessing, and approval flows are classic chains.',
            ]},
        ],
        'practice': {
            'title': 'Build the Approval Chain',
            'intro': 'A purchase request: manager approves under $1k, director under $10k, CFO above.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Build the three-handler chain with canHandle rules.'},
                {'label': 'Task 2', 'text': 'Handle the unhandled case (negative amount) explicitly.'},
                {'label': 'Task 3', 'text': 'Insert a compliance check between director and CFO without touching either.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why the sender should not know which handler acts. Start with the decoupling benefit.'},
            {'label': 'Compare & Contrast', 'text': 'Compare chain of responsibility with decorator (adds behavior around) and pipeline (all stages run). How does the pass-along differ?'},
            {'label': 'Boundary Testing', 'text': 'Every handler passes and the chain ends. Design the explicit terminal handler for unhandled requests.'},
        ],
        'takeaways': [
            'Handlers pass requests they cannot process',
            'The sender stays decoupled from the processor',
            'Order matters; insert handlers without touching others',
            'Terminal handling prevents silent drops',
        ],
        'further': [
            {'title': 'Chain of Responsibility — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/chain-of-responsibility'},
            {'title': 'Chain of Responsibility — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern'},
        ],
    },
    {
        'title': 'Chain of Responsibility in Production: Middleware',
        'desc': 'HTTP middleware, event preprocessing, and auth chains in real frameworks.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design middleware chains',
            'Short-circuit with early responses',
            'Order middleware deliberately',
            'Test chains in isolation and end-to-end',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'HTTP Middleware', 'paras': [
                'Express/Koa/Rails middleware are chains: each middleware can handle (respond), pass to the next, or modify the request as it flows. Auth middleware short-circuits with 401 before the handler runs; logging middleware always passes.',
            ], 'code': {'lang': 'typescript', 'body': '''
// Middleware chain: each piece passes or short-circuits
app.use('/api', auth);          // 401 if no token, else pass
app.use('/api', rateLimit);     // 429 if over limit, else pass
app.use('/api', validateBody);  // 400 if invalid, else pass
app.use('/api', cacheHit);      // serve cached if present, else pass
app.get('/api/orders/:id', handler);  // last in the chain

// Order matters: auth before rate limit, validation before handler.'''}},
            {'heading': 'Chain Testing', 'paras': [
                'Each middleware is tested in isolation (pass, handle, short-circuit), and the full chain is tested for order effects: a middleware that must run before another is verified with an ordering test.',
            ]},
        ],
        'practice': {
            'title': 'Design the API Chain',
            'intro': 'An API needs auth, tenant-scoping, rate limiting, caching, and audit — in the right order.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Decide the order and justify each adjacency (why auth before tenant?).'},
                {'label': 'Task 2', 'text': 'Implement short-circuit paths (401, 403, 429, cache hit).'},
                {'label': 'Task 3', 'text': 'Write an ordering test that fails if auth runs after tenant-scoping.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why middleware order is a security decision, not just style. Ask me to order a chain with a reason for each pair.'},
            {'label': 'Implementation Design', 'text': 'Design an event-preprocessing chain: validate, enrich, dedupe, route. What passes, what short-circuits?'},
            {'label': 'Boundary Testing', 'text': 'Two middlewares both want to respond (cache hit and audit). Design the priority rule.'},
        ],
        'takeaways': [
            'Middleware chains pass or short-circuit',
            'Order is a security and correctness decision',
            'Isolation tests plus ordering tests cover chains',
            'Terminal handlers respond when nothing else does',
        ],
        'further': [
            {'title': 'Express Middleware', 'url': 'https://expressjs.com/en/guide/using-middleware.html'},
            {'title': 'Rack Middleware (Ruby)', 'url': 'https://github.com/rack/rack'},
        ],
    },
    {
        'title': 'Advanced Chain: Dynamic and Concurrent Chains',
        'desc': 'Runtime-reconfigurable chains, async handlers, and chains that split.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Reconfigure chains at runtime',
            'Handle async and parallel chains',
            'Design branching (fork/join) chains',
            'Keep chains observable',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Dynamic Chains', 'paras': [
                'When handler sets change at runtime (feature flags, tenant configs), build the chain from a registry at request time instead of wiring it statically. The registry maps conditions to handler lists.',
            ], 'code': {'lang': 'go', 'body': '''
// Dynamic chain: assembled per request from a registry
func chainFor(r *Request) []Handler {
    var chain []Handler
    for _, h := range registry.all() {
        if h.appliesTo(r) {      // tenant/flag/route aware
            chain = append(chain, h)
        }
    }
    return chain
}

// Each request walks its own chain; flags flip chains live,
// no redeploy needed for handler selection changes.'''}},
            {'heading': 'Async and Fork/Join', 'paras': [
                'Handlers may be async (each awaits the next) and chains may fork: a request fans out to parallel chains and joins at a barrier. The pattern still holds — each stage passes or handles — but concurrency and ordering guarantees become explicit design decisions.',
            ]},
        ],
        'practice': {
            'title': 'Design the Dynamic Chain',
            'intro': 'Tenants configure their own processing pipeline: some add GDPR scrub, some add audit.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the registry and the per-tenant chain assembly.'},
                {'label': 'Task 2', 'text': 'Add async handlers and the join semantics for parallel branches.'},
                {'label': 'Task 3', 'text': 'Design the tracing: a chain ID on every log line so handlers are attributable.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain the difference between a static chain and a per-request assembled one.'},
            {'label': 'Implementation Design', 'text': 'Design a per-tenant data pipeline chain with fork/join and failure isolation. What happens when one branch fails?'},
            {'label': 'Boundary Testing', 'text': 'A flag flips mid-request and the chain changes. Design the snapshot semantics (use the chain you started with).'},
        ],
        'takeaways': [
            'Registries enable per-request chain assembly',
            'Async handlers make chains concurrent',
            'Fork/join needs explicit join semantics',
            'Chain IDs make async chains traceable',
        ],
        'further': [
            {'title': 'Middleware as a Chain — Go net/http', 'url': 'https://pkg.go.dev/net/http'},
            {'title': 'Pipeline Pattern — Go Concurrency', 'url': 'https://go.dev/blog/pipelines'},
        ],
    },
    {
        'title': 'Chain of Responsibility: Review & Mastery Quiz',
        'desc': 'Scenario questions on handlers, middleware, and dynamic chains.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate chain concepts',
            'Order handlers deliberately',
            'Build dynamic chains',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: A handler that cannot process a request should? (A: pass it on / B: drop it / C: log and retry)',
                'Q2: Middleware that responds 401 is? (A: short-circuiting / B: passing / C: forking)',
                'Q3: The sender in a chain? (A: knows the handler / B: stays decoupled / C: must be a handler)',
                'Q4: True or false: middleware order is a security decision.',
                'Q5: Dynamic chains are assembled? (A: per request / B: once at boot / C: never)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'An approval chain for code deploys: lint, tests, security scan, human approval. Design the chain and the terminal handler.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why a chain with no terminal handler silently swallows work.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: B; Q4: true; Q5: A',
            'Chains decouple requests from their processors',
            'Ordering and terminal handling are the safety rails',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# CIRCUIT BREAKER (PATTERN)
# ─────────────────────────────────────────────────────────────────────────────
_t('circuit-breaker-pattern', [
    {
        'title': 'Circuit Breaker: Fail Fast, Recover Slow',
        'desc': 'The resilience pattern that stops calling a failing dependency and probes recovery.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the three breaker states',
            'Open on failure threshold, close on probe success',
            'Define fallbacks',
            'Distinguish from retry and timeout',
        ],
        'prereqs': ['principles/circuit-breaker', 'patterns/retry'],
        'sections': [
            {'heading': 'The Pattern', 'paras': [
                'Wrap a dependency call in a breaker with three states: CLOSED (calls flow), OPEN (calls fail fast for a window), HALF_OPEN (a probe tests recovery). Failure counting happens in CLOSED; a successful probe closes, a failed probe reopens.',
            ], 'code': {'lang': 'python', 'body': '''
# Circuit breaker state machine (core)
class Breaker:
    def __init__(self, threshold=5, open_timeout=30):
        self.threshold = threshold
        self.open_timeout = open_timeout
        self.failures = 0
        self.state = 'CLOSED'
        self.opened_at = None

    def allow(self):
        if self.state == 'OPEN':
            if time.time() - self.opened_at > self.open_timeout:
                self.state = 'HALF_OPEN'   # allow one probe
            else:
                return False
        return True

    def record_success(self):
        self.failures = 0
        self.state = 'CLOSED'

    def record_failure(self):
        self.failures += 1
        if self.failures >= self.threshold:
            self.state = 'OPEN'
            self.opened_at = time.time()'''}},
            {'heading': 'The Point', 'paras': [
                'Failing fast in OPEN protects the caller\'s resources from a dead dependency and gives the dependency recovery room. Without it, every call waits on a timeout, threads exhaust, and the failure cascades.',
            ]},
        ],
        'practice': {
            'title': 'Instrument the Breaker',
            'intro': 'A search API starts returning 500s; your service times out at 5s per call.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Choose threshold, open timeout, and the fallback (stale index).'},
                {'label': 'Task 2', 'text': 'Trace the timeline: when does it open, what do users see, when does it probe?'},
                {'label': 'Task 3', 'text': 'Design the HALF_OPEN probe so it does not flood a recovering API.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why the breaker must fail fast in OPEN rather than retry. Start with thread exhaustion.'},
            {'label': 'Compare & Contrast', 'text': 'Compare circuit breaker with retry, timeout, and bulkhead. Which problem does each solve?'},
            {'label': 'Boundary Testing', 'text': 'The dependency returns 200 with garbage. Design the health signal that opens the breaker anyway.'},
        ],
        'takeaways': [
            'OPEN fails fast; HALF_OPEN probes recovery',
            'Breakers protect caller resources',
            'Fallbacks define the user-visible degraded state',
            'Health signals beyond status codes matter',
        ],
        'further': [
            {'title': 'Circuit Breaker — Microsoft Docs', 'url': 'https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker'},
            {'title': 'Netflix Hystrix', 'url': 'https://github.com/Netflix/Hystrix/wiki/How-it-Works'},
        ],
    },
    {
        'title': 'Circuit Breaker in Production: Libraries and Config',
        'desc': 'Resilience4j, Polly, and tuning breakers for real services.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Configure a real breaker library',
            'Tune thresholds with sliding windows',
            'Design fallbacks per dependency',
            'Alert on breaker events',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Sliding-Window Breakers', 'paras': [
                'Libraries like Resilience4j count failures in a sliding window: open at 50% failure over the last 10 calls, with a minimum call count to avoid opening on a blip. The knobs are failure-rate threshold, window size, minimum calls, and wait duration.',
            ], 'code': {'lang': 'java', 'body': '''
// Resilience4j: sliding-window breaker
CircuitBreakerConfig config = CircuitBreakerConfig.custom()
    .failureRateThreshold(50)                  // open at 50% failures
    .slidingWindowSize(10)                     // last 10 calls
    .minimumNumberOfCalls(5)                   // require 5 calls first
    .waitDurationInOpenState(Duration.ofSeconds(20))
    .build();
CircuitBreaker cb = CircuitBreaker.of("search", config);

Supplier<String> safe = CircuitBreaker.decorateSupplier(cb,
    () -> searchClient.query(q));
String result = Try.ofSupplier(safe)
    .recover(t -> staleIndex())                // fallback
    .get();'''}},
            {'heading': 'Fallback Design', 'paras': [
                'The fallback is what users actually see: cached data, degraded UI, a queued retry, or a clear error. A fallback that silently returns wrong data is worse than an error — each dependency gets a fallback designed for its failure cost.',
            ]},
        ],
        'practice': {
            'title': 'Wire the Platform Breakers',
            'intro': 'Four dependencies: payments, search, recommendations, email. Each has different failure costs.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Set thresholds + fallbacks per dependency (payments=queue, search=stale, recs=default, email=skip+log).'},
                {'label': 'Task 2', 'text': 'Define which breaker events page on-call vs just log.'},
                {'label': 'Task 3', 'text': 'Build the dashboard: breaker state per dependency over time.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why minimumNumberOfCalls prevents flapping breakers. Ask me to trace a transient blip.'},
            {'label': 'Implementation Design', 'text': 'Design a breaker for a batch job that retries forever. Should a batch job use a breaker at all?'},
            {'label': 'Boundary Testing', 'text': 'The fallback itself calls the same dependency. Design the guard that prevents fallback recursion.'},
        ],
        'takeaways': [
            'Sliding windows + minimum calls prevent flapping',
            'Fallbacks are the user-visible contract',
            'Breaker events are alerting signals',
            'Fallbacks must never call the broken dependency',
        ],
        'further': [
            {'title': 'Resilience4j Docs', 'url': 'https://resilience4j.readme.io/docs/circuitbreaker'},
            {'title': 'Polly (dotnet)', 'url': 'https://github.com/App-vNext/Polly'},
        ],
    },
    {
        'title': 'Advanced Circuit Breaker: Health Signals and Probing',
        'desc': 'Latency-based opening, adaptive probes, and distributed breaker state.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Open on latency and data-quality signals',
            'Design adaptive HALF_OPEN probing',
            'Coordinate breakers across nodes',
            'Avoid synchronized probe storms',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Signals Beyond Status', 'paras': [
                'A dependency can return 200 while being slow or returning garbage. Track p99 latency and response validity as health signals: if p99 exceeds a budget or validation fails, treat the dependency as degraded and open the breaker.',
            ], 'code': {'lang': 'go', 'body': '''
// Latency-based breaker signal
var p99 = percentile(0.99, window=60)

func Call(ctx context.Context, fn func() (any, error)) (any, error) {
    if p99.value() > 2*time.Second && breaker.isClosed() {
        breaker.open("p99 above budget")     // slow = degraded too
    }
    start := time.Now()
    v, err := fn()
    p99.add(time.Since(start))
    return v, err
}'''}},
            {'heading': 'Adaptive Probing', 'paras': [
                'Fixed HALF_OPEN probes can flood a barely-recovering dependency. Adaptive probing starts with one probe and ramps traffic as success proves out. In multi-node callers, per-node state means synchronized probes — coordinate via a shared health registry or stagger probes with jitter.',
            ]},
        ],
        'practice': {
            'title': 'Design the Adaptive Breaker',
            'intro': 'A dependency degrades: p99 goes 80ms -> 4s with no error codes.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the latency threshold and measurement window.'},
                {'label': 'Task 2', 'text': 'Design the probe ramp: 1 call, then 1% traffic, then scale as healthy.'},
                {'label': 'Task 3', 'text': 'Add jitter so 20 caller nodes do not probe in lockstep.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why percentile latency beats average latency as a health signal.'},
            {'label': 'Implementation Design', 'text': 'Design a per-tenant breaker: one tenant\'s flood opens only their breaker. What state and keys?'},
            {'label': 'Boundary Testing', 'text': 'All callers open simultaneously and all fallbacks hit one cold cache. Design the fallback hierarchy that avoids the new stampede.'},
        ],
        'takeaways': [
            'Latency and validity signals catch what codes miss',
            'Adaptive probes ramp traffic as recovery proves',
            'Per-node breakers need coordination or jitter',
            'Fallback hierarchies must not create a new stampede',
        ],
        'further': [
            {'title': 'Google SRE — Handling Overload', 'url': 'https://sre.google/sre-book/handling-overload/'},
            {'title': 'Finagle Resilience (Twitter)', 'url': 'https://twitter.github.io/finagle/guide/Clients.html'},
        ],
    },
    {
        'title': 'Circuit Breaker (Pattern): Review & Mastery Quiz',
        'desc': 'Scenario questions on states, tuning, and probing.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate breaker concepts',
            'Tune for real failure modes',
            'Design probing and fallbacks',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: In OPEN state, calls? (A: proceed / B: fail fast / C: queue)',
                'Q2: HALF_OPEN allows? (A: a probe call / B: all traffic / C: nothing)',
                'Q3: minimumNumberOfCalls prevents? (A: flapping / B: timeouts / C: caching)',
                'Q4: True or false: a breaker only reacts to HTTP status codes.',
                'Q5: The user-visible contract of a breaker is its? (A: fallback / B: threshold / C: timeout)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A provider fails for 2 minutes then recovers. Design the breaker timeline: open, probe at 30s, ramp, and what users see at each stage.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why timeouts alone cannot prevent cascading failures.'},
        ],
        'takeaways': [
            'Q1: B; Q2: A; Q3: A; Q4: false; Q5: A',
            'Breakers convert slow cascades into fast, bounded failures',
            'Signals, probes, and fallbacks make them production-safe',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# COMMAND
# ─────────────────────────────────────────────────────────────────────────────
_t('command', [
    {
        'title': 'Command: Turn Actions into Objects',
        'desc': 'Encapsulating an action and its parameters so it can be queued, logged, and undone.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the command intent',
            'Build command objects',
            'Queue, log, and undo commands',
            'Compare with plain method calls',
        ],
        'prereqs': ['patterns/strategy', 'patterns/memento'],
        'sections': [
            {'heading': 'The Idea', 'paras': [
                'A command wraps an action and its parameters in an object with execute() (and optionally undo()). The caller invokes the command without knowing its implementation — enabling queues, history, logging, and macro composition.',
            ], 'code': {'lang': 'java', 'body': '''
// Command: an action as an object
interface Command {
    void execute();
    void undo();
}

class TransferCommand implements Command {
    private final Account from, to;
    private final Money amount;
    private boolean executed = false;

    TransferCommand(Account from, Account to, Money amt) { ... }

    public void execute() { from.debit(amount); to.credit(amount); executed = true; }
    public void undo() { if (executed) { to.debit(amount); from.credit(amount); executed = false; } }
}

// A queue of commands, an undo stack, a log — all just objects
Deque<Command> undoStack = new ArrayDeque<>();
undoStack.push(new TransferCommand(a, b, 100));
undoStack.pop().undo();'''}},
            {'heading': 'Why Objectify Actions', 'paras': [
                'Methods run immediately; command objects can be stored, ordered, retried, batched, and undone. They turn "do this" into a first-class value — which is exactly what editors, queues, and transactional systems need.',
            ]},
        ],
        'practice': {
            'title': 'Build the Undo Stack',
            'intro': 'A text editor needs undo for insert, delete, and format operations.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the Command interface and three concrete commands.'},
                {'label': 'Task 2', 'text': 'Wire the undo stack and the redo stack.'},
                {'label': 'Task 3', 'text': 'Handle undo-after-undo and the empty-stack edge case.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about what command objects enable that method calls cannot. Start with undo.'},
            {'label': 'Compare & Contrast', 'text': 'Compare command with strategy and with the observer pattern. Where do they overlap?'},
            {'label': 'Boundary Testing', 'text': 'A command fails halfway through execute(). Design the state handling so undo still works.'},
        ],
        'takeaways': [
            'Commands encapsulate actions as objects',
            'They enable queueing, logging, retry, and undo',
            'execute/undo pairs need careful state handling',
            'The caller never knows the command implementation',
        ],
        'further': [
            {'title': 'Command — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/command'},
            {'title': 'Command Pattern — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Command_pattern'},
        ],
    },
    {
        'title': 'Command in Production: Jobs and Transactions',
        'desc': 'Job queues, transactional commands, and command-driven workflows.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Model jobs as commands',
            'Make commands idempotent and retryable',
            'Build multi-step workflows from commands',
            'Persist command history',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Jobs as Commands', 'paras': [
                'A job queue is a queue of command objects: serialize the command (type + params), enqueue it, and a worker deserializes and executes. Retries re-enqueue the same command — idempotency keys keep replays safe.',
            ], 'code': {'lang': 'text', 'body': '''
Job queue as commands:
  enqueue(ResizeImage{ path, size })   -> JSON {type, params}
  worker: deserialize -> execute -> mark done
  failure: re-enqueue with backoff (same command, idempotent)

Transactional commands:
  a command executes and its effects commit atomically;
  a compensating command (undo) rolls back on failure.'''}},
            {'heading': 'Workflows', 'paras': [
                'A workflow is a sequence of commands with state: each step enqueues the next. Sagas are workflows of commands with compensating undos — the command pattern is the unit that makes orchestration and rollback possible.',
            ]},
        ],
        'practice': {
            'title': 'Design the Job Queue',
            'intro': 'A media pipeline: upload, transcode, thumbnail, publish — each a job with retries.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the four commands and their serialization.'},
                {'label': 'Task 2', 'text': 'Make each command idempotent (re-running is safe).'},
                {'label': 'Task 3', 'text': 'Design the failure path: retries, dead-letter, and the compensating command for a partial publish.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why idempotency keys make re-enqueued commands safe. Ask me to trace a double-execution.'},
            {'label': 'Implementation Design', 'text': 'Design a saga as a chain of commands with compensations. What happens at each failure point?'},
            {'label': 'Boundary Testing', 'text': 'A worker crashes mid-command. Design the recovery: how does the queue know the command state?'},
        ],
        'takeaways': [
            'Job queues are command queues',
            'Commands must be idempotent for safe replays',
            'Workflows and sagas compose commands',
            'Compensating commands implement undo at scale',
        ],
        'further': [
            {'title': 'Saga Pattern — Microservices.io', 'url': 'https://microservices.io/patterns/data/saga.html'},
            {'title': 'Transactional Outbox', 'url': 'https://microservices.io/patterns/data/transactional-outbox.html'},
        ],
    },
    {
        'title': 'Advanced Command: Macro and Event-Sourced Commands',
        'desc': 'Macro commands, command sourcing, and commands as the audit trail.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Compose macro commands',
            'Apply command sourcing (commands as events)',
            'Replay and audit with commands',
            'Keep commands backward compatible',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Macro Commands', 'paras': [
                'A macro command is a list of commands executed in order, with undo running them in reverse. Editors and CI pipelines are macro commands — composite objects made of commands.',
            ], 'code': {'lang': 'java', 'body': '''
// Macro command: many commands, one undo
class MacroCommand implements Command {
    private final List<Command> commands = new ArrayList<>();
    void add(Command c) { commands.add(c); }

    public void execute() { for (Command c : commands) c.execute(); }
    public void undo() {
        List<Command> rev = new ArrayList<>(commands);
        Collections.reverse(rev);
        for (Command c : rev) c.undo();     // undo in reverse order
    }
}'''}},
            {'heading': 'Command Sourcing', 'paras': [
                'Command sourcing stores every command (not state) as the durable record. State is derived by replaying commands; audit and debugging are free because the history is complete. Combined with event sourcing, commands become the intent and events the outcomes — the fullest audit trail.',
            ]},
        ],
        'practice': {
            'title': 'Design the Audit Trail',
            'intro': 'A banking app must prove "who did what when" for every transfer.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Model transfers as commands persisted with actor and timestamp.'},
                {'label': 'Task 2', 'text': 'Design replay: rebuild account state by re-executing commands.'},
                {'label': 'Task 3', 'text': 'Handle versioned commands: an old command must still replay after schema changes.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain the difference between command sourcing (intent) and event sourcing (outcome).'},
            {'label': 'Implementation Design', 'text': 'Design a command-sourced inventory system with replay and a snapshot strategy.'},
            {'label': 'Boundary Testing', 'text': 'A replayed command hits a changed business rule and diverges from history. Design the versioning rule for commands.'},
        ],
        'takeaways': [
            'Macro commands compose and undo in reverse',
            'Command sourcing stores intent as the durable record',
            'Replay derives state; history is complete',
            'Versioned commands keep replays faithful',
        ],
        'further': [
            {'title': 'Event Sourcing — Microsoft Docs', 'url': 'https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing'},
            {'title': 'CQRS + Command Sourcing', 'url': 'https://martinfowler.com/bliki/CQRS.html'},
        ],
    },
    {
        'title': 'Command: Review & Mastery Quiz',
        'desc': 'Scenario questions on command objects, queues, and sourcing.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate command concepts',
            'Design command queues',
            'Apply command sourcing',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: A command wraps? (A: an action and its parameters / B: a database / C: a thread)',
                'Q2: Undo requires commands to expose? (A: undo() / B: caching / C: logging)',
                'Q3: A job queue is a queue of? (A: commands / B: threads / C: databases)',
                'Q4: True or false: commands should be idempotent for safe replays.',
                'Q5: Command sourcing stores? (A: commands / B: only state / C: only logs)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A payment flow needs retry, audit, and undo. Model it as commands with idempotency and a compensating undo.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "just call the method" loses the ability to queue, log, and undo.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Commands make actions first-class values',
            'Sourcing turns them into the complete audit trail',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# COMPOSITE
# ─────────────────────────────────────────────────────────────────────────────
_t('composite', [
    {
        'title': 'Composite: Trees of Part-Whole',
        'desc': 'Treating individual objects and groups of objects uniformly.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the composite intent',
            'Build leaf and composite nodes',
            'Treat leaves and branches uniformly',
            'Recognize tree structures in code',
        ],
        'prereqs': ['patterns/iterator', 'patterns/decorator'],
        'sections': [
            {'heading': 'The Idea', 'paras': [
                'Some structures are naturally trees: files and folders, employees and departments, UI widgets and panels. Composite lets code treat a single item and a group of items through the same interface — draw() on a file draws the file, draw() on a folder draws all its contents.',
            ], 'code': {'lang': 'java', 'body': '''
// Composite: leaf and branch share the interface
interface Graphic {
    void draw();
    void add(Graphic g);      // no-op on leaves
}

class Circle implements Graphic {
    public void draw() { System.out.println("circle"); }
    public void add(Graphic g) { }            // leaf: cannot add
}

class Group implements Graphic {
    private final List<Graphic> children = new ArrayList<>();
    public void draw() { for (Graphic c : children) c.draw(); }
    public void add(Graphic g) { children.add(g); }
}

// Callers draw() a circle or a group of groups — same call.
Graphic scene = new Group();
scene.add(new Circle());
scene.add(new Group().add(new Circle()));'''}},
            {'heading': 'Recursion Is the Point', 'paras': [
                'The composite pattern is recursive: a group contains graphics which may themselves be groups. Operations (draw, render, size) recurse naturally, and callers never branch on "is this a leaf or a group?" — the interface hides it.',
            ]},
        ],
        'practice': {
            'title': 'Build the File Tree',
            'intro': 'A file explorer shows files and folders; folder size is the sum of contents.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the FileSystemNode interface with size() and render().'},
                {'label': 'Task 2', 'text': 'Implement File (leaf) and Folder (composite).'},
                {'label': 'Task 3', 'text': 'Compute the total size of a deeply nested tree with one recursive call.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why leaves and composites sharing an interface removes caller branching. Start with the size() recursion.'},
            {'label': 'Compare & Contrast', 'text': 'Compare composite with decorator (both wrap objects) and with the visitor pattern (both traverse trees).'},
            {'label': 'Boundary Testing', 'text': 'A leaf\'s add() silently no-ops. Design the alternative: throw, or move add() to a Branch interface?'},
        ],
        'takeaways': [
            'Leaves and branches share one interface',
            'Operations recurse naturally through the tree',
            'Callers never branch on leaf vs group',
            'Trees of files, UI, and orgs are composite territory',
        ],
        'further': [
            {'title': 'Composite — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/composite'},
            {'title': 'Composite Pattern — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Composite_pattern'},
        ],
    },
    {
        'title': 'Composite in Production: UI Trees and Documents',
        'desc': 'Widget trees, document models, and query trees built as composites.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design widget/document trees',
            'Traverse composites with iterators and visitors',
            'Keep tree operations efficient',
            'Avoid deep-tree recursion pitfalls',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'UI and Document Trees', 'paras': [
                'A DOM or widget tree is a composite: a Panel contains buttons and nested panels; render() on the root renders everything. React/Vue component trees and document object models are composites by construction.',
            ], 'code': {'lang': 'text', 'body': '''
Composite in the wild:
  DOM: <div> contains <p> and <section> containing <p>  -> render(root)
  Document: Paragraph contains Runs; Section contains Paragraphs
  Query AST: And(Equals(a,b), Or(Less(c,d), Exists(e)))
Operations recurse: render, serialize, validate, compute-size.'''}},
            {'heading': 'Traversal and Depth', 'paras': [
                'Iterators and visitors traverse composites without exposing internals. Deep trees risk stack overflow on recursive operations — iterative traversal or explicit work queues handle pathological depth, and lazy subtrees (virtualized lists) keep big trees responsive.',
            ]},
        ],
        'practice': {
            'title': 'Design the Query Tree',
            'intro': 'A search builder combines filters with AND/OR into a tree.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define FilterNode (leaf) and BooleanNode (AND/OR composite).'},
                {'label': 'Task 2', 'text': 'Implement evaluate(record) recursively and toSQL() recursively.'},
                {'label': 'Task 3', 'text': 'Add a visitor that pretty-prints the tree without modifying nodes.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why visitors keep traversal logic out of the tree nodes. Ask me when to prefer visitor over methods on nodes.'},
            {'label': 'Implementation Design', 'text': 'Design a virtualized UI tree: a list with 100k rows renders only visible ones. Where does the composite pattern bend?'},
            {'label': 'Boundary Testing', 'text': 'A circular reference in a tree (folder containing its ancestor) loops forever. Design the cycle guard.'},
        ],
        'takeaways': [
            'DOM, document, and query trees are composites',
            'Visitors and iterators traverse without exposing internals',
            'Deep trees need iterative or lazy traversal',
            'Cycle guards prevent infinite recursion',
        ],
        'further': [
            {'title': 'Visitor — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/visitor'},
            {'title': 'Virtualized List — React Window', 'url': 'https://react-window.vercel.app/'},
        ],
    },
    {
        'title': 'Advanced Composite: ASTs and Interpreters',
        'desc': 'Syntax trees, expression evaluators, and composite-backed interpreters.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Build expression ASTs as composites',
            'Interpret and compile ASTs recursively',
            'Apply visitors for multiple operations',
            'Design tree mutations safely',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Expression Trees', 'paras': [
                'An expression like (1 + 2) * 3 is a tree: a Multiply node with two children, one a binary Plus node. Evaluating and compiling are recursive walks over the composite — the interpreter pattern is composite applied to language.',
            ], 'code': {'lang': 'java', 'body': '''
// Expression AST as a composite
interface Expr { int eval(); }

class Num implements Expr {
    private final int v;
    Num(int v) { this.v = v; }
    public int eval() { return v; }
}

class BinOp implements Expr {
    private final Expr l, r;
    private final char op;
    BinOp(char op, Expr l, Expr r) { this.op = op; this.l = l; this.r = r; }
    public int eval() {
        int a = l.eval(), b = r.eval();
        return switch (op) { case '+' -> a + b; case '*' -> a * b; default -> 0; };
    }
}
// (1 + 2) * 3
Expr tree = new BinOp('*', new BinOp('+', new Num(1), new Num(2)), new Num(3));'''}},
            {'heading': 'Multiple Operations', 'paras': [
                'An AST needs eval, print, typecheck, and optimize. Adding each as a visitor keeps the tree stable; adding a new node type touches all visitors. Choose: visitor (stable nodes, many ops) or methods (stable ops, many nodes) — the open-closed axis decides.',
            ]},
        ],
        'practice': {
            'title': 'Build a Mini-Interpreter',
            'intro': 'A calculator language: numbers, +, *, parentheses, and variables.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Build the AST composite (Num, Var, BinOp).'},
                {'label': 'Task 2', 'text': 'Add eval() with a symbol table and toPrefix() printing.'},
                {'label': 'Task 3', 'text': 'Decide visitor vs methods for the next operation (typecheck) and justify.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain the visitor/methods trade-off using the expression-problem frame.'},
            {'label': 'Implementation Design', 'text': 'Design an optimizer pass over an AST that folds constant subexpressions. Which composite walk does it need?'},
            {'label': 'Boundary Testing', 'text': 'A huge AST (1M nodes) is evaluated recursively and overflows the stack. Design the iterative evaluation.'},
        ],
        'takeaways': [
            'ASTs are composites — interpret and compile by walking',
            'Visitor vs methods is the expression problem',
            'Choose the axis you expect to grow',
            'Deep trees need iterative evaluation',
        ],
        'further': [
            {'title': 'Interpreter — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/interpreter'},
            {'title': 'Crafting Interpreters — Robert Nystrom', 'url': 'https://craftinginterpreters.com/'},
        ],
    },
    {
        'title': 'Composite: Review & Mastery Quiz',
        'desc': 'Scenario questions on part-whole trees, traversal, and ASTs.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate composite concepts',
            'Design tree structures',
            'Choose traversal strategies',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Composite treats leaves and groups? (A: uniformly / B: differently / C: never)',
                'Q2: Operations on composites? (A: recurse / B: loop / C: fail)',
                'Q3: A DOM is an example of? (A: composite / B: singleton / C: memento)',
                'Q4: True or false: a leaf\'s add() should be meaningful.',
                'Q5: The visitor pattern is useful for? (A: many ops on stable nodes / B: many nodes with stable ops / C: caching)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A permissions model: a role contains users and other roles. Design the composite and the hasPermission() recursion with cycle protection.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why caller branching on "is this a folder?" defeats the pattern.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: false; Q5: A',
            'Part-whole trees share one interface',
            'Visitors and iterators keep traversal clean',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# CONSISTENT HASHING
# ─────────────────────────────────────────────────────────────────────────────
_t('consistent-hashing', [
    {
        'title': 'Consistent Hashing: Stable Distribution Across Changing Nodes',
        'desc': 'Mapping keys to nodes so that adding or removing a node moves only a small fraction of keys.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the rehash problem',
            'Describe the hash ring',
            'Understand why only neighbors move',
            'Identify cache and shard uses',
        ],
        'prereqs': ['patterns/hash-index', 'patterns/sharding'],
        'sections': [
            {'heading': 'The Problem', 'paras': [
                'Naive sharding uses hash(key) % N. When N changes (a node joins or dies), nearly every key remaps — a full cache flush or a migration storm. Consistent hashing maps keys onto a ring and nodes onto the same ring, so a node change only affects its neighbors.',
            ], 'code': {'lang': 'text', 'body': '''
Hash ring (0..2^32):
  keys:   k1 at 100, k2 at 300, k3 at 900
  nodes:  n1 at 200, n2 at 800

  k1 (100) -> n1 (next clockwise: 200)
  k2 (300) -> n2 (800)
  k3 (900) -> n1 (wraps to 200)

Add n3 at 700: only k2 (300) moves from n2 to n3.
k1 and k3 stay put. 1/N of keys move, not all.'''}},
            {'heading': 'Virtual Nodes', 'paras': [
                'With few real nodes, hashing can be skewed (one node owns most of the ring). Virtual nodes place many pseudo-node positions per real node, smoothing the distribution — a standard fix in production systems.',
            ]},
        ],
        'practice': {
            'title': 'Simulate the Ring',
            'intro': 'A 3-node cache with 1000 keys; one node dies.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Compute how many keys remap under naive mod vs consistent hashing.'},
                {'label': 'Task 2', 'text': 'Explain why only the dead node\'s keys are lost, and where they go.'},
                {'label': 'Task 3', 'text': 'Add virtual nodes (say 100/node) and show the load skew before and after.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why consistent hashing limits remapping to neighbors. Start with the ring walk.'},
            {'label': 'Compare & Contrast', 'text': 'Compare consistent hashing with rendezvous hashing (HRW). When is each preferred?'},
            {'label': 'Boundary Testing', 'text': 'Nodes cluster on the ring and load skews despite hashing. Design virtual-node placement that fixes it.'},
        ],
        'takeaways': [
            'The ring maps keys and nodes to one space',
            'Node changes move only neighbor keys',
            'Virtual nodes smooth distribution',
            'It powers caches, shards, and DHTs',
        ],
        'further': [
            {'title': 'Consistent Hashing — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Consistent_hashing'},
            {'title': 'Consistent Hashing Paper (Karger et al.)', 'url': 'https://dl.acm.org/doi/10.1145/258533.258642'},
        ],
    },
    {
        'title': 'Consistent Hashing in Production: Caches and Shards',
        'desc': 'Memcached, Dynamo-style sharding, and consistent-hash-based load balancing.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design a consistent-hash shard map',
            'Handle node membership changes',
            'Rebalance without a storm',
            'Use it for sticky load balancing',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Shard Maps', 'paras': [
                'A shard map maps logical shards to physical nodes via consistent hashing: each shard key hashes to a node, and when nodes scale, only neighbor shards move. Membership is versioned; a config service distributes the map to clients.',
            ], 'code': {'lang': 'python', 'body': '''
# Consistent hash with virtual nodes (production-shaped)
import hashlib, bisect

class ConsistentHash:
    def __init__(self, nodes, vnodes=100):
        self.ring, self.owners = [], {}
        for n in nodes:
            for v in range(vnodes):
                h = int(hashlib.md5(f"{n}:{v}".encode()).hexdigest()[:8], 16)
                self.ring.append(h); self.owners[h] = n
        self.ring.sort()

    def node_for(self, key):
        h = int(hashlib.md5(key.encode()).hexdigest()[:8], 16)
        i = bisect.bisect_right(self.ring, h) % len(self.ring)
        return self.owners[self.ring[i]]'''.replace('\\\\', '\\')}},
            {'heading': 'Sticky Sessions and Load Balancing', 'paras': [
                'Consistent hashing routes requests for the same user to the same backend (sticky sessions, session affinity) while staying balanced. A backend leaving the pool remaps only its users — no global rebalance.',
            ]},
        ],
        'practice': {
            'title': 'Design the Cache Topology',
            'intro': 'A 6-node Redis cache grows to 8 nodes during a sale.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Build the ring with virtual nodes and map the current keys.'},
                {'label': 'Task 2', 'text': 'Compute the cache-hit impact of adding 2 nodes (how many keys move?).'},
                {'label': 'Task 3', 'text': 'Design the membership update flow so clients see the new map without a stampede.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why adding nodes is cheap with consistent hashing but still needs a warm-up plan for the moved keys.'},
            {'label': 'Implementation Design', 'text': 'Design a shard map service: versioned maps, client caching, and the rebalance protocol.'},
            {'label': 'Boundary Testing', 'text': 'Two nodes hash adjacent and one takes 90% of the ring. Design the virtual-node layout that prevents it.'},
        ],
        'takeaways': [
            'Shard maps distribute via the ring, versioned',
            'Scale-out moves only neighbor keys',
            'Warm-up plans handle the moved keys',
            'Session affinity falls out naturally',
        ],
        'further': [
            {'title': 'Dynamo Paper (consistent hashing)', 'url': 'https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf'},
            {'title': 'Memcached Consistent Hashing', 'url': 'https://github.com/spotify/dockerfile-memcached'},
        ],
    },
    {
        'title': 'Advanced Consistent Hashing: Bounded Loads and DHTs',
        'desc': 'Bounded-load hashing, distributed hash tables, and ring resilience.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Apply bounded-load consistent hashing',
            'Understand DHT ring routing',
            'Handle churn and replication',
            'Design load-aware placement',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Bounded Loads', 'paras': [
                'Standard consistent hashing balances on average but can overload a hot node. Bounded-load hashing places each key on the closest node that is under a load cap — guaranteeing no node exceeds the cap while keeping placement stable and minimal-movement.',
            ], 'code': {'lang': 'python', 'body': '''
# Bounded-load: place on the nearest under-cap node
def place(key, ring, load, cap):
    start = bisect.bisect_right(ring, h(key)) % len(ring)
    for i in range(len(ring)):
        node = ring[(start + i) % len(ring)]
        if load[node] < cap:
            return node
    raise OverloadedError()      # every node at cap: shed or scale'''}},
            {'heading': 'DHT Routing', 'paras': [
                'Distributed hash tables (Chord, Pastry) extend the ring with finger tables: each node knows a few distant nodes, so lookups jump logarithmically instead of walking the ring. Churn (nodes joining/leaving) is handled by stabilization protocols that fix finger tables continuously.',
            ]},
        ],
        'practice': {
            'title': 'Design Load-Aware Placement',
            'intro': 'A hot-key product gets 30% of traffic on one node under plain hashing.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Apply bounded-load placement and show the hot node stays under cap.'},
                {'label': 'Task 2', 'text': 'Model the movement cost when the cap forces keys off their natural node.'},
                {'label': 'Task 3', 'text': 'Design the DHT-style finger table for log-time lookups under churn.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain the trade-off between load balance and placement stability.'},
            {'label': 'Implementation Design', 'text': 'Design a replicated ring: each key replicated to the next k nodes. What happens when two adjacent nodes die?'},
            {'label': 'Boundary Testing', 'text': 'A hot key exceeds every cap and nothing fits. Design the overflow path (replicate, shed, or scale).'},
        ],
        'takeaways': [
            'Bounded-load hashing guarantees per-node caps',
            'DHT finger tables give log-time routing',
            'Stabilization handles churn continuously',
            'Replication across neighbors survives multi-node loss',
        ],
        'further': [
            {'title': 'Bounded Loads — SNAP Paper', 'url': 'https://arxiv.org/abs/1608.01350'},
            {'title': 'Chord: A Scalable P2P Lookup', 'url': 'https://pdos.csail.mit.edu/papers/chord:sigcomm01/chord_sigcomm.pdf'},
        ],
    },
    {
        'title': 'Consistent Hashing: Review & Mastery Quiz',
        'desc': 'Scenario questions on rings, virtual nodes, and bounded loads.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate ring concepts',
            'Design shard maps',
            'Handle load and churn',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Adding a node under consistent hashing moves? (A: all keys / B: neighbor keys only / C: nothing)',
                'Q2: Virtual nodes fix? (A: load skew / B: latency / C: memory)',
                'Q3: Naive hash(key) % N breaks when? (A: N changes / B: N is prime / C: keys are strings)',
                'Q4: True or false: consistent hashing is used for session affinity.',
                'Q5: Bounded-load hashing guarantees? (A: per-node load caps / B: zero movement / C: exact balance)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A cache cluster of 10 nodes must scale to 12 without a hit-ratio collapse. Design the ring, the warm-up, and the load cap.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why hash % N is dangerous in production and what replaces it.'},
        ],
        'takeaways': [
            'Q1: B; Q2: A; Q3: A; Q4: true; Q5: A',
            'The ring makes membership changes cheap',
            'Bounded loads and DHTs extend it to hard cases',
        ],
    },
])
