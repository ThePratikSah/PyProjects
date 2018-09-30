from tkinter import *
import time


def reset():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    entry7.delete(0, END)
    entry8.delete(0, END)
    entry9.delete(0, END)
    entry10.delete(0, END)
    entry11.delete(0, END)
    entry12.delete(0, END)


def amount_total():
    total_amt = (int(entry2.get()) * 35) + (int(entry3.get()) * 235) + \
                (int(entry4.get()) * 15) + (int(entry5.get()) * 65) + \
                (int(entry6.get()) * 45) + (int(entry7.get()) * 15) + \
                (int(entry8.get()) * 135)

    service_charge = total_amt + 0.005 * total_amt
    gst_amount = service_charge + int(entry10.get()) / 100 * service_charge
    sub_total = total_amt

    entry11.delete(0, END)
    entry11.insert(0, sub_total)

    entry12.delete(0, END)
    entry12.insert(0, gst_amount)


root = Tk()
root.minsize(1100, 500)
root.maxsize(1100, 500)

root.title('Restaurant Management System')

# frames for the project

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)


f1.pack(side=TOP, fill=X)
f2.pack(side=LEFT)
f3.pack(side=LEFT)
f4.pack(side=RIGHT)

# labels for the frame1

l1 = Label(f1, text='Restaurant Management System', bg='#487eb0', font=['Noto Serif', 40], fg='white')
l1.pack(fill=X)

localtime = time.asctime(time.localtime(time.time()))
labelTime = Label(f1, text="-------- " + localtime + " --------", bg='#487eb0', font=['Noto Serif', 15], fg='white')
labelTime.pack(fill=X)
labelTime.after(200)

# fields in frame 2--------------------------------------------------------------------->
label1 = Label(f2, text='Reference number', padx=10, pady=10)
label1.grid(row=0, column=0)

entry1 = Entry(f2)
entry1.grid(row=0, column=1)

label2 = Label(f2, text='Burger @ $35.00', padx=10, pady=10)
label2.grid(row=1, column=0)

entry2 = Entry(f2)
entry2.grid(row=1, column=1)

label3 = Label(f2, text='Pizza @ $235.00', padx=10, pady=10)
label3.grid(row=2, column=0)

entry3 = Entry(f2)
entry3.grid(row=2, column=1)

label4 = Label(f2, text='Noodles @ $15.00', padx=10, pady=10)
label4.grid(row=3, column=0)

entry4 = Entry(f2)
entry4.grid(row=3, column=1)

label5 = Label(f2, text='Chicken burger @ $65.00', padx=10, pady=10)
label5.grid(row=4, column=0)

entry5 = Entry(f2)
entry5.grid(row=4, column=1)

label6 = Label(f2, text='Cheese burger @ $45.00', padx=10, pady=10)
label6.grid(row=5, column=0)

entry6 = Entry(f2)
entry6.grid(row=5, column=1)

btnTotal = Button(f2, text='TOTAL', bd=5, padx=10, pady=10, command=amount_total)
btnTotal.grid(row=6, column=1)

# fields in frame 3--------------------------------------------------------------------------->
label7 = Label(f3, text='Drinks @ $15.00', padx=10, pady=10)
label7.grid(row=0, column=0)

entry7 = Entry(f3)
entry7.grid(row=0, column=1)

label8 = Label(f3, text='Cost of meal @ $135.00', padx=10, pady=10)
label8.grid(row=1, column=0)

entry8 = Entry(f3)
entry8.grid(row=1, column=1)

label9 = Label(f3, text='Service charge(%)', padx=10, pady=10)
label9.grid(row=2, column=0)

entry9 = Entry(f3)
entry9.grid(row=2, column=1)

label10 = Label(f3, text='GST(%)', padx=10, pady=10)
label10.grid(row=3, column=0)

entry10 = Entry(f3)
entry10.grid(row=3, column=1)

label11 = Label(f3, text='Sub total', padx=10, pady=10)
label11.grid(row=4, column=0)

entry11 = Entry(f3)
entry11.grid(row=4, column=1)

label12 = Label(f3, text='Total cost', padx=10, pady=10)
label12.grid(row=5, column=0)

entry12 = Entry(f3)
entry12.grid(row=5, column=1)

btnReset = Button(f3, text='RESET', bd=5, padx=10, pady=10, command=reset)
btnReset.grid(row=6, column=1)

# <----------------------------program for calculator------------------------------------------->


def clear():
    display.delete(0, END)
    return


val = StringVar()


def btn_click(numbers):
    global operator
    operator = operator + str(numbers)
    val.set(operator)


def total():
    global operator
    val.set(str(eval(operator)))
    operator = ""


operator = ""

frame1 = Frame(root)
frame1.pack(fill=X, side=TOP)

f4 = Frame(root)
f4.pack(side=TOP, fill=Y)

labelCalci = Label(frame1, text='Calculator', font=['Noto Serif', 20], pady=7)
labelCalci.pack(fill=X)

display = Entry(frame1, bd=20, textvariable=val, justify=RIGHT)
display.pack()

btn1 = Button(f4, text="1", bd=10, padx=20, pady=20, command=lambda: btn_click(1))
btn1.grid(row=0, column=0)

btn2 = Button(f4, text="2", bd=10, padx=20, pady=20, command=lambda: btn_click(2))
btn2.grid(row=0, column=1)

btn3 = Button(f4, text="3", bd=10, padx=20, pady=20, command=lambda: btn_click(3))
btn3.grid(row=0, column=2)

btn4 = Button(f4, text="+", bd=10, padx=20, pady=20, command=lambda: btn_click('+'))
btn4.grid(row=0, column=3)

btn5 = Button(f4, text="4", bd=10, padx=20, pady=20, command=lambda: btn_click(4))
btn5.grid(row=1, column=0)

btn6 = Button(f4, text="5", bd=10, padx=20, pady=20, command=lambda: btn_click(5))
btn6.grid(row=1, column=1)

btn7 = Button(f4, text="6", bd=10, padx=20, pady=20, command=lambda: btn_click(6))
btn7.grid(row=1, column=2)

btn8 = Button(f4, text="-", bd=10, padx=20, pady=20, command=lambda: btn_click('-'))
btn8.grid(row=1, column=3)

btn9 = Button(f4, text="7", bd=10, padx=20, pady=20, command=lambda: btn_click(7))
btn9.grid(row=2, column=0)

btn10 = Button(f4, text="8", bd=10, padx=20, pady=20, command=lambda: btn_click(8))
btn10.grid(row=2, column=1)

btn11 = Button(f4, text="9", bd=10, padx=20, pady=20, command=lambda: btn_click(9))
btn11.grid(row=2, column=2)

btn12 = Button(f4, text="*", bd=10, padx=20, pady=20, command=lambda: btn_click('*'))
btn12.grid(row=2, column=3)

btn13 = Button(f4, text="c", bd=10, padx=20, pady=20, command=clear)
btn13.grid(row=3, column=0)

btn14 = Button(f4, text="=", bd=10, padx=20, pady=20, command=total)
btn14.grid(row=3, column=2)

btn15 = Button(f4, text="0", bd=10, padx=20, pady=20, command=lambda: btn_click(0))
btn15.grid(row=3, column=1)

btn16 = Button(f4, text="/", bd=10, padx=20, pady=20, command=lambda: btn_click('/'))
btn16.grid(row=3, column=3)


root.mainloop()
