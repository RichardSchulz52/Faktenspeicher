import os

import pandas as pd
import psycopg2
import sqlalchemy


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
        line = pd.DataFrame({'text': [text_], 'link': [link_], 'extra_text': [extra_text_]})
        line.to_sql("faktenspeicher.faktenspeicher", self.con, if_exists="append")

    def search(self, text_field):
        frame = pd.read_sql(f"""
            SELECT text, link, extra_text FROM faktenspeicher.fakten 
            WHERE text like '%{text_field}%'
            ORDER BY id DESC 
        """, self.con)
        if not frame.empty:
            frame.rename(
                columns={frame.columns[0]: 'Fakt', frame.columns[1]: 'Beweis', frame.columns[2]: 'Erläuterung'},
                inplace=True)
        return frame

    def open_db(self):
        self.con = self.get_engine()

    def get_engine(self) -> sqlalchemy.engine:
        pg_connection_dict = {
            'dbname': self.dbname,
            'user': self.user,
            'password': self.password,
            'port': self.port,
            'host': self.host
        }
        return sqlalchemy.create_engine(**pg_connection_dict)
