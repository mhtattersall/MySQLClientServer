"""
Reading a table using an SQL driver 
"""

import mysql.connector

"""
Below is a connection string, which provides information about a data server
and how the connection to it is made
"""
cnx = mysql.connector.connect(user='root',
    password='Sharks16',
    host='127.0.0.1',
    database='education',
    auth_plugin='mysql_native_password')

"""
The cursor class allows python code to execute SQL commands in a database session
"""
cursor = cnx.cursor()
query = ("SELECT * FROM colleges")
cursor.execute(query)

# print all the rows
for row in cursor.fetchall():
    print(row)

"""
clean up by closing our cursor and connection to the database
"""
cursor.close()
cnx.close()