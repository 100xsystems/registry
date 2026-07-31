---
title: "MVVM: Model, View, ViewModel"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the MVVM roles"
  - "Describe data binding"
  - "Contrast with MVC"
  - "Build a simple view model"
prerequisites:
  - "patterns/mvc"
  - "patterns/observer"
knowledge_refs:
  - "patterns/mvvm"
---

# MVVM: Model, View, ViewModel

## The Roles

The model holds data and rules; the view renders; the view model exposes the model in a form the view can bind to — computed properties, formatted values, commands. The view binds to the view model declaratively, so the view has almost no code-behind logic and the view model has no UI references.

```typescript
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
// No imperative DOM updates, no view logic in the view model.
```

## Binding

Data binding observes view model properties and updates the view automatically — one-way (view model to view) or two-way (input elements write back). The framework (WPF, Vue, SwiftUI, Jetpack Compose) wires the bindings; the developer only declares them. The cost: debugging binding chains requires understanding the framework's reactivity.

## Practice: Build the Form View Model

A login form: email, password, validation state, and a submit command.

**Task 1:** Define the view model properties and derived validity.

**Task 2:** Bind the fields and the button enablement.

**Task 3:** Move the validation logic out of the view and into the view model.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why the view model prepares data for display rather than holding it directly.

**Prompt 2 — Compare & Contrast:**
> Compare MVVM with MVC: where does each put presentation logic, and which is easier to test?

**Prompt 3 — Boundary Testing:**
> A computed property depends on two observables that update together. Design the consistency that prevents a flash of invalid state.

## Key Takeaways

- MVVM separates model, presentation-ready state, and view
- The view model holds formatting and derived state
- Binding wires the view declaratively
- The view model is UI-free and testable

## Further Reading

- [Model-View-ViewModel — Wikipedia](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel)
- [The MVVM Pattern — Microsoft](https://learn.microsoft.com/en-us/dotnet/architecture/maui/mvvm)
