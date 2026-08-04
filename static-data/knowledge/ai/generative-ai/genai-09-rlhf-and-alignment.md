---
slug: genai-09-rlhf-and-alignment
title: "RLHF & Alignment"
description: "How we teach AI to be helpful, harmless, and honest — from human feedback to constitutional AI."
order: 9
tags:
  - generative-ai
  - rlhf
  - alignment
  - ppo
  - dpo
  - constitutional-ai
prerequisites:
  - genai-08-fine-tuning-llms
  - genai-06-llm-architecture
  - dl-07-optimizers
references:
  - title: "Training Language Models to Follow Instructions with Human Feedback (InstructGPT)"
    url: "https://arxiv.org/abs/2203.02155"
    description: "Ouyang et al.'s foundational RLHF paper from OpenAI"
  - title: "Direct Preference Optimization (DPO)"
    url: "https://arxiv.org/abs/2305.18290"
    description: "Rafailov et al.'s DPO paper — simpler alternative to PPO-based RLHF"
  - title: "Constitutional AI: Harmlessness from AI Feedback"
    url: "https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback"
    description: "Anthropic's Constitutional AI paper"
  - title: "Illustrating RLHF (Hugging Face)"
    url: "https://huggingface.co/blog/rlhf"
    description: "Hugging Face's visual guide to the RLHF pipeline"
  - title: "Claude's Constitution"
    url: "https://www.anthropic.com/news/claudes-constitution"
    description: "Anthropic's transparency about Claude's behavioral guidelines"
knowledge_refs:
  - genai-08-fine-tuning-llms
  - genai-06-llm-architecture
  - dl-07-optimizers
---

# RLHF & Alignment

A pretrained LLM predicts the next token — but that doesn't make it helpful, harmless, or honest. Alignment techniques like RLHF bridge this gap by training models to follow human preferences.

## The Alignment Problem

Base models are trained to predict text, not to be good assistants:
- They may generate harmful content
- They may be sycophantic (always agreeing)
- They may fabricate information confidently
- They may follow malicious instructions

**Alignment** = making the model's behavior match human values and intentions.

## The RLHF Pipeline

### Step 1: Supervised Fine-Tuning (SFT)
Train on high-quality instruction-response pairs:
```
Human: What is the capital of France?
Assistant: The capital of France is Paris. It has been the capital since 
the 10th century and is the country's largest city.
```

### Step 2: Reward Modeling
Create preference data by having humans rank model outputs:
```
Prompt: "Explain quantum computing"

Response A: "Quantum computing uses qubits..." (rank: 3rd)
Response B: "Quantum computing harnesses quantum mechanics..." (rank: 1st)  
Response C: "It's like regular computing but quantum..." (rank: 2nd)
```

Train a reward model to predict human preferences:
$$\mathcal{L}_{\text{RM}} = -\log(\sigma(r_\theta(x, y_w) - r_\theta(x, y_l)))$$

where $y_w$ is the preferred response and $y_l$ is the less preferred.

### Step 3: Policy Optimization (PPO)
Use reinforcement learning to optimize the model against the reward model:

$$\text{Reward} = r_\theta(x, y) - \beta D_{\text{KL}}(\pi_\theta \| \pi_{\text{ref}})$$

The KL penalty prevents the model from straying too far from the SFT model (avoiding reward hacking).

**PPO** is the standard RL algorithm, but it's complex:
- Requires 4 models in memory: policy, reference, reward, value critic
- Training is unstable and hard to tune
- Expensive (4x memory of standard training)

## Direct Preference Optimization (DPO)

DPO (Rafailov et al., 2023) simplifies RLHF by eliminating the reward model:

$$\mathcal{L}_{\text{DPO}} = -\log(\sigma(\beta \log\frac{\pi_\theta(y_w|x)}{\pi_{\text{ref}}(y_w|x)} - \beta \log\frac{\pi_\theta(y_l|x)}{\pi_{\text{ref}}(y_l|x)}))$$

**Key insight**: The optimal policy can be derived directly from preferences without an explicit reward model.

```python
from trl import DPOTrainer

dpo_trainer = DPOTrainer(
    model=model,
    ref_model=ref_model,
    tokenizer=tokenizer,
    train_dataset=preference_dataset,
    beta=0.1,
    max_length=512,
    max_prompt_length=256,
)
dpo_trainer.train()
```

**Benefits over PPO:**
- Only 2 models (policy + reference) instead of 4
- No reward model training needed
- More stable training
- Simpler implementation

## Constitutional AI (Anthropic)

Instead of human feedback, use **AI feedback** based on written principles:

### Phase 1: Self-Critique and Revision
```
Constitution principle: "Choose the response that is least likely to 
be considered harmful or unethical."

Model generates → Model critiques itself → Model revises → 
Fine-tune on revised responses
```

### Phase 2: RLAIF (RL from AI Feedback)
- Generate preference pairs using AI judgment
- Train reward model on AI preferences
- Optimize with standard RL

**Constitution examples:**
- "Please choose the assistant response that is as harmless and ethical as possible"
- "Which response is most helpful while being safe?"
- "Select the response that best follows the Universal Declaration of Human Rights"

## Other Alignment Methods

### RLAIF
Same as RLHF but with AI-generated preferences:
- Scalable (no human annotation needed)
- Can use a stronger model to train a weaker one
- Less expensive but potentially less aligned with actual human values

### KTO (Kahneman-Tversky Optimization)
Uses binary feedback (thumbs up/down) instead of ranked preferences:
- Simpler data collection
- More realistic (humans give binary feedback, not rankings)

### ORPO (Odds Ratio Preference Optimization)
Combines SFT and preference optimization in one step:
- No reference model needed
- Single training pass
- Competitive with DPO

## Reward Hacking

Models can exploit flaws in the reward model:
- **Length hacking**: Longer responses get higher rewards → model becomes verbose
- **Sycophancy**: Always agreeing with the user → never challenges incorrect beliefs
- **Style over substance**: Formal language scores higher than correct information

**Mitigation**: KL penalty, diverse reward models, adversarial testing.

## Practical Alignment

```python
# Complete alignment pipeline
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import SFTTrainer, DPOTrainer, RewardTrainer

# 1. SFT
sft_model = SFTTrainer(model, train_dataset=instruction_data)

# 2. Reward Model
reward_model = RewardTrainer(model, train_dataset=preference_data)

# 3. DPO (simpler than PPO)
dpo_trainer = DPOTrainer(
    model=sft_model,
    ref_model=base_model,
    train_dataset=preference_data,
)
```

## Further Reading

- InstructGPT paper is the foundational RLHF reference
- DPO paper simplified the entire alignment pipeline
- Constitutional AI showed AI feedback can scale alignment
- Hugging Face's RLHF blog is the best visual introduction
