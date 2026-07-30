---
title: "Beginner Project: Interactive Web Application"
description: "Build a complete interactive web application using all beginner concepts — DOM manipulation, events, arrays, and localStorage."
type: lesson
order: 7
duration: "120 min"
difficulty: beginner
level: Beginner
learning_objectives:
  - "Plan and architect a small web application from scratch"
  - "Combine DOM manipulation, event handling, and data management"
  - "Use localStorage for persistent state across page reloads"
  - "Debug and refine the application using DevTools"
knowledge_refs:
  - languages/javascript/js-beginner-07-project
prerequisites:
  - "JS-01 through JS-06"
references:
    - title: "Eloquent JavaScript (4th Edition)"
      url: "https://eloquentjavascript.net/"
      chapters: "Chapters 14-18 (DOM, Events, HTTP, Forms)"
      description: "All the browser-side concepts needed for the project"
    - title: "The Modern JavaScript Tutorial"
      url: "https://javascript.info/"
      sections: "All Browser: Document, Events, Interfaces sections"
      description: "Reference for all DOM APIs used in the project"
    - title: "MDN Web Docs"
      url: "https://developer.mozilla.org/en-US/docs/Web/API"
      sections: "localStorage, Document, Event, fetch"
      description: "API reference for project implementation"
---

# JS-07: Beginner Project — Interactive Web Application

## Project: Build a Kanban Board

Build a fully interactive Kanban-style task board with columns (To Do, In Progress,
Done). Users can add tasks, move them between columns, edit descriptions, and
persist data with localStorage.

### Requirements

1. **Three columns**: To Do, In Progress, Done
2. **Add tasks**: Form with title, description, and priority
3. **Move tasks**: Click to advance or drag-and-drop (optional)
4. **Edit/Delete**: Each task has edit and delete buttons
5. **Persistence**: Save all tasks to localStorage, restore on page load
6. **Empty states**: Each column shows a friendly message when empty
7. **Responsive**: Works on mobile and desktop

### Architecture

```javascript
// State management
const state = {
  columns: {
    todo: { title: 'To Do', tasks: [] },
    progress: { title: 'In Progress', tasks: [] },
    done: { title: 'Done', tasks: [] },
  }
};

// Key functions
function addTask(columnId, task) { /* ... */ }
function moveTask(taskId, fromColumn, toColumn) { /* ... */ }
function deleteTask(columnId, taskId) { /* ... */ }
function render() { /* Clear + rebuild DOM from state */ }
function saveState() { /* localStorage.setItem */ }
function loadState() { /* localStorage.getItem */ }
```

### Reference Implementation Structure

- Use event delegation on the board container for click handlers
- Render tasks using `document.createElement` or `innerHTML` (with sanitization)
- Save state after every mutation; load on page initialization
- Use `data-*` attributes to store IDs on DOM elements

## Evaluation Criteria

- All CRUD operations work correctly
- State persists across page reloads
- Clean, readable code with comments
- Error handling for edge cases (empty input, duplicate IDs, corrupted localStorage)
- Bonus: Drag-and-drop between columns, task search/filter, due dates
