from tkinter import *


root = Tk()
root.minsize(300, 400)
root.title('Design')

frame1 = Frame(root)
frame1.pack(fill=X, side=TOP)

frame2 = Frame(root)
frame2.pack(fill=X, side=LEFT)

frame3 = Frame(root)
frame3.pack(fill=X, side=RIGHT)

btn1 = Button(frame1, text='File', bd=10, padx=20, pady=20)
btn1.grid(row=0, column=0)

btn2 = Button(frame1, text='Edit', bd=10, padx=20, pady=20)
btn2.grid(row=0, column=1)

btn3 = Button(frame1, text='View', bd=10, padx=20, pady=20)
btn3.grid(row=0, column=2)

btn4 = Button(frame1, text='Clear', bd=10, padx=20, pady=20)
btn4.grid(row=0, column=3)

label1 = Label(frame2, text='This is sidebar.', font=['aerial', 23], bg='blue', fg='Black')
label1.pack(fill=X)

label2 = Label(frame3, text='This is right sidebar.', font=['aerial', 23], bg='red', fg='Black')
label2.pack(fill=X)

root.mainloop()
