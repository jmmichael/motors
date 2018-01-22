##Simple motor script for the RTK-000-001
import RPi.GPIO as GPIO
import time
#Set to broadcom pin numbers
GPIO.setmode(GPIO.BCM)

#Motor 1 = Pins 17 and 18
#Motor 2 = Pins 22 and 23
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

m1a = GPIO.PWM(17,100)
m1b = GPIO.PWM(18,100)

m1a.start(0)
m1b.stop()

#Now loop forever turning one direction for 5 seconds, then the other
while (True):
	try:
		for motor in range (0,101,1): #starts at 0, steps up to 101 in 1 steps
			m1a.ChangeDutyCycle(motor)
			time.sleep(0.5)
			print(motor)
		m1a.stop()
		m1b.start(0)	
		for motor in range (100,-1,-1):
			m1b.ChangeDutyCycle(motor)
			time.sleep(0.5)
			print(motor)
		m1b.stop()
	except(KeyboardInterrupt):
		#And final cleanup
		print "Finishing"
		GPIO.cleanup()
		quit()
