from tkinter import *

root = Tk()

root.minsize(600, 500)
menu = Menu(root)
root.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='New')
fileMenu.add_command(label='Open')
fileMenu.add_command(label='Save')
fileMenu.add_command(label='Save As')
fileMenu.add_separator()
fileMenu.add_command(label='Share')

root.mainloop()
