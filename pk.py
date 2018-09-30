import tkinter
from tkinter import *
root = Tk()
root.minsize(1100, 500)
root.title("Restaurant Management System")


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


def totalVal():
    totalvalue = (int(entry2.get()) * 35) + (int(entry3.get()) * 45) + \
                 (int(entry4.get()) * 25) + (int(entry5.get()) * 35) + \
                 (int(entry6.get()) * 135) + (int(entry7.get()) * 130) + \
                 (int(entry8.get()) * 95)

    serviceVal = totalvalue + int(entry9.get()) / 100 * totalvalue
    gstPrice = serviceVal + (int(entry10.get()) / 100) * serviceVal

    entry11.delete(0, END)
    entry11.insert(0, totalvalue)

    entry12.delete(0, END)
    entry12.insert(0, gstPrice)


frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)

frame1.pack(fill=X,side=TOP)
frame2.pack(side=LEFT)
frame3.pack(side=LEFT)
frame4.pack()

val = "Restaurant  Management  Systems"
label1 = Label(frame1, text=val, font=["Noto Serif", 40], bg="#044F67",fg="white",pady=2)
label1.pack(fill=X,side=TOP)

#----------------------------------------------------------------------------------------------->

label2 = Label(frame2,text="Reference",font=["Noto Serif", 15],padx=20,pady=7)
label2.grid(row=0, column=0)
entry1 = Entry(frame2)
entry1.grid(row=0,column=1)

label3 = Label(frame2,text="Large Fries",font=["Noto Serif", 15],padx=20,pady=7)
label3.grid(row=1, column=0)
entry2 = Entry(frame2)
entry2.grid(row=1,column=1)

label4 = Label(frame2,text="Burger Meal",font=["Noto Serif", 15],padx=20,pady=7)
label4.grid(row=2, column=0)
entry3 = Entry(frame2)
entry3.grid(row=2,column=1)

label5 = Label(frame2,text="Noodles",font=["Noto Serif", 15],padx=20,pady=7)
label5.grid(row=3, column=0)
entry4 = Entry(frame2)
entry4.grid(row=3,column=1)

label6 = Label(frame2,text="Ice-Cream",font=["Noto Serif", 15],padx=20,pady=7)
label6.grid(row=4, column=0)
entry5 = Entry(frame2)
entry5.grid(row=4,column=1)

label7 = Label(frame2,text="Chicken Rice",font=["Noto Serif", 15],padx=20,pady=7)
label7.grid(row=5, column=0)
entry6 = Entry(frame2)
entry6.grid(row=5,column=1)

#-------------------------------frame3-------------------------------------------
label2 = Label(frame3,text="Pizza",font=["Noto Serif", 15],padx=20,pady=7)
label2.grid(row=0, column=0)
entry7 = Entry(frame3)
entry7.grid(row=0,column=1)

label3 = Label(frame3,text="Taco Mexican",font=["Noto Serif", 15],padx=20,pady=7)
label3.grid(row=1, column=0)
entry8 = Entry(frame3)
entry8.grid(row=1,column=1)

label4 = Label(frame3,text="Service Charge(%)",font=["Noto Serif", 15],padx=20,pady=7)
label4.grid(row=2, column=0)
entry9 = Entry(frame3)
entry9.grid(row=2,column=1)

label5 = Label(frame3,text="GST(%)",font=["Noto Serif", 15],padx=20,pady=7)
label5.grid(row=3, column=0)
entry10 = Entry(frame3)
entry10.grid(row=3,column=1)

label6 = Label(frame3,text="Sub-total",font=["Noto Serif", 15],padx=20,pady=7)
label6.grid(row=4, column=0)
entry11 = Entry(frame3)
entry11.grid(row=4,column=1)

label7 = Label(frame3,text="Total Cost",font=["Noto Serif", 15],padx=20,pady=7)
label7.grid(row=5, column=0)
entry12 = Entry(frame3)
entry12.grid(row=5,column=1)

#========================Calculator===============================================>


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

btn1 = Button(f4, text="1", padx=20, pady=20, command=lambda: btn_click(1))
btn1.grid(row=0, column=0)

btn2 = Button(f4, text="2", padx=20, pady=20, command=lambda: btn_click(2))
btn2.grid(row=0, column=1)

btn3 = Button(f4, text="3", padx=20, pady=20, command=lambda: btn_click(3))
btn3.grid(row=0, column=2)

btn4 = Button(f4, text="+", padx=20, pady=20, command=lambda: btn_click('+'))
btn4.grid(row=0, column=3)

btn5 = Button(f4, text="4", padx=20, pady=20, command=lambda: btn_click(4))
btn5.grid(row=1, column=0)

btn6 = Button(f4, text="5", padx=20, pady=20, command=lambda: btn_click(5))
btn6.grid(row=1, column=1)

btn7 = Button(f4, text="6", padx=20, pady=20, command=lambda: btn_click(6))
btn7.grid(row=1, column=2)

btn8 = Button(f4, text="-", padx=20, pady=20, command=lambda: btn_click('-'))
btn8.grid(row=1, column=3)

btn9 = Button(f4, text="7", padx=20, pady=20, command=lambda: btn_click(7))
btn9.grid(row=2, column=0)

btn10 = Button(f4, text="8", padx=20, pady=20, command=lambda: btn_click(8))
btn10.grid(row=2, column=1)

btn11 = Button(f4, text="9", padx=20, pady=20, command=lambda: btn_click(9))
btn11.grid(row=2, column=2)

btn12 = Button(f4, text="*", padx=20, pady=20, command=lambda: btn_click('*'))
btn12.grid(row=2, column=3)

btn13 = Button(f4, text="c", padx=20, pady=20, command=clear)
btn13.grid(row=3, column=0)

btn14 = Button(f4, text="=", padx=20, pady=20, command=total)
btn14.grid(row=3, column=2)

btn15 = Button(f4, text="0", padx=20, pady=20, command=lambda: btn_click(0))
btn15.grid(row=3, column=1)

btn16 = Button(f4, text="/", padx=20, pady=20, command=lambda: btn_click('/'))
btn16.grid(row=3, column=3)

#=====================Button===========================================>

buttonTotal = Button(frame2,text="Total",padx=20,pady=10,command=totalVal)
buttonTotal.grid(row=6,column=1)

buttonReset = Button(frame3,text="Reset",padx=20,pady=10,command=reset)
buttonReset.grid(row=6,column=1)

root.mainloop()