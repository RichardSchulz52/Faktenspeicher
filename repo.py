import pandas as pd
import sqlite3
from sqlite3 import Cursor


def save_line(text_, link_, extra_text_):
    con = sqlite3.connect("info.db")
    cur = con.cursor()
    info_table(cur, con)
    cur.execute(f"INSERT INTO information (text, link, extra_text) VALUES ('{text_}', '{link_}', '{extra_text_}')")
    con.commit()
    cur.close()
    con.close()


def info_table(cur, con):
    cur.execute("""
            CREATE TABLE IF NOT EXISTS information (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                    text varchar(2000), 
                                                    link varchar(2000),
                                                    extra_text varchar(2000));
        """)
    con.commit()


def search(text_field):
    con = sqlite3.connect("info.db")
    cur: Cursor = con.cursor()
    info_table(cur, con)
    data = cur.execute(f"""
        SELECT text, link, extra_text FROM information 
        WHERE text like '%{text_field}%'
        ORDER BY id DESC 
    """).fetchall()
    frame = pd.DataFrame(data)
    if not frame.empty:
        frame.rename(columns={frame.columns[0]: 'Fakt', frame.columns[1]: 'Beweis', frame.columns[2]: 'Erläuterung'}, inplace=True)
    return frame
