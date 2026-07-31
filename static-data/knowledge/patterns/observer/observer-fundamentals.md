---
title: "Observer: Notify Without Knowing Who"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the observer intent"
  - "Decouple subject from observers"
  - "Implement subscription"
  - "Handle unsubscribe"
prerequisites:
  - "principles/separation-of-concerns"
  - "patterns/mediator"
knowledge_refs:
  - "patterns/observer"
---

# Observer: Notify Without Knowing Who

## The Model

A subject keeps a list of observers and notifies them when its state changes. Observers register via a subscribe call; the subject knows only the notification interface — not the concrete observer types. Adding a new observer never touches the subject.

```python
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
pub.publish("V2 released")    # both notified, publisher knows neither
```

## The Trade-Offs

Observers are decoupled but the notification order is implicit, and a slow observer blocks the rest if notification is synchronous. Update storms — one change rippling through many observers — are the classic failure, which is why modern systems batch or throttle. Errors in one observer must not break the others.

## Practice: Build the Notification Fan

A user profile change must update the profile view, the activity log, and the search index.

**Task 1:** Define the subject event and the observer interface.

**Task 2:** Register the three observers and handle unsubscribe.

**Task 3:** Design the error isolation: one failing observer must not block the others.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why the subject knowing only an interface is the whole point. Start with adding a new observer.

**Prompt 2 — Compare & Contrast:**
> Compare observer with publish-subscribe (broker) and with mediator. Where does each decouple?

**Prompt 3 — Boundary Testing:**
> An observer triggers a change in the subject mid-notification. Design the re-entrancy guard that prevents infinite loops.

## Key Takeaways

- Observer decouples notification from reaction
- The subject depends only on an interface
- Notification order and sync cost are implicit
- Error isolation protects the fan-out

## Further Reading

- [Observer — Refactoring Guru](https://refactoring.guru/design-patterns/observer)
- [Observer Pattern — Wikipedia](https://en.wikipedia.org/wiki/Observer_pattern)
