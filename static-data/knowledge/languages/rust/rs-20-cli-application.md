---
{
  "slug": "rs-20-cli-application",
  "title": "Building a CLI Application",
  "description": "Argument parsing with clap, error handling, configuration, logging, testing, and building a complete CLI tool.",
  "type": "lesson",
  "order": 20,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Parse command-line arguments with clap",
    "Implement robust error handling",
    "Add logging and configuration",
    "Build and distribute a CLI tool"
  ],
  "knowledge_refs": ["rust/rs-20-cli-application"],
  "prerequisites": ["RS-08", "RS-12"],
  "references": [
    {"title": "clap Documentation", "url": "https://docs.rs/clap/"},
    {"title": "anyhow Documentation", "url": "https://docs.rs/anyhow/"},
    {"title": "Command Line Rust Book", "url": "https://www.oreilly.com/library/view/command-line-rust/"},
    {"title": "Rust CLI Working Group", "url": "https://rust-cli.github.io/"}
  ]
}
---

# RS-20: Building a CLI Application

## Introduction

Rust is an excellent choice for building CLI tools. The ecosystem provides robust libraries for argument parsing, error handling, and output formatting. This lesson covers building a complete CLI application from scratch.

## Key Concepts

### 1. Argument Parsing with clap

clap is the most popular argument parsing library. It supports subcommands, flags, options, automatic help generation, and shell completion.

```rust
use clap::{Parser, Subcommand, Args};

#[derive(Parser)]
#[command(name = "myapp")]
#[command(about = "A CLI tool", long_about = None)]
struct Cli {
    /// Optional name to operate on
    #[arg(short = 'n', long = "name")]
    name: Option<String>,

    /// Number of times to greet
    #[arg(short = 'c', long = "count", default_value_t = 1)]
    count: u8,

    /// Verbose mode
    #[arg(short, long, action = clap::ArgAction::Count)]
    verbose: u8,

    #[command(subcommand)]
    command: Option<Commands>,
}

#[derive(Subcommand)]
enum Commands {
    /// Greet someone
    Greet {
        /// Name to greet
        #[arg(short, long)]
        name: String,
    },
    /// Show version
    Version,
}

fn main() {
    let cli = Cli::parse();

    match &cli.command {
        Some(Commands::Greet { name }) => {
            println!("Hello, {}!", name);
        }
        Some(Commands::Version) => {
            println!("Version 1.0.0");
        }
        None => {
            println!("No command specified");
        }
    }
}
```

### 2. Error Handling with anyhow

anyhow provides flexible error handling for CLI applications. It wraps any error type and provides context.

```rust
use anyhow::{Context, Result};
use std::fs;
use std::path::PathBuf;

fn read_config(path: &PathBuf) -> Result<String> {
    let content = fs::read_to_string(path)
        .with_context(|| format!("Failed to read config file: {:?}", path))?;
    Ok(content)
}

fn parse_config(content: &str) -> Result<Config> {
    toml::from_str(content)
        .context("Failed to parse config file")?
}

fn main() -> Result<()> {
    let path = PathBuf::from("config.toml");
    let content = read_config(&path)?;
    let config = parse_config(&content)?;

    println!("Config: {:?}", config);
    Ok(())
}

// Custom error types with thiserror
// use thiserror::Error;
//
// #[derive(Error, Debug)]
// enum AppError {
//     #[error("Config error: {0}")]
//     Config(String),
//     #[error("IO error: {0}")]
//     Io(#[from] std::io::Error),
// }
```

### 3. Logging and Output

Use the `log` crate with `env_logger` or `pretty_env_logger` for logging. Use colored output for better UX.

```rust
use log::{info, warn, error, debug};
use std::time::Instant;

fn main() {
    // Initialize logger
    env_logger::init();
    // or: pretty_env_logger::init();

    // Run: RUST_LOG=info myapp
    // Run: RUST_LOG=debug myapp
    // Run: RUST_LOG=error myapp

    info!("Starting application");
    let start = Instant::now();

    // Log with different levels
    debug!("Debug message: {}", "details");
    info!("Processing data...");
    warn!("This might be slow");
    error!("Something went wrong: {}", "error message");

    info!("Completed in {:?}", start.elapsed());

    // Colored output with colored crate
    // use colored::*;
    // println!("{}", "Error".red().bold());
    // println!("{}", "Success".green());
    // println!("{}", "Warning".yellow());
}
```

### 4. Configuration Management

Handle configuration from multiple sources with clear precedence: CLI args > env vars > config file > defaults.

```rust
use std::path::PathBuf;
use std::env;

struct Config {
    host: String,
    port: u16,
    debug: bool,
    config_path: PathBuf,
}

impl Config {
    fn load() -> Self {
        // Defaults
        let mut config = Config {
            host: String::from("localhost"),
            port: 8080,
            debug: false,
            config_path: PathBuf::from("config.toml"),
        };

        // Config file overrides defaults
        if let Ok(content) = std::fs::read_to_string(&config.config_path) {
            if let Ok(file_config) = toml::from_str::<Config>(&content) {
                config.host = file_config.host;
                config.port = file_config.port;
            }
        }

        // Env vars override config file
        if let Ok(host) = env::var("APP_HOST") {
            config.host = host;
        }
        if let Ok(port) = env::var("APP_PORT") {
            if let Ok(p) = port.parse() {
                config.port = p;
            }
        }

        // CLI args override everything (via clap)
        // Handled by clap::Parser::parse()

        config
    }
}
```

### 5. Distribution and Cross-Compilation

Build and distribute your CLI tool for multiple platforms.

```rust
// Cargo.toml for distribution
// [package]
// name = "myapp"
// version = "1.0.0"
// edition = "2021"
//
// [profile.release]
// lto = true
// codegen-units = 1
// strip = true
// panic = "abort"

// Cross-compile
// $ cargo build --release
// $ cargo install --path .
// $ cargo build --release --target x86_64-unknown-linux-gnu
// $ cargo build --release --target aarch64-apple-darwin
// $ cargo build --release --target x86_64-pc-windows-gnu

// Create a Homebrew formula
// class MyApp < Formula
//   desc "My CLI tool"
//   homepage "https://github.com/user/myapp"
//   url "https://github.com/user/myapp/releases/download/v1.0.0/myapp-macos.tar.gz"
//   sha256 "abc123..."
//   def install
//     bin.install "myapp"
//   end
// end

// GitHub Actions for cross-platform builds
// name: Build and Release
// on: [push]
// jobs:
//   build:
//     strategy:
//       matrix:
//         os: [ubuntu-latest, macos-latest, windows-latest]
//     runs-on: ${{ matrix.os }}
//     steps:
//       - uses: actions/checkout@v4
//       - run: cargo build --release
//       - uses: actions/upload-artifact@v4
//         with:
//           name: myapp-${{ matrix.os }}
//           path: target/release/myapp*
```

## Practice Questions

1. How do you define a CLI argument with clap? What attributes control its behavior?
2. What is the difference between anyhow and thiserror?
3. How do you configure logging with env_logger?
4. What is the precedence order for configuration sources?
5. How do you cross-compile a Rust CLI application?

## LLM Prompts for Deeper Understanding

1. "Explain clap: Parser derive, Subcommand, Args, and argument attributes"
2. "Show error handling: anyhow for applications, thiserror for libraries"
3. "Teach CLI development: logging, configuration, color output, and distribution"

## Key Takeaways

- clap provides ergonomic argument parsing with derive macros
- anyhow for flexible error handling; thiserror for custom error types
- env_logger for configurable logging; colored for terminal output
- Configuration precedence: CLI args > env vars > config file > defaults
- Cross-compile with --target flag; distribute via GitHub releases