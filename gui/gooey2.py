import Tkinter

class Prompt:
	def button_action(self):
		self.my_entry = self.busch.get()
		print self.my_entry

	def __init__(self, den):
		self.ent = Tkinter.Entry(den)
		self.livi = Tkinter.Button(den, text = "Livi", command = self.button_action)
		self.busch = Tkinter.Button(den, text = "Busch", command = self.button_action)
		self.lbl.pack()
		self.ent.pack()
		self.btn.pack()

den = Tkinter.Tk()
prompt = Prompt(den)
den.mainloop()