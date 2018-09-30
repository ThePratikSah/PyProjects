from tkinter import *

root = Tk()

root.minsize(278, 200)

root.title('Layout2')
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)

f1.pack(fill=X, side=TOP)
f2.pack(fill=Y, side=LEFT)
f3.pack(fill=X, side=TOP)
f4.pack(fill=X, side=TOP)

label1 = Label(f1, text='       ', bg='white', padx=30, pady=30)
label1.pack(fill=X, side=TOP)

label2 = Label(f2, text='       ', bg='red', padx=30, pady=30)
label2.pack(fill=Y, side=LEFT)

label3 = Label(f3, text='       ', bg='blue', padx=30, pady=30)
label3.pack(fill=X, side=TOP)

label3 = Label(f3, text='       ', bg='orange', padx=30, pady=30)
label3.pack(fill=X, side=TOP)


root.mainloop()
