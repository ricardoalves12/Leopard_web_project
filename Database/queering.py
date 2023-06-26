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


  


