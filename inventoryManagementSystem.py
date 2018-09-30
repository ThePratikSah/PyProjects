from tkinter import *
import pymysql

root = Tk()

root.title('Python Phone book')

root.minsize(200, 500)

con = pymysql.connect('localhost:8889',
    'root',
    'root',
    'class_database',
    unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock"
)

cursor = con.cursor()

labelName = Label()

root.mainloop()
