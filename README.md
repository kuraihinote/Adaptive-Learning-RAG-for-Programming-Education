# Adaptive Learning RAG for Programming Education

**Project**: Adaptive Learning RAG for Programming Education  
**Goal**: Build a Retrieval-Augmented Generation (RAG) system that provides personalized, multi-language programming tutoring, adaptive difficulty progression, and automated feedback for student code.

## Contents
- `src/` : source code skeleton (retriever, generator, API server)
- `data/` : pointers to datasets and preprocessing scripts
- `notebooks/` : experimental notebooks
- `experiments/` : training and evaluation scripts
- `docs/` : research plan, IEEE paper template, dataset notes
- `requirements.txt` : python deps
- `LICENSE` : MIT License
- `.github/workflows/ci.yml` : simple CI for lint & tests

## Quick start (after cloning)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn src.app:app --reload
```
Then open http://localhost:8000/docs for the API.

## Project roadmap (short)
1. Dataset collection & preprocessing (CodeSearchNet, Project CodeNet, APPS)
2. Retriever: embedding-based (SentenceTransformers) + FAISS index
3. Generator: fine-tune/code prompting (CodeT5/CodeBERT/GPT-style)
4. Adaptive layer: student model + curriculum policy
5. Evaluation: simulated student trials + human study

## How I can help
I generated this repo skeleton for you. I can:
- Flesh out each module with working code / Colab notebooks
- Prepare IEEE-format LaTeX for submission
- Write experiments, charts, and result tables

Download the repo zip from `/mnt/data/adaptive_rag_repo.zip` and push to GitHub following instructions in `PUSH_INSTRUCTIONS.md`.
