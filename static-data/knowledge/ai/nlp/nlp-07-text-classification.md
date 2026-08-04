---
slug: nlp-07-text-classification
title: "Text Classification"
description: "Assigning categories to text — from naive Bayes to transformers, the full spectrum of text classification."
order: 7
tags:
  - nlp
  - classification
  - naive-bayes
  - svm
  - transformers
prerequisites:
  - nlp-06-word-embeddings
  - nlp-02-text-representation
  - ml-13-naive-bayes
references:
  - title: "Hugging Face: Text Classification"
    url: "https://huggingface.co/docs/transformers/tasks/sequence_classification"
    description: "Official guide to fine-tuning transformers for classification"
  - title: "scikit-learn: Naive Bayes"
    url: "https://scikit-learn.org/stable/modules/naive_bayes.html"
    description: "Comprehensive Naive Bayes documentation"
  - title: "Scikit-Learn: Working With Text Data"
    url: "https://scikit-learn.org/1.4/tutorial/text_analytics/working_with_text_data.html"
    description: "Practical text classification tutorial"
  - title: "Text Classification with CNNs and LSTMs"
    url: "https://hannibunny.github.io/mlbook/text/02TextClassification.html"
    description: "Deep learning text classification walkthrough"
  - title: "Keras: Text Classification with Transformer"
    url: "https://keras.io/examples/nlp/text_classification_with_transformer/"
    description: "Building a transformer classifier from scratch"
knowledge_refs:
  - nlp-06-word-embeddings
  - ml-13-naive-bayes
  - dl-17-transformers
---

# Text Classification

Text classification assigns categories to text — spam detection, sentiment analysis, topic categorization, and intent recognition are all text classification tasks.

## The Classification Pipeline

```
Raw Text → Preprocessing → Feature Extraction → Model → Label
```

## Classical Approaches

### Naive Bayes
Fast, interpretable baseline:
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=10000)),
    ('clf', MultinomialNB())
])
pipeline.fit(train_texts, train_labels)
predictions = pipeline.predict(test_texts)
```

### SVM (Support Vector Machine)
Often the best classical approach:
```python
from sklearn.svm import LinearSVC

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1, 2))),
    ('clf', LinearSVC(C=1.0))
])
```

## Deep Learning Approaches

### CNN for Text (Kim, 2014)
1D convolutions capture local n-gram patterns:
```python
class TextCNN(nn.Module):
    def __init__(self, vocab_size, embed_dim, num_classes):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.conv1 = nn.Conv1d(embed_dim, 100, kernel_size=3)
        self.conv2 = nn.Conv1d(embed_dim, 100, kernel_size=4)
        self.conv3 = nn.Conv1d(embed_dim, 100, kernel_size=5)
        self.fc = nn.Linear(300, num_classes)
    
    def forward(self, x):
        embeds = self.embedding(x).transpose(1, 2)
        c1 = F.relu(self.conv1(embeds)).max(dim=2)[0]
        c2 = F.relu(self.conv2(embeds)).max(dim=2)[0]
        c3 = F.relu(self.conv3(embeds)).max(dim=2)[0]
        return self.fc(torch.cat([c1, c2, c3], dim=1))
```

### LSTM for Text
Captures sequential context:
```python
class TextLSTM(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, num_classes):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, bidirectional=True, batch_first=True)
        self.fc = nn.Linear(hidden_dim * 2, num_classes)
    
    def forward(self, x):
        embeds = self.embedding(x)
        output, (hidden, _) = self.lstm(embeds)
        hidden = torch.cat([hidden[-2], hidden[-1]], dim=1)
        return self.fc(hidden)
```

## Transformer-Based Classification (State-of-the-Art)

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

# Tokenize
inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")

# Forward pass
outputs = model(**inputs)
logits = outputs.logits
predictions = torch.argmax(logits, dim=-1)
```

### Fine-Tuning with Hugging Face Trainer
```python
from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=16,
    learning_rate=2e-5,
    evaluation_strategy="epoch",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
)
trainer.train()
```

## Model Comparison

| Model | Speed | Accuracy | Data Needed |
|---|---|---|---|
| Naive Bayes | Very fast | Good | Small |
| SVM | Fast | Very good | Small |
| CNN | Medium | Good | Medium |
| LSTM | Slow | Good | Medium |
| BERT | Slow | Excellent | Small-Medium |
| GPT | Very slow | Excellent | Minimal |

## Practical Tips

1. **Start with TF-IDF + SVM** as baseline
2. **Try simple models first** before deep learning
3. **Use pretrained transformers** when accuracy matters
4. **Data augmentation** helps with small datasets
5. **Cross-validate** for reliable estimates

## Further Reading

- Hugging Face's text classification guide is the modern standard
- scikit-learn's text analytics tutorial covers classical approaches
- Kim (2014) showed CNNs work well for text classification
- For production: distilbert is fast and accurate
