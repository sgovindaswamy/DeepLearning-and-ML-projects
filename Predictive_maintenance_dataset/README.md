## ANOMALY DETECTION

This section shows implementation of anamoly detection algorithm on the Ai4i2020 dataset from the UCI machine learning repository. Here is the official link for the dataset : https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset

After reducing the dimensionality using dimensionality reduction technique such as Principal Component Analysis, The anamoly detection algorithms that have been implemented are as follows, 

1) Isolation Forest
2) Density based spatial clustering
3) One-class SVM
4) Local outlier factor

These algorithms displayed poor performance on the test set even after performing hyperparameter tuning using Gridsearch CV.

however the Random forest classifier and AutoEncoders showed promising results with an F1 score of 78%





