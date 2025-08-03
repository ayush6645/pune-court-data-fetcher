# init_db.py
import sqlite3

# Connects to the database file (creates it if not present)
conn = sqlite3.connect('queries.db')
cursor = conn.cursor()

# SQL command to create the 'queries' table with the required columns
cursor.execute('''
CREATE TABLE IF NOT EXISTS queries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    court_complex TEXT,
    case_type TEXT,
    case_number TEXT,
    case_year TEXT,
    raw_response TEXT
)
''')

print("Database 'queries.db' and table 'queries' created successfully.")

conn.commit()
conn.close()