---
{
  "title": "Getting Started with PHP",
  "description": "Install PHP, run scripts from the CLI, and understand the request lifecycle.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install PHP and run your first script",
    "Use echo, print, and var_dump for output",
    "Understand the CLI vs web SAPIs",
    "Configure php.ini essentials"
  ],
  "knowledge_refs": [
    "php/php-01-getting-started"
  ],
  "prerequisites": [],
  "references": [
    {
      "title": "PHP Manual — Installation",
      "url": "https://www.php.net/manual/en/install.php"
    },
    {
      "title": "PHP Manual — CLI SAPI",
      "url": "https://www.php.net/manual/en/features.commandline.php"
    },
    {
      "title": "PHP The Right Way",
      "url": "https://phptherightway.com/"
    }
  ]
}
---

# PHP-01-GETTING-STARTED: Getting Started with PHP

## Introduction

Install PHP, run scripts from the CLI, and understand the request lifecycle. By the end of this lesson you will be able to: Install PHP and run your first script; Use echo, print, and var_dump for output; Understand the CLI vs web SAPIs; Configure php.ini essentials.

## Key Concepts

### 1. Install PHP and run your first script

Target: Install PHP and run your first script. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```php
<?php
// hello.php — run with: php hello.php
echo "Hello, 100x Systems!\n";
print "Another way to output.\n";
var_dump(42);          // int(42)
var_dump("php");       // string(3) "php"
```
### 2. Use echo, print, and var_dump for output

Target: Use echo, print, and var_dump for output. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```php
<?php
// CLI arguments
var_dump($argv);        // [0] script path, [1..] user args
$name = $argv[1] ?? "world";
echo "Hello, $name\n";
```
### 3. Understand the CLI vs web SAPIs

Target: Understand the CLI vs web SAPIs. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```php
<?php
// SAPI check
if (PHP_SAPI === "cli") {
    echo "Running on the CLI\n";
} else {
    echo "Running under a web server\n";
}
printf("PHP %s on %s\n", PHP_VERSION, PHP_OS);
```
### 4. Configure php.ini essentials

Target: Configure php.ini essentials. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```php
<?php
// php.ini essentials visible at runtime
echo "display_errors: " . ini_get("display_errors") . "\n";
echo "memory_limit: " . ini_get("memory_limit") . "\n";
// set for this process only
ini_set("memory_limit", "256M");
```

## Practice Questions

1. What is the key idea behind "Getting Started with PHP"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with PHP with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with PHP"
1. "Provide advanced patterns and performance considerations for Getting Started with PHP"

## Key Takeaways

- Master the core ideas of Getting Started with PHP through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
