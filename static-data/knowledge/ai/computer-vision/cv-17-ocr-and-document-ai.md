---
slug: cv-17-ocr-and-document-ai
title: "OCR & Document AI"
description: "Reading text from images and documents — from Tesseract to modern OCR models."
order: 17
tags:
  - computer-vision
  - ocr
  - document-ai
  - text-detection
  - text-recognition
prerequisites:
  - cv-06-cnns-for-vision
  - cv-12-opencv-fundamentals
  - dl-17-transformers
references:
  - title: "Tesseract OCR Documentation"
    url: "https://tesseract-ocr.github.io/"
    description: "Official Tesseract OCR documentation"
  - title: "CRNN: An End-to-End Trainable Neural OCR System"
    url: "https://arxiv.org/abs/1507.05717"
    description: "Shi et al.'s CRNN paper for scene text recognition"
  - title: "EAST: An Efficient and Accurate Scene Text Detector"
    url: "https://arxiv.org/abs/1704.03155"
    description: "Zhou et al.'s EAST paper for fast text detection"
  - title: "TrOCR: Transformer-Based OCR"
    url: "https://arxiv.org/abs/2109.10282"
    description: "Microsoft's TrOCR using transformers for OCR"
  - title: "EasyOCR Documentation"
    url: "https://www.jaided.ai/easyocr/"
    description: "EasyOCR — simple, multi-language OCR library"
knowledge_refs:
  - cv-06-cnns-for-vision
  - cv-12-opencv-fundamentals
  - dl-17-transformers
---

# OCR & Document AI

Optical Character Recognition (OCR) converts text from images into machine-readable text. Modern OCR combines text detection (finding where text is) with text recognition (reading what it says).

## OCR Pipeline

```
Input Image
    ↓
[Text Detection] → Find text regions/bounding boxes
    ↓
[Text Recognition] → Read text within each region
    ↓
Output: Text with bounding boxes and confidence scores
```

## Tesseract OCR (Classical)

Most widely-used open-source OCR engine:
```python
import pytesseract

# Simple OCR
text = pytesseract.image_to_string(image)

# With bounding boxes
data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
for i, text in enumerate(data['text']):
    if text.strip():
        x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
        print(f"Text: '{text}' at ({x}, {y})")
```

## Deep Learning OCR

### CRNN (Convolutional Recurrent Neural Network)
- CNN extracts visual features
- RNN (LSTM) models sequential text
- CTC loss for alignment

### EAST (Efficient and Accurate Scene Text Detector)
Fast text detection in natural scenes:
```python
# OpenCV's DNN module with EAST
net = cv2.dnn.readNet("frozen_east_text_detection.pb")
blob = cv2.dnn.blobFromImage(image, 1.0, (320, 320))
net.setInput(blob)
output = net.forward(["feature_fusion/Conv_7/Sigmoid", "feature_fusion/concat_3"])
```

### TrOCR (Transformer OCR)
Uses Vision Transformer encoder + text decoder:
```python
from transformers import TrOCRProcessor, VisionEncoderDecoderModel

processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-printed")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-printed")

pixel_values = processor(images=image, return_tensors="pt").pixel_values
generated_ids = model.generate(pixel_values)
text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
```

## Document AI

### Layout Analysis
Understanding document structure (headings, paragraphs, tables):
- **LayoutLM**: BERT-like model for document understanding
- **DiT**: Document Image Transformer
- **Donut**: OCR-free document understanding

### Table Extraction
Extract structured data from tables in documents:
```python
# Using table-transformer
from table_transformer import TableTransformer

model = TableTransformer.from_pretrained("microsoft/table-transformer-detection")
# Detect and parse table structure
```

## EasyOCR (Practical)

Multi-language, easy-to-use:
```python
import easyocr

reader = easyocr.Reader(['en', 'hi'])  # English + Hindi
results = reader.readtext("image.jpg")

for (bbox, text, confidence) in results:
    print(f"Text: '{text}', Confidence: {confidence:.2f}")
```

## Use Cases

| Application | Technology |
|---|---|
| **Document digitization** | Tesseract, TrOCR |
| **License plate reading** | EAST + CRNN |
| **Receipt scanning** | Document AI |
| **Handwriting recognition** | IAM dataset models |
| **Passport reading** | MRZ detection |
| **Invoice processing** | LayoutLM + OCR |

## Practical Tips

1. **Use Tesseract** for printed documents (simple, fast)
2. **Use EasyOCR** for multi-language scene text
3. **Preprocess images**: Binarize, deskew before OCR
4. **Language matters**: Specify language for better accuracy
5. **Confidence thresholding**: Filter low-confidence detections

## Further Reading

- Tesseract is the standard for document OCR
- CRNN established the end-to-end text recognition paradigm
- TrOCR showed transformers work well for OCR
- LayoutLM bridged NLP and document understanding
