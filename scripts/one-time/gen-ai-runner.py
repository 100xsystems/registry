#!/usr/bin/env python3
"""Generate complete 21-lesson AI courses for six domains.

Run from anywhere inside the registry repo:

    python3 scripts/one-time/gen-ai-runner.py

Creates static-data/knowledge/ai/<slug>/ with a hand-curated index.json
(resources + lesson metadata) and 21 lesson .md files for each domain:
data-science, machine-learning, deep-learning, computer-vision, nlp,
generative-ai.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gen_stub_lib import run_spec  # noqa: E402
from gen_ai_data_a import SPECS as SPECS_A  # noqa: E402
from gen_ai_data_b import SPECS as SPECS_B  # noqa: E402
from gen_ai_data_c import SPECS as SPECS_C  # noqa: E402

ALL_SPECS = SPECS_A + SPECS_B + SPECS_C

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'static-data', 'knowledge', 'ai',
)

# ── Hand-curated resources per hub ─────────────────────────────────────

HUB_RESOURCES: dict[str, dict] = {
    'data-science': {
        'name': 'Data Science',
        'description': 'From statistics and pandas to end-to-end projects — the complete foundation for turning raw data into decisions.',
        'categories': [
            {
                'label': 'Free Courses & Guides',
                'icon': 'book',
                'items': [
                    {'title': 'Kaggle Learn — Data Science', 'url': 'https://www.kaggle.com/learn', 'description': 'Hands-on micro-courses covering pandas, EDA and modeling.'},
                    {'title': 'Python for Data Analysis — Wes McKinney', 'url': 'https://wesmckinney.com/book/', 'description': 'The definitive guide to pandas and the PyData stack.'},
                    {'title': 'The Elements of Statistical Learning', 'url': 'https://hastie.su.domains/ElemStatLearn/', 'description': 'The classic statistical-learning reference (free PDF).'},
                ],
            },
            {
                'label': 'Official Documentation',
                'icon': 'docs',
                'items': [
                    {'title': 'Pandas User Guide', 'url': 'https://pandas.pydata.org/docs/user_guide/index.html', 'description': 'Official documentation for the pandas data-analysis library.'},
                    {'title': 'NumPy Documentation', 'url': 'https://numpy.org/doc/stable/', 'description': 'Reference for the array-computing foundation.'},
                    {'title': 'scikit-learn User Guide', 'url': 'https://scikit-learn.org/stable/user_guide.html', 'description': 'Authoritative guide to the Python machine-learning toolbox.'},
                ],
            },
        ],
    },
    'machine-learning': {
        'name': 'Machine Learning',
        'description': 'Supervised and unsupervised learning with scikit-learn: regression, trees, ensembles, SVMs, clustering and the math underneath.',
        'categories': [
            {
                'label': 'Free Courses & Guides',
                'icon': 'book',
                'items': [
                    {'title': 'scikit-learn User Guide', 'url': 'https://scikit-learn.org/stable/user_guide.html', 'description': 'The authoritative guide to the Python ML toolbox.'},
                    {'title': 'Hands-On Machine Learning — Géron', 'url': 'https://github.com/ageron/handson-ml3', 'description': 'Practical ML with scikit-learn, Keras and TensorFlow.'},
                    {'title': 'Andrew Ng — ML Specialization', 'url': 'https://www.coursera.org/specializations/machine-learning-introduction', 'description': 'The most popular introductory ML course in the world.'},
                ],
            },
            {
                'label': 'Official Documentation',
                'icon': 'docs',
                'items': [
                    {'title': 'The Elements of Statistical Learning', 'url': 'https://hastie.su.domains/ElemStatLearn/', 'description': 'The classic statistical-learning reference (free PDF).'},
                    {'title': 'Kaggle — Intro to Machine Learning', 'url': 'https://www.kaggle.com/learn/intro-to-machine-learning', 'description': 'Hands-on micro-course for the fundamentals.'},
                    {'title': 'XGBoost Documentation', 'url': 'https://xgboost.readthedocs.io/', 'description': 'Docs for the gradient-boosting workhorse.'},
                ],
            },
        ],
    },
    'deep-learning': {
        'name': 'Deep Learning',
        'description': 'Neural networks end to end: backprop, PyTorch, CNNs, RNNs, LSTMs and transformers — from perceptron to attention.',
        'categories': [
            {
                'label': 'Free Courses & Guides',
                'icon': 'book',
                'items': [
                    {'title': 'Dive into Deep Learning (d2l.ai)', 'url': 'https://d2l.ai/', 'description': 'Interactive deep-learning textbook with code in PyTorch.'},
                    {'title': 'Practical Deep Learning — fast.ai', 'url': 'https://course.fast.ai/', 'description': 'A top-down course that gets you training models quickly.'},
                    {'title': 'Deep Learning — Goodfellow et al.', 'url': 'https://www.deeplearningbook.org/', 'description': 'The canonical textbook on deep learning (free HTML).'},
                ],
            },
            {
                'label': 'Official Documentation',
                'icon': 'docs',
                'items': [
                    {'title': 'PyTorch Documentation', 'url': 'https://pytorch.org/docs/stable/index.html', 'description': 'The official reference for the deep-learning framework.'},
                    {'title': 'PyTorch Tutorials', 'url': 'https://pytorch.org/tutorials/', 'description': 'Step-by-step tutorials for tensors, autograd and models.'},
                    {'title': 'Attention Is All You Need', 'url': 'https://arxiv.org/abs/1706.03762', 'description': 'The paper that introduced the Transformer architecture.'},
                ],
            },
        ],
    },
    'computer-vision': {
        'name': 'Computer Vision',
        'description': 'From pixels to perception: image processing, CNNs, detection, segmentation, pose, tracking, OCR and vision transformers.',
        'categories': [
            {
                'label': 'Free Courses & Guides',
                'icon': 'book',
                'items': [
                    {'title': 'Stanford CS231n', 'url': 'http://cs231n.stanford.edu/', 'description': 'The classic university course on CNNs for visual recognition.'},
                    {'title': 'OpenCV-Python Tutorials', 'url': 'https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html', 'description': 'Practical image processing and computer vision with Python.'},
                    {'title': 'YOLOv8 (Ultralytics)', 'url': 'https://docs.ultralytics.com/', 'description': 'Real-time object detection documentation and models.'},
                ],
            },
            {
                'label': 'Official Documentation',
                'icon': 'docs',
                'items': [
                    {'title': 'PyTorch Vision Docs', 'url': 'https://pytorch.org/vision/stable/index.html', 'description': 'Datasets, transforms and model zoo for vision.'},
                    {'title': 'Torchvision Models', 'url': 'https://pytorch.org/vision/stable/models.html', 'description': 'Pretrained model catalog for transfer learning.'},
                    {'title': 'Papers with Code — Vision', 'url': 'https://paperswithcode.com/area/computer-vision', 'description': 'Latest vision methods with code and results.'},
                ],
            },
        ],
    },
    'nlp': {
        'name': 'NLP',
        'description': 'Natural language processing: tokenization, embeddings, classification, NER, sequence models, BERT and transformers.',
        'categories': [
            {
                'label': 'Free Courses & Guides',
                'icon': 'book',
                'items': [
                    {'title': 'Hugging Face NLP Course', 'url': 'https://huggingface.co/learn/nlp-course', 'description': 'The hands-on course for transformers and modern NLP.'},
                    {'title': 'Speech and Language Processing', 'url': 'https://web.stanford.edu/~jurafsky/slp3/', 'description': 'Jurafsky & Martin — the standard NLP textbook (free draft).'},
                    {'title': 'Stanford CS224n', 'url': 'https://web.stanford.edu/class/cs224n/', 'description': 'Natural Language Processing with Deep Learning.'},
                ],
            },
            {
                'label': 'Official Documentation',
                'icon': 'docs',
                'items': [
                    {'title': 'spaCy Documentation', 'url': 'https://spacy.io/usage', 'description': 'Industrial-strength NLP library docs.'},
                    {'title': 'NLTK Book', 'url': 'https://www.nltk.org/book/', 'description': 'Natural Language Processing with Python — classic fundamentals.'},
                    {'title': 'Hugging Face Transformers', 'url': 'https://huggingface.co/docs/transformers', 'description': 'Models and pipelines for modern NLP.'},
                ],
            },
        ],
    },
    'generative-ai': {
        'name': 'Generative AI',
        'description': 'Generative AI end to end: LLMs, prompting, fine-tuning, RAG, agents, diffusion, VLMs and running GenAI in production.',
        'categories': [
            {
                'label': 'Free Courses & Guides',
                'icon': 'book',
                'items': [
                    {'title': 'Hugging Face NLP Course', 'url': 'https://huggingface.co/learn/nlp-course', 'description': 'Transformers, fine-tuning and LLM fundamentals with hands-on code.'},
                    {'title': 'DeepLearning.AI Short Courses', 'url': 'https://www.deeplearning.ai/short-courses/', 'description': 'Practical AI courses from industry experts.'},
                    {'title': 'Attention Is All You Need', 'url': 'https://arxiv.org/abs/1706.03762', 'description': 'The Transformer paper that made generative AI possible.'},
                ],
            },
            {
                'label': 'Official Documentation',
                'icon': 'docs',
                'items': [
                    {'title': 'OpenAI Documentation', 'url': 'https://platform.openai.com/docs', 'description': 'API reference for GPT models, embeddings and function calling.'},
                    {'title': 'LangChain Documentation', 'url': 'https://python.langchain.com/docs', 'description': 'Frameworks for RAG, agents and LLM applications.'},
                    {'title': 'Diffusers Documentation', 'url': 'https://huggingface.co/docs/diffusers', 'description': 'State-of-the-art diffusion models for image generation.'},
                ],
            },
        ],
    },
}


def build_index(spec: dict) -> None:
    """Write the hub index.json (must exist before the lesson generator runs)."""
    slug = spec['lang']
    hub_dir = os.path.join(BASE, slug)
    os.makedirs(hub_dir, exist_ok=True)

    res = HUB_RESOURCES[slug]
    index = {
        'slug': slug,
        'name': res['name'],
        'description': res['description'],
        'categories': res['categories'],
        'lessons': [],
    }
    with open(os.path.join(hub_dir, 'index.json'), 'w') as fh:
        json.dump(index, fh, indent=2, ensure_ascii=False)
    print(f'[{slug}] wrote index.json')


if __name__ == '__main__':
    assert len(ALL_SPECS) == 6, f'expected 6 AI course specs, got {len(ALL_SPECS)}'
    os.makedirs(BASE, exist_ok=True)
    for spec in ALL_SPECS:
        build_index(spec)
        run_spec(spec, os.path.join(BASE, spec['lang']))
    print('Done. 6 AI courses generated.')
