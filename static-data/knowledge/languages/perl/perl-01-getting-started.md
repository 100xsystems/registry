---
{
  "title": "Getting Started with Perl",
  "description": "Hello world, TMTOWTDI, and running Perl code.",
  "type": "lesson",
  "order": 1,
  "duration": "20 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Run Perl scripts and one-liners",
    "Explain the TMTOWTDI philosophy",
    "Use print for output"
  ],
  "knowledge_refs": [
    "perl/perl-01-getting-started"
  ],
  "prerequisites": [],
  "references": [
    {
      "title": "Perl Documentation — perldoc",
      "url": "https://perldoc.perl.org/"
    },
    {
      "title": "Learn Perl — Official Tutorials",
      "url": "https://learn.perl.org/"
    },
    {
      "title": "Perl.com — Articles",
      "url": "https://www.perl.com/"
    }
  ]
}
---

# PERL-01-GETTING-STARTED: Getting Started with Perl

## Introduction

Hello world, TMTOWTDI, and running Perl code. By the end of this lesson you will be able to: Run Perl scripts and one-liners; Explain the TMTOWTDI philosophy; Use print for output.

## Key Concepts

### 1. Run Perl scripts and one-liners

Target: Run Perl scripts and one-liners. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```perl
# Your first Perl program
use strict;
use warnings;

print "Hello, 100X Systems!\n";
# Run with: perl hello.pl

```
### 2. Explain the TMTOWTDI philosophy

Target: Explain the TMTOWTDI philosophy. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```perl
# Perl's philosophy: TMTOWTDI — There's More Than One Way To Do It
use strict;
use warnings;

print "Hello\n", "World\n";
print("Parenthesized call\n");
print join(" ", "Hello", "World"), "\n";

```
### 3. Use print for output

Target: Use print for output. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```perl
# Running Perl in different modes
# perl script.pl          -> run a file
# perl -e 'print "hi"'    -> one-liner
# perl -ne 'print if /x/' -> line-by-line mode
use strict;
use warnings;
print "Perl is everywhere in sysadmin scripts\n";

```
### 4. Run Perl scripts and one-liners

Target: Run Perl scripts and one-liners. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```perl
# The shebang line and execution bit
#!/usr/bin/perl
use strict;
use warnings;
# chmod +x script.pl; ./script.pl
print "Shebang scripts run directly\n";

```

## Practice Questions

1. What is the key idea behind "Getting Started with Perl"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Perl with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Perl"
1. "Provide advanced patterns and performance considerations for Getting Started with Perl"

## Key Takeaways

- Master the core ideas of Getting Started with Perl through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
