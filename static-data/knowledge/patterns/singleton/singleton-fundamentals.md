---
title: "Singleton: One Instance, One Access Point"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the singleton intent"
  - "Implement a singleton"
  - "Make it thread-safe"
  - "Recognize the drawbacks"
prerequisites:
  - "patterns/factory"
  - "principles/separation-of-concerns"
knowledge_refs:
  - "patterns/singleton"
---

# Singleton: One Instance, One Access Point

## The Intent

Some resources must be unique: a config, a connection pool, a logger. The singleton enforces one instance and gives a global access point. The classic implementation is a private constructor plus a static instance — lazy or eager.

```java
// Thread-safe lazy singleton: double-checked locking
class Config {
    private static volatile Config instance;

    private Config() {                 // private: no other constructors
        loadFromDisk();
    }

    static Config get() {
        Config local = instance;       // fast path, no lock
        if (local == null) {
            synchronized (Config.class) {
                local = instance;
                if (local == null) {
                    local = new Config();     // create once
                    instance = local;
                }
            }
        }
        return local;
    }
}
// Config.get() is THE single instance and access point.
```

## Why It Is Controversial

Singletons are global state in disguise: they hide dependencies, make testing harder (a fake needs to replace the global), and couple callers to the access point. The modern guidance: scope the instance to its lifetime (app scope via dependency injection) and inject it — the "one instance" property survives, the global access point does not.

## Practice: Scope the Instance

A logger is used by 200 classes; tests must capture output per test.

**Task 1:** Implement the thread-safe singleton and note the hidden coupling.

**Task 2:** Refactor to an injected logger scoped per app and per test.

**Task 3:** Compare: what breaks if two instances exist in each design?

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why a global access point makes testing harder. Start with the fake.

**Prompt 2 — Compare & Contrast:**
> Compare singleton with dependency injection scoping and with the registry pattern.

**Prompt 3 — Boundary Testing:**
> Two threads call get() for the first time. Design the initialization that cannot create two instances.

## Key Takeaways

- Singleton enforces one instance and one access point
- Thread safety needs careful initialization
- Global access is hidden coupling
- DI scoping keeps the single instance, drops the global

## Further Reading

- [Singleton — Refactoring Guru](https://refactoring.guru/design-patterns/singleton)
- [Singletons are pathological liars — Miško Hevery](https://misko.hevery.com/2008/08/17/singletons-are-pathological-liars/)
