import sqlite3

database = sqlite3.connect("Documents/LeoRepo/Leopard_web_project/Database/tables.db") 
cursor = database.cursor() 

# sql_command = """ DELETE FROM INSTRUCTOR  WHERE ID =20004;"""
# cursor.execute(sql_command) 

# sql_command= """ UPDATE ADMIN SET TITLE = 'Vice President' WHERE ID = 30002;"""
# cursor.execute(sql_command) 

# sql_command="""INSERT INTO STUDENT  VALUES(10012, 'Dom', 'Smith', 2023,'BSCO','Dommi');"""


# sql_command="""INSERT INTO STUDENT  VALUES(10011, 'Jimbo', 'Low', 2023,'BSCO','Jimlo');"""


# sql_command= """ CREATE TABLE AUTHENTIFY(
#  PASSWORD TEXT  NOT NULL,
#  USERNAME TEXT NOT NULL,
#  USER_ID INTERGER NOT NULL
#  PRIMARY KEY 
# );"""

# sql_command = """INSERT INTO  AUTHENTIFY VALUES('Youtchouch', 'JimL' , 10011);"""
# cursor.execute(sql_command) 
# sql_command = """INSERT INTO  AUTHENTIFY VALUES('YourSista', 'DomS' , 10012);"""
# cursor.execute(sql_command) 
# sql_command = """INSERT  INTO AUTHENTIFY VALUES('GOOGLE ','MichaelF',10009);"""

#sql_command="""CREATE TABLE SCHEDULE(
"""ID INTERGER NOT NULL ,
    ST_NAME TEXT NOT NULL,
    CRN INTERGER NOT NULL,
    COURSE TEXT NOT NULL,
    S_DAY TEXT NOT NULL,
    E_DAY TEXT NOT NULL,
    S_TIME INTERGER NOT NULL,
    E_TIME INTERGER NOT NULL,
    T_NAME TEXT NOT NULL"""
    #);"""
#cursor.execute(sql_command)
sql_command="""CREATE TABLE COURSE (
    CRN INTERGER NOT NULL PRIMARY KEY,
    C_NAME TEXT NOT NULL,
    S_DAY TEXT NOT NULL,
    E_DAY TEXT NOT NULL,
    S_TIME INTERGER NOT NULL,
    E_TIME INTERGER NOT NULL,
    T_NAME TEXT NOT NULL);"""


cursor.execute(sql_command)
database.commit() 
database.close()