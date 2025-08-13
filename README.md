
# 🩺 Chronic Kidney Disease (CKD) Prediction System

## 📖 Abstract
Chronic Kidney Disease (CKD) is a global health concern characterized by a gradual loss of kidney function over time. Early detection plays a crucial role in preventing progression to end-stage renal disease, which requires dialysis or transplantation. Many patients remain unaware of the disease until it reaches an advanced stage.

This project leverages **routine medical test data** to predict CKD presence, severity, and progression. By analyzing parameters such as **serum creatinine, albumin levels, GFR, and hemoglobin**, the system uses **machine learning models** to provide early warnings, severity predictions, and monitoring alerts — improving patient outcomes through timely intervention and personalized treatment plans.

---

## 🎯 Objectives
- Detect CKD in its early stages using routine medical test results.
- Predict disease severity and patient survival probability.
- Monitor CKD progression over time and alert physicians of significant changes.
- Assist doctors in making timely, data-backed treatment decisions.

---

## 📚 Literature Review
- **Early Detection**: Early CKD detection can reduce the need for dialysis by up to 50%.
- **ML in CKD**: Models like Random Forest, Logistic Regression, and SVM show high accuracy for CKD classification.
- **Biomarkers**: Key indicators include **GFR, serum creatinine, albumin, blood pressure, and hemoglobin**.

---

## 🏗 Proposed System
The system has **three functional modules**:
1. **Early Detection** – Analyze test results to detect CKD presence.
2. **Severity & Survival Prediction** – Predict CKD stage and survival probability.
3. **Progress Monitoring** – Track patient results and generate alerts.

---

## 🔍 Methodology
### Step 1: Data Collection
- Use CKD datasets (UCI Repository or hospital records).
- Parameters: age, BP, specific gravity, albumin, sugar, serum creatinine, GFR, hemoglobin, RBC count, etc.

### Step 2: Data Preprocessing
- Handle missing values.
- Normalize continuous values.
- Encode categorical attributes (e.g., "normal" / "abnormal").

### Step 3: Feature Selection
- Use correlation analysis & feature importance.
- Key features: creatinine, albumin, hemoglobin, GFR.

### Step 4: Model Selection & Training
- Logistic Regression (baseline).
- Random Forest (high accuracy).
- SVM.
- Evaluation metrics: Accuracy, Precision, Recall, F1-score.

### Step 5: Prediction Module
- Predict presence (Yes/No).
- Predict CKD stage (1-5).
- Predict survival likelihood.

### Step 6: Monitoring Module
- Store follow-up data.
- Generate alerts when decline in kidney function is detected.

---

## ✅ Conclusion

This project demonstrates that routine medical test data can be leveraged to:
- Detect CKD early.
- Predict severity.
- Monitor disease progression.

Such a system can improve patient survival rates and reduce late-stage treatment costs.

## 🚀 Future Scope

- Integrating wearable devices for real-time health monitoring.
- Expanding dataset for better accuracy across demographics.
- Using deep learning models for better survival prediction.
= Mobile app integration for patient self-monitoring.

## 📚 References

- UCI Machine Learning Repository: Chronic Kidney Disease Dataset
- Levey AS, Coresh J. "Chronic kidney disease." The Lancet, 2012.
- Tangri N, et al. "A predictive model for progression of chronic kidney disease to kidney failure." JAMA, 2011.

## 🎦 Demo video
  
[Click here to see Demo](https://drive.google.com/file/d/1W85XYz7MRSYwtjMvLVE4TTxcCC1A2OMx/view?usp=sharing)
