---
{
  "title": "Databases with PDO",
  "description": "PDO, prepared statements, and safe database access.",
  "type": "lesson",
  "order": 13,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Connect with PDO and DSNs",
    "Use prepared statements to prevent SQL injection",
    "Fetch data in different modes",
    "Manage transactions"
  ],
  "knowledge_refs": [
    "php/php-13-databases-pdo"
  ],
  "prerequisites": [
    "PHP-12"
  ],
  "references": [
    {
      "title": "PHP Manual — PDO",
      "url": "https://www.php.net/manual/en/book.pdo.php"
    },
    {
      "title": "PHP Manual — PDO::prepare",
      "url": "https://www.php.net/manual/en/pdo.prepare.php"
    },
    {
      "title": "PHP Manual — PDO Transactions",
      "url": "https://www.php.net/manual/en/pdo.transactions.php"
    }
  ]
}
---

# PHP-13-DATABASES-PDO: Databases with PDO

## Introduction

PDO, prepared statements, and safe database access. By the end of this lesson you will be able to: Connect with PDO and DSNs; Use prepared statements to prevent SQL injection; Fetch data in different modes; Manage transactions.

## Key Concepts

### 1. Connect with PDO and DSNs

Target: Connect with PDO and DSNs. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```php
<?php
// PDO connection (SQLite for the demo)
$pdo = new PDO("sqlite::memory:");
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$pdo->exec("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INT)");
// prepared statement protects against injection
$stmt = $pdo->prepare("INSERT INTO users (name, age) VALUES (?, ?)");
$stmt->execute(["Alice", 30]);
$stmt->execute(["Bob", 25]);
```
### 2. Use prepared statements to prevent SQL injection

Target: Use prepared statements to prevent SQL injection. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```php
<?php
// named placeholders
$pdo = new PDO("sqlite::memory:");
$pdo->exec("CREATE TABLE t (name TEXT, city TEXT)");
$stmt = $pdo->prepare("INSERT INTO t (name, city) VALUES (:name, :city)");
$stmt->execute([":name" => "Alice", ":city" => "Paris"]);
$stmt->execute([":name" => "Bob", ":city" => "London"]);
echo $pdo->query("SELECT COUNT(*) FROM t")->fetchColumn() . "\n";  // 2
```
### 3. Fetch data in different modes

Target: Fetch data in different modes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```php
<?php
// fetch modes
$pdo = new PDO("sqlite::memory:");
$pdo->exec("CREATE TABLE t (id INTEGER, name TEXT)");
$pdo->exec("INSERT INTO t VALUES (1, 'Alice'), (2, 'Bob')");
$rows = $pdo->query("SELECT * FROM t")->fetchAll(PDO::FETCH_ASSOC);
var_dump($rows);
// as objects
class Row {}
$objs = $pdo->query("SELECT * FROM t")->fetchAll(PDO::FETCH_CLASS, Row::class);
echo $objs[0]->name . "\n";
```
### 4. Manage transactions

Target: Manage transactions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```php
<?php
// transactions
$pdo = new PDO("sqlite::memory:");
$pdo->exec("CREATE TABLE accounts (id INTEGER PRIMARY KEY, balance INT)");
$pdo->exec("INSERT INTO accounts VALUES (1, 100), (2, 0)");
$pdo->beginTransaction();
try {
    $pdo->exec("UPDATE accounts SET balance = balance - 50 WHERE id = 1");
    $pdo->exec("UPDATE accounts SET balance = balance + 50 WHERE id = 2");
    $pdo->commit();
} catch (Throwable $e) {
    $pdo->rollBack();
    throw $e;
}
foreach ($pdo->query("SELECT * FROM accounts") as $row) {
    echo $row["id"] . ":" . $row["balance"] . " ";
}
echo "\n";  // 1:50 2:50
```

## Practice Questions

1. What is the key idea behind "Databases with PDO"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Databases with PDO with analogies and real-world examples"
1. "Show me common mistakes beginners make with Databases with PDO"
1. "Provide advanced patterns and performance considerations for Databases with PDO"

## Key Takeaways

- Master the core ideas of Databases with PDO through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
