import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.io_utils import load_raw_data, save_processed_data, get_missing_summary

def clean_coverage_data():
    print("\n" + "="*60)
    print("CLEANING COVERAGE DATA")
    print("="*60 + "\n")
    df = load_raw_data('coverage-data.csv')

    print(f"Initial shape: {df.shape}\n")
    
    get_missing_summary(df)
    
    df = df.drop_duplicates()
    
    print(f"\nFinal shape: {df.shape}")
    save_processed_data(df, 'coverage_clean.csv')
    print("\nCoverage data cleaning completed!\n")
    return df

if __name__ == "__main__":
    clean_coverage_data()
