---
title: "Flyweight: Share the Repetitive State"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the flyweight intent"
  - "Split intrinsic from extrinsic state"
  - "Share state through a factory"
  - "Measure the memory win"
prerequisites:
  - "patterns/factory"
  - "principles/caching"
knowledge_refs:
  - "patterns/flyweight"
---

# Flyweight: Share the Repetitive State

## The Problem: Object Explosion

A text editor stores a glyph object per character: 10MB of text means millions of FontGlyph objects, each carrying the same font data. The flyweight pattern separates intrinsic state (shared, immutable — the glyph shape) from extrinsic state (per-use, mutable — the position), and shares the intrinsic part.

```java
// Intrinsic: the glyph shape — shared across all positions
final class Glyph {
    final char c; final Font font;
    Glyph(char c, Font f) { this.c = c; this.font = f; }
    void draw(int x, int y) { font.render(c, x, y); }  // extrinsic passed in
}

class GlyphFactory {
    private final Map<String, Glyph> cache = new HashMap<>();
    Glyph get(char c, Font f) {
        return cache.computeIfAbsent(c + ":" + f.id(), k -> new Glyph(c, f));
    }
}
// One Glyph per (char, font) pair — not one per character on screen
```

## Intrinsic vs Extrinsic

Intrinsic state never changes and is stored once. Extrinsic state changes per use and is passed in or held by the client. Getting the split wrong — sharing something mutable — silently corrupts every shared user.

## Practice: Share the Trees

A forest renderer creates 100,000 tree objects with 3 species; each species has a heavy mesh and texture.

**Task 1:** Split species data (intrinsic) from position/scale (extrinsic).

**Task 2:** Build the species factory and render 100,000 trees with 3 shared species.

**Task 3:** Measure memory before and after; report the ratio.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about the intrinsic/extrinsic split. Start with why intrinsic state must be immutable.

**Prompt 2 — Compare & Contrast:**
> Compare flyweight with the object pool. One shares identity, the other shares resources — when does each apply?

**Prompt 3 — Boundary Testing:**
> A caller mutates what was supposed to be intrinsic state. Design the defensive copy or freeze that prevents corruption.

## Key Takeaways

- Flyweight shares immutable intrinsic state
- Extrinsic state is passed per use, never stored
- A factory guarantees one shared instance per key
- The split must keep shared state immutable

## Further Reading

- [Flyweight — Refactoring Guru](https://refactoring.guru/design-patterns/flyweight)
- [Flyweight Pattern — Wikipedia](https://en.wikipedia.org/wiki/Flyweight_pattern)
