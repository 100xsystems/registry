---
title: "Advanced Project: Real-Time Data Dashboard"
description: "Build a real-time data dashboard using async/await, fetch, event-driven architecture, and data visualization."
type: lesson
order: 14
duration: "120 min"
difficulty: intermediate
level: Advanced
learning_objectives:
  - "Architect a multi-source data-fetching application"
  - "Implement real-time updates with polling and WebSocket patterns"
  - "Use async generators for streaming data processing"
  - "Build a reactive UI that responds to state changes"
knowledge_refs:
  - languages/javascript/js-advanced-07-project
prerequisites:
  - "JS-10 through JS-13"
references:
    - title: "Eloquent JavaScript (4th Edition)"
      url: "https://eloquentjavascript.net/"
      chapters: "Chapters 11, 18, 20"
      description: "Async programming, HTTP, Node.js — all relevant"
    - title: "The Modern JavaScript Tutorial"
      url: "https://javascript.info/"
      sections: "Promises, async/await | Fetch API | WebSocket | Data attributes and custom events"
      description: "Reference for all APIs used in project"
---

# JS-14: Advanced Project — Real-Time Data Dashboard

## Project: Stock Market Dashboard

Build a real-time dashboard that fetches stock/crypto prices from a public API,
displays them in a table with live updates, and charts price history using Canvas.

### Requirements

1. **Real-time data**: Poll a public API (e.g., CoinGecko, Alpha Vantage) every 30 seconds
2. **Multiple assets**: Display 10+ assets in a sortable, filterable table
3. **Price charts**: Simple line chart drawn on Canvas for each selected asset
4. **Real-time updates**: New data points animate in without full page reload
5. **Persistent state**: User preferences (selected assets, chart timeframe) saved to localStorage
6. **Error handling**: Graceful fallback when API is rate-limited or offline
7. **Responsive**: Works on mobile and desktop

### Architecture

```javascript
// Data layer
const dataStore = {
  assets: {},
  subscribers: new Map(),
  
  async fetchPrices() { /* ... */ },
  subscribe(component, callback) { /* ... */ },
  notify() { /* ... */ },
};

// Async generator for polling
async function* pollPrice(url, interval) {
  while (true) {
    const data = await fetch(url).then(r => r.json());
    yield data;
    await new Promise(r => setTimeout(r, interval));
  }
}

// Chart component
class PriceChart {
  constructor(canvas) { /* ... */ }
  update(prices) { /* ... */ }
  draw() { /* Canvas 2D API */ }
}
```

## Key Concepts Applied

- Event-driven architecture with pub/sub pattern
- Async generators for polling data streams
- Canvas 2D API for custom chart rendering
- localStorage for state persistence
- Event delegation for table sorting/filtering
