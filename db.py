import pymysql

connect = pymysql.connect(
    'localhost:8889',
    'root',
    ' '
    'demo'
)

cursor = con.cursor()

cursor.execute('create database db')
con.close()