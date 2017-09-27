import MySQLdb

class DBConnect:
    def __init__(self):
        self.user = 'root'
        self.host = '0.0.0.0'
        self.password = '1234'
        self.dbname = 'test'
        self.port = 6603

    def dbconnect(self):
        self.db = MySQLdb.connect(self.host,self.user,self.password,self.dbname, self.port)
        self.cursor = self.db.cursor()

    def dbclose(self):
        self.db.close()

    def runQuery(self, sql):
        self.cursor.execute(sql)
        self.results = self.cursor.fetchall()

    def runInsert(self,sql):
        self.cursor.execute(sql)
        self.db.commit()

    def runDelete(self, sql):
        self.cursor.execute(sql)
        self.db.commit()

    def runUpdate(self, sql):
        self.cursor.execute(sql)
        self.db.commit()

    def createTable(self, table_name, sql):
        self.cursor.execute("DROP TABLE IF EXISTS %s" % table_name)
        self.cursor.execute(sql)