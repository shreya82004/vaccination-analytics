import pandas as pd
import os

def load_raw_data(filename):
    filepath = os.path.join('data', 'raw', filename)
    print(f"Loading data from {filepath}...")
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} rows and {len(df.columns)} columns")
    return df

def save_processed_data(df, filename):
    filepath = os.path.join('data', 'processed', filename)
    df.to_csv(filepath, index=False)
    print(f"Saved {len(df)} rows to {filepath}")

def get_missing_summary(df):
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print(f"\nMissing values found: {missing.sum()}")
    else:
        print("\nNo missing values!")
    return missing
