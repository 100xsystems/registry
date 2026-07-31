---
{
  "title": "Regular Expressions",
  "description": "PCRE patterns, preg_match, and replacement.",
  "type": "lesson",
  "order": 17,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write PCRE patterns",
    "Match with preg_match and preg_match_all",
    "Replace and split with preg_ functions",
    "Use capture groups and modifiers"
  ],
  "knowledge_refs": [
    "php/php-17-regex"
  ],
  "prerequisites": [
    "PHP-07"
  ],
  "references": [
    {
      "title": "PHP Manual — PCRE",
      "url": "https://www.php.net/manual/en/book.pcre.php"
    },
    {
      "title": "PHP Manual — preg_match",
      "url": "https://www.php.net/manual/en/function.preg-match.php"
    },
    {
      "title": "PCRE Patterns Syntax",
      "url": "https://www.php.net/manual/en/reference.pcre.pattern.syntax.php"
    }
  ]
}
---

# PHP-17-REGEX: Regular Expressions

## Introduction

PCRE patterns, preg_match, and replacement. By the end of this lesson you will be able to: Write PCRE patterns; Match with preg_match and preg_match_all; Replace and split with preg_ functions; Use capture groups and modifiers.

## Key Concepts

### 1. Write PCRE patterns

Target: Write PCRE patterns. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```php
<?php
// preg_match captures
$text = "Order #12345 placed on 2026-07-29";
preg_match("/#(\d+)/", $text, $m);
echo $m[1] . "\n";  // 12345
preg_match("/(\d{4})-(\d{2})-(\d{2})/", $text, $d);
echo "$d[1]/$d[2]/$d[3]\n";
```
### 2. Match with preg_match and preg_match_all

Target: Match with preg_match and preg_match_all. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```php
<?php
// preg_match_all
$log = "GET /api 200\nPOST /api 201\nGET / 404";
preg_match_all("#(\w+) /\S* (\d{3})#", $log, $rows, PREG_SET_ORDER);
foreach ($rows as $r) { echo $r[1] . " -> " . $r[2] . "\n"; }
```
### 3. Replace and split with preg_ functions

Target: Replace and split with preg_ functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```php
<?php
// replace and split
$s = "  Trim   me   please  ";
$clean = preg_replace("/\s+/", " ", trim($s));
echo $clean . "\n";  // Trim me please
$parts = preg_split("/[,\s]+/", "apple, banana cherry");
var_dump($parts);
```
### 4. Use capture groups and modifiers

Target: Use capture groups and modifiers. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```php
<?php
// modifiers and validation
$email = "alice@example.com";
$pattern = "/^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/i";
echo preg_match($pattern, $email) ? "valid\n" : "invalid\n";
// non-capturing groups + lookahead
preg_match("/(?:\d{3}-)?\d{4}/", "555-1234", $m);
echo $m[0] . "\n";
```

## Practice Questions

1. What is the key idea behind "Regular Expressions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Regular Expressions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Regular Expressions"
1. "Provide advanced patterns and performance considerations for Regular Expressions"

## Key Takeaways

- Master the core ideas of Regular Expressions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
