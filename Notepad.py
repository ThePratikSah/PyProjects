from tkinter import *

root = Tk()

root.minsize(500, 400)
root.title('Notepad')
# root.iconbitmap('path of the icon')
option = ('file', 'edit', 'save', 'close')

menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New')
file_menu.add_command(label='Open')
text = StringVar()
text.set(option[0])
option_menu = OptionMenu(root, text, *option)
option_menu.pack()
text = Text(root, font=['aerial', 20])
text.pack(fill=X)
root.mainloop()
