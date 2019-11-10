import sqlite3

conn = sqlite3.connect('keywords.db')

conn.row_factory = sqlite3.Row

cur = conn.cursor()

cur.execute("select * from Keyword")

rows = cur.fetchall(); 

print(rows)