#!/usr/bin/env python3
"""Deep curriculum data batch 9: strategy, template-method, two-phase-commit, visitor."""

TOPICS = {}


def _t(slug, topics):
    TOPICS[slug] = topics
    return topics


# ─────────────────────────────────────────────────────────────────────────────
# STRATEGY
# ─────────────────────────────────────────────────────────────────────────────
_t('strategy', [
    {
        'title': 'Strategy: Swap Algorithms at Runtime',
        'desc': 'Defining a family of algorithms and making them interchangeable through composition.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the strategy intent',
            'Define a family of algorithms',
            'Compose instead of inherit',
            'Swap strategies at runtime',
        ],
        'prereqs': ['patterns/factory', 'principles/open-closed'],
        'sections': [
            {'heading': 'The Problem', 'paras': [
                'A class that computes in one way (a formatter, a pricing rule, a sort) hard-codes that algorithm. Every new algorithm means editing the class, growing an if-chain, and risking regressions. Strategy extracts each algorithm into its own object with a common interface; the context holds whichever strategy it needs and can swap it at runtime.',
            ], 'code': {'lang': 'python', 'body': '''
# Strategy: algorithms as interchangeable objects
from abc import ABC, abstractmethod

class Pricing(ABC):                 # the strategy interface
    @abstractmethod
    def price(self, base: float) -> float: ...

class StandardPricing(Pricing):
    def price(self, base): return base

class MemberPricing(Pricing):
    def price(self, base): return base * 0.85

class PremiumPricing(Pricing):
    def price(self, base): return base * 0.7

class Cart:
    def __init__(self, strategy: Pricing):
        self.strategy = strategy    # context holds the strategy
    def set_strategy(self, s: Pricing):
        self.strategy = s           # swap at runtime
    def total(self, base): return self.strategy.price(base)

cart = Cart(MemberPricing())
print(cart.total(100))              # 85.0
cart.set_strategy(PremiumPricing()) # swap: no if-chains
print(cart.total(100))              # 70.0'''}},
            {'heading': 'Composition over Inheritance', 'paras': [
                'Strategy is composition: the context has a strategy rather than being one. New algorithms extend the family without touching the context — the open-closed principle in action. The cost is indirection: one more object per algorithm, and callers must know which strategy fits.',
            ]},
        ],
        'practice': {
            'title': 'Build the Formatter Family',
            'intro': 'An exporter formats orders as JSON, XML, or CSV; the format is chosen per request.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the Formatter interface and three strategies.'},
                {'label': 'Task 2', 'text': 'Wire the context to accept and swap strategies.'},
                {'label': 'Task 3', 'text': 'Add a fourth format without touching the context.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why strategies beat if-chains. Start with adding a new format.'},
            {'label': 'Compare & Contrast', 'text': 'Compare strategy with the template method: composition vs inheritance for algorithm families.'},
            {'label': 'Boundary Testing', 'text': 'A strategy throws mid-use. Design the fallback strategy and the error path.'},
        ],
        'takeaways': [
            'Strategy makes algorithms interchangeable objects',
            'The context composes, not inherits',
            'Runtime swapping removes if-chains',
            'New algorithms extend without editing the context',
        ],
        'further': [
            {'title': 'Strategy — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/strategy'},
            {'title': 'Strategy pattern — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Strategy_pattern'},
        ],
    },
    {
        'title': 'Strategy in Production: Pricing, Routing, and Policy Engines',
        'desc': 'Strategy families in real systems — config-driven selection and registry-based strategies.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Select strategies by config',
            'Register strategies in a registry',
            'Combine strategies',
            'Test strategy swaps',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Config-Driven Selection', 'paras': [
                'Production systems select the strategy from configuration: a pricing tier, a routing rule, a policy name. A registry maps names to strategy instances, so adding a strategy is data plus one class — no call-site edits. The selection point (config, header, user attribute) decides which strategy the context composes.',
            ], 'code': {'lang': 'typescript', 'body': '''
// Strategy registry: select by name from config
type Routing = (req: Req) => string;

const strategies: Record<string, Routing> = {
  roundRobin: (r) => pick(pool),
  leastConn:   (r) => leastBusy(pool),
  ipHash:      (r) => pool[hash(r.ip) % pool.length],
};

export function route(req: Req, name: string): string {
  const fn = strategies[name] ?? strategies.roundRobin; // fallback
  return fn(req);
}
// New strategy = one entry in the map. Callers never change.
// Config: route_strategy: leastConn flips behavior without a
// deploy of the routing code — the definition of open/closed.'''}},
            {'heading': 'Composed Strategies', 'paras': [
                'Strategies compose: a checkout applies member discount, then loyalty points, then tax — a pipeline of strategies, or a composite strategy that runs a list. The composite is itself a strategy, so the pattern nests cleanly. Testing swaps a strategy for a fake and asserts the context behavior changed.',
            ]},
        ],
        'practice': {
            'title': 'Design the Policy Registry',
            'intro': 'A gateway routes by header, IP, or weight; operators change the policy via config with zero deploys.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the strategy interface and three implementations.'},
                {'label': 'Task 2', 'text': 'Build the registry and the config-driven selection.'},
                {'label': 'Task 3', 'text': 'Add the fallback and the test that swaps strategies.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why a registry turns strategy selection into configuration.'},
            {'label': 'Implementation Design', 'text': 'Design a pricing engine: tiers, coupons, and taxes as composable strategies. How do they combine?'},
            {'label': 'Boundary Testing', 'text': 'A config names a strategy that does not exist. Design the validation and the fallback.'},
        ],
        'takeaways': [
            'Registries make strategy selection configurable',
            'New strategies are data plus one class',
            'Strategies compose into pipelines',
            'Tests swap strategies to assert behavior change',
        ],
        'further': [
            {'title': 'Strategy — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/strategy'},
            {'title': 'Policy engines — OPA', 'url': 'https://www.openpolicyagent.org/docs/latest/'},
        ],
    },
    {
        'title': 'Advanced Strategy: Functional Strategies and Dynamic Selection',
        'desc': 'Strategies as functions, closure-based state, and machine-learned selection.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Use functional strategies',
            'Capture state in closures',
            'Select strategies dynamically',
            'Avoid strategy explosion',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Functional Strategies', 'paras': [
                'Where the strategy has no state of its own, a function is the strategy — the interface is a signature, the implementations are lambdas. Closures capture per-request state (a user tier, a region) without a class per combination. This collapses dozens of classes into a handful of functions and keeps the registry tiny.',
            ], 'code': {'lang': 'python', 'body': '''
# Functional strategies: the interface is a signature
from typing import Callable

Pricing = Callable[[float, float], float]   # (base, factor) -> price

def make_tier_price(tier: str) -> Pricing:   # closure captures state
    rates = {'standard': 1.0, 'member': 0.85, 'premium': 0.7}
    return lambda base, factor: base * rates[tier] * factor

prices: dict[str, Pricing] = {
    'standard': make_tier_price('standard'),
    'member':   make_tier_price('member'),
    'premium':  make_tier_price('premium'),
}
total = prices['premium'](100, 1.2)          # 84.0
# Dynamic selection: the tier comes from the user, ML scoring,
# or A/B flags at call time — the call site never changes.'''}},
            {'heading': 'Dynamic Selection and Limits', 'paras': [
                'Selection can be dynamic — a scorer picks the strategy per request (A/B, ML, load). The discipline: the strategy family must stay small and the selection point explicit. Strategy explosion (a class per combination) is the smell; composition and functions compress it.',
            ]},
        ],
        'practice': {
            'title': 'Functionalize the Family',
            'intro': 'Twelve pricing strategy classes for region x tier combinations. Collapse them.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Identify the orthogonal axes (tier, region, promotion).'},
                {'label': 'Task 2', 'text': 'Rebuild as closures composing the axes.'},
                {'label': 'Task 3', 'text': 'Add a dynamic selector (A/B flag) without new classes.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain when a function beats a class as a strategy.'},
            {'label': 'Implementation Design', 'text': 'Design a routing family with an ML scorer selecting the strategy per request. How do you keep it testable?'},
            {'label': 'Boundary Testing', 'text': 'The dynamic selector oscillates between strategies. Design the hysteresis and the logging that catches it.'},
        ],
        'takeaways': [
            'Functions are stateless strategies',
            'Closures capture state without class explosion',
            'Dynamic selection keeps call sites stable',
            'Small families and explicit selection avoid the smell',
        ],
        'further': [
            {'title': 'Strategy — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/strategy'},
            {'title': 'Partial application and closures — MDN', 'url': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures'},
        ],
    },
    {
        'title': 'Strategy: Review & Mastery Quiz',
        'desc': 'Scenario questions on families, selection, and composition.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate strategy concepts',
            'Select and compose strategies',
            'Recognize the explosion smell',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Strategy makes algorithms? (A: interchangeable / B: private / C: faster)',
                'Q2: The context holds a strategy via? (A: composition / B: inheritance / C: globals)',
                'Q3: Registries make selection? (A: configurable / B: random / C: slower)',
                'Q4: True or false: strategies compose into pipelines.',
                'Q5: Strategy explosion comes from? (A: a class per combination / B: too few strategies / C: caching)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A checkout applies tier, promotion, and tax. Design the strategy family and its composition order.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why composition beats inheritance for algorithm families.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Interchangeable algorithms, selected and composed',
            'Functions keep the family small',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# TEMPLATE METHOD
# ─────────────────────────────────────────────────────────────────────────────
_t('template-method', [
    {
        'title': 'Template Method: A Skeleton with Hooks',
        'desc': 'Defining the skeleton of an algorithm in a base class, letting subclasses fill the steps.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the template method intent',
            'Define the algorithm skeleton',
            'Override the variable steps',
            'Keep the flow invariant',
        ],
        'prereqs': ['patterns/strategy', 'principles/open-closed'],
        'sections': [
            {'heading': 'The Problem', 'paras': [
                'Several algorithms share the same steps but differ in the details: a data importer validates, parses, stores; a report generator gathers, formats, sends. Copying the flow per class duplicates it and drifts. The template method fixes the skeleton once in a base class, and subclasses override the variable steps — the flow itself never changes.',
            ], 'code': {'lang': 'python', 'body': '''
# Template method: skeleton fixed, steps overridable
from abc import ABC, abstractmethod

class DataImporter(ABC):
    def import_data(self, source):      # the template method
        data = self.validate(source)    # step 1
        rows = self.parse(data)         # step 2
        self.store(rows)                # step 3
        self.after_import()             # hook, optional

    @abstractmethod
    def validate(self, source): ...
    @abstractmethod
    def parse(self, data): ...
    @abstractmethod
    def store(self, rows): ...

    def after_import(self):             # hook: default no-op
        pass

class CsvImporter(DataImporter):
    def validate(self, s): return s if s.endswith('.csv') else error()
    def parse(self, d): return read_csv(d)
    def store(self, rows): return db.insert(rows)

class JsonImporter(DataImporter):
    def validate(self, s): return s if s.endswith('.json') else error()
    def parse(self, d): return read_json(d)
    def store(self, rows): return db.insert(rows)
# The flow (validate -> parse -> store) is written once.'''}},
            {'heading': 'Template vs Strategy', 'paras': [
                'Both fix a shape; they differ in mechanism. Template method uses inheritance — the subclass fills the steps of the base algorithm. Strategy uses composition — the context holds an interchangeable algorithm object. Template method is right when the steps are inherently shared; strategy when the algorithm family must swap at runtime.',
            ]},
        ],
        'practice': {
            'title': 'Build the Report Skeleton',
            'intro': 'Reports gather data, format it, and deliver via email, file, or dashboard — one flow, three variants.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the template method and the abstract steps.'},
                {'label': 'Task 2', 'text': 'Implement three concrete subclasses.'},
                {'label': 'Task 3', 'text': 'Add a hook (e.g., notify) that defaults off and is turned on by one subclass.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why fixing the skeleton prevents duplication drift.'},
            {'label': 'Compare & Contrast', 'text': 'Compare template method with strategy: when does inheritance beat composition and vice versa?'},
            {'label': 'Boundary Testing', 'text': 'A subclass forgets to call a required cleanup step. Design the base-class guard that enforces it.'},
        ],
        'takeaways': [
            'Template method fixes the algorithm skeleton',
            'Subclasses override the variable steps',
            'Hooks provide optional extension points',
            'The flow is written once and cannot drift',
        ],
        'further': [
            {'title': 'Template Method — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/template-method'},
            {'title': 'Template method — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Template_method_pattern'},
        ],
    },
    {
        'title': 'Template Method in Production: Frameworks and Lifecycles',
        'desc': 'Frameworks as template methods — callbacks, lifecycles, and inversion of control.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Recognize IoC frameworks',
            'Use lifecycle callbacks',
            'Implement framework hooks',
            'Test template subclasses',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Frameworks Are Template Methods', 'paras': [
                'Every framework is a template method on a grand scale: the framework runs the flow (request handling, component lifecycle) and calls your code at the hooks. That inversion of control — the framework calls you, not the reverse — is the template method at framework scale. Your components override steps: lifecycle callbacks, request handlers, middleware.',
            ], 'code': {'lang': 'typescript', 'body': '''
// A component lifecycle as a template method (framework-style)
abstract class Lifecycle {
  async run(): Promise<void> {          // fixed skeleton
    await this.onBeforeMount();
    await this.mount();
    await this.onMounted();             // hook
    await this.idle();
    await this.onBeforeUnmount();
    await this.unmount();
    await this.onUnmounted();           // hook
  }
  protected abstract mount(): Promise<void>;
  protected abstract unmount(): Promise<void>;
  protected abstract idle(): Promise<void>;
  protected async onBeforeMount(): Promise<void> {}
  protected async onMounted(): Promise<void> {}
  protected async onBeforeUnmount(): Promise<void> {}
  protected async onUnmounted(): Promise<void> {}
}
// The framework calls run(); your subclass fills mount/unmount.
// Hooks default to no-ops so subclasses override only what they
// need — the skeleton is shared, the steps are yours.'''}},
            {'heading': 'Hooks and Defaults', 'paras': [
                'Well-designed template methods provide sensible default steps and hooks so subclasses override the minimum. The anti-pattern: template methods that force subclasses to override steps they do not care about, or skeletons so rigid they cannot express the variation — then composition (strategy, callbacks) is the better tool.',
            ]},
        ],
        'practice': {
            'title': 'Implement a Lifecycle',
            'intro': 'A plugin system: plugins start, register routes, serve, and stop — with optional hooks for health and metrics.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the plugin skeleton with abstract steps and hooks.'},
                {'label': 'Task 2', 'text': 'Implement two plugins overriding the minimum.'},
                {'label': 'Task 3', 'text': 'Test the flow: a failing step must run the cleanup hooks.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why every framework is a template method and what hooks are for.'},
            {'label': 'Implementation Design', 'text': 'Design a middleware pipeline as a template method with before/after hooks per stage.'},
            {'label': 'Boundary Testing', 'text': 'A plugin override throws mid-lifecycle. Design the base-class error handling that still unmounts cleanly.'},
        ],
        'takeaways': [
            'Frameworks are template methods at scale',
            'IoC: the framework calls you at the hooks',
            'Sensible defaults minimize overrides',
            'Rigid skeletons signal composition instead',
        ],
        'further': [
            {'title': 'Inversion of Control — Martin Fowler', 'url': 'https://martinfowler.com/bliki/InversionOfControl.html'},
            {'title': 'React lifecycle — docs', 'url': 'https://react.dev/learn/lifecycle-of-reactive-effects'},
        ],
    },
    {
        'title': 'Advanced Template Method: Enforcing Invariants and Contracts',
        'desc': 'Making the skeleton safe: assertions, contracts, and design-by-contract in template methods.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Enforce step contracts',
            'Assert invariants in the skeleton',
            'Design hook ordering',
            'Audit subclass behavior',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Contracts in the Skeleton', 'paras': [
                'The skeleton owns the contract: preconditions before each step, postconditions after, invariants across the flow. Assertions in the template method catch subclasses that violate the contract — the base class verifies, the subclass provides. Design-by-contract turns the template method into a verifiable pipeline rather than a hope.',
            ], 'code': {'lang': 'python', 'body': '''
# Template method with contract enforcement
class Pipeline(ABC):
    def run(self, item):
        self._check(item, 'input')            # precondition
        cleaned = self.clean(item)
        self._check(cleaned, 'clean')         # step contract
        rows = self.transform(cleaned)
        self._check(rows, 'transform')
        self._invariant(rows)                 # invariant across flow
        return self.load(rows)

    def _check(self, value, stage):
        if value is None:
            raise ContractError(f'{stage} produced None')

    def _invariant(self, rows):
        if len(rows) != len({r.id for r in rows}):
            raise ContractError('duplicate ids after transform')

    @abstractmethod
    def clean(self, item): ...
    @abstractmethod
    def transform(self, cleaned): ...
    @abstractmethod
    def load(self, rows): ...
# Subclasses implement steps; the base enforces the contract
# between them — failure surfaces at the violating stage.'''}},
            {'heading': 'Hook Ordering and Auditing', 'paras': [
                'Hook ordering is part of the contract: before-hooks run in order, after-hooks in reverse, cleanups always run. Auditing the flow (logging each step and its timing) belongs in the skeleton, not the subclasses — every subclass gets observability for free.',
            ]},
        ],
        'practice': {
            'title': 'Harden the Skeleton',
            'intro': 'An ETL pipeline has had silent data-quality failures; the steps are subclassed by three teams.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Add pre/post contracts and the flow invariant.'},
                {'label': 'Task 2', 'text': 'Add step-level logging and timing to the skeleton.'},
                {'label': 'Task 3', 'text': 'Verify a violating subclass fails at the stage, not downstream.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why the skeleton, not the subclasses, should own the contract.'},
            {'label': 'Implementation Design', 'text': 'Design a validation pipeline: per-step preconditions and a cross-step invariant. Where do the assertions live?'},
            {'label': 'Boundary Testing', 'text': 'A subclass returns valid-but-wrong data. Design the invariant that catches it at the right stage.'},
        ],
        'takeaways': [
            'The skeleton owns pre/postconditions and invariants',
            'Assertions catch contract violations at the stage',
            'Hook ordering and cleanups are part of the contract',
            'Observability in the skeleton benefits every subclass',
        ],
        'further': [
            {'title': 'Design by Contract — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Design_by_contract'},
            {'title': 'Template Method — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/template-method'},
        ],
    },
    {
        'title': 'Template Method: Review & Mastery Quiz',
        'desc': 'Scenario questions on skeletons, hooks, and contracts.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate template method concepts',
            'Design hooks',
            'Enforce contracts',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Template method fixes? (A: the algorithm skeleton / B: the data / C: the UI)',
                'Q2: Subclasses fill? (A: the variable steps / B: the main method / C: the cache)',
                'Q3: A hook is? (A: an optional extension point / B: a database / C: an error)',
                'Q4: True or false: frameworks are template methods at scale.',
                'Q5: Contracts in the skeleton belong? (A: in the base class / B: in each subclass / C: nowhere)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A payment provider integration: authorize, capture, settle — one skeleton, two providers. Design the template and the hooks.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why the flow should be written once and only the steps overridden.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'One skeleton, overridable steps, optional hooks',
            'Contracts make the skeleton verifiable',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# TWO-PHASE COMMIT
# ─────────────────────────────────────────────────────────────────────────────
_t('two-phase-commit', [
    {
        'title': 'Two-Phase Commit: Atomicity Across Systems',
        'desc': 'Coordinating commit or abort across multiple participants so they agree atomically.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the 2PC protocol',
            'Describe the two phases',
            'Understand the coordinator',
            'Know the blocking problem',
        ],
        'prereqs': ['principles/acid', 'patterns/saga'],
        'sections': [
            {'heading': 'The Protocol', 'paras': [
                'A transaction spans two databases; each can commit or abort independently, but the business needs both or neither. 2PC adds a coordinator. Phase one (prepare): every participant prepares — writes its state so it can commit or roll back — and votes yes or no. Phase two (commit/abort): if all voted yes, the coordinator tells everyone to commit; if any voted no, everyone aborts. Atomicity through agreement.',
            ], 'code': {'lang': 'text', 'body': '''
Two-phase commit:
  Phase 1 - Prepare:
    coordinator -> participant: "can you commit?"
    participant: writes prepare log, holds the locks
    participant -> coordinator: vote YES or NO
  Phase 2 - Decide:
    all YES  -> coordinator: "commit" (participants commit)
    any NO   -> coordinator: "abort"  (participants roll back)
  Participants:
    - never commit before the coordinator decides
    - once they vote YES, they MUST follow the decision
  The catch: while waiting for the decision, a participant
  holds its locks and stays available-but-blocked. If the
  coordinator dies mid-protocol, participants block until a
  new coordinator completes the decision — the blocking
  problem of 2PC.'''}},
            {'heading': 'When It Works', 'paras': [
                '2PC gives strong atomicity across participants — the reason it powers distributed databases and XA transactions. It works best when participants are few, reliable, and the coordinator is highly available. The cost: blocking on failures and coordination latency — which is why modern microservices prefer sagas and accept eventual consistency.',
            ]},
        ],
        'practice': {
            'title': 'Trace the Protocol',
            'intro': 'A transfer moves money from Bank A to Bank B — two databases, one transaction.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Trace prepare, votes, and commit on the happy path.'},
                {'label': 'Task 2', 'text': 'Trace an abort when Bank B votes no.'},
                {'label': 'Task 3', 'text': 'Describe what happens if the coordinator dies after the first YES.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why participants must follow the decision after voting yes.'},
            {'label': 'Compare & Contrast', 'text': 'Compare 2PC with saga: atomicity and blocking vs eventual consistency and availability.'},
            {'label': 'Boundary Testing', 'text': 'A participant votes yes then crashes before committing. Design the recovery that completes the decision.'},
        ],
        'takeaways': [
            '2PC coordinates atomic commit across participants',
            'Prepare-then-decide with a coordinator',
            'Once yes, a participant must follow the decision',
            'Blocking on coordinator failure is the known cost',
        ],
        'further': [
            {'title': 'Two-phase commit — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Two-phase_commit_protocol'},
            {'title': 'Distributed Transactions — Martin Kleppmann', 'url': 'https://martin.kleppmann.com/2016/02/08/is-there-any-hope-for-consensus.html'},
        ],
    },
    {
        'title': 'Two-Phase Commit in Production: XA, Databases, and Coordinators',
        'desc': 'XA transactions, database 2PC, and the coordinator as the reliability crux.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Describe XA transactions',
            'Run database 2PC',
            'Make the coordinator reliable',
            'Handle participant failure',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'XA and Real Coordinators', 'paras': [
                'XA is the classic 2PC standard: a transaction manager coordinates participating resource managers (databases, queues). PostgreSQL, MySQL, and Oracle implement the prepare/commit interface. Production 2PC is only as reliable as the coordinator: it must persist its decision log before sending commit, so a crashed coordinator can resume and complete the decision.',
            ], 'code': {'lang': 'sql', 'body': '''
-- XA two-phase commit, PostgreSQL style
-- Phase 1: each participant prepares
xa start 'gtr1';
INSERT INTO accounts(id, balance) VALUES (1, 100);
xa end 'gtr1';
xa prepare 'gtr1';          -- vote YES (or NO on error)

xa start 'gtr1';
UPDATE accounts SET balance = balance - 50 WHERE id = 1;
xa end 'gtr1';
xa prepare 'gtr1';

-- Phase 2: coordinator decides
xa commit 'gtr1';           -- all prepared -> commit
-- or: xa rollback 'gtr1';  -- any no -> abort
-- The coordinator writes its decision to a durable log
-- BEFORE sending it, so a crash resumes the decision.'''}},
            {'heading': 'The Coordinator', 'paras': [
                'The coordinator is a single point of failure and the protocol\'s crux. Production coordinators: HA replicas, durable decision logs, and timeouts that drive recovery. Every participant must be able to ask the coordinator for the decision after a crash — the log is the source of truth.',
            ]},
        ],
        'practice': {
            'title': 'Operationalize 2PC',
            'intro': 'A checkout spans an orders DB and an inventory DB via XA; the coordinator must survive crashes.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the coordinator with a durable decision log.'},
                {'label': 'Task 2', 'text': 'Design participant recovery: asking the coordinator for the decision.'},
                {'label': 'Task 3', 'text': 'Design the timeout policy and the stuck-transaction dashboard.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why the coordinator must log its decision before sending it.'},
            {'label': 'Implementation Design', 'text': 'Design a 2PC coordinator service: prepare, decide, log, and recovery endpoints.'},
            {'label': 'Boundary Testing', 'text': 'A participant is unreachable at commit time. Design the retry, the timeout, and the manual resolution.'},
        ],
        'takeaways': [
            'XA standardizes 2PC across databases and queues',
            'The coordinator must log decisions durably',
            'Participants recover by asking the coordinator',
            'Timeouts and HA make the coordinator reliable',
        ],
        'further': [
            {'title': 'PostgreSQL — two-phase commit', 'url': 'https://www.postgresql.org/docs/current/sql-prepare-transaction.html'},
            {'title': 'XA transactions — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/X/Open_XA'},
        ],
    },
    {
        'title': 'Advanced 2PC: Blocking, Recovery, and Alternatives',
        'desc': 'The blocking problem, presumed-abort/presumed-commit, and when to avoid 2PC.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Analyze the blocking problem',
            'Design recovery protocols',
            'Use presumed-commit/abort',
            'Choose 2PC vs alternatives',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Blocking and Recovery', 'paras': [
                'The blocking problem: after a participant votes yes, it holds locks and waits for a decision that may never come (coordinator crash). Recovery protocols reconstruct the decision: participants contact the coordinator (or a replicated coordinator) whose durable log answers. Presumed-abort and presumed-commit are optimizations — abort unless told otherwise, or commit unless told otherwise — trading recovery complexity for fewer messages.',
            ], 'code': {'lang': 'text', 'body': '''
Recovery and optimizations:
  Coordinator crash recovery:
    - coordinator persists each decision before sending it
    - participants in doubt ask the (new) coordinator
    - HA coordinator: the log replicates, a peer resumes
  Presumed abort:
    - if the decision log has no entry, presume ABORT
    - participants resolve doubt quickly; commit needs a log
  Presumed commit:
    - if the decision log has no entry, presume COMMIT
    - faster common case; dangerous if a no-vote was lost
  Participant crash recovery:
    - on restart, check its prepare log; if prepared, ask the
      coordinator for the decision; apply it (commit or rollback)
  Timeouts:
    - every phase has a deadline; timeout drives the recovery
      query, never a unilateral commit by the participant'''}},
            {'heading': 'When Not to Use 2PC', 'paras': [
                '2PC trades availability for atomicity. When participants are many, slow, or failure-prone — typical microservices — sagas and idempotent steps preserve availability with eventual consistency. Use 2PC across few, reliable, homogeneous participants (databases), not across dozens of services.',
            ]},
        ],
        'practice': {
            'title': 'Design the Recovery',
            'intro': 'A coordinator crashes between prepare and commit across three participants.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the coordinator log and the participant doubt-resolution query.'},
                {'label': 'Task 2', 'text': 'Compare presumed-abort vs presumed-commit for this workload.'},
                {'label': 'Task 3', 'text': 'Design the timeout policy that bounds blocking.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain the blocking problem and how recovery resolves it.'},
            {'label': 'Implementation Design', 'text': 'Design a presumed-abort 2PC coordinator with an HA log. What does a participant do when in doubt?'},
            {'label': 'Boundary Testing', 'text': 'A no-vote is lost before reaching the coordinator. Design the safeguard that prevents a presumed-commit disaster.'},
        ],
        'takeaways': [
            'Blocking is 2PC\'s core failure cost',
            'Durable coordinator logs enable recovery',
            'Presumed-abort/commit optimize recovery',
            'Choose sagas across many services; 2PC across few databases',
        ],
        'further': [
            {'title': 'Consensus protocols — Kleppmann', 'url': 'https://martin.kleppmann.com/2016/02/08/is-there-any-hope-for-consensus.html'},
            {'title': '2PC — Distributed Systems Reading Group', 'url': 'https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf'},
        ],
    },
    {
        'title': 'Two-Phase Commit: Review & Mastery Quiz',
        'desc': 'Scenario questions on phases, recovery, and trade-offs.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate 2PC concepts',
            'Design recovery',
            'Choose the right protocol',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: 2PC provides? (A: atomicity across participants / B: eventual consistency / C: caching)',
                'Q2: Phase one is? (A: prepare and vote / B: commit / C: cleanup)',
                'Q3: The coordinator must persist? (A: its decision / B: the data / C: the cache)',
                'Q4: True or false: after voting yes, a participant must follow the decision.',
                'Q5: Microservices usually prefer? (A: sagas / B: 2PC / C: no transactions)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'Two financial databases need atomicity. Design the 2PC setup and its coordinator recovery.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer when 2PC is worth its blocking cost and when it is not.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Prepare-then-decide with durable coordination',
            'Atomicity for few reliable participants; sagas for many',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# VISITOR
# ─────────────────────────────────────────────────────────────────────────────
_t('visitor', [
    {
        'title': 'Visitor: Operations over Object Structures',
        'desc': 'Adding operations to objects without changing their classes — a visitor walks the structure.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the visitor intent',
            'Define the double dispatch',
            'Add operations without editing classes',
            'Know the structure constraint',
        ],
        'prereqs': ['patterns/composite', 'patterns/iterator'],
        'sections': [
            {'heading': 'The Problem', 'paras': [
                'An AST, a document tree, a config: classes are stable, but operations grow — pretty-print, validate, transform, compile. Adding each operation to every class is invasive and centralizes concern in the wrong place. The visitor moves the operation into one visitor class and dispatches on the element type — double dispatch: the element accepts the visitor, and the visitor\'s visit method matches the element\'s concrete type.',
            ], 'code': {'lang': 'python', 'body': '''
# Visitor: operation lives in the visitor, not the elements
from abc import ABC, abstractmethod

class Node(ABC):
    @abstractmethod
    def accept(self, v): ...           # double dispatch entry

class Num(Node):
    def __init__(self, value): self.value = value
    def accept(self, v): return v.visit_num(self)

class Add(Node):
    def __init__(self, left, right): self.left, self.right = left, right
    def accept(self, v): return v.visit_add(self)

class Eval(ABC):                       # one operation = one visitor
    def visit_num(self, n): return n.value
    def visit_add(self, a):
        return a.left.accept(self) + a.right.accept(self)

class ToString(ABC):                   # another operation, no edits
    def visit_num(self, n): return str(n.value)
    def visit_add(self, a):
        return f'({a.left.accept(self)} + {a.right.accept(self)})'

tree = Add(Num(2), Add(Num(3), Num(4)))
print(tree.accept(Eval()))             # 9
print(tree.accept(ToString()))         # (2 + (3 + 4))'''}},
            {'heading': 'The Cost', 'paras': [
                'The visitor adds a method per element type to every visitor — adding a new element class means editing every visitor. The pattern pays when the structure is stable and operations grow; it punishes structures that grow. That direction of change is the decision: stable structure, growing operations → visitor.',
            ]},
        ],
        'practice': {
            'title': 'Visit the Document Tree',
            'intro': 'A document AST (text, bold, link, list) needs rendering and word-count operations.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the elements with accept methods.'},
                {'label': 'Task 2', 'text': 'Implement the render visitor and the count visitor.'},
                {'label': 'Task 3', 'text': 'Add a third operation and confirm no element edits were needed.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why operations move out of the element classes.'},
            {'label': 'Compare & Contrast', 'text': 'Compare visitor with the strategy and with plain iteration plus instanceof checks.'},
            {'label': 'Boundary Testing', 'text': 'A new element type appears. Design the compilation error or fallback that catches unhandled visits.'},
        ],
        'takeaways': [
            'Visitor moves operations out of stable element classes',
            'Double dispatch routes by concrete element type',
            'Stable structure + growing operations is its niche',
            'New element types break every visitor — plan for it',
        ],
        'further': [
            {'title': 'Visitor — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/visitor'},
            {'title': 'Visitor pattern — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Visitor_pattern'},
        ],
    },
    {
        'title': 'Visitor in Production: Compilers and Analyzers',
        'desc': 'AST visitors in compilers, linters, and formatters — real production visitors.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Describe compiler visitors',
            'Write linter visitors',
            'Compose visitors',
            'Handle tree context',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Compilers as Visitors', 'paras': [
                'Every compiler, linter, and formatter walks an AST with visitors: type checking, lint rules, codegen, and formatting are separate visitors over a stable AST. ESLint\'s rules are visitors; Babel\'s transforms are visitors; so is the TypeScript checker. The AST stays stable; the toolchain\'s operations grow as visitors.',
            ], 'code': {'lang': 'javascript', 'body': '''
// ESLint rule as a visitor — operation over a stable AST
module.exports = {
  meta: { docs: { description: 'no console.log' } },
  create(context) {
    return {
      CallExpression(node) {            // visitor for one node type
        if (node.callee.type === 'MemberExpression' &&
            node.callee.object.name === 'console' &&
            node.callee.property.name === 'log') {
          context.report({ node, message: 'no console.log' });
        }
      },
      // Add a visitor per node type per rule. The AST never
      // changes; the rule set grows as new visitors.
    };
  },
};'''}},
            {'heading': 'Context and Composition', 'paras': [
                'Visitors often need context: parent pointers, scope chains, import tables. A walker carries the context and passes it to visitors, or visitors thread state through the traversal. Composing visitors (run several in one pass) needs a composite visitor — itself a visitor over the same structure.',
            ]},
        ],
        'practice': {
            'title': 'Write the Analyzer',
            'intro': 'A linter must find unused variables and forbid arrow-function abuse in one pass.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the visitor set and the shared context.'},
                {'label': 'Task 2', 'text': 'Implement the two rules as visitors.'},
                {'label': 'Task 3', 'text': 'Compose them into one pass and verify both report correctly.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why compilers are visitor ecosystems over stable ASTs.'},
            {'label': 'Implementation Design', 'text': 'Design a formatter visitor: indent, line width, and comments over an AST. Where does the context live?'},
            {'label': 'Boundary Testing', 'text': 'A visitor needs parent scope but the walker does not provide it. Design the context fix that does not break other visitors.'},
        ],
        'takeaways': [
            'Compilers, linters, and formatters are visitor ecosystems',
            'Rules and transforms are visitors over stable ASTs',
            'Context (scope, parents) is threaded through the walk',
            'Composite visitors run several operations in one pass',
        ],
        'further': [
            {'title': 'ESLint — custom rules', 'url': 'https://eslint.org/docs/latest/extend/custom-rules'},
            {'title': 'Babel — plugin handbook (visitors)', 'url': 'https://github.com/jamiebuilds/babel-handbook'},
        ],
    },
    {
        'title': 'Advanced Visitor: Extensible and Generic Visitors',
        'desc': 'Type-safe visitors, generics, and avoiding the expression problem.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Write type-safe visitors',
            'Use generic visitors',
            'Handle the expression problem',
            'Choose visitor vs pattern matching',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'The Expression Problem', 'paras': [
                'The expression problem: extend a system by adding new data variants (classes) or new operations (visitors) — classic OOP adds data variants easily (new classes) but struggles with new operations; visitors flip it: new operations are easy, new variants are painful. Modern languages solve it with pattern matching (exhaustive, compiler-checked) — the visitor without the boilerplate.',
            ], 'code': {'lang': 'typescript', 'body': '''
// Exhaustive pattern matching vs visitor boilerplate
type Expr =
  | { kind: 'num'; value: number }
  | { kind: 'add'; left: Expr; right: Expr }
  | { kind: 'mul'; left: Expr; right: Expr };

function evalExpr(e: Expr): number {
  switch (e.kind) {
    case 'num': return e.value;
    case 'add': return evalExpr(e.left) + evalExpr(e.right);
    case 'mul': return evalExpr(e.left) * evalExpr(e.right);
  }
}
// Adding an operation = adding a function (like a visitor).
// Adding a variant = the switch exhaustiveness check flags every
// operation that must handle it — the compiler does the bookkeeping
// the visitor pattern does by hand. Same expressiveness, no
// accept methods, no visitXXX boilerplate.'''}},
            {'heading': 'Choosing', 'paras': [
                'Use the visitor pattern where pattern matching is unavailable or where the structure is an external library you cannot change. Use pattern matching (Rust match, Kotlin sealed classes, TS discriminated unions, Python match) where available — it is the same idea with compiler enforcement. The visitor survives in ecosystems where the structure must stay open.',
            ]},
        ],
        'practice': {
            'title': 'Compare the Approaches',
            'intro': 'An expression language with num, add, and mul needs eval, print, and a new mul variant.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Implement eval and print as visitors.'},
                {'label': 'Task 2', 'text': 'Implement the same with sealed/discriminated union pattern matching.'},
                {'label': 'Task 3', 'text': 'Add a new variant in each and compare the change surface.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain the expression problem and why visitors are one side of it.'},
            {'label': 'Implementation Design', 'text': 'Design a type-safe visitor in a language with generics. How does the visitor carry a generic result type?'},
            {'label': 'Boundary Testing', 'text': 'A variant is added and half the visitors forget it. Design the exhaustive check that catches it at compile time.'},
        ],
        'takeaways': [
            'The expression problem pits variants against operations',
            'Visitors make operations easy, variants hard',
            'Pattern matching gives the same power with exhaustiveness',
            'Visitors persist where structures must stay open',
        ],
        'further': [
            {'title': 'The Expression Problem — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Expression_problem'},
            {'title': 'TypeScript discriminated unions', 'url': 'https://www.typescriptlang.org/docs/handbook/2/narrowing.html#discriminated-unions'},
        ],
    },
    {
        'title': 'Visitor: Review & Mastery Quiz',
        'desc': 'Scenario questions on dispatch, operations, and the expression problem.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate visitor concepts',
            'Design visitors',
            'Choose the right approach',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Visitor adds operations? (A: without editing elements / B: by editing elements / C: by copying)', 
                'Q2: Double dispatch matches? (A: the concrete element type / B: the visitor count / C: the cache)',
                'Q3: Compilers use visitors over? (A: ASTs / B: databases / C: sockets)',
                'Q4: True or false: adding a new element type breaks every visitor.',
                'Q5: Pattern matching gives visitors without? (A: boilerplate / B: correctness / C: speed)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A config tree (scalar, list, map) needs validate, flatten, and render. Design the visitor set.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer the expression problem and where visitors fit.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Stable structures, growing operations',
            'Pattern matching is the visitor with exhaustiveness',
        ],
    },
])
