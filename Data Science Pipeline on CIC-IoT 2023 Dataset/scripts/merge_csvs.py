import pandas as pd
from pathlib import Path
from tqdm import tqdm
import logging

from scripts.config import DATA_RAW, TRAIN_PATH, UNSEEN_PATH

# ─────────────── Logging ───────────────
logging.basicConfig(level=logging.INFO, format='%(message)s')

# ─────────────── Label Mapping ───────────────
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

def load_csvs(files):
    dfs = []
    for file in tqdm(files, desc="📥 Loading CSVs"):
        try:
            df = pd.read_csv(file)
            dfs.append(df)
            logging.info(f"✓ Loaded {file.name} (shape: {df.shape})")
        except Exception as e:
            logging.warning(f"× Skipped {file.name}: {e}")
    return pd.concat(dfs, ignore_index=True) if dfs else None

def clean_columns(df):
    df.columns = df.columns.str.lower()
    df.rename(columns={
        'protocol type': 'protocol_type',
        'tot sum': 'tot_sum',
        'tot size': 'tot_size',
        'magnitue': 'magnitude'
    }, inplace=True)
    return df

def apply_label_map(df, label_col="label"):
    df[label_col] = df[label_col].map(LABEL_MAP)
    logging.info("\n📊 Label distribution:\n" + str(df[label_col].value_counts()))
    return df

# ─────────────── Main ───────────────

def main():
    all_csvs = sorted(DATA_RAW.glob("*.csv"))
    if len(all_csvs) < 11:
        logging.error("❌ Not enough files in raw/. Need at least 11.")
        return

    train_files = all_csvs[:10]
    unseen_file = all_csvs[10]

    train_df = load_csvs(train_files)
    if train_df is not None:
        train_df = apply_label_map(clean_columns(train_df))
        TRAIN_PATH.parent.mkdir(parents=True, exist_ok=True)
        train_df.to_csv(TRAIN_PATH, index=False)
        logging.info(f"✅ Saved training data to {TRAIN_PATH}")

    try:
        unseen_df = pd.read_csv(unseen_file)
        unseen_df = apply_label_map(clean_columns(unseen_df))
        UNSEEN_PATH.parent.mkdir(parents=True, exist_ok=True)
        unseen_df.to_csv(UNSEEN_PATH, index=False)
        logging.info(f"✅ Saved unseen data to {UNSEEN_PATH}")
    except Exception as e:
        logging.error(f"× Unseen file error: {e}")

if __name__ == "__main__":
    main()
