import sqlite3


database = sqlite3.connect("Leopard_web_project/Database/tables.db") 
cursor = database.cursor() 

Teacher="Galileo"
Course="ARCHITECTURE"

cursor.execute(" SELECT 1 FROM COURSE WHERE INSTRUCTOR_NAME=? and COURSE_NAME=?",(Teacher,Course))

result=cursor.fetchone()

if result:
    print(f"{Teacher} is teaching {Course}")
else:
    print(f"{Teacher} not teaching {Course}")

#cursor.execute("ALTER TABLE COURSE DROP COLUMN ROASTER")
#cursor.execute("DELETE FROM STUDENT WHERE NAME='Tomasso'")
database.commit()

#Value ="""INSERT INTO COURSE(CRN,COURSE_NAME,COURSE_DAY,COURSE_TIME,INSTRUCTOR_NAME) VALUES(?,?,?,?,?)"""
#cursor.execute("DROP TABLE COURSE ")
cursor.execute("""INSERT INTO COURSE(CRN,COURSE_NAME,COURSE_DAY,COURSE_TIME,INSTRUCTOR_NAME) VALUES(158,"APLLIED PROGRAMING","M\F","7:00-8:00","Blake")""")
database.commit()
