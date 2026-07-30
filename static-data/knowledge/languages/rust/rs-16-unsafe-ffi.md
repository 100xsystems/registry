---
{
  "slug": "rs-16-unsafe-ffi",
  "title": "Unsafe Rust and FFI",
  "description": "Unsafe keyword, raw pointers, calling C functions, writing C-compatible APIs, and safety invariants.",
  "type": "lesson",
  "order": 16,
  "duration": "75 min",
  "difficulty": "expert",
  "learning_objectives": [
    "Use unsafe blocks for raw pointer operations",
    "Call C functions from Rust with FFI",
    "Expose Rust functions to C",
    "Understand safety invariants"
  ],
  "knowledge_refs": ["rust/rs-16-unsafe-ffi"],
  "prerequisites": ["RS-08"],
  "references": [
    {"title": "The Rust Book — Unsafe Rust", "url": "https://doc.rust-lang.org/book/ch19-01-unsafe-rust.html"},
    {"title": "The Rustonomicon", "url": "https://doc.rust-lang.org/nomicon/"},
    {"title": "Rust by Example — FFI", "url": "https://doc.rust-lang.org/stable/rust-by-example/std_misc/ffi.html"},
    {"title": "std::ffi", "url": "https://doc.rust-lang.org/std/ffi/index.html"}
  ]
}
---

# RS-16: Unsafe Rust and FFI

## Introduction

Unsafe Rust allows operations that the compiler cannot guarantee to be safe: dereferencing raw pointers, calling unsafe functions, accessing mutable statics, and implementing unsafe traits. FFI (Foreign Function Interface) allows calling C code from Rust and vice versa.

## Key Concepts

### 1. Unsafe Superpowers

Unsafe code has five superpowers: dereference raw pointers, call unsafe functions, access/modify mutable statics, implement unsafe traits, and access union fields. Unsafe does not disable borrow checking — it only enables these specific operations.

```rust
fn main() {
    // Dereference raw pointer
    let mut num = 5;
    let r1 = &num as *const i32;
    let r2 = &mut num as *mut i32;

    unsafe {
        println!("r1: {}", *r1);
        println!("r2: {}", *r2);
    }

    // Create raw pointer from heap allocation
    let ptr = Box::into_raw(Box::new(42));
    unsafe {
        println!("Box value: {}", *ptr);
        // Must manually free
        drop(Box::from_raw(ptr));
    }

    // Mutable static variable
    static mut COUNTER: u32 = 0;
    unsafe {
        COUNTER += 1;
        println!("Counter: {}", COUNTER);
    }
}
```

### 2. FFI: Calling C from Rust

The `extern "C"` block declares functions from a C library. The `#[link]` attribute specifies the library to link against.

```rust
// Declare C functions
extern "C" {
    fn abs(input: i32) -> i32;
    fn sqrt(x: f64) -> f64;
    fn cos(x: f64) -> f64;
}

fn main() {
    unsafe {
        println!("Absolute value of -3: {}", abs(-3));
        println!("Square root of 16: {}", sqrt(16.0));
        println!("Cosine of 0: {}", cos(0.0));
    }
}

// Linking to a custom C library
// #[link(name = "mylib")]
// extern "C" {
//     fn my_c_function(x: i32) -> i32;
// }
```

### 3. FFI: Exposing Rust to C

Use `extern "C"` on Rust functions to make them callable from C. The `#[no_mangle]` attribute prevents name mangling.

```rust
// Function callable from C
#[no_mangle]
pub extern "C" fn add(a: i32, b: i32) -> i32 {
    a + b
}

// More complex: return a struct
#[repr(C)]
pub struct Point {
    x: f64,
    y: f64,
}

#[no_mangle]
pub extern "C" fn create_point(x: f64, y: f64) -> Point {
    Point { x, y }
}

#[no_mangle]
pub extern "C" fn distance(p: Point) -> f64 {
    (p.x * p.x + p.y * p.y).sqrt()
}

// C-side usage:
// #include <stdint.h>
// typedef struct { double x; double y; } Point;
// int32_t add(int32_t a, int32_t b);
// Point create_point(double x, double y);
// double distance(Point p);
```

### 4. C String Handling

Converting between C strings (null-terminated) and Rust strings (sized, UTF-8). CString for owned C strings, CStr for borrowed C strings.

```rust
use std::ffi::{CString, CStr};
use std::os::raw::c_char;

// Calling C's puts function
extern "C" {
    fn puts(s: *const c_char) -> i32;
}

fn main() {
    // Rust String -> C String
    let rust_string = "Hello from Rust!";
    let c_string = CString::new(rust_string).unwrap();

    unsafe {
        puts(c_string.as_ptr());
    }

    // C String -> Rust String
    fn c_str_to_string(c_str: *const c_char) -> String {
        let c_str = unsafe { CStr::from_ptr(c_str) };
        c_str.to_str().unwrap().to_string()
    }

    // Return a C string from Rust
    #[no_mangle]
    pub extern "C" fn greet(name: *const c_char) -> *mut c_char {
        let name = unsafe { CStr::from_ptr(name) };
        let greeting = format!("Hello, {}!", name.to_str().unwrap());
        CString::new(greeting).unwrap().into_raw()
    }

    // Free the C string (must be called from C to avoid memory leak)
    #[no_mangle]
    pub extern "C" fn free_greeting(s: *mut c_char) {
        if !s.is_null() {
            unsafe { drop(CString::from_raw(s)); }
        }
    }
}
```

### 5. Safety Invariants and Best Practices

The key rule of unsafe: encapsulate unsafe code in safe abstractions. The unsafe block should be as small as possible. Document safety invariants with comments.

```rust
// Safe abstraction over unsafe code
mod split_at {
    // Safe function that internally uses unsafe
    pub fn split_at_mut<T>(slice: &mut [T], mid: usize) -> (&mut [T], &mut [T]) {
        let len = slice.len();
        assert!(mid <= len);  // safety check

        // SAFETY: mid is within bounds, and we return two non-overlapping slices
        unsafe {
            let ptr = slice.as_mut_ptr();
            (
                std::slice::from_raw_parts_mut(ptr, mid),
                std::slice::from_raw_parts_mut(ptr.add(mid), len - mid),
            )
        }
    }
}

// Safe wrapper around raw pointer
struct UnsafeBuffer {
    ptr: *mut u8,
    len: usize,
}

impl UnsafeBuffer {
    fn new(size: usize) -> Self {
        let layout = std::alloc::Layout::from_size_align(size, 1).unwrap();
        // SAFETY: layout is valid
        let ptr = unsafe { std::alloc::alloc(layout) };
        UnsafeBuffer { ptr, len: size }
    }

    fn write(&mut self, offset: usize, value: u8) {
        assert!(offset < self.len);
        // SAFETY: offset is within bounds
        unsafe {
            self.ptr.add(offset).write(value);
        }
    }

    fn read(&self, offset: usize) -> u8 {
        assert!(offset < self.len);
        // SAFETY: offset is within bounds
        unsafe { self.ptr.add(offset).read() }
    }
}

impl Drop for UnsafeBuffer {
    fn drop(&mut self) {
        let layout = std::alloc::Layout::from_size_align(self.len, 1).unwrap();
        // SAFETY: ptr was allocated with this layout
        unsafe { std::alloc::dealloc(self.ptr, layout); }
    }
}
```

## Practice Questions

1. What are the five superpowers of unsafe Rust?
2. Does unsafe disable the borrow checker?
3. How do you call a C function from Rust?
4. How do you expose a Rust function to C?
5. What is the most important rule when writing unsafe code?

## LLM Prompts for Deeper Understanding

1. "Explain unsafe Rust: raw pointers, unsafe functions, mutable statics, and unsafe traits"
2. "Show FFI: calling C from Rust, extern blocks, CString, and repr(C)"
3. "Teach safety: encapsulating unsafe in safe abstractions, safety invariants, and memory management"

## Key Takeaways

- Unsafe enables five superpowers: raw pointers, unsafe functions, mutable statics, unsafe traits, unions
- Unsafe does NOT disable borrow checking
- FFI uses extern "C" blocks for calling C and exposing Rust to C
- Use CString/CStr for C string interop
- Encapsulate unsafe code in safe abstractions; document safety invariants