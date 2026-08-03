---
{
  "title": "Events and Logging",
  "description": "Emit events for off-chain listeners.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare events",
    "Emit events on state change",
    "Index event parameters",
    "Query logs from clients"
  ],
  "knowledge_refs": [
    "solidity/solidity-05-events"
  ],
  "prerequisites": [
    "Solidity-04: Functions and Modifiers"
  ],
  "references": [
    {
      "title": "Solidity Documentation",
      "url": "https://docs.soliditylang.org/",
      "description": "Official language docs"
    },
    {
      "title": "Solidity by Example",
      "url": "https://solidity-by-example.org/",
      "description": "Learn by working examples"
    },
    {
      "title": "CryptoZombies",
      "url": "https://cryptozombies.io/",
      "description": "Interactive Solidity tutorial"
    },
    {
      "title": "Ethereum Development Docs",
      "url": "https://ethereum.org/en/developers/docs/",
      "description": "Ethereum developer docs"
    }
  ]
}
---

# SOLIDITY-05-EVENTS: Events and Logging

## Introduction

Emit events for off-chain listeners. By the end of this lesson you will be able to: Declare events; Emit events on state change; Index event parameters; Query logs from clients.

## Key Concepts

### 1. Declare events

Target: Declare events. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```solidity
event Transfer(address indexed from, address indexed to, uint256 value);

function transfer(address to, uint256 value) public {
    emit Transfer(msg.sender, to, value);
}
```
### 2. Emit events on state change

Target: Emit events on state change. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```solidity
event PriceSet(uint256 price);

function setPrice(uint256 p) public {
    price = p;
    emit PriceSet(p);
}
```
### 3. Index event parameters

Target: Index event parameters. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```solidity
event Log(string message);

function logIt() public {
    emit Log("action performed");
}
```
### 4. Query logs from clients

Target: Query logs from clients. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```solidity
event Deposit(address indexed who, uint256 amount);

receive() external payable {
    emit Deposit(msg.sender, msg.value);
}
```

## Practice Questions

1. What is the key idea behind "Events and Logging"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Events and Logging with analogies and real-world examples"
1. "Show me common mistakes beginners make with Events and Logging"
1. "Provide advanced patterns and performance considerations for Events and Logging"

## Key Takeaways

- Master the core ideas of Events and Logging through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
