import pandas as pd
from pathlib import Path
from tqdm import tqdm
import logging

# ─────────────── Logging ───────────────
logging.basicConfig(level=logging.INFO, format='%(message)s')

# ─────────────── Configurable Paths ───────────────
DATASET_DIRECTORY = Path(r"A:\master\Thesis\Raw_Data\data_process\Data\data_sets\CIC-IOT-23")
TRAIN_OUTPUT_PATH = Path(r"A:\master\Thesis\Raw_Data\data_process\Data\test\train_merged.csv")
UNSEEN_OUTPUT_PATH = Path(r"A:\master\Thesis\Raw_Data\data_process\Data\test\unseen.csv")

# ─────────────── Label Map ───────────────
LABEL_MAP = {
    'DDoS-RSTFINFlood': 'DDoS', 'DDoS-PSHACK_Flood': 'DDoS', 'DDoS-SYN_Flood': 'DDoS',
    'DDoS-UDP_Flood': 'DDoS', 'DDoS-TCP_Flood': 'DDoS', 'DDoS-ICMP_Flood': 'DDoS',
    'DDoS-SynonymousIP_Flood': 'DDoS', 'DDoS-ACK_Fragmentation': 'DDoS',
    'DDoS-UDP_Fragmentation': 'DDoS', 'DDoS-ICMP_Fragmentation': 'DDoS',
    'DDoS-SlowLoris': 'DDoS', 'DDoS-HTTP_Flood': 'DDoS',
    'DoS-UDP_Flood': 'DoS', 'DoS-SYN_Flood': 'DoS', 'DoS-TCP_Flood': 'DoS', 'DoS-HTTP_Flood': 'DoS',
    'Mirai-greeth_flood': 'Mirai', 'Mirai-greip_flood': 'Mirai', 'Mirai-udpplain': 'Mirai',
    'Recon-PingSweep': 'Recon', 'Recon-OSScan': 'Recon', 'Recon-PortScan': 'Recon',
    'Recon-HostDiscovery': 'Recon', 'VulnerabilityScan': 'Recon',
    'DNS_Spoofing': 'Spoofing', 'MITM-ArpSpoofing': 'Spoofing',
    'BenignTraffic': 'Benign',
    'BrowserHijacking': 'Web_Based', 'Backdoor_Malware': 'Web_Based', 'XSS': 'Web_Based',
    'Uploading_Attack': 'Web_Based', 'SqlInjection': 'Web_Based',
    'CommandInjection': 'Web_Based', 'DictionaryBruteForce': 'Brute_Force'
}

# ─────────────── Helpers ───────────────

def load_csv_files(files):
    dfs = []
    for file in tqdm(files, desc="📂 Loading CSV files"):
        try:
            df = pd.read_csv(file)
            dfs.append(df)
            logging.info(f"✓ Loaded {file.name} (shape: {df.shape})")
        except Exception as e:
            logging.warning(f"× Failed to load {file.name}: {e}")
    return pd.concat(dfs, ignore_index=True) if dfs else None

def standardize_columns(df):
    df.columns = df.columns.str.lower()
    df.rename(columns={
        'protocol type': 'protocol_type',
        'tot sum': 'tot_sum',
        'tot size': 'tot_size',
        'magnitue': 'magnitude'  # correct known typo
    }, inplace=True)
    return df

def remap_labels(df, label_column='label'):
    df[label_column] = df[label_column].map(LABEL_MAP)
    logging.info("\n📊 Label distribution after remapping:")
    logging.info(df[label_column].value_counts())
    return df

# ─────────────── Main ───────────────

def main():
    all_files = sorted(DATASET_DIRECTORY.glob("*.csv"))
    if len(all_files) < 11:
        logging.error("❌ Not enough CSV files. Need at least 11.")
        return

    # First 10 → training set
    train_files = all_files[:10]
    # 11th → unseen set
    unseen_file = all_files[10]

    # Process training set
    train_df = load_csv_files(train_files)
    if train_df is not None:
        train_df = remap_labels(standardize_columns(train_df))
        TRAIN_OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        train_df.to_csv(TRAIN_OUTPUT_PATH, index=False)
        logging.info(f"\n✅ Saved merged training dataset: {TRAIN_OUTPUT_PATH}")

    # Process unseen set
    try:
        unseen_df = pd.read_csv(unseen_file)
        unseen_df = remap_labels(standardize_columns(unseen_df))
        UNSEEN_OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        unseen_df.to_csv(UNSEEN_OUTPUT_PATH, index=False)
        logging.info(f"✅ Saved unseen dataset: {UNSEEN_OUTPUT_PATH}")
    except Exception as e:
        logging.error(f"× Failed to process unseen file {unseen_file.name}: {e}")

if __name__ == "__main__":
    main()
