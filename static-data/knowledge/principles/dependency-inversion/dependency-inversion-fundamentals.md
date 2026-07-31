---
title: "Dependency Inversion: Depend on Abstractions"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "State the dependency inversion principle"
  - "Explain how interfaces invert dependency direction"
  - "Refactor a concrete-coupling example"
  - "Distinguish inversion from dependency injection"
prerequisites:
  - "principles/single-responsibility"
  - "principles/interface-segregation"
knowledge_refs:
  - "principles/dependency-inversion"
---

# Dependency Inversion: Depend on Abstractions

## The Principle

Dependency Inversion (DIP): high-level modules should not depend on low-level modules; both should depend on abstractions. Abstractions should not depend on details; details should depend on abstractions.

When the notification service calls EmailSender directly, the high-level policy (what to send) is welded to the low-level detail (how to send). Introduce an interface, and the policy depends on the abstraction while both email and SMS implement it.

```java
// Before: high-level depends on low-level concrete class
class NotificationService {
    private EmailSender sender = new EmailSender();  // welded to detail
    void send(String msg) { sender.sendEmail(msg); }
}

// After: both depend on the abstraction
interface MessageSender { void send(String msg); }

class NotificationService {
    private final MessageSender sender;   // depends on abstraction
    NotificationService(MessageSender s) { this.sender = s; }
    void send(String msg) { sender.send(msg); }
}
class EmailSender implements MessageSender { public void send(String m) {} }
class SmsSender   implements MessageSender { public void send(String m) {} }
```

## Inversion vs Injection

Inversion is about the direction of dependency arrows. Injection (DI) is the delivery mechanism — passing the dependency in via constructor. You can invert without a framework, and you can inject without inverting. The principle is the point; the framework is optional.

## Practice: Invert the Reporting Stack

A ReportGenerator builds CSV rows and calls CsvWriter directly. Now you must also support JSON and PDF.

**Task 1:** Define the ReportWriter interface the generator should depend on.

**Task 2:** Implement CsvWriter, JsonWriter, PdfWriter behind it.

**Task 3:** Wire the choice at startup (constructor injection) and explain why the generator never changes again.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why depending on an interface is not the same as depending on a base class. Start with the direction of the arrow.

**Prompt 2 — Compare & Contrast:**
> Compare DIP with dependency injection frameworks (Spring, Guice). What does the framework solve, and what can you do without one?

**Prompt 3 — Boundary Testing:**
> An abstraction with only one implementation and no planned second one — is it over-engineering or correct DIP? Argue both sides.

## Key Takeaways

- High-level policy must not depend on low-level details
- Interfaces flip the dependency arrow
- Injection is delivery; inversion is direction
- One-implementation abstractions can still be justified by testability

## Further Reading

- [Dependency Inversion Principle — Clean Code Mentor](https://www.clean-code-mentor.com/dependency-inversion-principle)
- [SOLID — Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html)
