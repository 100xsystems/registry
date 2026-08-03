#!/usr/bin/env python3
"""Generate the 21-lesson Perl curriculum at Python/JS/Java depth.
Uses the shared gen_lib template. Exact refs from perldoc.perl.org.
Each lesson has 4 sub-topics, each with its OWN distinct code sample.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from gen_lib import main as run_gen  # noqa: E402

LANGUAGE = 'perl'

BASE = os.path.join(os.path.dirname(__file__), '..', '..', 'static-data', 'knowledge', 'languages', 'perl')

CODE = {
    1: [
        '''# Your first Perl program
use strict;
use warnings;

print "Hello, 100X Systems!\\n";
# Run with: perl hello.pl
''',
        '''# Perl's philosophy: TMTOWTDI — There's More Than One Way To Do It
use strict;
use warnings;

print "Hello\\n", "World\\n";
print("Parenthesized call\\n");
print join(" ", "Hello", "World"), "\\n";
''',
        '''# Running Perl in different modes
# perl script.pl          -> run a file
# perl -e 'print "hi"'    -> one-liner
# perl -ne 'print if /x/' -> line-by-line mode
use strict;
use warnings;
print "Perl is everywhere in sysadmin scripts\\n";
''',
        '''# The shebang line and execution bit
#!/usr/bin/perl
use strict;
use warnings;
# chmod +x script.pl; ./script.pl
print "Shebang scripts run directly\\n";
''',
    ],
    2: [
        '''# Scalar values: numbers and strings
use strict;
use warnings;

my $int = 42;
my $float = 3.14;
my $str = "hello";
my $bool = 1;
print "$int $float $str $bool\\n";
''',
        '''# Perl auto-converts between numbers and strings
use strict;
use warnings;

my $x = "3";
my $y = 4;
print $x + $y, "\\n";      # 7 — numeric context
print $x . $y, "\\n";      # "34" — string context
''',
        '''# Undef and defined()
use strict;
use warnings;

my $x;                     # undef
print "defined\\n" if defined $x;
print "undef\\n" unless defined $x;
my $y = $x // "default";   # defined-or operator
print "$y\\n";              # default
''',
        '''# Numeric and string comparison operators
use strict;
use warnings;

my $n = 10;
my $s = "10";
print "numeric eq\\n" if $n == $s;
print "string eq\\n" if $n eq $s;
print "compare: ", $n <=> 20, "\\n";   # -1
''',
    ],
    3: [
        '''# Three main variable types
use strict;
use warnings;

my $scalar = "one";        # $
my @array = (1, 2, 3);     # @
my %hash = (key => "value");  # %
print "$scalar @array $hash{key}\\n";
''',
        '''# strict and warnings catch common mistakes
use strict;
use warnings;

my $name = "Ada";
print "Hello, $name\\n";
# Unquoted bareword or typos would be caught by strict
''',
        '''# my declares lexical variables; scope is the enclosing block
use strict;
use warnings;

{
    my $inner = "temporary";
    print "$inner\\n";
}
# print "$inner\\n";  # would fail — out of scope
print "scoped variables vanish at block end\\n";
''',
        '''# Our vs my: package vs lexical scope
use strict;
use warnings;

our $global = "package-wide";
{
    my $lexical = "block-only";
    print "$global $lexical\\n";
}
print "$global\\n";
''',
    ],
    4: [
        '''# Arithmetic operators
use strict;
use warnings;

my $x = 7;
print $x + 3, "\\n";       # 10
print $x - 2, "\\n";       # 5
print $x * 2, "\\n";       # 14
print $x / 2, "\\n";       # 3.5
print $x % 4, "\\n";       # 3
print $x ** 2, "\\n";      # 49 — exponentiation
''',
        '''# Auto-increment and decrement
use strict;
use warnings;

my $count = 0;
$count++;                  # post-increment
++$count;                  # pre-increment
print "$count\\n";          # 2
$count--;
print "$count\\n";          # 1
''',
        '''# String operators: concatenation and repetition
use strict;
use warnings;

my $greeting = "Hello" . " " . "World";
my $line = "-" x 10;
print "$greeting\\n";
print "$line\\n";
''',
        '''# Assignment operators
use strict;
use warnings;

my $n = 10;
$n += 5;                   # 15
$n -= 3;                   # 12
$n *= 2;                   # 24
$n /= 4;                   # 6
print "$n\\n";
''',
    ],
    5: [
        '''# if / elsif / else
use strict;
use warnings;

my $score = 92;
if ($score >= 90) {
    print "A\\n";
} elsif ($score >= 80) {
    print "B\\n";
} else {
    print "C\\n";
}
''',
        '''# unless and statement modifiers
use strict;
use warnings;

my $debug = 0;
print "debug on\\n" if $debug;
print "not debugging\\n" unless $debug;
print "one-liner if\\n" if 1 > 0;
''',
        '''# The ternary operator
use strict;
use warnings;

my $age = 20;
my $status = $age >= 18 ? "adult" : "minor";
print "$status\\n";
''',
        '''# Logical operators with short-circuiting
use strict;
use warnings;

my $x = 0;
my $y = 5;
print "both true\\n" if $x && $y;       # false — x is falsy
print "x or y\\n" if $x || $y;          # true
my $z = $x || "fallback";
print "$z\\n";                          # fallback
''',
    ],
    6: [
        '''# for loops
use strict;
use warnings;

for (my $i = 0; $i < 5; $i++) {
    print "$i ";
}
print "\\n";
''',
        '''# foreach over a list
use strict;
use warnings;

my @fruits = ("apple", "banana", "cherry");
foreach my $fruit (@fruits) {
    print "$fruit ";
}
print "\\n";
''',
        '''# while loops
use strict;
use warnings;

my $n = 0;
while ($n < 5) {
    print "$n ";
    $n++;
}
print "\\n";
''',
        '''# do-while and loop control
use strict;
use warnings;

my $i = 0;
while ($i < 10) {
    $i++;
    next if $i == 3;       # skip 3
    last if $i == 6;       # stop at 6
    print "$i ";
}
print "\\n";                # 1 2 4 5
''',
    ],
    7: [
        '''# Arrays: indexing and assignment
use strict;
use warnings;

my @nums = (10, 20, 30);
print $nums[0], "\\n";      # 10
print $nums[-1], "\\n";     # 30 — negative index
$nums[1] = 99;
print "@nums\\n";           # 10 99 30
''',
        '''# Slicing arrays
use strict;
use warnings;

my @nums = (1, 2, 3, 4, 5);
my @slice = @nums[1..3];
print "@slice\\n";          # 2 3 4
my @every_other = @nums[0, 2, 4];
print "@every_other\\n";    # 1 3 5
''',
        '''# push, pop, shift, unshift
use strict;
use warnings;

my @stack = ();
push @stack, 1, 2, 3;
my $top = pop @stack;      # 3
unshift @stack, 0;
my $first = shift @stack;  # 0
print "@stack\\n";          # 1 2
''',
        '''# Array functions: sort, reverse, scalar
use strict;
use warnings;

my @nums = (5, 2, 8, 1);
my @sorted = sort { $a <=> $b } @nums;
my @reversed = reverse @sorted;
print "@sorted\\n";         # 1 2 5 8
print "@reversed\\n";       # 8 5 2 1
print scalar @nums, "\\n";  # 4 — count
''',
    ],
    8: [
        '''# Hashes: key-value pairs
use strict;
use warnings;

my %ages = (Ada => 36, Grace => 85);
print "$ages{Ada}\\n";      # 36
$ages{Linus} = 55;
print "$ages{Linus}\\n";    # 55
''',
        '''# Accessing and checking hash keys
use strict;
use warnings;

my %config = (host => "localhost", port => 8080);
print "has host\\n" if exists $config{host};
delete $config{port};
print "port gone\\n" unless exists $config{port};
''',
        '''# keys, values, and each
use strict;
use warnings;

my %score = (a => 90, b => 80, c => 70);
my @names = keys %score;
my @vals = values %score;
print scalar @names, " keys\\n";
print "total: ", $score{a} + $score{b} + $score{c}, "\\n";
''',
        '''# Iterating hashes
use strict;
use warnings;

my %fruit_color = (apple => "red", banana => "yellow");
while (my ($fruit, $color) = each %fruit_color) {
    print "$fruit is $color\\n";
}
''',
    ],
    9: [
        '''# Subroutines: declaration and call
use strict;
use warnings;

sub greet {
    my ($name) = @_;
    return "Hello, $name!";
}

print greet("Perl"), "\\n";
''',
        '''# @_ is the argument array
use strict;
use warnings;

sub add {
    my ($a, $b) = @_;
    return $a + $b;
}

print add(2, 3), "\\n";     # 5
print add(10, 20), "\\n";   # 30
''',
        '''# Default arguments with defined-or
use strict;
use warnings;

sub config {
    my ($key, $default) = @_;
    $default //= "unknown";
    return "$key=$default";
}

print config("host"), "\\n";
print config("port", 8080), "\\n";
''',
        '''# Context awareness with wantarray
use strict;
use warnings;

sub list_or_scalar {
    my @vals = (1, 2, 3);
    return wantarray ? @vals : scalar @vals;
}

my @list = list_or_scalar();
my $count = list_or_scalar();
print "@list\\n";           # 1 2 3
print "$count\\n";          # 3
''',
    ],
    10: [
        '''# Matching with =~
use strict;
use warnings;

my $text = "The quick brown fox";
print "has fox\\n" if $text =~ /fox/;
print "has cat\\n" if $text =~ /cat/;
''',
        '''# Capturing groups
use strict;
use warnings;

my $email = "ada@example.com";
if ($email =~ /^(.+)@(.+)$/) {
    print "user: $1\\n";
    print "domain: $2\\n";
}
''',
        '''# Substitution with s///
use strict;
use warnings;

my $msg = "Hello World";
$msg =~ s/World/Perl/;
print "$msg\\n";            # Hello Perl
$msg =~ s/Perl/Perl!/;
print "$msg\\n";            # Hello Perl!
''',
        '''# split and join
use strict;
use warnings;

my $csv = "a,b,c";
my @parts = split /,/, $csv;
print "@parts\\n";          # a b c
my $rejoined = join "-", @parts;
print "$rejoined\\n";       # a-b-c
''',
    ],
    11: [
        '''# Opening and reading a file
use strict;
use warnings;

open my $fh, "<", "data.txt" or die "Cannot open: $!";
while (my $line = <$fh>) {
    chomp $line;
    print "read: $line\\n";
}
close $fh;
''',
        '''# Writing to a file
use strict;
use warnings;

open my $out, ">", "out.txt" or die "Cannot write: $!";
print $out "line one\\n";
print $out "line two\\n";
close $out;
print "wrote file\\n";
''',
        '''# Reading all lines at once
use strict;
use warnings;

my @lines = <STDIN>;
print scalar @lines, " lines read\\n";
''',
        '''# The diamond operator <ARGV> reads from files or STDIN
use strict;
use warnings;

# perl script.pl file1.txt file2.txt
while (<>) {
    chomp;
    print "got: $_\\n";
}
''',
    ],
    12: [
        '''# References: scalars, arrays, and hashes
use strict;
use warnings;

my $scalar_ref = \\"value";
my @array = (1, 2, 3);
my $array_ref = \\@array;
my %hash = (a => 1);
my $hash_ref = \\%hash;

print $$scalar_ref, "\\n";        # value
print $array_ref->[0], "\\n";     # 1
print $hash_ref->{a}, "\\n";      # 1
''',
        '''# Anonymous references
use strict;
use warnings;

my $arr = [1, 2, 3];
my $hash = {name => "Ada", age => 36};
print $arr->[2], "\\n";           # 3
print $hash->{name}, "\\n";       # Ada
''',
        '''# Array of arrays (2D structures)
use strict;
use warnings;

my $matrix = [
    [1, 2],
    [3, 4],
];
print $matrix->[1][0], "\\n";     # 3
$matrix->[0][1] = 99;
print $matrix->[0][1], "\\n";     # 99
''',
        '''# Hash of hashes
use strict;
use warnings;

my $people = {
    Ada => {age => 36, lang => "Ada"},
    Grace => {age => 85, lang => "COBOL"},
};
print $people->{Grace}{lang}, "\\n";   # COBOL
''',
    ],
    13: [
        '''# Building nested structures
use strict;
use warnings;

my @rows = ();
for my $i (0..2) {
    my @row = ();
    for my $j (0..2) {
        push @row, $i * 10 + $j;
    }
    push @rows, \\@row;
}
print $rows[2][2], "\\n";          # 22
''',
        '''# Passing references to functions
use strict;
use warnings;

sub total {
    my ($arr_ref) = @_;
    my $sum = 0;
    $sum += $_ for @$arr_ref;
    return $sum;
}

my @nums = (1, 2, 3, 4, 5);
print total(\\@nums), "\\n";        # 15
''',
        '''# Deep copies vs shallow references
use strict;
use warnings;

my @orig = (1, 2, 3);
my $alias = \\@orig;
my @copy = @orig;                  # shallow copy of values

$alias->[0] = 99;                  # mutates @orig
print "@orig\\n";                   # 99 2 3
print "@copy\\n";                   # 1 2 3
''',
        '''# Walking a nested hash
use strict;
use warnings;

my $config = {
    db => {host => "localhost", pool => 10},
    cache => {ttl => 300},
};
for my $section (keys %$config) {
    my $opts = $config->{$section};
    print "$section: ", join(",", keys %$opts), "\\n";
}
''',
    ],
    14: [
        '''# chomp removes trailing newline
use strict;
use warnings;

my $line = "hello\\n";
chomp $line;
print "[$line]\\n";         # [hello]
''',
        '''# Case conversion and substring functions
use strict;
use warnings;

my $s = "Hello World";
print uc $s, "\\n";         # HELLO WORLD
print lc $s, "\\n";         # hello world
print substr($s, 0, 5), "\\n";  # Hello
print index($s, "World"), "\\n";  # 6
''',
        '''# sprintf for formatted output
use strict;
use warnings;

my $name = "Ada";
my $age = 36;
printf "%s is %d years old\\n", $name, $age;
my $formatted = sprintf("%04d", 42);
print "$formatted\\n";      # 0042
''',
        '''# length and regex-based string work
use strict;
use warnings;

my $word = "perl";
print length $word, "\\n";  # 4
my $upper = ucfirst $word;
print "$upper\\n";          # Perl
my $count = () = "a1b2c3" =~ /[0-9]/g;
print "$count digits\\n";   # 3
''',
    ],
    15: [
        '''# die and warn
use strict;
use warnings;

my $file = "missing.txt";
# open my $fh, "<", $file or die "Cannot open $file: $!";
warn "trying to open $file\\n";
print "continuing after warn\\n";
''',
        '''# eval to catch fatal errors
use strict;
use warnings;

eval {
    die "something failed";
};
if ($@) {
    print "caught: $@";
}
print "program survived\\n";
''',
        '''# The $@ variable holds the exception
use strict;
use warnings;

sub risky {
    die "boom";
}

eval { risky() };
print "error was: $@" if $@;
''',
        '''# Localized error handling and cleanup
use strict;
use warnings;

my $cleanup_done = 0;
eval {
    die "error inside eval";
};
$cleanup_done = 1 if $@;
print "cleanup: $cleanup_done\\n";
''',
    ],
    16: [
        '''# Loading modules
use strict;
use warnings;

use strict;
use warnings;
use List::Util qw(sum max);

my @nums = (1, 2, 3, 4);
print sum(@nums), "\\n";    # 10
print max(@nums), "\\n";    # 4
''',
        '''# require loads a module at runtime
use strict;
use warnings;

require List::Util;
my @nums = (5, 9, 1);
print List::Util::max(@nums), "\\n";   # 9
''',
        '''# Defining a package
use strict;
use warnings;

package Greeter;
sub hello {
    my ($name) = @_;
    return "Hello, $name!";
}
1;

package main;
print Greeter::hello("Perl"), "\\n";
''',
        '''# Exporting functions with Exporter
use strict;
use warnings;

# MyUtils.pm:
# package MyUtils;
# use Exporter qw(import);
# our @EXPORT_OK = qw(double);
# sub double { $_[0] * 2 }
# 1;
# use MyUtils qw(double);
print "modules are the unit of reuse in Perl\\n";
''',
    ],
    17: [
        '''# Object-oriented Perl with bless
use strict;
use warnings;

package Point;
sub new {
    my ($class, $x, $y) = @_;
    my $self = {x => $x, y => $y};
    bless $self, $class;
    return $self;
}
sub show {
    my ($self) = @_;
    return "($self->{x}, $self->{y})";
}

my $p = Point->new(1, 2);
print $p->show, "\\n";      # (1, 2)
''',
        '''# Methods and accessors
use strict;
use warnings;

package Counter;
sub new { bless {value => 0}, shift }
sub increment { $_[0]->{value}++ }
sub value { $_[0]->{value} }

my $c = Counter->new;
$c->increment;
$c->increment;
print $c->value, "\\n";     # 2
''',
        '''# Inheritance with @ISA or parent
use strict;
use warnings;

package Animal;
sub speak { "generic animal sound" }

package Dog;
use parent -norequire, "Animal";
sub speak { "Woof!" }

print Dog->speak, "\\n";    # Woof!
print Animal->speak, "\\n"; # generic animal sound
''',
        '''# Modern OO with Moo/Moose
use strict;
use warnings;

# package Person;
# use Moo;
# has name => (is => "ro");
# has age  => (is => "rw");
# sub greeting { "Hi, I am " . $_[0]->name }
# 1;
print "Moo and Moose provide modern OO on CPAN\\n";
''',
    ],
    18: [
        '''# Scalar and list context
use strict;
use warnings;

my @array = (1, 2, 3, 4);
my $count = @array;        # scalar context — count
my @copy = @array;         # list context — elements
print "$count\\n";          # 4
print "@copy\\n";           # 1 2 3 4
''',
        '''# Context affects how builtins behave
use strict;
use warnings;

my @sorted = sort (3, 1, 2);      # list context
my $last = (sort (3, 1, 2))[0];   # first element
print "@sorted\\n";               # 1 2 3
print "$last\\n";                 # 1
''',
        '''# Forcing context
use strict;
use warnings;

my @items = (5, 6, 7);
my $total = 0;
$total += $_ for @items;
print scalar(@items), " items, sum $total\\n";
''',
        '''# void context and side effects
use strict;
use warnings;

my @nums = (1, 2, 3);
@nums = sort { $b <=> $a } @nums;   # void-ish assignment
print "@nums\\n";                    # 3 2 1
''',
    ],
    19: [
        '''# CPAN: the Comprehensive Perl Archive Network
# cpan Module::Name          -> install
# cpanm Module::Name         -> fast installer
# perldoc Module::Name       -> documentation
print "CPAN hosts over 200,000 modules\\n";
''',
        '''# Common modules: List::Util, Scalar::Util
use strict;
use warnings;

use List::Util qw(any first);
use Scalar::Util qw(looks_like_number);

my @nums = (1, 2, 3);
print "has even\\n" if any { $_ % 2 == 0 } @nums;
print "first: ", first { $_ > 1 } @nums, "\\n";   # 2
print looks_like_number("42") ? "numeric\\n" : "text\\n";
''',
        '''# Text processing with Perl one-liners
# perl -pe 's/old/new/g' file.txt
# perl -ne 'print if /pattern/' file.txt
# perl -a -F, -n -e 'print $F[1]' file.csv
print "one-liners power the Unix toolbox\\n";
''',
        '''# perldoc is your best friend
# perldoc perl            -> overview
# perldoc perlfunc        -> all functions
# perldoc -f split        -> specific function
# perldoc perlre          -> regex reference
print "learn.perl.org has interactive tutorials\\n";
''',
    ],
    20: [
        '''# Unicode handling with utf8
use strict;
use warnings;
use utf8;
use Encode;

my $text = "héllo wörld";
print "char count: ", length($text), "\\n";
my $bytes = encode("UTF-8", $text);
print "byte count: ", length($bytes), "\\n";
''',
        '''# Reading UTF-8 from files
use strict;
use warnings;
use utf8;
use open ':std', ':encoding(UTF-8)';

# open my $fh, "<:encoding(UTF-8)", "file.txt" or die $!;
print "open with :encoding(UTF-8) layer\\n";
''',
        '''# Decoding external input
use strict;
use warnings;
use Encode qw(decode encode is_utf8);

my $bytes = "\\xc3\\xa9";      # é (U+00E9) encoded as UTF-8 bytes
my $decoded = decode("UTF-8", $bytes);
print "decoded: $decoded\\n";
''',
        '''# Unicode properties in regex
use strict;
use warnings;
use utf8;

my $greek = "αβγ";
print "greek letters\\n" if $greek =~ /[\\p{Greek}]/;
print "matched letter\\n" if $greek =~ /\\p{L}+/;
''',
    ],
    21: [
        '''# Web development with Mojolicious
use strict;
use warnings;

# use Mojolicious::Lite;
# get "/" => sub { shift->render(text => "Hello") };
# app->start;
print "Mojolicious is a modern Perl web framework\\n";
''',
        '''# Database access with DBI
use strict;
use warnings;

# use DBI;
# my $dbh = DBI->connect("dbi:SQLite:dbname=test.db", "", "");
# my $sth = $dbh->prepare("SELECT * FROM users");
# $sth->execute();
print "DBI speaks to every major database\\n";
''',
        '''# Testing with Test::More
use strict;
use warnings;
use Test::More;

sub double { $_[0] * 2 }
is(double(2), 4, "doubles 2 to 4");
is(double(0), 0, "doubles 0 to 0");

done_testing();
''',
        '''# Next steps: advanced Perl topics
# 1. Moose/Moo object systems in depth
# 2. Async with AnyEvent / IO::Async
# 3. Functional style with higher-order functions
# 4. Perl 5.40+ features: signatures, native arrays
print "You now have a complete foundation in Perl\\n";
''',
    ],
}

LESSONS = [
    dict(
        slug='perl-01-getting-started',
        title='Getting Started with Perl',
        desc='Hello world, TMTOWTDI, and running Perl code.',
        diff='beginner',
        dur=20,
        objs=[
            'Run Perl scripts and one-liners',
            'Explain the TMTOWTDI philosophy',
            'Use print for output',
        ],
        prereq=[],
        refs=[dict(title='Perl Documentation — perldoc', url='https://perldoc.perl.org/'),
              dict(title='Learn Perl — Official Tutorials', url='https://learn.perl.org/'),
              dict(title='Perl.com — Articles', url='https://www.perl.com/')]),
    dict(
        slug='perl-02-values-types',
        title='Values and Types',
        desc='Scalars, auto-conversion, undef, and comparisons.',
        diff='beginner',
        dur=25,
        objs=[
            'Create scalar values',
            'Explain automatic number/string conversion',
            'Use defined and the // operator',
        ],
        prereq=['perl-01-getting-started'],
        refs=[dict(title='perldoc — perldata', url='https://perldoc.perl.org/perldata'),
              dict(title='perldoc — perlsyn (values)', url='https://perldoc.perl.org/perlsyn')]),
    dict(
        slug='perl-03-variables',
        title='Variables',
        desc='Scalars, arrays, hashes, strict, and scoping.',
        diff='beginner',
        dur=25,
        objs=[
            'Declare the three variable sigils',
            'Use strict and warnings',
            'Distinguish my from our',
        ],
        prereq=['perl-02-values-types'],
        refs=[dict(title='perldoc — perlvar', url='https://perldoc.perl.org/perlvar'),
              dict(title='perldoc — perldata (variables)', url='https://perldoc.perl.org/perldata')]),
    dict(
        slug='perl-04-operators',
        title='Operators',
        desc='Arithmetic, string, assignment, and increment operators.',
        diff='beginner',
        dur=25,
        objs=[
            'Use arithmetic operators',
            'Concatenate and repeat strings',
            'Apply compound assignment',
        ],
        prereq=['perl-02-values-types'],
        refs=[dict(title='perldoc — perlop', url='https://perldoc.perl.org/perlop')]),
    dict(
        slug='perl-05-control-flow',
        title='Control Flow',
        desc='if/elsif, unless, ternary, and short-circuit logic.',
        diff='beginner',
        dur=25,
        objs=[
            'Write conditional branches',
            'Use statement modifiers',
            'Apply the ternary operator',
        ],
        prereq=['perl-01-getting-started'],
        refs=[dict(title='perldoc — perlsyn (conditionals)', url='https://perldoc.perl.org/perlsyn#Compound-Statements')]),
    dict(
        slug='perl-06-loops',
        title='Loops',
        desc='for, foreach, while, and loop control keywords.',
        diff='beginner',
        dur=25,
        objs=[
            'Iterate with for and foreach',
            'Loop with while loops',
            'Control loops with next and last',
        ],
        prereq=['perl-05-control-flow'],
        refs=[dict(title='perldoc — perlsyn (loops)', url='https://perldoc.perl.org/perlsyn#Compound-Statements'),
              dict(title='perldoc — perlsyn (Loop Control)', url='https://perldoc.perl.org/perlsyn#Loop-Control')]),
    dict(
        slug='perl-07-arrays',
        title='Lists and Arrays',
        desc='Indexing, slicing, stack ops, and array functions.',
        diff='beginner',
        dur=30,
        objs=[
            'Index and slice arrays',
            'Use push, pop, shift, unshift',
            'Sort, reverse, and count arrays',
        ],
        prereq=['perl-03-variables'],
        refs=[dict(title='perldoc — perldata (arrays)', url='https://perldoc.perl.org/perldata#List-value-constructors'),
              dict(title='perldoc — perlfunc (push/pop)', url='https://perldoc.perl.org/perlfunc')]),
    dict(
        slug='perl-08-hashes',
        title='Hashes',
        desc='Key-value pairs, exists, delete, and iteration.',
        diff='beginner',
        dur=30,
        objs=[
            'Create and update hashes',
            'Check keys with exists',
            'Iterate with each and keys',
        ],
        prereq=['perl-03-variables'],
        refs=[dict(title='perldoc — perldata (hashes)', url='https://perldoc.perl.org/perldata#Hash-variables'),
              dict(title='perldoc — perlfunc (keys/each)', url='https://perldoc.perl.org/perlfunc')]),
    dict(
        slug='perl-09-functions',
        title='Functions',
        desc='Subroutines, @_, return, and context.',
        diff='beginner',
        dur=30,
        objs=[
            'Define and call subroutines',
            'Access arguments via @_',
            'Return values and defaults',
        ],
        prereq=['perl-05-control-flow'],
        refs=[dict(title='perldoc — perlsub', url='https://perldoc.perl.org/perlsub'),
              dict(title='perldoc — perlfunc', url='https://perldoc.perl.org/perlfunc')]),
    dict(
        slug='perl-10-regular-expressions',
        title='Regular Expressions',
        desc='Matching, capturing, substitution, split, and join.',
        diff='intermediate',
        dur=35,
        objs=[
            'Match patterns with =~',
            'Capture groups with $1, $2',
            'Substitute with s///',
        ],
        prereq=['perl-06-loops'],
        refs=[dict(title='perldoc — perlre', url='https://perldoc.perl.org/perlre'),
              dict(title='perldoc — perlretut (tutorial)', url='https://perldoc.perl.org/perlretut')]),
    dict(
        slug='perl-11-file-io',
        title='File I/O',
        desc='Opening files, reading lines, and the diamond operator.',
        diff='intermediate',
        dur=30,
        objs=[
            'Open files with three-arg open',
            'Read lines with the <> operator',
            'Write to filehandles',
        ],
        prereq=['perl-06-loops'],
        refs=[dict(title='perldoc — perlopentut', url='https://perldoc.perl.org/perlopentut'),
              dict(title='perldoc — perlfunc (open)', url='https://perldoc.perl.org/perlfunc#open')]),
    dict(
        slug='perl-12-references',
        title='References',
        desc='Scalar, array, hash references, and dereferencing.',
        diff='intermediate',
        dur=35,
        objs=[
            'Create references with backslash',
            'Dereference with arrow and $$',
            'Build anonymous structures',
        ],
        prereq=['perl-08-hashes'],
        refs=[dict(title='perldoc — perlreftut', url='https://perldoc.perl.org/perlreftut'),
              dict(title='perldoc — perlref', url='https://perldoc.perl.org/perlref')]),
    dict(
        slug='perl-13-data-structures',
        title='Nested Data Structures',
        desc='Arrays of arrays, hashes of hashes, and traversal.',
        diff='intermediate',
        dur=35,
        objs=[
            'Build 2D structures with references',
            'Pass references to functions',
            'Traverse nested hashes',
        ],
        prereq=['perl-12-references'],
        refs=[dict(title='perldoc — perldsc', url='https://perldoc.perl.org/perldsc'),
              dict(title='perldoc — perllol', url='https://perldoc.perl.org/perllol')]),
    dict(
        slug='perl-14-strings',
        title='String Manipulation',
        desc='chomp, case, substr, index, and sprintf.',
        diff='intermediate',
        dur=25,
        objs=[
            'Trim newlines with chomp',
            'Transform case and substrings',
            'Format output with sprintf',
        ],
        prereq=['perl-10-regular-expressions'],
        refs=[dict(title='perldoc — perlfunc (chomp/substr)', url='https://perldoc.perl.org/perlfunc'),
              dict(title='perldoc — perlsyn (quotes)', url='https://perldoc.perl.org/perlsyn')]),
    dict(
        slug='perl-15-error-handling',
        title='Error Handling',
        desc='die, warn, eval, and the $@ variable.',
        diff='intermediate',
        dur=30,
        objs=[
            'Raise errors with die',
            'Emit warnings with warn',
            'Catch errors with eval',
        ],
        prereq=['perl-05-control-flow'],
        refs=[dict(title='perldoc — perlsyn (eval)', url='https://perldoc.perl.org/perlsyn#Statement-Modifiers'),
              dict(title='perldoc — perlfunc (die/eval)', url='https://perldoc.perl.org/perlfunc')]),
    dict(
        slug='perl-16-modules',
        title='Modules and Packages',
        desc='use, require, package, and the Exporter.',
        diff='intermediate',
        dur=30,
        objs=[
            'Load modules with use and require',
            'Define packages',
            'Export functions with Exporter',
        ],
        prereq=['perl-09-functions'],
        refs=[dict(title='perldoc — perlmod', url='https://perldoc.perl.org/perlmod'),
              dict(title='perldoc — perlmodlib', url='https://perldoc.perl.org/perlmodlib')]),
    dict(
        slug='perl-17-oop',
        title='Object-Oriented Perl',
        desc='bless, methods, inheritance, and modern OO.',
        diff='intermediate',
        dur=35,
        objs=[
            'Create objects with bless',
            'Write methods and accessors',
            'Use inheritance with parent',
        ],
        prereq=['perl-12-references'],
        refs=[dict(title='perldoc — perlobj', url='https://perldoc.perl.org/perlobj'),
              dict(title='perldoc — perlootut (OO tutorial)', url='https://perldoc.perl.org/perlootut'),
              dict(title='Moo — Modern OO on CPAN', url='https://metacpan.org/pod/Moo')]),
    dict(
        slug='perl-18-context',
        title='Context',
        desc='Scalar vs list context and wantarray.',
        diff='expert',
        dur=30,
        objs=[
            'Explain scalar and list context',
            'See how builtins change behavior',
            'Use wantarray for context-aware functions',
        ],
        prereq=['perl-09-functions'],
        refs=[dict(title='perldoc — perldata (context)', url='https://perldoc.perl.org/perldata#Scalar-values'),
              dict(title='perldoc — perlfunc (wantarray)', url='https://perldoc.perl.org/perlfunc#wantarray')]),
    dict(
        slug='perl-19-cpan-tooling',
        title='CPAN and Tooling',
        desc='The module ecosystem, installers, and perldoc.',
        diff='intermediate',
        dur=25,
        objs=[
            'Install modules with cpan and cpanm',
            'Use common utility modules',
            'Write one-liners',
        ],
        prereq=['perl-16-modules'],
        refs=[dict(title='MetaCPAN — Module Search', url='https://metacpan.org/'),
              dict(title='CPAN — Official Site', url='https://www.cpan.org/'),
              dict(title='Learn Perl — CPAN section', url='https://learn.perl.org/docs/')]),
    dict(
        slug='perl-20-unicode',
        title='Unicode and Encoding',
        desc='utf8, Encode, file layers, and character properties.',
        diff='expert',
        dur=30,
        objs=[
            'Enable utf8 in scripts',
            'Encode and decode strings',
            'Use Unicode properties in regex',
        ],
        prereq=['perl-10-regular-expressions'],
        refs=[dict(title='perldoc — perlunicode', url='https://perldoc.perl.org/perlunicode'),
              dict(title='perldoc — Encode module', url='https://perldoc.perl.org/Encode')]),
    dict(
        slug='perl-21-ecosystem-next-steps',
        title='Ecosystem and Next Steps',
        desc='Mojolicious, DBI, testing, and the road ahead.',
        diff='intermediate',
        dur=20,
        objs=[
            'Name key frameworks and modules',
            'Write tests with Test::More',
            'Identify next advanced topics',
        ],
        prereq=['perl-19-cpan-tooling'],
        refs=[dict(title='Mojolicious — Web Framework', url='https://mojolicious.org/'),
              dict(title='DBI — Database Interface', url='https://dbi.perl.org/'),
              dict(title='Perl Weekly — Newsletter', url='https://perlweekly.com/'),
              dict(title='Modern Perl — Free Book', url='https://modernperlbooks.com/')]),
]


if __name__ == '__main__':
    run_gen(LANGUAGE, 'perl', LESSONS, CODE, BASE)
