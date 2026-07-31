---
title: "MVC: Model, View, Controller"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the MVC roles"
  - "Trace a request through MVC"
  - "Understand separation of concerns"
  - "Know the MVC variants"
prerequisites:
  - "principles/separation-of-concerns"
  - "patterns/observer"
knowledge_refs:
  - "patterns/mvc"
---

# MVC: Model, View, Controller

## The Roles

The model holds data and business rules, the view renders the model, and the controller translates user input into model changes. The view observes the model and re-renders on change; the controller never renders and the model never touches the UI. Each layer can change without breaking the others.

```python
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
        print('display:', self.model._value)
```

## Variants

Classic MVC came from Smalltalk. Web frameworks use a request-response variant: the controller reads the request, the model persists, and the view (template) renders the response. Modern UI splits further — MVVM and unidirectional flows (Redux) address where classic MVC got tangled: views mutating the model directly and controllers ballooning.

## Practice: Trace the Request

A user clicks "add to cart" on a web shop.

**Task 1:** Trace: click -> controller -> model -> view. What does each layer do?

**Task 2:** Identify what breaks if the view writes the model directly.

**Task 3:** Draw the same flow in a modern variant (MVVM or unidirectional).

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why the controller must not render and the model must not know the UI. Start with the data flow.

**Prompt 2 — Compare & Contrast:**
> Compare MVC with MVVM and with unidirectional data flow. When does each fit a frontend?

**Prompt 3 — Boundary Testing:**
> Two views observe one model and update each other indirectly. Design the notification policy that prevents loops.

## Key Takeaways

- MVC separates data, presentation, and input
- The view observes the model; the controller mutates it
- Web MVC is a request-response variant
- Modern UIs refine MVC for testability

## Further Reading

- [Model-View-Controller — MDN](https://developer.mozilla.org/en-US/docs/Glossary/MVC)
- [GUI Architectures — Martin Fowler](https://martinfowler.com/eaaDev/uiArchs.html)
