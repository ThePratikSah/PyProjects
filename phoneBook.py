import pymysql
from tkinter import *

root = Tk()

root.title('Python Phone book')

root.minsize(400, 200)

con = pymysql.connect('localhost:8889',
    'root',
    'root',
    'class_database',
    unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock"
)

cursor = con.cursor()


def send():
    global con
    nameData = nameEntry.get()
    contactData = conatactEntry.get()
    cursor.execute("insert into phonebook(name, contact) value('{}', '{}')".format(nameData, contactData))
    con.commit()
    con.close()


name = Label(root, text='Name')
name.grid(row=0, column=0)

contact = Label(root, text='Contact')
contact.grid(row=1, column=0)

nameEntry = Entry(root)
nameEntry.grid(row=0, column=1)

conatactEntry = Entry(root)
conatactEntry.grid(row=1, column=1)

buttonSave = Button(root, text='Save', command=send)
buttonSave.grid(row=3, column=1)

root.mainloop()
