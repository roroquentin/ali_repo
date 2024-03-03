import sqlite3

def create_database():
    conn = sqlite3.connect("cars.db")
    c = conn.cursor()
    
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS cars
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 title TEXT,
                 price TEXT,
                 year TEXT)''')
    
    conn.commit()
    conn.close()

def insert_car(title, price, year):
    conn = sqlite3.connect("cars.db")
    c = conn.cursor()
    
    # Insert data into table
    c.execute('''INSERT INTO cars (title, price, year)
                 VALUES (?, ?, ?)''', (title, price, year))
    
    conn.commit()
    conn.close()
