from Tkinter import *

def campusChosen(c):
	print c

root = Tk()

campuses = ['Livingston', 'Busch', 'Cook/Douglas', 'College Avenue']
r = 0

for c in campuses:
	Button(text = c, relief = RIDGE, width = 15, command = campusChosen(c)).grid(row = r, column = 0)
	r += 1

root.wm_title("RU Studying")
mainloop()