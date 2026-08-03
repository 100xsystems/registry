---
{
  "title": "Functions",
  "description": "Subroutines, @_, return, and context.",
  "type": "lesson",
  "order": 9,
  "duration": "30 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define and call subroutines",
    "Access arguments via @_",
    "Return values and defaults"
  ],
  "knowledge_refs": [
    "perl/perl-09-functions"
  ],
  "prerequisites": [
    "perl-05-control-flow"
  ],
  "references": [
    {
      "title": "perldoc — perlsub",
      "url": "https://perldoc.perl.org/perlsub"
    },
    {
      "title": "perldoc — perlfunc",
      "url": "https://perldoc.perl.org/perlfunc"
    }
  ]
}
---

# PERL-09-FUNCTIONS: Functions

## Introduction

Subroutines, @_, return, and context. By the end of this lesson you will be able to: Define and call subroutines; Access arguments via @_; Return values and defaults.

## Key Concepts

### 1. Define and call subroutines

Target: Define and call subroutines. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```perl
# Subroutines: declaration and call
use strict;
use warnings;

sub greet {
    my ($name) = @_;
    return "Hello, $name!";
}

print greet("Perl"), "\n";

```
### 2. Access arguments via @_

Target: Access arguments via @_. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```perl
# @_ is the argument array
use strict;
use warnings;

sub add {
    my ($a, $b) = @_;
    return $a + $b;
}

print add(2, 3), "\n";     # 5
print add(10, 20), "\n";   # 30

```
### 3. Return values and defaults

Target: Return values and defaults. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```perl
# Default arguments with defined-or
use strict;
use warnings;

sub config {
    my ($key, $default) = @_;
    $default //= "unknown";
    return "$key=$default";
}

print config("host"), "\n";
print config("port", 8080), "\n";

```
### 4. Define and call subroutines

Target: Define and call subroutines. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```perl
# Context awareness with wantarray
use strict;
use warnings;

sub list_or_scalar {
    my @vals = (1, 2, 3);
    return wantarray ? @vals : scalar @vals;
}

my @list = list_or_scalar();
my $count = list_or_scalar();
print "@list\n";           # 1 2 3
print "$count\n";          # 3

```

## Practice Questions

1. What is the key idea behind "Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions"
1. "Provide advanced patterns and performance considerations for Functions"

## Key Takeaways

- Master the core ideas of Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
