import sqlite3

conn = sqlite3.connect('Melona restaurant.db')
c = conn.cursor()

conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        ''')

conn.close()