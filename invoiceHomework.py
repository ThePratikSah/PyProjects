from tkinter import *

root = Tk()

# deciding the size of window
root.maxsize(300, 430)
root.minsize(300, 430)

# title for the window
root.title('Shop management')


# function for finding the total
def total():
    total_amount = int(amountEntry.get()) * int(amountQuantity.get())
    discount_price = total_amount - (int(amountDiscount.get()) * total_amount / 100)
    gst_price = discount_price + (int(amountGST.get())) * discount_price / 100
    display.config(text=str(gst_price))


# frames for the widgets
f1 = Frame(root)
f2 = Frame(root)

f1.pack(side=TOP, fill=X)
f2.pack(side=TOP, fill=X)

# label for frame 1
l1 = Label(f1, text='INVOICE', font=['aerial', 20], bg='#4d8fac', fg='white', pady=7)
l1.pack(fill=X)

# label for amount
productAmount = Label(f2, text='Product amount:', font=['aerial', 14], pady=7)
productAmount.pack(fill=X)

# entry for amount
amountEntry = Entry(f2)
amountEntry.pack()

# label for quantity
productQuantity = Label(f2, text='Product quantity:', font=['aerial', 14], pady=7)
productQuantity.pack(fill=X)

# entry for quantity
amountQuantity = Entry(f2)
amountQuantity.pack()

# label for discount
productDiscount = Label(f2, text='Discount(%):', font=['aerial', 14], pady=7)
productDiscount.pack(fill=X)

# entry for discount
amountDiscount = Entry(f2)
amountDiscount.pack()

# label for GST
productGST = Label(f2, text='GST(%):', font=['aerial', 14], pady=7)
productGST.pack(fill=X)

# entry for GST
amountGST = Entry(f2)
amountGST.pack()

# Button for calculation
buttonTotal = Button(f2, text='TOTAL', command=total, bg='#5d3f6a', pady=7, padx=7)
buttonTotal.pack(pady=10)

# frame for displaying the value
display = Label(f2, font=['aerial', 16])
display.pack(fill=X, pady=20)


root.mainloop()
