from Tkinter import *
import tkMessageBox
import Tkinter

top = Tk()

mb = Menubutton(top, text = "Condiments", relief = RAISED)
mb.grid()
mb.menu = Menu(mb, tearoff = 0)
mb["menu"] = mb.menu

i = 1
for i in range(1, 10):
	mb.menu.add_checkbutton(label = str(i))


mb.pack()
top.mainloop()