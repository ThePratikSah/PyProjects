from tkinter import *
import pymysql

root = Tk()

v = StringVar()
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

root.minsize(550, 790)
root.maxsize(550, 790)
root.title('Admission Management System')

# ===============database connection===================

con = pymysql.connect('localhost:8889',
    'root',
    'root',
    'class_database',
    unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock"
)

cursor = con.cursor()


def save():
    global con
    branch = 'na'
    course = v.get()
    if course == 'btech':
        branch = v1.get()
    attachments1 = v2.get()
    attachments2 = v3.get()
    name = entryName.get()
    email = entryEmail.get()
    mobNo = entryMob.get()
    dob = entryDOB.get()
    gender = entryGender.get()
    nationality = entryNationality.get()
    pname = entryNamep.get()
    pemail = entryEmailp.get()
    pmob = entryMobp.get()
    address1 = entryAddress1.get()
    address2 = entryAddress2.get()
    city = entryCity.get()
    state = entryState.get()
    pin = entryPincode.get()

    cursor.execute("insert into students(course, branch, attachments1, attachments2, name, email, mobno, dob, gender, nationality, pname, pemail, pmobno, address1, address2, city, state, pincode) value('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"
                   .format(course, branch, attachments1, attachments2, name, email, mobNo, dob, gender, nationality, pname, pemail, pmob, address1, address2, city, state, pin))
    con.commit()
    con.close()



def reset():
    radioBtech.deselect()
    radioBtechCSE.deselect()
    radioBtechEEE.deselect()
    radioBtechECE.deselect()
    radioBtechME.deselect()
    radioBBA.deselect()
    radioBCA.deselect()
    radioClassMarks10.deselect()
    radioClassMarks12.deselect()
    radioDiplomaMarks.deselect()
    entryName.delete(0, END)
    entryEmail.delete(0, END)
    entryMob.delete(0, END)
    entryDOB.delete(0, END)
    entryGender.delete(0, END)
    entryNationality.delete(0, END)
    entryNamep.delete(0, END)
    entryEmailp.delete(0, END)
    entryMobp.delete(0, END)
    entryAddress1.delete(0, END)
    entryAddress2.delete(0, END)
    entryCity.delete(0, END)
    entryState.delete(0, END)
    entryPincode.delete(0, END)


# ===============frames for the form===================


frameTitle = Frame(root)
frameCoursePref = Frame(root)
frameLabel1 = Frame(root)
framePersonalDetails = Frame(root)

# ===============packing of the frames=================

frameTitle.pack(side=TOP, fill=X)
frameCoursePref.pack()
frameLabel1.pack()
framePersonalDetails.pack()

# ===============components of the frame title==============

labelTitle = Label(frameTitle, text='VVIT Admission Application Form', bg='#044F67', fg='white', font=['Noto Serif', 30], pady=5, bd=10)
labelTitle.pack(fill=X)

labelDesc = Label(frameTitle, text='Mark order of course/specialisation preference', pady=5)
labelDesc.pack()

radioBtech = Radiobutton(frameCoursePref, text='B.Tech', variable=v, value='btech')
radioBtech.grid(row=0, column=0, sticky=W)

radioBtechCSE = Radiobutton(frameCoursePref, text='CSE', variable=v1, value='CSE')
radioBtechCSE.grid(row=1, column=1, sticky=W)

radioBtechECE = Radiobutton(frameCoursePref, text='ECE', variable=v1, value='ECE')
radioBtechECE.grid(row=1, column=2, sticky=W)

radioBtechEEE = Radiobutton(frameCoursePref, text='EEE', variable=v1, value='EEE')
radioBtechEEE.grid(row=1, column=3, sticky=W)

radioBtechME = Radiobutton(frameCoursePref, text='ME', variable=v1, value='ME')
radioBtechME.grid(row=1, column=4, sticky=W)

radioBBA = Radiobutton(frameCoursePref, text='B.B.A', variable=v, value='bba')
radioBBA.grid(row=2, column=0, sticky=W)

radioBCA = Radiobutton(frameCoursePref, text='B.C.A', variable=v, value='bca')
radioBCA.grid(row=2, column=1, sticky=W)

labelAttachments = Label(frameCoursePref, text='Attachments', fg='#34495e', font=['Noto Serif', 30])
labelAttachments.grid(row=3, column=0, sticky=W)

radioClassMarks10 = Radiobutton(frameCoursePref, text='Class X', variable=v2, value='class10')
radioClassMarks10.grid(row=4, column=0, sticky=W)

radioClassMarks12 = Radiobutton(frameCoursePref, text='Class XII', variable=v3, value='class12')
radioClassMarks12.grid(row=5, column=0, sticky=W)

radioDiplomaMarks = Radiobutton(frameCoursePref, text='Diploma', variable=v3, value='diploma')
radioDiplomaMarks.grid(row=6, column=0, sticky=W)

labelAttachmentDetails = Label(frameLabel1, text='*Marksheet for pass out/admit card for appeared')
labelAttachmentDetails.pack()

# ======================== fields for the application ===========================

labelPersonalDetails = Label(framePersonalDetails, text='Personal Details', font=['Noto Serif', 30], fg='#34495e')
labelPersonalDetails.grid(row=0, column=0, sticky=W)

labelName = Label(framePersonalDetails, text='Name:')
labelName.grid(row=1, column=0, sticky=W)
entryName = Entry(framePersonalDetails)
entryName.grid(row=1, column=1, sticky=W)

labelEmail = Label(framePersonalDetails, text='Email:')
labelEmail.grid(row=2, column=0, sticky=W)
entryEmail = Entry(framePersonalDetails)
entryEmail.grid(row=2, column=1, sticky=W)

labelMob = Label(framePersonalDetails, text='Mobile No:')
labelMob.grid(row=3, column=0, sticky=W)
entryMob = Entry(framePersonalDetails)
entryMob.grid(row=3, column=1, sticky=W)

labelDOB = Label(framePersonalDetails, text='D.O.B:')
labelDOB.grid(row=4, column=0, sticky=W)
entryDOB = Entry(framePersonalDetails)
entryDOB.grid(row=4, column=1, sticky=W)

labelGender = Label(framePersonalDetails, text='Gender:')
labelGender.grid(row=5, column=0, sticky=W)
entryGender = Entry(framePersonalDetails)
entryGender.grid(row=5, column=1, sticky=W)

labelNationality = Label(framePersonalDetails, text='Nationality')
labelNationality.grid(row=6, column=0, sticky=W)
entryNationality = Entry(framePersonalDetails)
entryNationality.grid(row=6, column=1, sticky=W)

# ======================== fields for the application ===========================

labelParentsDetails = Label(framePersonalDetails, text='Parent\'s Details', font=['Noto Serif', 30], fg='#34495e')
labelParentsDetails.grid(row=7, column=0, sticky=W)

labelNamep = Label(framePersonalDetails, text='Name:')
labelNamep.grid(row=8, column=0, sticky=W)
entryNamep = Entry(framePersonalDetails)
entryNamep.grid(row=8, column=1, sticky=W)

labelEmailp = Label(framePersonalDetails, text='Email:')
labelEmailp.grid(row=9, column=0, sticky=W)
entryEmailp = Entry(framePersonalDetails)
entryEmailp.grid(row=9, column=1, sticky=W)

labelMobp = Label(framePersonalDetails, text='Mobile No:')
labelMobp.grid(row=10, column=0, sticky=W)
entryMobp = Entry(framePersonalDetails)
entryMobp.grid(row=10, column=1, sticky=W)

labelAddress1 = Label(framePersonalDetails, text='Address line 1:')
labelAddress1.grid(row=11, column=0, sticky=W)
entryAddress1 = Entry(framePersonalDetails)
entryAddress1.grid(row=11, column=1, sticky=W)

labelAddress2 = Label(framePersonalDetails, text='Address line 2:')
labelAddress2.grid(row=12, column=0, sticky=W)
entryAddress2 = Entry(framePersonalDetails)
entryAddress2.grid(row=12, column=1, sticky=W)

labelCity = Label(framePersonalDetails, text='City:')
labelCity.grid(row=13, column=0, sticky=W)
entryCity = Entry(framePersonalDetails)
entryCity.grid(row=13, column=1, sticky=W)

labelState = Label(framePersonalDetails, text='State:')
labelState.grid(row=14, column=0, sticky=W)
entryState = Entry(framePersonalDetails)
entryState.grid(row=14, column=1, sticky=W)

labelPincode = Label(framePersonalDetails, text='Pin Code:')
labelPincode.grid(row=15, column=0, sticky=W)
entryPincode = Entry(framePersonalDetails)
entryPincode.grid(row=15, column=1, sticky=W)

btnSave = Button(framePersonalDetails, text='Save', command=save)
btnSave.grid(row=15, column=2, sticky=W)

btnReset = Button(framePersonalDetails, text='Reset', command=reset)
btnReset.grid(row=15, column=3, sticky=W)

root.mainloop()
