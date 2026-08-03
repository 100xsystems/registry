---
{
  "title": "Values and Types",
  "description": "Scalars, auto-conversion, undef, and comparisons.",
  "type": "lesson",
  "order": 2,
  "duration": "25 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Create scalar values",
    "Explain automatic number/string conversion",
    "Use defined and the // operator"
  ],
  "knowledge_refs": [
    "perl/perl-02-values-types"
  ],
  "prerequisites": [
    "perl-01-getting-started"
  ],
  "references": [
    {
      "title": "perldoc — perldata",
      "url": "https://perldoc.perl.org/perldata"
    },
    {
      "title": "perldoc — perlsyn (values)",
      "url": "https://perldoc.perl.org/perlsyn"
    }
  ]
}
---

# PERL-02-VALUES-TYPES: Values and Types

## Introduction

Scalars, auto-conversion, undef, and comparisons. By the end of this lesson you will be able to: Create scalar values; Explain automatic number/string conversion; Use defined and the // operator.

## Key Concepts

### 1. Create scalar values

Target: Create scalar values. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```perl
# Scalar values: numbers and strings
use strict;
use warnings;

my $int = 42;
my $float = 3.14;
my $str = "hello";
my $bool = 1;
print "$int $float $str $bool\n";

```
### 2. Explain automatic number/string conversion

Target: Explain automatic number/string conversion. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```perl
# Perl auto-converts between numbers and strings
use strict;
use warnings;

my $x = "3";
my $y = 4;
print $x + $y, "\n";      # 7 — numeric context
print $x . $y, "\n";      # "34" — string context

```
### 3. Use defined and the // operator

Target: Use defined and the // operator. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```perl
# Undef and defined()
use strict;
use warnings;

my $x;                     # undef
print "defined\n" if defined $x;
print "undef\n" unless defined $x;
my $y = $x // "default";   # defined-or operator
print "$y\n";              # default

```
### 4. Create scalar values

Target: Create scalar values. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```perl
# Numeric and string comparison operators
use strict;
use warnings;

my $n = 10;
my $s = "10";
print "numeric eq\n" if $n == $s;
print "string eq\n" if $n eq $s;
print "compare: ", $n <=> 20, "\n";   # -1

```

## Practice Questions

1. What is the key idea behind "Values and Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Values and Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Values and Types"
1. "Provide advanced patterns and performance considerations for Values and Types"

## Key Takeaways

- Master the core ideas of Values and Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
