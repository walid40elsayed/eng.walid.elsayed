# 📉 Churn Analysis - Data Science Project

This repository contains a complete end-to-end project for analyzing and predicting customer churn. It includes data preprocessing, feature engineering, model building using machine learning (Random Forest), and visualization using Power BI.

---

## 📁 Project Structure

```
.
├── Churn_Analysis.ipynb       # Main Jupyter Notebook for model pipeline
├── Churn Analysis.pbix        # Power BI report for churn visualization
├── Predection_Data.xlsx       # Input dataset
├── churn_model.pkl            # Trained Random Forest model
├── encoding_pipeline.pkl      # Saved pipeline for preprocessing
├── requirements.txt           # Python package requirements
└── README.md                  # Project overview
```

---

## 🎯 Objective

The primary goal of this project is to identify customers who are likely to churn (i.e., discontinue service) and understand the key factors driving this behavior. This enables businesses to take proactive steps in retaining high-value customers.

---

## 🛠️ Tools & Technologies

- Python 3
- Jupyter Notebook
- Pandas, NumPy, Seaborn, Matplotlib
- Scikit-learn, Imbalanced-learn (SMOTE)
- Category Encoders
- Power BI (for dashboard visualization)
- Joblib (for saving models and pipelines)

---

## 📊 Dataset Overview

- **Source**: `Predection_Data.xlsx`
- **Rows**: Customers
- **Columns**: Demographic data, service details, billing information, and churn status

Key features include:

- `Gender`, `Age`, `Married`, `State`
- `Phone_Service`, `Internet_Type`, `Contract`
- `Monthly_Charge`, `Total_Charges`
- `Customer_Status` (Target: 0 = Stayed, 1 = Churned)

---

## 📌 Workflow Summary

### 1. 📥 Data Loading

```python
data = pd.read_excel("Predection_Data.xlsx", sheet_name='vw_ChurnData')
```

### 2. 🔎 Exploratory Data Analysis (EDA)

- Used `.info()`, `.describe()`, and value counts
- Handled anomalies like negative values in `Monthly_Charge`
- Visualized imbalance in `Customer_Status`

### 3. 🧹 Data Preprocessing

- Label encoding & OneHot encoding for categorical variables
- Feature selection with `f_classif`
- SMOTE for balancing target classes

### 4. 🤖 Modeling

- Used **Random Forest Classifier**
- Hyperparameter tuning with `GridSearchCV`
- Cross-validation with `StratifiedKFold`

### 5. 📈 Evaluation

- Accuracy, Confusion Matrix, Classification Report
- Handled model evaluation on unseen test data

### 6. 💾 Pipeline Saving

```python
joblib.dump(model_pipeline, "churn_model.pkl")
joblib.dump(encoder_pipeline, "encoding_pipeline.pkl")
```

### 7. 📊 Dashboard

- Created interactive Power BI report
- Visualized churn by region, gender, service type, and payment method

---

## 🧠 Insights

- Churn rates are higher among customers with:
  - Month-to-month contracts
  - No internet service
  - Lower tenure or higher monthly charges
- Targeted offers can help retain high-risk groups

---

## 🚀 Future Work

- Deploy model via Flask/FastAPI
- Connect model outputs to real-time dashboards
- Integrate additional data sources (e.g., call center logs)

---

## 📎 How to Use

1. Clone the repo:
```bash
git clone https://github.com/yourusername/churn-analysis-project.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the notebook:
```bash
jupyter notebook Churn_Analysis.ipynb
```

4. Open `Churn Analysis.pbix` in Power BI Desktop for dashboard.

---

## 📬 Contact

For questions, feel free to reach out via [LinkedIn](https://www.linkedin.com/) or raise an issue in this repo.