from DBconnect import DBConnect

if __name__ == "__main__":
    try:
        DBConnect.dbconnect()
        # create table
        createTqbleSQL = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
        DBConnect.dbclose()
        