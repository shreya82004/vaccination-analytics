import os
import sys
import pandas as pd
from sqlalchemy import create_engine

# project root ko path me add
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import get_connection_string


def load_table(csv_path, table_name):
    """Generic loader for simple tables where CSV columns == table columns."""
    conn_str = get_connection_string()
    engine = create_engine(conn_str)

    print(f"\nLoading {csv_path} -> {table_name} ...")
    df = pd.read_csv(csv_path)
    print(f"  Rows: {len(df)}, Columns: {len(df.columns)}")

    df.to_sql(table_name, engine, if_exists='append', index=False)
    print(f"  ✅ Loaded into table: {table_name}")


print(">>> load_data.py START")


def main():
    base = os.path.join('data', 'processed')

    conn_str = get_connection_string()
    engine = create_engine(conn_str)

    # 1) COVERAGE
    df_cov = pd.read_csv(os.path.join(base, 'coverage_clean.csv'))
    df_cov = df_cov.rename(columns={
        'CODE': 'code',
        'NAME': 'name',
        'YEAR': 'year',
        'ANTIGEN': 'antigen',
        'COVERAGE': 'coverage',
        'TARGET_NUMBER': 'target_number',
        'DOSES': 'doses'
    })
    df_cov = df_cov[['code', 'name', 'year', 'antigen', 'coverage', 'target_number', 'doses']]

    print("\nLoading coverage_clean.csv -> coverage ...")
    print(f"  Rows: {len(df_cov)}, Columns: {len(df_cov.columns)}")
    df_cov.to_sql('coverage', engine, if_exists='append', index=False)
    print("  ✅ Loaded into table: coverage")

    # 2) INCIDENCE
    df_inc = pd.read_csv(os.path.join(base, 'incidence_clean.csv'))
    df_inc = df_inc.rename(columns={
        'CODE': 'code',
        'NAME': 'name',
        'YEAR': 'year',
        'DISEASE': 'disease',
        'INCIDENCE_RATE': 'incidence_rate'
    })
    df_inc = df_inc[['code', 'name', 'year', 'disease', 'incidence_rate']]

    print("\nLoading incidence_clean.csv -> incidence ...")
    print(f"  Rows: {len(df_inc)}, Columns: {len(df_inc.columns)}")
    df_inc.to_sql('incidence', engine, if_exists='append', index=False)
    print("  ✅ Loaded into table: incidence")

    # 3) REPORTED CASES
    df_rep = pd.read_csv(os.path.join(base, 'reported_clean.csv'))
    df_rep = df_rep.rename(columns={
        'CODE': 'code',
        'NAME': 'name',
        'YEAR': 'year',
        'DISEASE': 'disease',
        'CASES': 'cases'
    })
    df_rep = df_rep[['code', 'name', 'year', 'disease', 'cases']]

    print("\nLoading reported_clean.csv -> reported_cases ...")
    print(f"  Rows: {len(df_rep)}, Columns: {len(df_rep.columns)}")
    df_rep.to_sql('reported_cases', engine, if_exists='append', index=False)
    print("  ✅ Loaded into table: reported_cases")

    # 4) VACCINE INTRODUCTION
       # 4) VACCINE INTRODUCTION
    df_intro = pd.read_csv(os.path.join(base, 'intro_clean.csv'))
    df_intro = df_intro.rename(columns={
        'ISO_3_CODE': 'code',
        'COUNTRYNAME': 'country',
        'WHO_REGION': 'region',
        'YEAR': 'year',
        'DESCRIPTION': 'description',
        'INTRO': 'introduced'
    })
    df_intro = df_intro[['code', 'country', 'region', 'year', 'description', 'introduced']]

    print("\nLoading intro_clean.csv -> vaccine_introduction ...")
    print(f"  Rows: {len(df_intro)}, Columns: {len(df_intro.columns)}")
    df_intro.to_sql('vaccine_introduction', engine, if_exists='append', index=False)
    print("  ✅ Loaded into table: vaccine_introduction")


    # 5) VACCINE SCHEDULE
         # 5) VACCINE SCHEDULE
    df_sched = pd.read_csv(os.path.join(base, 'schedule_clean.csv'))

    # Extra metadata rows remove karo: jahan ISO_3_CODE 3 letters nahi hai
    df_sched = df_sched[df_sched['ISO_3_CODE'].str.len() == 3]

    df_sched = df_sched.rename(columns={
        'ISO_3_CODE': 'code',
        'COUNTRYNAME': 'country',
        'WHO_REGION': 'region',
        'YEAR': 'year',
        'VACCINECODE': 'vaccine_code',
        'VACCINE_DESCRIPTION': 'vaccine_description',
        'SCHEDULEROUNDS': 'schedule_rounds',
        'TARGETPOP': 'target_pop',
        'TARGETPOP_DESCRIPTION': 'target_pop_description',
        'GEOAREA': 'geo_area',
        'AGEADMINISTERED': 'age_administered',
        'SOURCECOMMENT': 'source_comment'
    })
    df_sched = df_sched[['code', 'country', 'region', 'year',
                         'vaccine_code', 'vaccine_description',
                         'schedule_rounds', 'target_pop', 'target_pop_description',
                         'geo_area', 'age_administered', 'source_comment']]

    print("\nLoading schedule_clean.csv -> vaccine_schedule ...")
    print(f"  Rows after filter: {len(df_sched)}, Columns: {len(df_sched.columns)}")
    df_sched.to_sql('vaccine_schedule', engine, if_exists='append', index=False)
    print("  ✅ Loaded into table: vaccine_schedule")


if __name__ == "__main__":
    main()
