'''

'''
from Tkinter import *
#from Adafruit_PWM_Servo_Driver import PWM
import time
import RPi.GPIO as GPIO
#Set to broadcom pin numbers
GPIO.setmode(GPIO.BCM)


#Motor 1 = Pins 17 and 18
#Motor 2 = Pins 22 and 23
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

m1a = GPIO.PWM(17,25)
m1b = GPIO.PWM(18,100)

#m1a.start(0)
#m1b.stop()


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=100, to=120,
              orient=HORIZONTAL, length=500, resolution=0.1, command=self.updateh)
        scale.grid(row=0)
        scale.set(110)

        
    def updateh(self,duty):
		m1a.ChangeDutyCycle (0)
		m1a.ChangeDutyCycle (int(float(duty)+25))

		
root = Tk()
root.wm_title('Servo Control')
app = App(root)
root.geometry("550x550+100+100") #w h

root.mainloop()
GPIO.cleanup()
