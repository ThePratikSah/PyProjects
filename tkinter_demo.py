from tkinter import *
# import random

root = Tk()
# declaring the size of the window
root.minsize(250, 250)
root.maxsize(250, 250)

# title of the window
root.title('Password generator')
text1 = Label(text='Size of characters for your password:')
text1.pack()
# entry for the user
entry = Entry(root, bd=5)
entry.pack()

# button for the user
btnGenerate = Button(root, text='Generate', bd=20)
btnGenerate.pack()

# display to print the generated password
display = Entry(root, bd=5)
display.pack()

root.mainloop()

