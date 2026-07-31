---
{
  "title": "Testing with PHPUnit",
  "description": "Unit tests, assertions, and data providers.",
  "type": "lesson",
  "order": 19,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write PHPUnit test classes",
    "Use assertions and expectations",
    "Structure tests with data providers",
    "Run the test suite from the CLI"
  ],
  "knowledge_refs": [
    "php/php-19-testing"
  ],
  "prerequisites": [
    "PHP-18"
  ],
  "references": [
    {
      "title": "PHPUnit Documentation",
      "url": "https://docs.phpunit.de/en/11.5/index.html"
    },
    {
      "title": "PHPUnit Writing Tests",
      "url": "https://docs.phpunit.de/en/11.5/writing-tests-for-phpunit.html"
    },
    {
      "title": "PHPUnit Data Providers",
      "url": "https://docs.phpunit.de/en/11.5/attributes.html"
    }
  ]
}
---

# PHP-19-TESTING: Testing with PHPUnit

## Introduction

Unit tests, assertions, and data providers. By the end of this lesson you will be able to: Write PHPUnit test classes; Use assertions and expectations; Structure tests with data providers; Run the test suite from the CLI.

## Key Concepts

### 1. Write PHPUnit test classes

Target: Write PHPUnit test classes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```php
<?php
// phpunit test class
use PHPUnit\Framework\TestCase;
final class CalculatorTest extends TestCase {
    public function testAddition(): void {
        $calc = new Calculator();
        $this->assertSame(4, $calc->add(2, 2));
    }
}
// run: ./vendor/bin/phpunit --testdox
```
### 2. Use assertions and expectations

Target: Use assertions and expectations. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```php
<?php
// data providers
use PHPUnit\Framework\Attributes\DataProvider;
use PHPUnit\Framework\TestCase;
final class MulTest extends TestCase {
    #[DataProvider("pairs")]
    public function testMul(int $a, int $b, int $expected): void {
        $this->assertSame($expected, $a * $b);
    }
    public static function pairs(): array {
        return [[2, 3, 6], [0, 9, 0], [-1, 5, -5]];
    }
}
```
### 3. Structure tests with data providers

Target: Structure tests with data providers. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```php
<?php
// expectations (PHPUnit 10+)
use PHPUnit\Framework\TestCase;
final class OrderTest extends TestCase {
    public function testChargeThrowsOnNegative(): void {
        $order = new Order();
        $this->expectException(InvalidArgumentException::class);
        $this->expectExceptionMessage("negative");
        $order->charge(-5);
    }
}
```
### 4. Run the test suite from the CLI

Target: Run the test suite from the CLI. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```php
<?php
// test doubles
use PHPUnit\Framework\TestCase;
final class NotifierTest extends TestCase {
    public function testSendsOnSignup(): void {
        $mailer = $this->createMock(Mailer::class);
        $mailer->expects($this->once())
               ->method("send")
               ->with($this->stringContains("Welcome"));
        $service = new SignupService($mailer);
        $service->signup("alice@example.com");
    }
}
```

## Practice Questions

1. What is the key idea behind "Testing with PHPUnit"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Testing with PHPUnit with analogies and real-world examples"
1. "Show me common mistakes beginners make with Testing with PHPUnit"
1. "Provide advanced patterns and performance considerations for Testing with PHPUnit"

## Key Takeaways

- Master the core ideas of Testing with PHPUnit through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
