import time
import os
import psycopg2

class postgres:
    def __init__(self):
        pass

    def connect(self) -> psycopg2:
        host = os.environ.get('postgres-host')
        database = os.environ.get('postgres-database')
        user = os.environ.get('postgres-user')
        password = os.environ.get('postgres-password')
        conn = psycopg2.connect(dbname=database, user=user, password=password, host=host)
        self.conn = conn
    
    def write(self, payload):
        if self.conn is None:
            self.connect()
        cur = self.conn.cursor()
        query = f"INSERT INTO temperature (room, value) VALUES ('{payload.get('room','office')}',{payload.get('value','0')});"
        cur.execute(query)
        self.conn.commit()
        cur.close()

    def close(self):
        if self.conn is not None:
            self.conn.close()
			