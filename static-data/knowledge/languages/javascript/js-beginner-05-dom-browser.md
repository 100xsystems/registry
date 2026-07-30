---
title: "The DOM and Browser APIs"
description: "Document Object Model, DOM manipulation, event handling, and essential browser APIs."
type: lesson
order: 5
duration: "75 min"
difficulty: beginner
level: Beginner
learning_objectives:
  - "Traverse and manipulate the DOM tree using selectors and methods"
  - "Handle browser events: click, submit, scroll, keydown, and delegation"
  - "Create and remove DOM elements dynamically"
  - "Use browser APIs: localStorage, fetch, navigator, console"
knowledge_refs:
  - languages/javascript/js-beginner-05-dom-browser
prerequisites:
  - "JS-01: Values, Types, and Variables"
  - "JS-04: Objects and Arrays"
references:
    - title: "Eloquent JavaScript (4th Edition)"
      url: "https://eloquentjavascript.net/"
      chapters: "Chapter 14: The Document Object Model | Chapter 15: Handling Events | Chapter 18: HTTP and Forms"
      description: "The classic introduction to browser-side JavaScript"
    - title: "The Modern JavaScript Tutorial"
      url: "https://javascript.info/"
      sections: "Browser: Document, Events, Interfaces — all sections (DOM, events, forms, documents, styles, size, coordinates)"
      description: "The most comprehensive browser JavaScript tutorial online"
    - title: "MDN Web Docs"
      url: "https://developer.mozilla.org/en-US/docs/Web/API"
      sections: "Document, Element, Event, Window, Node, DOM API Reference"
      description: "Complete reference for all browser APIs"
---

# JS-05: The DOM and Browser APIs

## Introduction

The Document Object Model (DOM) is JavaScript's interface to HTML documents.
It represents the page as a tree of nodes that you can query, traverse, and
modify. Combined with event handling, the DOM enables interactive web pages.

## Subtopics

### 1. The DOM Tree

- **Node types**: Document, Element, Text, Comment, DocumentFragment
- **Tree structure**: `document → html → head + body → divs, spans, etc.`
- **Properties**: `nodeType`, `nodeName`, `nodeValue`, `childNodes`, `parentElement`
- *Reference:* javascript.info — DOM tree | Eloquent JS Ch. 14 | MDN — Node

### 2. Selecting Elements

- **`document.getElementById(id)`** — fastest, returns single element
- **`document.querySelector(selector)` / `querySelectorAll(selector)`** — CSS selector syntax
- **`document.getElementsByClassName(name)`** — live HTMLCollection
- **`document.getElementsByTagName(tag)`** — live HTMLCollection
- **`elem.closest(selector)`** — find the nearest ancestor matching selector
- *Reference:* javascript.info — Searching DOM | MDN — Document.querySelector
- *Deep dive:* `querySelectorAll` returns a STATIC NodeList; `getElementsBy*` returns a LIVE
  HTMLCollection. Live collections automatically update when the DOM changes.

### 3. Manipulating the DOM

- **Creating**: `document.createElement(tag)`, `document.createTextNode(text)`
- **Inserting**: `parent.appendChild(child)`, `parent.insertBefore(child, ref)`,
  `parent.prepend(child)`, `parent.append(child)`, `elem.insertAdjacentHTML(pos, html)`
- **Removing**: `parent.removeChild(child)`, `elem.remove()`
- **Replacing**: `parent.replaceChild(newChild, oldChild)`
- **HTML content**: `elem.innerHTML = ""` (XSS risk!), `elem.textContent = ""` (safe)
- *Reference:* javascript.info — Modifying document | Eloquent JS Ch. 14

### 4. Event Handling

- **Adding listeners**: `elem.addEventListener("click", handler)`
- **Removing listeners**: `elem.removeEventListener("click", handler)` — must pass same function reference
- **Event object**: `event.type`, `event.target`, `event.currentTarget`, `event.preventDefault()`, `event.stopPropagation()`
- **Event phases**: capturing → target → bubbling
- **Event delegation**: Listen on a parent, use `event.target` to determine which child was clicked
- *Reference:* javascript.info — Events | Eloquent JS Ch. 15 | MDN — Event
- *Deep dive:* Event delegation is critical for performance. Instead of adding 100 listeners
  to 100 list items, add ONE listener to the parent `<ul>`. Check `event.target` to find
  which child was clicked. Also enables handling elements added dynamically.

### 5. Essential Browser APIs

- **`localStorage` / `sessionStorage`**: Persist key-value data across sessions
- **`fetch()`**: Modern HTTP request API — returns a Promise
- **`navigator`**: Browser info, geolocation, user agent, clipboard, media devices
- **`console`**: `.log()`, `.warn()`, `.error()`, `.table()`, `.time()`/`.timeEnd()`, `.group()`
- **`setTimeout()` / `setInterval()`**: Delayed and repeated execution
- *Reference:* javascript.info — Browser environment, Fetch, Storing data | Eloquent JS Ch. 18

## Practice Questions

1. What's the difference between `innerHTML` and `textContent`? Which is safer?
2. Explain event delegation. Why would you use it instead of attaching listeners to each element?
3. How do you stop an event from bubbling up the DOM tree?
4. Write code that saves a form input to localStorage and retrieves it on page load.
5. What does `document.querySelectorAll(".item")` return? Is it live or static?

## LLM Prompts

1. **Socratic Tutor**: "I'm building a todo app. Should I attach a click handler to every todo item's delete button, or should I use event delegation on the list? Walk me through both approaches."
2. **Debugging Coach**: "My `addEventListener` isn't working. Here's my code: `const btn = document.querySelector('.btn'); btn.addEventListener('click', handleClick());`. What's wrong?"
3. **Project Architect**: "Design a simple image gallery component that uses event delegation and allows keyboard navigation with arrow keys."

## Key Takeaways

- The DOM is a tree of Node objects — query, traverse, and modify with standard methods
- Prefer `querySelector`/`querySelectorAll` for flexibility and consistency
- Event delegation is more efficient than per-element listeners
- `innerHTML` re-parses HTML (XSS risk); `textContent` is safe for text
- `localStorage` is synchronous and blocking — use it sparingly for small data

## Further Reading

- Eloquent JS, Chapters 14-15: DOM and Events
- javascript.info: The entire "Browser: Document, Events, Interfaces" section
- MDN: DOM API Reference
