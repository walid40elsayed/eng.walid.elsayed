from pathlib import Path

# 📁 Project root (adjust if needed)
BASE_DIR = Path(__file__).resolve().parent.parent

# 📂 Data directories
DATA_RAW       = r'.\data_sets\CIC-IOT-23' # change for your own path
DATA_PROCESSED = r'.\test' # change for your own path

# 📄 Input/output files
TRAIN_PATH     = r'.\test\new_2.csv' # change for your own path
UNSEEN_PATH    = r'.\test\unseen.csv' # change for your own path
CLEANED_TRAIN  = r'.\test\cleaned_data_2.csv' # change for your own path
CLEANED_UNSEEN = r'.\test\unseen_cleaned.csv' # change for your own path

# 📁 Other useful directories
VISUALS_DIR    = BASE_DIR / "outputs" / "visualizations"
MODELS_DIR     = BASE_DIR / "models"
