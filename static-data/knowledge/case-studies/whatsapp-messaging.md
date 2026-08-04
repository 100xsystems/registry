---
slug: whatsapp-messaging
title: "WhatsApp Real-Time Messaging"
description: "How WhatsApp delivers 100B+ messages/day to 2B+ users with only ~50 engineers using Erlang and XMPP."
order: 3
tags:
  - case-study
  - messaging
  - erlang
  - real-time
  - end-to-end-encryption
prerequisites: []
references:
  - title: "How WhatsApp Handled 1 Billion Users with 50 Engineers"
    author: "Better Engineering"
    url: "https://betterengineers.substack.com/p/how-whatsapp-handled-1-billion-users"
    type: "article"
    description: "Deep dive into WhatsApp's architectural simplicity and scaling strategy."
  - title: "How WhatsApp Delivers Messages to 2 Billion Users"
    author: "Akshay Ghalme"
    url: "https://akshayghalme.com/blogs/how-whatsapp-handles-2-billion-users/"
    type: "article"
    description: "Messaging at planetary scale with technical architecture details."
  - title: "How WhatsApp Handles 40 Billion Messages Per Day"
    author: "ByteByteGo"
    url: "https://blog.bytebytego.com/p/how-whatsapp-handles-40-billion-messages"
    type: "article"
    description: "Visual breakdown of WhatsApp's message delivery pipeline."
  - title: "How WhatsApp Handles 100 Billion Messages Daily"
    author: "CodeToDeploy"
    url: "https://medium.com/codetodeploy/how-whatsapp-handles-100-billion-messages-daily-a-deep-dive-into-its-system-architecture-c43203834a02"
    type: "article"
    description: "Comprehensive system architecture deep dive."
  - title: "Designing WhatsApp"
    author: "High Scalability"
    url: "https://highscalability.com/designing-whatsapp/"
    type: "article"
    description: "Architecture analysis from the High Scalability archive."
related_knowledge:
  - slug: case-studies-twitter-newsfeed
    title: "Twitter/X News Feed"
    lesson_number: 2
  - slug: case-studies-discord-chat
    title: "Discord Real-Time Communication"
    lesson_number: 4
knowledge_refs:
  - slug: "languages-erlang"
    title: "Erlang"
  - slug: "patterns-circuit-breaker-pattern"
    title: "Circuit Breaker"
  - slug: "databases-redis"
    title: "Redis"
---

# WhatsApp Real-Time Messaging

WhatsApp is one of the most efficient distributed systems ever deployed — serving 2B+ monthly active users and routing 100B+ messages daily with famously fewer than 50 engineers.

## The Scale

- **2B+ monthly active users**
- **100B+ messages per day**
- **~50 engineers** (pre-acquisition)
- **2M concurrent connections per server**
- **Sub-10ms server-side processing time**

## The Core Architecture

### Erlang and the BEAM Virtual Machine

WhatsApp's backend runs on **Erlang** using the **BEAM virtual machine** with a modified XMPP implementation (`ejabberd`).

**Why Erlang?**
- **Lightweight processes:** Each Erlang process uses ~300 bytes of memory (vs. 1-8MB for OS threads)
- **One process per connection:** Every connected client gets its own Erlang process
- **Massive concurrency:** A single commodity server handles **2M concurrent TCP connections**
- **"Let It Crash" philosophy:** Processes crash in isolation and are auto-restarted by supervisors in milliseconds
- **Hot code swapping:** Deploy updates without restarting or dropping connections

### Message Delivery Pipeline

**Online delivery (< 10ms):**
1. Alice's device encrypts message locally
2. Encrypted blob sent over persistent TCP socket to WhatsApp server
3. Server matches recipient (Bob) to his active Erlang process
4. Encrypted blob forwarded immediately
5. Bob's device decrypts and sends ACK (second grey checkmark ✓✓)

**Offline delivery:**
1. If Bob is offline, server holds encrypted blob in offline queue (up to 30 days)
2. When Bob reconnects, queue flushes in order
3. Push notification via APNs/FCM (no message text, just a wake-up ping)

### End-to-End Encryption (Signal Protocol)

Every message, photo, video, and call is E2EE by default:
- **X3DH key exchange:** Initial handshake using pre-keys
- **Double Ratchet algorithm:** Unique key per message (forward + future secrecy)
- **Sender Key for groups:** Encrypt once, server fans out to all participants

### Media Handling

Multimedia files are handled asynchronously:
1. Sender encrypts media locally with unique symmetric key
2. Encrypted blob uploaded to CDN-backed cloud storage
3. Sender transmits lightweight message with CDN URL + decryption key
4. Recipient downloads and decrypts locally

## Scaling Strategies

- **Mnesia & ETS:** In-memory stores for session state and routing tables
- **Database fragmentation:** Data partitioned via consistent hashing, each fragment bound to one process
- **One-way replication:** Primary node for writes, passive secondary for failover (no bidirectional consensus)
- **Feature minimalism:** No ads, no feeds, no recommendations — just fast, secure messaging

## Key Design Decisions

1. **Erlang's actor model** solves the C10K problem (and beyond) elegantly
2. **End-to-end encryption by default** means the server never sees plaintext
3. **Feature minimalism** reduces operational complexity and bug surface
4. **One-process-per-connection** scales horizontally with simple hardware

## Lessons Learned

- **Technology choice matters:** Erlang's concurrency model was critical to WhatsApp's efficiency ratio
- **Simplicity scales:** Fewer features = fewer bugs = smaller team = faster iteration
- **Security by default:** E2EE from day one built user trust
- **Let it crash:** Supervision trees are more robust than defensive programming

---

*References:*
1. Better Engineering, "How WhatsApp Handled 1 Billion Users with 50 Engineers." [Link](https://betterengineers.substack.com/p/how-whatsapp-handled-1-billion-users)
2. Akshay Ghalme, "How WhatsApp Delivers Messages to 2 Billion Users." [Link](https://akshayghalme.com/blogs/how-whatsapp-handles-2-billion-users/)
3. ByteByteGo, "How WhatsApp Handles 40 Billion Messages Per Day." [Link](https://blog.bytebytego.com/p/how-whatsapp-handles-40-billion-messages)
4. CodeToDeploy, "How WhatsApp Handles 100 Billion Messages Daily." [Link](https://medium.com/codetodeploy/how-whatsapp-handles-100-billion-messages-daily-a-deep-dive-into-its-system-architecture-c43203834a02)
5. High Scalability, "Designing WhatsApp." [Link](https://highscalability.com/designing-whatsapp/)
