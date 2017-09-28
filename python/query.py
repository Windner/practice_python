from DBconnect import DBConn

if __name__ == "__main__":
    
    db_use = DBConn()
    db_use.dbconnect()
    # create table
    createTqbleSQL = """CREATE TABLE EMPLOYEE (
        FIRST_NAME  CHAR(20) NOT NULL,
        LAST_NAME  CHAR(20),
        AGE INT,  
        SEX CHAR(1),
        INCOME FLOAT )"""
    db_use.createTable("EMPLOYEE", createTqbleSQL)

    InsertSQL = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

    db_use.runInsert(InsertSQL)

    UpdateSQL = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')

    db_use.runUpdate(UpdateSQL)
    
    db_use.dbclose()
        
    