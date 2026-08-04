---
slug: interview-framework
title: "The 4-Step Framework"
description: "A structured approach to system design interviews — from requirements gathering to trade-off analysis."
order: 14
tags:
  - system-design
  - interview
  - framework
  - methodology
  - trade-offs
prerequisites:
  - fundamentals-scalability
  - fundamentals-availability
  - fundamentals-estimation
references:
  - title: "System Design Interview – An Insider's Guide"
    author: "Alex Xu"
    url: "https://bytebytego.com/"
    type: "book"
    description: "The 4-step framework applied to real interview questions."
  - title: "Hello Interview: System Design Framework"
    author: "Hello Interview"
    url: "https://www.hellointerview.com/learn/system-design/in-a-hurry"
    type: "article"
    description: "Practical framework for system design interviews."
  - title: "Grokking the System Design Interview"
    author: "Design Gurus"
    url: "https://www.designgurus.io/course/grokking-the-system-design-interview"
    type: "course"
    description: "Structured approach to system design questions."
  - title: "System Design Interview Prep"
    author: "ByteByteGo"
    url: "https://blog.bytebytego.com/p/system-design-interview-prep"
    type: "article"
    description: "Comprehensive interview preparation guide."
  - title: "Designing Data-Intensive Applications"
    author: "Martin Kleppmann"
    url: "https://dataintensive.net/"
    type: "book"
    description: "Deep technical foundation for system design discussions."
related_knowledge:
  - slug: interview-common-questions
    title: "Common Design Questions"
    lesson_number: 15
  - slug: interview-trade-offs
    title: "Trade-off Analysis"
    lesson_number: 16
  - slug: fundamentals-estimation
    title: "Back-of-the-Envelope Estimation"
    lesson_number: 4
knowledge_refs:
  - slug: "patterns-consistent-hashing"
    title: "Consistent Hashing"
  - slug: "building-blocks-load-balancers"
    title: "Load Balancers"
  - slug: "building-blocks-caching"
    title: "Caching"
---

# The 4-Step Framework

System design interviews test your ability to design large-scale systems under time pressure. This 4-step framework provides a structured approach that interviewers expect.

## Step 1: Understand the Problem (2-3 minutes)

### Clarify Requirements
Before designing anything, understand what you're building:

**Functional Requirements:**
- What specific features must the system support?
- What are the core use cases?
- What is the scope? (e.g., "just the feed" vs "entire social network")

**Non-Functional Requirements:**
- **Scale:** How many users/requests/data?
- **Latency:** What response time is acceptable?
- **Availability:** What uptime is required?
- **Consistency:** Strong or eventual consistency?

### Ask Questions
Good candidates ask clarifying questions:
- "Should I focus on reads or writes?"
- "Is this read-heavy or write-heavy?"
- "What's the expected data volume?"
- "Are there any specific constraints?"

## Step 2: High-Level Design (5-10 minutes)

### Design the Architecture
Sketch the major components:
```
Client → Load Balancer → API Servers → Database
                     → Cache
                     → Message Queue → Workers
```

### Identify Key Components
- What services do you need?
- What databases are appropriate?
- Where does caching help?
- What needs to be asynchronous?

### Draw the Diagram
A clear diagram communicates your design better than words:
- Show data flow direction
- Label key components
- Indicate synchronous vs asynchronous paths

## Step 3: Deep Dive (15-20 minutes)

### Design Critical Components
The interviewer will ask you to focus on specific areas:
- "How would you design the news feed?"
- "How would you handle the search functionality?"
- "What about the notification system?"

### Address Bottlenecks
Identify and solve scaling challenges:
- **Database:** Sharding strategy, read replicas
- **Caching:** What to cache, eviction policy
- **Queue:** What needs async processing
- **Consistency:** How to handle eventual consistency

### Use Back-of-the-Envelope Estimation
Validate your design with numbers:
- "With 100M DAU and 10 actions per user, we need ~12K QPS"
- "Each user generates 1KB of data per action, so 100GB/day"
- "We need 3x replication, so 300GB/day storage"

## Step 4: Wrap Up (3-5 minutes)

### Summarize Your Design
Recap the key decisions:
- Architecture overview
- Key technology choices
- Scaling strategy

### Discuss Trade-offs
Every design has trade-offs. Acknowledge them:
- "We chose eventual consistency for performance"
- "We're trading storage for read speed with caching"
- "This design handles reads well but writes could be a bottleneck"

### Mention Improvements
If time permits, discuss:
- What you would do differently with more time
- Monitoring and alerting
- Disaster recovery
- Future scaling considerations

## Common Mistakes

| Mistake | Why It's Bad | Better Approach |
|---|---|---|
| Jumping to implementation | Shows lack of planning | Start with requirements |
| Ignoring non-functional requirements | Incomplete design | Explicitly discuss scale, latency, availability |
| Over-engineering | Wastes time on unnecessary complexity | Start simple, add complexity as needed |
| Not asking questions | Assumes wrong requirements | Clarify scope early |
| Ignoring trade-offs | Shows shallow thinking | Explicitly discuss pros/cons |

## Time Management

| Step | Time | Focus |
|---|---|---|
| Step 1: Requirements | 2-3 min | Clarify scope, ask questions |
| Step 2: High-Level | 5-10 min | Architecture, major components |
| Step 3: Deep Dive | 15-20 min | Critical components, bottlenecks |
| Step 4: Wrap Up | 3-5 min | Summary, trade-offs, improvements |

**Total: 30-45 minutes**

---

*References:*
1. Alex Xu, *System Design Interview – An Insider's Guide.* [Link](https://bytebytego.com/)
2. Hello Interview, "System Design Framework." [Link](https://www.hellointerview.com/learn/system-design/in-a-hurry)
3. Design Gurus, "Grokking the System Design Interview." [Link](https://www.designgurus.io/course/grokking-the-system-design-interview)
4. ByteByteGo, "System Design Interview Prep." [Link](https://blog.bytebytego.com/p/system-design-interview-prep)
5. Martin Kleppmann, *Designing Data-Intensive Applications.* [Link](https://dataintensive.net/)
