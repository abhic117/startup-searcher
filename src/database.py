import sqlite3
import pandas as pd

def initialise_database():
    conn = sqlite3.connect('startups.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS startups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            overview TEXT,
            location TEXT,
            industry TEXT,
            stage TEXT,
            focus TEXT,
            type TEXT,
            team TEXT,
            funding TEXT,
            description TEXT,
            url TEXT
        )
    """)

    conn.commit()
    conn.close()

def insert_startup(startup):
    conn = sqlite3.connect('startups.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO startups (name, overview, location, industry, stage, focus, type, team, funding, description, url) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (startup["name"], startup["overview"], startup["location"], startup["industry"], startup["stage"], startup["focus"], startup["type"], startup["team"], startup["funding"], startup["description"], startup["url"]))

    conn.commit()
    conn.close()

def database_to_dataframe():
    conn = sqlite3.connect('startups.db')

    query = "SELECT * FROM startups"

    df = pd.read_sql_query(query, conn)

    return df