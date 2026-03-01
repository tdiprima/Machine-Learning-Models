# 🚀 Simple Revenue Forecaster

## Overview

This project automates monthly revenue prediction using advertising spend and website visit data. It replaces manual spreadsheet-based forecasting with a lightweight, repeatable machine learning workflow that can be retrained quickly as new data becomes available.

The model is designed for practical business automation rather than competitive modeling complexity. It focuses on clarity, speed, and interpretability.

## Purpose

Revenue forecasting is often handled manually in spreadsheets, which can be time-consuming and error-prone. This project streamlines the process by training a regression model that learns the relationship between marketing inputs (such as ad spend and traffic) and resulting revenue.

The result is a fast, automated pipeline that can generate consistent forecasts with minimal operational overhead.

## Quick Start

To train the model, evaluate its performance, and generate a forecast, run:

```bash id="k82nqv"
python revenue_predictor.py
```

The script will automatically handle training, testing, and producing a sample future prediction.

## Outputs

After execution, the program provides:

* **Model performance metrics**, including:

  * **R² (R-squared)**, or the coefficient of determination. This measures how well the model explains the variation in revenue. An R² value closer to 1 indicates that the model accounts for a larger proportion of revenue variability.
  * **MSE (Mean Squared Error)**, which measures the average squared difference between predicted revenue and actual revenue. Lower MSE values indicate more accurate predictions.

* **Model coefficients**, showing how strongly each input variable (such as ad spend or visits) influences predicted revenue.

* **A future revenue prediction example**, demonstrating how the model can be used for forward planning.

## Production Readiness

This solution is intentionally simple and easy to retrain. It avoids unnecessary complexity while remaining interpretable and operationally efficient. The design prioritizes automation, maintainability, and business usability over experimentation or competitive modeling.

It is built for real-world deployment and repeatable forecasting workflows.

<br>
