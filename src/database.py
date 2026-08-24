import sqlite3

from src.models import Startup

def initialise_database():
    conn = sqlite3.connect('data/startups.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS startups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            overview TEXT,
            location TEXT,
            industry TEXT,
            stage TEXT,
            team TEXT,
            funding TEXT,
            description TEXT,
            url TEXT
        )
    """)

    conn.commit()
    conn.close()

def insert_startup(startup: Startup):
    conn = sqlite3.connect('data/startups.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO startups (name, overview, location, industry, stage, focus, type, team, funding, description, url) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (startup.name, startup.overview, startup.location, startup.industry, startup.stage, startup.team, startup.funding, startup.description, startup.url))

    conn.commit()
    conn.close()

def row_to_startup(row):
    return Startup (
        name=row[1],
        overview=row[2],
        location=row[3],
        industry=row[4],
        stage=row[5],
        team=row[6],
        funding=row[7],
        description=row[8],
        url=row[9]
    )

def get_startups():
    conn = sqlite3.connect('data/startups.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM startups")

    rows = cursor.fetchall()

    return [
        row_to_startup(row) for row in rows
    ]