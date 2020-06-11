import sqlite3

conn = sqlite3.connect("data.db")
c = conn.cursor()

c.execute("SELECT * FROM data")
print(c.fetchall())

conn.close()
