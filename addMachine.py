from tkinter import *

root = Tk()

# defining the min size
root.minsize(300, 400)

# title
root.title('Add machine')

# defining the main function


def add():
    total = int(input1.get()) + int(input2.get())
    display.config(text=str(total))


# frames
f1 = Frame(root)
f2 = Frame(root)
f1.pack(side=TOP, fill=X)
f2.pack(side=TOP, fill=X)

# label
l1 = Label(f1, text='Add this!', font=['arial', 20], bg='red', fg='white')
l1.pack(fill=X)

#Gender label
genderMale = Checkbutton(root, text="Male").pack()
genderFemale = Checkbutton(root, text="Female").pack()


# entry for the machine
input1 = Entry(f2)
input2 = Entry(f2)

input1.pack(pady=10)
input2.pack(pady=10)

add = Button(f2, text='Calculate', fg='black', bg='red', padx=10, command=add)
add.pack(pady=10, side=TOP)

display = Label(f2)
display.pack(fill=X, pady=20)

root.mainloop()
