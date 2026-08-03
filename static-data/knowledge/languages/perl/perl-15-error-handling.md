---
{
  "title": "Error Handling",
  "description": "die, warn, eval, and the $@ variable.",
  "type": "lesson",
  "order": 15,
  "duration": "30 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Raise errors with die",
    "Emit warnings with warn",
    "Catch errors with eval"
  ],
  "knowledge_refs": [
    "perl/perl-15-error-handling"
  ],
  "prerequisites": [
    "perl-05-control-flow"
  ],
  "references": [
    {
      "title": "perldoc — perlsyn (eval)",
      "url": "https://perldoc.perl.org/perlsyn#Statement-Modifiers"
    },
    {
      "title": "perldoc — perlfunc (die/eval)",
      "url": "https://perldoc.perl.org/perlfunc"
    }
  ]
}
---

# PERL-15-ERROR-HANDLING: Error Handling

## Introduction

die, warn, eval, and the $@ variable. By the end of this lesson you will be able to: Raise errors with die; Emit warnings with warn; Catch errors with eval.

## Key Concepts

### 1. Raise errors with die

Target: Raise errors with die. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```perl
# die and warn
use strict;
use warnings;

my $file = "missing.txt";
# open my $fh, "<", $file or die "Cannot open $file: $!";
warn "trying to open $file\n";
print "continuing after warn\n";

```
### 2. Emit warnings with warn

Target: Emit warnings with warn. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```perl
# eval to catch fatal errors
use strict;
use warnings;

eval {
    die "something failed";
};
if ($@) {
    print "caught: $@";
}
print "program survived\n";

```
### 3. Catch errors with eval

Target: Catch errors with eval. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```perl
# The $@ variable holds the exception
use strict;
use warnings;

sub risky {
    die "boom";
}

eval { risky() };
print "error was: $@" if $@;

```
### 4. Raise errors with die

Target: Raise errors with die. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```perl
# Localized error handling and cleanup
use strict;
use warnings;

my $cleanup_done = 0;
eval {
    die "error inside eval";
};
$cleanup_done = 1 if $@;
print "cleanup: $cleanup_done\n";

```

## Practice Questions

1. What is the key idea behind "Error Handling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Error Handling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Error Handling"
1. "Provide advanced patterns and performance considerations for Error Handling"

## Key Takeaways

- Master the core ideas of Error Handling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
