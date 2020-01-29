import pandas as pd
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
  )

mycursor = mydb.cursor(buffered=True)
mycursor.execute("CREATE DATABASE IF NOT EXISTS University")
mycursor.execute("USE University")
mycursor.execute("CREATE TABLE IF NOT EXISTS Grades (student_id VARCHAR(255) PRIMARY KEY, grade VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Students (student_id VARCHAR(255) PRIMARY KEY, department VARCHAR(255), class VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Instructor (instructor_id VARCHAR(255) PRIMARY KEY, name VARCHAR(255), class VARCHAR(255))")
sql1 = "INSERT INTO Grades (student_id, grade) VALUES (%s, %s)"
sql2 = "INSERT INTO Students (student_id, department, class) VALUES (%s, %s, %s)"
sql3 = "INSERT INTO Instructor (instructor_id, name, class) VALUES (%s, %s, %s)"
Instructors = pd.read_csv ("instructors.csv") 
Students = pd.read_csv ("students.csv")
Grades = pd.read_csv ("grades.csv")

for record1 in Grades.values:
 mycursor.execute(sql1, (str(record1[0]),str(record1[1])))

for record2 in Students.values:
    mycursor.execute(sql2, (str(record2[0]),str(record2[1]),str(record2[2])))
    
for record3 in Instructors.values:
    mycursor.execute(sql3, (record3[0],record3[1],record3[2]))
mycursor.execute("CREATE TABLE Result AS SELECT * FROM Instructor CROSS JOIN Grades")
mycursor.execute("SELECT AVG(grade) FROM Result WHERE class=1")
print(mycursor.fetchone())
mydb.commit()
mycursor.close()
