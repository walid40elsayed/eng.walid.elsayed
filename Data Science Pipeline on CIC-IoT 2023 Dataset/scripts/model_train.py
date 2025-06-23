import argparse
import joblib
import os
import time
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder

from config import CLEANED_TRAIN, MODEL_PATH
from model_utils import log_metrics, clean_memory

def parse_args():
    parser = argparse.ArgumentParser(description="Train a Random Forest model on IoT data")
    parser.add_argument("--data", type=str, default=CLEANED_TRAIN, help="Path to cleaned training data")
    parser.add_argument("--model", type=str, default=MODEL_PATH, help="Path to save model")
    return parser.parse_args()

def load_and_preprocess(path):
    df = pd.read_csv(path)
    df['label'] = df['label'].astype('category')
    features = df.drop('label', axis=1).astype(np.float32)

    scaler = StandardScaler()
    features_scaled = pd.DataFrame(scaler.fit_transform(features), columns=features.columns)
    encoded = pd.concat([features_scaled, df['label']], axis=1)
    clean_memory()
    return encoded

def apply_smote(df):
    from imblearn.over_sampling import SMOTE
    X = df.drop(columns='label')
    y = df['label']
    smote = SMOTE(random_state=42)
    X_res, y_res = smote.fit_resample(X, y)
    df_resampled = pd.DataFrame(X_res, columns=X.columns)
    df_resampled['label'] = y_res
    return df_resampled

def train_rf_model(X_train, y_train):
    model = RandomForestClassifier(
        n_estimators=75,
        class_weight='balanced',
        oob_score=True,
        min_samples_split=5,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)
    print(f"🌲 OOB Score: {model.oob_score_:.4f}")
    scores = cross_val_score(model, X_train, y_train, cv=5)
    print(f"✅ CV Accuracy: {scores.mean():.4f} ± {scores.std():.4f}")
    return model

if __name__ == "__main__":
    args = parse_args()
    df = load_and_preprocess(args.data)

    print("📊 Class distribution before SMOTE:")
    print(df['label'].value_counts())

    resampled = apply_smote(df)

    print("\n📈 Class distribution after SMOTE:")
    print(resampled['label'].value_counts())

    encoder = LabelEncoder()
    resampled['label'] = encoder.fit_transform(resampled['label'])

    X = resampled.drop('label', axis=1)
    y = resampled['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

    model = train_rf_model(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = np.mean(y_pred == y_test)
    f1 = cross_val_score(model, X_test, y_test, cv=3, scoring='f1_macro').mean()

    log_metrics(acc, f1)
    os.makedirs(os.path.dirname(args.model), exist_ok=True)
    joblib.dump(model, args.model)

    # Check model size
    model_size_kb = os.path.getsize(MODEL_PATH) / 1024
    print(f"🧠 Model size: {model_size_kb:.2f} KB")

    # Measure inference time
    start = time.time()
    _ = model.predict(X_test[:1])
    print(f"⚡ Inference Time: {(time.time() - start)*1000:.2f} ms")

    print(f"\n✅ Model saved to: {args.model}")
