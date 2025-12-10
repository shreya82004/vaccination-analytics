import pandas as pd
import os

def load_raw_data(filename):
    filepath = os.path.join('data', 'raw', filename)
    print(f"Loading data from {filepath}...")
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df):,} rows and {len(df.columns)} columns")
    return df

def save_processed_data(df, filename):
    filepath = os.path.join('data', 'processed', filename)
    df.to_csv(filepath, index=False)
    print(f"Saved {len(df):,} rows to {filepath}")

def get_missing_summary(df):
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    
    missing_df = pd.DataFrame({
        'Column': missing.index,
        'Missing_Count': missing.values,
        'Missing_Percentage': missing_pct.values
    })
    
    missing_df = missing_df[missing_df['Missing_Count'] > 0].sort_values(
        'Missing_Count', ascending=False
    )
    
    if len(missing_df) > 0:
        print("\nMissing Values Summary:")
        print(missing_df.to_string(index=False))
    else:
        print("\nNo missing values found!")
    
    return missing_df
