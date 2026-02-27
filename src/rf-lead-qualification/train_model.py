#!/usr/bin/env python3
"""
Random Forest for lead qualification automation.
Trains on scraped leads data, predicts worth pursuing (0/1).
Outputs: accuracy, feature importances (for explainability),
         predictions on test set, sample decisions.
Simple deployable script: retrain or predict in prod pipelines.
Real problem: Automate sales pursuit from web scrapes.
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# Load data (run generate_dataset.py first)
print("Loading data...")
train_df = pd.read_csv('leads_train.csv')
test_df = pd.read_csv('leads_test.csv')

X_train = train_df.drop('worth_pursuing', axis=1)
y_train = train_df['worth_pursuing']
X_test = test_df.drop('worth_pursuing', axis=1)
y_test = test_df['worth_pursuing']

# Train RF (200 trees for balance of speed/accuracy)
print("Training Random Forest...")
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]  # Prob for pursuit

# Metrics
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy on test: {accuracy:.2%}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Feature importances (key for interpretability in automation)
importances = pd.DataFrame({
    'feature': X_train.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print("\nFeature Importances (Explainable Decisions):")
print(importances.round(3))

# Sample predictions (understandable output for deployment)
sample_idx = np.random.choice(len(X_test), 5, replace=False)
print("\nSample Test Leads & Predictions:")
for i in sample_idx:
    lead = X_test.iloc[i]
    pred = y_pred[i]
    proba = y_pred_proba[i]
    true = y_test.iloc[i]
    print(f"Lead: size={lead['company_size']}, rev=${lead['revenue_estimate']/1e3:.0f}k, "
          f"loc={lead['location_score']:.1f}, traffic={lead['traffic']/1e3:.0f}k")
    print(f"  True: {true}, Pred: {pred} (prob: {proba:.2%}) {'✅' if pred==true else '❌'}")
    print()

print("Model ready for deployment. Save with: joblib.dump(model, 'rf_lead_model.pkl')")
