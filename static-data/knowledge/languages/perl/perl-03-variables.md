---
{
  "title": "Variables",
  "description": "Scalars, arrays, hashes, strict, and scoping.",
  "type": "lesson",
  "order": 3,
  "duration": "25 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare the three variable sigils",
    "Use strict and warnings",
    "Distinguish my from our"
  ],
  "knowledge_refs": [
    "perl/perl-03-variables"
  ],
  "prerequisites": [
    "perl-02-values-types"
  ],
  "references": [
    {
      "title": "perldoc — perlvar",
      "url": "https://perldoc.perl.org/perlvar"
    },
    {
      "title": "perldoc — perldata (variables)",
      "url": "https://perldoc.perl.org/perldata"
    }
  ]
}
---

# PERL-03-VARIABLES: Variables

## Introduction

Scalars, arrays, hashes, strict, and scoping. By the end of this lesson you will be able to: Declare the three variable sigils; Use strict and warnings; Distinguish my from our.

## Key Concepts

### 1. Declare the three variable sigils

Target: Declare the three variable sigils. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```perl
# Three main variable types
use strict;
use warnings;

my $scalar = "one";        # $
my @array = (1, 2, 3);     # @
my %hash = (key => "value");  # %
print "$scalar @array $hash{key}\n";

```
### 2. Use strict and warnings

Target: Use strict and warnings. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```perl
# strict and warnings catch common mistakes
use strict;
use warnings;

my $name = "Ada";
print "Hello, $name\n";
# Unquoted bareword or typos would be caught by strict

```
### 3. Distinguish my from our

Target: Distinguish my from our. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```perl
# my declares lexical variables; scope is the enclosing block
use strict;
use warnings;

{
    my $inner = "temporary";
    print "$inner\n";
}
# print "$inner\n";  # would fail — out of scope
print "scoped variables vanish at block end\n";

```
### 4. Declare the three variable sigils

Target: Declare the three variable sigils. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```perl
# Our vs my: package vs lexical scope
use strict;
use warnings;

our $global = "package-wide";
{
    my $lexical = "block-only";
    print "$global $lexical\n";
}
print "$global\n";

```

## Practice Questions

1. What is the key idea behind "Variables"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables"
1. "Provide advanced patterns and performance considerations for Variables"

## Key Takeaways

- Master the core ideas of Variables through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
