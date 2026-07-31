---
title: "Publish-Subscribe: Decouple Producers from Consumers"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the pub-sub model"
  - "Describe topics and subscriptions"
  - "Decouple producers and consumers"
  - "Compare with observer"
prerequisites:
  - "patterns/observer"
  - "patterns/mediator"
knowledge_refs:
  - "patterns/publish-subscribe"
---

# Publish-Subscribe: Decouple Producers from Consumers

## The Model

Publishers emit messages to a named topic. The broker routes each message to every subscriber of that topic. Publishers never know subscribers; subscribers never know publishers; new parties join without touching the others. The broker mediates the decoupling.

```python
# Pub-sub: an in-process broker decouples sides
class Broker:
    def __init__(self):
        self.topics = {}

    def publish(self, topic, message):
        for sub in self.topics.get(topic, []):
            sub.on_message(message)

    def subscribe(self, topic, subscriber):
        self.topics.setdefault(topic, []).append(subscriber)

class EmailService:
    def on_message(self, msg):
        if msg.type == 'user_signed_up':
            send_welcome(msg.email)

broker = Broker()
broker.subscribe('user_events', EmailService())
broker.publish('user_events', Message('user_signed_up', email='a@b.com'))
# The email service never imports the publisher; the publisher
# never imports the email service.
```

## Pub-Sub vs Observer

Observer is in-process and direct: the subject holds observer references and notifies synchronously. Pub-sub adds a broker and a topic channel: the decoupling is stronger (no direct references at all) and it works across processes, at the cost of indirection, ordering, and delivery guarantees you must choose.

## Practice: Wire the Events

A signup flow publishes user_signed_up; email, analytics, and the CRM consume it.

**Task 1:** Define the topics and the message shape.

**Task 2:** Wire the three subscribers and prove neither side imports the other.

**Task 3:** Add a fourth consumer without touching the publisher or the other three.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about what the broker adds over direct observer references. Start with cross-process.

**Prompt 2 — Compare & Contrast:**
> Compare pub-sub with observer and with a plain queue. When is a topic (fan-out) the right shape?

**Prompt 3 — Boundary Testing:**
> A subscriber is slow and blocks the broker. Design the async delivery or the bounded queue that isolates it.

## Key Takeaways

- Pub-sub decouples via a broker and topics
- Publishers and subscribers never meet
- Fan-out is the defining shape
- Broker indirection adds delivery and ordering choices

## Further Reading

- [Publish–subscribe pattern — Wikipedia](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)
- [Microsoft — publisher-subscriber guidance](https://learn.microsoft.com/en-us/azure/architecture/patterns/publisher-subscriber)
