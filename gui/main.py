import Tkinter
from Tkinter import *
import time
import urllib2
import json

def splash(selection):
	campus = selection
	currTime = time.strftime("%I:%M")
	currDay = time.strftime("%a")

	label.config(text = selection)
	timeLabel = Label(f)
	timeLabel.pack()
	timeLabel.config(text = currDay + "\n" + currTime)

def sel():
	if var.get() == 1:
		selection = "Livingston"
	elif var.get() == 2:
		selection = "Busch"
	elif var.get() == 3:
		selection = "Cook/Douglas"
	elif var.get() == 4:
		selection = "College Ave"

	label.config(text = selection)

	livi.pack_forget()
	bus.pack_forget()
	cd.pack_forget()
	ca.pack_forget()

	splash(selection)

def selectCampus():
	global var, label, livi, bus, cd, ca
	var = IntVar()

	livi = Radiobutton(root, text = "Livingston", variable = var, value = 1, command = sel)
	bus = Radiobutton(root, text = "Busch", variable = var, value = 2, command = sel)
	cd = Radiobutton(root, text = "Cook/Douglas", variable = var, value = 3, command = sel)
	ca = Radiobutton(root, text = "College Ave", variable = var, value = 4, command = sel)

	livi.pack(anchor = W)
	bus.pack(anchor = W)
	cd.pack(anchor = W)
	ca.pack(anchor = W)

	label = Label(f)
	label.pack()

def main():
	global root, f
	root = Tk()
	f = Frame(root, width = 500, height = 500)
	f.pack(fill=X, expand = True)
	f.pack_propagate(0)

	selectCampus()

	root.wm_title("RU Studying")
	root.mainloop()

main()