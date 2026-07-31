---
title: "Advanced Graceful Degradation: Adaptive Quality"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Design adaptive quality tiers"
  - "Use client hints for progressive enhancement"
  - "Apply degradation at the edge (CDN)"
  - "Measure the cost of each degraded state"
prerequisites:
  []
knowledge_refs:
  - "principles/graceful-degradation"
---

# Advanced Graceful Degradation: Adaptive Quality

## Adaptive Quality

Instead of a fixed fallback, adapt quality to load: lower image resolution, thinner payloads, fewer widgets — driven by current capacity. Video streaming (adaptive bitrate) is the canonical example; the same principle applies to APIs returning lighter response shapes under pressure.

```typescript
// Adaptive quality: lighter responses as load rises
function responseShape(load: number) {
    if (load < 0.6) return 'full';     // all fields, images, widgets
    if (load < 0.85) return 'core';    // essential fields only
    return 'minimal';                  // id + cached text, no media
}

// Client advertises capability; server adapts
app.get('/feed', (req, res) => {
    const shape = responseShape(loadAvg());
    res.json(trim(feed, shape));
});
```

## Edge and Client Degradation

CDNs and service workers let degradation happen without the origin: serve cached HTML at the edge when the origin is slow, or let the client render from a cached bundle offline. Progressive enhancement is client-side degradation: the page works without JS, then upgrades.

## Practice: Design Adaptive Response Shapes

A video platform serves 4K streams; under load, users still need playback.

**Task 1:** Design the quality ladder (4K → 1080p → 720p → audio-only) and the load thresholds for stepping down.

**Task 2:** Design the API response-shape ladder for the recommendations endpoint.

**Task 3:** Measure the savings: how much bandwidth and CPU each step saves, and what users lose.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why adaptive quality needs hysteresis (don't oscillate between tiers).

**Prompt 2 — Implementation Design:**
> Design an API that returns full, core, or minimal shapes with an explicit header so clients render accordingly. What contract does the client need?

**Prompt 3 — Boundary Testing:**
> A load spike triggers minimal shape, and users complain they lost the media they paid for. Design the policy that protects premium features from degradation.

## Key Takeaways

- Adapt quality to capacity instead of failing
- Response shapes and bitrates are degradation levers
- Edge caching and SWR make degradation invisible
- Hysteresis prevents tier oscillation

## Further Reading

- [Adaptive Bitrate Streaming — Wikipedia](https://en.wikipedia.org/wiki/Adaptive_bitrate_streaming)
- [Service Workers — MDN](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)
