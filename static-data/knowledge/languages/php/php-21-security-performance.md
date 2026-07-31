---
{
  "title": "Security and Performance",
  "description": "Injection defense, escaping, opcache, and profiling.",
  "type": "lesson",
  "order": 21,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Prevent SQL injection and XSS",
    "Use password hashing correctly",
    "Leverage OPcache for speed",
    "Profile with Xdebug and identify hotspots"
  ],
  "knowledge_refs": [
    "php/php-21-security-performance"
  ],
  "prerequisites": [
    "PHP-14"
  ],
  "references": [
    {
      "title": "PHP Manual — Security",
      "url": "https://www.php.net/manual/en/security.php"
    },
    {
      "title": "PHP Manual — OPcache",
      "url": "https://www.php.net/manual/en/book.opcache.php"
    },
    {
      "title": "PHP Manual — Xdebug",
      "url": "https://www.php.net/manual/en/ref.xdebug.php"
    }
  ]
}
---

# PHP-21-SECURITY-PERFORMANCE: Security and Performance

## Introduction

Injection defense, escaping, opcache, and profiling. By the end of this lesson you will be able to: Prevent SQL injection and XSS; Use password hashing correctly; Leverage OPcache for speed; Profile with Xdebug and identify hotspots.

## Key Concepts

### 1. Prevent SQL injection and XSS

Target: Prevent SQL injection and XSS. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```php
<?php
// SQL injection defense: parameterized queries only
$pdo = new PDO("sqlite::memory:");
$pdo->exec("CREATE TABLE t (id INTEGER, name TEXT)");
$userInput = "Alice'; DROP TABLE t; --";
$stmt = $pdo->prepare("INSERT INTO t (name) VALUES (?)");
$stmt->execute([$userInput]);  // stored literally, harmless
echo $pdo->query("SELECT COUNT(*) FROM t")->fetchColumn() . "\n";
```
### 2. Use password hashing correctly

Target: Use password hashing correctly. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```php
<?php
// XSS defense: escape on output
$user = "<script>alert(1)</script>";
echo htmlspecialchars($user, ENT_QUOTES, "UTF-8") . "\n";
// never: echo $user;  — raw injection into HTML
```
### 3. Leverage OPcache for speed

Target: Leverage OPcache for speed. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```php
<?php
// password hashing
$hash = password_hash("s3cret!", PASSWORD_DEFAULT);
$ok = password_verify("s3cret!", $hash);
echo $ok ? "verified\n" : "failed\n";
// never store plain text; never md5/sha1 for passwords
// PASSWORD_DEFAULT auto-upgrades as PHP evolves
```
### 4. Profile with Xdebug and identify hotspots

Target: Profile with Xdebug and identify hotspots. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```php
<?php
// OPcache + profiling
// php.ini: opcache.enable=1, opcache.memory_consumption=128
if (function_exists("opcache_get_status")) {
    $s = opcache_get_status(false);
    echo "cached scripts: " . $s["opcache_statistics"]["num_cached_scripts"] . "\n";
}
// profile with Xdebug: xdebug.mode=profile
$start = hrtime(true);
usleep(1000);   // simulate work
echo "elapsed ms: " . ((hrtime(true) - $start) / 1e6) . "\n";
```

## Practice Questions

1. What is the key idea behind "Security and Performance"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Security and Performance with analogies and real-world examples"
1. "Show me common mistakes beginners make with Security and Performance"
1. "Provide advanced patterns and performance considerations for Security and Performance"

## Key Takeaways

- Master the core ideas of Security and Performance through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
