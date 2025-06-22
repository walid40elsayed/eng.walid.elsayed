import os
import pandas as pd
from tqdm import tqdm
import logging

# ─────────────── Logging Setup ───────────────
logging.basicConfig(level=logging.INFO, format='%(message)s')

# ─────────────── Configuration ───────────────
DATASET_DIRECTORY = r'A:\master\Thesis\Raw_Data\data_process\Data\data_sets\CIC-IOT-23' # change for your own path
OUTPUT_PATH = r'A:\master\Thesis\Raw_Data\data_process\Data\test\new_2.csv' # change for your own path
MAX_FILES = 10  # Adjust for how many files to merge

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

# ─────────────── Functions ───────────────

def load_and_merge_csvs(directory, max_files=None):
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    if max_files:
        csv_files = csv_files[:max_files]
    
    data_frames = []
    for file in tqdm(csv_files, desc='📂 Loading CSV files'):
        path = os.path.join(directory, file)
        try:
            df = pd.read_csv(path)
            data_frames.append(df)
            logging.info(f"✓ Loaded {file} (shape: {df.shape})")
        except Exception as e:
            logging.warning(f"× Failed to load {file}: {e}")
    
    if not data_frames:
        logging.error("❌ No valid dataframes to merge.")
        return None

    combined = pd.concat(data_frames, ignore_index=True)
    logging.info(f"\n🔗 Merged dataset shape: {combined.shape}")
    return combined

def standardize_columns(df):
    df.columns = df.columns.str.lower()
    df.rename(columns={
        'protocol type': 'protocol_type',
        'tot sum': 'tot_sum',
        'tot size': 'tot_size',
        'magnitue': 'magnitude'  # known typo in raw data
    }, inplace=True)
    return df

def remap_labels(df, label_column='label'):
    df[label_column] = df[label_column].map(LABEL_MAP)
    logging.info("\n📊 Label distribution after remapping:")
    logging.info(df[label_column].value_counts())
    return df

def main():
    df = load_and_merge_csvs(DATASET_DIRECTORY, MAX_FILES)
    if df is not None:
        df = standardize_columns(df)
        df = remap_labels(df, label_column='label')
        df.to_csv(OUTPUT_PATH, index=False)
        logging.info(f"\n✅ Merged dataset saved to: {OUTPUT_PATH}")

# ─────────────── Entry Point ───────────────
if __name__ == "__main__":
    main()
