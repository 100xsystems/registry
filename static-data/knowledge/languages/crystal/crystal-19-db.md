---
{
  "title": "Database Access",
  "description": "SQLite and Postgres with Crystal.",
  "type": "lesson",
  "order": 19,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Connect to databases",
    "Run queries",
    "Use prepared statements",
    "Map rows"
  ],
  "knowledge_refs": [
    "crystal/crystal-19-db"
  ],
  "prerequisites": [
    "Crystal-18: HTTP Clients and JSON"
  ],
  "references": [
    {
      "title": "Crystal Language Reference",
      "url": "https://crystal-lang.org/reference/",
      "description": "Official docs"
    },
    {
      "title": "Crystal for Rubyists",
      "url": "https://crystal-lang.org/reference/guides/faq.html",
      "description": "Migration guide"
    },
    {
      "title": "Crystal Book",
      "url": "https://crystal-lang.org/reference/",
      "description": "Official reference book"
    },
    {
      "title": "Crystal Forum",
      "url": "https://forum.crystal-lang.org/",
      "description": "Community"
    }
  ]
}
---

# CRYSTAL-19-DB: Database Access

## Introduction

SQLite and Postgres with Crystal. By the end of this lesson you will be able to: Connect to databases; Run queries; Use prepared statements; Map rows.

## Key Concepts

### 1. Connect to databases

Target: Connect to databases. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```crystal
require "sqlite3"

db = DB.open("sqlite3://./test.db")
db.exec("CREATE TABLE IF NOT EXISTS users (name TEXT)")
```
### 2. Run queries

Target: Run queries. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```crystal
db.exec("INSERT INTO users (name) VALUES (?)", "Ada")
```
### 3. Use prepared statements

Target: Use prepared statements. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```crystal
db.query("SELECT name FROM users") do |rs|
  rs.each do
    puts rs.read(String)
  end
end
```
### 4. Map rows

Target: Map rows. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```crystal
db.exec("DELETE FROM users WHERE name = ?", "Ada")
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
