import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="employee")

mycursor=mydb.cursor()
query="INSERT INTO employee.emp (id, name, department) VALUES (2, 'sai', 'it');"

mycursor.execute(query)
mydb.commit()
print(mycursor.rowcount, "record inserted.")