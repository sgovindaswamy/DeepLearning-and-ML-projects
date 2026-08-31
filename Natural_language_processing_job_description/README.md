# Natural Language Processing for Job Description Classification

This project applies natural language processing (NLP) to classify job descriptions into their respective categories using a pre-trained language model from FastAI. Instead of relying on handcrafted rules or simple bag-of-words approaches, the notebook uses transfer learning with a state-of-the-art language model to understand the semantics of job text and predict the correct class.

## Overview

Job description classification is a text classification problem where the goal is to infer the job category from the words and phrases in a job description. This is useful for recruitment systems, talent matching, job recommendation engines, and resume-to-role categorization.

In this notebook, the workflow is built around FastAI’s ULMFiT (Universal Language Model Fine-tuning) approach:

- prepare the text dataset
- fine-tune a pre-trained language model on job descriptions
- adapt the model for classification
- generate predictions for unseen job descriptions
- export the trained model for reuse

---

## Dataset

The project uses a Kaggle dataset for job description classification. The notebook loads a training label file and merges it with the text data on the `Id` field. After the merge, the dataset is cleaned and prepared for NLP training.

The key idea is to combine:

- the textual job description
- the target label or category associated with that job

The dataset is then split into training and validation sets so the model can learn patterns from one subset and be evaluated on a held-out subset.

### Typical Data Flow

- read the label file
- merge labels with the description dataset
- remove non-essential columns such as `gender` and `Id`
- create text-only training/validation splits
- train a language model and then a classifier

---

## NLP Pipeline and Model Architecture

This notebook uses FastAI’s text modeling pipeline, which is designed specifically for NLP tasks and integrates pre-trained embeddings and recurrent language models.

### 1) Language Model Pretraining

The first stage uses `TextLMDataBunch.from_df(...)` to create a FastAI text dataset from the training and validation DataFrames.

A language model is then built with:

- `language_model_learner(...)`
- `arch = AWD_LSTM`
- `pretrained = True`
- `drop_mult = 0.4`

This approach is based on the ULMFiT concept: a pre-trained recurrent language model is fine-tuned on domain-specific text (job descriptions), enabling it to learn the vocabulary, phrasing, and structure of the target domain before classification.

### 2) Transfer Learning with AWD-LSTM

The model architecture is based on the AWD-LSTM network, a highly effective recurrent model for text. AWD-LSTM improves generalization through weight dropping and other regularization tricks, making it well suited for text classification tasks.

The notebook fine-tunes the language model in stages using FastAI’s learning-rate scheduling:

- `learn.fit_one_cycle(1, 1e-2)`
- `learn.fit_one_cycle(2, min_grad_lr)`
- `learn.fit_one_cycle(2, 1e-3)`

These cycles progressively adapt the model to the job-description domain while keeping the training stable.

### 3) Text Classifier

After the language model is fine-tuned, the notebook builds a text classifier using:

- `text_classifier_learner(...)`
- `AWD_LSTM`
- `drop_mult = 0.5`

This classifier head learns to map the learned text representations to the target job categories. The notebook then unfreezes the model and continues training with:

- `learn.unfreeze()`
- `learn.fit_one_cycle(...)`

This second stage allows deeper layers to adapt to the classification problem more precisely.

---

## Training Process

The project follows a standard transfer-learning workflow used in modern NLP:

1. Build a text data bundle from job descriptions
2. Train a language model on the raw text data
3. Use the learned representations for classification
4. Fine-tune the classifier with a lower learning rate
5. Evaluate validation performance using the built-in FastAI metrics
6. Export the trained model for reuse

This is a strong approach for text data because it captures contextual language patterns better than simple keyword matching.

---

## Evaluation Metrics

The notebook uses FastAI’s built-in performance tracking, which logs:

- `train_loss`
- `valid_loss`
- `accuracy`

The training outputs show the evolution of these metrics over multiple fine-tuning cycles, which is the standard way to monitor whether the model is learning and generalizing properly.

### Why accuracy is used

This is a classification task, so accuracy is the primary metric reported during training. It measures how often the model predicts the correct job category for the validation examples.

The notebook also computes predictions on the test set and converts the output probabilities into category labels using:

- `preds = learn.get_preds(...)`
- `testlabels = np.argmax(preds, 1)`

This output is then saved to a CSV file for submission or downstream use.

---

## Model Output and Export

Once training is complete, the model is exported using:

- `learn.export('modelfastai.pkl')`

This allows the trained classifier to be reused later for inference on new job-description text without retraining.

---

## Key Takeaways

1. The project uses a modern NLP transfer-learning workflow rather than a basic rule-based method.
2. `AWD_LSTM` is the core architecture, making the model good at handling sequential text data.
3. The language-model pretraining step is especially important because it adapts the model to the domain-specific wording used in job descriptions.
4. FastAI’s training loop enables stable fine-tuning with a small number of training epochs.
5. The final model is suitable for real-world job classification and recommendation tasks.

---

## Project Structure

- `FAST_AI.ipynb`: full notebook implementing data preparation, language-model fine-tuning, and job classification
- `README.md`: project overview and documentation

---

## Conclusion

This project demonstrates how transfer learning can be effectively applied to job description classification. By using a pre-trained AWD-LSTM language model and then fine-tuning it on domain-specific text, the notebook achieves a practical and scalable NLP solution for classifying job descriptions.

It is a strong example of how modern language models can be adapted for real-world text classification problems in recruitment and HR analytics.

---

## Suggested Next Steps

- Compare with traditional machine learning baselines such as TF-IDF + Logistic Regression or SVM
- Add more job categories or improve class balance
- Evaluate using precision, recall, F1-score, and confusion matrix in addition to accuracy
- Deploy the model as a small API for automatic job categorization
- Explore multilingual job descriptions and skill extraction tasks

This project is a good introduction to domain-specific transfer learning for NLP and serves as a practical benchmark for text classification in recruitment data.

For the original dataset, the notebook references the Kaggle competition here:
https://www.kaggle.com/competitions/defi-ia-insa-toulouse/data
