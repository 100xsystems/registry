---
{
  "title": "Security: Reentrancy",
  "description": "Reentrancy attacks and checks-effects-interactions.",
  "type": "lesson",
  "order": 13,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand reentrancy attacks",
    "Apply checks-effects-interactions",
    "Use reentrancy guards",
    "Audit withdrawal functions"
  ],
  "knowledge_refs": [
    "solidity/solidity-13-security"
  ],
  "prerequisites": [
    "Solidity-12: DeFi and DEX Patterns"
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

# SOLIDITY-13-SECURITY: Security: Reentrancy

## Introduction

Reentrancy attacks and checks-effects-interactions. By the end of this lesson you will be able to: Understand reentrancy attacks; Apply checks-effects-interactions; Use reentrancy guards; Audit withdrawal functions.

## Key Concepts

### 1. Understand reentrancy attacks

Target: Understand reentrancy attacks. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```solidity
// VULNERABLE: external call before state update
function withdraw(uint amount) public {
    require(balances[msg.sender] >= amount, "insufficient");
    (bool ok, ) = msg.sender.call{value: amount}("");
    require(ok);
    balances[msg.sender] -= amount;   // too late
}
```
### 2. Apply checks-effects-interactions

Target: Apply checks-effects-interactions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```solidity
// SAFE: state first, then call
function withdraw(uint amount) public {
    require(balances[msg.sender] >= amount, "insufficient");
    balances[msg.sender] -= amount;
    (bool ok, ) = msg.sender.call{value: amount}("");
    require(ok);
}
```
### 3. Use reentrancy guards

Target: Use reentrancy guards. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```solidity
bool private locked;
modifier noReentrant() {
    require(!locked, "reentrant");
    locked = true;
    _;
    locked = false;
}
```
### 4. Audit withdrawal functions

Target: Audit withdrawal functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```solidity
function withdraw(uint amount) public noReentrant {
    require(balances[msg.sender] >= amount);
    balances[msg.sender] -= amount;
    (bool ok, ) = msg.sender.call{value: amount}("");
    require(ok);
}
```

## Practice Questions

1. What is the key idea behind "Security: Reentrancy"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Security: Reentrancy with analogies and real-world examples"
1. "Show me common mistakes beginners make with Security: Reentrancy"
1. "Provide advanced patterns and performance considerations for Security: Reentrancy"

## Key Takeaways

- Master the core ideas of Security: Reentrancy through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
