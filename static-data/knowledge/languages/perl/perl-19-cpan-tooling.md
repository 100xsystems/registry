---
{
  "title": "CPAN and Tooling",
  "description": "The module ecosystem, installers, and perldoc.",
  "type": "lesson",
  "order": 19,
  "duration": "25 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Install modules with cpan and cpanm",
    "Use common utility modules",
    "Write one-liners"
  ],
  "knowledge_refs": [
    "perl/perl-19-cpan-tooling"
  ],
  "prerequisites": [
    "perl-16-modules"
  ],
  "references": [
    {
      "title": "MetaCPAN — Module Search",
      "url": "https://metacpan.org/"
    },
    {
      "title": "CPAN — Official Site",
      "url": "https://www.cpan.org/"
    },
    {
      "title": "Learn Perl — CPAN section",
      "url": "https://learn.perl.org/docs/"
    }
  ]
}
---

# PERL-19-CPAN-TOOLING: CPAN and Tooling

## Introduction

The module ecosystem, installers, and perldoc. By the end of this lesson you will be able to: Install modules with cpan and cpanm; Use common utility modules; Write one-liners.

## Key Concepts

### 1. Install modules with cpan and cpanm

Target: Install modules with cpan and cpanm. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```perl
# CPAN: the Comprehensive Perl Archive Network
# cpan Module::Name          -> install
# cpanm Module::Name         -> fast installer
# perldoc Module::Name       -> documentation
print "CPAN hosts over 200,000 modules\n";

```
### 2. Use common utility modules

Target: Use common utility modules. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```perl
# Common modules: List::Util, Scalar::Util
use strict;
use warnings;

use List::Util qw(any first);
use Scalar::Util qw(looks_like_number);

my @nums = (1, 2, 3);
print "has even\n" if any { $_ % 2 == 0 } @nums;
print "first: ", first { $_ > 1 } @nums, "\n";   # 2
print looks_like_number("42") ? "numeric\n" : "text\n";

```
### 3. Write one-liners

Target: Write one-liners. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```perl
# Text processing with Perl one-liners
# perl -pe 's/old/new/g' file.txt
# perl -ne 'print if /pattern/' file.txt
# perl -a -F, -n -e 'print $F[1]' file.csv
print "one-liners power the Unix toolbox\n";

```
### 4. Install modules with cpan and cpanm

Target: Install modules with cpan and cpanm. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```perl
# perldoc is your best friend
# perldoc perl            -> overview
# perldoc perlfunc        -> all functions
# perldoc -f split        -> specific function
# perldoc perlre          -> regex reference
print "learn.perl.org has interactive tutorials\n";

```

## Practice Questions

1. What is the key idea behind "CPAN and Tooling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain CPAN and Tooling with analogies and real-world examples"
1. "Show me common mistakes beginners make with CPAN and Tooling"
1. "Provide advanced patterns and performance considerations for CPAN and Tooling"

## Key Takeaways

- Master the core ideas of CPAN and Tooling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
