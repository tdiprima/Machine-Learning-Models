# 🚀 Fast Email Spam Filter

## Overview

This project implements a fast and lightweight email spam filter using the Naive Bayes algorithm. It is designed for efficient spam versus ham (non-spam) classification, making it suitable for real-time or high-volume email processing systems.

## Model Approach

The classifier uses a probabilistic Naive Bayes model to learn patterns in labeled email data. Because Naive Bayes is computationally simple and highly efficient, the model trains in seconds and performs inference almost instantly.

## Setup

Install the required dependencies:

```bash
pip install scikit-learn pandas numpy
```

To train the model and run the benchmark, execute:

```bash
python email_classifier.py
```

The script will train the classifier and report performance metrics.

## Performance

Typical benchmark results include:

* Training time of approximately 0.01 seconds
* Inference time of roughly 1 millisecond for 500 emails
* Classification accuracy of around 95 percent

## Output

The program reports training duration, inference speed, and accuracy metrics directly in the console. The resulting model is simple, efficient, and ready to be deployed in production environments where fast spam detection is required.

This implementation demonstrates how a classic machine learning algorithm can deliver strong performance with minimal computational overhead.

<br>
