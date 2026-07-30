---
{
  "slug": "rs-19-performance",
  "title": "Performance and Optimization",
  "description": "Profiling with perf/flamegraph, release optimizations, SIMD, inlining, and benchmark-driven optimization.",
  "type": "lesson",
  "order": 19,
  "duration": "60 min",
  "difficulty": "expert",
  "learning_objectives": [
    "Profile Rust code with perf and flamegraphs",
    "Use release optimizations effectively",
    "Apply SIMD and vectorization",
    "Measure and optimize hot paths"
  ],
  "knowledge_refs": ["rust/rs-19-performance"],
  "prerequisites": ["RS-03"],
  "references": [
    {"title": "Rust Performance Book", "url": "https://nnethercote.github.io/perf-book/"},
    {"title": "The Rust Book — Performance", "url": "https://doc.rust-lang.org/book/ch14-01-release-profiles.html"},
    {"title": "Compiler Optimizations", "url": "https://doc.rust-lang.org/rustc/codegen-options/index.html"},
    {"title": "Criterion Benchmarking", "url": "https://docs.rs/criterion/"}
  ]
}
---

# RS-19: Performance and Optimization

## Introduction

Rust provides zero-cost abstractions, but performance still requires understanding compilation, optimization, and profiling. This section covers tools and techniques for writing fast Rust code, from compiler flags to benchmarking.

## Key Concepts

### 1. Release Profiles and Compiler Flags

Cargo supports different profiles (dev, release, test, bench). The release profile enables optimizations. Custom profiles can be defined in Cargo.toml.

```toml
[profile.release]
opt-level = 3           # max optimization (0-3, s, z)
lto = "fat"            # link-time optimization
codegen-units = 1      # single codegen unit for more optimization
debug = false          # no debug symbols
strip = "symbols"      # strip symbols from binary
panic = "abort"        # abort on panic (smaller binary)
```

```rust
// Conditional compilation based on profile
#[cfg(debug_assertions)]
fn debug_only() {
    println!("Debug mode");
}

#[cfg(not(debug_assertions))]
fn release_only() {
    println!("Release mode");
}

// Build commands
// $ cargo build --release
// $ cargo build --profile=performance  // custom profile

// View generated assembly
// $ cargo asm my_function
// $ cargo asm --rust my_function
```

### 2. Profiling Tools

Profile your code to find bottlenecks before optimizing. Common tools: perf (Linux), flamegraph, samply, and cargo-flamegraph.

```rust
// Use std::time::Instant for manual timing
use std::time::Instant;

fn measure() {
    let start = Instant::now();
    // ... code to measure ...
    let duration = start.elapsed();
    println!("Time: {:?}", duration);
}

// Profiling with perf (Linux)
// $ perf record --call-graph dwarf ./target/release/my_program
// $ perf report

// Flamegraph
// $ cargo flamegraph  // requires cargo-flamegraph

// Using criterion for benchmarks
// [dev-dependencies]
// criterion = "0.5"
//
// [[bench]]
// name = "my_bench"
// harness = false
//
// benches/my_bench.rs
// use criterion::{black_box, criterion_group, criterion_main, Criterion};

// fn fibonacci(n: u64) -> u64 {
//     match n {
//         0 => 1,
//         1 => 1,
//         n => fibonacci(n-1) + fibonacci(n-2),
//     }
// }
//
// fn bench_fib(c: &mut Criterion) {
//     c.bench_function("fib 20", |b| b.iter(|| fibonacci(black_box(20))));
// }
//
// criterion_group!(benches, bench_fib);
// criterion_main!(benches);
```

### 3. Common Optimization Techniques

Optimization strategies for common Rust code patterns.

```rust
// 1. Pre-allocate collections
fn pre_allocate() {
    // Bad: grows multiple times
    let mut v = Vec::new();
    for i in 0..1000 { v.push(i); }

    // Good: pre-allocate exact capacity
    let mut v = Vec::with_capacity(1000);
    for i in 0..1000 { v.push(i); }
}

// 2. Use iterators over indexed loops
fn iter_vs_index() {
    let data = vec![1, 2, 3, 4, 5];

    // Access pattern: iterators are faster (no bounds check)
    let sum: i32 = data.iter().sum();

    // 3. Avoid unnecessary clones
    fn process(s: &str) {
        // Bad: String::from creates a new allocation
        // let owned = s.to_string();

        // Good: use &str
        println!("{}", s);
    }

    // 4. Use SmallVec for small collections
    // use smallvec::SmallVec;
    // let v: SmallVec<[i32; 4]> = smallvec![1, 2, 3];

    // 5. String building: use format! or push_str
    fn build_string() -> String {
        let mut s = String::with_capacity(100);
        s.push_str("Hello");
        s.push_str(", ");
        s.push_str("World");
        s
    }
}
```

### 4. Inlining and Function Attributes

Control function inlining with attributes. The compiler decides inlining based on heuristics, but you can provide hints.

```rust
// Force inlining (small, hot functions)
#[inline(always)]
fn small_hot_function(x: i32) -> i32 {
    x * 2
}

// Prevent inlining (large, cold functions)
#[inline(never)]
fn large_cold_function() {
    // expensive error handling
}

// The compiler applies inlining automatically in release mode
// LTO enables cross-crate inlining

// Cold path hint
#[cold]
fn cold_path() {
    // This function is unlikely to be called
    // Compiler optimizes for the hot path
}

// #[track_caller] for better error messages
#[track_caller]
fn assert_nonzero(n: i32) {
    if n == 0 {
        panic!("zero!");
    }
}
```

### 5. SIMD and Advanced Optimizations

Single Instruction, Multiple Data (SIMD) for parallel processing. The `core::simd` module (nightly) and the `packed_simd` crate provide portable SIMD.

```rust
// Auto-vectorization: the compiler can vectorize simple loops
fn sum_auto_vectorized(data: &[f32]) -> f32 {
    data.iter().sum()  // compiler auto-vectorizes this
}

// Manual SIMD (nightly)
// #![feature(portable_simd)]
// use std::simd::f32x4;

// fn sum_simd(data: &[f32]) -> f32 {
//     let mut sums = f32x4::splat(0.0);
//     for chunk in data.chunks(4) {
//         let v = f32x4::from_slice(chunk);
//         sums += v;
//     }
//     sums.reduce_sum()
// }

// Cache-friendly data access
// 1. Iterate in row-major order (cache locality)
// 2. Use arrays of structs (AoS) vs structs of arrays (SoA)
// 3. Align data to cache line boundaries

// #[repr(align(64))]  // align to cache line
// struct Aligned {
//     data: [u8; 64],
// }

// Compiler intrinsics
// use std::arch::x86_64::*;
// unsafe {
//     let a = _mm_set1_epi32(1);
//     let b = _mm_set1_epi32(2);
//     let c = _mm_add_epi32(a, b);
// }
```

## Practice Questions

1. What is the difference between debug and release profiles?
2. What is LTO? How does it improve performance?
3. What is the purpose of profiling before optimizing?
4. When would you use #[inline(always)] vs #[inline(never)]?
5. What is auto-vectorization? How can you help the compiler vectorize code?

## LLM Prompts for Deeper Understanding

1. "Explain Rust optimization: release profiles, LTO, codegen-units, and compiler flags"
2. "Show profiling tools: perf, flamegraph, criterion, and benchmark-driven optimization"
3. "Teach advanced topics: SIMD, inlining, cache-friendly data layouts, and allocator tuning"

## Key Takeaways

- Profile before optimizing; use perf, flamegraph, and criterion
- Release builds enable optimizations (opt-level, LTO, codegen-units)
- Pre-allocate collections, avoid clones, use iterators for performance
- Inline attributes provide hints to the compiler
- Auto-vectorization handles simple loops; SIMD for manual parallelization