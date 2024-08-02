import mysql.connector
import pandas as pd
"""
Define connection string
"""
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Sharks16',
    database = 'education'
)
"""
Define our query
"""
query = 'select * from Colleges'
"""
Integrate the information by creating a dataframe by reading into pandas
and passing the query and the connection string
"""
df = pd.read_sql(query, con = mydb)
print(df)