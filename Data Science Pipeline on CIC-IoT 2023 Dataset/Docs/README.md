 # 🧠 Data Science Pipeline on CIC-IoT 2023 Dataset

This project is a complete, production-ready **data science and analysis pipeline** for multiclass classification on IoT network traffic data. While the dataset originates from the cybersecurity domain, the project emphasizes **feature selection**, **data balancing**, **modeling**, and **interpretability**—making it a strong portfolio piece for any aspiring data scientist.

---

## 📌 Project Highlights

- Clean preprocessing pipeline for large structured datasets
- Exploratory and statistical data analysis (EDA)
- Feature engineering using importance and correlation
- Balanced modeling using SMOTE
- Hyperparameter tuning and model optimization
- Beautiful visualizations for insights and communication

---

## 🗃️ Dataset Summary

- **Source**: [CIC IoT 2023 - Official Website](https://www.unb.ca/cic/datasets/iot-2023.html)
- **Features**: 45+ numeric and protocol-based network attributes
- **Target**: 8 multiclass labels (representing different traffic behaviors)
- **Files Used**: 10 files (80% train + 20% test) + 1 file as unseen for prediction

---

## 📁 Data Availability

To keep the repository lightweight, output files (merged data, cleaned CSVs, models, and visualizations) are excluded from version control.

- 📥 **Raw Dataset**: Download from [CIC-IoT 2023 Official Site](https://www.unb.ca/cic/datasets/iot-2023.html)
- 🛠 **To reproduce**: Run the scripts inside the `/scripts` folder:
  - `merge_csvs.py` → Merges and remaps raw files
  - `01_feature_selection.ipynb` → Drops redundant features
  - `02_modeling_evaluation.ipynb` → Trains and evaluates model

 ---

## 🔧 Workflow

### 🧹 1. Data Cleaning
- Merged multiple raw CSVs
- Handled nulls, duplicates, and inconsistent values

### 📊 2. Exploratory Data Analysis (EDA)
- Feature importance via Random Forest
- Correlation with target (ANOVA F-Score / Cramér’s V)
- Visual heatmap of inter-feature correlation

### ✂️ 3. Feature Selection
- Dropped features with zero predictive power
- Removed one from each highly correlated feature pair based on relative target impact

### 🔄 4. Transformation
- Label encoding for categorical variables
- Scaling with MinMaxScaler
- Applied SMOTE to handle class imbalance

### 🤖 5. Modeling
- Split data into 80/20 train-test
- Trained models (Random Forest) with GridSearchCV for hyperparameter tuning

### 📈 6. Evaluation
- Accuracy, precision, recall, F1 Score (macro/weighted)
- Visualizations:
  - Feature importance (before & after selection)
  - Heat map for correlation
  - Class distribution
  - Confusion matrix
  - ROC & PR curves
  - Learning curves
  - Calibration curves
  - Accuracy, precision, recall, F1 Score (macro/weighted)

---

### 🗂️ 7. Project Structure

Data Since Pipeline/
├── data/
│   ├── raw/             # Raw CIC-IoT 2023 CSVs
│   ├── processed/       # Merged & cleaned files
│   └── unseen/          # Unseen file for testing
│
├── notebooks/
│   ├── 01_feature_selection.ipynb
│   └── 02_modeling_evaluation.ipynb
│
├── scripts/
│   ├── merge_csvs.py
│   ├── predict.py
│   ├── helpers.py
│   └── config.py
│
├── models/                # Trained model files (e.g., joblib or pkl)
├── outputs/
│   └── visualizations/    # Saved PNGs of heatmaps, feature bars, etc.
│
├── docs/                  # MkDocs documentation if applicable
├── requirements.txt
├── README.md
└── LICENSE


---

### 📊 8. Sample Results

| Metric     | Value (Weighted Avg) |
|------------|----------------------|
| Accuracy   | 99.91%               |
| Precision  | 99.91%               |
| Recall     | 99.91%               |
| F1 Score   | 99.91%               |

*Results will vary based on feature selection and model.*

---

### 🚀 9. Getting Started

Clone the repository and install required packages:


## 🧑‍💻 10. About the Author
Walid is a data scientist focused on building interpretable, production-ready machine learning systems. His passion lies in making technical workflows accessible and transparent through visualization, thoughtful design, and reproducibility. He blends deep curiosity with a methodical mindset to extract meaning from data—one line of Python at a time.
“This project reflects my belief that clean data pipelines and clear results speak louder than hype. Strong modeling starts with understanding—and that begins with analysis.”

---

### 📄 11. License
This project is licensed under the MIT License. See the LICENSE file for details.
