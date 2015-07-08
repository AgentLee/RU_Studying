import Tkinter as tk

class App:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		self.button = Button(frame, text = "QUIT", fg = "red", command = frame.quit)
		self.button.pack(side = LEFT)
		
		self.slogan = Button(frame, text = "hello", command = self.write_slogan)
		self.slogan.pack(side = LEFT)

	def write_slogan(self):
		print "Tkinter is easy"


counter = 0

def counter_label(label):
	counter = 0

	def count():
		global counter
		counter += 1
		label.config(text = str(counter))
		label.after(1000, count)

	count()

root = tk.Tk()
root.title("Counting Sounds")

label = tk.Label(root, fg = "dark green")
label.pack()

counter_label(label)
button = tk.Button(root, text = 'Stop', width = 25, command = root.destroy)
button.pack()

#app = App(root)
root.mainloop()