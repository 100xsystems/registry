---
{
  "title": "Modules and Packages",
  "description": "use, require, package, and the Exporter.",
  "type": "lesson",
  "order": 16,
  "duration": "30 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Load modules with use and require",
    "Define packages",
    "Export functions with Exporter"
  ],
  "knowledge_refs": [
    "perl/perl-16-modules"
  ],
  "prerequisites": [
    "perl-09-functions"
  ],
  "references": [
    {
      "title": "perldoc — perlmod",
      "url": "https://perldoc.perl.org/perlmod"
    },
    {
      "title": "perldoc — perlmodlib",
      "url": "https://perldoc.perl.org/perlmodlib"
    }
  ]
}
---

# PERL-16-MODULES: Modules and Packages

## Introduction

use, require, package, and the Exporter. By the end of this lesson you will be able to: Load modules with use and require; Define packages; Export functions with Exporter.

## Key Concepts

### 1. Load modules with use and require

Target: Load modules with use and require. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```perl
# Loading modules
use strict;
use warnings;

use strict;
use warnings;
use List::Util qw(sum max);

my @nums = (1, 2, 3, 4);
print sum(@nums), "\n";    # 10
print max(@nums), "\n";    # 4

```
### 2. Define packages

Target: Define packages. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```perl
# require loads a module at runtime
use strict;
use warnings;

require List::Util;
my @nums = (5, 9, 1);
print List::Util::max(@nums), "\n";   # 9

```
### 3. Export functions with Exporter

Target: Export functions with Exporter. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```perl
# Defining a package
use strict;
use warnings;

package Greeter;
sub hello {
    my ($name) = @_;
    return "Hello, $name!";
}
1;

package main;
print Greeter::hello("Perl"), "\n";

```
### 4. Load modules with use and require

Target: Load modules with use and require. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```perl
# Exporting functions with Exporter
use strict;
use warnings;

# MyUtils.pm:
# package MyUtils;
# use Exporter qw(import);
# our @EXPORT_OK = qw(double);
# sub double { $_[0] * 2 }
# 1;
# use MyUtils qw(double);
print "modules are the unit of reuse in Perl\n";

```

## Practice Questions

1. What is the key idea behind "Modules and Packages"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Modules and Packages with analogies and real-world examples"
1. "Show me common mistakes beginners make with Modules and Packages"
1. "Provide advanced patterns and performance considerations for Modules and Packages"

## Key Takeaways

- Master the core ideas of Modules and Packages through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
