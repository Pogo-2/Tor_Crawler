import sqlite3

conn = sqlite3.connect("./url.db")
c = conn.cursor()

c.execute("""
CREATE TABLE website(
hostname text,
title text,
url text,
content blob

)
""")

conn.commit()
conn.close()
