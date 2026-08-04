{
  "title": "Types of Learning",
  "description": "Understand supervised, unsupervised, semi-supervised, reinforcement, and self-supervised learning — when to use each and how they differ.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Distinguish between supervised, unsupervised, and reinforcement learning",
    "Explain semi-supervised and self-supervised learning and their practical value",
    "Identify which paradigm fits a given real-world problem",
    "Understand contrastive learning and its role in modern representation learning"
  ],
  "knowledge_refs": [
    "machine-learning/ml-01-what-is-machine-learning",
    "machine-learning/ml-03-the-learning-problem",
    "deep-learning/dl-01-what-is-deep-learning"
  ],
  "prerequisites": ["ML-01: What Is Machine Learning?"],
  "references": [
    {
      "title": "MIT 6.390 — Introduction to Machine Learning",
      "url": "https://introml.mit.edu/notes/",
      "description": "MIT's modern ML course covering all learning paradigms with mathematical rigor and practical exercises."
    },
    {
      "title": "Self-Supervised Learning and Computer Vision — fast.ai",
      "url": "https://www.fast.ai/posts/2020-01-13-self_supervised.html",
      "description": "Excellent overview of self-supervised and contrastive learning with practical PyTorch examples."
    },
    {
      "title": "A Brief Survey of Machine Learning — Wikipedia",
      "url": "https://en.wikipedia.org/wiki/Machine_learning",
      "description": "Comprehensive taxonomy of ML paradigms with links to authoritative sources for each type."
    },
    {
      "title": "Machine Learning Mastery — Types of Machine Learning Algorithms",
      "url": "https://machinelearningmastery.com/types-of-machine-learning-algorithms/",
      "description": "Practical guide to ML algorithm families organized by learning paradigm."
    },
    {
      "title": "Stanford CS229 — Unsupervised Learning",
      "url": "https://cs229.stanford.edu/summer2019/cs229-notes.pdf",
      "description": "Andrew Ng's notes on unsupervised learning covering clustering, EM, and PCA."
    }
  ]
}
---

Machine learning isn't one technique — it's a family of approaches that differ fundamentally in how they learn from data. Understanding these differences is the first step to choosing the right tool for your problem.

---

## Supervised Learning: Learning with Labels

The most common and well-understood paradigm. You provide the algorithm with **labeled examples** — pairs of inputs and desired outputs — and it learns a mapping function.

### How It Works

Given a dataset of input-output pairs `(x₁, y₁), (x₂, y₂), ..., (xₙ, yₙ)`, supervised learning finds a function `f(x) ≈ y` that generalizes to new, unseen inputs.

### Two Flavors

**Classification** predicts discrete categories:
- Email → spam or not spam
- Image → cat, dog, or bird
- Medical scan → malignant or benign

**Regression** predicts continuous values:
- House features → price
- Weather data → temperature tomorrow
- Stock history → future price

### Real-World Applications

Spam filters, voice assistants, medical diagnosis, fraud detection, recommendation engines — the majority of deployed ML systems use supervised learning. It's the workhorse of the industry because labeled data, while expensive to collect, provides clear optimization targets.

### Limitations

Supervised learning requires labeled data. Labeling is expensive, time-consuming, and sometimes impossible (how do you label "artistic quality"?). This creates a bottleneck that other paradigms address.

---

## Unsupervised Learning: Finding Hidden Structure

No labels. The algorithm discovers patterns, groupings, or structure in data without any guidance about what to look for.

### Core Tasks

**Clustering** groups similar data points:
- Customer segmentation (group shoppers by behavior)
- Document topic discovery
- Gene expression analysis

**Dimensionality reduction** compresses data while preserving structure:
- PCA for visualization of high-dimensional data
- Autoencoders for feature learning
- t-SNE and UMAP for embedding visualization

**Anomaly detection** finds unusual patterns:
- Network intrusion detection
- Manufacturing defect detection
- Financial fraud identification

### Why It Matters

Most data in the world is unlabeled. Unsupervised learning lets you extract value from this data — discovering customer segments, finding structural patterns in social networks, or identifying the fundamental components of complex signals.

### The Challenge

Without labels, there's no clear "right answer." How do you evaluate a clustering algorithm? The quality of unsupervised results often depends on domain expertise and post-hoc interpretation.

---

## Reinforcement Learning: Learning from Consequences

An **agent** learns to make decisions by interacting with an **environment**. It takes **actions**, receives **rewards** (or penalties), and adjusts its **policy** (strategy) to maximize cumulative reward over time.

### Key Components

- **State**: What the agent observes about the environment
- **Action**: What the agent can do
- **Reward**: Scalar signal after each action
- **Policy**: The agent's strategy — mapping states to actions
- **Value function**: Expected cumulative reward from a state

### Why RL Is Different

Unlike supervised learning, RL doesn't need labeled examples. It learns through trial and error, which is how humans and animals learn many skills. The challenge is that the agent must balance **exploration** (trying new actions) with **exploitation** (using known good actions).

### Applications

Game playing (AlphaGo, OpenAI Five), robotics (learning to walk, grasp objects), autonomous driving, recommendation systems (balancing user engagement with long-term satisfaction), and resource management.

### The Credit Assignment Problem

One of RL's hardest challenges: when you receive a reward at the end of a long sequence of actions, which actions were responsible? This is like playing chess and only learning whether you won or lost 50 moves later.

---

## Semi-Supervised Learning: Best of Both Worlds

A small amount of labeled data combined with a large pool of unlabeled data. The unlabeled data helps the model learn the underlying data structure, while the labels provide supervision.

### When It's Valuable

Labeling data is expensive — medical imaging requires expert radiologists, legal document review requires lawyers. Semi-supervised learning lets you get 80% of the performance of fully supervised learning with 10% of the labeled data.

### How It Works

The key insight is **consistency regularization**: if you add small perturbations to an unlabeled input, the model's prediction shouldn't change much. This forces the model to learn smooth decision boundaries that respect the data's natural structure.

### Real-World Example

Google's speech recognition uses semi-supervised learning. They have millions of hours of unlabeled audio but only thousands of hours transcribed. The unlabeled audio teaches the model about speech patterns; the labeled data teaches it to map sounds to words.

---

## Self-Supervised Learning: The Labels Come from the Data

A breakthrough paradigm where the model generates its own supervisory signals from the structure of unlabeled data. This has driven most of the recent AI advances.

### Pretext Tasks

The model solves a "pretext task" designed to force it to learn useful representations:

- **Next word prediction** (GPT): Given "The cat sat on the ___", predict "mat"
- **Image inpainting**: Given an image with a missing patch, predict what goes there
- **Contrastive learning**: Given two views of the same image, bring their representations close together
- **Colorization**: Given a grayscale image, predict the colors

### Why It's Revolutionary

Self-supervised learning has eliminated the labeling bottleneck for language and vision. GPT, BERT, and their successors learn from trillions of tokens of raw text. CLIP learns from billions of image-text pairs. The representations learned through self-supervision often exceed what supervised learning achieves.

### The Pretrain-Finetune Paradigm

1. **Pretrain** a large model on massive unlabeled data using self-supervision
2. **Fine-tune** it on your specific task with a small labeled dataset

This is how most modern NLP and vision systems work. You don't train from scratch — you start with a pretrained foundation model.

---

## Contrastive Learning: Learning by Comparison

A specialized form of self-supervised learning that learns representations by comparing positive pairs (similar items) against negative pairs (dissimilar items).

### The Core Idea

If you show the model two different crops of the same cat photo (positive pair) and a photo of a dog (negative pair), the model learns to bring the cat representations close together while pushing the dog representation away.

### Why It Works

Contrastive learning forces the model to capture semantic similarity rather than superficial features. This leads to representations that transfer well to downstream tasks like image classification, object detection, and visual search.

### Applications

- **CLIP**: Maps images and text into a shared space for zero-shot classification
- **SimCLR/MoCo**: Self-supervised visual representations that rival supervised training
- **Sentence-BERT**: Contrastive learning for semantic text similarity

---

## Choosing the Right Paradigm

| Scenario | Best Paradigm |
|----------|---------------|
| Labeled data available, prediction needed | Supervised learning |
| No labels, want to find groups/patterns | Unsupervised learning |
| Sequential decisions, trial and error | Reinforcement learning |
| Few labels, lots of unlabeled data | Semi-supervised learning |
| Massive unlabeled data, specific task | Self-supervised + fine-tuning |
| Need good representations for multiple tasks | Contrastive/pretraining |

The boundaries between these paradigms are blurring. Modern systems often combine approaches: a self-supervised model pretrained on unlabeled data, fine-tuned with supervised learning, and deployed with reinforcement learning from human feedback (RLHF).

---

## Key Takeaways

- **Supervised**: Labeled data, clear optimization target, most common in industry
- **Unsupervised**: No labels, discovers structure, essential for unlabeled data
- **Reinforcement**: Trial and error, learns policies through rewards
- **Semi-supervised**: Small labeled + large unlabeled dataset
- **Self-supervised**: Labels come from data structure (pretext tasks), drives modern AI
- **Contrastive**: Learns by comparing positive vs. negative pairs, produces transferable representations

---

## References

1. **MIT 6.390 — Introduction to Machine Learning** — MIT Open Learning. Comprehensive course covering all learning paradigms. https://introml.mit.edu/notes/
2. **Self-Supervised Learning and Computer Vision** — fast.ai. Practical guide to modern self-supervised methods. https://www.fast.ai/posts/2020-01-13-self_supervised.html
3. **Machine Learning Overview** — Wikipedia. Comprehensive taxonomy of ML paradigms. https://en.wikipedia.org/wiki/Machine_learning
4. **Types of Machine Learning Algorithms** — Machine Learning Mastery. Practical guide organized by paradigm. https://machinelearningmastery.com/types-of-machine-learning-algorithms/
5. **CS229 Notes** — Andrew Ng, Stanford. Mathematical foundations of supervised and unsupervised learning. https://cs229.stanford.edu/summer2019/cs229-notes.pdf

---

## Footnotes

The taxonomy presented here follows the framework established in Bishop's *Pattern Recognition and Machine Learning* (2006) and updated by recent advances in self-supervised learning (LeCun, 2020, "A Path Towards Autonomous Machine Intelligence"). The contrastive learning section draws on SimCLR (Chen et al., 2020) and CLIP (Radford et al., 2021).
