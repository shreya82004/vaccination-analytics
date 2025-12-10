# vaccination-analytics
Vaccination data analysis with Python, SQL, and Power BI
# Global Vaccination Analytics

End-to-end analytics project on WHO global vaccination data (2000–2023) using PostgreSQL, Python, SQL, and Power BI.  
The goal is to understand vaccination coverage trends, regional inequalities, and how close countries are to WHO targets.

---

## 🔍 1. Project Overview

This project implements a complete analytics pipeline:

- Raw WHO vaccination CSVs → Python cleaning scripts → PostgreSQL database  
- Advanced SQL queries for trends, inequality, and country rankings  
- Jupyter notebooks for EDA and statistical analysis  
- Power BI dashboard for interactive exploration

Business questions:

- How has vaccination coverage evolved over the last two decades?
- Which regions and countries lag behind WHO’s 95% coverage target?
- How unequal is coverage within each WHO region?
- Which countries consistently achieve high coverage for key vaccines (DTP3, MCV1, POL3)?

---

## 🛠 2. Tech Stack

- **Database:** PostgreSQL  
- **ETL & Analysis:** Python (pandas, psycopg2, SQLAlchemy)  
- **Visualization:** Jupyter Notebook (Matplotlib, Seaborn), Power BI  
- **Tools:** VS Code, pgAdmin, Git, GitHub  

---

## 📁 3. Folder Structure

vaccination-analytics/
│
├─ data/
│ ├─ raw/ # Original WHO CSVs
│ └─ processed/ # Cleaned CSVs used for loading into DB
│
├─ notebooks/
│ ├─ 01_eda_coverage.ipynb # Coverage table EDA
│ ├─ 02_eda_disease_trends.ipynb # Time-series & regional trends
│ └─ 03_feature_analysis_questions.ipynb # Advanced SQL-based analysis
│
├─ src/
│ ├─ config.py
│ ├─ utils/
│ │ ├─ io_utils.py
│ │ └─ eda_utils.py
│ ├─ data_cleaning/ # Cleaning scripts for each raw file
│ ├─ database/
│ │ ├─ db_connection.py
│ │ ├─ schema.sql # PostgreSQL table definitions
│ │ └─ load_data.py # Loads processed CSVs into PostgreSQL
│ └─ analysis/
│ ├─ easy_questions.sql # Basic SQL queries
│ ├─ medium_questions.sql # Intermediate SQL
│ └─ scenario_queries.sql # Advanced SQL (CTEs, window functions, rankings)
│
├─ powerbi/
│ ├─ Vaccination_Dashboard.pbix # Multi-page Power BI report
│ └─ data_model_notes.md
│
├─ docs/
│ ├─ requirements.md
│ ├─ architecture.md
│ ├─ data_dictionary.md
│ └─ project_report.md
│
├─ .env
├─ requirements.txt
└─ README.md

---

## 🚀 4. How to Run

### 4.1. Setup environment


