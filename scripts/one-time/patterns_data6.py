#!/usr/bin/env python3
"""Deep curriculum data batch 6: mvc, mvcc-pattern, mvvm, observer, paxos, prototype."""

TOPICS = {}


def _t(slug, topics):
    TOPICS[slug] = topics
    return topics


# ─────────────────────────────────────────────────────────────────────────────
# MVC
# ─────────────────────────────────────────────────────────────────────────────
_t('mvc', [
    {
        'title': 'MVC: Model, View, Controller',
        'desc': 'Separating data, presentation, and input handling so each can change independently.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the MVC roles',
            'Trace a request through MVC',
            'Understand separation of concerns',
            'Know the MVC variants',
        ],
        'prereqs': ['principles/separation-of-concerns', 'patterns/observer'],
        'sections': [
            {'heading': 'The Roles', 'paras': [
                'The model holds data and business rules, the view renders the model, and the controller translates user input into model changes. The view observes the model and re-renders on change; the controller never renders and the model never touches the UI. Each layer can change without breaking the others.',
            ], 'code': {'lang': 'python', 'body': '''
# MVC flow: input -> controller -> model -> notify -> view re-render
class Model:
    def __init__(self):
        self.views = []
        self._value = 0
    def add_observer(self, view):
        self.views.append(view)
    def set(self, v):
        self._value = v
        for view in self.views: view.render()     # notify views

class Controller:
    def __init__(self, model):
        self.model = model
    def increment(self):
        self.model.set(self.model._value + 1)     # translate input

class View:
    def __init__(self, model):
        self.model = model
        self.model.add_observer(self)
    def render(self):
        print('display:', self.model._value)'''}},
            {'heading': 'Variants', 'paras': [
                'Classic MVC came from Smalltalk. Web frameworks use a request-response variant: the controller reads the request, the model persists, and the view (template) renders the response. Modern UI splits further — MVVM and unidirectional flows (Redux) address where classic MVC got tangled: views mutating the model directly and controllers ballooning.',
            ]},
        ],
        'practice': {
            'title': 'Trace the Request',
            'intro': 'A user clicks "add to cart" on a web shop.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Trace: click -> controller -> model -> view. What does each layer do?'},
                {'label': 'Task 2', 'text': 'Identify what breaks if the view writes the model directly.'},
                {'label': 'Task 3', 'text': 'Draw the same flow in a modern variant (MVVM or unidirectional).'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why the controller must not render and the model must not know the UI. Start with the data flow.'},
            {'label': 'Compare & Contrast', 'text': 'Compare MVC with MVVM and with unidirectional data flow. When does each fit a frontend?'},
            {'label': 'Boundary Testing', 'text': 'Two views observe one model and update each other indirectly. Design the notification policy that prevents loops.'},
        ],
        'takeaways': [
            'MVC separates data, presentation, and input',
            'The view observes the model; the controller mutates it',
            'Web MVC is a request-response variant',
            'Modern UIs refine MVC for testability',
        ],
        'further': [
            {'title': 'Model-View-Controller — MDN', 'url': 'https://developer.mozilla.org/en-US/docs/Glossary/MVC'},
            {'title': 'GUI Architectures — Martin Fowler', 'url': 'https://martinfowler.com/eaaDev/uiArchs.html'},
        ],
    },
    {
        'title': 'MVC in Production: Web Frameworks',
        'desc': 'Rails, Django, and the request lifecycle — plus where business logic lives.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Describe the request lifecycle',
            'Keep models fat, controllers thin',
            'Organize views and templates',
            'Test each layer',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'The Lifecycle', 'paras': [
                'In Rails and Django, a request flows: router -> controller action -> model operations -> view rendering. "Fat model, thin controller" means business rules live in the model (or service objects), and controllers only parse input and orchestrate. Views stay dumb: templates read, never mutate.',
            ], 'code': {'lang': 'ruby', 'body': '''
# Rails-style controller: thin, orchestration only
class OrdersController < ApplicationController
  def create
    order = Order.new(order_params)          # model owns rules
    if order.charge_and_save                # business logic in model
      redirect_to order, notice: "Placed"
    else
      render :new, status: :unprocessable_entity
    end
  end

  private
  def order_params
    params.require(:order).permit(:sku, :qty)   # input parsing only
  end
end
# The model validates, computes totals, and persists; the
# controller never knows business rules.'''}},
            {'heading': 'Where Logic Lives', 'paras': [
                'The classic failure: logic migrates into the controller (fat controllers) or into the view (logic in templates). Service objects and form objects pull orchestration out of controllers; presenters pull formatting out of views. The model layer stays the single home of domain rules.',
            ]},
        ],
        'practice': {
            'title': 'Refactor the Fat Controller',
            'intro': 'A checkout controller has 200 lines: tax, discount, and inventory rules inline.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Move tax and discount rules into the model/service layer.'},
                {'label': 'Task 2', 'text': 'Move formatting (currency, dates) into a presenter.'},
                {'label': 'Task 3', 'text': 'Rewrite the controller to orchestrate only and re-run the tests.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why fat controllers are the MVC failure mode and where the rules should live instead.'},
            {'label': 'Implementation Design', 'text': 'Design a service layer for a checkout: which steps are services, what does the controller keep?'},
            {'label': 'Boundary Testing', 'text': 'A template starts computing discounts. Design the presenter move and the test that guards it.'},
        ],
        'takeaways': [
            'The request lifecycle is router -> controller -> model -> view',
            'Fat models, thin controllers, dumb views',
            'Service objects keep controllers lean',
            'Presenters keep formatting out of templates',
        ],
        'further': [
            {'title': 'Ruby on Rails — Action Controller Overview', 'url': 'https://guides.rubyonrails.org/action_controller_overview.html'},
            {'title': 'Django — request/response cycle', 'url': 'https://docs.djangoproject.com/en/stable/intro/tutorial03/'},
        ],
    },
    {
        'title': 'Advanced MVC: Unidirectional Flow and State Management',
        'desc': 'From observer chaos to Redux and the modern frontend architecture.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Explain the observer tangle',
            'Design unidirectional data flow',
            'Manage global state',
            'Handle side effects',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Why Classic MVC Tangles', 'paras': [
                'As apps grow, views mutate models, models notify views, and views call other views — the observer graph becomes untraceable. Unidirectional data flow (Redux, Flux) fixes this: one store holds state, actions describe intent, reducers produce new state, and views re-render from the store. One way, always.',
            ], 'code': {'lang': 'typescript', 'body': '''
// Unidirectional flow: action -> reducer -> store -> view
type State = { count: number };
type Action = { type: 'INCREMENT' } | { type: 'SET'; value: number };

function reducer(state: State, action: Action): State {
    switch (action.type) {
        case 'INCREMENT': return { ...state, count: state.count + 1 };
        case 'SET': return { ...state, count: action.value };
    }
}
// The view dispatches actions and reads the store.
// It never mutates state directly; time travel = replay actions.'''}},
            {'heading': 'Side Effects and Testing', 'paras': [
                'Reducers must be pure, so side effects (API calls, timers) live in middleware or effects — outside the state transition. That purity is the payoff: every state change is a pure function of the previous state and an action, which makes the app testable and the history replayable.',
            ]},
        ],
        'practice': {
            'title': 'Convert to Unidirectional',
            'intro': 'A settings screen with 12 widgets mutates models directly and bugs are untraceable.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the state shape and the action set.'},
                {'label': 'Task 2', 'text': 'Convert widgets to dispatch actions and read the store.'},
                {'label': 'Task 3', 'text': 'Move the API call to an effect and test the reducer in isolation.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why unidirectional flow kills the observer tangle.'},
            {'label': 'Implementation Design', 'text': 'Design a global store for a shopping app: state shape, action set, and the effect layer for payments.'},
            {'label': 'Boundary Testing', 'text': 'A reducer is called twice (React StrictMode) and must be pure. Find the impure pattern in a sample reducer and fix it.'},
        ],
        'takeaways': [
            'Classic MVC tangles as views mutate models',
            'Unidirectional flow makes state transitions pure',
            'Side effects move to middleware',
            'Pure reducers enable time travel and tests',
        ],
        'further': [
            {'title': 'Redux — core concepts', 'url': 'https://redux.js.org/introduction/core-concepts'},
            {'title': 'The Evolution of Flux Frameworks — M. Fowler', 'url': 'https://martinfowler.com/articles/evolving-flux.html'},
        ],
    },
    {
        'title': 'MVC: Review & Mastery Quiz',
        'desc': 'Scenario questions on roles, lifecycle, and modern state.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate MVC concepts',
            'Keep layers clean',
            'Design state flow',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: The model holds? (A: data and rules / B: input parsing / C: rendering)',
                'Q2: The view re-renders when the model? (A: notifies / B: crashes / C: loads)',
                'Q3: "Fat model, thin controller" means logic lives? (A: in the model / B: in the view / C: in CSS)',
                'Q4: True or false: unidirectional flow makes state changes pure.',
                'Q5: Side effects in Redux live in? (A: middleware / B: reducers / C: components)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A checkout form with validation, totals, and a pay button. Design the MVC layers and where the rules live.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why separating data, presentation, and input is worth the files.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Separation of concerns is the point of MVC',
            'Unidirectional flow fixes the tangle at scale',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# MVCC
# ─────────────────────────────────────────────────────────────────────────────
_t('mvcc-pattern', [
    {
        'title': 'MVCC: Multi-Version Concurrency Control',
        'desc': 'Readers never block writers: each transaction sees a consistent snapshot of versions.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the MVCC model',
            'Describe version chains',
            'Understand snapshot isolation',
            'Know why reads do not block',
        ],
        'prereqs': ['principles/optimistic-locking', 'principles/pessimistic-locking'],
        'sections': [
            {'heading': 'The Model', 'paras': [
                'MVCC keeps multiple versions of each row instead of overwriting. A writer creates a new version; readers see the version that existed when their transaction started. Because readers never touch the new version, they never block writers — the core win over row locks.',
            ], 'code': {'lang': 'sql', 'body': '''
-- MVCC in Postgres: every row carries xmin/xmax version markers
-- Tx 1 (begins first): reads the row at its snapshot
BEGIN;
SELECT balance FROM accounts WHERE id = 1;   -- sees v0 (100)

-- Concurrent Tx 2 updates the row:
BEGIN;
UPDATE accounts SET balance = 90 WHERE id = 1;  -- creates v1
COMMIT;

-- Tx 1 reads again: still sees v0 (100) — its snapshot
SELECT balance FROM accounts WHERE id = 1;   -- 100, not 90
COMMIT;
-- No locks were held by Tx 2's write: readers never blocked.'''}},
            {'heading': 'Snapshots', 'paras': [
                'Each transaction takes a snapshot — the set of committed versions visible to it — at its start (or statement). Versions a transaction itself created are visible to it; versions from uncommitted or later transactions are not. Old versions stay until no snapshot references them, which is where vacuuming comes in.',
            ]},
        ],
        'practice': {
            'title': 'Trace the Versions',
            'intro': 'A bank balance is updated by three overlapping transactions.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Trace the version chain as each transaction commits.'},
                {'label': 'Task 2', 'text': 'Show what each concurrent snapshot sees.'},
                {'label': 'Task 3', 'text': 'Identify the anomaly (write skew) that snapshot isolation still allows.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why keeping versions removes the reader-writer conflict. Start with a long read.'},
            {'label': 'Compare & Contrast', 'text': 'Compare MVCC with pessimistic locking and with optimistic rechecking. When does each fit?'},
            {'label': 'Boundary Testing', 'text': 'A long transaction keeps old versions alive and storage grows. Design the vacuum/sweep policy that reclaims them safely.'},
        ],
        'takeaways': [
            'MVCC keeps versions so readers never block',
            'Each transaction reads a consistent snapshot',
            'Old versions live until no snapshot needs them',
            'Snapshot isolation still has write-skew anomalies',
        ],
        'further': [
            {'title': 'PostgreSQL — MVCC', 'url': 'https://www.postgresql.org/docs/current/mvcc.html'},
            {'title': 'MVCC — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Multiversion_concurrency_control'},
        ],
    },
    {
        'title': 'MVCC in Production: Postgres and Isolation Levels',
        'desc': 'Read committed vs repeatable read, visibility rules, and vacuum.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Compare isolation levels',
            'Explain visibility rules',
            'Tune vacuum',
            'Handle write skew',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Isolation Levels', 'paras': [
                'Read committed takes a fresh snapshot per statement; repeatable read (snapshot isolation in Postgres) takes one per transaction. Read committed is the default — each statement sees the latest committed data. Repeatable read guarantees the whole transaction sees one consistent snapshot, but both still allow write skew and (with certain engines) phantom anomalies.',
            ], 'code': {'lang': 'sql', 'body': '''
-- Isolation levels in PostgreSQL
BEGIN ISOLATION LEVEL READ COMMITTED;    -- snapshot per statement
SELECT balance FROM accounts WHERE id = 1;  -- sees latest committed
-- another tx commits an update; THIS statement sees it
SELECT balance FROM accounts WHERE id = 1;  -- new snapshot, new value
COMMIT;

BEGIN ISOLATION LEVEL REPEATABLE READ;   -- one snapshot for the tx
SELECT balance FROM accounts WHERE id = 1;
-- concurrent update commits; this statement STILL sees the old value
SELECT balance FROM accounts WHERE id = 1;
COMMIT;
-- Write skew: two txs each read old values and both write — neither
-- sees the other until commit. MVCC prevents lost updates only if
-- the write rechecks (SELECT ... FOR UPDATE).'''}},
            {'heading': 'Vacuum and Bloat', 'paras': [
                'Old versions accumulate as dead tuples; vacuum removes them and reclaims space. Autovacuum tunes itself, but pathological workloads (massive updates, long transactions) need manual attention. Index bloat follows table bloat: a table that is 50% dead tuples makes every scan 2x cost.',
            ]},
        ],
        'practice': {
            'title': 'Tune the Vacuum',
            'intro': 'A table updated 1M rows/hour shows 60% bloat and slow scans.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Measure bloat with pg_stat_user_tables and estimate dead tuples.'},
                {'label': 'Task 2', 'text': 'Set autovacuum thresholds and a manual vacuum schedule for the peak.'},
                {'label': 'Task 3', 'text': 'Verify scan cost recovery after the vacuum run.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me the difference between a per-statement snapshot and a per-transaction snapshot. Ask me to show the observable difference.'},
            {'label': 'Implementation Design', 'text': 'Design a balance-transfer flow safe under repeatable read: where do you add FOR UPDATE and why?'},
            {'label': 'Boundary Testing', 'text': 'A report transaction runs for an hour and blocks vacuum. Design the statement-level isolation or snapshot freeze that bounds the bloat.'},
        ],
        'takeaways': [
            'Isolation level = snapshot scope',
            'Read committed vs repeatable read differ per statement',
            'Dead tuples need vacuum to reclaim space',
            'Write skew needs explicit locking, not MVCC',
        ],
        'further': [
            {'title': 'PostgreSQL — Transaction Isolation', 'url': 'https://www.postgresql.org/docs/current/transaction-iso.html'},
            {'title': 'Routine Database Maintenance — vacuum', 'url': 'https://www.postgresql.org/docs/current/routine-vacuuming.html'},
        ],
    },
    {
        'title': 'Advanced MVCC: Distributed Snapshot Isolation',
        'desc': 'MVCC across shards, and how Spanner-style systems manage snapshots.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Explain distributed snapshot isolation',
            'Describe commit ordering',
            'Design cross-shard consistent reads',
            'Compare MVCC engines',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Distributed Snapshots', 'paras': [
                'In a sharded database, a snapshot spans shards: the read must see a consistent set of versions across all of them. True distributed snapshot isolation needs synchronized commit timestamps (Spanner uses TrueTime) or a global commit protocol that orders transactions and hands out timestamps from a coordinator.',
            ], 'code': {'lang': 'text', 'body': '''
Distributed MVCC approaches:
  CockroachDB: hybrid logical clocks (HLC) order commits; a
    transaction's timestamp defines its snapshot across shards.
  Spanner: TrueTime (GPS + atomic clocks) gives a global commit
    timestamp with bounded uncertainty; reads at a timestamp see
    a consistent snapshot across the whole database.
  YugaByte/others: central timestamp authority for ordering.
The invariant every approach provides: if tx A commits before B
starts, B's snapshot must include A — no matter which shards
each touched. Clock sync is the entire problem.'''}},
            {'heading': 'Reads Across Shards', 'paras': [
                'A cross-shard read either takes a consistent snapshot (paying for global ordering) or reads at a possibly inconsistent point in time. Materialized aggregates and causal consistency (read-your-writes across shards) are the practical middle grounds most apps actually need.',
            ]},
        ],
        'practice': {
            'title': 'Design the Snapshot',
            'intro': 'A 16-shard ledger needs a cross-shard balance report that never double-counts in-flight transfers.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the HLC ordering and the per-shard snapshot.'},
                {'label': 'Task 2', 'text': 'Design the read protocol that assembles a consistent view.'},
                {'label': 'Task 3', 'text': 'Compare the TrueTime vs coordinator approaches for a global financial table.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why cross-shard snapshots need globally ordered timestamps.'},
            {'label': 'Implementation Design', 'text': 'Design causal read-your-writes across shards without full distributed snapshot isolation. What is the routing guarantee?'},
            {'label': 'Boundary Testing', 'text': 'Two shards commit at clock-skewed times and a report sees a half-committed transfer. Design the guard (timestamp bounds) that prevents it.'},
        ],
        'takeaways': [
            'Distributed snapshots need globally ordered timestamps',
            'HLCs and TrueTime are the two main answers',
            'Causal consistency is the practical middle ground',
            'Clock skew is the enemy of cross-shard reads',
        ],
        'further': [
            {'title': 'Spanner — TrueTime', 'url': 'https://research.google/pubs/spanner-google-s-globally-distributed-database/'},
            {'title': 'CockroachDB — Serializable Transactions', 'url': 'https://www.cockroachlabs.com/docs/stable/serializable.html'},
        ],
    },
    {
        'title': 'MVCC: Review & Mastery Quiz',
        'desc': 'Scenario questions on snapshots, isolation, and distribution.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate MVCC concepts',
            'Choose isolation levels',
            'Design distributed snapshots',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: MVCC readers see? (A: a consistent snapshot / B: the latest write / C: random rows)',
                'Q2: Readers and writers? (A: never block each other / B: always block / C: share locks)',
                'Q3: Read committed takes a snapshot? (A: per statement / B: per transaction / C: never)',
                'Q4: True or false: snapshot isolation prevents write skew.',
                'Q5: Old versions are reclaimed by? (A: vacuum / B: the optimizer / C: the cache)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'An analytics read runs an hour while writes stream in. Design the isolation and the vacuum policy that keeps both healthy.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why versioning beats locking for read-heavy workloads.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: false; Q5: A',
            'Versions make readers and writers coexist',
            'Isolation level and vacuum are the operational dials',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# MVVM
# ─────────────────────────────────────────────────────────────────────────────
_t('mvvm', [
    {
        'title': 'MVVM: Model, View, ViewModel',
        'desc': 'Binding the view to a view model that prepares the model for display.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the MVVM roles',
            'Describe data binding',
            'Contrast with MVC',
            'Build a simple view model',
        ],
        'prereqs': ['patterns/mvc', 'patterns/observer'],
        'sections': [
            {'heading': 'The Roles', 'paras': [
                'The model holds data and rules; the view renders; the view model exposes the model in a form the view can bind to — computed properties, formatted values, commands. The view binds to the view model declaratively, so the view has almost no code-behind logic and the view model has no UI references.',
            ], 'code': {'lang': 'typescript', 'body': '''
// MVVM: the view model is a presentation-ready projection
class BalanceViewModel {
    balance = 0;                       // observable
    get formatted(): string {          // presentation logic here
        return `$${this.balance.toFixed(2)}`;
    }
    get isOverdrawn(): boolean {       // derived state
        return this.balance < 0;
    }
    deposit(amount: number) {
        this.balance += amount;        // calls through to the model
    }
}
// The view binds: <span text={vm.formatted} class={vm.isOverdrawn} />
// No imperative DOM updates, no view logic in the view model.'''}},
            {'heading': 'Binding', 'paras': [
                'Data binding observes view model properties and updates the view automatically — one-way (view model to view) or two-way (input elements write back). The framework (WPF, Vue, SwiftUI, Jetpack Compose) wires the bindings; the developer only declares them. The cost: debugging binding chains requires understanding the framework\'s reactivity.',
            ]},
        ],
        'practice': {
            'title': 'Build the Form View Model',
            'intro': 'A login form: email, password, validation state, and a submit command.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the view model properties and derived validity.'},
                {'label': 'Task 2', 'text': 'Bind the fields and the button enablement.'},
                {'label': 'Task 3', 'text': 'Move the validation logic out of the view and into the view model.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why the view model prepares data for display rather than holding it directly.'},
            {'label': 'Compare & Contrast', 'text': 'Compare MVVM with MVC: where does each put presentation logic, and which is easier to test?'},
            {'label': 'Boundary Testing', 'text': 'A computed property depends on two observables that update together. Design the consistency that prevents a flash of invalid state.'},
        ],
        'takeaways': [
            'MVVM separates model, presentation-ready state, and view',
            'The view model holds formatting and derived state',
            'Binding wires the view declaratively',
            'The view model is UI-free and testable',
        ],
        'further': [
            {'title': 'Model-View-ViewModel — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel'},
            {'title': 'The MVVM Pattern — Microsoft', 'url': 'https://learn.microsoft.com/en-us/dotnet/architecture/maui/mvvm'},
        ],
    },
    {
        'title': 'MVVM in Production: SwiftUI, Compose, and WPF',
        'desc': 'Reactive bindings in modern frameworks and the view model lifecycle.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Use state-driven bindings',
            'Manage view model lifecycle',
            'Handle async updates',
            'Test view models',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Modern Reactive Frameworks', 'paras': [
                'SwiftUI and Jetpack Compose are MVVM-flavored: the view model exposes observable state, and the framework recomputes the view from it. SwiftUI drives views from @State and @Observable; Compose from state holders. The reactive core makes the view model the single source of truth for the screen.',
            ], 'code': {'lang': 'swift', 'body': '''
// SwiftUI: the view model is an ObservableObject
@MainActor
final class CheckoutViewModel: ObservableObject {
    @Published var items: [Item] = []
    @Published var isProcessing = false

    var total: Decimal { items.reduce(0) { $0 + $1.price } }
    var canCheckout: Bool { !items.isEmpty && !isProcessing }

    func checkout() {
        isProcessing = true
        Task {                                  // async update
            await api.charge(items)
            isProcessing = false
        }
    }
}
// The view reads the view model; SwiftUI re-renders on @Published.''',
                    }},
            {'heading': 'Lifecycle and Async', 'paras': [
                'The view model lives with its view: created on navigation, cancelled on dispose. Async updates must be bound to the lifecycle — a view model completing an API call after its view is gone must not touch the view. Cancellation tokens and structured concurrency handle this; leaks are the classic bug.',
            ]},
        ],
        'practice': {
            'title': 'Design the Screen State',
            'intro': 'A product detail screen: loading, loaded, error, and refresh states.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the state enum and the view model properties.'},
                {'label': 'Task 2', 'text': 'Bind each state to the view and handle async refresh.'},
                {'label': 'Task 3', 'text': 'Add cancellation on dispose and test a slow API leaves no dangling update.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why the view model must outlive or cancel its async work, and how cancellation fixes it.'},
            {'label': 'Implementation Design', 'text': 'Design a search screen view model with debounce and request cancellation. How do stale responses get dropped?'},
            {'label': 'Boundary Testing', 'text': 'A view model property updates 60x/s and the view recomputes eagerly. Design the throttling or diffing that keeps the UI smooth.'},
        ],
        'takeaways': [
            'Reactive frameworks recompute views from view model state',
            'The view model is the screen\'s single source of truth',
            'Async work must be cancelled with the lifecycle',
            'View models are unit-testable without a UI',
        ],
        'further': [
            {'title': 'SwiftUI — managing model data', 'url': 'https://developer.apple.com/documentation/swiftui/managing-model-data-in-your-app'},
            {'title': 'Compose — state holders', 'url': 'https://developer.android.com/jetpack/compose/state'},
        ],
    },
    {
        'title': 'Advanced MVVM: Dependency Injection and Navigation',
        'desc': 'Scoping view models, injecting dependencies, and navigating between screens.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Scope view models to screens',
            'Inject dependencies cleanly',
            'Design navigation state',
            'Test with fakes',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Scoping and Injection', 'paras': [
                'View models need dependencies (API clients, repositories, analytics) — injected, never constructed internally, so tests can fake them. Scoping decides lifetime: a screen-scoped view model dies with the screen; a shared one survives. A DI container or a factory function wires both without global singletons.',
            ], 'code': {'lang': 'kotlin', 'body': '''
// Compose: view model scoped to the screen, dependencies injected
class ProductViewModel(
    private val repo: ProductRepository,   // injected fake-able
    private val analytics: Analytics
) : ViewModel() {
    val uiState = MutableStateFlow<ProductUiState>(Loading)

    fun load(id: String) {
        viewModelScope.launch {
            uiState.value = repo.fetch(id).fold(
                onSuccess = { ProductUiState.Loaded(it) },
                onFailure = { ProductUiState.Error(it.message) }
            )
        }
    }
}
// navigation-scoped factory:
val vm: ProductViewModel =
    viewModel(factory = ProductViewModel.Factory(repo, analytics))'''}},
            {'heading': 'Navigation State', 'paras': [
                'Navigation is a graph: destinations, arguments, and back-stack state. Frameworks let each destination bind its own view model; the navigator owns the stack. Deep links and process death restore both the back stack and each screen\'s state — which is why view models save and restore state (SavedStateHandle).',
            ]},
        ],
        'practice': {
            'title': 'Wire the Screens',
            'intro': 'A three-screen checkout with shared cart state and per-screen forms.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Scope the view models: shared cart, per-screen forms.'},
                {'label': 'Task 2', 'text': 'Inject the repositories through a factory and test with fakes.'},
                {'label': 'Task 3', 'text': 'Design navigation with saved state for process death.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why injection beats internal construction for testability.'},
            {'label': 'Implementation Design', 'text': 'Design a multi-module app: where do view models get their dependencies, and how does navigation cross module boundaries?'},
            {'label': 'Boundary Testing', 'text': 'Process death loses the in-memory view model. Design the saved-state restore that brings the screen back intact.'},
        ],
        'takeaways': [
            'Inject dependencies; construct in factories',
            'Scope view models to their screens',
            'Navigation owns the back stack and restore',
            'Fakes make view model tests fast and focused',
        ],
        'further': [
            {'title': 'Jetpack — ViewModel overview', 'url': 'https://developer.android.com/topic/libraries/architecture/viewmodel'},
            {'title': 'Navigation — Compose', 'url': 'https://developer.android.com/jetpack/compose/navigation'},
        ],
    },
    {
        'title': 'MVVM: Review & Mastery Quiz',
        'desc': 'Scenario questions on roles, binding, and lifecycle.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate MVVM concepts',
            'Scope and inject view models',
            'Handle async safely',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: The view model prepares? (A: data for display / B: the database / C: the network)',
                'Q2: Binding wires? (A: the view to the view model / B: models together / C: the router)',
                'Q3: Async updates must be? (A: lifecycle-cancelled / B: global / C: synchronous)',
                'Q4: True or false: view models are unit-testable without a UI.',
                'Q5: Dependencies should be? (A: injected / B: constructed inline / C: global)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A live sports scoreboard: scores stream in, views update live. Design the view model, binding, and lifecycle.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why a UI-free view model is the testability win.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Presentation-ready state, bound declaratively',
            'Lifecycle and injection make it production-safe',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# OBSERVER
# ─────────────────────────────────────────────────────────────────────────────
_t('observer', [
    {
        'title': 'Observer: Notify Without Knowing Who',
        'desc': 'Subjects announce changes; observers react — one-to-many, decoupled.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the observer intent',
            'Decouple subject from observers',
            'Implement subscription',
            'Handle unsubscribe',
        ],
        'prereqs': ['principles/separation-of-concerns', 'patterns/mediator'],
        'sections': [
            {'heading': 'The Model', 'paras': [
                'A subject keeps a list of observers and notifies them when its state changes. Observers register via a subscribe call; the subject knows only the notification interface — not the concrete observer types. Adding a new observer never touches the subject.',
            ], 'code': {'lang': 'python', 'body': '''
# Observer: the subject knows nothing about concrete observers
class NewsPublisher:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, observer):
        self._subscribers.append(observer)

    def unsubscribe(self, observer):
        self._subscribers.remove(observer)

    def publish(self, headline):
        for obs in list(self._subscribers):   # copy: safe to mutate
            obs.update(headline)

class EmailSubscriber:
    def update(self, headline):
        print(f'email: {headline}')

class SmsSubscriber:
    def update(self, headline):
        print(f'sms: {headline}')

pub = NewsPublisher()
pub.subscribe(EmailSubscriber())
pub.subscribe(SmsSubscriber())
pub.publish("V2 released")    # both notified, publisher knows neither'''}},
            {'heading': 'The Trade-Offs', 'paras': [
                'Observers are decoupled but the notification order is implicit, and a slow observer blocks the rest if notification is synchronous. Update storms — one change rippling through many observers — are the classic failure, which is why modern systems batch or throttle. Errors in one observer must not break the others.',
            ]},
        ],
        'practice': {
            'title': 'Build the Notification Fan',
            'intro': 'A user profile change must update the profile view, the activity log, and the search index.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the subject event and the observer interface.'},
                {'label': 'Task 2', 'text': 'Register the three observers and handle unsubscribe.'},
                {'label': 'Task 3', 'text': 'Design the error isolation: one failing observer must not block the others.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why the subject knowing only an interface is the whole point. Start with adding a new observer.'},
            {'label': 'Compare & Contrast', 'text': 'Compare observer with publish-subscribe (broker) and with mediator. Where does each decouple?'},
            {'label': 'Boundary Testing', 'text': 'An observer triggers a change in the subject mid-notification. Design the re-entrancy guard that prevents infinite loops.'},
        ],
        'takeaways': [
            'Observer decouples notification from reaction',
            'The subject depends only on an interface',
            'Notification order and sync cost are implicit',
            'Error isolation protects the fan-out',
        ],
        'further': [
            {'title': 'Observer — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/observer'},
            {'title': 'Observer Pattern — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Observer_pattern'},
        ],
    },
    {
        'title': 'Observer in Production: Events and Reactive Streams',
        'desc': 'DOM events, reactive streams, and distributed event buses as observers.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Use DOM and UI events',
            'Design reactive streams',
            'Apply backpressure',
            'Bridge to distributed events',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'From Callbacks to Streams', 'paras': [
                'UI frameworks are observer engines: every click, scroll, and keystroke is a subject notifying listeners. Reactive streams (RxJS, Reactive Streams) formalize the observer into push-based pipelines with operators — map, filter, debounce — and add backpressure so a slow observer signals the producer to slow down.',
            ], 'code': {'lang': 'typescript', 'body': '''
// RxJS: observer pipelines with backpressure semantics
import { fromEvent } from 'rxjs';
import { debounceTime, map, distinctUntilChanged } from 'rxjs/operators';

const input = document.querySelector('#search')!;
fromEvent(input, 'input')            // subject: every keystroke
  .pipe(
    debounceTime(300),               // throttle bursty events
    map((e: any) => e.target.value),
    distinctUntilChanged()           // skip repeats
  )
  .subscribe(q => search(q));        // observer reacts
// The pipeline is lazy; backpressure via debounce/drain policies.'''}},
            {'heading': 'Distributed Observers', 'paras': [
                'Cross-service, the observer becomes publish-subscribe with a broker: services subscribe to topics, producers publish, and the broker decouples them across machines. Durability is the new concern — a broker buffers for offline observers — and the ordering guarantees differ from in-process observers.',
            ]},
        ],
        'practice': {
            'title': 'Design the Reactive Form',
            'intro': 'A search box fires 20 keystrokes/s; each triggers an API call that must be debounced and deduped.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Build the pipeline: debounce, map, distinct, switch to latest.'},
                {'label': 'Task 2', 'text': 'Add cancellation: a stale response must not overwrite a newer one.'},
                {'label': 'Task 3', 'text': 'Add the distributed variant: publish the query events to a topic for analytics.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why reactive streams add backpressure to the observer model. Ask me what a slow subscriber does without it.'},
            {'label': 'Implementation Design', 'text': 'Design a real-time dashboard: sensor streams, windows, and the UI subscription. Where does backpressure live?'},
            {'label': 'Boundary Testing', 'text': 'A subscriber throws on one event and the stream dies. Design the error handler that keeps the stream alive.'},
        ],
        'takeaways': [
            'UI frameworks are observer engines',
            'Reactive streams add operators and backpressure',
            'Distributed observers need a durable broker',
            'Error handling must not kill the stream',
        ],
        'further': [
            {'title': 'RxJS — docs', 'url': 'https://rxjs.dev/guide/overview'},
            {'title': 'Reactive Streams — the spec', 'url': 'https://www.reactive-streams.org/'},
        ],
    },
    {
        'title': 'Advanced Observer: Event Sourcing as Observer',
        'desc': 'Events as the source of truth, projections as observers.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Explain event sourcing',
            'Build projections as observers',
            'Replay events',
            'Handle schema evolution',
        ],
        'prereqs': ['patterns/event-sourcing', 'patterns/cqrs'],
        'sections': [
            {'heading': 'Events as Truth', 'paras': [
                'Event sourcing stores facts — every state change as an event — instead of current state. Observers (projections) subscribe to the event stream and maintain read models: a report view, a search index, an email trigger. The same stream feeds every observer, and any projection can be rebuilt by replaying events.',
            ], 'code': {'lang': 'python', 'body': '''
# Event sourcing: events are the source of truth
# Aggregate: apply(Event) -> state
class Account:
    def __init__(self):
        self.balance = 0
    def apply(self, event):
        if event.type == 'DEPOSITED': self.balance += event.amount
        if event.type == 'WITHDRAWN': self.balance -= event.amount

# Projection (observer): maintains a read model from the stream
class BalanceProjection:
    def __init__(self):
        self.accounts = {}
    def on(self, event):
        a = self.accounts.setdefault(event.account_id, Account())
        a.apply(event)
# Rebuild = replay the event log from the start.
# Every observer consumes the same immutable stream.'''}},
            {'heading': 'Rebuilds and Evolution', 'paras': [
                'A projection is rebuildable: drop and replay. That is the power — a buggy projection fixes itself by replaying. Schema evolution is the cost: old events must stay readable, so events are versioned and upgrades translate old shapes. Event stores are append-only; immutable history is the contract.',
            ]},
        ],
        'practice': {
            'title': 'Build the Projection',
            'intro': 'An order system publishes OrderPlaced, PaymentReceived, OrderShipped; three projections must stay in sync.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define the event stream and the aggregate applies.'},
                {'label': 'Task 2', 'text': 'Build the three projections as observers.'},
                {'label': 'Task 3', 'text': 'Simulate a projection bug, drop it, and rebuild from the log.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why replaying events can rebuild any projection.'},
            {'label': 'Implementation Design', 'text': 'Design the event schema for a cart: add, remove, checkout. How does a projection compute the current cart, and how is a v2 event handled?'},
            {'label': 'Boundary Testing', 'text': 'A projection lags behind the stream and events age out. Design the snapshot + replay strategy for large histories.'},
        ],
        'takeaways': [
            'Event sourcing stores facts; projections observe them',
            'Rebuild any projection by replaying the log',
            'Events must stay readable across schema changes',
            'The event store is append-only truth',
        ],
        'further': [
            {'title': 'Event Sourcing — Martin Fowler', 'url': 'https://martinfowler.com/eaaDev/EventSourcing.html'},
            {'title': 'Eventuate — event sourcing platform', 'url': 'https://eventuate.io/'},
        ],
    },
    {
        'title': 'Observer: Review & Mastery Quiz',
        'desc': 'Scenario questions on decoupling, streams, and sourcing.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate observer concepts',
            'Design streams',
            'Model events',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: An observer pattern is? (A: one-to-many / B: one-to-one / C: many-to-one)',
                'Q2: The subject knows observers by? (A: interface / B: concrete type / C: memory address)',
                'Q3: Backpressure lets a slow observer? (A: slow the producer / B: skip events / C: restart)',
                'Q4: True or false: event sourcing stores state changes as facts.',
                'Q5: A projection is rebuilt by? (A: replaying events / B: restarting / C: patching)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A notification system must email, push, and log every order event. Design the observer set and the error isolation.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why knowing an interface beats knowing an implementation.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Decoupled notification is the superpower',
            'Streams and event sourcing scale the pattern',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# PAXOS
# ─────────────────────────────────────────────────────────────────────────────
_t('paxos', [
    {
        'title': 'Paxos: Consensus with a Majority',
        'desc': 'The foundational consensus protocol: a majority of acceptors agree on one value.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the consensus problem',
            'Describe proposers, acceptors, learners',
            'Trace a two-phase round',
            'Know the majority guarantee',
        ],
        'prereqs': ['principles/quorum', 'patterns/raft'],
        'sections': [
            {'heading': 'The Problem', 'paras': [
                'Consensus: several nodes must agree on one value even with failures and message loss. Paxos solves it with three roles: proposers suggest values, acceptors vote in phases, learners observe the outcome. The key invariant — once a value is chosen, every future round chooses the same value — comes from the majority intersection: any two majorities share a node.',
            ], 'code': {'lang': 'text', 'body': '''
Paxos two phases (prepare/accept):
  Prepare phase:
    1. proposer -> acceptors: prepare(n)   (n = new higher ballot)
    2. acceptors reply: promise to ignore ballots < n,
       and return any value they already accepted
    3. proposer picks the value from the highest returned ballot,
       or its own value if none
  Accept phase:
    4. proposer -> acceptors: accept(n, v)
    5. acceptors accept if they have promised >= n; a majority
       acceptance means v is CHOSEN
  Learn phase:
    6. chosen value is learned by learners and all nodes
Why it works: a future proposer with a higher ballot must
intersect the previous majority in prepare, learn v, and propose
v again. Majorities always intersect -> one chosen value.'''}},
            {'heading': 'Roles and Safety', 'paras': [
                'Safety (only one value chosen) holds under any failure pattern; liveness (progress) needs a distinguished proposer (leader) to avoid livelock — competing proposers can starve each other by raising ballots forever. Multi-Paxos runs repeated instances over a log with a stable leader.',
            ]},
        ],
        'practice': {
            'title': 'Trace the Round',
            'intro': 'Three acceptors; two propose different values concurrently.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Trace: prepare(1, X) then prepare(2, Y) — which promises win?'},
                {'label': 'Task 2', 'text': 'Show why the higher ballot must adopt the earlier accepted value.'},
                {'label': 'Task 3', 'text': 'Design the leader election that prevents ballot livelock.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why any two majorities intersect. Start with 3 nodes and 2-of-3 quorums.'},
            {'label': 'Compare & Contrast', 'text': 'Compare Paxos with Raft. Raft reorders roles and phases for understandability — where are the practical differences?'},
            {'label': 'Boundary Testing', 'text': 'An acceptor fails after prepare but before accept. Show why the round still completes and the value stays safe.'},
        ],
        'takeaways': [
            'Paxos: proposers, acceptors, learners',
            'Majority intersection guarantees one chosen value',
            'Safety holds under any failure; liveness needs a leader',
            'Multi-Paxos logs repeated instances',
        ],
        'further': [
            {'title': 'The Part-Time Parliament (original Paxos paper)', 'url': 'https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf'},
            {'title': 'Paxos Made Simple — Lamport', 'url': 'https://lamport.azurewebsites.net/pubs/paxos-simple.pdf'},
        ],
    },
    {
        'title': 'Paxos in Production: Chubby and ZooKeeper',
        'desc': 'How real systems use Paxos for locks, config, and coordination.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Describe Chubby\'s use of Paxos',
            'Use ZooKeeper coordination primitives',
            'Understand linearizability',
            'Handle leader failures',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Chubby', 'paras': [
                'Google\'s Chubby wraps Paxos in a lock service: a Paxos-replicated log backs a file-system-like namespace used for leader election and configuration. Clients lease locks; the Paxos state machine guarantees one lock owner. The pattern — consensus behind a familiar API — is what ZooKeeper and etcd replicate.',
            ], 'code': {'lang': 'java', 'body': '''
// ZooKeeper: ephemeral znode = lease-based lock via consensus
String path = "/locks/db-writer";
try {
    // create ephemeral: auto-deleted if this session dies
    zk.create(path, data, ZooDefs.Ids.OPEN_ACL_UNSAFE,
              CreateMode.EPHEMERAL);
    // We hold the lock — ZooKeeper consensus ensures only one
    // ephemeral node exists at this path.
} catch (KeeperException.NodeExistsException e) {
    // Someone else holds the lock; watch it for deletion
}
// Leader election = same pattern; the session is the lease,
// and the consensus log guarantees ordering.'''}},
            {'heading': 'Linearizability', 'paras': [
                'The replicated log makes every operation appear instantaneous and total-ordered — linearizable. That is the coordination guarantee: reads and writes to the consensus service act as if on one machine. Application leaders use this to fence (epoch the lock) and to publish config atomically.',
            ]},
        ],
        'practice': {
            'title': 'Build the Coordination Layer',
            'intro': 'Three app instances need a single leader, a shared config, and fencing.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the leader election with ephemeral nodes and fencing tokens.'},
                {'label': 'Task 2', 'text': 'Publish the config atomically as a versioned znode.'},
                {'label': 'Task 3', 'text': 'Design the failure path: leader death, lease expiry, and re-election.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why coordination services wrap consensus in familiar primitives. Ask me what a fencing token is for.'},
            {'label': 'Implementation Design', 'text': 'Design a distributed cron: one leader schedules, workers execute. How does the lease and fencing work?'},
            {'label': 'Boundary Testing', 'text': 'A partitioned leader still thinks it holds the lock. Design the fencing that makes its writes rejected.'},
        ],
        'takeaways': [
            'Coordination services wrap Paxos in familiar APIs',
            'Ephemeral nodes + leases = distributed locks',
            'The log gives linearizable ordering',
            'Fencing rejects stale leaders',
        ],
        'further': [
            {'title': 'The Chubby Lock Service — Google', 'url': 'https://static.googleusercontent.com/media/research.google.com/en//archive/chubby-osdi06.pdf'},
            {'title': 'ZooKeeper — programmer guide', 'url': 'https://zookeeper.apache.org/doc/current/zookeeperProgrammers.html'},
        ],
    },
    {
        'title': 'Advanced Paxos: Multi-Paxos and Fast Paxos',
        'desc': 'Log replication, leader optimization, and the family of Paxos variants.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Explain Multi-Paxos',
            'Describe Fast Paxos',
            'Compare variants',
            'Reason about liveness',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Multi-Paxos', 'paras': [
                'Consensus on one value is not enough — a replicated state machine needs consensus on every log entry. Multi-Paxos elects a stable leader once, then the leader drives accept rounds for each log slot without re-running prepare every time. The leader change is the expensive moment; steady state is one message round.',
            ], 'code': {'lang': 'text', 'body': '''
Multi-Paxos: consensus on a log of values
  Phase 1 (once per leader term): the leader runs prepare with
    a new ballot and learns the highest chosen value per slot.
  Phase 2 (steady state): for each log slot i, the leader sends
    accept(i, v); a majority ack -> slot i is decided.
  Clients read by following the decided log; the state machine
  applies entries in order.
Leader failure -> a new leader runs phase 1 for all slots and
  continues. The cost of consensus is thus one round trip per
  log entry in the common case.
Variants: Fast Paxos (clients propose directly to acceptors,
  one phase in the happy path), Mencius (no leader, per-slot
  rotation), EPaxos (dependent commands ordered causally).'''}},
            {'heading': 'Choosing a Variant', 'paras': [
                'Raft made Paxos understandable and is the default choice today; ZooKeeper uses Zab; etcd and CockroachDB use Raft. Mencius and EPaxos optimize for wide-area deployments where a single leader is a bottleneck. The trade space: leader simplicity vs message rounds vs fault tolerance vs WAN latency.',
            ]},
        ],
        'practice': {
            'title': 'Compare the Family',
            'intro': 'A WAN-replicated database spanning 5 regions needs consistent replication.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Trace Multi-Paxos steady state: message rounds per log entry.'},
                {'label': 'Task 2', 'text': 'Compare Raft and EPaxos for the WAN topology.'},
                {'label': 'Task 3', 'text': 'Design the leader-change protocol and its cost.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why Multi-Paxos pays the prepare cost once per leader term.'},
            {'label': 'Implementation Design', 'text': 'Design a replicated state machine over Multi-Paxos: what is in the log, how do reads work, and how is a new leader caught up?'},
            {'label': 'Boundary Testing', 'text': 'A leader partitions and a new one is elected with an older log. Design the quorum rule that prevents stale overwrites.'},
        ],
        'takeaways': [
            'Multi-Paxos = consensus on every log slot',
            'Stable leaders make steady state one round',
            'Raft, Zab, Mencius, EPaxos trade the same guarantees',
            'Leader changes are the expensive moments',
        ],
        'further': [
            {'title': 'Paxos Made Moderately Complex', 'url': 'https://paxos.systems/'},
            {'title': 'EPaxos — the paper', 'url': 'https://dl.acm.org/doi/10.1145/2517349.2522732'},
        ],
    },
    {
        'title': 'Paxos: Review & Mastery Quiz',
        'desc': 'Scenario questions on phases, quorums, and variants.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate Paxos concepts',
            'Design coordination',
            'Choose variants',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Paxos roles are? (A: proposers, acceptors, learners / B: leaders, workers, clients / C: masters, slaves, caches)',
                'Q2: Safety comes from? (A: majority intersection / B: majority votes / C: backups)',
                'Q3: Livelock is prevented by? (A: a distinguished proposer / B: more votes / C: caching)',
                'Q4: True or false: Multi-Paxos runs consensus per log entry.',
                'Q5: ZooKeeper locks use? (A: ephemeral znodes / B: file locks / C: DNS)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A 5-node config service must elect a leader and fence the old one. Design the consensus layer and the fencing token.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why two majorities must always intersect.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Consensus is majority agreement, proven once',
            'Every modern variant is a Paxos descendant',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# PROTOTYPE
# ─────────────────────────────────────────────────────────────────────────────
_t('prototype', [
    {
        'title': 'Prototype: Clone Instead of Construct',
        'desc': 'Creating new objects by copying a prototype rather than calling constructors.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the prototype intent',
            'Clone complex objects cheaply',
            'Avoid constructor coupling',
            'Implement a clone interface',
        ],
        'prereqs': ['patterns/factory', 'patterns/flyweight'],
        'sections': [
            {'heading': 'The Problem', 'paras': [
                'Some objects are expensive or complex to construct: deep configuration, loaded assets, recursive structures. The prototype pattern creates new instances by cloning a configured prototype — the clone is a starting point that already has the hard parts done.',
            ], 'code': {'lang': 'java', 'body': '''
// Prototype: clone() gives a ready-configured copy
class Document implements Cloneable {
    private String title;
    private List<Section> sections;   // deep structure
    private Theme theme;              // expensive to load

    Document cloneDocument() {
        try {
            Document d = (Document) super.clone();   // shallow
            d.sections = new ArrayList<>(this.sections);  // deep copy
            d.theme = this.theme;     // share the immutable theme
            return d;
        } catch (CloneNotSupportedException e) { throw new RuntimeException(e); }
    }
}
// Prototype registry: ready-made templates
Document invoiceTemplate = buildInvoiceTemplate();
Document invoice = invoiceTemplate.cloneDocument();  // no rebuild
invoice.setTitle("Invoice #1042");'''}},
            {'heading': 'Shallow vs Deep', 'paras': [
                'Shallow clone shares references; deep clone copies the graph. Which is right depends on what the clone may mutate: sharing immutable parts is cheap and safe; sharing mutable parts corrupts the prototype. The clone method must document its depth.',
            ]},
        ],
        'practice': {
            'title': 'Clone the Scene',
            'intro': 'A game loads a heavy scene (meshes, textures, AI graphs) and needs many variants.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define clone() with the right depth for each field.'},
                {'label': 'Task 2', 'text': 'Build the prototype registry of scene templates.'},
                {'label': 'Task 3', 'text': 'Trace what happens when two clones mutate a shared field.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about when shallow sharing is safe and when it corrupts. Start with mutable fields.'},
            {'label': 'Compare & Contrast', 'text': 'Compare prototype with factory and with copy constructors. When does cloning beat constructing?'},
            {'label': 'Boundary Testing', 'text': 'A clone mutates the prototype\'s shared theme. Design the immutable-share or copy-on-write rule.'},
        ],
        'takeaways': [
            'Prototype clones configured objects instead of rebuilding',
            'Deep vs shallow copy is a contract',
            'Sharing immutable parts is safe; mutable is not',
            'Registries make templates reusable',
        ],
        'further': [
            {'title': 'Prototype — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/prototype'},
            {'title': 'Prototype Pattern — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Prototype_pattern'},
        ],
    },
    {
        'title': 'Prototype in Production: Serialization and Deep Copy',
        'desc': 'Serialization-based cloning, copy-on-write, and prototype registries in the wild.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Clone via serialization',
            'Apply copy-on-write',
            'Handle cycles and identity',
            'Use registries safely',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Serialization Cloning', 'paras': [
                'Deep cloning through serialization — object -> bytes -> object — works for arbitrary graphs but is slow and has identity surprises: the clone is a new identity even for values that were shared. Copy-on-write defers the copy: clones share until one mutates, which is how persistent structures and COW filesystems amortize cloning.',
            ], 'code': {'lang': 'python', 'body': '''
# Deep clone via serialization (pickle) — simple but slow
import copy

original = load_expensive_graph()
deep = copy.deepcopy(original)      # full graph copy

# Copy-on-write alternative: share until mutation
class CowNode:
    def __init__(self, shared_ref=None):
        self._ref = shared_ref      # shared until written
        self._owned = None
    def mutate(self, value):
        if self._owned is None:
            self._owned = deepcopy(self._ref)   # copy now, once
        self._owned.value = value
# Many readers share; the first writer pays the copy.
# This is how COW snapshots and persistent structures work.'''}},
            {'heading': 'Cycles and Identity', 'paras': [
                'Cyclic graphs break naive recursive copy — you need a visited map or a serialization format that handles references. Identity matters when the clone must preserve shared sub-objects (the graph stays a graph) vs duplicating them. Prototype registries must be careful: a mutated template clones wrong by default.',
            ]},
        ],
        'practice': {
            'title': 'Design the Clone Strategy',
            'intro': 'A configuration graph has shared nodes, cycles, and immutable leaves; it is cloned 1,000 times per deploy.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Clone with a visited map to preserve the graph shape.'},
                {'label': 'Task 2', 'text': 'Add copy-on-write for the hot path and measure the savings.'},
                {'label': 'Task 3', 'text': 'Guard the registry: freeze templates after registration.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why cycles break naive deep copy and how a visited map fixes it.'},
            {'label': 'Implementation Design', 'text': 'Design a COW document model: shared immutable history, copy on edit. How do versions stay cheap?'},
            {'label': 'Boundary Testing', 'text': 'A registered template is mutated after cloning begins. Design the freeze-and-version that makes clones deterministic.'},
        ],
        'takeaways': [
            'Serialization cloning is simple but slow',
            'Copy-on-write defers copy until mutation',
            'Cycles need visited maps; identity must be defined',
            'Registries must freeze or version templates',
        ],
        'further': [
            {'title': 'Copy-on-write — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Copy-on-write'},
            {'title': 'Python — copy module docs', 'url': 'https://docs.python.org/3/library/copy.html'},
        ],
    },
    {
        'title': 'Advanced Prototype: Structural Sharing and Versioned Clones',
        'desc': 'Persistent data structures, structural sharing, and branch/merge history.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Explain structural sharing',
            'Build persistent structures',
            'Version documents by clone',
            'Analyze clone complexity',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Structural Sharing', 'paras': [
                'A persistent (immutable) data structure clones by sharing: an update copies only the path from root to the changed node and shares the rest. Cloning a document becomes O(log n) or O(1) instead of O(n). The clone is a new version; the old version remains — which is version history for free.',
            ], 'code': {'lang': 'clojure', 'body': '''
; Clojure: persistent structures share structure across versions
(def v0 [1 2 3 4 5 6 7 8])
(def v1 (assoc v0 3 :changed))     ; O(log32 n) — shares v0's tail

; Both v0 and v1 exist simultaneously:
v0   ; => [1 2 3 4 5 6 7 8]
v1   ; => [1 2 3 :changed 5 6 7 8]

; A version stack is just a list of roots:
(def history (list v1 v0))         ; undo = pop, redo = push
; This is the prototype pattern's advanced form: cloning by
; sharing instead of copying. Git's object model is the same idea.'''}},
            {'heading': 'Versioned Clones', 'paras': [
                'With structural sharing, "clone then mutate" becomes "create a new version": each version is a prototype of the next, and history is the chain. Branch and merge operate on version graphs. The cost shifts to garbage collection of unreachable old versions.',
            ]},
        ],
        'practice': {
            'title': 'Design the Version Chain',
            'intro': 'A collaborative document needs per-edit versions with O(1) undo and cheap forks.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Implement the persistent structure and measure per-edit cost.'},
                {'label': 'Task 2', 'text': 'Design the version chain and the branch/merge operations.'},
                {'label': 'Task 3', 'text': 'Design GC for abandoned versions and the retention policy.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why an update touches only the root path in a persistent structure.'},
            {'label': 'Implementation Design', 'text': 'Design a Git-like config versioning: commit, branch, checkout. What are the clones and the shared history?'},
            {'label': 'Boundary Testing', 'text': 'A version chain grows unbounded. Design the snapshot + compact policy that bounds history without losing undo depth.'},
        ],
        'takeaways': [
            'Structural sharing makes clones O(log n)',
            'Versions are clones; history is the chain',
            'Old versions survive until GC',
            'Branch and merge are version-graph operations',
        ],
        'further': [
            {'title': 'Persistent data structures — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Persistent_data_structure'},
            {'title': 'Git — object model', 'url': 'https://git-scm.com/book/en/v2/Git-Internals-Git-Objects'},
        ],
    },
    {
        'title': 'Prototype: Review & Mastery Quiz',
        'desc': 'Scenario questions on cloning, copy depth, and versions.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate prototype concepts',
            'Choose copy depth',
            'Design versioned clones',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Prototype creates objects by? (A: cloning / B: constructing / C: injecting)',
                'Q2: Shallow copy? (A: shares references / B: copies everything / C: deletes)',
                'Q3: Cyclic graphs break naive copy without? (A: a visited map / B: a cache / C: a compiler)',
                'Q4: True or false: structural sharing makes clone O(log n).',
                'Q5: Copy-on-write defers the copy until? (A: mutation / B: read / C: garbage collection)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A config system clones a heavy graph 1000x per deploy. Design the clone strategy and the version chain.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why copying the whole object is not the only way to get a new one.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Clone with intent: depth, identity, and sharing',
            'Structural sharing turns cloning into versioning',
        ],
    },
])
