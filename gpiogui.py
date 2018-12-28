#http://www.pibits.net/learning/basic-python-gpio-gui-example.php
from Tkinter import *
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
 
class App:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		self.check_var = BooleanVar()
		check = Checkbutton(frame, text='Pin 17',
			command=self.update,
			variable=self.check_var, onvalue=True, offvalue=False)
		check.grid(row=1)
 
	def update(self):
		GPIO.output(17, self.check_var.get())
 
root = Tk()
root.wm_title('GPIO GUI Example')
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()
 
