import pymysql
import pyodbc

def buka_koneksi():
    try:
        koneksi = pymysql.connect('122317203930.ip-dynamic.com', 'sa_dev_magang', 'TyRTRGB8Pfu5VRjg', 'DBLATIHAN')
        return koneksi

    except Exception as ex:
        return None

def buka_koneksi2():
    server = '122317203930.ip-dynamic.com,8989' 
    database = 'DBLATIHAN' 
    username = 'sa_dev_magang' 
    password = 'TyRTRGB8Pfu5VRjg' 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    return cnxn

def tutup_koneksi(koneksi):
    try:
        koneksi.close()
    except Exception as ex:
        pass