---
title: "Bridge in Production: Pluggable Rendering and Persistence"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design rendering bridges (view + platform)"
  - "Design persistence bridges (model + store)"
  - "Swap implementations at runtime"
  - "Keep both axes testable"
prerequisites:
  []
knowledge_refs:
  - "patterns/bridge"
---

# Bridge in Production: Pluggable Rendering and Persistence

## The Rendering Bridge

A charting library faces two axes: chart types (bar, line, pie) and rendering targets (SVG, Canvas, WebGL). Bridge gives one chart hierarchy holding a Renderer implementation — adding a chart type or a renderer never touches the other axis.

```typescript
// Bridge: Chart (abstraction) holds a Renderer (implementation)
interface Renderer {
    drawRect(x: number, y: number, w: number, h: number): void;
    drawLine(points: number[]): void;
}

abstract class Chart {
    constructor(protected renderer: Renderer) {}
    abstract render(): void;
}

class BarChart extends Chart {            // one axis: chart type
    render() {
        this.renderer.drawRect(0, 0, 10, 20);
        this.renderer.drawRect(12, 0, 10, 5);
    }
}
class SvgRenderer implements Renderer { ... }
class CanvasRenderer implements Renderer { ... }

// renderer = new CanvasRenderer()  -> swap at runtime, chart untouched
```

## The Persistence Bridge

Models vary by domain; stores vary by engine (SQL, Redis, S3). Bridge lets a domain repository hold a Store implementation — the same repository logic reads from Postgres or an in-memory store for tests, without an inheritance explosion.

## Practice: Bridge the Rendering Stack

A reporting app renders 5 report types to HTML, PDF, and JSON.

**Task 1:** Count naive classes (5 x 3) and design the bridge instead.

**Task 2:** Implement one report type on two renderers to prove the seam.

**Task 3:** Add a fourth renderer and show only one class is added.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why the bridge seam is "the abstraction holds the implementation" and how that differs from plain interfaces.

**Prompt 2 — Implementation Design:**
> Design a persistence bridge for a domain: repository abstraction + store implementations, with the wiring at the composition root.

**Prompt 3 — Boundary Testing:**
> A renderer only supports a subset of chart features. Design the capability query that keeps the bridge honest.

## Key Takeaways

- Chart/device-style pairs are textbook bridge territory
- Renderers and stores are implementation axes
- Runtime swapping is a free benefit of the seam
- Capability queries prevent dishonest implementations

## Further Reading

- [Bridge Pattern in UI Toolkits](https://refactoring.guru/design-patterns/bridge)
- [Repository + Bridge — DDD](https://martinfowler.com/eaaCatalog/repository.html)
