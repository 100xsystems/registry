# 100xSystems Registry

This repository is the central index for all available learning systems on [100xSystems](https://github.com/100xsystems).

## How It Works

The `registry.json` file contains metadata for every system. Both the [CLI](https://github.com/100xsystems/cli) and the [Website](https://github.com/100xsystems/website) read this file to discover available systems, their repositories, and tracks.

The CLI downloads only the repository it needs. The website shallow-clones all repositories during build.

## Adding a New System

1. Create a new repository under `100xsystems/<system-slug>` following the [system template](https://github.com/100xsystems/system-template) (coming soon)
2. Open a PR to this repository adding your system to `registry.json`
3. Once merged, the CLI and website will automatically discover it

## Current Systems

| System | Description | Tracks |
|--------|-------------|--------|
| Claude Code | Build an AI-powered coding agent | TypeScript, Java |
| Microservices | Master distributed systems architecture | Spring Boot, NestJS |
