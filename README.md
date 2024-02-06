# SourceP
The project's code and dataset set will be open-sourced after the paper is published.

This paper has been accepted by ICASSP 2024.

Arxiv address: https://arxiv.org/abs/2306.01665

# Experimental Results
RQ1: Performance comparison with state-of-the-art methods.
| **Method**        | **Recall** | **Precision** | **F-score** |
| ----------------- | ---------- | ------------- | ----------- |
| XGBoost-TF-IDF    | 0.234      | 0.882         | 0.370       |
| SadPonzi          | 0.52       | 0.59          | 0.55        |
| SVM-NC            | 0.375      | 0.923         | 0.533       |
| Ridge-NC          | 0.453      | 0.829         | 0.586       |
| MulCas            | 0.674      | 0.951         | 0.789       |
| **SourceP**       | **0.887**   | **0.956**      | **0.918**   |


RQ2: Sustainability of the model compared to other state-of-the-art methods.
| **Method** | **Metric** | **P2** | **P3** | **P4** | **P5** |
|------------|------------|--------|--------|--------|--------|
| SadPonzi   | Precision  | 0.33   | 0.42   | 0.18   | 0.24   |
|            | Recall     | **1.0**| 0.71   | 0.25   | 0.18   |
|            | F-score    | 0.5    | 0.53   | 0.21   | 0.20   |
|------------|------------|--------|--------|--------|--------|
| MulCas     | Precision  | 0.88   | 0.96   | 0.81   | 0.95   |
|            | Recall     | 0.38   | 0.32   | **0.94**| 0.67   |
|            | F-score    | 0.53   | 0.48   | 0.87   | 0.79   |
|------------|------------|--------|--------|--------|--------|
| **SourceP**| Precision  | **0.99**| **0.97**| **0.88**| **0.96**|
|            | Recall     | 0.55   | **0.89**| 0.90   | **0.89**|
|            | F-score    | **0.59**| **0.92**| **0.88**| **0.92**|


RQ3: Ablation experiments.
| **Method**       | **Recall** | **Precision** | **F-score** |
|------------------|------------|---------------|-------------|
| SourceP          | **0.887**  | **0.956**     | **0.918**   |
| -w/o EdgePred    | 0.867      | 0.919         | 0.891       |
| -w/o NodeAlign   | 0.821      | 0.914         | 0.860       |
| -w/o Data Flow   | 0.806      | 0.909         | 0.847       |

RQ4: Generalization ability of SourceP.

| **Method** | **Recall** | **Precision** | **F-score** |
|------------|------------|---------------|-------------|
| SourceP    | 0.90       | 0.92          | 0.91        |
