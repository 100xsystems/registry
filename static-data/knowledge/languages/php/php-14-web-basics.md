---
{
  "title": "Web Basics: HTTP, Forms, Sessions",
  "description": "Superglobals, HTTP headers, form handling, and sessions.",
  "type": "lesson",
  "order": 14,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read requests via superglobals",
    "Send responses with headers",
    "Validate and sanitize form input",
    "Manage state with sessions"
  ],
  "knowledge_refs": [
    "php/php-14-web-basics"
  ],
  "prerequisites": [
    "PHP-13"
  ],
  "references": [
    {
      "title": "PHP Manual — Superglobals",
      "url": "https://www.php.net/manual/en/language.variables.superglobals.php"
    },
    {
      "title": "PHP Manual — Sessions",
      "url": "https://www.php.net/manual/en/book.session.php"
    },
    {
      "title": "PHP Manual — Header Function",
      "url": "https://www.php.net/manual/en/function.header.php"
    }
  ]
}
---

# PHP-14-WEB-BASICS: Web Basics: HTTP, Forms, Sessions

## Introduction

Superglobals, HTTP headers, form handling, and sessions. By the end of this lesson you will be able to: Read requests via superglobals; Send responses with headers; Validate and sanitize form input; Manage state with sessions.

## Key Concepts

### 1. Read requests via superglobals

Target: Read requests via superglobals. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```php
<?php
// superglobals
// $_GET["q"] — query string (?q=php)
// $_POST["name"] — form body
// $_SERVER["REQUEST_METHOD"] — GET/POST/...
$q = $_GET["q"] ?? "default";
echo "query: " . htmlspecialchars($q) . "\n";
echo "method: " . $_SERVER["REQUEST_METHOD"] . "\n";
```
### 2. Send responses with headers

Target: Send responses with headers. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```php
<?php
// sending HTTP headers
header("Content-Type: application/json");
header("Cache-Control: no-store");
http_response_code(200);
$payload = ["ok" => true, "items" => [1, 2, 3]];
echo json_encode($payload);
```
### 3. Validate and sanitize form input

Target: Validate and sanitize form input. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```php
<?php
// form validation + sanitization
$email = filter_input(INPUT_POST, "email", FILTER_VALIDATE_EMAIL);
$age   = filter_input(INPUT_POST, "age", FILTER_VALIDATE_INT);
if ($email === false) { echo "invalid email\n"; }
$clean = htmlspecialchars((string) ($_POST["name"] ?? ""), ENT_QUOTES);
// ALWAYS escape on output to prevent XSS
echo "<p>Hello, $clean</p>\n";
```
### 4. Manage state with sessions

Target: Manage state with sessions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```php
<?php
// sessions
session_start();
$_SESSION["user_id"] = 42;
$_SESSION["cart"] = ["kbd", "mouse"];
// on later requests the same session is resumed
echo "user_id: " . ($_SESSION["user_id"] ?? "none") . "\n";
session_destroy();  // careful: clears the session
```

## Practice Questions

1. What is the key idea behind "Web Basics: HTTP, Forms, Sessions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Web Basics: HTTP, Forms, Sessions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Web Basics: HTTP, Forms, Sessions"
1. "Provide advanced patterns and performance considerations for Web Basics: HTTP, Forms, Sessions"

## Key Takeaways

- Master the core ideas of Web Basics: HTTP, Forms, Sessions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
