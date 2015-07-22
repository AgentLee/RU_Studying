from Tkinter import *

class App:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		
		self.button = Button(frame, text = "Quit", fg = "red", command = frame.quit)
		self.button.pack(side = BOTTOM)

		livi = Button(frame, text = "Livingston", command = self.write_slogan)
		livi.pack(side = LEFT)

		busch = Button(frame, text = "Busch", command = self.write_slogan)
		busch.button.pack(side = LEFT)

		cd = Button(frame, text = "Cook/Douglas", command = self.write_slogan)
		cd.button.pack(side = LEFT)

		collegeave.button = Button(frame, text = "College Ave", command = self.write_slogan)
		collegeave.button.pack(side = LEFT)

	def write_slogan(self):
		print 

root = Tk()
app = App(root)
root.mainloop()
