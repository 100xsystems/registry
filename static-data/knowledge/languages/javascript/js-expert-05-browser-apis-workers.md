---
title: "Browser APIs, Web Workers, and Performance"
description: "Service Workers, IndexedDB, WebSockets, Canvas, WebRTC, and advanced browser performance optimization."
type: lesson
order: 19
duration: "60 min"
difficulty: expert
level: Expert
learning_objectives:
  - "Register and implement Service Workers for offline support and caching"
  - "Use IndexedDB for client-side structured data storage"
  - "Implement WebSocket communication for real-time bidirectional data"
  - "Profile and optimize rendering performance with requestAnimationFrame and layers"
knowledge_refs:
  - languages/javascript/js-expert-05-browser-apis-workers
prerequisites:
  - "JS-05: DOM"
  - "JS-10: Async"
  - "JS-11: Event Loop"
references:
    - title: "The Modern JavaScript Tutorial"
      url: "https://javascript.info/"
      sections: "Network requests: Fetch, WebSocket | Storing data: IndexedDB | Service Workers | Animations: requestAnimationFrame"
      description: "Comprehensive coverage of advanced browser APIs"
    - title: "MDN Web Docs"
      url: "https://developer.mozilla.org/en-US/docs/Web/API"
      sections: "Service Worker API | IndexedDB API | WebSocket API | Canvas API | WebRTC API"
      description: "Complete reference for all browser APIs"
    - title: "Eloquent JavaScript (4th Edition)"
      url: "https://eloquentjavascript.net/"
      chapters: "Chapter 18: HTTP and Forms (browser networking) | Chapter 22 (Node.js: file I/O, networking)"
      description: "Practical browser and networking patterns"
---

# JS-19: Browser APIs, Web Workers, and Performance

## Introduction

Modern browsers expose powerful APIs beyond basic DOM manipulation. Service Workers
enable offline-first architectures. IndexedDB provides client-side databases.
WebSockets enable real-time communication. Understanding these APIs enables building
progressive, performant web applications.

## Subtopics

### 1. Service Workers

- **Lifecycle**: Register → Install → Activate → Fetch
- **Install**: Pre-cache critical resources
- **Activate**: Clean old caches, take control of clients
- **Fetch**: Intercept network requests, serve from cache or network
- **Update**: Byte-diff comparison triggers update flow
- **Cache strategies**: Cache-first, Network-first, Stale-while-revalidate, Cache-only, Network-only
- *Reference:* javascript.info — Service Workers | MDN — Service Worker API

### 2. IndexedDB

- Object-oriented database — stores structured data (any structured-cloneable value)
- Asynchronous API with transactions and indexes
- `idb` wrapper library recommended over raw IndexedDB API
- Common patterns: offline data sync, caching structured data, user preferences
- *Reference:* MDN — IndexedDB API | javascript.info — IndexedDB

### 3. WebSockets

- Full-duplex communication over a single TCP connection
- `new WebSocket("wss://server.com")` — connect
- Events: `open`, `message`, `error`, `close`
- Binary and text messages
- Auto-reconnection patterns: exponential backoff, heartbeat/ping-pong
- *Reference:* MDN — WebSocket API | javascript.info — WebSocket

### 4. Rendering Performance

- **Critical rendering path**: DOM → CSSOM → Render Tree → Layout → Paint → Composite
- **Reflow vs Repaint**: Reflow (layout) is more expensive than repaint (paint)
- **`requestAnimationFrame`**: Schedule visual updates before the next paint
- **CSS containment**: `contain: layout style paint` — isolate subtrees
- **`will-change`**: Hint browser about animating properties
- *Reference:* MDN — Rendering performance | google web.dev — Rendering performance
  | javascript.info — Animations, requestAnimationFrame

## Practice Questions

1. Design a cache strategy for a news website: which resources would you cache-first vs network-first?
2. How does IndexedDB differ from localStorage in terms of storage limits and data types?
3. What causes a reflow in the browser? How can you minimize it?
4. Write a WebSocket reconnection handler with exponential backoff.

## Key Takeaways

- Service Workers turn web apps into progressive, offline-capable applications
- IndexedDB scales well beyond localStorage's 5MB limit
- WebSockets enable real-time bidirectional communication
- Minimize layout reflows by batching DOM reads/writes
- `requestAnimationFrame` is the correct scheduling mechanism for visual updates
