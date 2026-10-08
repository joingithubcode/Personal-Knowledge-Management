---
title: Analyzing the Scientific Method in ML Research - Retraction Prediction
status: active
created: 2026-10-08
tags: [scientific-method, machine-learning, retraction]
---

# Analyzing the Scientific Method in ML Research: Retraction Prediction

Fletcher, A. H. A., & Stevenson, M. (2025). Predicting retracted research: a dataset and machine learning approaches. *Research Integrity and Peer Review, 10*(9). Springer Nature. https://doi.org/10.1186/s41073-025-00168-w

## 1. Selecting and Defining a Problem
The authors identify that retractions are increasing while retracted papers continue to be cited extensively, undermining scientific integrity. Prior to this work, no open dataset combined Retraction Watch with OpenAlex, and no machine learning models had been systematically trained to predict retractions. The research gap lies in the absence of reproducible predictive tools and the lack of understanding which features most strongly correlate with retractions. The study's objective is to build a comprehensive dataset and evaluate ML models' ability to distinguish retracted from non-retracted articles, providing a screening mechanism for research integrity monitoring.

## 2. Describing the Methodology of Research
The study employs a case-control, retrospective design spanning 2000–2020, using a balanced sample of 9,028 articles (50% retracted, 50% non-retracted). Data were sourced by merging Retraction Watch records with OpenAlex metadata, then split into training (64%), validation (16%), and test (20%) sets. Feature sets include publication year, author country, journal topic, and abstract text. Models evaluated range from traditional machine learning (SVM, XGBoost, Random Forest, Decision Tree, Super Learner) to large language models (BERT, BioBERT, Llama 3.2, Gemma 2, GPT-4o mini, Claude 3.5). Performance is measured by accuracy, precision for the retracted class, and ablation studies assessing feature importance.

## 3. Collecting and Analyzing Data
Results show that 7.54% of Retraction Watch papers were not marked as retracted by OpenAlex, highlighting data consistency issues. Traditional ML models outperformed commercial LLMs, except Llama 3.2 base, which achieved the highest accuracy (0.682). SVM achieved the best precision for the retracted class (0.690). Ablation analysis revealed that publication year is the most important feature, followed by topic and country, while the abstract contributed the least predictive power. Commercial LLMs consistently predicted "not retracted" for all test cases, suggesting a misalignment between their training objectives and retraction detection.

## 4. Interpreting Results
The authors interpret their findings as evidence that models learn correlational patterns rather than causal signals of misconduct, making them suitable as screening tools but not for automated decisions. Ethical concerns include potential bias against certain research topics or regions, self-censorship by authors aware of predictive tools, and the risk of gaming the model by manipulating selected features. Human-in-the-loop oversight is deemed essential. Future work should explore causal inference methods, expand the dataset to include pre-registration data, and investigate real-time retraction prediction pipelines integrated into publishing workflows.