from tkinter import *
import pymysql
import time

root = Tk()

root.minsize(770, 600)
root.maxsize(770, 600)

root.title('mBaazar POS service')

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
    contactData = entryContact.get()
    dateData = entryDate.get()
    addressData = entryAddress.get()
    prod1 = entryProduct1.get()
    prod2 = entryProduct2.get()
    prod3 = entryProduct3.get()
    prod4 = entryProduct4.get()
    prod5 = entryProduct5.get()
    prod6 = entryProduct6.get()
    qty1 = entryQuantity1.get()
    qty2 = entryQuantity2.get()
    qty3 = entryQuantity3.get()
    qty4 = entryQuantity4.get()
    qty5 = entryQuantity5.get()
    qty6 = entryQuantity6.get()
    amt1 = entryAmount1.get()
    amt2 = entryAmount2.get()
    amt3 = entryAmount3.get()
    amt4 = entryAmount4.get()
    amt5 = entryAmount5.get()
    amt6 = entryAmount6.get()
    tot1 = entryTotal1.get()
    tot2 = entryTotal2.get()
    tot3 = entryTotal3.get()
    tot4 = entryTotal4.get()
    tot5 = entryTotal5.get()
    tot6 = entryTotal6.get()
    discount = entryDiscount.get()
    discPrice = entryDiscountPrice.get()
    cgstPrice = entryCgst.get()
    sgstPrice = entrySgst.get()
    payableAmount = entryPayableAmt.get()
    amtPaid = entryAmountPaid.get()
    returned = entryReturnAmt.get()
    cursor.execute("insert into mBazaar_customer_details(date, name, address, contact, prod1, prod2, prod3, prod4, prod5, prod6, qty1, qty2, qty3, qty4, qty5, qty6, amt1, amt2, amt3, amt4, amt5, amt6, tot1, tot2, tot3, tot4, tot5, tot6, discount, discPrice, cgstPrice, sgstPrice, payableAmount, amtPaid, returned) value('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"
                   .format(dateData, nameData, addressData, contactData, prod1, prod2, prod3, prod4, prod5, prod6, qty1, qty2, qty3, qty4, qty5, qty6, amt1, amt2, amt3, amt4, amt5, amt6, tot1, tot2, tot3, tot4, tot5, tot6, discount, discPrice, cgstPrice, sgstPrice, payableAmount, amtPaid, returned))
    con.commit()
    con.close()
    reset()


# ======================== functions =============================
var = 0

# ======================== set default value =====================

dataName = StringVar()
dataContact = StringVar()
dataAddress = StringVar()
dataDate = StringVar()
dataDate.set(time.strftime("%d/%m/%Y"))

dataDiscount = IntVar()
dataDiscountPrice = IntVar()
dataCgst = IntVar()
dataSgst = IntVar()
dataPayableAmt = IntVar()
dataAmtPaid = IntVar()
dataReturned = IntVar()

dataTotal1 = IntVar()
dataTotal2 = IntVar()
dataTotal3 = IntVar()
dataTotal4 = IntVar()
dataTotal5 = IntVar()
dataTotal6 = IntVar()

dataAmount1 = IntVar()
dataAmount2 = IntVar()
dataAmount3 = IntVar()
dataAmount4 = IntVar()
dataAmount5 = IntVar()
dataAmount6 = IntVar()

dataQty1 = IntVar()
dataQty2 = IntVar()
dataQty3 = IntVar()
dataQty4 = IntVar()
dataQty5 = IntVar()
dataQty6 = IntVar()

dataProduct1 = StringVar()
dataProduct2 = StringVar()
dataProduct3 = StringVar()
dataProduct4 = StringVar()
dataProduct5 = StringVar()
dataProduct6 = StringVar()


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
    dataDate.set(time.strftime("%d/%m/%Y"))


def total():
    global var
    total_1st = int(entryQuantity1.get()) * int(entryAmount1.get())
    dataTotal1.set(total_1st)
    total_2nd = int(entryQuantity2.get()) * int(entryAmount2.get())
    dataTotal2.set(total_2nd)
    total_3rd = int(entryQuantity3.get()) * int(entryAmount3.get())
    dataTotal3.set(total_3rd)
    total_4th = int(entryQuantity4.get()) * int(entryAmount4.get())
    dataTotal4.set(total_4th)
    total_5th = int(entryQuantity5.get()) * int(entryAmount5.get())
    dataTotal5.set(total_5th)
    total_6th = int(entryQuantity6.get()) * int(entryAmount6.get())
    dataTotal6.set(total_6th)

    totalPrice = total_1st + total_2nd + total_3rd + total_4th + total_5th + total_6th
    discountPriceValue = totalPrice - (int(entryDiscount.get()) / 100 * totalPrice)
    dataDiscountPrice.set(discountPriceValue)

    cgstPrice = 9 / 100 * discountPriceValue
    dataCgst.set(round(cgstPrice, 2))

    sgstPrice = 9 / 100 * discountPriceValue
    dataSgst.set(round(sgstPrice, 2))

    payableAmtTotal = discountPriceValue + cgstPrice + sgstPrice
    dataPayableAmt.set(round(payableAmtTotal))
    var = payableAmtTotal


def check():
    global var
    dataReturned.set(round(int(entryAmountPaid.get()) - var))

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

labelTitle = Label(frameTitle, text='mBaazar Invoice', bg='#487eb0', font=['Noto Serif', 40],\
                   fg='white', pady=15)

labelTitle.pack(fill=X)

# frame for the customer information

labelName = Label(frameCustomerDetails, text='Name', padx=10, pady=15)
labelName.grid(row=0, column=0)

entryName = Entry(frameCustomerDetails, textvariable=dataName)
entryName.grid(row=0, column=1)

labelContact = Label(frameCustomerDetails, text='Contact', padx=10, pady=10)
labelContact.grid(row=1, column=0)

entryContact = Entry(frameCustomerDetails, textvariable=dataContact)
entryContact.grid(row=1, column=1)

labelDate = Label(frameCustomerDetails, text='Date', padx=10, pady=10)
labelDate.grid(row=0, column=2)

entryDate = Entry(frameCustomerDetails, textvariable=dataDate)
entryDate.grid(row=0, column=3)

labelAddress = Label(frameCustomerDetails, text='Address', padx=10, pady=10)
labelAddress.grid(row=1, column=2)

entryAddress = Entry(frameCustomerDetails, textvariable=dataAddress)
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

entryProduct1 = Entry(frameProductTable, textvariable=dataProduct1)
entryProduct1.grid(row=1, column=0)

entryQuantity1 = Entry(frameProductTable, textvariable=dataQty1)
entryQuantity1.grid(row=1, column=1)

entryAmount1 = Entry(frameProductTable, textvariable=dataAmount1)
entryAmount1.grid(row=1, column=2)

entryTotal1 = Entry(frameProductTable, textvariable=dataTotal1)
entryTotal1.grid(row=1, column=3)

#==================================================================

entryProduct2 = Entry(frameProductTable, textvariable=dataProduct2)
entryProduct2.grid(row=2, column=0)

entryQuantity2 = Entry(frameProductTable, textvariable=dataQty2)
entryQuantity2.grid(row=2, column=1)

entryAmount2 = Entry(frameProductTable, textvariable=dataAmount2)
entryAmount2.grid(row=2, column=2)

entryTotal2 = Entry(frameProductTable, textvariable=dataTotal2)
entryTotal2.grid(row=2, column=3)

#==================================================================

entryProduct3 = Entry(frameProductTable, textvariable=dataProduct3)
entryProduct3.grid(row=3, column=0)

entryQuantity3 = Entry(frameProductTable, textvariable=dataQty3)
entryQuantity3.grid(row=3, column=1)

entryAmount3 = Entry(frameProductTable, textvariable=dataAmount3)
entryAmount3.grid(row=3, column=2)

entryTotal3 = Entry(frameProductTable, textvariable=dataTotal3)
entryTotal3.grid(row=3, column=3)

#==================================================================

entryProduct4 = Entry(frameProductTable, textvariable=dataProduct4)
entryProduct4.grid(row=4, column=0)

entryQuantity4 = Entry(frameProductTable, textvariable=dataQty4)
entryQuantity4.grid(row=4, column=1)

entryAmount4 = Entry(frameProductTable, textvariable=dataAmount4)
entryAmount4.grid(row=4, column=2)

entryTotal4 = Entry(frameProductTable, textvariable=dataTotal4)
entryTotal4.grid(row=4, column=3)

#==================================================================

entryProduct5 = Entry(frameProductTable, textvariable=dataProduct5)
entryProduct5.grid(row=5, column=0)

entryQuantity5 = Entry(frameProductTable, textvariable=dataQty5)
entryQuantity5.grid(row=5, column=1)

entryAmount5 = Entry(frameProductTable, textvariable=dataAmount5)
entryAmount5.grid(row=5, column=2)

entryTotal5 = Entry(frameProductTable, textvariable=dataTotal5)
entryTotal5.grid(row=5, column=3)

#==================================================================

entryProduct6 = Entry(frameProductTable, textvariable=dataProduct6)
entryProduct6.grid(row=6, column=0)

entryQuantity6 = Entry(frameProductTable, textvariable=dataQty6)
entryQuantity6.grid(row=6, column=1)

entryAmount6 = Entry(frameProductTable, textvariable=dataAmount6)
entryAmount6.grid(row=6, column=2)

entryTotal6 = Entry(frameProductTable, textvariable=dataTotal6)
entryTotal6.grid(row=6, column=3)

# =================================================================

# frame calculation

labelDiscount = Label(frameCalculation, text='Discount')
labelDiscount.grid(row=0, column=0)

entryDiscount = Entry(frameCalculation, textvariable=dataDiscount)
entryDiscount.grid(row=0, column=1)

labelDiscountPrice = Label(frameCalculation, text='Discount price')
labelDiscountPrice.grid(row=1, column=0)

entryDiscountPrice = Entry(frameCalculation, textvariable=dataDiscountPrice)
entryDiscountPrice.grid(row=1, column=1)

buttonTotalPrice = Button(frameCalculation, text='Total', command=total)
buttonTotalPrice.grid(row=1, column=2)

labelCgst = Label(frameCalculation, text='CGST 9%')
labelCgst.grid(row=2, column=0)

entryCgst = Entry(frameCalculation, textvariable=dataCgst)
entryCgst.grid(row=2, column=1)

labelSgst = Label(frameCalculation, text='SGST 9%')
labelSgst.grid(row=3, column=0)

entrySgst = Entry(frameCalculation, textvariable=dataSgst)
entrySgst.grid(row=3, column=1)

labelPayableAmt = Label(frameCalculation, text='Payable amount')
labelPayableAmt.grid(row=4, column=0)

entryPayableAmt = Entry(frameCalculation, textvariable=dataPayableAmt)
entryPayableAmt.grid(row=4, column=1)

labelAmountPaid = Label(frameCalculation, text='Amount paid')
labelAmountPaid.grid(row=5, column=0)

entryAmountPaid = Entry(frameCalculation, textvariable=dataAmtPaid)
entryAmountPaid.grid(row=5, column=1)

labelReturnAmt = Label(frameCalculation, text='Return amount')
labelReturnAmt.grid(row=6, column=0)

entryReturnAmt = Entry(frameCalculation, textvariable=dataReturned)
entryReturnAmt.grid(row=6, column=1)

buttonCheck = Button(frameCalculation, text='Check', padx=15, command=check)
buttonCheck.grid(row=6, column=2)

buttonSave = Button(frameCalculation, text='Save', padx=15, command=save)
buttonSave.grid(row=6, column=3)

buttonReset = Button(frameCalculation, text='Reset', padx=15, command=reset)
buttonReset.grid(row=6, column=4)


root.mainloop()