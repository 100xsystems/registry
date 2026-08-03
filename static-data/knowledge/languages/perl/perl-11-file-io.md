---
{
  "title": "File I/O",
  "description": "Opening files, reading lines, and the diamond operator.",
  "type": "lesson",
  "order": 11,
  "duration": "30 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Open files with three-arg open",
    "Read lines with the <> operator",
    "Write to filehandles"
  ],
  "knowledge_refs": [
    "perl/perl-11-file-io"
  ],
  "prerequisites": [
    "perl-06-loops"
  ],
  "references": [
    {
      "title": "perldoc — perlopentut",
      "url": "https://perldoc.perl.org/perlopentut"
    },
    {
      "title": "perldoc — perlfunc (open)",
      "url": "https://perldoc.perl.org/perlfunc#open"
    }
  ]
}
---

# PERL-11-FILE-IO: File I/O

## Introduction

Opening files, reading lines, and the diamond operator. By the end of this lesson you will be able to: Open files with three-arg open; Read lines with the <> operator; Write to filehandles.

## Key Concepts

### 1. Open files with three-arg open

Target: Open files with three-arg open. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```perl
# Opening and reading a file
use strict;
use warnings;

open my $fh, "<", "data.txt" or die "Cannot open: $!";
while (my $line = <$fh>) {
    chomp $line;
    print "read: $line\n";
}
close $fh;

```
### 2. Read lines with the <> operator

Target: Read lines with the <> operator. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```perl
# Writing to a file
use strict;
use warnings;

open my $out, ">", "out.txt" or die "Cannot write: $!";
print $out "line one\n";
print $out "line two\n";
close $out;
print "wrote file\n";

```
### 3. Write to filehandles

Target: Write to filehandles. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```perl
# Reading all lines at once
use strict;
use warnings;

my @lines = <STDIN>;
print scalar @lines, " lines read\n";

```
### 4. Open files with three-arg open

Target: Open files with three-arg open. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```perl
# The diamond operator <ARGV> reads from files or STDIN
use strict;
use warnings;

# perl script.pl file1.txt file2.txt
while (<>) {
    chomp;
    print "got: $_\n";
}

```

## Practice Questions

1. What is the key idea behind "File I/O"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain File I/O with analogies and real-world examples"
1. "Show me common mistakes beginners make with File I/O"
1. "Provide advanced patterns and performance considerations for File I/O"

## Key Takeaways

- Master the core ideas of File I/O through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
