---
title: Reading Notes - Fletcher & Stevenson 2025
status: complete
created: 2026-10-08
tags: [retraction, machine-learning]
---

# Reading Notes: Fletcher & Stevenson (2025)

## Problem
- Retractions are increasing; retracted papers keep getting cited.
- No open dataset + predictive ML models existed before.
- Objective: build dataset, train models, run ablation.

## Methodology
- Case-control, retrospective (2000–2020)
- Data: Retraction Watch + OpenAlex
- 9,028 articles (50/50 balanced)
- Split: 64/16/20
- Models: SVM, XGBoost, RF, MLP, Decision Tree, Super Learner, BERT, BioBERT, Llama 3.2, Gemma 2, GPT-4o mini, Claude 3.5

## Data & Results
- 7.54% Retraction Watch papers were not marked as retracted by OpenAlex
- Best accuracy: Llama 3.2 base = 0.682
- Best precision (retracted): SVM = 0.690
- Traditional ML > LLMs (except Llama 3.2 base)
- Commercial LLMs = all "not retracted"
- Ablation: Year > Topic > Country > Abstract (least)

## Interpretation
- Models are learning correlational patterns
- Useful as screening tool, not for automatic decisions
- Ethical concerns: bias, self-censorship, gaming
- Human-in-the-loop is essential

## Source
- [[fletcher-2025-predicting-retracted-research]]