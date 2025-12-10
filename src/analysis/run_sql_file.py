import psycopg2

def run_sql_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        sql = f.read()

    conn = psycopg2.connect(
        host="localhost",
        database="vaccination_db",   # apna DB naam
        user="postgres",             # apna username
        password="Shreya@26",    # apna password
        port=5432
    )

    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

    cur.close()
    conn.close()
    print(f"✅ Executed: {path}")

if __name__ == "__main__":
    # 1) Easy queries
    run_sql_file("src/analysis/easy_questions.sql")

    # 2) Medium queries
    run_sql_file("src/analysis/medium_questions.sql")

    # 3) Advanced / scenario queries
    run_sql_file("src/analysis/scenario_queries.sql")
