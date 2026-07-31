---
title: "MVVM in Production: SwiftUI, Compose, and WPF"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Use state-driven bindings"
  - "Manage view model lifecycle"
  - "Handle async updates"
  - "Test view models"
prerequisites:
  []
knowledge_refs:
  - "patterns/mvvm"
---

# MVVM in Production: SwiftUI, Compose, and WPF

## Modern Reactive Frameworks

SwiftUI and Jetpack Compose are MVVM-flavored: the view model exposes observable state, and the framework recomputes the view from it. SwiftUI drives views from @State and @Observable; Compose from state holders. The reactive core makes the view model the single source of truth for the screen.

```swift
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
// The view reads the view model; SwiftUI re-renders on @Published.
```

## Lifecycle and Async

The view model lives with its view: created on navigation, cancelled on dispose. Async updates must be bound to the lifecycle — a view model completing an API call after its view is gone must not touch the view. Cancellation tokens and structured concurrency handle this; leaks are the classic bug.

## Practice: Design the Screen State

A product detail screen: loading, loaded, error, and refresh states.

**Task 1:** Define the state enum and the view model properties.

**Task 2:** Bind each state to the view and handle async refresh.

**Task 3:** Add cancellation on dispose and test a slow API leaves no dangling update.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why the view model must outlive or cancel its async work, and how cancellation fixes it.

**Prompt 2 — Implementation Design:**
> Design a search screen view model with debounce and request cancellation. How do stale responses get dropped?

**Prompt 3 — Boundary Testing:**
> A view model property updates 60x/s and the view recomputes eagerly. Design the throttling or diffing that keeps the UI smooth.

## Key Takeaways

- Reactive frameworks recompute views from view model state
- The view model is the screen's single source of truth
- Async work must be cancelled with the lifecycle
- View models are unit-testable without a UI

## Further Reading

- [SwiftUI — managing model data](https://developer.apple.com/documentation/swiftui/managing-model-data-in-your-app)
- [Compose — state holders](https://developer.android.com/jetpack/compose/state)
