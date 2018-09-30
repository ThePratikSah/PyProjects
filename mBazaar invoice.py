from tkinter import *
import pymysql
import time

root = Tk()

root.minsize(770, 600)
root.maxsize(770, 600)

root.title('mBazaar POS service')

con = pymysql.connect('localhost:8889',
    'root',
    'root',
    'class_database',
    unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock"
)

cursor = con.cursor()

def save():
    global con
    nameData = entryName.get()
    dateData = entryDate.get()
    contactData = entryContact.get()
    addressData = entryAddress.get()
    prod1 = entryProduct1.get()
    prod2 = entryProduct2.get()
    prod3 = entryProduct3.get()
    prod4 = entryProduct4.get()
    prod5 = entryProduct5.get()
    prod6 = entryProduct6.get()
    cursor.execute("insert into mBazaar_customer_details(name, date, contact, address, prod1,\
    prod2,prod3,prod4,prod5,prod6) value('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}' )".format(nameData, dateData, contactData, addressData, prod1, prod2, prod3, prod4, prod5, prod6))
    con.commit()
    con.close()

var = 0

def total():
    total_1st = int(entryQuantity1.get()) * int(entryAmount1.get())
    global var
    entryTotal1.delete(0, END)
    entryTotal1.insert(0, round(total_1st, 2))
    total_2nd = int(entryQuantity2.get()) * int(entryAmount2.get())
    entryTotal2.delete(0, END)
    entryTotal2.insert(0, round(total_2nd, 2))
    total_3rd = int(entryQuantity3.get()) * int(entryAmount3.get())
    entryTotal3.delete(0, END)
    entryTotal3.insert(0, round(total_3rd, 2))
    total_4th = int(entryQuantity4.get()) * int(entryAmount4.get())
    entryTotal4.delete(0, END)
    entryTotal4.insert(0, round(total_4th, 2))
    total_5th = int(entryQuantity5.get()) * int(entryAmount5.get())
    entryTotal5.delete(0, END)
    entryTotal5.insert(0, round(total_5th, 2))
    total_6th = int(entryQuantity6.get()) * int(entryAmount6.get())
    entryTotal6.delete(0, END)
    entryTotal6.insert(0, round(total_6th, 2))

    totalPrice = total_1st + total_2nd + total_3rd + total_4th + total_5th + total_6th
    discountPriceValue = totalPrice - (int(entryDiscount.get()) / 100 * totalPrice)
    entryDiscountPrice.delete(0, END)
    entryDiscountPrice.insert(0, round(discountPriceValue, 2))

    cgstPrice = 9 / 100 * discountPriceValue
    entryCgst.insert(0, round(cgstPrice, 2))

    sgstPrice = 9 / 100 * discountPriceValue
    entrySgst.insert(0, round(sgstPrice, 2))

    payableAmtTotal = discountPriceValue + cgstPrice + sgstPrice
    entryPayableAmt.insert(0, round(payableAmtTotal, 2))
    var = payableAmtTotal


def initialize():
    entryQuantity1.insert(0, '0')
    entryAmount1.insert(0, '0')
    entryQuantity2.insert(0, '0')
    entryAmount2.insert(0, '0')
    entryQuantity3.insert(0, '0')
    entryAmount3.insert(0, '0')
    entryQuantity4.insert(0, '0')
    entryAmount4.insert(0, '0')
    entryQuantity5.insert(0, '0')
    entryAmount5.insert(0, '0')
    entryQuantity6.insert(0, '0')
    entryAmount6.insert(0, '0')
    entryDiscount.insert(0, '0')
    entryDate.insert(0, time.strftime("%d/%m/%Y"))
    entryProduct1.insert(0, '0')
    entryProduct2.insert(0, '0')
    entryProduct3.insert(0, '0')
    entryProduct4.insert(0, '0')
    entryProduct5.insert(0, '0')
    entryProduct6.insert(0, '0')



def check():
    global var
    entryReturnAmt.insert(0, round(int(entryAmountPaid.get()) - var))
    var = 0

def reset():
    entryName.delete(0, END)
    entryDate.delete(0, END)
    entryAddress.delete(0, END)
    entryContact.delete(0, END)
    entryProduct1.delete(0, END)
    entryProduct2.delete(0, END)
    entryProduct3.delete(0, END)
    entryProduct4.delete(0, END)
    entryProduct5.delete(0, END)
    entryProduct6.delete(0, END)
    entryAmount1.delete(0, END)
    entryAmount2.delete(0, END)
    entryAmount3.delete(0, END)
    entryAmount4.delete(0, END)
    entryAmount5.delete(0, END)
    entryAmount6.delete(0, END)
    entryQuantity1.delete(0, END)
    entryQuantity2.delete(0, END)
    entryQuantity3.delete(0, END)
    entryQuantity4.delete(0, END)
    entryQuantity5.delete(0, END)
    entryQuantity6.delete(0, END)
    entryTotal1.delete(0, END)
    entryTotal2.delete(0, END)
    entryTotal3.delete(0, END)
    entryTotal4.delete(0, END)
    entryTotal5.delete(0, END)
    entryTotal6.delete(0, END)
    entryDiscount.delete(0, END)
    entryDiscountPrice.delete(0, END)
    entryCgst.delete(0, END)
    entrySgst.delete(0, END)
    entryPayableAmt.delete(0, END)
    entryAmountPaid.delete(0, END)
    entryReturnAmt.delete(0, END)
    initialize()


# frames for the project

frameTitle = Frame(root)
frameCustomerDetails = Frame(root)
frameProductTable = Frame(root)
frameCalculation = Frame(root)

# packing of frames

frameTitle.pack(side=TOP, fill=X)
frameCustomerDetails.pack(side=TOP)
frameProductTable.pack(side=TOP)
frameCalculation.pack(side=TOP, pady=10)


# title for the window

labelTitle = Label(frameTitle, text='mBazaar Invoice', bg='#487eb0', font=['Noto Serif', 40], fg='white', pady=15)
labelTitle.pack(fill=X)


# frame for the customer information

labelName = Label(frameCustomerDetails, text='Name', padx=10, pady=15)
labelName.grid(row=0, column=0)

entryName = Entry(frameCustomerDetails)
entryName.grid(row=0, column=1)

labelContact = Label(frameCustomerDetails, text='Contact', padx=10, pady=10)
labelContact.grid(row=1, column=0)

entryContact = Entry(frameCustomerDetails)
entryContact.grid(row=1, column=1)

labelDate = Label(frameCustomerDetails, text='Date', padx=10, pady=10)
labelDate.grid(row=0, column=2)

entryDate = Entry(frameCustomerDetails)
entryDate.grid(row=0, column=3)

labelAddress = Label(frameCustomerDetails, text='Address', padx=10, pady=10)
labelAddress.grid(row=1, column=2)

entryAddress = Entry(frameCustomerDetails)
entryAddress.grid(row=1, column=3)

# frame for the products

labelProducts = Label(frameProductTable, text='Product')
labelProducts.grid(row=0, column=0)

labelQuantity = Label(frameProductTable, text='Quantity')
labelQuantity.grid(row=0, column=1)

labelAmount = Label(frameProductTable, text='Amount')
labelAmount.grid(row=0, column=2)

labelTotal = Label(frameProductTable, text='Total')
labelTotal.grid(row=0, column=3)

# ====================== Entries for the products =====================

entryProduct1 = Entry(frameProductTable)
entryProduct1.grid(row=1, column=0)

entryQuantity1 = Entry(frameProductTable)
entryQuantity1.grid(row=1, column=1)

entryAmount1 = Entry(frameProductTable)
entryAmount1.grid(row=1, column=2)

entryTotal1 = Entry(frameProductTable)
entryTotal1.grid(row=1, column=3)

#==================================================================

entryProduct2 = Entry(frameProductTable)
entryProduct2.grid(row=2, column=0)

entryQuantity2 = Entry(frameProductTable)
entryQuantity2.grid(row=2, column=1)

entryAmount2 = Entry(frameProductTable)
entryAmount2.grid(row=2, column=2)

entryTotal2 = Entry(frameProductTable)
entryTotal2.grid(row=2, column=3)

#==================================================================

entryProduct3 = Entry(frameProductTable)
entryProduct3.grid(row=3, column=0)

entryQuantity3 = Entry(frameProductTable)
entryQuantity3.grid(row=3, column=1)

entryAmount3 = Entry(frameProductTable)
entryAmount3.grid(row=3, column=2)

entryTotal3 = Entry(frameProductTable)
entryTotal3.grid(row=3, column=3)

#==================================================================

entryProduct4 = Entry(frameProductTable)
entryProduct4.grid(row=4, column=0)

entryQuantity4 = Entry(frameProductTable)
entryQuantity4.grid(row=4, column=1)

entryAmount4 = Entry(frameProductTable)
entryAmount4.grid(row=4, column=2)

entryTotal4 = Entry(frameProductTable)
entryTotal4.grid(row=4, column=3)

#==================================================================

entryProduct5 = Entry(frameProductTable)
entryProduct5.grid(row=5, column=0)

entryQuantity5 = Entry(frameProductTable)
entryQuantity5.grid(row=5, column=1)

entryAmount5 = Entry(frameProductTable)
entryAmount5.grid(row=5, column=2)

entryTotal5 = Entry(frameProductTable)
entryTotal5.grid(row=5, column=3)

#==================================================================

entryProduct6 = Entry(frameProductTable)
entryProduct6.grid(row=6, column=0)

entryQuantity6 = Entry(frameProductTable)
entryQuantity6.grid(row=6, column=1)

entryAmount6 = Entry(frameProductTable)
entryAmount6.grid(row=6, column=2)

entryTotal6 = Entry(frameProductTable)
entryTotal6.grid(row=6, column=3)

# =================================================================

# frame calculation

labelDiscount = Label(frameCalculation, text='Discount')
labelDiscount.grid(row=0, column=0)

entryDiscount = Entry(frameCalculation)
entryDiscount.grid(row=0, column=1)

initialize()

labelDiscountPrice = Label(frameCalculation, text='Discount price')
labelDiscountPrice.grid(row=1, column=0)

entryDiscountPrice = Entry(frameCalculation)
entryDiscountPrice.grid(row=1, column=1)

buttonTotalPrice = Button(frameCalculation, text='Total', command=total)
buttonTotalPrice.grid(row=1, column=2)

labelCgst = Label(frameCalculation, text='CGST 9%')
labelCgst.grid(row=2, column=0)

entryCgst = Entry(frameCalculation)
entryCgst.grid(row=2, column=1)

labelSgst = Label(frameCalculation, text='SGST 9%')
labelSgst.grid(row=3, column=0)

entrySgst = Entry(frameCalculation)
entrySgst.grid(row=3, column=1)

labelPayableAmt = Label(frameCalculation, text='Payable amount')
labelPayableAmt.grid(row=4, column=0)

entryPayableAmt = Entry(frameCalculation)
entryPayableAmt.grid(row=4, column=1)

labelAmountPaid = Label(frameCalculation, text='Amount paid')
labelAmountPaid.grid(row=5, column=0)

entryAmountPaid = Entry(frameCalculation)
entryAmountPaid.grid(row=5, column=1)

labelReturnAmt = Label(frameCalculation, text='Return amount')
labelReturnAmt.grid(row=6, column=0)

entryReturnAmt = Entry(frameCalculation)
entryReturnAmt.grid(row=6, column=1)

buttonTotal = Button(frameCalculation, text='Check', padx=15, command=check)
buttonTotal.grid(row=6, column=2)

buttonSave = Button(frameCalculation, text='Save', padx=15, command=save)
buttonSave.grid(row=6, column=3)

buttonTotal = Button(frameCalculation, text='Reset', padx=15, command=reset)
buttonTotal.grid(row=6, column=4)

root.mainloop()