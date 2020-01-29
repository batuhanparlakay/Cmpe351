import mysql.connector
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS UNIVERSITY")
mycursor.execute("USE UNIVERSITY")
mycursor.execute("CREATE TABLE IF NOT EXISTS Grades (student_id VARCHAR(25) PRIMARY KEY, grade VARCHAR(255)) ")

sql = "INSERT INTO Grades (student_id , grade) VALUES (%s, %s)"

for i in range (30) :
    rand_grade = random.randint (0,100)
    rand_id = random.randint (123456789 , 987654321)
    val = (rand_id,rand_grade)
    mycursor.execute(sql, val)
    mydb.commit()