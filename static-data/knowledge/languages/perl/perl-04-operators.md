---
{
  "title": "Operators",
  "description": "Arithmetic, string, assignment, and increment operators.",
  "type": "lesson",
  "order": 4,
  "duration": "25 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use arithmetic operators",
    "Concatenate and repeat strings",
    "Apply compound assignment"
  ],
  "knowledge_refs": [
    "perl/perl-04-operators"
  ],
  "prerequisites": [
    "perl-02-values-types"
  ],
  "references": [
    {
      "title": "perldoc — perlop",
      "url": "https://perldoc.perl.org/perlop"
    }
  ]
}
---

# PERL-04-OPERATORS: Operators

## Introduction

Arithmetic, string, assignment, and increment operators. By the end of this lesson you will be able to: Use arithmetic operators; Concatenate and repeat strings; Apply compound assignment.

## Key Concepts

### 1. Use arithmetic operators

Target: Use arithmetic operators. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```perl
# Arithmetic operators
use strict;
use warnings;

my $x = 7;
print $x + 3, "\n";       # 10
print $x - 2, "\n";       # 5
print $x * 2, "\n";       # 14
print $x / 2, "\n";       # 3.5
print $x % 4, "\n";       # 3
print $x ** 2, "\n";      # 49 — exponentiation

```
### 2. Concatenate and repeat strings

Target: Concatenate and repeat strings. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```perl
# Auto-increment and decrement
use strict;
use warnings;

my $count = 0;
$count++;                  # post-increment
++$count;                  # pre-increment
print "$count\n";          # 2
$count--;
print "$count\n";          # 1

```
### 3. Apply compound assignment

Target: Apply compound assignment. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```perl
# String operators: concatenation and repetition
use strict;
use warnings;

my $greeting = "Hello" . " " . "World";
my $line = "-" x 10;
print "$greeting\n";
print "$line\n";

```
### 4. Use arithmetic operators

Target: Use arithmetic operators. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```perl
# Assignment operators
use strict;
use warnings;

my $n = 10;
$n += 5;                   # 15
$n -= 3;                   # 12
$n *= 2;                   # 24
$n /= 4;                   # 6
print "$n\n";

```

## Practice Questions

1. What is the key idea behind "Operators"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Operators with analogies and real-world examples"
1. "Show me common mistakes beginners make with Operators"
1. "Provide advanced patterns and performance considerations for Operators"

## Key Takeaways

- Master the core ideas of Operators through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
