import pandas as pd
import pyodbc


server = '122317203930.ip-dynamic.com,8989' 
database = 'DBLATIHAN' 
username = 'sa_dev_magang' 
password = 'TyRTRGB8Pfu5VRjg' 
conn =  pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = conn.cursor()
  
# execute your query
cursor.execute("SELECT * FROM TOFLMB")
# fetch all the matching rows
result = cursor.fetchall()
  
# loop through the rows
for row in result:
    print(row, '\n') 
