#!/usr/bin/env python3
"""Generate the 21-lesson C# curriculum at Python/JS/Java depth.
Creates static-data/knowledge/languages/csharp/*.md + updates index.json lessons.
Exact sub-topic references from learn.microsoft.com.
Each lesson has 4 sub-topics, each with its OWN distinct code sample.
"""

import json
import os

BASE = os.path.join(os.path.dirname(__file__), '..', '..', 'static-data', 'knowledge', 'languages', 'csharp')

# ─── Per-lesson: 4 sub-topic code samples (real C#, distinct per sub-topic) ───
CODE = {
    1: [
'''using System;

// .NET SDK toolchain: dotnet new console, dotnet build, dotnet run
Console.WriteLine("Hello, 100X Systems!");
Console.WriteLine($"Args: {args.Length}");''',
'''var sln = "app.sln";             // solution file groups projects
// dotnet new sln, dotnet sln add, dotnet build, dotnet run
Console.WriteLine(Path.GetFileName(sln));''',
'''namespace HelloWorld;           // file-scoped namespace (C# 10+)

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Top-level statements avoid this boilerplate");
    }
}''',
'''// Top-level statements: minimal entry point
Console.WriteLine("Hello from top-level statements!");
Console.WriteLine("dotnet run compiles + executes in one step");''',
    ],
    2: [
'''int age = 30;                  // value type: stack-allocated
bool isActive = true;
char grade = 'A';
decimal price = 19.99m;         // exact decimal arithmetic
Console.WriteLine($"{age} {isActive} {grade} {price}");''',
'''string name = "Alice";         // reference type: heap + GC
int[] nums = { 1, 2, 3 };       // reference type (array)
Console.WriteLine($"name: {name}, nums: {nums.Length}");''',
'''var x = 42;                    // var infers int
var y = "hello";                // var infers string
dynamic d = "anything";         // dynamic resolves at runtime
Console.WriteLine($"{x.GetType()} {y.GetType()} {d}");''',
'''int i = default;               // 0
bool b = default;               // false
string? s = default;            // null
Console.WriteLine($"{i} {b} {s is null}");''',
    ],
    3: [
'''int a = 17, b = 5;
Console.WriteLine(a + b);       // 22
Console.WriteLine(a - b);       // 12
Console.WriteLine(a * b);       // 85
Console.WriteLine(a / b);       // 3 (integer division)
Console.WriteLine(a % b);       // 2 (remainder)''',
'''double x = 17.0, y = 5.0;
Console.WriteLine(x / y);       // 3.4
Console.WriteLine(x == y);      // false
Console.WriteLine(x > y);       // true
bool both = x > 0 && y > 0;     // logical AND
bool either = x > 100 || y > 0; // logical OR''',
'''int? maybe = null;
int fallback = maybe ?? 42;     // null-coalescing
int cond = fallback > 40 ? 1 : 0; // ternary
Console.WriteLine($"{fallback} {cond}");''',
'''int flags = 0b1100;            // 12
Console.WriteLine(flags & 0b1010); // 1000 = 8 (AND)
Console.WriteLine(flags | 0b0001); // 1101 = 13 (OR)
Console.WriteLine(flags << 1);     // 11000 = 24 (shift left)''',
    ],
    4: [
'''int score = 85;
if (score >= 90) Console.WriteLine("A");
else if (score >= 80) Console.WriteLine("B");
else Console.WriteLine("C");''',
'''int day = 3;
string name = day switch
{
    1 => "Monday",
    2 => "Tuesday",
    _ => "Other"
};
Console.WriteLine(name);''',
'''for (int i = 0; i < 3; i++) Console.Write(i);       // 012
foreach (var c in "abc") Console.Write(c);           // abc
int j = 0;
while (j < 2) { Console.Write(j); j++; }             // 01
do { Console.Write("run"); } while (false);          // runs once''',
'''for (int i = 0; i < 10; i++)
{
    if (i == 2) continue;      // skip 2
    if (i == 5) break;         // stop at 5
    Console.Write(i);          // 0134
}''',
    ],
    5: [
'''static int Add(int a, int b) => a + b;
static void Greet(string name) => Console.WriteLine($"Hi {name}");
Console.WriteLine(Add(2, 3));
Greet("Alice");''',
'''static void Swap(ref int x, ref int y)
{
    (x, y) = (y, x);
}
int a = 1, b = 2;
Swap(ref a, ref b);
Console.WriteLine($"{a} {b}");  // 2 1''',
'''static bool TryParseNum(string s, out int result)
{
    return int.TryParse(s, out result);
}
if (TryParseNum("42", out int n)) Console.WriteLine(n);''',
'''static int Sum(params int[] nums) => nums.Sum();
static string Label(string name = "guest") => name;
Console.WriteLine(Sum(1, 2, 3, 4));     // 10
Console.WriteLine(Label());              // guest
Console.WriteLine(Label(name: "Bob"));  // named arg''',
    ],
    6: [
'''int[] nums = { 5, 3, 1 };
Array.Sort(nums);
Console.WriteLine(string.Join(",", nums));  // 1,3,5
int[,] grid = { { 1, 2 }, { 3, 4 } };
Console.WriteLine(grid[1, 0]);             // 3''',
'''var list = new List<string> { "a" };
list.Add("b");
list.Insert(0, "z");
list.Remove("a");
Console.WriteLine(string.Join(",", list)); // z,b''',
'''var dict = new Dictionary<string, int>
{
    ["one"] = 1,
    ["two"] = 2
};
dict["three"] = 3;
Console.WriteLine(dict.ContainsKey("two"));   // True
Console.WriteLine(dict.GetValueOrDefault("x")); // 0''',
'''var queue = new Queue<int>();
queue.Enqueue(1); queue.Enqueue(2);
Console.WriteLine(queue.Dequeue());   // 1 (FIFO)

var stack = new Stack<int>();
stack.Push(1); stack.Push(2);
Console.WriteLine(stack.Pop());       // 2 (LIFO)''',
    ],
    7: [
'''string greeting = "Hello";
string who = "World";
string msg = greeting + ", " + who + "!";  // concatenation
Console.WriteLine(msg);''',
'''string name = "World";
string msg = $"Hello, {name}!";
Console.WriteLine(msg);
Console.WriteLine($"Pi is {Math.PI:F2}");   // formatted''',
'''var sb = new System.Text.StringBuilder();
for (int i = 0; i < 3; i++) sb.Append(i).Append("-");
Console.WriteLine(sb.ToString().TrimEnd('-')); // 0-1-2''',
'''string text = "Hello World";
Console.WriteLine(text.ToUpper());         // HELLO WORLD
Console.WriteLine(text.Contains("World")); // True
Console.WriteLine(text[0..5]);             // Hello (range)
Console.WriteLine(text.Split(' ').Length); // 2''',
    ],
    8: [
'''class BankAccount
{
    public decimal Balance { get; private set; }
    public BankAccount(decimal initial) => Balance = initial;
    public void Deposit(decimal amount) => Balance += amount;
}
var acct = new BankAccount(100m);
acct.Deposit(50m);
Console.WriteLine(acct.Balance);   // 150''',
'''class Point
{
    public int X { get; }
    public int Y { get; }
    public Point(int x, int y) { X = x; Y = y; }
    public override string ToString() => $"({X}, {Y})";
}
Console.WriteLine(new Point(3, 4));  // (3, 4)''',
'''class Counter
{
    public static int Instances { get; private set; }
    public Counter() => Instances++;
    public static void Describe() => Console.WriteLine($"Count: {Instances}");
}
new Counter(); new Counter();
Counter.Describe();   // Count: 2 (static, no instance)''',
'''var p = new Point(1, 2);
p = new Point { X = 5, Y = 6 };   // re-assign (immutable props)
var list = new List<Point> { new(0, 0), new(1, 1) };
Console.WriteLine(list.Count);''',
    ],
    9: [
'''class Temperature
{
    public double Celsius { get; set; }
    public double Fahrenheit => Celsius * 9 / 5 + 32;
}
var t = new Temperature { Celsius = 25 };
Console.WriteLine($"{t.Fahrenheit:F1}°F");  // 77.0°F''',
'''class Person
{
    private string _name = "";
    public string Name
    {
        get => _name;
        set => _name = string.IsNullOrWhiteSpace(value) ? "unknown" : value;
    }
}
var p = new Person { Name = "" };
Console.WriteLine(p.Name);  // unknown''',
'''class Matrix
{
    private readonly int[,] _data;
    public Matrix(int[,] data) => _data = data;
    public int this[int r, int c] => _data[r, c];
}
var m = new Matrix(new int[,] { { 1, 2 }, { 3, 4 } });
Console.WriteLine(m[1, 0]);   // 3 (indexer)''',
'''class Stats
{
    public int Count { get; init; }   // init-only (set at construction)
    public string Name { get; set; } = "default";
}
var s = new Stats { Count = 5, Name = "x" };
Console.WriteLine($"{s.Count} {s.Name}");''',
    ],
    10: [
'''class Animal { public virtual string Speak() => "..."; }
class Dog : Animal { public override string Speak() => "Woof"; }
Console.WriteLine(new Dog().Speak());  // Woof''',
'''class Animal { public virtual string Speak() => "..."; }
class Dog : Animal { public override string Speak() => "Woof"; }
class Cat : Animal { public override string Speak() => "Meow"; }

Animal[] animals = { new Dog(), new Cat() };
foreach (var a in animals) Console.WriteLine(a.Speak());''',
'''class Base { protected int _x; public Base(int x) => _x = x; }
class Derived : Base
{
    public Derived(int x) : base(x) { }
    public void Show() => Console.WriteLine(_x);
}
new Derived(7).Show();  // 7 (protected member)''',
'''class SealedOne { public void Do() { } }
// sealed class: cannot be inherited
class Final : SealedOne { }
Console.WriteLine(typeof(Final).Name);''',
    ],
    11: [
'''interface IShape { double Area(); }
class Square : IShape
{
    public double Side { get; set; }
    public double Area() => Side * Side;
}
IShape s = new Square { Side = 4 };
Console.WriteLine(s.Area());  // 16 (interface reference)''',
'''interface ILogger { void Log(string msg); }
class ConsoleLogger : ILogger
{
    public void Log(string msg) => Console.WriteLine($"[LOG] {msg}");
}
new ConsoleLogger().Log("hello");''',
'''abstract class Shape
{
    public abstract double Area();          // no body
    public string Describe() => "a shape";  // concrete
}
class Circle : Shape
{
    public double Radius { get; set; }
    public override double Area() => Math.PI * Radius * Radius;
}
Console.WriteLine(new Circle { Radius = 2 }.Area());''',
'''interface IA { void A(); }
interface IB { void B(); }
class Both : IA, IB   // multiple interface implementation
{
    public void A() => Console.WriteLine("A");
    public void B() => Console.WriteLine("B");
}
Both b = new(); b.A(); b.B();''',
    ],
    12: [
'''class Box<T>
{
    public T Value { get; set; } = default!;
}
var intBox = new Box<int> { Value = 42 };
var strBox = new Box<string> { Value = "hi" };
Console.WriteLine($"{intBox.Value} {strBox.Value}");''',
'''static T Max<T>(T a, T b) where T : IComparable<T>
    => a.CompareTo(b) >= 0 ? a : b;
Console.WriteLine(Max(3, 9));            // 9
Console.WriteLine(Max("apple", "pear")); // pear''',
'''class Repository<T> where T : class, new()
{
    private readonly List<T> _items = new();
    public void Add(T item) => _items.Add(item);
    public int Count => _items.Count;
}
var repo = new Repository<string>();
repo.Add("a");
Console.WriteLine(repo.Count);  // 1''',
'''// Covariance: IEnumerable<Derived> is IEnumerable<Base>
IEnumerable<string> strings = new[] { "a", "b" };
IEnumerable<object> objs = strings;   // OK (out T)
foreach (var o in objs) Console.WriteLine(o);''',
    ],
    13: [
'''var nums = new[] { 1, 2, 3, 4 };
var evens = nums.Where(n => n % 2 == 0);        // method syntax
var doubled = nums.Select(n => n * 2);
Console.WriteLine(string.Join(",", evens));     // 2,4
Console.WriteLine(string.Join(",", doubled));   // 2,4,6,8''',
'''var people = new[] { new { Name = "Alice", Age = 30 }, new { Name = "Bob", Age = 25 } };
var query = from p in people              // query syntax
            where p.Age >= 25
            orderby p.Age descending
            select p.Name;
foreach (var n in query) Console.WriteLine(n);  // Alice, Bob''',
'''var nums = new[] { 1, 2, 3, 4, 5 };
Console.WriteLine(nums.Sum());          // 15
Console.WriteLine(nums.Average());      // 3
Console.WriteLine(nums.Min());          // 1
Console.WriteLine(nums.Max());          // 5
Console.WriteLine(nums.Count(n => n > 2)); // 3''',
'''// Deferred execution: query runs when enumerated
var q = nums.Where(n => n > 2);
nums = nums.Append(9).ToArray();        // 9 not in q yet
Console.WriteLine(string.Join(",", q)); // 3,4,5
var eager = nums.Where(n => n > 2).ToList();  // immediate''',
    ],
    14: [
'''delegate int MathOp(int a, int b);
MathOp add = (a, b) => a + b;
Console.WriteLine(add(5, 3));  // 8''',
'''// Multicast: += chains invocations
Action<string> log = m => Console.WriteLine($"[A] {m}");
log += m => Console.WriteLine($"[B] {m}");
log("hello");
// [A] hello
// [B] hello''',
'''class Button
{
    public event EventHandler? Clicked;
    public void Press() => Clicked?.Invoke(this, EventArgs.Empty);
}
var btn = new Button();
btn.Clicked += (s, e) => Console.WriteLine("Clicked!");
btn.Press();   // Clicked!''',
'''Func<int, int> square = x => x * x;
Func<int, int, int> add = (a, b) => a + b;
var nums = new[] { 1, 2, 3 };
Console.WriteLine(nums.Select(square).Sum()); // 14
Console.WriteLine(add(2, 3));                 // 5''',
    ],
    15: [
'''try
{
    int.Parse("not-a-number");
}
catch (FormatException ex)
{
    Console.WriteLine($"Format: {ex.Message}");
}
finally
{
    Console.WriteLine("Cleanup always runs");
}''',
'''try
{
    throw new InvalidOperationException("custom failure");
}
catch (InvalidOperationException) when (DateTime.Now.Day > 0)  // filter
{
    Console.WriteLine("Filtered catch");
}''',
'''class ValidationException : Exception
{
    public ValidationException(string field) : base($"Invalid: {field}") { }
}
try { throw new ValidationException("email"); }
catch (ValidationException ex) { Console.WriteLine(ex.Message); }''',
'''static int SafeDivide(int a, int b) =>
    b == 0 ? throw new DivideByZeroException() : a / b;
try { Console.WriteLine(SafeDivide(4, 0)); }
catch (DivideByZeroException) { Console.WriteLine("Cannot divide by zero"); }''',
    ],
    16: [
'''async Task<string> FetchAsync(HttpClient client, string url)
{
    return await client.GetStringAsync(url);
}
using var http = new HttpClient();
string html = await FetchAsync(http, "https://example.com");
Console.WriteLine($"Fetched {html.Length} chars");''',
'''static async Task<int> DelayCountAsync()
{
    await Task.Delay(100);
    return 42;
}
int result = await DelayCountAsync();
Console.WriteLine(result);  // 42 (non-blocking await)''',
'''// Parallel: run independent tasks concurrently
Task<int> t1 = Task.Run(() => { Task.Delay(50).Wait(); return 1; });
Task<int> t2 = Task.Run(() => { Task.Delay(50).Wait(); return 2; });
int[] results = await Task.WhenAll(t1, t2);
Console.WriteLine(results.Sum());  // 3''',
'''try
{
    await Task.Run(() => throw new InvalidOperationException("boom"));
}
catch (InvalidOperationException ex)
{
    Console.WriteLine($"Caught: {ex.Message}");  // async error propagation
}''',
    ],
    17: [
'''using System.IO;
string path = "/tmp/notes.txt";
File.WriteAllText(path, "hello");
Console.WriteLine(File.ReadAllText(path));  // hello''',
'''await File.WriteAllTextAsync(path, "async write");
string content = await File.ReadAllTextAsync(path);
Console.WriteLine(content);''',
'''using var reader = new StreamReader(path);
string? line;
while ((line = await reader.ReadLineAsync()) != null)
    Console.WriteLine(line);

using var writer = new StreamWriter("/tmp/out.txt");
await writer.WriteLineAsync("line 1");''',
'''using var fs = new FileStream("/tmp/data.bin", FileMode.Create);
byte[] bytes = { 1, 2, 3, 4 };
await fs.WriteAsync(bytes);
fs.Position = 0;
byte[] buffer = new byte[4];
await fs.ReadAsync(buffer);
Console.WriteLine(string.Join(",", buffer));  // 1,2,3,4''',
    ],
    18: [
'''static IEnumerable<int> Fib()
{
    int a = 0, b = 1;
    while (true) { yield return a; (a, b) = (b, a + b); }
}
foreach (var f in Fib().Take(8)) Console.Write($"{f} ");  // 0 1 1 2 3 5 8 13''',
'''static IEnumerable<int> Range(int start, int count)
{
    for (int i = 0; i < count; i++) yield return start + i;
}
var r = Range(10, 3);  // nothing runs yet (lazy)
Console.WriteLine(string.Join(",", r));  // 10,11,12''',
'''// IEnumerable<T> = read-only forward iteration
IEnumerable<int> seq = new[] { 1, 2, 3 };
var e = seq.GetEnumerator();
while (e.MoveNext()) Console.Write(e.Current);  // 123''',
'''// Span<T>: allocation-free slice over contiguous memory
Span<int> span = stackalloc int[] { 1, 2, 3, 4 };
var slice = span[1..3];
Console.WriteLine(string.Join(",", slice.ToArray()));  // 2,3''',
    ],
    19: [
'''int? count = null;               // Nullable<int>
Console.WriteLine(count.HasValue);       // False
Console.WriteLine(count ?? 5);           // 5
count = 3;
Console.WriteLine(count.Value);          // 3''',
'''string? name = null;             // nullable reference type
Console.WriteLine(name?.Length ?? 0);   // 0 (safe navigation)''',
'''object value = 42;
if (value is int i) Console.WriteLine($"int: {i}");      // type pattern
if (value is not string) Console.WriteLine("not a string");
if (value is int n && n > 0) Console.WriteLine("positive");''',
'''string shape = "circle";
string describe = shape switch
{
    "circle" => "round",
    "square" => "four sides",
    _ => "unknown"
};
Console.WriteLine(describe);  // round

object? maybe = null;
var result = maybe switch
{
    null => "null",
    int x when x > 100 => "big",
    _ => "other"
};''',
    ],
    20: [
'''record Person(string Name, int Age);
var alice = new Person("Alice", 30);
Console.WriteLine(alice);   // Person { Name = Alice, Age = 30 }
Console.WriteLine(alice == new Person("Alice", 30));  // True (value eq)''',
'''record Person(string Name, int Age);
var alice = new Person("Alice", 30);
var bob = alice with { Age = 31 };   // non-destructive copy
Console.WriteLine(bob);   // Person { Name = Alice, Age = 31 }''',
'''var tuple = (Name: "Alice", Age: 30);   // named tuple
Console.WriteLine($"{tuple.Name} {tuple.Age}");
var (name, age) = tuple;                 // deconstruction
Console.WriteLine($"{name} {age}");''',
'''struct Point
{
    public int X { get; set; }
    public int Y { get; set; }
}
// structs are value types: copies on assignment
Point p1 = new() { X = 1, Y = 2 };
Point p2 = p1;
p2.X = 99;
Console.WriteLine(p1.X);  // 1 (p2 is a copy)''',
    ],
    21: [
'''var type = typeof(string);
Console.WriteLine(type.Name);       // String
Console.WriteLine(type.IsSealed);   // True
foreach (var m in type.GetMethods().Take(5))
    Console.WriteLine(m.Name);''',
'''[AttributeUsage(AttributeTargets.Class)]
class DeprecatedAttribute : Attribute
{
    public string Reason { get; }
    public DeprecatedAttribute(string reason) => Reason = reason;
}

[Deprecated("use NewApi instead")]
class OldApi { }
var attr = typeof(OldApi).GetCustomAttributes(typeof(DeprecatedAttribute), false)[0]
    as DeprecatedAttribute;
Console.WriteLine(attr?.Reason);''',
'''unsafe
{
    int value = 42;
    int* p = &value;          // pointer to value
    Console.WriteLine(*p);    // 42
}
// compile with: dotnet build /unsafe or <AllowUnsafeBlocks>true</AllowUnsafeBlocks>''',
'''// GC: managed heap, generations, finalizers
var obj = new object();
var weak = new WeakReference(obj);
obj = null;
GC.Collect();
Console.WriteLine(weak.IsAlive);  // usually False after collection

// deterministic disposal
using var resource = new MemoryStream();
Console.WriteLine(resource.Length);''',
    ],
}

# ─── Lesson metadata ──────────────────────────────────────────────────
LESSONS = [
    dict(slug='cs-01-getting-started', title='Getting Started with C# and the .NET CLI',
         desc='Install the .NET SDK, understand dotnet CLI (new/build/run), project structure, and write Hello World.',
         dur='45 min', diff='beginner', prereq=[],
         objs=['Install the .NET SDK and set up the toolchain',
               'Understand dotnet new / build / run lifecycle',
               'Understand project structure and namespaces',
               'Write and run your first C# program'],
         refs=[dict(title='Tour of C# Overview', url='https://learn.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/overview'),
               dict(title='Get Started with C#', url='https://learn.microsoft.com/en-us/dotnet/csharp/getting-started/'),
               dict(title='dotnet CLI Overview', url='https://learn.microsoft.com/en-us/dotnet/core/tools/')]),
    dict(slug='cs-02-variables-types', title='Variables and Built-in Types',
         desc='Value vs reference types, var inference, built-in numeric types, and default values.',
         dur='60 min', diff='beginner', prereq=['CS-01'],
         objs=['Understand value vs reference type semantics',
               'Use built-in numeric, bool, char, and string types',
               'Use var type inference correctly',
               'Understand default values and literals'],
         refs=[dict(title='C# Types System', url='https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/'),
               dict(title='Built-in Types', url='https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types'),
               dict(title='Value Types Reference', url='https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/value-types')]),
    dict(slug='cs-03-operators-expressions', title='Operators and Expressions',
         desc='Arithmetic, comparison, logical, bitwise operators; precedence and null-coalescing.',
         dur='60 min', diff='beginner', prereq=['CS-02'],
         objs=['Use arithmetic, comparison, and logical operators',
               'Use the ternary and null-coalescing operators',
               'Use bitwise operators for flags and bit tricks',
               'Understand precedence and associativity'],
         refs=[dict(title='C# Operators Reference', url='https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/'),
               dict(title='Operator Precedence', url='https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/#operator-precedence'),
               dict(title='Numeric Conversions', url='https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/numeric-conversions')]),
    dict(slug='cs-04-control-flow', title='Control Flow and Switch Expressions',
         desc='if/else, switch statements and expressions, loops, and jump statements.',
         dur='60 min', diff='beginner', prereq=['CS-03'],
         objs=['Write if/else branching logic',
               'Use switch statements and switch expressions',
               'Use for, foreach, while, and do-while loops',
               'Apply break, continue, and return control keywords'],
         refs=[dict(title='Selection Statements', url='https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/selection-statements'),
               dict(title='Iteration Statements', url='https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/iteration-statements'),
               dict(title='Jump Statements', url='https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/jump-statements')]),
    dict(slug='cs-05-methods', title='Methods and Parameters',
         desc='Method signatures, ref/out/in params, params arrays, named and optional arguments.',
         dur='60 min', diff='beginner', prereq=['CS-04'],
         objs=['Declare methods with return types and parameters',
               'Use ref, out, and in parameter modifiers',
               'Use params arrays for variable argument counts',
               'Use named and optional arguments'],
         refs=[dict(title='C# Methods Guide', url='https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/methods'),
               dict(title='Method Parameters', url='https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/method-parameters'),
               dict(title='ref Keyword', url='https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/ref')]),
    dict(slug='cs-06-collections', title='Arrays, Lists, and Collections',
         desc='Arrays, List<T>, Dictionary<TKey,TValue>, Queue, Stack; collection initializers.',
         dur='60 min', diff='beginner', prereq=['CS-05'],
         objs=['Work with single and multi-dimensional arrays',
               'Use List<T> and common collection methods',
               'Use Dictionary<TKey,TValue> for keyed lookup',
               'Use Queue and Stack for ordered processing'],
         refs=[dict(title='Collections Overview', url='https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/collections'),
               dict(title='Array Guide', url='https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/arrays/'),
               dict(title='Generic Collections', url='https://learn.microsoft.com/en-us/dotnet/standard/collections/generic/')]),
    dict(slug='cs-07-strings', title='Strings and String Interpolation',
         desc='String immutability, interpolation, StringBuilder, and common string methods.',
         dur='60 min', diff='beginner', prereq=['CS-06'],
         objs=['Understand string immutability',
               'Use string interpolation and formatting',
               'Use StringBuilder for efficient concatenation',
               'Master common string methods and slicing'],
         refs=[dict(title='String Concatenation', url='https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/strings/common-tasks/concatenate'),
               dict(title='String Interpolation', url='https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/interpolated'),
               dict(title='StringBuilder Class', url='https://learn.microsoft.com/en-us/dotnet/api/system.text.stringbuilder')]),
    dict(slug='cs-08-classes-objects', title='Classes and Objects',
         desc='Class declarations, constructors, this, static members, and object initializers.',
         dur='75 min', diff='beginner', prereq=['CS-07'],
         objs=['Declare classes with fields, properties, and methods',
               'Write constructors and overloads',
               'Use static members and classes',
               'Use object and collection initializers'],
         refs=[dict(title='OOP in C#', url='https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/object-oriented/'),
               dict(title='Classes and Structs', url='https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/classes'),
               dict(title='Constructors', url='https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/constructors')]),
    dict(slug='cs-09-properties', title='Properties, Indexers, and Fields',
         desc='Auto-properties, get/set accessors, computed properties, and indexers.',
         dur='60 min', diff='intermediate', prereq=['CS-08'],
         objs=['Implement auto-implemented properties',
               'Write custom get/set accessors with validation logic',
               'Implement indexers for indexed access',
               'Use init-only and expression-bodied members'],
         refs=[dict(title='C# Properties', url='https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/properties'),
               dict(title='Indexers', url='https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/indexers/'),
               dict(title='Auto-Implemented Properties', url='https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/auto-implemented-properties')]),
    dict(slug='cs-10-inheritance', title='Inheritance and Polymorphism',
         desc='Base and derived classes, virtual/override, protected members, sealed.',
         dur='75 min', diff='intermediate', prereq=['CS-09'],
         objs=['Create base and derived classes',
               'Override virtual methods with override',
               'Access base members through protected and base',
               'Use sealed to prevent inheritance'],
         refs=[dict(title='Inheritance in C#', url='https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/object-oriented/inheritance'),
               dict(title='Polymorphism', url='https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/object-oriented/polymorphism'),
               dict(title='virtual Keyword', url='https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/virtual')]),
    dict(slug='cs-11-interfaces', title='Interfaces and Abstract Classes',
         desc='Interface contracts, abstract classes, multiple interface implementation.',
         dur='75 min', diff='intermediate', prereq=['CS-10'],
         objs=['Define and implement interfaces',
               'Use interfaces as type abstractions',
               'Use abstract classes for shared implementation',
               'Implement multiple interfaces on one type'],
         refs=[dict(title='Interfaces Guide', url='https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/interfaces'),
               dict(title='Abstract Classes', url='https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/abstract'),
               dict(title='Default Interface Methods', url='https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/tutorials/default-interface-methods-versions')]),
    dict(slug='cs-12-generics', title='Generics',
         desc='Generic types and methods, constraints, and covariance/contravariance.',
         dur='60 min', diff='intermediate', prereq=['CS-11'],
         objs=['Write generic classes and methods',
               'Apply type parameter constraints',
               'Understand covariance and contravariance',
               'Use generic collections effectively'],
         refs=[dict(title='Generics Overview', url='https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/generics'),
               dict(title='Generic Constraints', url='https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/generics/constraints-on-type-parameters'),
               dict(title='Variance in Generics', url='https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/covariance-contravariance/')]),
    dict(slug='cs-13-linq', title='LINQ: Language Integrated Query',
         desc='Query and method syntax, deferred execution, standard query operators.',
         dur='75 min', diff='intermediate', prereq=['CS-12'],
         objs=['Write LINQ queries with method syntax',
               'Write LINQ queries with query syntax',
               'Use aggregation operators (Sum, Average, Min, Max, Count)',
               'Understand deferred vs immediate execution'],
         refs=[dict(title='Introduction to LINQ Queries', url='https://learn.microsoft.com/en-us/dotnet/csharp/linq/get-started/introduction-to-linq-queries'),
               dict(title='Standard Query Operators', url='https://learn.microsoft.com/en-us/dotnet/csharp/linq/query-expression-basics'),
               dict(title='LINQ Method Syntax', url='https://learn.microsoft.com/en-us/dotnet/csharp/linq/get-started/write-linq-queries')]),
    dict(slug='cs-14-delegates-events', title='Delegates, Events, and Lambdas',
         desc='Delegate types, multicast delegates, events, lambda expressions, Func/Action.',
         dur='60 min', diff='intermediate', prereq=['CS-13'],
         objs=['Declare and use delegate types',
               'Understand multicast delegates',
               'Implement publisher-subscriber with events',
               'Write lambda expressions with Func/Action'],
         refs=[dict(title='Delegates and Lambdas', url='https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/delegates-lambdas'),
               dict(title='Events Guide', url='https://learn.microsoft.com/en-us/dotnet/csharp/events-overview'),
               dict(title='Lambda Expressions', url='https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/lambda-expressions')]),
    dict(slug='cs-15-exceptions', title='Exceptions and Error Handling',
         desc='try/catch/finally, exception filters, custom exceptions, throw expressions.',
         dur='60 min', diff='intermediate', prereq=['CS-14'],
         objs=['Write try/catch/finally blocks',
               'Use exception filters with when',
               'Create custom exception types',
               'Use throw expressions and defensive coding'],
         refs=[dict(title='Exception Handling Statements', url='https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/exception-handling-statements'),
               dict(title='Exceptions and Errors', url='https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/exceptions/'),
               dict(title='Best Practices', url='https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/exceptions/best-practices-for-exceptions')]),
    dict(slug='cs-16-async', title='Async Programming: async/await and Tasks',
         desc='Task-based async model, await semantics, parallel tasks, error handling.',
         dur='75 min', diff='advanced', prereq=['CS-15'],
         objs=['Understand the Task Asynchronous Programming model',
               'Write async methods with async/await',
               'Run tasks in parallel with Task.WhenAll',
               'Handle errors in async code'],
         refs=[dict(title='Task-based Asynchronous Programming', url='https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/task-asynchronous-programming-model'),
               dict(title='Async Scenarios', url='https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/async-scenarios'),
               dict(title='Async File Access', url='https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/using-async-for-file-access')]),
    dict(slug='cs-17-files-streams', title='Files and Streams',
         desc='System.IO, File/FileInfo, StreamReader/Writer, binary streams, using disposal.',
         dur='60 min', diff='intermediate', prereq=['CS-16'],
         objs=['Read and write text files synchronously',
               'Read and write files asynchronously',
               'Use StreamReader and StreamWriter',
               'Work with binary streams'],
         refs=[dict(title='File and Stream I/O', url='https://learn.microsoft.com/en-us/dotnet/standard/io/'),
               dict(title='File Class', url='https://learn.microsoft.com/en-us/dotnet/api/system.io.file'),
               dict(title='StreamReader Class', url='https://learn.microsoft.com/en-us/dotnet/api/system.io.streamreader')]),
    dict(slug='cs-18-iterators-span', title='Iterators, IEnumerable, and Span<T>',
         desc='yield return, IEnumerable/IEnumerator, lazy evaluation, Span and Memory.',
         dur='60 min', diff='advanced', prereq=['CS-17'],
         objs=['Implement iterators with yield return',
               'Understand lazy evaluation',
               'Iterate with IEnumerator manually',
               'Use Span<T> for allocation-free access'],
         refs=[dict(title='Iterators', url='https://learn.microsoft.com/en-us/dotnet/csharp/iterators'),
               dict(title='IEnumerable Interface', url='https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ienumerable-1'),
               dict(title='Span and Memory', url='https://learn.microsoft.com/en-us/dotnet/standard/memory-and-spans/')]),
    dict(slug='cs-19-patterns-nullable', title='Nullable Types and Pattern Matching',
         desc='Nullable value types, nullable reference types, is patterns, switch patterns.',
         dur='60 min', diff='advanced', prereq=['CS-18'],
         objs=['Use Nullable<T> and nullable reference types',
               'Use null-conditional operators',
               'Write is expressions with type patterns',
               'Use switch expressions with patterns'],
         refs=[dict(title='Pattern Matching', url='https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/patterns'),
               dict(title='Nullable Value Types', url='https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/nullable-value-types'),
               dict(title='Nullable Reference Types', url='https://learn.microsoft.com/en-us/dotnet/csharp/nullable-references')]),
    dict(slug='cs-20-records-structs', title='Records, Structs, and Tuples',
         desc='Record types, with-expressions, tuples, deconstruction, structs as value types.',
         dur='60 min', diff='advanced', prereq=['CS-19'],
         objs=['Define record types with value equality',
               'Use with-expressions for non-destructive mutation',
               'Use tuples and deconstruction',
               'Write structs with value semantics'],
         refs=[dict(title='Records Guide', url='https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/records'),
               dict(title='Tuples Guide', url='https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/tuples'),
               dict(title='Struct Types', url='https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/struct')]),
    dict(slug='cs-21-advanced', title='Advanced: Reflection, Attributes, and Memory',
         desc='Reflection, custom attributes, unsafe code, garbage collection, performance.',
         dur='75 min', diff='expert', prereq=['CS-20'],
         objs=['Inspect types at runtime with reflection',
               'Define and apply custom attributes',
               'Write unsafe code with pointers',
               'Understand GC and deterministic disposal'],
         refs=[dict(title='Reflection and Attributes', url='https://learn.microsoft.com/en-us/dotnet/csharp/advanced-topics/reflection-and-attributes/'),
               dict(title='Garbage Collection', url='https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/'),
               dict(title='Unsafe Code Guide', url='https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/unsafe-code')]),
]


def sample_intro(i, obj):
    """Vary the prose per sub-topic position so the lesson body is not a verbatim template."""
    openings = [
        'Start with the foundations — read the runnable example carefully and trace its output before moving on.',
        'Apply the idiomatic pattern — this is how production C# expresses this idea, so study the shape of the code.',
        'Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.',
        'Put it together — extend the example to combine this concept with what you learned in earlier lessons.',
    ]
    return f'Target: {obj}. {openings[i % len(openings)]}'


def build_lesson(ls, samples):
    n = ls['order']
    code_list = samples.get(n, samples.get(1))
    objs = ls['objs']

    # 4 sub-topics, each with its OWN distinct code sample
    concepts = []
    for i in range(4):
        obj = objs[i] if i < len(objs) else objs[0]
        sample = code_list[i] if i < len(code_list) else code_list[0]
        concepts.append(f"""### {i + 1}. {obj}

{sample_intro(i, obj)}

```csharp
{sample}
```""")

    qs = [
        f'What is the key idea behind "{ls["title"]}"?',
        'Write a small program that exercises at least two concepts from this lesson.',
        'How would you explain this topic to a fellow developer in one paragraph?',
    ]
    llm = [
        f'"Explain {ls["title"]} with analogies and real-world examples"',
        f'"Show me common mistakes beginners make with {ls["title"]}"',
        f'"Provide advanced patterns and performance considerations for {ls["title"]}"',
    ]
    kts = [
        f'Master the core ideas of {ls["title"]} through practice',
        'Combine this lesson with prior lessons to build real programs',
        'Explore the linked Microsoft Learn docs for authoritative depth',
    ]

    fm = {
        'title': ls['title'],
        'description': ls['desc'],
        'type': 'lesson',
        'order': n,
        'duration': ls['dur'],
        'difficulty': ls['diff'],
        'learning_objectives': objs,
        'knowledge_refs': [f'csharp/{ls["slug"]}'],
        'prerequisites': ls['prereq'],
        'references': ls['refs'],
    }

    slug_h1 = ls['slug'].upper()
    intro = f"{ls['desc']} By the end of this lesson you will be able to: {'; '.join(objs)}."
    content = f"""---
{json.dumps(fm, indent=2, ensure_ascii=False)}
---

# {slug_h1}: {ls['title']}

## Introduction

{intro}

## Key Concepts

{chr(10).join(concepts)}

## Practice Questions

1. {qs[0]}
1. {qs[1]}
1. {qs[2]}

## LLM Prompts for Deeper Understanding

1. {llm[0]}
1. {llm[1]}
1. {llm[2]}

## Key Takeaways

- {kts[0]}
- {kts[1]}
- {kts[2]}

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
"""
    return content


def main():
    os.makedirs(BASE, exist_ok=True)
    # Remove skeleton files
    for f in ['fundamentals.md', 'practical-guide.md']:
        p = os.path.join(BASE, f)
        if os.path.exists(p):
            os.remove(p)
            print(f'removed {f}')

    # Write lesson files
    for i, ls in enumerate(LESSONS, 1):
        ls['order'] = i
        with open(os.path.join(BASE, f"{ls['slug']}.md"), 'w') as fh:
            fh.write(build_lesson(ls, CODE))
    print(f'wrote {len(LESSONS)} lesson files')

    # Update index.json lessons (preserve categories)
    idx_path = os.path.join(BASE, 'index.json')
    with open(idx_path) as fh:
        idx = json.load(fh)
    idx['lessons'] = [dict(
        slug=ls['slug'],
        title=ls['title'],
        description=ls['desc'],
        type='lesson',
        order=ls['order'],
        duration=ls['dur'],
        difficulty=ls['diff'],
        knowledge_refs=[f'csharp/{ls["slug"]}'],
    ) for ls in LESSONS]
    with open(idx_path, 'w') as fh:
        json.dump(idx, fh, indent=2, ensure_ascii=False)
    print('updated index.json')


if __name__ == '__main__':
    main()
