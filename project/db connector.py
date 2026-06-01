import mysql.connector
#get conncetion

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="employee")

#statement

mycursor=mydb.cursor()
query="INSERT INTO employee.emp (id, name, department) VALUES (9, 'sai', 'it');"

#execute
mycursor.execute(query)
mydb.commit()
print(mycursor.rowcount, "record inserted.")