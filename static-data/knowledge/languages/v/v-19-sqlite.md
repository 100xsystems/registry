---
{
  "title": "Database Access",
  "description": "SQLite in V.",
  "type": "lesson",
  "order": 19,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Open databases",
    "Create tables",
    "Run queries",
    "Use prepared statements"
  ],
  "knowledge_refs": [
    "v/v-19-sqlite"
  ],
  "prerequisites": [
    "V-18: CLI Applications"
  ],
  "references": [
    {
      "title": "V Documentation",
      "url": "https://docs.vlang.io/",
      "description": "Official docs"
    },
    {
      "title": "V Manual",
      "url": "https://docs.vlang.io/introduction.html",
      "description": "Language manual"
    },
    {
      "title": "V Language GitHub",
      "url": "https://github.com/vlang/v",
      "description": "Source code"
    }
  ]
}
---

# V-19-SQLITE: Database Access

## Introduction

SQLite in V. By the end of this lesson you will be able to: Open databases; Create tables; Run queries; Use prepared statements.

## Key Concepts

### 1. Open databases

Target: Open databases. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```v
import sqlite

mut db := sqlite.connect("test.db") or { panic(err) }
```
### 2. Create tables

Target: Create tables. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```v
db.exec("create table if not exists users (id integer primary key, name text)") or { panic(err) }
```
### 3. Run queries

Target: Run queries. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```v
db.exec("insert into users (name) values (?)", "Ada") or { panic(err) }
```
### 4. Use prepared statements

Target: Use prepared statements. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```v
rows := db.exec("select name from users") or { panic(err) }
println(rows)
```

## Practice Questions

1. What is the key idea behind "Database Access"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Database Access with analogies and real-world examples"
1. "Show me common mistakes beginners make with Database Access"
1. "Provide advanced patterns and performance considerations for Database Access"

## Key Takeaways

- Master the core ideas of Database Access through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
