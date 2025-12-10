import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.io_utils import load_raw_data, save_processed_data, get_missing_summary

def clean_vaccine_schedule_data():
    print("\n" + "="*60)
    print("CLEANING VACCINE SCHEDULE DATA")
    print("="*60 + "\n")
    
    df = load_raw_data('vaccine-schedule-data.csv')
    print(f"Initial shape: {df.shape}\n")
    
    get_missing_summary(df)
    df = df.drop_duplicates()
    
    print(f"\nFinal shape: {df.shape}")
    save_processed_data(df, 'schedule_clean.csv')
    print("\nVaccine schedule data cleaning completed!\n")
    return df

if __name__ == "__main__":
    clean_vaccine_schedule_data()
