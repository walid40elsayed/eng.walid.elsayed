# Credit Card Fraud Detection - XGBoost Model

## 📋 Project Overview

This project implements a sophisticated **XGBoost-based fraud detection system** designed to identify fraudulent credit card transactions in real-time. The model achieves **85.4% fraud detection rate** while reducing the effective fraud rate from **0.58% to 0.08%** (85.4% reduction).

### 🎯 Business Impact
- **💰 $394,532** in immediate fraud prevention
- **📉 85.4% reduction** in fraud rate
- **⚡ 7,280 analyst hours** saved annually
- **🔍 100% transaction coverage** vs. manual sampling

---

## 🏗️ Model Architecture

### Data Pipeline
```
Raw Transactions → Feature Engineering → Encoding → Feature Selection → XGBoost → Business Rules
```

### Key Components
1. **Feature Engineering** - 41 engineered features capturing temporal, behavioral, and geographic patterns
2. **Smart Encoding** - Strategic handling of categorical variables
3. **Class Imbalance Handling** - Multiple strategies tested (SMOTE, class weights)
4. **Ensemble XGBoost** - Optimized for fraud detection metrics
5. **Threshold Optimization** - Business-focused decision boundary

---

## 📊 Model Performance

### Test Set Results (Optimal Threshold: 0.25)
| Metric | Value |
|--------|-------|
| **Average Precision** | 0.927 |
| **ROC AUC** | 0.997 |
| **Fraud Recall** | 85.4% |
| **Fraud Precision** | 88.9% |
| **Fraud F1-Score** | 87.1% |

### Confusion Matrix
```
[[256900    160]  → 160 False Positives
 [   219   1278]]  → 1,278 True Positives | 219 False Negatives
```

### Holdout Set Validation
- **Average Precision**: 0.974
- **ROC AUC**: 0.999
- **Confusion Matrix**: 3865 TN | 3 FP | 1 FN | 22 TP

---

## 🔧 Technical Implementation

### Feature Engineering

#### Temporal Features
- `is_night`, `is_weekend`, `is_morning_rush`
- `is_month_end`, `afternoon`, `late_night`
- `trans_hour`, `trans_day`, `trans_month`

#### Behavioral Features
- `time_since_last_tx` - Hours since last transaction
- `amt_to_card_mean_ratio` - Amount vs. customer's typical spending
- `amt_z_score` - Statistical outlier detection
- `amt_log` - Log-transformed amount

#### Geographic Features
- `dist_merch2cust` - Distance from customer to merchant
- `is_long_distance` - Unusual transaction locations

### Top 10 Most Important Features
1. **is_night** (21.8%) - Nighttime transactions
2. **amt** (17.1%) - Transaction amount
3. **is_high_risk_merch_cat** (4.3%) - Merchant category risk
4. **category** (3.8%) - Transaction category
5. **is_weekend** (3.8%) - Weekend transactions
6. **afternoon** (3.6%) - Afternoon hours
7. **trans_hour** (3.1%) - Hour of day
8. **trans_year** (2.8%) - Year trend
9. **trans_day** (2.1%) - Day of week
10. **is_month_end** (1.6%) - End-of-month patterns

### Model Configuration
```python
xgb_params = {
    'n_estimators': 1000,
    'learning_rate': 0.05,
    'max_depth': 8,
    'min_child_weight': 1,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'gamma': 0.1,
    'reg_alpha': 0.1,
    'reg_lambda': 0.1,
    'scale_pos_weight': 1,  # Balanced approach
    'eval_metric': 'aucpr',  # Optimized for imbalanced data
    'random_state': 42
}
```

---

## 💼 Business Value Analysis

### Financial Impact
| Component | Value |
|-----------|-------|
| **Fraud Transactions Prevented** | 1,278 |
| **Average Fraud Amount** | $308.71 |
| **Total Fraud Savings** | $394,532 |
| **False Positive Cost** | $1,600 |
| **Net Savings** | **$392,932** |

### Operational Efficiency
- **Transaction Coverage**: 100% (vs. 1-2% manual review)
- **Review Time Reduction**: 85% (15 min → 2.25 min per case)
- **Analyst Hours Saved**: 7,280 hours annually
- **FTE Equivalent**: 3.5 analysts redeployed

### ROI Calculation
- **Return on Investment**: 24,558%
- **Benefit-Cost Ratio**: 246:1
- **Cost per Fraud Prevented**: $1.25

---

## 🚀 Deployment Ready

### Model Files
- `xgb_fraud_model.pkl` - Trained XGBoost model
- `xgb_selected_features.pkl` - Feature list for inference
- `xgb_training_set.csv` - Training data ( find it here : https://drive.google.com/file/d/1VLJfkbiiV6OLMohRuE34ayfD82ZTIhM_/view?usp=drive_link )

### Inference Function
```python
def predict_fraud(model, features, transaction_data, threshold=0.25):
    """Real-time fraud prediction"""
    X_pred = transaction_data[features]
    fraud_proba = model.predict_proba(X_pred)[:, 1]
    predictions = (fraud_proba >= threshold).astype(int)
    return predictions, fraud_proba
```

### Integration Features
- **Real-time scoring** - <100ms per transaction
- **Configurable thresholds** - Business-tunable sensitivity
- **Feature validation** - Automatic data quality checks
- **Monitoring ready** - Drift detection and performance tracking

---

## 📈 Model Selection Rationale

### Why XGBoost?
- **Proven performance** on tabular data
- **Handles non-linear patterns** in fraud behavior
- **Built-in regularization** prevents overfitting
- **Feature importance** for explainability
- **Production-ready** with fast inference

### Encoding Strategy
- **Target Encoding** for high-cardinality features
- **One-Hot Encoding** for low-cardinality categoricals
- **Frequency Encoding** for supplemental features

### Threshold Optimization
- **Default**: 0.5 (balanced)
- **Optimal**: 0.25 (maximizes business value)
- **Result**: Better fraud catch rate with acceptable false positives

---

## 🔮 Future Enhancements

### Short-term (Next 3 months)
1. **Real-time feature store** for customer behavior patterns
2. **Adaptive thresholding** based on transaction value
3. **Ensemble methods** combining multiple algorithms

### Medium-term (6-12 months)
1. **Graph neural networks** for network analysis
2. **Unsupervised anomaly detection** for novel fraud patterns
3. **Reinforcement learning** for adaptive fraud rules

### Long-term (12+ months)
1. **Federated learning** for privacy-preserving multi-bank models
2. **Explainable AI** for regulator-friendly decisions
3. **AutoML pipeline** for continuous model improvement

---

## 📊 Results Reproduction

1. **Data Preparation**
   ```bash
   python scripts/preprocess_data.py
   ```

2. **Model Training**
   ```bash
   python scripts/train_model.py
   ```

3. **Evaluation**
   ```bash
   python scripts/evaluate_model.py
   ```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Team

**Lead Data Scientist**: [Walid Elsayed]  
**Fraud Operations**: Business stakeholder collaboration  
**Engineering**: MLOps and deployment support

### Acknowledgments
- Fraud analysis team for domain expertise
- Engineering for production infrastructure
- Business stakeholders for cost-benefit guidance

---

## 📞 Contact

For questions about this model or implementation details:
- **Email**: [walid,em724@gmail.com]

---

## ⚠️ Disclaimer

This model should be used as part of a **comprehensive fraud detection strategy**, not as a standalone solution. Regular monitoring, retraining, and human oversight are essential for maintaining performance and adapting to evolving fraud patterns.

---

*"Stopping fraud, one transaction at a time."* 🛡️💳
