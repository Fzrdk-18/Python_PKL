import pyodbc

server = '122317203930.ip-dynamic.com,8989' 
database = 'DBLATIHAN' 
username = 'sa_dev_magang' 
password = 'TyRTRGB8Pfu5VRjg' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
print (cnxn)