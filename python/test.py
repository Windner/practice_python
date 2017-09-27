import sys
import MySQLdb

def main():
    check_mysql_version()

# def connect_mysql:
    
def check_mysql_version():
    try:
        db = MySQLdb.connect("0.0.0.0","root","1234","test",6603)
        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print "Database version : %s " % data
        db.close()

    except MySQLdb.Error as e:
        print "Error %d: %s" % (e.args[0], e.args[1])
    
def query_mysql():
    print "query_mysql"

def update_mysql():
    print "update_mysql======================"
    try:
        db = MySQLdb.connect("0.0.0.0","root","1234","test",6603)
        cursor = db.cursor()

        sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
        print sql

        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

        db.close()

    except MySQLdb.Error as e:
        print "Error %d: %s" % (e.args[0], e.args[1])

def delete_mysql():
    print "delete_mysql======================"
    try:
        db = MySQLdb.connect("0.0.0.0","root","1234","test",6603)
        cursor = db.cursor()

        sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
        print sql

        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

        db.close()

    except MySQLdb.Error as e:
        print "Error %d: %s" % (e.args[0], e.args[1])

def create_mysql():
    print "create_mysql======================"
    try:
        db = MySQLdb.connect("0.0.0.0","root","1234","test",6603)
        cursor = db.cursor()

        sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
        print sql

        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

        db.close()

    except MySQLdb.Error as e:
        print "Error %d: %s" % (e.args[0], e.args[1])

def create_table():
    print "create_table======================"
    try:
        db = MySQLdb.connect("0.0.0.0","root","1234","test",6603)
        cursor = db.cursor()
        cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

        sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
       
        cursor.execute(sql)    
        db.close()

    except MySQLdb.Error as e:
        print "Error %d: %s" % (e.args[0], e.args[1])

def query_table(table_name):
    print "print table======================"
    try:
        db = MySQLdb.connect("0.0.0.0","root","1234","test",6603)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM %s" % (table_name))
        results = cursor.fetchall()
        count = cursor.rowcount
        #for row in results:
        #    name = row[0]
        #    employ_id = row[1]
        #    recordtime = row[2]
        if count > 0:
            #print results
            for row in results:
                name = row[0]
                lname = row[1]
                age = row[2]
                sex = row[3]
                income = row[4]

            #print "Name: %s, Employ_id: %s, RecordTime: %s" % (name, employ_id, recordtime)
            print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % (name, lname, age, sex, income )
        else:
            print "table is empty"

        db.close()

    except MySQLdb.Error as e:
        print "Error %d: %s" % (e.args[0], e.args[1])

if __name__ == "__main__":
    main()
    create_table()
    create_mysql()
    query_table("EMPLOYEE")
    update_mysql()
    query_table("EMPLOYEE")
    delete_mysql()
    query_table("EMPLOYEE")