import gc
import datetime
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

# ───────────────────── Memory + Logging ─────────────────────

def clean_memory():
    gc.collect()

def log_metrics(acc, f1, log_path=r'.\test\training_log.csv'):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a") as log_file:
        log_file.write(f"{timestamp}, Accuracy: {acc:.4f}, F1: {f1:.4f}\n")

# ───────────────────── Preprocessing ─────────────────────

def load_and_preprocess(path):
    df = pd.read_csv(path)
    df['label'] = df['label'].astype('category')
    features = df.drop('label', axis=1).astype(np.float32)

    scaler = StandardScaler()
    scaled = pd.DataFrame(scaler.fit_transform(features), columns=features.columns)
    processed = pd.concat([scaled, df['label']], axis=1)

    clean_memory()
    return processed

# ───────────────────── Balancing ─────────────────────

def apply_smote(df):
    X = df.drop(columns='label')
    y = df['label']
    smote = SMOTE(random_state=42)
    X_res, y_res = smote.fit_resample(X, y)

    resampled = pd.DataFrame(X_res, columns=X.columns)
    resampled['label'] = y_res
    return resampled
