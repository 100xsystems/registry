---
{
  "title": "Namespaces and Autoloading",
  "description": "Namespaces, use statements, and PSR-4 autoloading with Composer.",
  "type": "lesson",
  "order": 9,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Organize code with namespaces",
    "Import symbols with use",
    "Register an autoloader",
    "Follow PSR-4 conventions"
  ],
  "knowledge_refs": [
    "php/php-09-namespaces-autoloading"
  ],
  "prerequisites": [
    "PHP-08"
  ],
  "references": [
    {
      "title": "PHP Manual — Namespaces",
      "url": "https://www.php.net/manual/en/language.namespaces.php"
    },
    {
      "title": "PHP-FIG — PSR-4 Autoloading",
      "url": "https://www.php-fig.org/psr/psr-4/"
    },
    {
      "title": "Composer Autoloading",
      "url": "https://getcomposer.org/doc/01-basic-usage.md#autoloading"
    }
  ]
}
---

# PHP-09-NAMESPACES-AUTOLOADING: Namespaces and Autoloading

## Introduction

Namespaces, use statements, and PSR-4 autoloading with Composer. By the end of this lesson you will be able to: Organize code with namespaces; Import symbols with use; Register an autoloader; Follow PSR-4 conventions.

## Key Concepts

### 1. Organize code with namespaces

Target: Organize code with namespaces. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```php
<?php
// file: src/Acme/Logger.php
namespace Acme;
class Logger {
    public function log(string $msg): void { echo "[LOG] $msg\n"; }
}
```
### 2. Import symbols with use

Target: Import symbols with use. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```php
<?php
// file: src/Acme/User.php
namespace Acme;
class User { public function __construct(public string $name) {} }
```
### 3. Register an autoloader

Target: Register an autoloader. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```php
<?php
// consuming namespaces
use Acme\Logger;
use Acme\User as Account;
$logger = new Logger();
$logger->log("startup");
$user = new Account("Alice");
echo $user->name . "\n";
```
### 4. Follow PSR-4 conventions

Target: Follow PSR-4 conventions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```php
<?php
// simple autoloader + PSR-4 flavor
spl_autoload_register(function (string $class): void {
    $prefix = "Acme\\";
    if (str_starts_with($class, $prefix)) {
        $rel = substr($class, strlen($prefix));
        $file = __DIR__ . "/src/" . str_replace("\\", "/", $rel) . ".php";
        if (is_file($file)) require $file;
    }
});
// composer does this for you: require __DIR__ . '/vendor/autoload.php';
$logger = new \Acme\Logger();
$logger->log("autoloaded");
```

## Practice Questions

1. What is the key idea behind "Namespaces and Autoloading"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Namespaces and Autoloading with analogies and real-world examples"
1. "Show me common mistakes beginners make with Namespaces and Autoloading"
1. "Provide advanced patterns and performance considerations for Namespaces and Autoloading"

## Key Takeaways

- Master the core ideas of Namespaces and Autoloading through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
