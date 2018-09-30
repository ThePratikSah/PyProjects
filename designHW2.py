from tkinter import *

root = Tk()

root.minsize(215, 355)

root.title('Layout3')
f1 = Frame(root)
f2 = Frame(root)

f1.pack(fill=X, side=TOP)
f2.pack(fill=X, side=TOP)

label1 = Label(f1, text='       ', bg='black', padx=30, pady=20)
label1.pack(fill=X, side=TOP)

label2 = Label(f1, text='       ', bg='grey', padx=30, pady=20)
label2.pack(fill=X, side=TOP)

btn00 = Label(f2, text=' ', bg='black', padx=30, pady=30)
btn00.grid(row=0, column=0)

btn01 = Label(f2, text=' ', bg='white', padx=30, pady=30)
btn01.grid(row=0, column=1)

btn02 = Label(f2, text=' ', bg='black', padx=30, pady=30)
btn02.grid(row=0, column=2)

btn10 = Label(f2, text=' ', bg='white', padx=30, pady=30)
btn10.grid(row=1, column=0)

btn11 = Label(f2, text=' ', bg='black', padx=30, pady=30)
btn11.grid(row=1, column=1)

btn12 = Label(f2, text=' ', bg='white', padx=30, pady=30)
btn12.grid(row=1, column=2)

btn20 = Label(f2, text=' ', bg='black', padx=30, pady=30)
btn20.grid(row=2, column=0)

btn21 = Label(f2, text=' ', bg='white', padx=30, pady=30)
btn21.grid(row=2, column=1)

btn22 = Label(f2, text=' ', bg='black', padx=30, pady=30)
btn22.grid(row=2, column=2)

root.mainloop()
