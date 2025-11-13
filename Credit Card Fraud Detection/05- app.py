import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and selected features
model = joblib.load(r"A:\work\datascince\projects\Fraud Use Case\xgb\xgb_fraud_model.pkl")
features = joblib.load(r"A:\work\datascince\projects\Fraud Use Case\xgb\xgb_selected_features.pkl")
threshold = 0.5  # Replace with your optimal threshold if known

# 💡 App Title
st.set_page_config(page_title="Fraud Detection App", layout="wide")
st.title("🔍 Real-Time Fraud Detection")
st.markdown("Upload transaction data to predict fraud and estimate business impact.")

# Upload CSV
uploaded_file = st.file_uploader("xgb_holdout_set.csv", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)

    # Check for missing features
    missing = set(features) - set(data.columns)
    if missing:
        st.error(f"Missing features: {missing}")
    else:
        # Predict fraud probabilities
        X_pred = data[features]
        fraud_proba = model.predict_proba(X_pred)[:, 1]
        data['fraud_probability'] = fraud_proba
        data['fraud_prediction'] = (fraud_proba >= threshold).astype(int)

        # Summary metrics
        fraud_count = data['fraud_prediction'].sum()
        total_count = len(data)
        fraud_percentage = (fraud_count / total_count) * 100

        # Business impact
        avg_fraud_amt = data[data['fraud_prediction'] == 1]['amt'].mean() if 'amt' in data.columns else 100
        savings = fraud_count * avg_fraud_amt
        false_positives = ((data['fraud_prediction'] == 1) & (data['is_fraud'] == 0)).sum() if 'is_fraud' in data.columns else 0
        fp_cost = false_positives * 10
        net_savings = savings - fp_cost

        # Display results
        st.success("Predictions complete!")
        st.dataframe(data.head())

        #Download predictions
        st.download_button("Download Predictions", data.to_csv(index=False), "fraud_predictions.csv")

        # Summary Report
        st.markdown("### 📊 Summary Report")
        st.markdown(f"""
        - Total Transactions: **{total_count}**
        - Fraudulent Predictions: **{fraud_count}**
        - Estimated Savings: **${savings:.2f}**
        - Fraud Percentage: **{fraud_percentage:.2f}%**
        - False Positives: **{false_positives}**
        - False Positive Cost: **${fp_cost:.2f}**
        - **Net Savings**: **${net_savings:.2f}**
        """)

        # Threshold slider
        st.sidebar.header("🔧 Threshold Tuning")
        new_threshold = st.sidebar.slider("Set fraud threshold", 0.05, 0.95, threshold, 0.01)
        if new_threshold != threshold:
            data['fraud_prediction'] = (fraud_proba >= new_threshold).astype(int)
            st.sidebar.write(f"Updated fraud predictions with threshold = {new_threshold:.2f}")
            st.sidebar.write(f"New fraud count: {data['fraud_prediction'].sum()}")

else:
    st.info("Please upload a CSV file to begin.")
    

# copy between (streamlit run "a:/work/datascince/projects/Fraud Use Case/xgb/app.py") and run 