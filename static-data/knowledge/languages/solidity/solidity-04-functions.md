---
{
  "title": "Functions and Modifiers",
  "description": "Visibility, view/pure, and custom modifiers.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Set function visibility",
    "Use view and pure",
    "Write custom modifiers",
    "Understand function overloading"
  ],
  "knowledge_refs": [
    "solidity/solidity-04-functions"
  ],
  "prerequisites": [
    "Solidity-03: State Variables and Storage"
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

# SOLIDITY-04-FUNCTIONS: Functions and Modifiers

## Introduction

Visibility, view/pure, and custom modifiers. By the end of this lesson you will be able to: Set function visibility; Use view and pure; Write custom modifiers; Understand function overloading.

## Key Concepts

### 1. Set function visibility

Target: Set function visibility. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```solidity
function add(uint a, uint b) public pure returns (uint) {
    return a + b;
}
```
### 2. Use view and pure

Target: Use view and pure. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```solidity
function getBalance() public view returns (uint) {
    return address(this).balance;
}
```
### 3. Write custom modifiers

Target: Write custom modifiers. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```solidity
modifier onlyOwner() {
    require(msg.sender == owner, "not owner");
    _;
}

function adminAction() public onlyOwner {}
```
### 4. Understand function overloading

Target: Understand function overloading. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```solidity
function over(uint a) public pure returns (uint) { return a; }
function over(uint a, uint b) public pure returns (uint) { return a + b; }
```

## Practice Questions

1. What is the key idea behind "Functions and Modifiers"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions and Modifiers with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions and Modifiers"
1. "Provide advanced patterns and performance considerations for Functions and Modifiers"

## Key Takeaways

- Master the core ideas of Functions and Modifiers through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
