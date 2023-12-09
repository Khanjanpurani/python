import mysql.connector
db=mysql.connector.connect(user="root",passwd="1234",host="localhost",database='student_details')
my_cursor=db.cursor()
my_cursor=db.cursor()
query="CREATE TABLE student_details (name VARCHAR(255), roll INT(10), class INT(10))" #query to create a table
my_cursor.execute(query) #executing the query
