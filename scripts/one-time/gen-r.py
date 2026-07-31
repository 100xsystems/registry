#!/usr/bin/env python3
"""Generate the 21-lesson R curriculum at Python/JS/Java depth.
Uses the shared gen_lib template. Exact refs from r-project.org / tidyverse.
Each lesson has 4 sub-topics, each with its OWN distinct code sample.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from gen_lib import main as run_gen  # noqa: E402

LANGUAGE = 'r'

BASE = os.path.join(os.path.dirname(__file__), '..', '..', 'static-data', 'knowledge', 'languages', 'r')

CODE = {
    1: [
        '''# Your first R program
print("Hello, 100X Systems!")

# Run with: Rscript hello.R  ->  [1] "Hello, 100X Systems!"
''',
        '''# The R console: RStudio IDE or the terminal
# Use <- for assignment (the R convention)
x <- 42
x               # prints the value
''',
        '''# R is vectorized: operations apply to whole vectors
numbers <- c(1, 2, 3, 4, 5)
print(numbers * 2)         # [1]  2  4  6  8 10
print(sum(numbers))        # [1] 15
''',
        '''# Scripts, the working directory, and projects
# setwd("/path/to/project")   # change working directory
# RStudio projects keep everything organized
print(getwd())             # current working directory
''',
    ],
    2: [
        '''# Core types: numeric, integer, character, logical
print(class(3.14))         # "numeric"
print(class(42L))          # "integer" (L suffix)
print(class("hello"))      # "character"
print(class(TRUE))         # "logical"
''',
        '''# typeof() gives the lower-level type
print(typeof(3.14))        # "double"
print(typeof("hi"))        # "character"
print(typeof(TRUE))        # "logical"
''',
        '''# NA, NULL, NaN, and Inf — R's special values
x <- NA                     # missing value
print(is.na(x))             # TRUE
print(is.null(NULL))        # TRUE
print(0 / 0)                # NaN
print(1 / 0)                # Inf
''',
        '''# Vectors hold one type; coercion happens automatically
mixed <- c(1, "two", 3)
print(mixed)                # "1" "two" "3" — everything became character
print(typeof(mixed))        # "character"
''',
    ],
    3: [
        '''# Assignment: <- is idiomatic, = also works
x <- 10
y = 20
print(x + y)                # 30
''',
        '''# Object names: letters, digits, dots, underscores
my_variable <- 1
my.var <- 2
print(my_variable + my.var) # 3
''',
        '''# Environment: ls() lists objects, rm() removes them
a <- 1
b <- 2
print(ls())                 # "a" "b"
rm(a)
print(exists("a"))          # FALSE
''',
        '''# Everything in R is an object — even functions
f <- function(x) x * 2
print(f)                    # prints the function body
print(is.function(f))       # TRUE
''',
    ],
    4: [
        '''# Arithmetic operators
print(7 %% 4)               # 3 — modulo
print(7 %/% 2)              # 3 — integer division
print(2^10)                 # 1024 — exponentiation
''',
        '''# Comparison operators
print(1 == 1)               # TRUE
print(1 != 2)               # TRUE
print("a" < "b")            # TRUE — lexicographic
''',
        '''# Logical operators: & and | are vectorized; && and || short-circuit
print(c(TRUE, FALSE) & c(TRUE, TRUE))    # TRUE FALSE
if (TRUE && 1 < 2) print("both true")
''',
        '''# Vectorized arithmetic is the R superpower
x <- c(1, 2, 3)
y <- c(10, 20, 30)
print(x + y)                # 11 22 33
print(x^2)                  # 1 4 9
''',
    ],
    5: [
        '''# Functions: last expression is the return value
square <- function(x) {
    x^2
}
print(square(5))            # 25
''',
        '''# Explicit return() and early exits
classify <- function(n) {
    if (n < 0) return("negative")
    if (n == 0) return("zero")
    "positive"
}
print(classify(-5))         # "negative"
print(classify(3))          # "positive"
''',
        '''# Default arguments
greet <- function(name = "world") {
    paste("Hello,", name, "!")
}
print(greet())              # "Hello, world !"
print(greet("R"))           # "Hello, R !"
''',
        '''# Anonymous functions and lapply
squares <- lapply(c(1, 2, 3), function(x) x^2)
print(unlist(squares))      # 1 4 9
''',
    ],
    6: [
        '''# Vectors: the fundamental data structure
v <- c(10, 20, 30, 40)
print(v[1])                 # 10 — indexing starts at 1!
print(v[2:3])               # 20 30
print(v[c(1, 4)])           # 10 40
''',
        '''# Named vectors
scores <- c(ada = 95, grace = 88, linus = 91)
print(scores["ada"])        # ada: 95
print(names(scores))        # "ada" "grace" "linus"
''',
        '''# Logical subsetting — the idiomatic R pattern
ages <- c(25, 40, 33, 60)
print(ages[ages > 30])      # 40 33 60
print(which(ages > 30))     # 2 3 4
''',
        '''# seq(), rep(), and colon operator
print(1:5)                  # 1 2 3 4 5
print(seq(1, 10, by = 2))   # 1 3 5 7 9
print(rep("x", 3))          # "x" "x" "x"
''',
    ],
    7: [
        '''# if / else if / else
grade <- function(score) {
    if (score >= 90) {
        "A"
    } else if (score >= 80) {
        "B"
    } else {
        "C"
    }
}
print(grade(95))            # "A"
''',
        '''# Vectorized conditionals: ifelse
ages <- c(10, 25, 60)
labels <- ifelse(ages >= 18, "adult", "minor")
print(labels)               # "minor" "adult" "adult"
''',
        '''# for loops over vectors
total <- 0
for (i in 1:5) {
    total <- total + i
}
print(total)                # 15
''',
        '''# while loops and next/break
n <- 0
while (n < 5) {
    n <- n + 1
    if (n == 3) next        # skip 3
    print(n)                # 1 2 4 5
}
''',
    ],
    8: [
        '''# Strings: paste, paste0, and sprintf
print(paste("Hello", "R"))          # "Hello R"
print(paste0("Hello", "R"))         # "HelloR"
print(sprintf("%s scored %d", "Ada", 95))  # "Ada scored 95"
''',
        '''# String manipulation: nchar, toupper, tolower
s <- "Hello, R"
print(nchar(s))             # 8
print(toupper(s))           # "HELLO, R"
print(tolower(s))           # "hello, r"
''',
        '''# substring, substr, strsplit
s <- "a-b-c"
print(strsplit(s, "-")[[1]])    # "a" "b" "c"
print(substr("abcdef", 2, 4))   # "bcd"
''',
        '''# Regular expressions: grep, gsub, grepl
text <- c("cat", "car", "dog")
print(grepl("ca", text))        # TRUE TRUE FALSE
print(gsub("a", "o", "banana")) # "bonono"
''',
    ],
    9: [
        '''# Lists: containers that can hold any type
lst <- list(name = "Ada", age = 36, scores = c(90, 95))
print(lst$name)             # "Ada"
print(lst[[3]])             # 90 95 — double bracket extracts
''',
        '''# Accessing lists: $, [[]], and []
lst <- list(a = 1, b = 2)
print(lst[["a"]])           # 1 — the element itself
print(lst["a"])             # list of length 1
''',
        '''# Matrices: two-dimensional arrays
m <- matrix(1:6, nrow = 2, ncol = 3)
print(m)
#      [,1] [,2] [,3]
# [1,]    1    3    5
# [2,]    2    4    6
print(m[1, 2])              # 3
''',
        '''# Data frames: the heart of data analysis
df <- data.frame(
    name = c("Ada", "Grace"),
    age = c(36, 85)
)
print(df$name)              # "Ada" "Grace"
print(df[1, ])              # first row
print(df[df$age > 40, ])    # filter rows
''',
    ],
    10: [
        '''# Factors: categorical variables with levels
sizes <- factor(c("S", "M", "L", "M"))
print(levels(sizes))        # "L" "M" "S"
print(table(sizes))         # counts per level
''',
        '''# Ordered factors preserve natural order
ratings <- factor(c("low", "high", "medium"),
                  levels = c("low", "medium", "high"),
                  ordered = TRUE)
print(ratings[2] > ratings[1])  # TRUE
''',
        '''# Dates and times: as.Date and POSIXct
d <- as.Date("2026-07-28")
print(d + 1)                # "2026-07-29"
print(format(d, "%A"))      # day of week
''',
        '''# Attributes: metadata attached to objects
v <- 1:3
attr(v, "my_note") <- "hello"
print(attributes(v))        # my_note attribute
''',
    ],
    11: [
        '''# apply family: apply, lapply, sapply, tapply
m <- matrix(1:6, nrow = 2)
print(apply(m, 1, sum))     # row sums: 9 12
print(apply(m, 2, sum))     # col sums: 3 7 11
''',
        '''# lapply returns a list; sapply simplifies
print(lapply(c(1, 2, 3), function(x) x^2))  # list
print(sapply(c(1, 2, 3), function(x) x^2))  # 1 4 9 (vector)
''',
        '''# tapply: group-wise operations
groups <- c("a", "a", "b", "b")
values <- c(1, 2, 10, 20)
print(tapply(values, groups, mean))  # a: 1.5, b: 15
''',
        '''# Reduce, Filter, and Map
nums <- c(1, 2, 3, 4, 5)
print(Filter(function(x) x %% 2 == 0, nums))   # 2 4
print(Reduce(`+`, nums))                       # 15
print(Map(function(x) x * 10, nums))           # list of 10 20 ...
''',
    ],
    12: [
        '''# Writing functions that reuse other functions
power <- function(base, exp = 2) {
    base^exp
}
print(power(3))             # 9
print(power(2, 10))         # 1024
''',
        '''# ... (dot-dot-dot): pass along extra arguments
wrapper <- function(..., prefix = "result:") {
    values <- list(...)
    paste(prefix, sum(unlist(values)))
}
print(wrapper(1, 2, 3))     # "result: 6"
''',
        '''# Closures: functions that remember their environment
make_counter <- function() {
    count <- 0
    function() {
        count <<- count + 1   # <<- assigns in the enclosing scope
        count
    }
}
counter <- make_counter()
print(counter())            # 1
print(counter())            # 2
''',
        '''# Lexical scoping: functions see their defining environment
x <- 10
f <- function() x + 5
print(f())                  # 15

y <- 1
g <- function() y
y <- 100
print(g())                  # 100 — lookup happens at call time
''',
    ],
    13: [
        '''# tidyverse: the modern R ecosystem
# install.packages("tidyverse")
# library(tidyverse)
# dplyr verbs: filter, select, mutate, arrange, summarize
print("tidyverse = ggplot2 + dplyr + tidyr + ...")
''',
        '''# dplyr pipeline with the pipe operator |>
data <- data.frame(name = c("Ada", "Grace", "Linus"),
                   age = c(36, 85, 55))
result <- data |>
    dplyr::filter(age > 40) |>
    dplyr::select(name)
print(result)               # Grace, Linus
''',
        '''# ggplot2: grammar of graphics
# library(ggplot2)
# ggplot(data, aes(x = age)) +
#   geom_histogram(bins = 10) +
#   labs(title = "Age distribution")
print("ggplot2 builds plots layer by layer")
''',
        '''# readr and tidyr: reading and reshaping data
# library(readr); df <- read_csv("data.csv")
# library(tidyr); tidyr::pivot_longer(df, cols = c(a, b))
print("readr reads CSVs fast; tidyr reshapes tables")
''',
    ],
    14: [
        '''# Base R plotting: the classic scatterplot
x <- 1:10
y <- x^2
plot(x, y, main = "Squares", col = "blue", pch = 19)
print("plot() opens a graphics device")
''',
        '''# hist() for distributions
set.seed(42)
values <- rnorm(1000, mean = 0, sd = 1)
hist(values, breaks = 30, main = "Normal distribution")
''',
        '''# boxplot() for comparing groups
groups <- list(a = rnorm(50), b = rnorm(50, mean = 2))
boxplot(groups, main = "Group comparison")
''',
        '''# Saving plots to files
# png("plot.png", width = 800, height = 600)
# plot(1:10, 1:10)
# dev.off()
print("dev.off() closes the graphics device")
''',
    ],
    15: [
        '''# Errors and warnings: stop(), warning(), message()
check <- function(x) {
    if (x < 0) stop("x must be non-negative")
    if (x == 0) warning("x is zero")
    message("checking x = ", x)
    sqrt(x)
}
print(check(4))             # 2
''',
        '''# tryCatch: R's structured exception handling
result <- tryCatch(
    expr = {
        stop("boom")
    },
    error = function(e) {
        paste("caught:", conditionMessage(e))
    },
    finally = {
        print("cleanup ran")
    }
)
print(result)               # "caught: boom"
''',
        '''# withCallingHandlers for warnings
withCallingHandlers(
    expr = { warning("a warning"); 42 },
    warning = function(w) print(paste("warn:", conditionMessage(w)))
)
''',
        '''# Validating inputs: stopifnot
require_positive <- function(x) {
    stopifnot(is.numeric(x), x > 0)
    sqrt(x)
}
print(require_positive(9))  # 3
''',
    ],
    16: [
        '''# Reading data: read.csv and read.table
# df <- read.csv("data.csv")
# df <- read.csv("data.csv", stringsAsFactors = FALSE)
print("read.csv is the base-R workhorse")
''',
        '''# Writing data: write.csv
df <- data.frame(name = c("Ada", "Grace"), age = c(36, 85))
write.csv(df, "people.csv", row.names = FALSE)
print(read.csv("people.csv"))
''',
        '''# readLines for raw text files
lines <- readLines(textConnection(c("line one", "line two")))
print(lines)                # "line one" "line two"
''',
        '''# Working with JSON and CSV via packages
# library(jsonlite)
# data <- jsonlite::fromJSON("data.json")
# library(readr)
# df <- readr::read_csv("data.csv")
print("jsonlite and readr handle modern formats")
''',
    ],
    17: [
        '''# Sampling: sample() and set.seed()
set.seed(42)
print(sample(1:10, 3))      # random sample without replacement
print(sample(1:10, 5, replace = TRUE))  # with replacement
''',
        '''# Random distributions
set.seed(1)
print(rnorm(3))             # 3 draws from N(0, 1)
print(runif(3, 0, 1))       # 3 draws from Uniform(0, 1)
''',
        '''# Summary statistics
x <- c(1, 2, 3, 4, 100)
print(mean(x))              # 22
print(median(x))            # 3
print(sd(x))                # standard deviation
print(summary(x))           # min, quartiles, max
''',
        '''# Correlation and basic tests
x <- c(1, 2, 3, 4, 5)
y <- c(2, 4, 6, 8, 10)
print(cor(x, y))            # 1 — perfectly correlated
print(t.test(x, mu = 3))    # one-sample t-test
''',
    ],
    18: [
        '''# NA handling: na.rm and complete.cases
data <- c(1, NA, 3, NA, 5)
print(mean(data))           # NA — propagates!
print(mean(data, na.rm = TRUE))  # 3
print(data[!is.na(data)])   # 1 3 5
''',
        '''# na.omit drops incomplete rows
df <- data.frame(a = c(1, NA, 3), b = c("x", "y", "z"))
print(na.omit(df))          # rows 1 and 3
''',
        '''# tidyr::drop_na and fill
# library(tidyr)
# df |> tidyr::drop_na()     # drop rows with any NA
# df |> tidyr::fill(col)     # forward fill
print("tidyr handles missing data elegantly")
''',
        '''# impute strategies: mean replacement
values <- c(1, NA, 3)
values[is.na(values)] <- mean(values, na.rm = TRUE)
print(values)               # 1 2 3
''',
    ],
    19: [
        '''# Factors for grouping; table() for counts
colors <- factor(c("red", "blue", "red", "green"))
print(table(colors))
# blue  green   red
#    1      1     2
''',
        '''# aggregate(): group-wise summaries the base way
df <- data.frame(group = c("a", "a", "b", "b"),
                 value = c(1, 2, 10, 20))
print(aggregate(value ~ group, data = df, FUN = mean))
''',
        '''# split(): divide a vector by groups
groups <- c("x", "y", "x", "y")
values <- c(1, 10, 2, 20)
print(split(values, groups))    # list of x-values and y-values
''',
        '''# dplyr::group_by + summarize (tidyverse way)
# library(dplyr)
# df |> group_by(group) |> summarize(avg = mean(value))
print("group_by + summarize is the modern idiom")
''',
    ],
    20: [
        '''# Functions are first-class: pass them around
apply_twice <- function(f, x) f(f(x))
print(apply_twice(function(n) n * 2, 5))  # 20
''',
        '''# Environments and scope: globalenv() and local()
x <- "global"
f <- local({
    x <- "local"
    function() x
})
print(f())                  # "local"
print(x)                    # "global" — untouched
''',
        '''# S3 classes: R's simple OOP system
person <- function(name, age) {
    obj <- list(name = name, age = age)
    class(obj) <- "person"
    obj
}
print.person <- function(p) {
    cat(p$name, "is", p$age, "years old\\n")
}
ada <- person("Ada", 36)
print(ada)                  # Ada is 36 years old
''',
        '''# S4 classes: formal OOP (Bioconductor style)
# setClass("Person", slots = c(name = "character", age = "numeric"))
# ada <- new("Person", name = "Ada", age = 36)
print("S4 brings formal validation and inheritance")
''',
    ],
    21: [
        '''# The ecosystem: CRAN, Bioconductor, and RStudio
# install.packages("dplyr")
# BiocManager::install("limma")
print("CRAN hosts 20,000+ packages")
''',
        '''# R Markdown: reproducible reports
# ---
# title: "My Report"
# ---
# ```{r}
# summary(mtcars)
# ```
print("R Markdown mixes prose, code, and output")
''',
        '''# Shiny: interactive web apps in R
# library(shiny)
# ui <- fluidPage(selectInput("var", "Variable", names(mtcars)))
# server <- function(input, output) {}
# shinyApp(ui, server)
print("Shiny turns R analyses into interactive apps")
''',
        '''# Next steps: advanced R topics
# 1. Data.table for big data speed
# 2. Rcpp for C++ performance
# 3. Functional programming with purrr
# 4. Package development best practices
print("You now have a complete foundation in R")
''',
    ],
}

LESSONS = [
    dict(
        slug='r-01-getting-started',
        title='Getting Started with R',
        desc='Console, scripts, RStudio, and the R execution model.',
        diff='beginner',
        dur=20,
        objs=[
            'Run R code in the console and from scripts',
            'Explain how R vectorizes operations',
            'Use basic assignment and print statements',
        ],
        prereq=[],
        refs=[dict(title='The R Project — Home', url='https://www.r-project.org/'),
              dict(title='An Introduction to R — Official Manual', url='https://cran.r-project.org/doc/manuals/r-release/R-intro.html'),
              dict(title='RStudio — Free IDE', url='https://posit.co/products/open-source/rstudio/')]),
    dict(
        slug='r-02-values-types',
        title='Values and Types',
        desc='Numeric, integer, character, logical — and special values.',
        diff='beginner',
        dur=25,
        objs=[
            'Identify core R types with class() and typeof()',
            'Explain NA, NULL, NaN, and Inf',
            'Describe automatic type coercion in vectors',
        ],
        prereq=['r-01-getting-started'],
        refs=[dict(title='R Language Definition — Objects', url='https://cran.r-project.org/doc/manuals/r-release/R-lang.html#Objects'),
              dict(title='R for Data Science — Data Types', url='https://r4ds.hadley.nz/vectors')]),
    dict(
        slug='r-03-variables-scoping',
        title='Variables and Scoping',
        desc='Assignment, object names, environments, and existence checks.',
        diff='beginner',
        dur=25,
        objs=[
            'Assign values with <- and =',
            'List and remove objects with ls() and rm()',
            'Explain that everything in R is an object',
        ],
        prereq=['r-01-getting-started'],
        refs=[dict(title='Advanced R — Names and Values', url='https://adv-r.hadley.nz/names-values.html'),
              dict(title='Advanced R — Environments', url='https://adv-r.hadley.nz/environments.html')]),
    dict(
        slug='r-04-arithmetic-operators',
        title='Arithmetic and Operators',
        desc='Numeric, comparison, logical, and vectorized operators.',
        diff='beginner',
        dur=25,
        objs=[
            'Use arithmetic and comparison operators',
            'Distinguish vectorized & / | from short-circuit && / ||',
            'Leverage vectorized arithmetic',
        ],
        prereq=['r-02-values-types'],
        refs=[dict(title='An Introduction to R — Elementary Operations', url='https://cran.r-project.org/doc/manuals/r-release/R-intro.html#Simple-manipulations-numbers-and-vectors')]),
    dict(
        slug='r-05-functions',
        title='Functions',
        desc='Definitions, defaults, return values, and anonymous functions.',
        diff='beginner',
        dur=30,
        objs=[
            'Define functions with default arguments',
            'Use explicit and implicit return values',
            'Write anonymous functions with lapply',
        ],
        prereq=['r-01-getting-started'],
        refs=[dict(title='Advanced R — Functions', url='https://adv-r.hadley.nz/functions.html'),
              dict(title='R Language Definition — Functions', url='https://cran.r-project.org/doc/manuals/r-release/R-lang.html#Functions')]),
    dict(
        slug='r-06-vectors-indexing',
        title='Vectors and Indexing',
        desc='Atomic vectors, naming, logical subsetting, and sequences.',
        diff='beginner',
        dur=30,
        objs=[
            'Create and index vectors (1-based indexing)',
            'Name vector elements',
            'Filter with logical subsetting',
        ],
        prereq=['r-02-values-types'],
        refs=[dict(title='An Introduction to R — Vectors', url='https://cran.r-project.org/doc/manuals/r-release/R-intro.html#Vectors-and-assignment'),
              dict(title='R for Data Science — Subsetting', url='https://r4ds.hadley.nz/subset')]),
    dict(
        slug='r-07-control-flow',
        title='Control Flow',
        desc='if/else, ifelse, for, and while loops.',
        diff='beginner',
        dur=25,
        objs=[
            'Write conditional branches',
            'Use vectorized ifelse',
            'Iterate with for and while loops',
        ],
        prereq=['r-01-getting-started'],
        refs=[dict(title='An Introduction to R — Control Structures', url='https://cran.r-project.org/doc/manuals/r-release/R-intro.html#Control-statement'),
              dict(title='R for Data Science — Iteration', url='https://r4ds.hadley.nz/iteration')]),
    dict(
        slug='r-08-strings-text',
        title='Strings and Text',
        desc='paste, sprintf, string functions, and regular expressions.',
        diff='beginner',
        dur=25,
        objs=[
            'Build strings with paste and sprintf',
            'Manipulate strings with base functions',
            'Use regular expressions with grep and gsub',
        ],
        prereq=['r-02-values-types'],
        refs=[dict(title='R for Data Science — Strings', url='https://r4ds.hadley.nz/strings'),
              dict(title='stringr — Tidyverse Docs', url='https://stringr.tidyverse.org/')]),
    dict(
        slug='r-09-lists-data-frames',
        title='Lists, Matrices, and Data Frames',
        desc='Heterogeneous containers and tabular data.',
        diff='intermediate',
        dur=35,
        objs=[
            'Create and access lists with $ and [[]]',
            'Work with matrices',
            'Build and subset data frames',
        ],
        prereq=['r-06-vectors-indexing'],
        refs=[dict(title='An Introduction to R — Lists', url='https://cran.r-project.org/doc/manuals/r-release/R-intro.html#Lists'),
              dict(title='An Introduction to R — Data Frames', url='https://cran.r-project.org/doc/manuals/r-release/R-intro.html#Data-frames'),
              dict(title='R for Data Science — Data Frames', url='https://r4ds.hadley.nz/data-frame')]),
    dict(
        slug='r-10-factors-dates',
        title='Factors, Dates, and Attributes',
        desc='Categorical variables, ordered factors, and time handling.',
        diff='intermediate',
        dur=30,
        objs=[
            'Create and reorder factors',
            'Work with ordered factors',
            'Handle dates with as.Date and format',
        ],
        prereq=['r-06-vectors-indexing'],
        refs=[dict(title='An Introduction to R — Factors', url='https://cran.r-project.org/doc/manuals/r-release/R-intro.html#Factors'),
              dict(title='R for Data Science — Dates and Times', url='https://r4ds.hadley.nz/datetimes')]),
    dict(
        slug='r-11-apply-family',
        title='The Apply Family',
        desc='apply, lapply, sapply, tapply, and friends.',
        diff='intermediate',
        dur=35,
        objs=[
            'Apply functions over rows and columns',
            'Simplify lists with sapply',
            'Compute group-wise summaries with tapply',
        ],
        prereq=['r-05-functions'],
        refs=[dict(title='R for Data Science — The map functions', url='https://r4ds.hadley.nz/iteration'),
              dict(title='An Introduction to R — apply family', url='https://cran.r-project.org/doc/manuals/r-release/R-intro.html#The-function-apply')]),
    dict(
        slug='r-12-functions-advanced',
        title='Advanced Functions',
        desc='Reuse, ... arguments, closures, and lexical scoping.',
        diff='intermediate',
        dur=35,
        objs=[
            'Compose functions that reuse other functions',
            'Use ... to forward arguments',
            'Build closures with <<-',
        ],
        prereq=['r-05-functions'],
        refs=[dict(title='Advanced R — Function Composition', url='https://adv-r.hadley.nz/functions.html'),
              dict(title='Advanced R — Environments', url='https://adv-r.hadley.nz/environments.html')]),
    dict(
        slug='r-13-tidyverse',
        title='The Tidyverse',
        desc='dplyr, ggplot2, readr, and tidyr — the modern R.',
        diff='intermediate',
        dur=30,
        objs=[
            'Install and load the tidyverse',
            'Use dplyr verbs with the pipe operator',
            'Explain the grammar of graphics in ggplot2',
        ],
        prereq=['r-09-lists-data-frames'],
        refs=[dict(title='Tidyverse — Main Site', url='https://www.tidyverse.org/'),
              dict(title='R for Data Science — Whole book', url='https://r4ds.hadley.nz/'),
              dict(title='dplyr — Documentation', url='https://dplyr.tidyverse.org/'),
              dict(title='ggplot2 — Documentation', url='https://ggplot2.tidyverse.org/')]),
    dict(
        slug='r-14-data-visualization',
        title='Data Visualization',
        desc='Base R plots, histograms, boxplots, and saving output.',
        diff='intermediate',
        dur=30,
        objs=[
            'Create scatterplots with plot()',
            'Build histograms and boxplots',
            'Save plots to image files',
        ],
        prereq=['r-06-vectors-indexing'],
        refs=[dict(title='An Introduction to R — Graphics', url='https://cran.r-project.org/doc/manuals/r-release/R-intro.html#Graphics'),
              dict(title='R Graphics Cookbook', url='https://r-graphics.org/')]),
    dict(
        slug='r-15-errors-exceptions',
        title='Errors and Exceptions',
        desc='stop, warning, tryCatch, and input validation.',
        diff='intermediate',
        dur=30,
        objs=[
            'Raise errors and warnings with stop and warning',
            'Handle errors with tryCatch',
            'Validate inputs with stopifnot',
        ],
        prereq=['r-07-control-flow'],
        refs=[dict(title='Advanced R — Debugging and Exceptions', url='https://adv-r.hadley.nz/debugging.html'),
              dict(title='R Language Definition — Errors', url='https://cran.r-project.org/doc/manuals/r-release/R-lang.html#Error-handling')]),
    dict(
        slug='r-16-file-io',
        title='File I/O',
        desc='Reading and writing CSV, text, and modern formats.',
        diff='intermediate',
        dur=30,
        objs=[
            'Read CSVs with read.csv',
            'Write data with write.csv',
            'Read raw text with readLines',
        ],
        prereq=['r-09-lists-data-frames'],
        refs=[dict(title='R for Data Science — Data Import', url='https://r4ds.hadley.nz/data-import'),
              dict(title='readr — Documentation', url='https://readr.tidyverse.org/'),
              dict(title='jsonlite — Documentation', url='https://cran.r-project.org/web/packages/jsonlite/vignettes/json-aaquickstart.html')]),
    dict(
        slug='r-17-statistics',
        title='Statistics and Sampling',
        desc='Sampling, distributions, summaries, and hypothesis tests.',
        diff='intermediate',
        dur=30,
        objs=[
            'Sample data with sample() and set.seed()',
            'Draw from random distributions',
            'Compute summary statistics and run t-tests',
        ],
        prereq=['r-06-vectors-indexing'],
        refs=[dict(title='R for Data Science — Distributions', url='https://r4ds.hadley.nz/'),
              dict(title='An Introduction to R — Statistical Functions', url='https://cran.r-project.org/doc/manuals/r-release/R-intro.html#Statistical-distributions')]),
    dict(
        slug='r-18-missing-data',
        title='Missing Data',
        desc='NA propagation, na.rm, and imputation strategies.',
        diff='intermediate',
        dur=25,
        objs=[
            'Explain how NA propagates through calculations',
            'Use na.rm and complete.cases',
            'Apply basic imputation strategies',
        ],
        prereq=['r-02-values-types'],
        refs=[dict(title='R for Data Science — Missing Values', url='https://r4ds.hadley.nz/missing-values'),
              dict(title='tidyr — Missing data docs', url='https://tidyr.tidyverse.org/articles/tidy-data.html')]),
    dict(
        slug='r-19-grouping-aggregation',
        title='Grouping and Aggregation',
        desc='table, aggregate, split, and group_by + summarize.',
        diff='intermediate',
        dur=30,
        objs=[
            'Count categories with table()',
            'Compute group-wise means with aggregate()',
            'Use dplyr group_by + summarize',
        ],
        prereq=['r-11-apply-family'],
        refs=[dict(title='R for Data Science — Groups', url='https://r4ds.hadley.nz/data-transform'),
              dict(title='An Introduction to R — tabulating', url='https://cran.r-project.org/doc/manuals/r-release/R-intro.html#Grouping-loops-and-conditional-execution')]),
    dict(
        slug='r-20-functions-oop',
        title='Functional Programming and OOP',
        desc='First-class functions, environments, S3 and S4 classes.',
        diff='expert',
        dur=40,
        objs=[
            'Pass functions as arguments',
            'Use environments with local()',
            'Build S3 classes with class assignment',
        ],
        prereq=['r-12-functions-advanced'],
        refs=[dict(title='Advanced R — S3', url='https://adv-r.hadley.nz/s3.html'),
              dict(title='Advanced R — S4', url='https://adv-r.hadley.nz/s4.html'),
              dict(title='Advanced R — Functional Programming', url='https://adv-r.hadley.nz/fp.html')]),
    dict(
        slug='r-21-ecosystem-next-steps',
        title='Ecosystem and Next Steps',
        desc='CRAN, R Markdown, Shiny, and the road ahead.',
        diff='intermediate',
        dur=20,
        objs=[
            'Install packages from CRAN and Bioconductor',
            'Create reproducible R Markdown reports',
            'Build interactive apps with Shiny',
        ],
        prereq=['r-13-tidyverse'],
        refs=[dict(title='CRAN — Package Repository', url='https://cran.r-project.org/'),
              dict(title='R Markdown — Official Docs', url='https://rmarkdown.rstudio.com/'),
              dict(title='Shiny — Official Docs', url='https://shiny.posit.co/'),
              dict(title='R for Data Science — 2nd Edition', url='https://r4ds.hadley.nz/')]),
]


if __name__ == '__main__':
    run_gen(LANGUAGE, 'r', LESSONS, CODE, BASE)
