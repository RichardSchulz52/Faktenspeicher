import os

import pandas as pd
import psycopg2


class Repository:

    def __init__(self) -> None:
        self.con = None
        self.cur = None

        self.host = os.environ['db_host']
        self.port = os.environ['db_port']
        self.dbname = os.environ['db_name']
        self.user = os.environ['db_user']
        self.password = os.environ['db_password']

    def save_line(self, text_, link_, extra_text_):
        self.cur.execute(
            f"INSERT INTO faktenspeicher (text, link, extra_text) VALUES ('{text_}', '{link_}', '{extra_text_}')")
        self.con.commit()

    def info_table(self):
        self.cur.execute("CREATE SCHEMA IF NOT EXISTS faktenspeicher")
        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS faktenspeicher.fakten (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                        text varchar(2000), 
                                                        link varchar(2000),
                                                        extra_text varchar(2000));
            """)
        self.con.commit()

    def search(self, text_field):
        data = self.cur.execute(f"""
            SELECT text, link, extra_text FROM fakten 
            WHERE text like '%{text_field}%'
            ORDER BY id DESC 
        """).fetchall()
        frame = pd.DataFrame(data)
        if not frame.empty:
            frame.rename(
                columns={frame.columns[0]: 'Fakt', frame.columns[1]: 'Beweis', frame.columns[2]: 'Erläuterung'},
                inplace=True)
        return frame

    def open_db(self):
        self.con = psycopg2.connect(host=self.host,
                                    port=self.port,
                                    dbname=self.dbname,
                                    user=self.user,
                                    password=self.password)
        self.cur = self.con.cursor()
        self.info_table()
