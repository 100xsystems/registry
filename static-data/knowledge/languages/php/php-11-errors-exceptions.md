---
{
  "title": "Errors and Exceptions",
  "description": "Throwables, try/catch/finally, and custom exceptions.",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Distinguish Error from Exception",
    "Catch and handle exceptions with try/catch/finally",
    "Throw typed exceptions",
    "Set a global error handler"
  ],
  "knowledge_refs": [
    "php/php-11-errors-exceptions"
  ],
  "prerequisites": [
    "PHP-07"
  ],
  "references": [
    {
      "title": "PHP Manual — Exceptions",
      "url": "https://www.php.net/manual/en/language.exceptions.php"
    },
    {
      "title": "PHP Manual — Throwable",
      "url": "https://www.php.net/manual/en/class.throwable.php"
    },
    {
      "title": "PHP Manual — Error Handling",
      "url": "https://www.php.net/manual/en/book.errorfunc.php"
    }
  ]
}
---

# PHP-11-ERRORS-EXCEPTIONS: Errors and Exceptions

## Introduction

Throwables, try/catch/finally, and custom exceptions. By the end of this lesson you will be able to: Distinguish Error from Exception; Catch and handle exceptions with try/catch/finally; Throw typed exceptions; Set a global error handler.

## Key Concepts

### 1. Distinguish Error from Exception

Target: Distinguish Error from Exception. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```php
<?php
// try/catch/finally
function risky(int $n): int {
    if ($n < 0) throw new InvalidArgumentException("negative!");
    if ($n === 0) throw new RuntimeException("zero!");
    return 100 / $n;
}
try {
    echo risky(0) . "\n";
} catch (InvalidArgumentException $e) {
    echo "bad input: " . $e->getMessage() . "\n";
} catch (RuntimeException $e) {
    echo "runtime: " . $e->getMessage() . "\n";
} finally {
    echo "always runs\n";
}
```
### 2. Catch and handle exceptions with try/catch/finally

Target: Catch and handle exceptions with try/catch/finally. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```php
<?php
// Throwable covers both Error and Exception
function fail(): void {
    throw new TypeError("wrong type");
}
try {
    fail();
} catch (Throwable $t) {
    echo get_class($t) . ": " . $t->getMessage() . "\n";
}
```
### 3. Throw typed exceptions

Target: Throw typed exceptions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```php
<?php
// custom exception types
class PaymentFailed extends RuntimeException {}
class InsufficientFunds extends PaymentFailed {}
function charge(float $amount): void {
    if ($amount > 100) throw new InsufficientFunds("limit exceeded");
}
try {
    charge(500);
} catch (PaymentFailed $e) {   // catches the subtype too
    echo "payment error: " . $e->getMessage() . "\n";
}
```
### 4. Set a global error handler

Target: Set a global error handler. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```php
<?php
// global error handler + throw on error
set_error_handler(function (int $severity, string $msg, string $file, int $line): bool {
    if (!(error_reporting() & $severity)) return false;
    throw new ErrorException($msg, 0, $severity, $file, $line);
});
// now a PHP warning becomes an exception
try {
    $fp = fopen("/nonexistent/file", "r");
} catch (ErrorException $e) {
    echo "caught warning as exception: " . $e->getMessage() . "\n";
}
```

## Practice Questions

1. What is the key idea behind "Errors and Exceptions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Errors and Exceptions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Errors and Exceptions"
1. "Provide advanced patterns and performance considerations for Errors and Exceptions"

## Key Takeaways

- Master the core ideas of Errors and Exceptions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
