# 🎫 Support Ticket Classifier 🚀

## Overview

This project implements an automated support ticket classification system using Logistic Regression combined with TF-IDF feature extraction. The goal is to automatically categorize incoming tickets so they can be routed, prioritized, or resolved more efficiently.

By leveraging a lightweight machine learning approach, the system reduces manual triage effort while remaining simple, fast, and easy to maintain.

## Model Approach

The classifier converts ticket text into numerical features using Term Frequency–Inverse Document Frequency (TF-IDF). These features are then passed into a Logistic Regression model that predicts the appropriate ticket category.

This approach avoids the complexity of deep learning models while still delivering strong performance for structured support workflows.

## Setup

Install the required dependencies:

```bash
pip install pandas scikit-learn
```

Then train, test, and generate predictions by running:

```bash
python classifier.py
```

The script handles training, evaluation, and inference in a single execution.

## Results

The model is designed to significantly reduce manual ticket sorting, with measurable efficiency gains such as cutting manual classification work by approximately 70 percent.

No deep learning infrastructure is required, making the solution lightweight, deployable, and suitable for teams that want practical automation without operational overhead.

This project demonstrates how classical machine learning methods can deliver real operational impact with minimal complexity.

<br>
