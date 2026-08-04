---
slug: discord-chat
title: "Discord Real-Time Communication"
description: "How Discord handles 19M+ servers and trillions of messages using Elixir, ScyllaDB, and custom C++ voice infrastructure."
order: 4
tags:
  - case-study
  - real-time
  - elixir
  - webbrtc
  - messaging
prerequisites: []
references:
  - title: "Real-time Communication at Scale with Elixir at Discord"
    author: "Elixir Language"
    url: "https://elixir-lang.org/blog/2020/10/08/real-time-communication-at-scale-with-elixir-at-discord/"
    type: "article"
    description: "Details the BEAM runtime, WebSocket gateways, and service discovery."
  - title: "How Discord Stores Trillions of Messages"
    author: "Discord Engineering"
    url: "https://discord.com/blog/how-discord-stores-trillions-of-messages"
    type: "article"
    description: "Deep dive on message storage evolution from MongoDB to ScyllaDB."
  - title: "How Discord Handles Two and Half Million Concurrent Voice Users"
    author: "Discord Engineering"
    url: "https://medium.com/discord-engineering/how-discord-handles-two-and-half-million-concurrent-voice-users-using-webrtc-ce01c3187429"
    type: "article"
    description: "Voice channel architecture with custom C++ SFU and WebRTC."
  - title: "Using Rust to Scale Elixir for 11 Million Concurrent Users"
    author: "Discord Engineering"
    url: "https://discord.com/blog/using-rust-to-scale-elixir-for-11-million-concurrent-users"
    type: "article"
    description: "How Discord integrated Rust NIFs for memory and performance optimization."
  - title: "How Discord Stores Trillions of Messages with High Performance"
    author: "ByteByteGo"
    url: "https://blog.bytebytego.com/p/how-discord-stores-trillions-of-messages"
    type: "article"
    description: "Technical analysis of ScyllaDB migration and request coalescing."
related_knowledge:
  - slug: case-studies-whatsapp-messaging
    title: "WhatsApp Real-Time Messaging"
    lesson_number: 3
  - slug: case-studies-twitter-newsfeed
    title: "Twitter/X News Feed"
    lesson_number: 2
knowledge_refs:
  - slug: "languages-erlang"
    title: "Erlang"
  - slug: "databases-cassandra"
    title: "Cassandra"
  - slug: "patterns-consistent-hashing"
    title: "Consistent Hashing"
---

# Discord Real-Time Communication

Discord supports 19M+ active servers and tens of millions of concurrent users through a combination of Elixir on the BEAM runtime, ScyllaDB for message storage, and custom C++ infrastructure for voice channels.

## The Scale

- **19M+ active servers** (guilds)
- **Tens of millions** of concurrent users
- **Trillions** of total messages stored
- **2.5M+ concurrent voice users**
- **850+ voice servers** across 13 regions

## Real-Time Messaging: Elixir & Phoenix

### The BEAM Foundation
Discord uses Elixir and the Erlang Virtual Machine (BEAM) from day one:
- **Lightweight processes:** Millions of concurrent WebSocket connections on ~400-500 machines
- **WebSocket Gateways:** Clients maintain persistent connections to Discord Gateway
- **Guild Sharding:** Consistent hashing distributes servers across backend processes

### Message Fan-Out with Manifold
When a message is sent in a 600K-user server, it must reach all connected clients. Distributed Erlang's default `send` saturates node interconnects at scale, so Discord open-sourced **Manifold**:
- Limits remote node sends to one per target node
- Target node handles local distribution via ETS (Erlang Term Storage)

### Service Discovery
Instead of full mesh networking, Discord uses `-connect_all false` with **etcd** for service discovery and configuration sharing.

## Message Storage: MongoDB → Cassandra → ScyllaDB

### The Cassandra Bottleneck
- Scaled to 177 nodes but hit two problems:
  - **Hot partitions:** Active channels overwhelmed single nodes
  - **JVM GC pauses:** Triggered severe tail-latency spikes

### The ScyllaDB Migration
ScyllaDB (C++ drop-in replacement for Cassandra) solved both issues:
- **Shard-per-core architecture:** Eliminated JVM GC entirely
- **p99 latency:** Dropped from 40-125ms to steady **15ms**
- **Node count:** Reduced from 177 to 72 while holding more data

### Rust Data Services Layer
A stateless Rust layer (Tokio + gRPC) sits in front of ScyllaDB:
- **Request coalescing:** Multiple clients requesting the same hot message → one DB query → result broadcast to all
- **High-speed migration:** Custom Rust tool moved trillions of messages at 3.2M messages/second, completing in 9 days

## Voice Channels: WebRTC & Custom C++ SFU

### Architecture
- **No P2P:** All traffic routes through dedicated media servers (prevents IP leakage and DDoS)
- **Custom C++ SFU:** Selective Forwarding Unit receives and forwards audio/video streams
- **Protocol optimizations:** Bypasses heavy ICE handshakes, uses Salsa20 encryption instead of DTLS/SRTP

### Failover
- Voice servers report health to etcd
- On crash or DDoS, guilds service selects healthy backup and seamlessly reconnects clients

## Key Design Decisions

1. **Elixir/BEAM** for massive WebSocket concurrency with minimal hardware
2. **ScyllaDB over Cassandra** for predictable low latency without JVM overhead
3. **Request coalescing** prevents database storms from hot messages
4. **Custom C++ SFU** for voice — off-the-shelf solutions couldn't meet latency requirements

## Lessons Learned

- **Choose your runtime for the problem:** BEAM excels at concurrent connections; Rust/C++ for performance-critical paths
- **Database migrations at scale need custom tooling:** Standard approaches can't move trillions of records
- **Request coalescing is essential** for hot-key scenarios
- **Voice and text have different requirements:** Separate infrastructure for each

---

*References:*
1. Elixir Language, "Real-time Communication at Scale with Elixir at Discord." [Link](https://elixir-lang.org/blog/2020/10/08/real-time-communication-at-scale-with-elixir-at-discord/)
2. Discord Engineering, "How Discord Stores Trillions of Messages." [Link](https://discord.com/blog/how-discord-stores-trillions-of-messages)
3. Discord Engineering, "How Discord Handles 2.5M Concurrent Voice Users." [Link](https://medium.com/discord-engineering/how-discord-handles-two-and-half-million-concurrent-voice-users-using-webrtc-ce01c3187429)
4. Discord Engineering, "Using Rust to Scale Elixir for 11 Million Concurrent Users." [Link](https://discord.com/blog/using-rust-to-scale-elixir-for-11-million-concurrent-users)
5. ByteByteGo, "How Discord Stores Trillions of Messages." [Link](https://blog.bytebytego.com/p/how-discord-stores-trillions-of-messages)
