import mysql.connector


class DbHelper:

    conn = None
    dbname = None
    host = None
    password = None
    user = None

    def __init__(self, user, host, password, dbname):
        self.user = user
        self.host = host
        self.password = password
        self.dbname = dbname

        if self.conn is not None:
            self.close()

        self.conn = mysql.connector.connect(host=host, user=user, password=password, database=dbname,
                                            autocommit=True, buffered=True)

    def fetch_records(self, sql):
        cursor = self.get_cursor()
        cursor.execute(sql)

        try:
            results = cursor.fetchall()
        except:
            results = ()
            pass

        return results

    def execute_query(self, sql, params):
        cursor = self.get_cursor()

        try:
            cursor.execute(sql, params)
            res = cursor.lastrowid
        except:
            res = False
            pass

        return res

    def is_connected(self):
        return self.conn.is_connected()

    def close(self):
        return self.conn.close()

    def get_cursor(self):
        self.conn.reconnect()

        return self.conn.cursor(buffered=True, dictionary=True)
