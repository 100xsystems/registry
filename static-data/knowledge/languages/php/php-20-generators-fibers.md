---
{
  "title": "Generators and Fibers",
  "description": "yield generators, iterators, and cooperative concurrency with Fibers.",
  "type": "lesson",
  "order": 20,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create generators with yield",
    "Stream large datasets lazily",
    "Suspend and resume with Fibers",
    "Compare coroutines to blocking code"
  ],
  "knowledge_refs": [
    "php/php-20-generators-fibers"
  ],
  "prerequisites": [
    "PHP-15"
  ],
  "references": [
    {
      "title": "PHP Manual — Generators",
      "url": "https://www.php.net/manual/en/language.generators.php"
    },
    {
      "title": "PHP Manual — Fiber",
      "url": "https://www.php.net/manual/en/class.fiber.php"
    },
    {
      "title": "PHP 8.1 Fibers RFC",
      "url": "https://wiki.php.net/rfc/fibers"
    }
  ]
}
---

# PHP-20-GENERATORS-FIBERS: Generators and Fibers

## Introduction

yield generators, iterators, and cooperative concurrency with Fibers. By the end of this lesson you will be able to: Create generators with yield; Stream large datasets lazily; Suspend and resume with Fibers; Compare coroutines to blocking code.

## Key Concepts

### 1. Create generators with yield

Target: Create generators with yield. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```php
<?php
// generator yields lazily
function squares(int $n): Generator {
    for ($i = 1; $i <= $n; $i++) {
        yield $i * $i;
    }
}
foreach (squares(5) as $s) { echo "$s "; }
echo "\n";  // 1 4 9 16 25
// nothing runs until iteration starts — lazy!
```
### 2. Stream large datasets lazily

Target: Stream large datasets lazily. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```php
<?php
// yield with keys + delegating with yield from
function pairs(): Generator {
    yield "a" => 1;
    yield "b" => 2;
}
function all(): Generator {
    yield 0;
    yield from pairs();
    yield 99;
}
foreach (all() as $k => $v) { echo "$k=>$v "; }
echo "\n";  // 0=>0 a=>1 b=>2 99=>99
```
### 3. Suspend and resume with Fibers

Target: Suspend and resume with Fibers. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```php
<?php
// streaming a huge file
function readLines(string $path): Generator {
    $fp = fopen($path, "r");
    while (($line = fgets($fp)) !== false) {
        yield rtrim($line, "\r\n");
    }
    fclose($fp);
}
foreach (readLines("big.log") as $n => $line) {
    if ($n > 2) break;   // memory stays flat
    echo $line . "\n";
}
```
### 4. Compare coroutines to blocking code

Target: Compare coroutines to blocking code. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```php
<?php
// Fiber: cooperative multitasking (PHP 8.1+)
$fiber = new Fiber(function (): void {
    $value = Fiber::suspend("waiting...");
    echo "resumed with: $value\n";
});
echo $fiber->start() . "\n";  // waiting...
$fiber->resume("payload");      // resumed with: payload
// yields control without blocking — foundation of async libraries
```

## Practice Questions

1. What is the key idea behind "Generators and Fibers"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Generators and Fibers with analogies and real-world examples"
1. "Show me common mistakes beginners make with Generators and Fibers"
1. "Provide advanced patterns and performance considerations for Generators and Fibers"

## Key Takeaways

- Master the core ideas of Generators and Fibers through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
