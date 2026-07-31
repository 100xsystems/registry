---
{
  "title": "Variables and Data Types",
  "description": "Scalar types, arrays, type juggling, and strict typing.",
  "type": "lesson",
  "order": 2,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare variables and understand the eight data types",
    "Use type juggling and explicit casts",
    "Enforce strict_types in modern PHP",
    "Work with constants and null"
  ],
  "knowledge_refs": [
    "php/php-02-variables-types"
  ],
  "prerequisites": [
    "PHP-01"
  ],
  "references": [
    {
      "title": "PHP Manual — Types",
      "url": "https://www.php.net/manual/en/language.types.php"
    },
    {
      "title": "PHP Manual — Variables",
      "url": "https://www.php.net/manual/en/language.variables.php"
    },
    {
      "title": "PHP 8 Type System Overview",
      "url": "https://php.watch/articles/php-type-system"
    }
  ]
}
---

# PHP-02-VARIABLES-TYPES: Variables and Data Types

## Introduction

Scalar types, arrays, type juggling, and strict typing. By the end of this lesson you will be able to: Declare variables and understand the eight data types; Use type juggling and explicit casts; Enforce strict_types in modern PHP; Work with constants and null.

## Key Concepts

### 1. Declare variables and understand the eight data types

Target: Declare variables and understand the eight data types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```php
<?php
declare(strict_types=1);  // strict mode: no silent coercion
$i = 42;        // int
$f = 3.14;      // float
$s = "hello";   // string
$b = true;      // bool
$n = null;      // null
var_dump($i, $f, $s, $b, $n);
```
### 2. Use type juggling and explicit casts

Target: Use type juggling and explicit casts. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```php
<?php
// type juggling (loose mode default)
var_dump("42" + 8);        // int(50)  — numeric string coerced
var_dump("5 apples" * 2);  // int(10)  — leading numeric part
var_dump((int)"3.99");     // int(3)   — explicit cast
var_dump((string)100);     // string(3) "100"
```
### 3. Enforce strict_types in modern PHP

Target: Enforce strict_types in modern PHP. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```php
<?php
declare(strict_types=1);
function add(int $a, int $b): int {
    return $a + $b;
}
// In strict mode this throws TypeError, not coercion:
try {
    add("5", 3);
} catch (TypeError $e) {
    echo "TypeError: " . $e->getMessage() . "\n";
}
```
### 4. Work with constants and null

Target: Work with constants and null. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```php
<?php
define("APP_NAME", "100x");   // global constant
const VERSION = "1.0";         // compile-time constant
$value = null;
$result = $value ?? "default";  // null coalescing
var_dump(APP_NAME, VERSION, $result);
```

## Practice Questions

1. What is the key idea behind "Variables and Data Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables and Data Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables and Data Types"
1. "Provide advanced patterns and performance considerations for Variables and Data Types"

## Key Takeaways

- Master the core ideas of Variables and Data Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
