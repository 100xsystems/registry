---
title: "Advanced MVVM: Dependency Injection and Navigation"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Scope view models to screens"
  - "Inject dependencies cleanly"
  - "Design navigation state"
  - "Test with fakes"
prerequisites:
  []
knowledge_refs:
  - "patterns/mvvm"
---

# Advanced MVVM: Dependency Injection and Navigation

## Scoping and Injection

View models need dependencies (API clients, repositories, analytics) — injected, never constructed internally, so tests can fake them. Scoping decides lifetime: a screen-scoped view model dies with the screen; a shared one survives. A DI container or a factory function wires both without global singletons.

```kotlin
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
    viewModel(factory = ProductViewModel.Factory(repo, analytics))
```

## Navigation State

Navigation is a graph: destinations, arguments, and back-stack state. Frameworks let each destination bind its own view model; the navigator owns the stack. Deep links and process death restore both the back stack and each screen's state — which is why view models save and restore state (SavedStateHandle).

## Practice: Wire the Screens

A three-screen checkout with shared cart state and per-screen forms.

**Task 1:** Scope the view models: shared cart, per-screen forms.

**Task 2:** Inject the repositories through a factory and test with fakes.

**Task 3:** Design navigation with saved state for process death.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why injection beats internal construction for testability.

**Prompt 2 — Implementation Design:**
> Design a multi-module app: where do view models get their dependencies, and how does navigation cross module boundaries?

**Prompt 3 — Boundary Testing:**
> Process death loses the in-memory view model. Design the saved-state restore that brings the screen back intact.

## Key Takeaways

- Inject dependencies; construct in factories
- Scope view models to their screens
- Navigation owns the back stack and restore
- Fakes make view model tests fast and focused

## Further Reading

- [Jetpack — ViewModel overview](https://developer.android.com/topic/libraries/architecture/viewmodel)
- [Navigation — Compose](https://developer.android.com/jetpack/compose/navigation)
