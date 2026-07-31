#!/usr/bin/env python3
"""Deep curriculum data batch 1: abstract-factory, adapter, ambassador, b-tree, bloom-filter, bridge."""

TOPICS = {}


def _t(slug, topics):
    TOPICS[slug] = topics
    return topics


# ─────────────────────────────────────────────────────────────────────────────
# ABSTRACT FACTORY
# ─────────────────────────────────────────────────────────────────────────────
_t('abstract-factory', [
    {
        'title': 'Abstract Factory: Families of Related Objects',
        'desc': 'Creating related objects that must stay consistent — buttons and windows, databases and queries.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the abstract factory intent',
            'Build a factory of factories',
            'Keep related products consistent',
            'Compare with the factory method',
        ],
        'prereqs': ['patterns/factory', 'patterns/singleton'],
        'sections': [
            {'heading': 'The Problem: Related Objects Drift', 'paras': [
                'Some objects belong together: a Windows dialog uses Windows buttons and Windows menus; a dark theme uses dark widgets. If callers construct these individually, a bug can mix a Windows button into a Linux dialog — an inconsistent family.',
                'The abstract factory provides one interface for creating an entire family of related objects. Each concrete factory (WindowsFactory, LinuxFactory) produces a consistent set.',
            ], 'code': {'lang': 'java', 'body': '''
// Abstract factory: one interface per product family
interface GUIFactory {
    Button createButton();
    Dialog createDialog();
}

class WindowsFactory implements GUIFactory {
    public Button createButton() { return new WindowsButton(); }
    public Dialog createDialog() { return new WindowsDialog(); }
}

class LinuxFactory implements GUIFactory {
    public Button createButton() { return new LinuxButton(); }
    public Dialog createDialog() { return new LinuxDialog(); }
}

// The app is given a factory; it can never mix families.
void buildUI(GUIFactory f) {
    Button b = f.createButton();   // always matches the dialog
    Dialog d = f.createDialog();
}'''}},
            {'heading': 'Consistency Is the Point', 'paras': [
                'The pattern exists to guarantee consistency, not just to avoid new. The factory encodes the constraint "these objects belong together" in the type system — a compiler-enforced product family.',
            ]},
        ],
        'practice': {
            'title': 'Build a Cross-Platform Layer',
            'intro': 'A data layer must support Postgres and SQLite with matching Connection and Query objects.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the abstract factory and the two product interfaces.'},
                {'label': 'Task 2', 'text': 'Implement the two concrete factories with their products.'},
                {'label': 'Task 3', 'text': 'Show why the app can never mix a Postgres connection with a SQLite query.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about the difference between factory method and abstract factory. Start with the number of products.'},
            {'label': 'Compare & Contrast', 'text': 'Compare abstract factory with the builder pattern. When is a family of products the right abstraction versus a single complex product?'},
            {'label': 'Boundary Testing', 'text': 'A new product type joins the family and every factory must change. Is that a violation of open-closed? Design the fix.'},
        ],
        'takeaways': [
            'Abstract factory creates families of related objects',
            'Consistency of the family is the core guarantee',
            'The type system enforces "no mixed products"',
            'Growing the product set touches every factory — extend with care',
        ],
        'further': [
            {'title': 'Abstract Factory — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/abstract-factory'},
            {'title': 'Abstract Factory — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Abstract_factory_pattern'},
        ],
    },
    {
        'title': 'Abstract Factory in Production: Pluggable Backends',
        'desc': 'Theme engines, database adapters, and cloud provider abstractions built on abstract factories.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design a pluggable backend factory',
            'Wire the factory at the composition root',
            'Test with an in-memory product family',
            'Avoid factory sprawl',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'The Provider Pattern', 'paras': [
                'Cloud SDKs and database drivers use abstract factories so application code is provider-agnostic: an S3Factory and a GCSFactory both produce Bucket and Blob products. Swapping the provider is a one-line wiring change.',
            ], 'code': {'lang': 'typescript', 'body': '''
// Pluggable storage: the app depends only on the factory interface
interface StorageFactory {
    createBucket(name: string): Bucket;
    createBlob(key: string): Blob;
}
const factory: StorageFactory = process.env.PROVIDER === 'gcs'
    ? new GcsFactory()      // one wiring change swaps the cloud
    : new S3Factory();

const bucket = factory.createBucket('uploads');  // consistent pair
const blob = factory.createBlob('a/b.jpg');      // same provider'''}},
            {'heading': 'Testing with a Family', 'paras': [
                'A MemoryFactory that produces in-memory Buckets and Blobs lets integration tests run without a cloud. Because the app depends on the factory interface, the fake family is a drop-in — the same contract tests validate both families.',
            ]},
        ],
        'practice': {
            'title': 'Design the Provider Factory',
            'intro': 'A media service must support S3 and GCS with matching upload and stream products.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the factory and product interfaces (Uploader, Streamer).'},
                {'label': 'Task 2', 'text': 'Implement S3Factory, GcsFactory, and MemoryFactory.'},
                {'label': 'Task 3', 'text': 'Run the same contract tests against all three families and wire the choice at startup.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why the composition root is the only place the concrete factory should appear.'},
            {'label': 'Implementation Design', 'text': 'Design a notification system with email/push/sms families. Where does the factory fit, and what product types does each family produce?'},
            {'label': 'Boundary Testing', 'text': 'Two providers have incompatible capabilities (GCS supports X, S3 does not). Design the capability negotiation that keeps the family abstraction honest.'},
        ],
        'takeaways': [
            'Provider abstractions are abstract factories at scale',
            'The composition root is the single wiring point',
            'Fake families enable contract-tested integration tests',
            'Capability negotiation keeps the abstraction honest',
        ],
        'further': [
            {'title': 'AWS SDK — Provider Interfaces', 'url': 'https://docs.aws.amazon.com/sdk-for-javascript/'},
            {'title': 'The Provider Pattern — Martin Fowler', 'url': 'https://martinfowler.com/eaaCatalog/serviceLocator.html'},
        ],
    },
    {
        'title': 'Advanced Abstract Factory: Registries and Conventions',
        'desc': 'Factory registries, convention-based selection, and keeping factories open for extension.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Build a factory registry',
            'Select factories by convention or config',
            'Keep the family open-closed',
            'Handle cross-cutting product concerns',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Factory Registries', 'paras': [
                'When the number of families grows (ten databases, eight clouds), a registry maps a key to its factory: register(Key, Factory) at startup, then factory = registry.get(key). New families join by registration — the core stays closed.',
            ], 'code': {'lang': 'python', 'body': '''
# Registry: new families join by registration, core never changes
class FactoryRegistry:
    def __init__(self):
        self._factories = {}

    def register(self, name, factory):
        self._factories[name] = factory

    def get(self, name):
        if name not in self._factories:
            raise KeyError(f'unknown family: {name}')
        return self._factories[name]

registry = FactoryRegistry()
registry.register('postgres', PostgresFactory())
registry.register('sqlite', SqliteFactory())
registry.register('memory', MemoryFactory())

factory = registry.get(os.environ.get('DB', 'memory'))'''}},
            {'heading': 'Cross-Cutting Concerns', 'paras': [
                'Every product may need logging, metrics, or retries. A decorator factory wraps every product the base factory creates — one place to add cross-cutting behavior across the whole family, keeping each concrete factory simple.',
            ]},
        ],
        'practice': {
            'title': 'Design the Registry',
            'intro': 'A data layer supports 6 databases; each needs a matching Connection and Query product with metrics.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Build the registry and register the six factories.'},
                {'label': 'Task 2', 'text': 'Add a decorator factory that wraps products with metrics — no concrete factory changes.'},
                {'label': 'Task 3', 'text': 'Design the error when an unknown family is requested, and the startup validation that lists registered families.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain how a registry keeps the abstract factory open-closed.'},
            {'label': 'Implementation Design', 'text': 'Design a theme system where themes register as factories and the UI core stays untouched. How do themes discover and hot-swap?'},
            {'label': 'Boundary Testing', 'text': 'Two factories produce the same product type with different behaviors. Design the contract test that keeps them substitutable.'},
        ],
        'takeaways': [
            'Registries make families extensible by registration',
            'Decorator factories apply cross-cutting concerns once',
            'Startup validation catches misconfiguration early',
            'Contract tests keep families substitutable',
        ],
        'further': [
            {'title': 'Registry Pattern — Martin Fowler', 'url': 'https://martinfowler.com/eaaCatalog/registry.html'},
            {'title': 'Decorator Pattern — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/decorator'},
        ],
    },
    {
        'title': 'Abstract Factory: Review & Mastery Quiz',
        'desc': 'Scenario questions on product families, registries, and consistency.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate abstract factory concepts',
            'Design product families',
            'Extend families safely',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Abstract factory creates? (A: one object / B: a family of related objects / C: a singleton)',
                'Q2: The core guarantee of the pattern is? (A: speed / B: family consistency / C: caching)',
                'Q3: Factory method differs from abstract factory by? (A: one product vs a family / B: being faster / C: using singletons)',
                'Q4: True or false: the composition root is where concrete factories are chosen.',
                'Q5: A registry keeps the family? (A: open for extension / B: fixed forever / C: un-testable)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A reporting tool must render PDF and HTML with matching headers, tables, and charts. Design the abstract factory and the registry.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "just new it up everywhere" breaks product families.'},
        ],
        'takeaways': [
            'Q1: B; Q2: B; Q3: A; Q4: true; Q5: A',
            'Families stay consistent by construction',
            'Registries and decorators keep them extensible',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# ADAPTER
# ─────────────────────────────────────────────────────────────────────────────
_t('adapter', [
    {
        'title': 'Adapter: Make Incompatible Interfaces Talk',
        'desc': 'Wrapping a foreign interface so your code can use it without changing either side.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the adapter intent',
            'Build an object adapter',
            'Distinguish adapter from facade and proxy',
            'Apply adapters at boundaries',
        ],
        'prereqs': ['patterns/facade', 'patterns/proxy'],
        'sections': [
            {'heading': 'The Problem', 'paras': [
                'A third-party SDK exposes saveDocument(doc, opts) but your code calls store(doc). Without an adapter, either your code contorts to the SDK or you fork the SDK. The adapter wraps the SDK and exposes the interface your code expects.',
            ], 'code': {'lang': 'java', 'body': '''
// Your interface (what the app wants):
interface DocumentStore {
    void store(Document doc);
}

// The third-party SDK (what exists):
class SdkClient {
    void saveDocument(Document doc, SaveOptions opts) { ... }
}

// Adapter: translate without touching either side
class SdkStoreAdapter implements DocumentStore {
    private final SdkClient client;
    SdkStoreAdapter(SdkClient c) { this.client = c; }
    public void store(Document doc) {
        client.saveDocument(doc, SaveOptions.defaults());
    }
}'''}},
            {'heading': 'Adapters vs Facades vs Proxies', 'paras': [
                'An adapter changes an interface (so A can call B). A facade simplifies a complex subsystem behind one simple interface. A proxy controls access to an object (lazy, remote, protected). They are often combined at real boundaries, but their intents differ.',
            ]},
        ],
        'practice': {
            'title': 'Adapt the Legacy System',
            'intro': 'Your new order service needs an interface the legacy billing system does not provide.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the interface your code needs and the legacy API that exists.'},
                {'label': 'Task 2', 'text': 'Write the adapter translating calls, including error and return translation.'},
                {'label': 'Task 3', 'text': 'Unit-test the adapter with a fake legacy client.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about the difference between adapting an interface and simplifying a subsystem. Start with the intent.'},
            {'label': 'Compare & Contrast', 'text': 'Compare adapter, facade, and proxy with concrete examples of each at a system boundary.'},
            {'label': 'Boundary Testing', 'text': 'The SDK throws checked exceptions your interface does not declare. Design the adapter\'s error translation policy.'},
        ],
        'takeaways': [
            'Adapters translate interfaces at boundaries',
            'Neither side changes — the adapter bridges',
            'Adapter changes shape; facade simplifies; proxy controls',
            'Error translation is part of the adapter contract',
        ],
        'further': [
            {'title': 'Adapter — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/adapter'},
            {'title': 'Adapter Pattern — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Adapter_pattern'},
        ],
    },
    {
        'title': 'Adapter in Production: Third-Party Integration',
        'desc': 'Wrapping vendor SDKs, legacy systems, and wire protocols behind stable internal interfaces.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Isolate vendor SDKs behind adapters',
            'Translate data models at the boundary',
            'Handle version and breaking changes',
            'Test integrations without the vendor',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Vendor Isolation', 'paras': [
                'Direct vendor-SDK calls scattered through the codebase make upgrades and vendor swaps terrifying. One adapter per vendor concentrates the SDK dependency: the rest of the codebase depends on your interface, so a vendor change touches one file.',
            ], 'code': {'lang': 'go', 'body': '''
// Vendor isolated behind one adapter
type PaymentProvider interface {
    Charge(ctx context.Context, req ChargeRequest) (ChargeResult, error)
    Refund(ctx context.Context, id string, amount int64) error
}

// StripeAdapter and SquareAdapter both implement PaymentProvider.
// The checkout code depends on the interface, never on a vendor SDK.
// Vendor SDK upgrade or swap = touch one adapter file.'''}},
            {'heading': 'Model Translation', 'paras': [
                'Adapters translate between your domain model and the vendor model at the boundary: your Money{amount, currency} becomes the vendor\'s {amount_cents, currency_code}. The translation — including rounding, timezones, and enums — lives in one place with tests.',
            ]},
        ],
        'practice': {
            'title': 'Isolate the Email Vendor',
            'intro': 'Email sending is called from 30 places directly on the vendor SDK. A new vendor must be supported.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the EmailSender interface your app needs.'},
                {'label': 'Task 2', 'text': 'Write the adapter for the current vendor and the new one.'},
                {'label': 'Task 3', 'text': 'Migrate the 30 call sites to the interface and delete the direct SDK usage.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why adapter isolation makes vendor upgrades a one-file change. Ask me what breaks if it is not isolated.'},
            {'label': 'Implementation Design', 'text': 'Design a payment adapter with idempotency keys and retries inside the adapter. What does the app\'s interface look like?'},
            {'label': 'Boundary Testing', 'text': 'The vendor changes a field meaning silently. Design the adapter\'s defensive validation and the contract test against the live vendor.'},
        ],
        'takeaways': [
            'One adapter per vendor concentrates SDK risk',
            'Model translation lives at the boundary, tested',
            'The app depends on your interface, not the vendor',
            'Contract tests catch silent vendor changes',
        ],
        'further': [
            {'title': 'Anti-Corruption Layer — DDD', 'url': 'https://martinfowler.com/bliki/AntiCorruptionLayer.html'},
            {'title': 'Vendor Lock-In Mitigation — Martin Fowler', 'url': 'https://martinfowler.com/bliki/SoftwareLockIn.html'},
        ],
    },
    {
        'title': 'Advanced Adapter: Protocols and Wire-Level Adaptation',
        'desc': 'Adapter hierarchies, protocol translation, and adapting at the network level.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Build adapter hierarchies for families of vendors',
            'Translate protocols (REST, gRPC, SOAP) at the boundary',
            'Compose adapters with decorators',
            'Design adaptive fallbacks',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Adapter Hierarchies', 'paras': [
                'When several vendors share behavior, an abstract adapter holds the common logic and concrete adapters override the differences: AbstractPaymentAdapter implements retry, idempotency, and logging; StripeAdapter and SquareAdapter supply the wire calls.',
            ], 'code': {'lang': 'python', 'body': '''
# Abstract adapter: shared cross-cutting, concrete wire calls
class AbstractPaymentAdapter(PaymentProvider):
    def __init__(self, client):
        self.client = client

    def charge(self, req):
        for attempt in retry_backoff(3):        # shared logic
            try:
                return self._do_charge(req)
            except TransientError:
                continue

    def _do_charge(self, req):                  # implemented by subclass
        raise NotImplementedError

class StripeAdapter(AbstractPaymentAdapter):
    def _do_charge(self, req):
        return self.client.charges.create(**to_stripe(req))'''}},
            {'heading': 'Protocol Translation', 'paras': [
                'At the network boundary, adapters translate protocols: a gRPC service wrapped so a REST client can call it, or a SOAP API exposed as JSON. The adapter handles the mechanics — framing, headers, errors — so the core stays protocol-agnostic.',
            ]},
        ],
        'practice': {
            'title': 'Design the Adapter Stack',
            'intro': 'Three vendors expose three different protocols (REST, gRPC, SOAP) for the same capability.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the common interface and the shared abstract adapter.'},
                {'label': 'Task 2', 'text': 'Implement one concrete adapter per protocol.'},
                {'label': 'Task 3', 'text': 'Add a circuit-breaker decorator around the adapter stack and test a vendor outage.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why an abstract adapter centralizes retries while concrete adapters own wire formats.'},
            {'label': 'Implementation Design', 'text': 'Design a protocol-translating gateway: REST in, gRPC out, with error mapping and headers. What belongs in the adapter?'},
            {'label': 'Boundary Testing', 'text': 'One vendor is down. Design the adaptive fallback that routes to a healthy vendor through the same adapter interface.'},
        ],
        'takeaways': [
            'Abstract adapters centralize shared cross-cutting logic',
            'Protocol translation belongs at the boundary',
            'Decorators compose around adapters for resilience',
            'Adapters enable adaptive multi-vendor fallback',
        ],
        'further': [
            {'title': 'Anti-Corruption Layer — DDD', 'url': 'https://martinfowler.com/bliki/AntiCorruptionLayer.html'},
            {'title': 'BFF (Backend for Frontend) as Adapter', 'url': 'https://samnewman.io/patterns/architectural/bff/'},
        ],
    },
    {
        'title': 'Adapter: Review & Mastery Quiz',
        'desc': 'Scenario questions on interface translation and vendor isolation.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate adapter concepts',
            'Isolate vendor dependencies',
            'Translate models safely',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: An adapter changes? (A: the interface / B: the algorithm / C: the database)',
                'Q2: A facade differs from an adapter by? (A: simplifying vs translating / B: being slower / C: being faster)',
                'Q3: Vendor SDK usage should be? (A: scattered / B: isolated behind one adapter / C: copied)',
                'Q4: True or false: model translation should live at the boundary.',
                'Q5: A proxy controls? (A: access / B: translation / C: rendering)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A legacy SOAP billing API must serve the new JSON order service. Design the adapter, the model translation, and the error mapping.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why calling the vendor SDK in 30 places is a time bomb.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: B; Q4: true; Q5: A',
            'Adapters make boundaries clean and upgrades cheap',
            'Isolate, translate, and test at the edge',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# AMBASSADOR
# ─────────────────────────────────────────────────────────────────────────────
_t('ambassador', [
    {
        'title': 'Ambassador: Offload Client-Side Plumbing',
        'desc': 'Putting retries, caching, and circuit breaking in a helper that sits in front of a remote service.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the ambassador intent',
            'Identify client-side concerns it offloads',
            'Compare with proxy and sidecar',
            'Build a basic ambassador',
        ],
        'prereqs': ['patterns/proxy', 'patterns/sidecar', 'principles/circuit-breaker'],
        'sections': [
            {'heading': 'The Problem', 'paras': [
                'Every client of a remote service reimplements the same plumbing: retries, timeouts, caching, circuit breaking, logging. The ambassador is a co-located helper that performs these cross-cutting concerns on the client\'s behalf, so the client code stays thin.',
                'Unlike a general proxy, the ambassador is service-specific and lives with the client — often as a library or a sidecar process in the same pod.',
            ], 'code': {'lang': 'go', 'body': '''
// Ambassador: wraps the remote client with resilience, transparently
type Ambassador struct {
    client  *remote.Client
    breaker *circuit.Breaker
    cache   *cache.TTL
}

func (a *Ambassador) Get(ctx context.Context, key string) (Value, error) {
    if v, ok := a.cache.Get(key); ok {           // caching for the client
        return v, nil
    }
    var v Value
    err := a.breaker.Call(func() error {         // circuit breaking
        var e error
        for attempt := 0; attempt < 3; attempt++ {   // retries
            v, e = a.client.Get(ctx, key)
            if e == nil { break }
            backoff(attempt)
        }
        return e
    })
    if err != nil { return Value{}, err }
    a.cache.Set(key, v, 5*time.Minute)
    return v, nil
}'''}},
            {'heading': 'Ambassador vs Proxy vs Sidecar', 'paras': [
                'A proxy sits in front of a service (server-side). An ambassador sits with the client (client-side) and does work on its behalf. A sidecar is an ambassador packaged as a separate process next to the app — same intent, deployment choice.',
            ]},
        ],
        'practice': {
            'title': 'Build the Ambassador',
            'intro': 'Your app calls a search API and reimplements retries and caching at every call site.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Identify the cross-cutting concerns repeated across call sites.'},
                {'label': 'Task 2', 'text': 'Build the ambassador encapsulating retries, caching, and circuit breaking.'},
                {'label': 'Task 3', 'text': 'Rewrite call sites to use it and measure the code removed.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why client-side plumbing belongs in an ambassador rather than the business code. Start with retries.'},
            {'label': 'Compare & Contrast', 'text': 'Compare ambassador with sidecar, proxy, and service mesh. Where does each deployment model fit?'},
            {'label': 'Boundary Testing', 'text': 'The ambassador\'s circuit breaker opens and the fallback must still serve something. Design the degraded response.'},
        ],
        'takeaways': [
            'Ambassadors offload client-side cross-cutting concerns',
            'Clients stay thin; resilience lives in the helper',
            'Sidecar is the process-deployment form',
            'Fallbacks inside the ambassador define degraded behavior',
        ],
        'further': [
            {'title': 'Ambassador Pattern — Microsoft Docs', 'url': 'https://learn.microsoft.com/en-us/azure/architecture/patterns/ambassador'},
            {'title': 'Sidecar Pattern — Microsoft Docs', 'url': 'https://learn.microsoft.com/en-us/azure/architecture/patterns/sidecar'},
        ],
    },
    {
        'title': 'Ambassador in Production: Sidecars and Meshes',
        'desc': 'Ambassadors as sidecar processes, in service meshes, and in client SDKs.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Deploy an ambassador as a sidecar',
            'Understand mesh proxies as ambassadors',
            'Version the ambassador with the client',
            'Monitor ambassador health',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Sidecar Deployment', 'paras': [
                'The ambassador as a sidecar container runs in the same pod as the app, sharing localhost. The app calls the sidecar; the sidecar talks to the remote service with all the resilience logic. Language-independent, hot-updatable without rebuilding the app.',
            ], 'code': {'lang': 'yaml', 'body': '''
# Sidecar ambassador in a Kubernetes pod
containers:
  - name: app
    image: my-app
    command: ["/app", "--search=http://localhost:9090"]
  - name: ambassador
    image: search-ambassador:1.4   # retries, circuit breaker, cache
    ports:
      - containerPort: 9090        # app calls localhost:9090
# Update the ambassador image without rebuilding the app.'''}},
            {'heading': 'Service Mesh as Ambassador', 'paras': [
                'A service mesh data plane (Envoy, Linkerd) is an ambassador deployed everywhere: it injects retries, timeouts, mTLS, and circuit breaking into every service-to-service call without application changes. The mesh centralizes the ambassador pattern across the platform.',
            ]},
        ],
        'practice': {
            'title': 'Choose the Deployment',
            'intro': 'Your platform has 12 services calling a flaky partner API.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Compare: in-process library ambassador vs sidecar vs mesh proxy.'},
                {'label': 'Task 2', 'text': 'Pick one for the flaky partner and justify with update and isolation needs.'},
                {'label': 'Task 3', 'text': 'Design the monitoring: how do you see ambassador retry and breaker events per service?'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me the trade-offs between an in-process ambassador and a sidecar process. Ask me about updates and failure modes.'},
            {'label': 'Implementation Design', 'text': 'Design a mesh proxy configuration for a partner API: retries, timeout budget, circuit breaker, and observability. What are the exact settings?'},
            {'label': 'Boundary Testing', 'text': 'The sidecar crashes but the app is fine. Design the degraded mode (fail open, direct call) and its alert.'},
        ],
        'takeaways': [
            'Sidecars deploy ambassadors without app rebuilds',
            'Service meshes centralize the pattern platform-wide',
            'Ambassador updates are independent of the app',
            'Ambassador health is a first-class signal',
        ],
        'further': [
            {'title': 'Sidecar Pattern — Microsoft Docs', 'url': 'https://learn.microsoft.com/en-us/azure/architecture/patterns/sidecar'},
            {'title': 'What is a Service Mesh — Istio', 'url': 'https://istio.io/latest/about/service-mesh/'},
        ],
    },
    {
        'title': 'Advanced Ambassador: Smart Clients and Fallback Routing',
        'desc': 'Ambassadors that learn, route around failures, and negotiate capabilities.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Build a smart client with adaptive routing',
            'Add capability negotiation to the ambassador',
            'Design multi-provider fallback routing',
            'Keep ambassador state consistent',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Smart Clients', 'paras': [
                'An advanced ambassador measures backend health (latency, error rate) and routes requests adaptively: healthy instances get traffic, degraded ones get drained, and a region-wide failure triggers cross-region routing. This is client-side load balancing as an ambassador concern.',
            ], 'code': {'lang': 'go', 'body': '''
// Adaptive routing in the ambassador: prefer healthy backends
func (a *Ambassador) pickBackend() *Backend {
    var best *Backend
    for _, b := range a.backends {
        if b.score() < threshold && (best == nil || b.score() > best.score()) {
            best = b
        }
    }
    if best == nil { return a.fallbackBackend() }  // cross-region fallback
    return best
}'''}},
            {'heading': 'Capability Negotiation', 'paras': [
                'Backends differ in capabilities (one supports bulk ops, another does not). The ambassador negotiates at connect time and exposes only what the chosen backend supports — the app sees one interface, the ambassador adapts to reality.',
            ]},
        ],
        'practice': {
            'title': 'Design the Smart Ambassador',
            'intro': 'Three backend clusters serve one API; one cluster degrades during a sale.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the health scoring and the routing rule.'},
                {'label': 'Task 2', 'text': 'Add the cross-region fallback with the capacity guard.'},
                {'label': 'Task 3', 'text': 'Design the observability: routing decisions, drained backends, and fallback events.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain how an ambassador does client-side load balancing without the app knowing.'},
            {'label': 'Implementation Design', 'text': 'Design capability negotiation between an app and a storage backend with two feature levels. What happens at connect, and what at runtime?'},
            {'label': 'Boundary Testing', 'text': 'All backends degrade at once. Design the ambassador\'s final fallback and the alert that fires.'},
        ],
        'takeaways': [
            'Smart ambassadors route around unhealthy backends',
            'Capability negotiation keeps one interface, many realities',
            'Cross-region fallback needs capacity guards',
            'Ambassador decisions must be observable',
        ],
        'further': [
            {'title': 'Client-Side Load Balancing — Finagle', 'url': 'https://twitter.github.io/finagle/guide/Clients.html'},
            {'title': 'Envoy Upstream Selection', 'url': 'https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/load_balancing/overview'},
        ],
    },
    {
        'title': 'Ambassador: Review & Mastery Quiz',
        'desc': 'Scenario questions on client plumbing, sidecars, and smart routing.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate ambassador concepts',
            'Choose deployment models',
            'Design smart clients',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: An ambassador offloads? (A: server-side rendering / B: client-side plumbing / C: database writes)',
                'Q2: A sidecar is an ambassador? (A: in a separate process / B: in the database / C: in the UI)',
                'Q3: A service mesh data plane is? (A: an ambassador everywhere / B: a database / C: a UI framework)',
                'Q4: True or false: the app should reimplement retries at every call site.',
                'Q5: Smart ambassadors route based on? (A: backend health / B: user name / C: cache size)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A partner API fails often; 6 services call it. Design the ambassador strategy (library vs sidecar vs mesh) with the exact resilience settings.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why client-side resilience should be centralized, not copy-pasted.'},
        ],
        'takeaways': [
            'Q1: B; Q2: A; Q3: A; Q4: false; Q5: A',
            'Ambassadors centralize client resilience',
            'Sidecars and meshes operationalize the pattern',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# B-TREE
# ─────────────────────────────────────────────────────────────────────────────
_t('b-tree', [
    {
        'title': 'B-Trees: The Database Index Workhorse',
        'desc': 'Why databases store indexes in B-trees and how the structure keeps lookups logarithmic.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the B-tree structure',
            'Understand the branching factor',
            'Trace a lookup, insert, and split',
            'Explain why B-trees beat binary trees on disk',
        ],
        'prereqs': ['patterns/hash-index', 'principles/caching'],
        'sections': [
            {'heading': 'The Structure', 'paras': [
                'A B-tree is a balanced multi-way tree: every node holds up to B keys, every internal node has up to B+1 children, and all leaves sit at the same depth. The branching factor (B, often hundreds) keeps the tree short — a 4-level B-tree can index billions of keys.',
                'On disk, each node is one page read. A binary tree would need ~30 disk reads to find a key among a billion; a B-tree needs ~4. That is the entire reason databases use B-trees.',
            ], 'code': {'lang': 'text', 'body': '''
B-tree shape (branching factor 4, leaves at same depth):
            [  17 |  52 ]
           /     |      \\
    [3|9|11]  [23|31|41]  [61|77|83]
      |   |      |   |       |   |
     leaf leaf  leaf leaf   leaf leaf

Lookup: 3-4 page reads for billions of keys (vs ~30 for binary).'''}},
            {'heading': 'Ordered and Range-Friendly', 'paras': [
                'Because keys stay sorted, B-trees support range scans (WHERE id BETWEEN 10 AND 20), ordered iteration, and prefix matching — things hash indexes cannot do. This is why B-trees are the default index for most databases.',
            ]},
        ],
        'practice': {
            'title': 'Trace the Operations',
            'intro': 'A B-tree with branching factor 3 stores integers. Insert 25 into a full leaf [20, 23, 27].',
            'tasks': [
                {'label': 'Task 1', 'text': 'Trace the split: which key promotes to the parent, and how the leaf divides?'},
                {'label': 'Task 2', 'text': 'Trace a range scan [23, 41] through the tree — which nodes are visited?'},
                {'label': 'Task 3', 'text': 'Estimate the tree height for 1 billion keys at branching factor 200 and justify the disk reads.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why branching factor matters more than tree cleverness on disk. Start with page reads.'},
            {'label': 'Compare & Contrast', 'text': 'Compare B-trees with LSM-trees for write-heavy vs read-heavy workloads. When is each the right choice?'},
            {'label': 'Boundary Testing', 'text': 'A B-tree index becomes fragmented with random inserts. Design the page-fill heuristics (like the 2/3 fill rule) that delay splits.'},
        ],
        'takeaways': [
            'B-trees are balanced, multi-way, disk-aware trees',
            'Branching factor keeps height logarithmic in page reads',
            'Sorted keys enable range scans and prefixes',
            'One node = one page read is the design constraint',
        ],
        'further': [
            {'title': 'B-Tree — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/B-tree'},
            {'title': 'Use The Index, Luke!', 'url': 'https://use-the-index-luke.com/'},
        ],
    },
    {
        'title': 'B-Trees in Production: Database Indexes',
        'desc': 'How Postgres, MySQL, and SQLite index with B-trees, and how to read an execution plan.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Read an index scan vs sequential scan plan',
            'Design composite B-tree indexes',
            'Use index-only scans',
            'Avoid index-destroying queries',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Reading the Plan', 'paras': [
                'EXPLAIN shows whether the query used an index scan (B-tree descent) or a sequential scan (full table). An index scan costs ~log(n) reads; a sequential scan costs n. The optimizer picks based on selectivity — that is the planning decision.',
            ], 'code': {'lang': 'sql', 'body': '''
-- Composite index: (tenant_id, status, created_at)
CREATE INDEX idx_orders_tenant_status_created
  ON orders (tenant_id, status, created_at);

-- Uses the B-tree: exact tenant, exact status, range on created_at
SELECT * FROM orders
WHERE tenant_id = 42 AND status = 'open' AND created_at > now() - '1 day';

-- Index-only scan: all columns in the index -> no table read
EXPLAIN ANALYZE SELECT tenant_id, status FROM orders
WHERE tenant_id = 42 AND status = 'open';'''}},
            {'heading': 'Composite Index Design', 'paras': [
                'Composite indexes work left to right: leading columns should be equality filters, trailing columns ranges. A query filtering on the second column alone cannot use the index — a classic index-destroying mistake.',
            ]},
        ],
        'practice': {
            'title': 'Design the Index Set',
            'intro': 'A orders table queried by: tenant+status, tenant+created_at range, and status alone.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the minimal index set that covers the three query shapes.'},
                {'label': 'Task 2', 'text': 'Use EXPLAIN ANALYZE to verify each query hits an index, not a seq scan.'},
                {'label': 'Task 3', 'text': 'Find the query that cannot use an index (status alone with low selectivity) and decide: index it or accept the scan?'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why composite indexes follow left-to-right prefix rules. Ask me to design one for a real table.'},
            {'label': 'Implementation Design', 'text': 'Design indexes for a messaging table queried by (conversation_id, created_at DESC) with a LIMIT. What does the B-tree order support?'},
            {'label': 'Boundary Testing', 'text': 'A function on the indexed column (WHERE lower(email) = ...) kills the index. Design the expression-index fix.'},
        ],
        'takeaways': [
            'Index scans cost log(n); seq scans cost n',
            'Composite indexes follow left-prefix rules',
            'Index-only scans skip the table entirely',
            'Functions on indexed columns defeat the index',
        ],
        'further': [
            {'title': 'PostgreSQL — Index Types', 'url': 'https://www.postgresql.org/docs/current/indexes-types.html'},
            {'title': 'Use The Index, Luke!', 'url': 'https://use-the-index-luke.com/sql/where-clause'},
        ],
    },
    {
        'title': 'Advanced B-Trees: Concurrency and Variants',
        'desc': 'B-link trees, optimistic locking, and the variants databases actually use.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Explain concurrency on B-trees',
            'Describe the B-link variant',
            'Understand crash safety (WAL + page checksums)',
            'Compare with LSM-trees deeply',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Concurrency', 'paras': [
                'Concurrent inserts into a B-tree split nodes, and a reader mid-traversal must not see a torn state. Databases use latches (short-lived page locks), optimistic latch coupling, and B-link trees where each node points to its right sibling so a split never loses a reader.',
            ], 'code': {'lang': 'text', 'body': '''
Concurrency techniques on B-trees:
  - Latch coupling: hold a node latch while acquiring the child
  - B-link: each node links to its right sibling; a reader that
    finds a split mid-traversal follows the link instead of restarting
  - Copy-on-write B-trees (LMDB style): readers see a consistent snapshot
Crash safety:
  - WAL: redo records make page changes durable and replayable
  - Page checksums: detect torn pages from partial writes'''}},
            {'heading': 'B-Tree vs LSM', 'paras': [
                'B-trees optimize reads (in-place, sorted, compact); LSM-trees optimize writes (append-only, batched compaction) at the cost of read amplification and space. Read-heavy OLTP prefers B-trees; write-heavy ingest prefers LSMs. Many modern stores (RocksDB) are LSM; most classic RDBMS are B-tree.',
            ]},
        ],
        'practice': {
            'title': 'Compare the Engines',
            'intro': 'A metrics-ingestion workload writes 100k rows/s and reads recent values.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Model the write cost of a B-tree (random page writes, splits) vs an LSM (sequential appends).'},
                {'label': 'Task 2', 'text': 'Model the read cost of the LSM (multi-level lookups) vs the B-tree (log n).'},
                {'label': 'Task 3', 'text': 'Pick an engine and justify with the workload\'s write/read ratio.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why B-link trees keep readers safe during splits.'},
            {'label': 'Implementation Design', 'text': 'Design a storage engine that serves hot recent data from an LSM and archive data from a B-tree. How do queries route?'},
            {'label': 'Boundary Testing', 'text': 'A crash mid-split corrupts the tree. Design the WAL + recovery path that reconstructs the invariant.'},
        ],
        'takeaways': [
            'Latches and B-links keep concurrent traversals safe',
            'WAL and checksums make page writes crash-safe',
            'B-trees read-optimized, LSM write-optimized',
            'Hybrid engines route by data age',
        ],
        'further': [
            {'title': 'B-Link Trees — Paper', 'url': 'https://www.cs.cornell.edu/courses/cs4410/2016fa/slides/lecture17.pdf'},
            {'title': 'The Design and Implementation of InnoDB', 'url': 'https://dev.mysql.com/doc/refman/8.0/en/innodb-architecture.html'},
        ],
    },
    {
        'title': 'B-Trees: Review & Mastery Quiz',
        'desc': 'Scenario questions on structure, indexes, and engines.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate B-tree concepts',
            'Design composite indexes',
            'Choose engines',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: B-trees beat binary trees on disk because of? (A: branching factor / B: smaller data / C: caching)',
                'Q2: Range scans are supported because B-trees? (A: keep keys sorted / B: hash keys / C: compress data)',
                'Q3: A composite index (a, b, c) is useless for a filter on? (A: a / B: b alone / C: a and b)',
                'Q4: True or false: an index-only scan avoids reading the table.',
                'Q5: LSM-trees optimize? (A: reads / B: writes / C: memory)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A chat app stores messages by conversation. Design the B-tree index for "latest 50 messages of conversation X" and explain the page reads.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "add an index" needs a query-shape analysis first.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: B; Q4: true; Q5: B',
            'B-trees are the read-optimized default',
            'Index design follows query shapes',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# BLOOM FILTER
# ─────────────────────────────────────────────────────────────────────────────
_t('bloom-filter', [
    {
        'title': 'Bloom Filters: Maybe Yes, Definitely No',
        'desc': 'A space-efficient probabilistic set that never says "no" wrongly but may say "yes" wrongly.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the bloom filter structure',
            'Describe false positives and zero false negatives',
            'Tune size and hash count',
            'Use "definitely not in set" to skip work',
        ],
        'prereqs': ['principles/caching', 'principles/eventual-consistency'],
        'sections': [
            {'heading': 'The Structure', 'paras': [
                'A bloom filter is a bit array with k hash functions. Adding a key sets k bits. Membership checks the same k bits: if any is zero, the key is definitely absent; if all are set, the key is probably present (false positive possible).',
                'The magic: no false negatives. "Definitely not in the set" is a reliable negative that lets systems skip expensive lookups.',
            ], 'code': {'lang': 'python', 'body': '''
# Bloom filter: the classic probabilistic set
import hashlib, struct

class BloomFilter:
    def __init__(self, size, k):
        self.bits = bytearray(size // 8 + 1)
        self.size, self.k = size, k

    def _hashes(self, key):
        return [int.from_bytes(hashlib.md5(f'{key}:{i}'.encode()).digest()[:4], 'big')
                % self.size for i in range(self.k)]

    def add(self, key):
        for h in self._hashes(key):
            self.bits[h // 8] |= 1 << (h % 8)

    def might_contain(self, key):
        return all(self.bits[h // 8] & (1 << (h % 8)) for h in self._hashes(key))

bf = BloomFilter(10_000, 7)
bf.add('user-42')
print(bf.might_contain('user-42'))   # True
print(bf.might_contain('user-99'))   # False (definitely absent)'''}},
            {'heading': 'Tuning', 'paras': [
                'False-positive rate depends on bit size m, keys n, and hash count k: k = (m/n) * ln 2 minimizes it. A 1% false-positive filter needs ~10 bits per key. Fewer bits = smaller but noisier.',
            ]},
        ],
        'practice': {
            'title': 'Skip the Cache Miss',
            'intro': 'A cache of 1M keys receives 100M lookups; most keys do not exist in the cache.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Estimate the false-positive rate for a 10M-bit filter over 1M keys with optimal k.'},
                {'label': 'Task 2', 'text': 'Design the flow: bloom filter before the cache to skip unnecessary lookups.'},
                {'label': 'Task 3', 'text': 'Quantify the savings when 90% of lookups hit "definitely absent".'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why a bloom filter never produces a false negative. Start with the bit-setting mechanics.'},
            {'label': 'Compare & Contrast', 'text': 'Compare bloom filters with hash sets and with counting bloom filters (deletions). When does each fit?'},
            {'label': 'Boundary Testing', 'text': 'The filter is 99% full and false positives skyrocket. Design the rebuild/rescale strategy without downtime.'},
        ],
        'takeaways': [
            'No false negatives; false positives tunable',
            'Bit array + k hashes, k = (m/n) ln 2 optimal',
            '"Definitely absent" is the valuable answer',
            'Counting filters add deletions',
        ],
        'further': [
            {'title': 'Bloom Filter — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Bloom_filter'},
            {'title': 'Bloom Filters Explained — Brilliant', 'url': 'https://brilliant.org/wiki/bloom-filter/'},
        ],
    },
    {
        'title': 'Bloom Filters in Production: Caches and Dedupe',
        'desc': 'Cache-thinning, URL deduplication, and spell-check-style membership in real systems.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Use bloom filters to thin cache lookups',
            'Deduplicate seen URLs and events',
            'Combine with a small exact cache',
            'Handle filter saturation',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Cache Thinning', 'paras': [
                'A bloom filter in front of a cache answers "is this key even worth a cache lookup?" for a fraction of the memory of the cache itself. Databases like Cassandra and RocksDB use them to skip SSTable lookups that cannot hit.',
            ], 'code': {'lang': 'go', 'body': '''
// Bloom filter guards the cache: skip lookups that cannot hit
var filter = bloom.New(1_000_000, 7)

func Get(key string) (Value, bool) {
    if !filter.TestString(key) {
        return Value{}, false     // definitely not in cache: skip
    }
    return cache.Get(key)          // only probable keys hit the cache
}

func Set(key string, v Value) {
    filter.AddString(key)
    cache.Set(key, v)
}'''}},
            {'heading': 'Deduplication', 'paras': [
                'Crawlers and event pipelines dedupe with bloom filters: "have I already seen this URL/event ID?" The no-false-negative property is exactly right — reprocessing an unseen event is safe, missing one is not.',
            ]},
        ],
        'practice': {
            'title': 'Dedupe the Event Stream',
            'intro': 'An event pipeline receives 50k events/s; ~10% are duplicates from retries.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the filter (size, k) for a day of events and the false-positive policy (drop vs verify).'},
                {'label': 'Task 2', 'text': 'Combine with a small exact LRU for recent IDs to cut false positives.'},
                {'label': 'Task 3', 'text': 'Design the daily rebuild and the saturation alert.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why dedupe needs "no false negatives" and how the false-positive policy (drop vs verify) is a product choice.'},
            {'label': 'Implementation Design', 'text': 'Design a spell-check membership filter: dictionary in a bloom filter, correction lookup only on probable matches. What is the UX of a false positive?'},
            {'label': 'Boundary Testing', 'text': 'The filter saturates and everything looks present. Design the rebuild trigger and the exact-set fallback.'},
        ],
        'takeaways': [
            'Bloom filters skip impossible lookups cheaply',
            'Dedupe loves the no-false-negative property',
            'Pair with a small exact cache to cut false positives',
            'Saturation needs rebuild triggers',
        ],
        'further': [
            {'title': 'RocksDB — Bloom Filters', 'url': 'https://github.com/facebook/rocksdb/wiki/RocksDB-Bloom-Filter'},
            {'title': 'Bloom filter in Apache Cassandra', 'url': 'https://cassandra.apache.org/doc/stable/cassandra/operating/bloom_filters.html'},
        ],
    },
    {
        'title': 'Advanced Bloom Filters: Counting and Scaling',
        'desc': 'Counting filters, scalable filters, and distributed membership at scale.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Implement a counting bloom filter',
            'Design a scalable (multi-tier) filter',
            'Shard filters across nodes',
            'Merge filters in distributed systems',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Counting Filters', 'paras': [
                'A counting bloom filter replaces bits with small counters, supporting deletion. The cost: 4x memory. It is the standard when membership changes over time (caching proxies that evict).',
            ], 'code': {'lang': 'python', 'body': '''
# Counting filter: counters instead of bits, deletion supported
class CountingBloom:
    def __init__(self, size, k):
        self.counters = [0] * size
        self.k = k

    def _hashes(self, key):  # returns k positions
        ...

    def add(self, key):
        for p in self._hashes(key):
            self.counters[p] += 1

    def remove(self, key):   # the operation plain filters lack
        for p in self._hashes(key):
            if self.counters[p] > 0:
                self.counters[p] -= 1

    def might_contain(self, key):
        return all(self.counters[p] > 0 for p in self._hashes(key))'''}},
            {'heading': 'Scalable and Distributed', 'paras': [
                'Scalable filters grow by adding tiers when the base saturates; lookups check all tiers. Distributed systems merge filters (bitwise OR) when memberships are unions — gossip protocols use this to spread "I have seen X" cheaply. Counting filters do not merge cleanly; plain ones do.',
            ]},
        ],
        'practice': {
            'title': 'Design the Scalable Filter',
            'intro': 'A cache membership filter grows past its design size every week.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the tiered scalable filter: when to add a tier, and how lookups check tiers.'},
                {'label': 'Task 2', 'text': 'Design cross-node merging for the gossip membership use case.'},
                {'label': 'Task 3', 'text': 'Quantify the memory and false-positive trade-off per tier.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why counting filters cannot merge while plain filters can (bitwise OR).'},
            {'label': 'Implementation Design', 'text': 'Design distributed dedupe across 10 nodes: shared filter vs merged per-node filters. What are the consistency requirements?'},
            {'label': 'Boundary Testing', 'text': 'A counter overflows (a hot key set many times). Design the saturation handling that prevents a false-negative.'},
        ],
        'takeaways': [
            'Counting filters add deletion at 4x memory',
            'Scalable filters grow by tiers on saturation',
            'Plain filters merge via bitwise OR',
            'Gossip membership loves mergeable filters',
        ],
        'further': [
            {'title': 'Scalable Bloom Filters — Paper', 'url': 'https://gsd.di.uminho.pt/members/cbm/ps/dbloom.pdf'},
            {'title': 'Counting Bloom Filters — Paper', 'url': 'https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=6f95bf72914165dc59dd8d07e1db7ab84a33c6f0'},
        ],
    },
    {
        'title': 'Bloom Filters: Review & Mastery Quiz',
        'desc': 'Scenario questions on structure, tuning, and scale.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate bloom filter concepts',
            'Tune filters for workloads',
            'Design scalable membership',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: A bloom filter never produces? (A: false positives / B: false negatives / C: collisions)',
                'Q2: The optimal hash count is? (A: (m/n) ln 2 / B: m / C: k=1)',
                'Q3: The valuable answer a bloom filter gives is? (A: definitely present / B: definitely absent / C: exact count)',
                'Q4: True or false: counting filters support deletion.',
                'Q5: Plain bloom filters merge via? (A: bitwise OR / B: addition / C: XOR)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A URL crawler must not revisit 1B URLs with 200MB of memory. Design the filter and the false-positive policy.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "sometimes says yes" is a feature, not a bug.'},
        ],
        'takeaways': [
            'Q1: B; Q2: A; Q3: B; Q4: true; Q5: A',
            'Probabilistic membership trades exactness for space',
            'No false negatives is the superpower',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# BRIDGE
# ─────────────────────────────────────────────────────────────────────────────
_t('bridge', [
    {
        'title': 'Bridge: Decouple Abstraction from Implementation',
        'desc': 'When an abstraction grows in two dimensions, bridge separates them so each can vary independently.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the bridge intent',
            'Identify two-dimensional hierarchies',
            'Split abstraction and implementation',
            'Compare with inheritance explosion',
        ],
        'prereqs': ['patterns/abstract-factory', 'patterns/strategy'],
        'sections': [
            {'heading': 'The Problem: Exploding Hierarchy', 'paras': [
                'A remote-control abstraction with two device implementations (TV, Radio) and two input methods (basic, advanced) naively produces 4 classes: BasicTvRemote, AdvancedTvRemote, BasicRadioRemote, AdvancedRadioRemote. Add a third device and it grows to 6 — an inheritance explosion.',
                'Bridge separates the two axes: the Remote hierarchy (abstraction) holds a reference to the Device hierarchy (implementation). Each axis varies independently.',
            ], 'code': {'lang': 'java', 'body': '''
// Bridge: abstraction (Remote) holds an implementation (Device)
interface Device { void powerOn(); void setVolume(int v); int getVolume(); }

abstract class Remote {
    protected final Device device;
    Remote(Device d) { this.device = d; }
    abstract void togglePower();
    abstract void volumeUp();
}

class BasicRemote extends Remote {      // one axis: input method
    BasicRemote(Device d) { super(d); }
    public void togglePower() { device.powerOn(); }
    public void volumeUp() { device.setVolume(device.getVolume() + 1); }
}
// AdvancedRemote extends Remote, same Device reference.

// Adding a third device = new Device class. Adding a third input =
// new Remote class. No explosion: 2 axes x N each.'''}},
            {'heading': 'When to Bridge', 'paras': [
                'Bridge pays off when you have two independent axes of variation that both grow. If only one dimension varies, an interface suffices; if the axes are coupled, bridge fights reality. The pattern is about finding the seam between abstraction and implementation.',
            ]},
        ],
        'practice': {
            'title': 'Find the Second Axis',
            'intro': 'A message sender supports email/SMS/push and plain/rich/encrypted formats.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Count the classes in the naive cross-product.'},
                {'label': 'Task 2', 'text': 'Design the bridge: Message abstraction holding a Channel implementation.'},
                {'label': 'Task 3', 'text': 'Add one new channel and one new format; count the classes added under each design.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why two growing axes need bridge while one axis does not. Start with the class count.'},
            {'label': 'Compare & Contrast', 'text': 'Compare bridge with strategy and adapter. How do they differ in intent and structure?'},
            {'label': 'Boundary Testing', 'text': 'The two axes are not truly independent (certain formats only work on certain channels). Design the capability check that keeps the bridge honest.'},
        ],
        'takeaways': [
            'Bridge separates two independent axes of variation',
            'It kills the inheritance explosion (cross-product classes)',
            'Abstraction holds the implementation, both vary freely',
            'Use it when axes grow independently',
        ],
        'further': [
            {'title': 'Bridge — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/bridge'},
            {'title': 'Bridge Pattern — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Bridge_pattern'},
        ],
    },
    {
        'title': 'Bridge in Production: Pluggable Rendering and Persistence',
        'desc': 'UI toolkits, renderers, and persistence engines that vary on two axes.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design rendering bridges (view + platform)',
            'Design persistence bridges (model + store)',
            'Swap implementations at runtime',
            'Keep both axes testable',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'The Rendering Bridge', 'paras': [
                'A charting library faces two axes: chart types (bar, line, pie) and rendering targets (SVG, Canvas, WebGL). Bridge gives one chart hierarchy holding a Renderer implementation — adding a chart type or a renderer never touches the other axis.',
            ], 'code': {'lang': 'typescript', 'body': '''
// Bridge: Chart (abstraction) holds a Renderer (implementation)
interface Renderer {
    drawRect(x: number, y: number, w: number, h: number): void;
    drawLine(points: number[]): void;
}

abstract class Chart {
    constructor(protected renderer: Renderer) {}
    abstract render(): void;
}

class BarChart extends Chart {            // one axis: chart type
    render() {
        this.renderer.drawRect(0, 0, 10, 20);
        this.renderer.drawRect(12, 0, 10, 5);
    }
}
class SvgRenderer implements Renderer { ... }
class CanvasRenderer implements Renderer { ... }

// renderer = new CanvasRenderer()  -> swap at runtime, chart untouched'''}},
            {'heading': 'The Persistence Bridge', 'paras': [
                'Models vary by domain; stores vary by engine (SQL, Redis, S3). Bridge lets a domain repository hold a Store implementation — the same repository logic reads from Postgres or an in-memory store for tests, without an inheritance explosion.',
            ]},
        ],
        'practice': {
            'title': 'Bridge the Rendering Stack',
            'intro': 'A reporting app renders 5 report types to HTML, PDF, and JSON.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Count naive classes (5 x 3) and design the bridge instead.'},
                {'label': 'Task 2', 'text': 'Implement one report type on two renderers to prove the seam.'},
                {'label': 'Task 3', 'text': 'Add a fourth renderer and show only one class is added.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why the bridge seam is "the abstraction holds the implementation" and how that differs from plain interfaces.'},
            {'label': 'Implementation Design', 'text': 'Design a persistence bridge for a domain: repository abstraction + store implementations, with the wiring at the composition root.'},
            {'label': 'Boundary Testing', 'text': 'A renderer only supports a subset of chart features. Design the capability query that keeps the bridge honest.'},
        ],
        'takeaways': [
            'Chart/device-style pairs are textbook bridge territory',
            'Renderers and stores are implementation axes',
            'Runtime swapping is a free benefit of the seam',
            'Capability queries prevent dishonest implementations',
        ],
        'further': [
            {'title': 'Bridge Pattern in UI Toolkits', 'url': 'https://refactoring.guru/design-patterns/bridge'},
            {'title': 'Repository + Bridge — DDD', 'url': 'https://martinfowler.com/eaaCatalog/repository.html'},
        ],
    },
    {
        'title': 'Advanced Bridge: Engines and Platforms',
        'desc': 'JVM/CLR/JS engine abstractions, multi-platform kernels, and the bridge in real products.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Design engine-agnostic abstractions',
            'Apply bridge across platforms',
            'Version the two axes independently',
            'Avoid the "bridge everything" trap',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Engine Abstractions', 'paras': [
                'Scripting engines (V8, JSC, Hermes) are a classic bridge: the runtime abstraction (executing scripts, calling functions) is separate from the engine implementation. Products swap engines under the same abstraction to tune performance or memory.',
            ], 'code': {'lang': 'text', 'body': '''
Engine bridge (React Native / Hermes / JSC):
  JSExecutor (abstraction): evaluate, call, createRuntime
  HermesExecutor, JSCExecutor (implementations)
  -> swap engines by configuration; app code untouched.

The bridge pattern at platform scale:
  - OS abstraction (POSIX) is the oldest bridge
  - Database drivers (JDBC/ODBC) bridge SQL dialects
  - Web APIs bridge browser engines'''}},
            {'heading': 'Versioning and the Over-Bridge Trap', 'paras': [
                'The two axes version independently: the abstraction bumps when contracts change, implementations bump on engine upgrades. But not everything needs a bridge — bridging a single-axis variation adds a pointless indirection layer. Bridge only the axes that actually vary.',
            ]},
        ],
        'practice': {
            'title': 'Design the Engine Seam',
            'intro': 'A product runs scripts on V8 today and must support Hermes for mobile.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the JSExecutor abstraction the product uses.'},
                {'label': 'Task 2', 'text': 'Implement V8 and Hermes adapters behind it.'},
                {'label': 'Task 3', 'text': 'Design the capability/version matrix and the startup engine selection.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can articulate when an abstraction is a bridge (two axes) versus a needless indirection (one axis).'},
            {'label': 'Implementation Design', 'text': 'Design a cross-platform storage layer (local disk, cloud, memory) as a bridge where the data-model axis is separate from the store axis.'},
            {'label': 'Boundary Testing', 'text': 'An engine supports a language feature another lacks. Design the feature detection that degrades gracefully instead of crashing.'},
        ],
        'takeaways': [
            'Engines and platforms are the bridge at product scale',
            'The two axes version independently',
            'Feature detection keeps implementations honest',
            'Bridge only axes that actually vary',
        ],
        'further': [
            {'title': 'Hermes Engine — React Native', 'url': 'https://reactnative.dev/docs/hermes'},
            {'title': 'JDBC — the database bridge', 'url': 'https://docs.oracle.com/javase/tutorial/jdbc/overview/index.html'},
        ],
    },
    {
        'title': 'Bridge: Review & Mastery Quiz',
        'desc': 'Scenario questions on two-axis variation and the seam.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate bridge concepts',
            'Detect inheritance explosions',
            'Design honest seams',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Bridge separates? (A: two axes of variation / B: two teams / C: two databases)',
                'Q2: The naive cross-product of 3 x 4 classes is? (A: 7 / B: 12 / C: 3)',
                'Q3: In bridge, the abstraction? (A: holds the implementation / B: extends it / C: copies it)',
                'Q4: True or false: bridge lets each axis vary independently.',
                'Q5: Bridging a single-axis variation is usually? (A: necessary / B: needless indirection / C: faster)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A notification system supports 3 channels and 4 format policies. Redesign the naive 12-class hierarchy as a bridge and count the real classes.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "an interface and two implementations" is not automatically a bridge.'},
        ],
        'takeaways': [
            'Q1: A; Q2: B; Q3: A; Q4: true; Q5: B',
            'Bridge kills cross-product class explosions',
            'The seam is the abstraction holding the implementation',
        ],
    },
])
