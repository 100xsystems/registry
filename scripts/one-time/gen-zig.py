#!/usr/bin/env python3
"""Generate the 21-lesson Zig curriculum at Python/JS/Java depth.
Uses the shared gen_lib template. Exact refs from ziglang.org.
Each lesson has 4 sub-topics, each with its OWN distinct code sample.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from gen_lib import main as run_gen  # noqa: E402

LANGUAGE = 'zig'

BASE = os.path.join(os.path.dirname(__file__), '..', '..', 'static-data', 'knowledge', 'languages', 'zig')

CODE = {
    1: [
        '''// Your first Zig program
const std = @import("std");

pub fn main() void {
    std.debug.print("Hello, 100X Systems!\\n", .{});
}
// Run with: zig run hello.zig
''',
        '''// Zig requires you to be explicit about everything
const std = @import("std");

pub fn main() void {
    const name = "Zig";
    std.debug.print("Hello, {s}!\\n", .{name});
}
''',
        '''// Build system: zig build-exe and zig build
// zig build-exe hello.zig   -> produces ./hello
// zig build                 -> builds with build.zig
// A build.zig file defines build steps, targets, and dependencies.
''',
        '''// Compile-time awareness from the start
const std = @import("std");

pub fn main() void {
    // The {d} format specifier prints a decimal integer
    std.debug.print("2 + 2 = {d}\\n", .{2 + 2});
}
''',
    ],
    2: [
        '''// Integer types: signed and unsigned, sized explicitly
const std = @import("std");

pub fn main() void {
    const a: i32 = -10;      // signed 32-bit
    const b: u8 = 255;       // unsigned 8-bit (max 255)
    const c: usize = 1000;   // pointer-sized unsigned
    std.debug.print("{d} {d} {d}\\n", .{ a, b, c });
}
''',
        '''// Floats: f16, f32, f64, f128
const std = @import("std");

pub fn main() void {
    const pi: f64 = 3.14159;
    const half: f32 = 0.5;
    std.debug.print("{d} {d}\\n", .{ pi, half });
}
''',
        '''// Bools and char literals
const std = @import("std");

pub fn main() void {
    const ok: bool = true;
    const letter = 'a';        // a comptime_int char literal
    std.debug.print("{any} {c}\\n", .{ ok, letter });
}
''',
        '''// Type coercion is explicit: use @intCast, @floatCast
const std = @import("std");

pub fn main() void {
    const small: u8 = 42;
    const big: u32 = @intCast(small);   // widening cast
    std.debug.print("{d}\\n", .{big});
}
''',
    ],
    3: [
        '''// const vs var: prefer const by default
const std = @import("std");

pub fn main() void {
    const fixed = 10;        // cannot be reassigned
    var mutable: i32 = 0;
    mutable += 5;            // var allows mutation
    std.debug.print("{d} {d}\\n", .{ fixed, mutable });
}
''',
        '''// Variable shadowing is allowed and often idiomatic
const std = @import("std");

pub fn main() void {
    var x: i32 = 1;
    x = x + 1;               // mutate in place
    const y = x * 2;
    std.debug.print("{d} {d}\\n", .{ x, y });
}
''',
        '''// Undefined values must be initialized before use
const std = @import("std");

pub fn main() void {
    var total: i32 = 0;      // always initialize
    for (1..6) |i| {
        total += @intCast(i);
    }
    std.debug.print("sum 1..5 = {d}\\n", .{total});
}
''',
        '''// Type inference with const keeps code clean
const std = @import("std");

pub fn main() void {
    const greeting = "hello";          // *const [5:0]u8 comptime literal
    const count: u32 = 100;
    std.debug.print("{s} {d}\\n", .{ greeting, count });
}
''',
    ],
    4: [
        '''// Arithmetic operators
const std = @import("std");

pub fn main() void {
    const a: i32 = 7;
    std.debug.print("{d}\\n", .{a + 3});   // 10
    std.debug.print("{d}\\n", .{a - 2});   // 5
    std.debug.print("{d}\\n", .{a * 2});   // 14
    std.debug.print("{d}\\n", .{a / 2});   // 3 — integer division
    std.debug.print("{d}\\n", .{a % 4});   // 3 — modulo
}
''',
        '''// Division semantics differ by type
const std = @import("std");

pub fn main() void {
    const int_div = 7 / 2;       // 3 (i32 comptime)
    const float_div = @as(f64, 7) / 2.0;  // 3.5
    std.debug.print("{d} {d}\\n", .{ int_div, float_div });
}
''',
        '''// Bitwise operators
const std = @import("std");

pub fn main() void {
    const a: u8 = 0b1100;
    const b: u8 = 0b1010;
    std.debug.print("{b}\\n", .{a & b});   // 1000
    std.debug.print("{b}\\n", .{a | b});   // 1110
    std.debug.print("{b}\\n", .{a ^ b});   // 0110 (xor)
    std.debug.print("{b}\\n", .{a << 1});  // 11000
}
''',
        '''// Comparison and logical operators
const std = @import("std");

pub fn main() void {
    const x: i32 = 5;
    std.debug.print("{any} {any}\\n", .{ x < 10, x >= 3 });
    std.debug.print("{any}\\n", .{x > 0 and x < 10});   // true
    std.debug.print("{any}\\n", .{x < 0 or x == 5});    // true
    std.debug.print("{any}\\n", .{!(x == 0)});          // true
}
''',
    ],
    5: [
        '''// Functions: explicit return types, named parameters
const std = @import("std");

fn add(a: i32, b: i32) i32 {
    return a + b;
}

pub fn main() void {
    std.debug.print("{d}\\n", .{add(2, 3)});   // 5
}
''',
        '''// Functions that return void and use values
const std = @import("std");

fn describe(x: i32) void {
    if (x > 0) {
        std.debug.print("positive\\n", .{});
    } else {
        std.debug.print("non-positive\\n", .{});
    }
}

pub fn main() void {
    describe(5);
    describe(-1);
}
''',
        '''// Nested functions are not allowed; use top-level fns
const std = @import("std");

fn square(x: i32) i32 {
    return x * x;
}

pub fn main() void {
    std.debug.print("{d}\\n", .{square(square(3))});   // 81
}
''',
        '''// Function pointers and passing functions
const std = @import("std");

fn twice(f: *const fn (i32) i32, x: i32) i32 {
    return f(f(x));
}

fn inc(x: i32) i32 {
    return x + 1;
}

pub fn main() void {
    std.debug.print("{d}\\n", .{twice(inc, 5)});   // 7
}
''',
    ],
    6: [
        '''// if is an expression in Zig
const std = @import("std");

pub fn main() void {
    const x: i32 = 10;
    const label = if (x > 5) "big" else "small";
    std.debug.print("{s}\\n", .{label});   // big
}
''',
        '''// switch expressions — exhaustive by default
const std = @import("std");

fn day_name(d: u8) []const u8 {
    return switch (d) {
        1 => "Monday",
        2 => "Tuesday",
        3 => "Wednesday",
        else => "another day",
    };
}

pub fn main() void {
    std.debug.print("{s}\\n", .{day_name(2)});
}
''',
        '''// for loops over slices and ranges
const std = @import("std");

pub fn main() void {
    const nums = [_]i32{ 1, 2, 3, 4, 5 };
    var total: i32 = 0;
    for (nums) |n| {
        total += n;
    }
    std.debug.print("{d}\\n", .{total});   // 15
}
''',
        '''// while loops with continue and break
const std = @import("std");

pub fn main() void {
    var i: u32 = 0;
    var total: u32 = 0;
    while (i < 10) : (i += 1) {
        if (i == 3) continue;
        if (i == 7) break;
        total += i;
    }
    std.debug.print("{d}\\n", .{total});   // 0+1+2+4+5+6 = 18
}
''',
    ],
    7: [
        '''// Error unions: return error.NAME or a value
const std = @import("std");

fn safeDivide(a: i32, b: i32) !i32 {
    if (b == 0) return error.DivisionByZero;
    return a / b;
}

pub fn main() void {
    const result = safeDivide(10, 2) catch |err| {
        std.debug.print("error: {s}\\n", .{@errorName(err)});
        return;
    };
    std.debug.print("{d}\\n", .{result});
}
''',
        '''// try: propagate errors to the caller
const std = @import("std");

fn inner() !i32 {
    return error.NotReady;
}

fn outer() !i32 {
    const value = try inner();   // propagates the error
    return value + 1;
}

pub fn main() void {
    const r = outer() catch |err| {
        std.debug.print("caught {s}\\n", .{@errorName(err)});
        return;
    };
    std.debug.print("{d}\\n", .{r});
}
''',
        '''// Global error sets and error unions as values
const std = @import("std");

const MyError = error{ OutOfRange, BadInput };

fn validate(n: i32) MyError!i32 {
    if (n < 0) return error.BadInput;
    if (n > 100) return error.OutOfRange;
    return n;
}

pub fn main() void {
    const r = validate(-1) catch |err| {
        std.debug.print("{s}\\n", .{@errorName(err)});
        return;
    };
    std.debug.print("{d}\\n", .{r});
}
''',
        '''// Error handling with orelse-style fallbacks
const std = @import("std");

fn parseNumber(s: []const u8) !i32 {
    return std.fmt.parseInt(i32, s, 10);
}

pub fn main() void {
    const a = parseNumber("42") catch 0;
    const b = parseNumber("nope") catch 0;
    std.debug.print("{d} {d}\\n", .{ a, b });   // 42 0
}
''',
    ],
    8: [
        '''// Optionals: ?T holds T or null
const std = @import("std");

pub fn main() void {
    const maybe: ?i32 = null;
    const value: ?i32 = 42;

    const a = maybe orelse 0;    // 0
    const b = value orelse 0;    // 42
    std.debug.print("{d} {d}\\n", .{ a, b });
}
''',
        '''// Unwrap with if — the idiomatic optional pattern
const std = @import("std");

pub fn main() void {
    const maybe: ?i32 = 7;
    if (maybe) |v| {
        std.debug.print("got {d}\\n", .{v});
    } else {
        std.debug.print("nothing\\n", .{});
    }
}
''',
        '''// Optionals wrap any type, including pointers
const std = @import("std");

fn find(nums: []const i32, target: i32) ?usize {
    for (nums, 0..) |n, i| {
        if (n == target) return i;
    }
    return null;
}

pub fn main() void {
    const nums = [_]i32{ 10, 20, 30 };
    const idx = find(&nums, 20) orelse 99;
    std.debug.print("{d}\\n", .{idx});   // 1
}
''',
        '''// Error unions and optionals compose: !?T
const std = @import("std");

fn lookup(key: []const u8) !?i32 {
    if (key.len == 0) return error.EmptyKey;
    return null;   // valid: not found
}

pub fn main() void {
    const r = lookup("a") catch null;
    const v = r orelse -1;
    std.debug.print("{d}\\n", .{v});   // -1
}
''',
    ],
    9: [
        '''// Arrays have fixed length; slices are views
const std = @import("std");

pub fn main() void {
    const arr = [_]i32{ 1, 2, 3, 4, 5 };
    const slice: []const i32 = arr[0..3];   // 1 2 3
    std.debug.print("{d}\\n", .{slice.len});
}
''',
        '''// Bounds checking is mandatory at runtime
const std = @import("std");

pub fn main() void {
    const arr = [_]i32{ 1, 2, 3 };
    const idx: usize = 1;
    // arr[idx] panics if idx >= arr.len — no silent UB
    std.debug.print("{d}\\n", .{arr[idx]});
}
''',
        '''// Slicing with comptime-known bounds when possible
const std = @import("std");

pub fn main() void {
    const data = "hello world";
    const first5 = data[0..5];
    std.debug.print("{s}\\n", .{first5});   // hello
}
''',
        '''// Copying with std.mem.copyForwards
const std = @import("std");

pub fn main() void {
    var dest = [_]i32{ 0, 0, 0, 0, 0 };
    const src = [_]i32{ 7, 8, 9 };
    @memcpy(dest[0..3], &src);
    std.debug.print("{d} {d} {d}\\n", .{ dest[0], dest[1], dest[2] });
}
''',
    ],
    10: [
        '''// Strings are []const u8 in Zig
const std = @import("std");

pub fn main() void {
    const greeting: []const u8 = "hello";
    std.debug.print("{s} (len {d})\\n", .{ greeting, greeting.len });
}
''',
        '''// String literals are null-terminated comptime values
const std = @import("std");

pub fn main() void {
    const lit = "c-string";   // *const [9:0]u8
    const slice: []const u8 = lit;
    std.debug.print("{s}\\n", .{slice});
}
''',
        '''// Building strings at runtime needs an allocator
const std = @import("std");

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    var buf = std.ArrayList(u8).init(allocator);
    defer buf.deinit();
    try buf.appendSlice("Hello, ");
    try buf.appendSlice("Zig!");
    std.debug.print("{s}\\n", .{buf.items});
}
''',
        '''// Comparing and searching strings
const std = @import("std");

pub fn main() void {
    const a = "hello";
    const b = "hello";
    const eq = std.mem.eql(u8, a, b);
    const starts = std.mem.startsWith(u8, "hello world", "hello");
    std.debug.print("{any} {any}\\n", .{ eq, starts });
}
''',
    ],
    11: [
        '''// Structs: named fields with types
const std = @import("std");

const Point = struct {
    x: f64,
    y: f64,
};

pub fn main() void {
    const p = Point{ .x = 1.0, .y = 2.0 };
    std.debug.print("{d} {d}\\n", .{ p.x, p.y });
}
''',
        '''// Methods are just functions whose first param is self
const std = @import("std");

const Rectangle = struct {
    width: f64,
    height: f64,

    fn area(self: Rectangle) f64 {
        return self.width * self.height;
    }
};

pub fn main() void {
    const r = Rectangle{ .width = 3.0, .height = 4.0 };
    std.debug.print("{d}\\n", .{r.area()});   // 12
}
''',
        '''// Mutable structs: declare var and mutate fields
const std = @import("std");

const Counter = struct {
    value: i32,

    fn increment(self: *Counter) void {
        self.value += 1;
    }
};

pub fn main() void {
    var c = Counter{ .value = 0 };
    c.increment();
    c.increment();
    std.debug.print("{d}\\n", .{c.value});   // 2
}
''',
        '''// Default field values
const std = @import("std");

const Config = struct {
    host: []const u8 = "localhost",
    port: u16 = 8080,
};

pub fn main() void {
    const cfg = Config{};
    std.debug.print("{s}:{d}\\n", .{ cfg.host, cfg.port });
}
''',
    ],
    12: [
        '''// Enums: named values with optional explicit tags
const std = @import("std");

const Color = enum { red, green, blue };

pub fn main() void {
    const c = Color.green;
    std.debug.print("{s}\\n", .{@tagName(c)});   // green
}
''',
        '''// Switch over enums is exhaustive
const std = @import("std");

const Shape = enum { circle, square, triangle };

fn describe(s: Shape) []const u8 {
    return switch (s) {
        .circle => "round",
        .square => "four sides",
        .triangle => "three sides",
    };
}

pub fn main() void {
    std.debug.print("{s}\\n", .{describe(.square)});
}
''',
        '''// Tagged unions: one payload among many
const std = @import("std");

const Value = union(enum) {
    int: i32,
    text: []const u8,
    none,
};

pub fn main() void {
    const v = Value{ .text = "hi" };
    switch (v) {
        .int => |i| std.debug.print("int {d}\\n", .{i}),
        .text => |s| std.debug.print("text {s}\\n", .{s}),
        .none => std.debug.print("none\\n", .{}),
    }
}
''',
        '''// Enum values can carry explicit numeric tags
const std = @import("std");

const HttpStatus = enum(u16) {
    ok = 200,
    not_found = 404,
    server_error = 500,
};

pub fn main() void {
    const s = HttpStatus.not_found;
    const n: u16 = @intFromEnum(s);
    std.debug.print("{d}\\n", .{n});   // 404
}
''',
    ],
    13: [
        '''// Pointers: & takes an address; *T is a pointer type
const std = @import("std");

pub fn main() void {
    var x: i32 = 42;
    const p: *i32 = &x;
    p.* = 43;               // dereference to write
    std.debug.print("{d}\\n", .{x});   // 43
}
''',
        '''// const pointers prevent mutation
const std = @import("std");

pub fn main() void {
    const value: i32 = 10;
    const p: *const i32 = &value;
    std.debug.print("{d}\\n", .{p.*});
    // p.* = 20 would fail to compile
}
''',
        '''// Many-item pointers and slices
const std = @import("std");

pub fn main() void {
    const arr = [_]i32{ 1, 2, 3 };
    const ptr: [*]const i32 = &arr;
    _ = ptr;   // used only for illustration
    const slice: []const i32 = arr[0..];
    std.debug.print("{d}\\n", .{slice.len});
}
''',
        '''// Optional pointers: ?*T — the null-able pointer
const std = @import("std");

fn maybePtr(flag: bool) ?*const i32 {
    const value: i32 = 5;
    if (flag) return &value;
    return null;
}

pub fn main() void {
    const p = maybePtr(true) orelse return;
    std.debug.print("{d}\\n", .{p.*});
}
''',
    ],
    14: [
        '''// Zig has no hidden allocator: you pass one explicitly
const std = @import("std");

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    const nums = try allocator.alloc(i32, 3);
    defer allocator.free(nums);
    nums[0] = 10;
    nums[1] = 20;
    nums[2] = 30;
    std.debug.print("{d}\\n", .{nums[2]});
}
''',
        '''// defer frees resources when the scope exits
const std = @import("std");

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    var list = std.ArrayList(i32).init(allocator);
    defer list.deinit();
    try list.append(1);
    try list.append(2);
    std.debug.print("{d}\\n", .{list.items.len});
}
''',
        '''// realloc: grow a buffer in place when possible
const std = @import("std");

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    var buf = try allocator.alloc(u8, 2);
    defer allocator.free(buf);
    buf = try allocator.realloc(buf, 8);   // may move
    buf[7] = 'x';
    std.debug.print("{d}\\n", .{buf.len});
}
''',
        '''// Arena allocator: free everything at once
const std = @import("std");

pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const allocator = arena.allocator();

    _ = try allocator.alloc(u8, 1000);
    _ = try allocator.alloc(u8, 2000);
    std.debug.print("arena freed at scope exit\\n", .{});
}
''',
    ],
    15: [
        '''// comptime: code that runs at compile time
const std = @import("std");

fn power(comptime base: i32, comptime exp: u32) i32 {
    var result: i32 = 1;
    var i: u32 = 0;
    while (i < exp) : (i += 1) {
        result *= base;
    }
    return result;
}

pub fn main() void {
    const v = comptime power(2, 10);
    std.debug.print("{d}\\n", .{v});   // 1024
}
''',
        '''// comptime expressions are evaluated at build time
const std = @import("std");

const TableSize = comptime blk: {
    var size: usize = 16;
    while (size < 1000) size *= 2;
    break :blk size;
};

pub fn main() void {
    std.debug.print("{d}\\n", .{TableSize});   // 1024
}
''',
        '''// @TypeOf and comptime introspection
const std = @import("std");

pub fn main() void {
    const x: u8 = 255;
    const T = @TypeOf(x);
    std.debug.print("{any}\\n", .{T});   // u8
}
''',
        '''// inline for unrolls loops at compile time
const std = @import("std");

pub fn main() void {
    const types = [_]type{ i32, f64, bool };
    inline for (types) |T| {
        std.debug.print("{any} size {d}\\n", .{ T, @sizeOf(T) });
    }
}
''',
    ],
    16: [
        '''// Generic functions via comptime type parameters
const std = @import("std");

fn maxOf(comptime T: type, a: T, b: T) T {
    return if (a > b) a else b;
}

pub fn main() void {
    std.debug.print("{d}\\n", .{maxOf(i32, 3, 7)});
    std.debug.print("{d}\\n", .{maxOf(f64, 2.5, 1.5)});
}
''',
        '''// Generic data structures
const std = @import("std");

fn Stack(comptime T: type) type {
    return struct {
        items: []T,
        len: usize = 0,

        fn push(self: *@This(), item: T) void {
            self.items[self.len] = item;
            self.len += 1;
        }
    };
}

pub fn main() void {
    var arr = [_]i32{ 0, 0, 0 };
    var stack = Stack(i32){ .items = &arr };
    stack.push(42);
    std.debug.print("{d}\\n", .{stack.len});
}
''',
        '''// Generic over the element type with constraints
const std = @import("std");

fn sum(comptime T: type, items: []const T) T {
    var total: T = 0;
    for (items) |it| {
        total += it;
    }
    return total;
}

pub fn main() void {
    const ints = [_]i32{ 1, 2, 3, 4 };
    const floats = [_]f64{ 0.5, 1.5 };
    std.debug.print("{d} {d}\\n", .{ sum(i32, &ints), sum(f64, &floats) });
}
''',
        '''// std.ArrayList is a ready-made generic
const std = @import("std");

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    var list = std.ArrayList(i32).init(allocator);
    defer list.deinit();
    try list.appendSlice(&[_]i32{ 1, 2, 3 });
    std.debug.print("{d}\\n", .{list.items.len});   // 3
}
''',
    ],
    17: [
        '''// @import loads modules; pub exposes declarations
const std = @import("std");

pub fn main() void {
    std.debug.print("std is Zig's standard library\\n", .{});
}
''',
        '''// Cross-file imports
// math.zig:
// pub fn add(a: i32, b: i32) i32 { return a + b; }
//
// main.zig:
// const math = @import("math.zig");
// const result = math.add(2, 3);
''',
        '''// pub const and pub fn create the public API
const std = @import("std");

const Greetings = struct {
    pub const DefaultName = "world";

    pub fn hello(name: []const u8) void {
        std.debug.print("Hello, {s}!\\n", .{name});
    }
};

pub fn main() void {
    Greetings.hello(Greetings.DefaultName);
}
''',
        '''// build.zig wires files into build steps
// pub fn build(b: *std.Build) void {
//     const exe = b.addExecutable(.{
//         .name = "app",
//         .root_source_file = b.path("src/main.zig"),
//         .target = b.standardTargetOptions(.{}),
//     });
//     b.installArtifact(exe);
// }
''',
    ],
    18: [
        '''// Reading a file requires an allocator and open options
const std = @import("std");

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    const contents = try std.fs.cwd().readFileAlloc(allocator, "data.txt", 1 << 20);
    defer allocator.free(contents);
    std.debug.print("read {d} bytes\\n", .{contents.len});
}
''',
        '''// Writing a file
const std = @import("std");

pub fn main() !void {
    const data = "line one\\nline two\\n";
    try std.fs.cwd().writeFile(.{
        .sub_path = "out.txt",
        .data = data,
    });
    std.debug.print("wrote file\\n", .{});
}
''',
        '''// Iterating over directory entries
const std = @import("std");

pub fn main() !void {
    var dir = try std.fs.cwd().openDir(".", .{ .iterate = true });
    defer dir.close();

    var it = dir.iterate();
    var count: usize = 0;
    while (try it.next()) |entry| {
        _ = entry;
        count += 1;
    }
    std.debug.print("{d} entries\\n", .{count});
}
''',
        '''// std.fs.cwd() is the current working directory handle
const std = @import("std");

pub fn main() !void {
    const cwd = std.fs.cwd();
    _ = cwd;   // placeholder for file operations
    std.debug.print("cwd handle acquired\\n", .{});
}
''',
    ],
    19: [
        '''// test blocks compile and run with `zig test`
const std = @import("std");

fn add(a: i32, b: i32) i32 {
    return a + b;
}

test "add adds numbers" {
    try std.testing.expectEqual(@as(i32, 5), add(2, 3));
}

// Run with: zig test file.zig
''',
        '''// Testing errors with expectError
const std = @import("std");

fn divide(a: i32, b: i32) !i32 {
    if (b == 0) return error.DivisionByZero;
    return a / b;
}

test "divide by zero" {
    try std.testing.expectError(error.DivisionByZero, divide(1, 0));
}
''',
        '''// expectEqualDeep and standard testing helpers
const std = @import("std");

test "deep equality" {
    try std.testing.expectEqualDeep(&[_]i32{ 1, 2 }, &[_]i32{ 1, 2 });
    try std.testing.expect(true);
}
''',
        '''// Test organization: many small focused tests
const std = @import("std");

fn isEven(n: i32) bool {
    return n % 2 == 0;
}

test "even numbers" {
    try std.testing.expect(isEven(2));
    try std.testing.expect(isEven(100));
}

test "odd numbers" {
    try std.testing.expect(!isEven(3));
}
''',
    ],
    20: [
        '''// std.debug.print is the quick print; use it in main only
const std = @import("std");

pub fn main() void {
    std.debug.print("debug print\\n", .{});
}
''',
        '''// std.mem: eql, startsWith, endsWith, indexOf
const std = @import("std");

pub fn main() void {
    const text = "hello world";
    const idx = std.mem.indexOf(u8, text, "world") orelse 0;
    std.debug.print("{d}\\n", .{idx});   // 6
}
''',
        '''// std.ArrayList: the dynamic array workhorse
const std = @import("std");

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    var list = std.ArrayList(u8).init(allocator);
    defer list.deinit();
    try list.append('a');
    try list.appendSlice("bc");
    std.debug.print("{s}\\n", .{list.items});   // abc
}
''',
        '''// std.StringHashMap: a ready-made hash map
const std = @import("std");

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    var map = std.StringHashMap(i32).init(allocator);
    defer map.deinit();
    try map.put("age", 36);
    const age = map.get("age") orelse 0;
    std.debug.print("{d}\\n", .{age});   // 36
}
''',
    ],
    21: [
        '''// The ecosystem: the Zig standard library is the star
// Zig keeps dependencies minimal; std covers a lot of ground.
// Package managers exist: zigmod, gyro, and the built-in build system.
''',
        '''// zig build is the canonical build tool
// zig build-exe, zig build-lib, zig test, zig fmt, zig translate-c
// `zig fmt` auto-formats code — run it before committing.
''',
        '''// Zig interops with C: @cImport and build.zig links
// const c = @cImport({ @cInclude("stdio.h"); });
// c.printf("from C\\n");
// Linking C libraries is a first-class Zig feature.
''',
        '''// Next steps: advanced Zig topics
// 1. Comptime metaprogramming — generic containers, DSLs
// 2. std.Thread and concurrency primitives
// 3. Network programming with std.net
// 4. WebAssembly targets: zig build-lib -target wasm32-freestanding
// 5. Read ziglearn.org and the official language reference
''',
    ],
}

LESSONS = [
    dict(
        slug='zig-01-getting-started',
        title='Getting Started with Zig',
        desc='Hello world, zig run, and the build system.',
        diff='beginner',
        dur=20,
        objs=[
            'Run Zig code with zig run and zig build-exe',
            'Explain how Zig compiles to native code',
            'Use std.debug.print for output',
        ],
        prereq=[],
        refs=[dict(title='Zig Language Reference', url='https://ziglang.org/documentation/master/'),
              dict(title='Zig Learn — Official Guide', url='https://ziglearn.org/'),
              dict(title='Ziglang — Home', url='https://ziglang.org/')]),
    dict(
        slug='zig-02-values-types',
        title='Values and Types',
        desc='Integers, floats, bools, chars, and explicit casts.',
        diff='beginner',
        dur=25,
        objs=[
            'Choose integer types with explicit sizes',
            'Work with floats and bools',
            'Cast between types with @intCast and @floatCast',
        ],
        prereq=['zig-01-getting-started'],
        refs=[dict(title='Zig Reference — Primitive Types', url='https://ziglang.org/documentation/master/#Primitive-Types'),
              dict(title='Zig Reference — Casting', url='https://ziglang.org/documentation/master/#Casting')]),
    dict(
        slug='zig-03-variables',
        title='Variables',
        desc='const vs var, mutation, and type inference.',
        diff='beginner',
        dur=25,
        objs=[
            'Prefer const over var',
            'Mutate values only when needed',
            'Leverage type inference',
        ],
        prereq=['zig-02-values-types'],
        refs=[dict(title='Zig Reference — Values', url='https://ziglang.org/documentation/master/#Values'),
              dict(title='Zig Reference — Variables', url='https://ziglang.org/documentation/master/#Variables')]),
    dict(
        slug='zig-04-operators',
        title='Operators',
        desc='Arithmetic, division semantics, bitwise, and logic.',
        diff='beginner',
        dur=25,
        objs=[
            'Use arithmetic operators on integers and floats',
            'Explain division semantics by type',
            'Apply bitwise and logical operators',
        ],
        prereq=['zig-02-values-types'],
        refs=[dict(title='Zig Reference — Operators', url='https://ziglang.org/documentation/master/#Operators'),
              dict(title='Zig Reference — Assignment', url='https://ziglang.org/documentation/master/#Assignment')]),
    dict(
        slug='zig-05-functions',
        title='Functions',
        desc='Explicit signatures, void returns, and function pointers.',
        diff='beginner',
        dur=30,
        objs=[
            'Define functions with explicit return types',
            'Write void functions that produce output',
            'Pass functions as values',
        ],
        prereq=['zig-01-getting-started'],
        refs=[dict(title='Zig Reference — Functions', url='https://ziglang.org/documentation/master/#Functions')]),
    dict(
        slug='zig-06-control-flow',
        title='Control Flow',
        desc='if expressions, switch, for, and while loops.',
        diff='beginner',
        dur=30,
        objs=[
            'Use if and switch as expressions',
            'Iterate with for over slices and ranges',
            'Control loops with continue and break',
        ],
        prereq=['zig-01-getting-started'],
        refs=[dict(title='Zig Reference — If', url='https://ziglang.org/documentation/master/#If'),
              dict(title='Zig Reference — Switch', url='https://ziglang.org/documentation/master/#Switch'),
              dict(title='Zig Reference — Loops', url='https://ziglang.org/documentation/master/#While')]),
    dict(
        slug='zig-07-errors',
        title='Errors',
        desc='Error unions, try, catch, and propagation.',
        diff='intermediate',
        dur=35,
        objs=[
            'Return errors from functions with !T',
            'Propagate errors with try',
            'Handle errors with catch blocks',
        ],
        prereq=['zig-05-functions'],
        refs=[dict(title='Zig Reference — Errors', url='https://ziglang.org/documentation/master/#Errors'),
              dict(title='Zig Guide — Error Handling', url='https://zig.guide/error-handling/')]),
    dict(
        slug='zig-08-optionals',
        title='Optionals',
        desc='?T, null, orelse, and if-unwrapping.',
        diff='intermediate',
        dur=30,
        objs=[
            'Represent absence with optional types',
            'Unwrap with orelse and if payloads',
            'Compose optionals with error unions',
        ],
        prereq=['zig-07-errors'],
        refs=[dict(title='Zig Reference — Optionals', url='https://ziglang.org/documentation/master/#Optionals')]),
    dict(
        slug='zig-09-arrays-slices',
        title='Arrays and Slices',
        desc='Fixed arrays, runtime slices, and bounds checking.',
        diff='intermediate',
        dur=30,
        objs=[
            'Create fixed-length arrays',
            'Slice arrays for views',
            'Explain mandatory bounds checking',
        ],
        prereq=['zig-02-values-types'],
        refs=[dict(title='Zig Reference — Arrays', url='https://ziglang.org/documentation/master/#Arrays'),
              dict(title='Zig Reference — Slices', url='https://ziglang.org/documentation/master/#Slices')]),
    dict(
        slug='zig-10-strings',
        title='Strings',
        desc='[]const u8, literals, allocation, and comparison.',
        diff='intermediate',
        dur=30,
        objs=[
            'Explain that strings are byte slices',
            'Build strings at runtime with ArrayList',
            'Compare and search strings with std.mem',
        ],
        prereq=['zig-09-arrays-slices'],
        refs=[dict(title='Zig Guide — Strings', url='https://zig.guide/strings/'),
              dict(title='Zig Reference — Sentinel-Terminated Arrays', url='https://ziglang.org/documentation/master/#Sentinel-Terminated-Arrays')]),
    dict(
        slug='zig-11-structs',
        title='Structs',
        desc='Fields, methods, mutation, and defaults.',
        diff='intermediate',
        dur=30,
        objs=[
            'Define structs with typed fields',
            'Write methods on structs',
            'Use default field values',
        ],
        prereq=['zig-05-functions'],
        refs=[dict(title='Zig Reference — Structs', url='https://ziglang.org/documentation/master/#struct'),
              dict(title='Zig Reference — Containers', url='https://ziglang.org/documentation/master/#Containers')]),
    dict(
        slug='zig-12-enums-unions',
        title='Enums and Tagged Unions',
        desc='Enums, exhaustive switch, and union(enum) payloads.',
        diff='intermediate',
        dur=35,
        objs=[
            'Define enums with @tagName',
            'Write exhaustive switches over enums',
            'Model alternatives with tagged unions',
        ],
        prereq=['zig-06-control-flow'],
        refs=[dict(title='Zig Reference — Enums', url='https://ziglang.org/documentation/master/#enum'),
              dict(title='Zig Reference — Unions', url='https://ziglang.org/documentation/master/#union')]),
    dict(
        slug='zig-13-pointers',
        title='Pointers',
        desc='Single-item pointers, const pointers, and optional pointers.',
        diff='intermediate',
        dur=30,
        objs=[
            'Take addresses with & and dereference with .*',
            'Distinguish *T from *const T',
            'Use optional pointers ?*T',
        ],
        prereq=['zig-03-variables'],
        refs=[dict(title='Zig Reference — Pointers', url='https://ziglang.org/documentation/master/#Pointers'),
              dict(title='Zig Reference — Many-Item Pointers', url='https://ziglang.org/documentation/master/#Many-Item-Pointers')]),
    dict(
        slug='zig-14-memory-management',
        title='Memory Management',
        desc='Explicit allocators, defer, realloc, and arenas.',
        diff='expert',
        dur=45,
        objs=[
            'Explain why Zig makes allocators explicit',
            'Allocate and free with allocator.alloc and free',
            'Use defer and arenas for cleanup',
        ],
        prereq=['zig-09-arrays-slices'],
        refs=[dict(title='Zig Reference — Memory', url='https://ziglang.org/documentation/master/#Memory'),
              dict(title='Zig Guide — Memory', url='https://zig.guide/memory/'),
              dict(title='Zig Reference — defer', url='https://ziglang.org/documentation/master/#defer')]),
    dict(
        slug='zig-15-comptime',
        title='Comptime',
        desc='Compile-time evaluation, comptime params, and introspection.',
        diff='expert',
        dur=40,
        objs=[
            'Evaluate expressions at compile time',
            'Use comptime function parameters',
            'Introspect types with @TypeOf and @sizeOf',
        ],
        prereq=['zig-06-control-flow'],
        refs=[dict(title='Zig Reference — comptime', url='https://ziglang.org/documentation/master/#comptime'),
              dict(title='Zig Guide — Comptime', url='https://zig.guide/comptime/')]),
    dict(
        slug='zig-16-generics',
        title='Generics',
        desc='Generic functions and data structures via comptime T.',
        diff='expert',
        dur=40,
        objs=[
            'Parameterize functions with comptime types',
            'Build generic structs',
            'Reuse std.ArrayList and friends',
        ],
        prereq=['zig-15-comptime'],
        refs=[dict(title='Zig Guide — Comptime and Generics', url='https://zig.guide/comptime/'),
              dict(title='Zig Reference — Generic Data Structures', url='https://ziglang.org/documentation/master/#Generic-Data-Structures')]),
    dict(
        slug='zig-17-modules-imports',
        title='Modules and Imports',
        desc='@import, pub declarations, and build.zig wiring.',
        diff='intermediate',
        dur=30,
        objs=[
            'Import modules with @import',
            'Expose declarations with pub',
            'Understand the build.zig file layout',
        ],
        prereq=['zig-01-getting-started'],
        refs=[dict(title='Zig Reference — Import', url='https://ziglang.org/documentation/master/#Import'),
              dict(title='Zig Build System — Documentation', url='https://ziglang.org/learn/build-system/')]),
    dict(
        slug='zig-18-file-io',
        title='File I/O',
        desc='Reading, writing, and iterating with std.fs.',
        diff='intermediate',
        dur=30,
        objs=[
            'Read files with readFileAlloc',
            'Write files with writeFile',
            'Iterate directory entries',
        ],
        prereq=['zig-14-memory-management'],
        refs=[dict(title='Zig Standard Library — std.fs', url='https://ziglang.org/documentation/master/std/#std.fs'),
              dict(title='Zig Reference — File System', url='https://ziglang.org/documentation/master/std/#root')]),
    dict(
        slug='zig-19-testing',
        title='Testing',
        desc='test blocks, expect, expectError, and test organization.',
        diff='intermediate',
        dur=30,
        objs=[
            'Write test blocks run with zig test',
            'Assert with std.testing.expect',
            'Expect errors with expectError',
        ],
        prereq=['zig-07-errors'],
        refs=[dict(title='Zig Reference — Testing', url='https://ziglang.org/documentation/master/#Testing'),
              dict(title='Zig Guide — Testing', url='https://zig.guide/testing/')]),
    dict(
        slug='zig-20-standard-library',
        title='The Standard Library',
        desc='std.debug, std.mem, std.ArrayList, and StringHashMap.',
        diff='intermediate',
        dur=30,
        objs=[
            'Print and inspect with std.debug',
            'Search memory with std.mem',
            'Use ArrayList and StringHashMap',
        ],
        prereq=['zig-14-memory-management'],
        refs=[dict(title='Zig Standard Library — Index', url='https://ziglang.org/documentation/master/std/#root'),
              dict(title='Zig Reference — std.ArrayList', url='https://ziglang.org/documentation/master/std/#std.ArrayList')]),
    dict(
        slug='zig-21-ecosystem-next-steps',
        title='Ecosystem and Next Steps',
        desc='zig fmt, C interop, tooling, and advanced topics.',
        diff='intermediate',
        dur=20,
        objs=[
            'Use zig build and zig fmt workflows',
            'Explain Zig-C interop via @cImport',
            'Identify next advanced topics',
        ],
        prereq=['zig-17-modules-imports'],
        refs=[dict(title='Zig Learn — Official Guide', url='https://ziglearn.org/'),
              dict(title='Zig Reference — @cImport', url='https://ziglang.org/documentation/master/#C-Import'),
              dict(title='Awesome Zig — Curated List', url='https://github.com/catdevnull/awesome-zig')]),
]


if __name__ == '__main__':
    run_gen(LANGUAGE, 'zig', LESSONS, CODE, BASE)
