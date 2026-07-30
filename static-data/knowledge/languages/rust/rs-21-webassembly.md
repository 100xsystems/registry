---
{
  "slug": "rs-21-webassembly",
  "title": "WebAssembly with Rust",
  "description": "Compiling to WebAssembly, wasm-pack, wasm-bindgen, web-sys, DOM access, and performance considerations.",
  "type": "lesson",
  "order": 21,
  "duration": "60 min",
  "difficulty": "expert",
  "learning_objectives": [
    "Compile Rust to WebAssembly",
    "Use wasm-pack for building and packaging",
    "Interact with JavaScript and DOM",
    "Optimize WebAssembly performance"
  ],
  "knowledge_refs": ["rust/rs-21-webassembly"],
  "prerequisites": ["RS-09"],
  "references": [
    {"title": "Rust and WebAssembly Book", "url": "https://rustwasm.github.io/docs/book/"},
    {"title": "wasm-pack Documentation", "url": "https://rustwasm.github.io/wasm-pack/"},
    {"title": "wasm-bindgen", "url": "https://rustwasm.github.io/docs/wasm-bindgen/"},
    {"title": "web-sys crate", "url": "https://docs.rs/web-sys/"}
  ]
}
---

# RS-21: WebAssembly with Rust

## Introduction

Rust can compile to WebAssembly (Wasm), enabling high-performance code in the browser. wasm-pack and wasm-bindgen provide tools for building, packaging, and integrating with JavaScript. Rust's memory safety and performance make it ideal for WebAssembly.

## Key Concepts

### 1. Setting Up a Wasm Project

Create a Rust library project and configure it for WebAssembly. The `wasm-pack` tool handles building and packaging.

```rust
// Cargo.toml
// [package]
// name = "my-wasm-app"
// version = "0.1.0"
// edition = "2021"
//
// [lib]
// crate-type = ["cdylib"]  // required for wasm
//
// [dependencies]
// wasm-bindgen = "0.2"

// lib.rs
use wasm_bindgen::prelude::*;

// Export a function to JavaScript
#[wasm_bindgen]
pub fn greet(name: &str) -> String {
    format!("Hello, {}!", name)
}

// Build
// $ wasm-pack build --target web
// $ wasm-pack build --target bundler  // for webpack/vite
// $ wasm-pack build --target nodejs   // for Node.js
```

### 2. Exporting Functions and Structs

Export Rust functions, structs, and enums to JavaScript. Use `#[wasm_bindgen]` to mark exports.

```rust
use wasm_bindgen::prelude::*;

// Export a struct
#[wasm_bindgen]
pub struct Point {
    x: f64,
    y: f64,
}

#[wasm_bindgen]
impl Point {
    #[wasm_bindgen(constructor)]
    pub fn new(x: f64, y: f64) -> Point {
        Point { x, y }
    }

    #[wasm_bindgen(getter)]
    pub fn x(&self) -> f64 {
        self.x
    }

    #[wasm_bindgen(setter)]
    pub fn set_x(&mut self, x: f64) {
        self.x = x;
    }

    pub fn distance(&self, other: &Point) -> f64 {
        ((self.x - other.x).powi(2) + (self.y - other.y).powi(2)).sqrt()
    }
}

// Export an enum
#[wasm_bindgen]
pub enum Color {
    Red,
    Green,
    Blue,
}

// Export a function that returns a struct
#[wasm_bindgen]
pub fn create_point(x: f64, y: f64) -> Point {
    Point::new(x, y)
}
```

### 3. DOM Access with web-sys

The `web-sys` crate provides bindings to Web APIs. Access DOM elements, manipulate the document, and handle events.

```rust
// Cargo.toml
// [dependencies]
// wasm-bindgen = "0.2"
// web-sys = { version = "0.3", features = [
//     "Document",
//     "Element",
//     "HtmlElement",
//     "Window",
//     "console",
// ] }

use wasm_bindgen::prelude::*;
use wasm_bindgen::JsCast;

#[wasm_bindgen]
pub fn setup() -> Result<(), JsValue> {
    // Access window and document
    let window = web_sys::window().expect("no global window");
    let document = window.document().expect("no document");
    let body = document.body().expect("no body");

    // Create a new element
    let div = document.create_element("div")?;
    div.set_text_content(Some("Hello from Rust!"));
    body.append_child(&div)?;

    // Access console
    let console = web_sys::console::log_1(&"Hello from Rust!".into());

    Ok(())
}

// Event listeners
#[wasm_bindgen]
pub fn add_click_handler(selector: &str) -> Result<(), JsValue> {
    let window = web_sys::window().expect("no window");
    let document = window.document().expect("no document");
    let element = document.query_selector(selector)?.expect("element not found");

    let closure = Closure::wrap(Box::new(move || {
        web_sys::console::log_1(&"Clicked!".into());
    }) as Box<dyn FnMut()>);

    element.add_event_listener_with_callback("click", closure.as_ref().unchecked_ref())?;
    closure.forget();  // prevent closure from being dropped
    Ok(())
}
```

### 4. Interacting with JavaScript

Import JavaScript functions and call them from Rust. Handle complex types and promises.

```rust
use wasm_bindgen::prelude::*;

// Import a JavaScript function
#[wasm_bindgen]
extern "C" {
    #[wasm_bindgen(js_namespace = console)]
    fn log(s: &str);

    #[wasm_bindgen(js_namespace = Math)]
    fn random() -> f64;

    #[wasm_bindgen(js_namespace = JSON)]
    fn parse(text: &str) -> Result<JsValue, JsValue>;

    #[wasm_bindgen(js_namespace = console)]
    fn warn(s: &str);
}

// Use imported functions
#[wasm_bindgen]
pub fn use_js_functions() {
    log("Hello from Rust!");
    let r = random();
    log(&format!("Random: {}", r));
}

// Import a JavaScript class
// #[wasm_bindgen(module = "/js/utils.js")]
// extern "C" {
//     pub type MyClass;
//     #[wasm_bindgen(constructor)]
//     fn new() -> MyClass;
//     #[wasm_bindgen(method)]
//     fn method(this: &MyClass, input: &str) -> String;
// }

// Working with Promises (async)
// use wasm_bindgen_futures::JsFuture;
//
// #[wasm_bindgen]
// pub async fn fetch_data(url: &str) -> Result<JsValue, JsValue> {
//     let window = web_sys::window().unwrap();
//     let promise = window.fetch_with_str(url);
//     let response = JsFuture::from(promise).await?;
//     Ok(response)
// }
```

### 5. Performance Optimization

Optimize WebAssembly for size and speed. Use `wee_alloc` for smaller binaries, enable link-time optimization, and profile with browser tools.

```rust
// Use a smaller allocator
// Cargo.toml
// [dependencies]
// wee_alloc = { version = "0.4", default-features = false }

// #[global_allocator]
// static ALLOC: wee_alloc::WeeAlloc = wee_alloc::WeeAlloc::INIT;

// Cargo.toml optimization
// [profile.release]
// opt-level = "s"       // optimize for size
// lto = true
// codegen-units = 1
// strip = "symbols"
// panic = "abort"

// Benchmarking in the browser
// Use console.time() and console.timeEnd()
// Or use the `web-sys` Performance API

#[wasm_bindgen]
pub fn performance_test() {
    let performance = web_sys::window()
        .unwrap()
        .performance()
        .unwrap();

    let start = performance.now();
    // ... do work ...
    let end = performance.now();
    web_sys::console::log_1(&format!("Time: {}ms", end - start).into());
}

// Avoid unnecessary allocations
// - Use &str instead of String in function signatures
// - Use slices instead of Vec
// - Minimize serialization/deserialization overhead

// Size optimization tips
// - Use `wasm-opt` for post-processing
// - Remove unused code with dead code elimination
// - Use `twiggy` to analyze binary size
// $ wasm-opt -Oz -o output.wasm input.wasm
// $ twiggy top output.wasm
```

## Practice Questions

1. What is the difference between `--target web` and `--target bundler` in wasm-pack?
2. How do you export a Rust struct to JavaScript?
3. How do you import a JavaScript function into Rust?
4. What is the `Closure` type used for in wasm-bindgen?
5. How do you optimize WebAssembly binary size?

## LLM Prompts for Deeper Understanding

1. "Explain Rust-Wasm: compilation target, wasm-bindgen, memory model, and the glue layer"
2. "Show web-sys: DOM access, event listeners, and Web API bindings"
3. "Teach Wasm optimization: binary size, performance, profiling, and the allocator"

## Key Takeaways

- Rust compiles to WebAssembly; wasm-pack handles building and packaging
- `#[wasm_bindgen]` exports Rust functions, structs, and enums to JS
- `web-sys` provides bindings to Web APIs (DOM, console, fetch)
- Import JS functions with `extern "C"` blocks
- Optimize for size with `opt-level = "s"`, LTO, and `wee_alloc`