import sqlite3

class Connection:
    def connection_sqlite3(self):
        try:
            conn = sqlite3.connect('state.db')
            cursor = conn.cursor()
            return cursor, conn
        except Exception as error:
            raise error