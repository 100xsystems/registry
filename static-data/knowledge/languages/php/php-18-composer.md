---
{
  "title": "Composer and Packages",
  "description": "Composer.json, dependency management, and Packagist.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Initialize a composer project",
    "Add and manage dependencies",
    "Understand version constraints",
    "Publish and consume packages"
  ],
  "knowledge_refs": [
    "php/php-18-composer"
  ],
  "prerequisites": [
    "PHP-09"
  ],
  "references": [
    {
      "title": "Composer Documentation",
      "url": "https://getcomposer.org/doc/"
    },
    {
      "title": "Packagist",
      "url": "https://packagist.org/"
    },
    {
      "title": "Composer Versions Guide",
      "url": "https://getcomposer.org/doc/articles/versions.md"
    }
  ]
}
---

# PHP-18-COMPOSER: Composer and Packages

## Introduction

Composer.json, dependency management, and Packagist. By the end of this lesson you will be able to: Initialize a composer project; Add and manage dependencies; Understand version constraints; Publish and consume packages.

## Key Concepts

### 1. Initialize a composer project

Target: Initialize a composer project. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```php
<?php
// composer.json (minimal)
// {
//   "require": { "php": ">=8.2", "monolog/monolog": "^3.0" }
// }
// commands:
//   composer init   — create composer.json
//   composer install — install from lockfile
//   composer require monolog/monolog — add + install
//   composer update  — update within constraints
```
### 2. Add and manage dependencies

Target: Add and manage dependencies. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```php
<?php
// using a dependency
require __DIR__ . "/vendor/autoload.php";
use Monolog\Logger;
use Monolog\Handler\StreamHandler;
$log = new Logger("app");
$log->pushHandler(new StreamHandler(__DIR__ . "/app.log", Logger::DEBUG));
$log->info("booted", ["pid" => getmypid()]);
```
### 3. Understand version constraints

Target: Understand version constraints. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```php
<?php
// version constraints
// "monolog/monolog": "^3.0"   — >=3.0.0 <4.0.0 (major locked)
// "psr/log": "~1.0"           — >=1.0.0 <1.1.0
// "guzzlehttp/guzzle": "*"    — any (avoid in production)
// exact: "1.2.3"  |  range: ">=1.0 <2.0"
// the lockfile (composer.lock) pins exact versions for reproducibility
```
### 4. Publish and consume packages

Target: Publish and consume packages. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```php
<?php
// scripts in composer.json
// {
//   "scripts": {
//     "test": "phpunit",
//     "lint": "php -l src",
//     "post-install-cmd": ["@php artisan migrate"]
//   }
// }
// run: composer test   (composer run-script test)
// $COMPOSER_VENDOR_DIR and env vars control behaviour
```

## Practice Questions

1. What is the key idea behind "Composer and Packages"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Composer and Packages with analogies and real-world examples"
1. "Show me common mistakes beginners make with Composer and Packages"
1. "Provide advanced patterns and performance considerations for Composer and Packages"

## Key Takeaways

- Master the core ideas of Composer and Packages through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
