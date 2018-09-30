from tkinter import *


root = Tk()
root.title("Pratik calculator by Python")
root.minsize(220, 400)


def clear():
    display.delete(0, END)
    return


val = StringVar()


def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    val.set(operator)


def total():
    global operator
    val.set(str(eval(operator)))
    operator = ""


operator = ""

frame1 = Frame(root)
frame1.pack(fill=X,side=TOP)

frame2 = Frame(root)
frame2.pack(side=TOP)

frame3 = Frame(root)
frame3.pack(fill=X, side=BOTTOM)

credit = Label(frame3, text="Design by SadiQ")
credit.pack(fill=X)
display = Entry(frame1, bd=10, textvariable=val)
display.pack(fill=X)

btn1 = Button(frame2, text="1", bd=10, padx=20, pady=20, command=lambda: btnclick(1))
btn1.grid(row=0,column=0)

btn2 = Button(frame2, text="2", bd=10, padx=20, pady=20, command=lambda: btnclick(2))
btn2.grid(row=0, column=1)

btn3 = Button(frame2, text="3", bd=10, padx=20, pady=20, command=lambda : btnclick(3))
btn3.grid(row=0, column=2)

btn4 = Button(frame2,text="+",bd=10,padx=20,pady=20,command=lambda : btnclick('+'))
btn4.grid(row=0,column=3)


btn5 = Button(frame2,text="4",bd=10,padx=20,pady=20,command=lambda : btnclick(4))
btn5.grid(row=1,column=0)

btn6 = Button(frame2,text="5",bd=10,padx=20,pady=20,command=lambda : btnclick(5))
btn6.grid(row=1,column=1)

btn7 = Button(frame2,text="6",bd=10,padx=20,pady=20,command=lambda : btnclick(6))
btn7.grid(row=1,column=2)

btn8 = Button(frame2,text="-",bd=10,padx=20,pady=20,command=lambda : btnclick('-'))
btn8.grid(row=1,column=3)


btn9 = Button(frame2,text="7",bd=10,padx=20,pady=20,command=lambda : btnclick(7))
btn9.grid(row=2,column=0)

btn10 = Button(frame2,text="8",bd=10,padx=20,pady=20,command=lambda : btnclick(8))
btn10.grid(row=2,column=1)

btn11 = Button(frame2,text="9",bd=10,padx=20,pady=20,command=lambda : btnclick(9))
btn11.grid(row=2,column=2)

btn12 = Button(frame2,text="*",bd=10,padx=20,pady=20,command=lambda : btnclick('*'))
btn12.grid(row=2,column=3)

btn13 = Button(frame2,text="c",bd=10,padx=20,pady=20,command=clear)
btn13.grid(row=3,column=0)

btn14 = Button(frame2,text="=",bd=10,padx=20,pady=20,command=total)
btn14.grid(row=3,column=1)

btn15 = Button(frame2,text="0",bd=10,padx=20,pady=20,command=lambda : btnclick(0))
btn15.grid(row=3,column=2)
btn16 = Button(frame2,text="/",bd=10,padx=20,pady=20,command=lambda : btnclick('/'))
btn16.grid(row=3,column=3)
root.mainloop()