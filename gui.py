import tkinter
from tkinter import *

root = Tk()
root.minsize(300, 400)
root.title('Calculator')
root.config(bg='black')

frame1 = Frame(root)
frame1.pack(fill=X, side=TOP)

display = Entry(frame1, bd=30)
display.pack(fill=X)


frame2 = Frame(root)
frame2.pack(fill=X, side=TOP)

btn1 = Button(frame2, text='1', bd=10, padx=20, pady=20)
btn1.grid(row=0, column=0)

btn2 = Button(frame2, text='2', bd=10, padx=20, pady=20)
btn2.grid(row=0, column=1)

btn3 = Button(frame2, text='3', bd=10, padx=20, pady=20)
btn3.grid(row=0, column=2)

btn4 = Button(frame2, text='+', bd=10, padx=20, pady=20)
btn4.grid(row=0, column=3)

btn5 = Button(frame2, text='4', bd=10, padx=20, pady=20)
btn5.grid(row=1, column=0)

btn6 = Button(frame2, text='5', bd=10, padx=20, pady=20)
btn6.grid(row=1, column=1)

btn7 = Button(frame2, text='6', bd=10, padx=20, pady=20)
btn7.grid(row=1, column=2)

btn8 = Button(frame2, text='-', bd=10, padx=20, pady=20)
btn8.grid(row=1, column=3)

btn9 = Button(frame2, text='7', bd=10, padx=20, pady=20)
btn9.grid(row=2, column=0)

btn10 = Button(frame2, text='8', bd=10, padx=20, pady=20)
btn10.grid(row=2, column=1)

btn11 = Button(frame2, text='9', bd=10, padx=20, pady=20)
btn11.grid(row=2, column=2)

btn12 = Button(frame2, text='*', bd=10, padx=20, pady=20)
btn12.grid(row=2, column=3)

btn13 = Button(frame2, text='C', bd=10, padx=20, pady=20)
btn13.grid(row=3, column=0)

btn14 = Button(frame2, text='0', bd=10, padx=20, pady=20)
btn14.grid(row=3, column=1)

btn15 = Button(frame2, text='=', bd=10, padx=20, pady=20)
btn15.grid(row=3, column=2)

btn16 = Button(frame2, text='/', bd=10, padx=20, pady=20)
btn16.grid(row=3, column=3)

root.mainloop()
