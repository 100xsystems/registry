---
{
  "title": "Constructors and Inheritance",
  "description": "Initialize contracts and build hierarchies.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write constructors",
    "Pass initial parameters",
    "Inherit contracts",
    "Call parent constructors"
  ],
  "knowledge_refs": [
    "solidity/solidity-08-constructor"
  ],
  "prerequisites": [
    "Solidity-07: Mappings and Structs"
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

# SOLIDITY-08-CONSTRUCTOR: Constructors and Inheritance

## Introduction

Initialize contracts and build hierarchies. By the end of this lesson you will be able to: Write constructors; Pass initial parameters; Inherit contracts; Call parent constructors.

## Key Concepts

### 1. Write constructors

Target: Write constructors. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```solidity
contract Token {
    string public name;

    constructor(string memory _name) {
        name = _name;
    }
}
```
### 2. Pass initial parameters

Target: Pass initial parameters. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```solidity
contract Child is Parent {
    constructor() Parent("arg") {}
}
```
### 3. Inherit contracts

Target: Inherit contracts. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```solidity
contract A { function f() public pure virtual returns (string memory) { return "A"; } }
contract B is A { function f() public pure override returns (string memory) { return "B"; } }
```
### 4. Call parent constructors

Target: Call parent constructors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```solidity
abstract contract Base {
    function doWork() public virtual;
}

contract Impl is Base {
    function doWork() public override {}
}
```

## Practice Questions

1. What is the key idea behind "Constructors and Inheritance"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Constructors and Inheritance with analogies and real-world examples"
1. "Show me common mistakes beginners make with Constructors and Inheritance"
1. "Provide advanced patterns and performance considerations for Constructors and Inheritance"

## Key Takeaways

- Master the core ideas of Constructors and Inheritance through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
