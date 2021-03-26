import psycopg2
from student import Student
from web import errors

# psycopg -- популярная библиотека, в туториале исполизовали именно ее, я решила не отступать от туториала

class DataBase:
    def __init__(self, dbname: str, username: str, pswd: str, host: str, port: str, table_name:str):
        self.dbname = dbname
        self.username = username
        self.pswd = pswd
        self.host = host
        self.port = port
        self.table_name = table_name
        self.conn = psycopg2.connect(database=self.dbname, user=self.username,
                                     password=self.pswd, host=self.host, port=self.port)
        self.cur = self.conn.cursor()
