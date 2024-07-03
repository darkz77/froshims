import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
# cur.execute("CREATE TABLE movie(title, year, score)")
cur.execute("""
    INSERT INTO movie VALUES 
        ('Harry Potter', 2024, 9.4)
""")
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()
res = cur.execute(("SELECT title FROM movie"))
res.fetchall()

for row in cur.execute("SELECT year, title, score FROM movie ORDER BY year"):
    print(row)