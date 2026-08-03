---
{
  "title": "Control Flow",
  "description": "if/elsif, unless, ternary, and short-circuit logic.",
  "type": "lesson",
  "order": 5,
  "duration": "25 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write conditional branches",
    "Use statement modifiers",
    "Apply the ternary operator"
  ],
  "knowledge_refs": [
    "perl/perl-05-control-flow"
  ],
  "prerequisites": [
    "perl-01-getting-started"
  ],
  "references": [
    {
      "title": "perldoc — perlsyn (conditionals)",
      "url": "https://perldoc.perl.org/perlsyn#Compound-Statements"
    }
  ]
}
---

# PERL-05-CONTROL-FLOW: Control Flow

## Introduction

if/elsif, unless, ternary, and short-circuit logic. By the end of this lesson you will be able to: Write conditional branches; Use statement modifiers; Apply the ternary operator.

## Key Concepts

### 1. Write conditional branches

Target: Write conditional branches. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```perl
# if / elsif / else
use strict;
use warnings;

my $score = 92;
if ($score >= 90) {
    print "A\n";
} elsif ($score >= 80) {
    print "B\n";
} else {
    print "C\n";
}

```
### 2. Use statement modifiers

Target: Use statement modifiers. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```perl
# unless and statement modifiers
use strict;
use warnings;

my $debug = 0;
print "debug on\n" if $debug;
print "not debugging\n" unless $debug;
print "one-liner if\n" if 1 > 0;

```
### 3. Apply the ternary operator

Target: Apply the ternary operator. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```perl
# The ternary operator
use strict;
use warnings;

my $age = 20;
my $status = $age >= 18 ? "adult" : "minor";
print "$status\n";

```
### 4. Write conditional branches

Target: Write conditional branches. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```perl
# Logical operators with short-circuiting
use strict;
use warnings;

my $x = 0;
my $y = 5;
print "both true\n" if $x && $y;       # false — x is falsy
print "x or y\n" if $x || $y;          # true
my $z = $x || "fallback";
print "$z\n";                          # fallback

```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
