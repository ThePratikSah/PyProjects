from tkinter import *
import pymysql

root = Tk()

root.minsize(450, 700)
root.maxsize(450, 700)
root.title('Result Management System')

con = pymysql.connect('localhost:8889',
    'root',
    'root',
    'class_database',
    unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock"
)

cursor = con.cursor()

# ====================frames for the view===================

frameTitle = Frame(root)
frameDetails = Frame(root)
frameMarksTitle = Frame(root)
frameMarksDetailsTitle = Frame(root)
frameMarksDetails = Frame(root)
frameResultDetailsTitle = Frame(root)
frameResultDetails = Frame(root)

# ===================== packing of frames ===================

frameTitle.pack(side=TOP, fill=X)
frameDetails.pack(side=TOP, fill=X)
frameMarksTitle.pack(side=TOP, fill=X)
frameMarksDetailsTitle.pack(side=TOP, fill=X)
frameMarksDetails.pack(side=TOP, fill=X)
frameResultDetailsTitle.pack(side=TOP, fill=X)
frameResultDetails.pack(side=TOP, fill=X)

# ==================== Label title for the window ===================
labelTitle = Label(frameTitle, text='Personal Details', bg='#044F67', fg='white', font=['Noto Serif', 20], pady=5, bd=10)
labelTitle.pack(fill=X)

# ==================== personal details grid =======================
labelName = Label(frameDetails, text='Name')
labelName.grid(row=0, column=0)

entryName = Entry(frameDetails)
entryName.grid(row=0, column=1)

labelFName = Label(frameDetails, text='Father\'s name')
labelFName.grid(row=1, column=0)

entryFName = Entry(frameDetails)
entryFName.grid(row=1, column=1)

labelContact = Label(frameDetails, text='Contact')
labelContact.grid(row=2, column=0)

entryContact = Entry(frameDetails)
entryContact.grid(row=2, column=1)

labelEmail = Label(frameDetails, text='Email')
labelEmail.grid(row=3, column=0)

entryEmail = Entry(frameDetails)
entryEmail.grid(row=3, column=1)

labelSchool = Label(frameDetails, text='School')
labelSchool.grid(row=4, column=0)

entrySchool = Entry(frameDetails)
entrySchool.grid(row=4, column=1)

# ========================= frame marks details title =========================

labelMarksDetails = Label(frameMarksDetailsTitle, text='Marks Details', bg='#044F67', fg='white', font=['Noto Serif', 20], pady=5, bd=10)
labelMarksDetails.pack(fill=X)

labelSubject = Label(frameMarksDetails, text='Subject')
labelSubject.grid(row=0, column=0)

labelTotal = Label(frameMarksDetails, text='Total')
labelTotal.grid(row=0, column=1)

labelPass = Label(frameMarksDetails, text='Pass')
labelPass.grid(row=0, column=2)

labelObtain = Label(frameMarksDetails, text='Obtain')
labelObtain.grid(row=0, column=3)

# ========================== frame marks details ==============================

labelMaths = Label(frameMarksDetails, text='Maths')
labelMaths.grid(row=1, column=0)

labelScience = Label(frameMarksDetails, text='Science')
labelScience.grid(row=2, column=0)

labelSST = Label(frameMarksDetails, text='Social Science')
labelSST.grid(row=3, column=0)

labelEnglish = Label(frameMarksDetails, text='English')
labelEnglish.grid(row=4, column=0)

labelHindi = Label(frameMarksDetails, text='Hindi')
labelHindi.grid(row=5, column=0)

# ========================== total Label ==================================


root.mainloop()