import MySQLdb

class DBConn:
    def __init__(self):
        self.user = 'root'
        self.host = '0.0.0.0'
        self.password = '1234'
        self.dbname = 'test'
        self.port = 6603

    def dbconnect(self):
        try:
            self.db = MySQLdb.connect(self.host,self.user,self.password,self.dbname, self.port)
            self.cursor = self.db.cursor()

        except MySQLdb.Error as e:
            print "Error %d: %s" % (e.args[0], e.args[1])

    def dbclose(self):
        try:
            self.db.close()
        
        except MySQLdb.Error as e:
            print "Error %d: %s" % (e.args[0], e.args[1])

    def runQuery(self, sql):
        try:
            self.cursor.execute(sql)
            self.results = self.cursor.fetchall()

        except MySQLdb.Error as e:
            self.db.rollback()
            print "Error %d: %s" % (e.args[0], e.args[1])

    def runInsert(self,sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except MySQLdb.Error as e:
            self.db.rollback()
            print "Error %d: %s" % (e.args[0], e.args[1])

    def runDelete(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except MySQLdb.Error as e:
            self.db.rollback()
            print "Error %d: %s" % (e.args[0], e.args[1])

    def runUpdate(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except MySQLdb.Error as e:
            self.db.rollback()
            print "Error %d: %s" % (e.args[0], e.args[1])

    def createTable(self, table_name, sql):
        try:
            self.cursor.execute("DROP TABLE IF EXISTS %s" % table_name)
            self.cursor.execute(sql)

        except MySQLdb.Error as e:
            self.db.rollback()
            print "Error %d: %s" % (e.args[0], e.args[1])