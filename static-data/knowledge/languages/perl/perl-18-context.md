---
{
  "title": "Context",
  "description": "Scalar vs list context and wantarray.",
  "type": "lesson",
  "order": 18,
  "duration": "30 min",
  "difficulty": "expert",
  "learning_objectives": [
    "Explain scalar and list context",
    "See how builtins change behavior",
    "Use wantarray for context-aware functions"
  ],
  "knowledge_refs": [
    "perl/perl-18-context"
  ],
  "prerequisites": [
    "perl-09-functions"
  ],
  "references": [
    {
      "title": "perldoc — perldata (context)",
      "url": "https://perldoc.perl.org/perldata#Scalar-values"
    },
    {
      "title": "perldoc — perlfunc (wantarray)",
      "url": "https://perldoc.perl.org/perlfunc#wantarray"
    }
  ]
}
---

# PERL-18-CONTEXT: Context

## Introduction

Scalar vs list context and wantarray. By the end of this lesson you will be able to: Explain scalar and list context; See how builtins change behavior; Use wantarray for context-aware functions.

## Key Concepts

### 1. Explain scalar and list context

Target: Explain scalar and list context. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```perl
# Scalar and list context
use strict;
use warnings;

my @array = (1, 2, 3, 4);
my $count = @array;        # scalar context — count
my @copy = @array;         # list context — elements
print "$count\n";          # 4
print "@copy\n";           # 1 2 3 4

```
### 2. See how builtins change behavior

Target: See how builtins change behavior. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```perl
# Context affects how builtins behave
use strict;
use warnings;

my @sorted = sort (3, 1, 2);      # list context
my $last = (sort (3, 1, 2))[0];   # first element
print "@sorted\n";               # 1 2 3
print "$last\n";                 # 1

```
### 3. Use wantarray for context-aware functions

Target: Use wantarray for context-aware functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```perl
# Forcing context
use strict;
use warnings;

my @items = (5, 6, 7);
my $total = 0;
$total += $_ for @items;
print scalar(@items), " items, sum $total\n";

```
### 4. Explain scalar and list context

Target: Explain scalar and list context. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```perl
# void context and side effects
use strict;
use warnings;

my @nums = (1, 2, 3);
@nums = sort { $b <=> $a } @nums;   # void-ish assignment
print "@nums\n";                    # 3 2 1

```

## Practice Questions

1. What is the key idea behind "Context"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Context with analogies and real-world examples"
1. "Show me common mistakes beginners make with Context"
1. "Provide advanced patterns and performance considerations for Context"

## Key Takeaways

- Master the core ideas of Context through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
