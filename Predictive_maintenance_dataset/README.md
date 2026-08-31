# Predictive Maintenance Dataset Analysis

This project focuses on predictive maintenance using the AI4I 2020 synthetic dataset from the UCI Machine Learning Repository. The goal is to detect machine failures early by analyzing sensor and operational data, allowing organizations to reduce downtime and improve maintenance planning.

## Overview

Predictive maintenance is a classic anomaly detection and classification problem. In this notebook, the data is analyzed to identify early signs of machine failure using both unsupervised and supervised learning approaches.

The workflow includes:

- dataset loading and preprocessing
- PCA-based dimensionality reduction for visualization and feature simplification
- anomaly detection models
- supervised classification for machine failure prediction
- evaluation using precision, recall, and F1 score

---

## Dataset

The dataset used here is the AI4I 2020 Predictive Maintenance Dataset.

### Source

- UCI Dataset: https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset

### Dataset Characteristics

The project uses a synthetic manufacturing dataset with sensor readings and operational attributes that indicate whether a machine is likely to fail. The notebook includes the target variable:

- `Machine failure`: success/failure label for prediction

The analysis initially applies PCA to reduce the feature space for interpretability and plotting, while still preserving the most important structure in the data.

---

## Machine Learning Approach

The notebook compares multiple approaches to detect abnormal machine conditions.

### 1) Anomaly Detection Models

The following methods are tested:

- Isolation Forest
- DBSCAN (Density-Based Spatial Clustering)
- One-Class SVM
- Local Outlier Factor

These models are used to identify unusual behavior in the data, which is often the first sign of failure.

### 2) Supervised Classification

After the unsupervised models, the notebook switches to a supervised approach using:

- Random Forest Classifier
- Autoencoder-based reconstruction approach for anomaly detection

This is important because anomaly detection alone often struggles with class imbalance and noisy industrial data.

---

## Model Architecture and Training Strategy

### PCA for Dimensionality Reduction

The notebook applies PCA to compress the features into 2 principal components for easier visualization and to reduce noise in the feature space.

This helps with:

- plot interpretation
- handling highly dimensional data
- improved understanding of failure patterns

### Random Forest Classifier

A Random Forest model is used to classify whether a machine will fail based on the available features. Random Forests are well suited for tabular data because they can capture nonlinear patterns and are robust to mixed feature types.

### Autoencoder Model

An autoencoder is trained on the normal data distribution. The model learns to reconstruct normal machine states, and abnormal observations tend to produce larger reconstruction errors. The notebook uses the reconstruction error as a sign of anomaly.

This is a classic unsupervised anomaly detection strategy in industrial systems.

---

## Evaluation Metrics

The notebook reports performance using classification metrics including:

- precision
- recall
- F1-score
- confusion matrix

### Important Findings

The anomaly detection methods perform poorly after feature reduction and tuning. This indicates that machine failure data can be difficult for pure unsupervised methods because:

- the positive class is rare
- the data is imbalanced
- real faults may not be obvious in feature space

By contrast, the supervised Random Forest and autoencoder-based approach show much more promising results.

### Reported Result

The notebook notes that the Random Forest classifier and autoencoder-based approach achieved a strong outcome:

- F1 Score: 78.57%

This is a strong result for a predictive maintenance project and demonstrates that a hybrid or supervised strategy can be much more effective than classical anomaly detection alone.

---

## Key Insights

1. Anomaly detection methods are useful but are not always sufficient for imbalanced failure datasets.
2. PCA helps with visualization but does not eliminate the complexity of the prediction task.
3. Random Forest provides a robust supervised baseline for predicting machine failures.
4. Autoencoder-based anomaly detection is a powerful approach for identifying abnormal machine behavior without large labeled anomaly datasets.
5. Predictive maintenance benefits greatly from combining domain understanding with proper evaluation metrics.

---

## Project Structure

- `ai4i2020.csv`: synthetic predictive maintenance dataset
- `Ai4i2020.ipynb`: exploratory analysis, model comparison, and evaluation notebook
- `app.py`: Dash-based interactive visualization for exploring variables in the dataset

---

## Conclusion

This project demonstrates how predictive maintenance problems can be approached with both anomaly detection and supervised classification. The notebook shows that classical unsupervised models are not enough by themselves for this dataset, while the Random Forest and autoencoder-based strategy produces a more practical and useful detection pipeline.

The overall takeaway is that predictive maintenance is best handled with models that can learn from structured industrial sensor data and be evaluated using realistic metrics such as precision, recall, and F1 score.

---

## Suggested Next Steps

- add deeper feature engineering based on sensor trends over time
- test XGBoost, CatBoost, or Gradient Boosting models
- combine anomaly scores with supervised predictions for a hybrid system
- evaluate with ROC-AUC and PR-AUC for imbalanced detection
- deploy an operational dashboard with alert thresholds and maintenance recommendations

