---
{
  "title": "Dates and Time",
  "description": "DateTime, DateTimeImmutable, and timezone handling.",
  "type": "lesson",
  "order": 16,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Work with DateTime and DateTimeImmutable",
    "Format and parse dates",
    "Handle timezones correctly",
    "Calculate intervals and differences"
  ],
  "knowledge_refs": [
    "php/php-16-datetime"
  ],
  "prerequisites": [
    "PHP-07"
  ],
  "references": [
    {
      "title": "PHP Manual — DateTimeImmutable",
      "url": "https://www.php.net/manual/en/class.datetimeimmutable.php"
    },
    {
      "title": "PHP Manual — DateTimeInterface",
      "url": "https://www.php.net/manual/en/class.datetimeinterface.php"
    },
    {
      "title": "PHP Manual — Date and Time Functions",
      "url": "https://www.php.net/manual/en/book.datetime.php"
    }
  ]
}
---

# PHP-16-DATETIME: Dates and Time

## Introduction

DateTime, DateTimeImmutable, and timezone handling. By the end of this lesson you will be able to: Work with DateTime and DateTimeImmutable; Format and parse dates; Handle timezones correctly; Calculate intervals and differences.

## Key Concepts

### 1. Work with DateTime and DateTimeImmutable

Target: Work with DateTime and DateTimeImmutable. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```php
<?php
// DateTime basics
$now = new DateTime();
echo $now->format("Y-m-d H:i:s") . "\n";
$date = new DateTime("2026-07-29 10:30:00", new DateTimeZone("UTC"));
echo $date->format("D, d M Y") . "\n";
```
### 2. Format and parse dates

Target: Format and parse dates. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```php
<?php
// DateTimeImmutable: never mutates
try {
    $d = new DateTimeImmutable("2026-07-29");
    $plus = $d->modify("+10 days");
    echo $d->format("Y-m-d") . "\n";     // unchanged
    echo $plus->format("Y-m-d") . "\n";  // 2026-08-08
} catch (Exception $e) {
    echo "parse error: " . $e->getMessage() . "\n";
}
```
### 3. Handle timezones correctly

Target: Handle timezones correctly. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```php
<?php
// timezone handling
$zones = ["UTC", "America/New_York", "Asia/Kolkata"];
$utc = new DateTime("2026-07-29 12:00:00", new DateTimeZone("UTC"));
foreach ($zones as $z) {
    $local = clone $utc;
    $local->setTimezone(new DateTimeZone($z));
    echo $z . ": " . $local->format("H:i") . "\n";
}
```
### 4. Calculate intervals and differences

Target: Calculate intervals and differences. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```php
<?php
// intervals and differences
$a = new DateTimeImmutable("2026-01-01");
$b = new DateTimeImmutable("2026-07-29");
$diff = $a->diff($b);
echo $diff->days . " days\n";
echo $diff->format("%y years %m months %d days") . "\n";
```

## Practice Questions

1. What is the key idea behind "Dates and Time"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Dates and Time with analogies and real-world examples"
1. "Show me common mistakes beginners make with Dates and Time"
1. "Provide advanced patterns and performance considerations for Dates and Time"

## Key Takeaways

- Master the core ideas of Dates and Time through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
