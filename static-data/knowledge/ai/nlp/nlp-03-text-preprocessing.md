---
slug: nlp-03-text-preprocessing
title: "Text Preprocessing"
description: "Cleaning and normalizing raw text — tokenization, stemming, lemmatization, and Unicode handling."
order: 3
tags:
  - nlp
  - preprocessing
  - tokenization
  - stemming
  - lemmatization
prerequisites:
  - nlp-01-what-is-nlp
  - nlp-02-text-representation
references:
  - title: "NLTK Book: Processing Raw Text"
    url: "https://www.nltk.org/book/ch03.html"
    description: "Definitive chapter on raw text processing"
  - title: "Text Preprocessing in NLP (GeeksforGeeks)"
    url: "https://www.geeksforgeeks.org/nlp/text-preprocessing-for-nlp-tasks/"
    description: "Comprehensive preprocessing guide with code"
  - title: "Text Normalization Guide (Michael Brenndoerfer)"
    url: "https://mbrenndoerfer.com/writing/text-normalization-unicode-nlp"
    description: "Deep dive into Unicode normalization forms"
  - title: "spaCy Tokenization"
    url: "https://spacy.io/usage/linguistic-features#tokenization"
    description: "spaCy's linguistic tokenization documentation"
  - title: "Hugging Face Tokenizers"
    url: "https://huggingface.co/docs/tokenizers/"
    description: "Modern tokenization for transformers"
knowledge_refs:
  - nlp-01-what-is-nlp
  - nlp-04-regular-expressions
  - nlp-02-text-representation
---

# Text Preprocessing

Raw text from the real world is messy — inconsistent formatting, HTML tags, misspellings, and encoding issues. Preprocessing cleans and normalizes text for downstream NLP tasks.

## The Preprocessing Pipeline

```
Raw Text → Unicode Normalization → Lowercasing → Tokenization
→ Stop Word Removal → Stemming/Lemmatization → Clean Text
```

## Unicode Normalization

Resolve encoding inconsistencies:
```python
import unicodedata

text = "café"  # Could be "cafe\u0301" or "caf\u00e9"

# NFC: Compose (recommended for storage)
normalized = unicodedata.normalize('NFC', text)

# NFD: Decompose (useful for accent stripping)
decomposed = unicodedata.normalize('NFD', text)
```

## Lowercasing

Reduces vocabulary size:
```python
text = "Hello World NLP"
clean = text.lower()  # "hello world nlp"
```

**Caveat**: Don't lowercase when capitalization matters (NER, sentiment).

## Tokenization

Split text into meaningful units:

### Word Tokenization
```python
import nltk
nltk.download('punkt')

# NLTK
tokens = nltk.word_tokenize("Don't you love NLP?")
# ["Do", "n't", "you", "love", "NLP", "?"]

# spaCy
import spacy
nlp = spacy.load("en_core_web_sm")
tokens = [token.text for token in nlp("Don't you love NLP?")]
```

### Sentence Tokenization
```python
from nltk.tokenize import sent_tokenize

sentences = sent_tokenize("First sentence. Second sentence.")
# ["First sentence.", "Second sentence."]
```

### Subword Tokenization (for modern NLP)
```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
tokens = tokenizer.tokenize("tokenization is important")
# ['token', '##ization', 'is', 'important']
```

## Stop Word Removal

Remove common words that carry little meaning:
```python
from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
tokens = ["I", "love", "NLP", "it", "is", "great"]
filtered = [t for t in tokens if t.lower() not in stop_words]
# ["love", "NLP", "great"]
```

**When NOT to remove stop words**: Sentiment analysis (negation matters), text generation.

## Stemming

Rule-based suffix removal (may produce non-words):
```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
print(stemmer.stem("running"))   # "run"
print(stemmer.stem("better"))    # "better" (not "good")
print(stemmer.stem("studies"))   # "studi"
```

## Lemmatization

Dictionary-based reduction (always produces real words):
```python
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("running", pos='v'))  # "run"
print(lemmatizer.lemmatize("better", pos='a'))    # "good"
print(lemmatizer.lemmatize("studies", pos='n'))   # "study"
```

### Stemming vs. Lemmatization

| Aspect | Stemming | Lemmatization |
|---|---|---|
| Method | Rule-based suffix removal | Dictionary lookup |
| Speed | Faster | Slower |
| Output | May be non-words | Always real words |
| Example | "studies" → "studi" | "studies" → "study" |

## Complete Preprocessing Pipeline

```python
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

def preprocess(text):
    # 1. Lowercase
    text = text.lower()
    
    # 2. Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # 3. Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    
    # 4. Remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # 5. Tokenize
    tokens = nltk.word_tokenize(text)
    
    # 6. Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [t for t in tokens if t not in stop_words]
    
    # 7. Lemmatize
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    
    return ' '.join(tokens)
```

## Practical Tips

1. **Don't over-clean**: Keep negation words for sentiment
2. **Choose lemmatization** over stemming when accuracy matters
3. **Use spaCy** for production preprocessing
4. **Subword tokenization** for transformer models
5. **Preserve original** for debugging and analysis

## Further Reading

- NLTK Book Chapter 3 is the definitive preprocessing reference
- GeeksforGeeks guide covers all techniques with code
- Unicode normalization is essential for multilingual NLP
- For modern NLP: preprocessing is often handled by the tokenizer
