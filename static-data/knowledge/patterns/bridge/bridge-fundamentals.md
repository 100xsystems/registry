---
title: "Bridge: Decouple Abstraction from Implementation"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the bridge intent"
  - "Identify two-dimensional hierarchies"
  - "Split abstraction and implementation"
  - "Compare with inheritance explosion"
prerequisites:
  - "patterns/abstract-factory"
  - "patterns/strategy"
knowledge_refs:
  - "patterns/bridge"
---

# Bridge: Decouple Abstraction from Implementation

## The Problem: Exploding Hierarchy

A remote-control abstraction with two device implementations (TV, Radio) and two input methods (basic, advanced) naively produces 4 classes: BasicTvRemote, AdvancedTvRemote, BasicRadioRemote, AdvancedRadioRemote. Add a third device and it grows to 6 — an inheritance explosion.

Bridge separates the two axes: the Remote hierarchy (abstraction) holds a reference to the Device hierarchy (implementation). Each axis varies independently.

```java
// Bridge: abstraction (Remote) holds an implementation (Device)
interface Device { void powerOn(); void setVolume(int v); int getVolume(); }

abstract class Remote {
    protected final Device device;
    Remote(Device d) { this.device = d; }
    abstract void togglePower();
    abstract void volumeUp();
}

class BasicRemote extends Remote {      // one axis: input method
    BasicRemote(Device d) { super(d); }
    public void togglePower() { device.powerOn(); }
    public void volumeUp() { device.setVolume(device.getVolume() + 1); }
}
// AdvancedRemote extends Remote, same Device reference.

// Adding a third device = new Device class. Adding a third input =
// new Remote class. No explosion: 2 axes x N each.
```

## When to Bridge

Bridge pays off when you have two independent axes of variation that both grow. If only one dimension varies, an interface suffices; if the axes are coupled, bridge fights reality. The pattern is about finding the seam between abstraction and implementation.

## Practice: Find the Second Axis

A message sender supports email/SMS/push and plain/rich/encrypted formats.

**Task 1:** Count the classes in the naive cross-product.

**Task 2:** Design the bridge: Message abstraction holding a Channel implementation.

**Task 3:** Add one new channel and one new format; count the classes added under each design.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why two growing axes need bridge while one axis does not. Start with the class count.

**Prompt 2 — Compare & Contrast:**
> Compare bridge with strategy and adapter. How do they differ in intent and structure?

**Prompt 3 — Boundary Testing:**
> The two axes are not truly independent (certain formats only work on certain channels). Design the capability check that keeps the bridge honest.

## Key Takeaways

- Bridge separates two independent axes of variation
- It kills the inheritance explosion (cross-product classes)
- Abstraction holds the implementation, both vary freely
- Use it when axes grow independently

## Further Reading

- [Bridge — Refactoring Guru](https://refactoring.guru/design-patterns/bridge)
- [Bridge Pattern — Wikipedia](https://en.wikipedia.org/wiki/Bridge_pattern)
