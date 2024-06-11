import mysql
import mysql.connector
conn = mysql.connector.connect(
    user="root",  
    password="root123", 
    host="localhost", 
    database="spidata" , 
    auth_plugin="mysql_native_password"
)
print("Connection successful!")
cursor = conn.cursor()
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
for table in tables:
    print(table[0])  # Access the table name from the first column
cursor.close()


