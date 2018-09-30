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


def send():
    global con, nameEntry, conatactEntry, genderEntry, emailEntry
    nameData = nameEntry.get()
    contactData = conatactEntry.get()
    emailData = emailEntry.get()
    genderData = genderEntry.get()
    addressData = addressEntry.get()
    stateData = stateEntry.get()
    cityData = cityEntry.get()
    hobbyData = hobbyEntry.get()
    nationalityData = nationalityEntry.get()
    websiteData = websiteEntry.get()
    pincodeData = pincdeEntry.get()
    cursor.execute("insert into contact(name, email, contact, gender, address, state, city, nationality, website, pincode, hobby) value('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"
                   .format(nameData, emailData, contactData, genderData, addressData, stateData, cityData, nationalityData, websiteData, pincodeData, hobbyData))
    con.commit()
    con.close()
    nameEntry.delete(0, END)
    conatactEntry.delete(0, END)
    genderEntry.delete(0, END)
    emailEntry.delete(0, END)
    addressEntry.delete(0, END)
    stateEntry.delete(0, END)
    cityEntry.delete(0, END)
    hobbyEntry.delete(0, END)
    nationalityEntry.delete(0, END)
    websiteEntry.delete(0, END)
    pincdeEntry.delete(0, END)


name = Label(root, text='Name')
name.grid(row=0, column=0)

nameEntry = Entry(root)
nameEntry.grid(row=0, column=1)

contact = Label(root, text='Contact')
contact.grid(row=1, column=0)

conatactEntry = Entry(root)
conatactEntry.grid(row=1, column=1)

email = Label(root, text='Email')
email.grid(row=2, column=0)

emailEntry = Entry(root)
emailEntry.grid(row=2, column=1)

gender = Label(root, text='Gender')
gender.grid(row=3, column=0)

genderEntry = Entry(root)
genderEntry.grid(row=3, column=1)

addressLabel = Label(root, text='Address')
addressLabel.grid(row=4, column=0)

addressEntry = Entry(root)
addressEntry.grid(row=4, column=1)

stateLabel = Label(root, text='State')
stateLabel.grid(row=5, column=0)

stateEntry = Entry(root)
stateEntry.grid(row=5, column=1)

cityLabel = Label(root, text='City')
cityLabel.grid(row=6, column=0)

cityEntry = Entry(root)
cityEntry.grid(row=6, column=1)

nationalityLabel = Label(root, text='Nationality')
nationalityLabel.grid(row=7, column=0)

nationalityEntry = Entry(root)
nationalityEntry.grid(row=7, column=1)

websiteLabel = Label(root, text='Website')
websiteLabel.grid(row=8, column=0)

websiteEntry = Entry(root)
websiteEntry.grid(row=8, column=1)

pincdeLabel = Label(root, text='Pincode')
pincdeLabel.grid(row=9, column=0)

pincdeEntry = Entry(root)
pincdeEntry.grid(row=9, column=1)

hobbyLabel = Label(root, text='Hobby')
hobbyLabel.grid(row=10, column=0)

hobbyEntry = Entry(root)
hobbyEntry.grid(row=10, column=1)

buttonSave = Button(root, text='Save', command=send)
buttonSave.grid(row=11, column=1)

root.mainloop()
