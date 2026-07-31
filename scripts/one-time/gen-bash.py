#!/usr/bin/env python3
"""Generate the 21-lesson Bash curriculum at Python/JS/Java depth.
Uses the shared gen_lib template. Exact refs from gnu.org bash manual + shellcheck.
Each lesson has 4 sub-topics, each with its OWN distinct code sample.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from gen_lib import main as run_gen  # noqa: E402

LANGUAGE = 'bash'

BASE = os.path.join(os.path.dirname(__file__), '..', '..', 'static-data', 'knowledge', 'languages', 'bash')

CODE = {
    1: [
        '''#!/usr/bin/env bash
# Your first Bash script: shebang, echo, and comments
echo "Hello, 100X Systems!"
echo "Running with bash $BASH_VERSION"
# This line is a comment — the shell ignores it
echo "Done."
# run: bash hello.sh  (or chmod +x hello.sh && ./hello.sh)''',
        '''#!/usr/bin/env bash
# Variables: assignment, expansion, and word splitting
name="Alice"
echo "Hello, $name"          # quoted expansion: safe
echo "Hello, ${name}!"       # braces disambiguate
echo "count: $(wc -l < /etc/hostname)"   # command substitution
echo 'Literal $name'          # single quotes: no expansion''',
        '''#!/usr/bin/env bash
# Reading user input
read -rp "What is your name? " name
read -rp "How old are you? " age
echo "Nice to meet you, $name ($age years)."
if (( age >= 18 )); then
  echo "You are an adult."
else
  echo "You are a minor."
fi''',
        '''#!/usr/bin/env bash
# Checking a command succeeded with $?
mkdir -p /tmp/demo
cd /tmp/demo || { echo "cd failed"; exit 1; }
echo "hello" > file.txt
if [ -f file.txt ]; then
  echo "file.txt exists with $(wc -c < file.txt) bytes"
fi
cd - >/dev/null''',
    ],
    2: [
        '''#!/usr/bin/env bash
# Variable scoping: script-level vs function-local
greeting="Hello"                 # global
greet() {
  local name="$1"                # local to the function
  echo "$greeting, $name"
}
greet "World"
echo "greeting is still: $greeting"
# local keeps globals unclobbered — critical in big scripts''',
        '''#!/usr/bin/env bash
# Quoting: single vs double quotes vs no quotes
word="hello world"
echo $word        # unquoted: splits into two words
echo "$word"      # double-quoted: one word
echo '$word'      # single-quoted: literal $word
echo "path: $HOME/file with space.txt"
# Rule: always quote expansions unless you WANT splitting''',
        '''#!/usr/bin/env bash
# Exporting variables to child processes
export APP_ENV="production"
export API_URL="https://api.example.com"
./child.sh           # child inherits the exported vars
# Without export, child processes never see the variable:
NORMAL_VAR="hidden"
env | grep -E 'APP_ENV|NORMAL_VAR' || true''',
        '''#!/usr/bin/env bash
# Readonly and special shell parameters
readonly CONFIG="/etc/myapp.conf"
echo "config: $CONFIG"
echo "script name: $0"
echo "first arg: $1, arg count: $#"
echo "all args: $*"
echo "last exit: $?"''',
    ],
    3: [
        '''#!/usr/bin/env bash
# if / elif / else with test brackets
score=85
if (( score >= 90 )); then
  echo "Grade: A"
elif (( score >= 75 )); then
  echo "Grade: B"
else
  echo "Grade: C or lower"
fi''',
        '''#!/usr/bin/env bash
# case statement: pattern matching
fruit="banana"
case "$fruit" in
  apple|pear) echo "tree fruit" ;;
  banana)     echo "tropical fruit" ;;
  *)          echo "unknown fruit" ;;
esac
# Note the double semicolons — required per clause''',
        '''#!/usr/bin/env bash
# [ ] vs [[ ]] vs (( ))
if [[ "$name" == a* ]]; then        # [[ ]] glob & regex support
  echo "starts with a"
fi
if [ -f file.txt ]; then             # [ ] POSIX: file tests
  echo "file exists"
fi
if (( 3 > 2 )); then                 # (( )) arithmetic
  echo "3 is greater than 2"
fi''',
        '''#!/usr/bin/env bash
# Logical operators: && || !
if command -v jq >/dev/null 2>&1 && command -v curl >/dev/null 2>&1; then
  echo "jq and curl are installed"
fi
error=0
if [ $error -ne 0 ]; then
  echo "error state"
else
  echo "ok"
fi
# -a / -o are deprecated; always chain with && || inside [[ ]]''',
    ],
    4: [
        '''#!/usr/bin/env bash
# for loop over a list
for color in red green blue; do
  echo "color: $color"
done
# brace expansion produces the list:
for n in {1..5}; do
  echo "number $n"
done''',
        '''#!/usr/bin/env bash
# for loop with command output and C-style arithmetic
for file in *.txt; do
  echo "processing $file"
done
for (( i = 0; i < 3; i++ )); do
  echo "iteration $i"
done''',
        '''#!/usr/bin/env bash
# while and until loops
count=0
while (( count < 3 )); do
  echo "count: $count"
  (( count++ ))
done
until [ -f /tmp/ready ]; do
  echo "waiting for /tmp/ready..."
  sleep 1
done
echo "ready file appeared!"''',
        '''#!/usr/bin/env bash
# break and continue
for n in {1..10}; do
  (( n % 2 == 0 )) && continue    # skip evens
  [ "$n" -ge 7 ] && break          # stop at 7
  echo "odd under 7: $n"
done
# Output: 1 3 5''',
    ],
    5: [
        '''#!/usr/bin/env bash
# Defining and calling functions
say_hello() {
  echo "Hello, $1!"       # $1 is the first argument
}
say_hello "World"
# Function names must be called WITHOUT parentheses''',
        '''#!/usr/bin/env bash
# Return values: exit status, not data
is_even() {
  local n="$1"
  (( n % 2 == 0 ))          # exit status is the last command
}
if is_even 4; then
  echo "4 is even"
fi
# Functions returning data use echo/printf capture:
get_user() { echo "$USER"; }
user="$(get_user)"
echo "current user: $user"''',
        '''#!/usr/bin/env bash
# local variables and argument shifting
describe() {
  local name="$1"
  local role="${2:-unknown}"    # default value
  echo "$name is a $role"
}
describe "Bash" "shell"
describe "Python"''',
        '''#!/usr/bin/env bash
# A reusable helper pattern with error checking
die() {
  echo "ERROR: $*" >&2
  exit 1
}
require() {
  command -v "$1" >/dev/null 2>&1 || die "missing command: $1"
}
require jq
echo "jq is available"''',
    ],
    6: [
        '''#!/usr/bin/env bash
# String basics: length, concatenation, uppercase
name="bash"
echo "length: ${#name}"
full="${name} scripting"
echo "$full"
upper="${name^^}"
lower="${upper,,}"
echo "upper: $upper, lower: $lower"''',
        '''#!/usr/bin/env bash
# Substring extraction
text="Hello, World!"
echo "${text:0:5}"      # Hello
echo "${text:7}"        # World!
echo "${text: -6}"      # World! (space before -6 needed)
# Pattern removal
path="/usr/local/bin/bash"
echo "${path#*/}"       # remove shortest prefix to first /
echo "${path##*/}"      # remove longest prefix -> bash
echo "${path%.*}"       # nothing (no dot at end)
echo "${path%/*}"       # /usr/local/bin''',
        '''#!/usr/bin/env bash
# Replacement in strings
msg="the quick brown fox"
echo "${msg/fox/dog}"           # replace first match
echo "${msg//o/0}"              # replace ALL matches
echo "${msg/#the/ThE}"          # replace at start
echo "${msg/%fox/dog}"          # replace at end''',
        '''#!/usr/bin/env bash
# Default values and error on unset
unset MAYBE
echo "${MAYBE:-fallback}"      # fallback if unset/empty
echo "${MAYBE:=assigned}"      # assign if unset/empty
echo "$MAYBE"                  # now assigned
echo "${REQUIRED:?must be set}"  # errors if unset (with message)
# Note: ${var?} exits the script with the message''',
    ],
    7: [
        '''#!/usr/bin/env bash
# Indexed arrays
colors=(red green blue)
colors[3]="yellow"
echo "first: ${colors[0]}"
echo "all: ${colors[*]}"
echo "count: ${#colors[@]}"
for c in "${colors[@]}"; do
  echo "color $c"
done''',
        '''#!/usr/bin/env bash
# Associative arrays (Bash 4+)
declare -A cities
cities[IN]="Mumbai"
cities[US]="New York"
cities[JP]="Tokyo"
echo "US -> ${cities[US]}"
for country in "${!cities[@]}"; do
  echo "$country -> ${cities[$country]}"
done''',
        '''#!/usr/bin/env bash
# Slicing and appending to arrays
nums=(1 2 3 4 5)
echo "slice 1..3: ${nums[@]:1:3}"
nums+=(6 7)
echo "appended: ${nums[*]}"
# Copy an array safely
copy=("${nums[@]}")
echo "copy count: ${#copy[@]}"''',
        '''#!/usr/bin/env bash
# Reading lines into an array
mapfile -t lines < /etc/hostname
echo "lines read: ${#lines[@]}"
# Or read stdin into array:
mapfile -t words <<< "one two three"
echo "words: ${words[*]}"
# mapfile is efficient — avoid while-read loops when possible''',
    ],
    8: [
        '''#!/usr/bin/env bash
# Pipes: connect commands
cat /etc/passwd | grep "/bin/bash" | awk -F: '{print $1}'
# pipefail catches failures mid-pipeline:
set -o pipefail
false | true
echo "pipeline failed: $?"  # 1 with pipefail, 0 without''',
        '''#!/usr/bin/env bash
# Redirection: stdin, stdout, stderr
echo "stdout" > out.txt          # overwrite
echo "append" >> out.txt         # append
ls /nonexistent 2> err.txt       # stderr only
cmd > all.txt 2>&1               # both to one file
cmd &> combined.txt              # shorthand for the above''',
        '''#!/usr/bin/env bash
# Here-documents and here-strings
cat <<EOF
This is a here-doc.
Variables: $HOME expands here.
EOF
cat <<'EOF'
Literally no expansion: $HOME stays literal.
EOF
# Here-string:
grep -o "world" <<< "hello world"''',
        '''#!/usr/bin/env bash
# Process substitution
diff <(ls /usr/local/bin) <(ls /usr/bin) || true
# Commands run in parallel, outputs treated as files.
# Also useful to avoid subshell pitfalls:
while read -r line; do
  echo "got: $line"
done < <(printf 'a\\nb\\nc\\n')''',
    ],
    9: [
        '''#!/usr/bin/env bash
# Glob patterns
echo *.txt                # all txt files
echo file?.txt            # single char wildcard
echo file[0-9].txt        # character class
echo file[!0-9].txt       # negation
# Enable extended globs:
shopt -s extglob
echo !(backup).txt        # all txt except backup''',
        '''#!/usr/bin/env bash
# grep: regular expression search
echo "error 42 occurred" | grep -E "error [0-9]+"
grep -i "warning" *.log || true        # case-insensitive
grep -rn "TODO" src/ | head -5         # recursive with line numbers
# Capture the matched portion with -o:
echo "key=value" | grep -oE "=.*"''',
        '''#!/usr/bin/env bash
# sed: stream editor basics
echo "hello world" | sed 's/world/universe/'
echo "a b c" | sed 's/ /-/g'               # global replace
printf '1\\n2\\n3\\n' | sed -n '2p'            # print line 2
printf 'x\\ny\\n' | sed '/x/d'                # delete matching
sed -i.bak 's/old/new/g' file.txt           # in-place edit''',
        '''#!/usr/bin/env bash
# awk: columnar text processing
printf 'Alice 30\\nBob 25\\n' | awk '{print $2, $1}'   # swap columns
printf 'Alice 30\\nBob 25\\n' | awk '$2 > 26 {print $1}'
# With field separator:
awk -F: '{print $1}' /etc/passwd | head -3
# Sum a column:
printf '1\\n2\\n3\\n' | awk '{s+=$1} END {print s}'   # 6''',
    ],
    10: [
        '''#!/usr/bin/env bash
# sort, uniq, cut, wc
printf 'b\\na\\nb\\n' | sort | uniq -c
printf '1,2,3\\n4,5,6\\n' | cut -d, -f2
printf 'hello world\\n' | wc -w        # word count
# Classic pipeline: most common word
tr -s ' ' '\\n' < text.txt | sort | uniq -c | sort -rn | head -5''',
        '''#!/usr/bin/env bash
# head, tail, and line ranges
seq 1 100 | head -3
seq 1 100 | tail -3
seq 1 100 | sed -n '10,15p'
# tail -f for live logs:
tail -f /var/log/system.log 2>/dev/null | head -2 || true''',
        '''#!/usr/bin/env bash
# xargs: build and run commands from stdin
printf 'a.txt\\nb.txt\\n' | xargs -n1 echo "processing"
find . -name "*.tmp" -print0 | xargs -0 rm -f    # null-safe
# Parallel execution with -P:
seq 1 4 | xargs -P4 -I{} sh -c 'echo running {}; sleep 1'
echo "all done"''',
        '''#!/usr/bin/env bash
# join and paste
paste -d, <(printf 'a\\nb\\n') <(printf '1\\n2\\n')
# join requires sorted inputs:
sort a.txt > a.sorted
sort b.txt > b.sorted
join a.sorted b.sorted || true
# tr: translate characters
echo "hello" | tr 'a-z' 'A-Z'
echo "a,b,c" | tr ',' '\\n' ''',
    ],
    11: [
        '''#!/usr/bin/env bash
# set -e: exit on first error
set -e
echo "before error"
false
echo "this never runs"   # set -e stops here''',
        '''#!/usr/bin/env bash
# trap: cleanup on exit and signals
cleanup() {
  rm -f /tmp/lockfile
  echo "cleaned up"
}
trap cleanup EXIT
trap 'echo "interrupted"; exit 1' INT TERM
echo "work in progress..."
sleep 2
# Ctrl-C or normal exit both run cleanup''',
        '''#!/usr/bin/env bash
# Robust error handling patterns
set -euo pipefail       # -e exit, -u unset vars, pipefail
die() { echo "FATAL: $*" >&2; exit 1; }
[ -n "${REQUIRED_VAR:-}" ] || die "REQUIRED_VAR not set"
command -v curl || die "curl is required"
curl -fsSL https://example.com/data.json -o data.json \\
  || die "download failed"
echo "download OK"''',
        '''#!/usr/bin/env bash
# Exit codes and $? handling
run_or_fallback() {
  if "$@"; then
    return 0
  else
    echo "WARN: $* failed (exit $?)" >&2
    return 1
  fi
}
run_or_fallback true
run_or_fallback false || echo "caught the failure"
# 0 = success; non-zero = failure — always check!''',
    ],
    12: [
        '''#!/usr/bin/env bash
# Background jobs
sleep 3 &
job1=$!
echo "started job $job1"
wait $job1
echo "job finished"
# Multiple jobs and wait:
sleep 1 & sleep 2 & wait
echo "all done"''',
        '''#!/usr/bin/env bash
# Job control: jobs, fg, bg, kill
sleep 100 &
sleep 200 &
jobs -l
kill %1                  # kill by job number
kill 12345 2>/dev/null || true   # kill by PID
wait
echo "jobs terminated"''',
        '''#!/usr/bin/env bash
# Disowning and nohup
nohup sleep 60 >/dev/null 2>&1 &
# nohup survives terminal close; & backgrounds it
# disown removes a job from the shell's job table:
sleep 30 &
disown
echo "disowned"''',
        '''#!/usr/bin/env bash
# Checking if a process is running
if pgrep -x "nginx" >/dev/null; then
  echo "nginx is running"
else
  echo "nginx is NOT running"
fi
# Kill by pattern with pkill:
pkill -f "my-app" || true
# Monitor a command:
until pgrep -x "nginx" >/dev/null; do sleep 1; done
echo "nginx came up"''',
    ],
    13: [
        '''#!/usr/bin/env bash
# Positional parameters and defaults
script() {
  local name="${1:-world}"
  local count="${2:-1}"
  for (( i = 0; i < count; i++ )); do
    echo "hello $name"
  done
}
script
script "Bash" 2''',
        '''#!/usr/bin/env bash
# getopts: standard option parsing
usage() { echo "Usage: $0 -n NAME [-v]" >&2; exit 1; }
name=""
verbose=0
while getopts "n:v" opt; do
  case "$opt" in
    n) name="$OPTARG" ;;
    v) verbose=1 ;;
    *) usage ;;
  esac
done
shift $((OPTIND - 1))
echo "name=$name verbose=$verbose rest=$*"''',
        '''#!/usr/bin/env bash
# shift: walking positional arguments
process() {
  while [ $# -gt 0 ]; do
    echo "arg: $1"
    shift
  done
}
process a b c
# Extract a range:
echo "arg2..3: ${@:2:2}"''',
        '''#!/usr/bin/env bash
# Parsing flags with a case-based loop
verbose=false
debug=false
for arg in "$@"; do
  case "$arg" in
    -v|--verbose) verbose=true ;;
    -d|--debug)   debug=true ;;
    *)            echo "unknown: $arg" ;;
  esac
done
$verbose && echo "verbose mode"
$debug && echo "debug mode"''',
    ],
    14: [
        '''#!/usr/bin/env bash
# Environment variables: reading and defaults
echo "HOME=$HOME"
echo "USER=$USER"
echo "PWD=$PWD"
: "${EDITOR:=vi}"        # set default if unset
echo "editor: $EDITOR"
# List all exported env vars:
env | head -5''',
        '''#!/usr/bin/env bash
# Exporting for child processes
export DEBUG=1
export PATH="$PATH:$HOME/bin"
run_child() {
  # child sees the inherited environment
  echo "child sees DEBUG=$DEBUG and PATH=$PATH"
}
run_child
# Scope: exports in a subshell do NOT leak out
(
  export TEMP_ONLY=1
  echo "inside subshell: $TEMP_ONLY"
)
echo "outside: ${TEMP_ONLY:-unset}"''',
        '''#!/usr/bin/env bash
# Dotfiles and sourcing
# ~/.bashrc, ~/.bash_profile load environment at startup.
# Source a config file (runs it in THIS shell):
# shellcheck disable=SC1090
source "$HOME/.myenv" 2>/dev/null || echo "no .myenv"
# Difference: source vs executing
#   source ./x.sh   -> runs in current shell (vars persist)
#   ./x.sh          -> runs in subshell (vars lost)''',
        '''#!/usr/bin/env bash
# Interactive vs non-interactive shell detection
if [[ $- == *i* ]]; then
  echo "interactive shell"
else
  echo "non-interactive (script) shell"
fi
# Bash startup files differ by mode:
#   login interactive: .bash_profile
#   non-login interactive: .bashrc
#   non-interactive: $BASH_ENV''',
    ],
    15: [
        '''#!/usr/bin/env bash
# File descriptor gymnastics
exec 3<> /tmp/fd3.txt        # open read/write
echo "written via fd3" >&3
exec 3>&-                    # close fd3
cat /tmp/fd3.txt
# Duplicate descriptors:
exec 4>&1                    # save stdout
exec 1> /tmp/capture.txt     # redirect stdout
echo "this is captured"
exec 1>&4                    # restore stdout
echo "this is visible again"''',
        '''#!/usr/bin/env bash
# /dev/null and /dev/zero
# Discard output:
command -v nonexistent >/dev/null 2>&1 || echo "not found"
# Provide infinite zeros:
head -c 10 /dev/zero | wc -c
# /dev/null as a sink:
curl -s https://example.com >/dev/null 2>&1 || true
echo "done"''',
        '''#!/usr/bin/env bash
# Reading files with while-read (safe pattern)
while IFS= read -r line; do
  echo "line: $line"
done < file.txt
# Avoid the classic pipe-subshell bug:
# BAD:  cat file.txt | while read ...  (runs in subshell)
# GOOD: while read ... < file.txt      (same shell)''',
        '''#!/usr/bin/env bash
# FIFOs and named pipes
mkfifo /tmp/mypipe
# writer in background
(echo "through the pipe" > /tmp/mypipe) &
# reader blocks until a writer connects
read -r msg < /tmp/mypipe
echo "received: $msg"
rm -f /tmp/mypipe''',
    ],
    16: [
        '''#!/usr/bin/env bash
# jq: querying JSON from the shell
echo '{"name":"Alice","age":30}' | jq '.name'
echo '[1,2,3]' | jq '.[] | . * 2'
echo '{"a":1,"b":2}' | jq '.a + .b'
# Pretty-print any JSON:
echo '{"x":1}' | jq .''',
        '''#!/usr/bin/env bash
# jq: filtering and transforming
curl -fsSL https://api.github.com/repos/jqlang/jq 2>/dev/null |
  jq '{name, stars: .stargazers_count, desc: .description}' ||
  echo '{"name":"jq","stars":0}' | jq .
# Selecting array elements:
echo '[{"id":1,"ok":true},{"id":2,"ok":false}]' | jq ".[] | select(.ok)"''',
        '''#!/usr/bin/env bash
# Building JSON with jq
name="Alice"
age=30
jq -n --arg name "$name" --argjson age "$age" \\
  '{name: $name, age: $age, active: true}'
# Array of values:
jq -n '[range(3) | {index: .}]' ''',
        '''#!/usr/bin/env bash
# yq for YAML (install separately) — pattern shown for JSON only
# Parse CSV via awk into JSON:
printf 'Alice,30\\nBob,25\\n' | awk -F, '{printf "{\\"name\\":\\"%s\\",\\"age\\":%s}\\n", $1, $2}'
# Validate JSON:
if echo '{"ok":true}' | jq -e . >/dev/null 2>&1; then
  echo "valid JSON"
fi''',
    ],
    17: [
        '''#!/usr/bin/env bash
# xargs parallel execution
seq 1 8 | xargs -P8 -I{} sh -c 'echo "task {}"; sleep 0.5'
echo "parallel batch done"
# -n1 processes one at a time:
seq 1 3 | xargs -n1 echo "single"''',
        '''#!/usr/bin/env bash
# GNU parallel (if installed): fan-out with output control
# seq 1 4 | parallel -j4 'sleep 0.5; echo job {}' 2>/dev/null
# Without parallel, emulate with background jobs:
run_task() { sleep 0.5; echo "task $1 done"; }
pids=()
for i in 1 2 3 4; do
  run_task "$i" & pids+=("$!")
done
for p in "${pids[@]}"; do wait "$p"; done
echo "all 4 tasks finished"''',
        '''#!/usr/bin/env bash
# Subshells vs current shell: (
(
  cd /tmp
  echo "subshell pwd: $PWD"
)
echo "parent pwd: $PWD"    # unchanged!
# Variables set in subshells don't persist:
x=1
( x=2 )
echo "x is still $x"''',
        '''#!/usr/bin/env bash
# Coprocesses (Bash 4+)
coproc MYPROC { cat; }
echo "hello coproc" >&"${MYPROC[1]}"
read -r reply <&"${MYPROC[0]}"
echo "coproc replied: $reply"
# Coprocesses let a script talk to a long-running program
# bidirectionally — rare but powerful.''',
    ],
    18: [
        '''#!/usr/bin/env bash
# The canonical "library" script pattern
#!/usr/bin/env bash
set -euo pipefail

VERSION="1.0.0"

log()  { printf '[%s] %s\\n' "$(date +%H:%M:%S)" "$*"; }
info() { log "INFO  $*"; }
warn() { log "WARN  $*" >&2; }
die()  { log "FATAL $*" >&2; exit 1; }

main() {
  info "starting $0 v$VERSION"
  command -v git >/dev/null || die "git not found"
  git status >/dev/null 2>&1 || warn "not a git repo"
  info "done"
}
main "$@"''',
        '''#!/usr/bin/env bash
# Dry-run pattern: preview what would run
DRY_RUN="${DRY_RUN:-0}"
run() {
  echo "+ $*"
  if [ "$DRY_RUN" -eq 0 ]; then "$@"; fi
}
run mkdir -p /tmp/x
run echo "real work"
DRY_RUN=1
run echo "preview only"''',
        '''#!/usr/bin/env bash
# Logging with levels and a log file
LOG_FILE="${LOG_FILE:-/tmp/script.log}"
debug() { [ "${DEBUG:-0}" = "1" ] && echo "DEBUG: $*" | tee -a "$LOG_FILE"; }
info()  { echo "INFO:  $*" | tee -a "$LOG_FILE"; }
error() { echo "ERROR: $*" | tee -a "$LOG_FILE" >&2; }
DEBUG=1 debug "verbose detail"
info "step 1 complete"
error "something bad"''',
        '''#!/usr/bin/env bash
# Idempotency: safe re-runs
mkdir -p /opt/myapp                    # -p: no error if exists
[ -f /etc/myapp.conf ] || cp default.conf /etc/myapp.conf
if ! grep -q "MYAPP_ENABLED" .env 2>/dev/null; then
  echo "MYAPP_ENABLED=1" >> .env
fi
echo "re-run safe"''',
    ],
    19: [
        '''#!/usr/bin/env bash
# Avoiding external processes: builtins win
# BAD:  for f in $(cat list.txt)
# GOOD: while read -r f <&3; do ... done 3< list.txt
# printf is a builtin; echo with -e is not portable:
printf 'value=%s\\n' "$x"
# Arithmetic in the shell, not awk:
sum=$(( 3 + 4 * 2 ))
echo "sum=$sum"''',
        '''#!/usr/bin/env bash
# Timing and profiling a script
start=$(date +%s%N)
sleep 0.1
end=$(date +%s%N)
echo "elapsed: $(( (end - start) / 1000000 ))ms"
# Or use the `time` keyword:
time ( sleep 0.1 )''',
        '''#!/usr/bin/env bash
# Reduce forking: group work into one awk/one sed pass
# BAD: 3 forks per line
# GOOD: single awk pass
awk '{s+=$1} END {print s}' numbers.txt
# Bash pattern matching instead of external grep:
if [[ "$str" == *error* ]]; then
  echo "contains error"
fi
# $RANDOM is a builtin:
echo "random: $RANDOM"''',
        '''#!/usr/bin/env bash
# Memoization and caching in a loop
cached=""
for url in $(cat urls.txt); do
  key=$(echo "$url" | md5 -q 2>/dev/null || echo "$url")
  if [ -f "/tmp/cache/$key" ]; then
    echo "cached: $url"
    continue
  fi
  sleep 0.2   # simulate fetch
  mkdir -p /tmp/cache
  echo "$url" > "/tmp/cache/$key"
  echo "fetched: $url"
done''',
    ],
    20: [
        '''#!/usr/bin/env bash
# Quoting is security: the injection lesson
filename="user input; rm -rf /"
# BAD:  eval "ls $filename"       # executes the rm!
# GOOD: never eval user input
# Quoting prevents word-splitting/globbing surprises:
safe="a b*c"
echo "$safe"                # literal
printf '%s\\n' "$safe"
echo "quoted properly"''',
        '''#!/usr/bin/env bash
# shellcheck: static analysis (install separately)
# shellcheck disable=SC2086   # when you intentionally split
# SC2086 is "double quote to prevent globbing/word splitting"
name="Alice"
echo "$name"                 # fixed: quoted
# Check scripts with: shellcheck myscript.sh
echo "run shellcheck on your scripts!"''',
        '''#!/usr/bin/env bash
# Reading secrets without leaking them
# NEVER: pass secrets via argv (visible in `ps`)
# Use stdin or env:
read -r -s -p "Password: " secret
echo
echo "received ${#secret} chars (not shown)"
# Prefer secret managers; avoid echo-ing secrets:
printf '%s\\n' "${secret//?/*}"   # mask: *****''',
        '''#!/usr/bin/env bash
# Privilege checks and safe temp files
if [ "$(id -u)" -ne 0 ]; then
  echo "not root" >&2
fi
# Safe temp files:
tmp=$(mktemp /tmp/app.XXXXXX)
trap 'rm -f "$tmp"' EXIT
echo "temp file: $tmp"
# mktemp -d for directories; never guess names in /tmp''',
    ],
    21: [
        '''#!/usr/bin/env bash
# BASH_REMATCH: regex captures
if [[ "order-12345" =~ ^order-([0-9]+)$ ]]; then
  echo "order id: ${BASH_REMATCH[1]}"
fi
# Named capture via array indexing:
[[ "key=value" =~ ^([^=]+)=(.*)$ ]]
echo "key=${BASH_REMATCH[1]} value=${BASH_REMATCH[2]}"''',
        '''#!/usr/bin/env bash
# Process substitution tricks and /dev/fd
diff <(sort a.txt) <(sort b.txt) && echo "same content" || true
# Feed a function's output as a file argument:
echo_data() { printf 'x\\ny\\nz\\n'; }
while read -r l; do echo "> $l"; done < <(echo_data)''',
        '''#!/usr/bin/env bash
# Bash completion hooks (for interactive shells)
# _example() { COMPREPLY=( $(compgen -W "start stop restart" -- "${COMP_WORDS[1]}") ); }
# complete -F _example myapp
# This snippet documents the pattern; completion needs an
# interactive shell to demo.
echo "completion functions registered via complete -F"''',
        '''#!/usr/bin/env bash
# Performance & portability checklist
set -euo pipefail
# Prefer [[ ]] over [ ], (( )) over expr, ${var//} over sed.
# Batch with awk/sed/tr once instead of per-line.
# Quote everything, never eval, shellcheck before commit.
# Profile with `time` and bash -x when debugging.
bash -n "$0" && echo "syntax check passed"
echo "advanced Bash: done"''',
]
}

LESSONS = [
    dict(slug='bash-01-getting-started', title='Getting Started with Bash',
         desc='Shebang, echo, variables, comments, and your first script.',
         dur='45 min', diff='beginner', prereq=[],
         objs=['Write a shebang and run a script',
               'Use variables and command substitution',
               'Read user input',
               'Check command exit status'],
         refs=[dict(title='GNU Bash Reference Manual', url='https://www.gnu.org/software/bash/manual/bash.html'),
               dict(title='Bash Guide (TLDP)', url='https://tldp.org/LDP/abs/html/'),
               dict(title='ShellCheck', url='https://www.shellcheck.net/')]),
    dict(slug='bash-02-variables-scope', title='Variables and Scoping',
         desc='local vs global scope, quoting, export, and special parameters.',
         dur='45 min', diff='beginner', prereq=['BASH-01'],
         objs=['Understand local vs global scope',
               'Quote variables correctly',
               'Export variables to children',
               'Use readonly and special params'],
         refs=[dict(title='Bash — Shell Parameters', url='https://www.gnu.org/software/bash/manual/bash.html#Shell-Parameters'),
               dict(title='Bash — Quoting', url='https://www.gnu.org/software/bash/manual/bash.html#Quoting'),
               dict(title='ShellCheck SC2155', url='https://www.shellcheck.net/wiki/SC2155')]),
    dict(slug='bash-03-control-flow', title='Control Flow',
         desc='if/elif/else, case, and the test commands [ ], [[ ]], ( ( ) ).',
         dur='45 min', diff='beginner', prereq=['BASH-02'],
         objs=['Write if/elif/else branches',
               'Use case for pattern matching',
               'Distinguish [ ], [[ ]] and (( ))',
               'Chain conditions with && and ||'],
         refs=[dict(title='Bash — Conditional Constructs', url='https://www.gnu.org/software/bash/manual/bash.html#Conditional-Constructs'),
               dict(title='Test — man page', url='https://man7.org/linux/man-pages/man1/test.1.html'),
               dict(title='BashGuide — Tests', url='https://mywiki.wooledge.org/BashGuide/TestsAndConditionals')]),
    dict(slug='bash-04-loops', title='Loops',
         desc='for, while, until, break, continue, and brace expansion.',
         dur='45 min', diff='beginner', prereq=['BASH-03'],
         objs=['Iterate with for over lists',
               'Loop over command output',
               'Use while and until',
               'Control loops with break/continue'],
         refs=[dict(title='Bash — Looping Constructs', url='https://www.gnu.org/software/bash/manual/bash.html#Looping-Constructs'),
               dict(title='BashGuide — Loops', url='https://mywiki.wooledge.org/BashGuide/Loops'),
               dict(title='Brace Expansion', url='https://www.gnu.org/software/bash/manual/bash.html#Brace-Expansion')]),
    dict(slug='bash-05-functions', title='Functions',
         desc='Defining functions, arguments, return values, and reusable helpers.',
         dur='45 min', diff='intermediate', prereq=['BASH-04'],
         objs=['Define and call functions',
               'Return exit status and data',
               'Use local variables and defaults',
               'Build reusable helper functions'],
         refs=[dict(title='Bash — Shell Functions', url='https://www.gnu.org/software/bash/manual/bash.html#Shell-Functions'),
               dict(title='BashGuide — Functions', url='https://mywiki.wooledge.org/BashGuide/Functions'),
               dict(title='Advanced Bash-Scripting — Functions', url='https://tldp.org/LDP/abs/html/functions.html')]),
    dict(slug='bash-06-strings', title='String Manipulation',
         desc='Length, substring, pattern removal, replacement, and defaults.',
         dur='60 min', diff='intermediate', prereq=['BASH-05'],
         objs=['Compute length and concatenate',
               'Extract substrings',
               'Replace and transform patterns',
               'Apply parameter expansion defaults'],
         refs=[dict(title='Bash — Parameter Expansion', url='https://www.gnu.org/software/bash/manual/bash.html#Shell-Parameter-Expansion'),
               dict(title='BashGuide — Parameter Expansion', url='https://mywiki.wooledge.org/BashGuide/Parameters'),
               dict(title='Parameter Expansion Cheat Sheet', url='https://devhints.io/bash')]),
    dict(slug='bash-07-arrays', title='Arrays and Associative Arrays',
         desc='Indexed arrays, associative arrays, slicing, and safe copying.',
         dur='60 min', diff='intermediate', prereq=['BASH-06'],
         objs=['Build and index arrays',
               'Use associative arrays',
               'Slice and append arrays',
               'Read files into arrays with mapfile'],
         refs=[dict(title='Bash — Arrays', url='https://www.gnu.org/software/bash/manual/bash.html#Arrays'),
               dict(title='BashGuide — Arrays', url='https://mywiki.wooledge.org/BashGuide/Arrays'),
               dict(title='mapfile builtin', url='https://www.gnu.org/software/bash/manual/bash.html#index-mapfile')]),
    dict(slug='bash-08-files-pipes', title='Files, Pipes, and Redirection',
         desc='Pipelines, stdout/stderr redirection, here-docs, and process substitution.',
         dur='60 min', diff='intermediate', prereq=['BASH-07'],
         objs=['Build pipelines with pipefail',
               'Redirect stdout and stderr',
               'Use here-documents and here-strings',
               'Leverage process substitution'],
         refs=[dict(title='Bash — Pipelines', url='https://www.gnu.org/software/bash/manual/bash.html#Pipelines'),
               dict(title='Bash — Redirections', url='https://www.gnu.org/software/bash/manual/bash.html#Redirections'),
               dict(title='Here Documents', url='https://www.gnu.org/software/bash/manual/bash.html#Here-Documents')]),
    dict(slug='bash-09-globbing-regex', title='Globbing and Regular Expressions',
         desc='Glob patterns, extended globs, grep, sed, and awk fundamentals.',
         dur='60 min', diff='intermediate', prereq=['BASH-08'],
         objs=['Match files with glob patterns',
               'Search with grep regexes',
               'Edit streams with sed',
               'Process columns with awk'],
         refs=[dict(title='Bash — Filename Expansion', url='https://www.gnu.org/software/bash/manual/bash.html#Filename-Expansion'),
               dict(title='grep manual', url='https://man7.org/linux/man-pages/man1/grep.1.html'),
               dict(title='sed — a stream editor', url='https://www.gnu.org/software/sed/manual/sed.html')]),
    dict(slug='bash-10-text-processing', title='Text Processing Toolkit',
         desc='sort, uniq, cut, wc, head, tail, xargs, join, paste, tr.',
         dur='60 min', diff='intermediate', prereq=['BASH-09'],
         objs=['Sort and deduplicate with uniq',
               'Slice columns and lines',
               'Run commands from stdin with xargs',
               'Combine files with join and paste'],
         refs=[dict(title='coreutils manual', url='https://www.gnu.org/software/coreutils/manual/'),
               dict(title='xargs manual', url='https://man7.org/linux/man-pages/man1/xargs.1.html'),
               dict(title='Command Line Text Processing', url='https://learnbyexample.github.io/')]),
    dict(slug='bash-11-error-handling', title='Error Handling',
         desc='set -euo pipefail, trap, robust patterns, and exit codes.',
         dur='60 min', diff='intermediate', prereq=['BASH-10'],
         objs=['Exit on errors with set -e',
               'Clean up with trap',
               'Apply robust error patterns',
               'Handle exit codes explicitly'],
         refs=[dict(title='Bash — The Set Builtin', url='https://www.gnu.org/software/bash/manual/bash.html#The-Set-Builtin'),
               dict(title='BashGuide — Error Handling', url='https://mywiki.wooledge.org/BashGuide/Practices'),
               dict(title='ShellCheck — useful patterns', url='https://www.shellcheck.net/wiki/')]),
    dict(slug='bash-12-process-management', title='Process Management',
         desc='Background jobs, wait, kill, pgrep, and job control.',
         dur='60 min', diff='intermediate', prereq=['BASH-11'],
         objs=['Run jobs in the background',
               'Manage jobs with fg/bg/kill',
               'Use nohup and disown',
               'Probe processes with pgrep'],
         refs=[dict(title='Bash — Job Control', url='https://www.gnu.org/software/bash/manual/bash.html#Job-Control'),
               dict(title='pgrep manual', url='https://man7.org/linux/man-pages/man1/pgrep.1.html'),
               dict(title='kill manual', url='https://man7.org/linux/man-pages/man1/kill.1.html')]),
    dict(slug='bash-13-command-line', title='Command-Line Argument Parsing',
         desc='Positional params, getopts, shift, and flag loops.',
         dur='60 min', diff='intermediate', prereq=['BASH-12'],
         objs=['Use positional parameters',
               'Parse options with getopts',
               'Shift through arguments',
               'Handle flags with case loops'],
         refs=[dict(title='Bash — Positional Parameters', url='https://www.gnu.org/software/bash/manual/bash.html#Positional-Parameters'),
               dict(title='getopts builtin', url='https://www.gnu.org/software/bash/manual/bash.html#index-getopts'),
               dict(title='BashGuide — Parameters', url='https://mywiki.wooledge.org/BashGuide/Parameters')]),
    dict(slug='bash-14-environment-config', title='Environment and Configuration',
         desc='Env vars, exports, dotfiles, sourcing, and shell modes.',
         dur='60 min', diff='intermediate', prereq=['BASH-13'],
         objs=['Read and set environment variables',
               'Export to child processes',
               'Manage dotfiles and sourcing',
               'Detect shell interaction modes'],
         refs=[dict(title='Bash — Bash Startup Files', url='https://www.gnu.org/software/bash/manual/bash.html#Bash-Startup-Files'),
               dict(title='Environment Variables', url='https://man7.org/linux/man-pages/man7/environ.7.html'),
               dict(title='Dotfiles guide', url='https://dotfiles.github.io/')]),
    dict(slug='bash-15-io-redirection', title='Advanced I/O and Redirection',
         desc='File descriptors, /dev/null, safe file reads, and named pipes.',
         dur='75 min', diff='advanced', prereq=['BASH-14'],
         objs=['Manipulate file descriptors',
               'Use /dev/null and /dev/zero',
               'Read files safely with while-read',
               'Build FIFOs and named pipes'],
         refs=[dict(title='Bash — Redirections', url='https://www.gnu.org/software/bash/manual/bash.html#Redirections'),
               dict(title='File descriptor overview', url='https://en.wikipedia.org/wiki/File_descriptor'),
               dict(title='mkfifo manual', url='https://man7.org/linux/man-pages/man1/mkfifo.1.html')]),
    dict(slug='bash-16-json-yaml', title='JSON and Data Parsing',
         desc='jq for JSON: queries, transforms, building, and validation.',
         dur='75 min', diff='advanced', prereq=['BASH-15'],
         objs=['Query JSON with jq',
               'Filter and transform with jq',
               'Build JSON payloads',
               'Validate JSON in scripts'],
         refs=[dict(title='jq manual', url='https://jqlang.github.io/jq/manual/'),
               dict(title='jq Cookbook', url='https://github.com/stedolan/jq/wiki/Cookbook'),
               dict(title='yq (YAML)', url='https://github.com/mikefarah/yq')]),
    dict(slug='bash-17-concurrency', title='Concurrency and Parallelism',
         desc='xargs -P, parallel, background fan-out, subshells, and coprocesses.',
         dur='75 min', diff='advanced', prereq=['BASH-16'],
         objs=['Parallelize with xargs',
               'Fan out with background jobs',
               'Understand subshell semantics',
               'Use coprocesses'],
         refs=[dict(title='GNU parallel', url='https://www.gnu.org/software/parallel/'),
               dict(title='Bash — Command Execution', url='https://www.gnu.org/software/bash/manual/bash.html#Command-Execution-Environment'),
               dict(title='Bash — Coprocesses', url='https://www.gnu.org/software/bash/manual/bash.html#Coprocesses')]),
    dict(slug='bash-18-scripting-patterns', title='Production Scripting Patterns',
         desc='Library scripts, dry-run, logging, and idempotency.',
         dur='75 min', diff='advanced', prereq=['BASH-17'],
         objs=['Structure maintainable scripts',
               'Implement dry-run mode',
               'Log with levels',
               'Make scripts idempotent'],
         refs=[dict(title='BashGuide — Practices', url='https://mywiki.wooledge.org/BashGuide/Practices'),
               dict(title='12-factor CLI apps', url='https://clig.dev/'),
               dict(title='The Bash Hackers Wiki', url='https://wiki.bash-hackers.org/')]),
    dict(slug='bash-19-performance', title='Performance',
         desc='Builtins over forks, timing, profiling, and caching.',
         dur='75 min', diff='advanced', prereq=['BASH-18'],
         objs=['Avoid external process forks',
               'Time and profile scripts',
               'Batch work into single passes',
               'Cache expensive results'],
         refs=[dict(title='Bash — Why builtins are faster', url='https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins'),
               dict(title='Bash pitfalls (BashPitfalls)', url='https://mywiki.wooledge.org/BashPitfalls'),
               dict(title='time — GNU manual', url='https://www.gnu.org/software/time/')]),
    dict(slug='bash-20-security', title='Security',
         desc='Quoting against injection, shellcheck, secrets, and privilege checks.',
         dur='75 min', diff='advanced', prereq=['BASH-19'],
         objs=['Prevent injection with quoting',
               'Apply shellcheck rules',
               'Handle secrets safely',
               'Check privileges and temp files'],
         refs=[dict(title='ShellCheck wiki', url='https://www.shellcheck.net/wiki/'),
               dict(title='OWASP Shell Injection', url='https://owasp.org/www-community/attacks/Command_Injection'),
               dict(title='mktemp manual', url='https://man7.org/linux/man-pages/man1/mktemp.1.html')]),
    dict(slug='bash-21-advanced', title='Advanced Bash: Regex, Substitution, and Completion',
         desc='BASH_REMATCH, process substitution tricks, completions, and checklists.',
         dur='75 min', diff='expert', prereq=['BASH-20'],
         objs=['Capture with BASH_REMATCH',
               'Use /dev/fd and substitution tricks',
               'Register completion functions',
               'Apply the production checklist'],
         refs=[dict(title='Bash — The Shopt Builtin', url='https://www.gnu.org/software/bash/manual/bash.html#The-Shopt-Builtin'),
               dict(title='BashFAQ', url='https://mywiki.wooledge.org/BashFAQ'),
               dict(title='Programmable Completion', url='https://www.gnu.org/software/bash/manual/bash.html#Programmable-Completion')]),
]


if __name__ == '__main__':
    run_gen(LANGUAGE, 'bash', LESSONS, CODE, BASE)
