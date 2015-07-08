from Tkinter import *

""" SIMPLE Tutorial from python-course.eu
root = Tk()

v = IntVar()

Label(root, text = "Choose a programming language:", justify = LEFT, padx = 20).pack()

Radiobutton(root, text = "Python", padx = 20, variable = v, value = 1).pack(anchor = W)

Radiobutton(root, text = "Perl", padx = 20, variable = v, value = 2).pack(anchor = W)

mainloop()
"""


"""
	Use this for choosing campus
"""

root = Tk()
v = StringVar()
v.set(1) #init choice to 1

campuses = [("Livingston", "Livi"), ("Busch", "Busch"), ("Cook/Douglas", "CD"), ("College Ave", "CA")]
def ShowChoice():
 	print v.get()

 
Label(root, text="""Choose your campus:""", justify = LEFT, padx = 20).pack()

for txt, val in campuses:
	Radiobutton(root, 
				text = txt,
				indicatoron = 0,
				width = 20, 
				padx = 20,
				variable = v, 
				command = ShowChoice, 
				value = val).pack(anchor = W)

mainloop()