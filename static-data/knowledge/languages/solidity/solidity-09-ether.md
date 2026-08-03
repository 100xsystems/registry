---
{
  "title": "Ether and Payable Functions",
  "description": "Send, receive, and track ether.",
  "type": "lesson",
  "order": 9,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Send ether with transfer/send/call",
    "Receive ether with receive()",
    "Track balances",
    "Handle refunds safely"
  ],
  "knowledge_refs": [
    "solidity/solidity-09-ether"
  ],
  "prerequisites": [
    "Solidity-08: Constructors and Inheritance"
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

# SOLIDITY-09-ETHER: Ether and Payable Functions

## Introduction

Send, receive, and track ether. By the end of this lesson you will be able to: Send ether with transfer/send/call; Receive ether with receive(); Track balances; Handle refunds safely.

## Key Concepts

### 1. Send ether with transfer/send/call

Target: Send ether with transfer/send/call. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```solidity
function pay() public payable {}

function balance() public view returns (uint) {
    return address(this).balance;
}
```
### 2. Receive ether with receive()

Target: Receive ether with receive(). Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```solidity
receive() external payable {}
fallback() external payable {}
```
### 3. Track balances

Target: Track balances. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```solidity
(bool ok, ) = to.call{value: amount}("");
require(ok, "send failed");
```
### 4. Handle refunds safely

Target: Handle refunds safely. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```solidity
function withdrawAll() public onlyOwner {
    (bool ok, ) = payable(owner).call{value: address(this).balance}("");
    require(ok, "withdraw failed");
}
```

## Practice Questions

1. What is the key idea behind "Ether and Payable Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Ether and Payable Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Ether and Payable Functions"
1. "Provide advanced patterns and performance considerations for Ether and Payable Functions"

## Key Takeaways

- Master the core ideas of Ether and Payable Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
