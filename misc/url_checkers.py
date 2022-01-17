import urllib
import sqlite3


def compare_urls_to_sql(sql_path, url):
    conn = sqlite3.connect("../Data/url.db")
    c = conn.cursor()
    c.execute("""
    SELECT 
    """)


def upload_new_urls(website):
    w = website
    conn = sqlite3.connect("../Data/url.db")
    c = conn.cursor()
    c.execute(f"""
    INSERT INTO table (host, name, url, content) VALUES({w.domain}, {w.name}, {w.url}, {w.response}) ON DUPLICATE KEY UPDATE    
    name="A", age=19
    """)

