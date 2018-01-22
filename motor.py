#www.theraspberrypiguy.com/raspberry-pi-how-to-control-motors-2
import RPi.GPIO as GPIO
import time
#Set to broadcom pin numbers
GPIO.setmode(GPIO.BCM)

#Motor 1 = Pins 17 and 18
#Motor 2 = Pins 22 and 23
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

print "Starting"

while (True):
	try:
		#Makes the motor spin one way for 3 seconds
		GPIO.output(17, True)
		GPIO.output(18, False)
		time.sleep(.01)
		#pause
		GPIO.output(17, False)
		GPIO.output(18, False)
		time.sleep(1)
		#And now the other way round
		GPIO.output(17, False)
		GPIO.output(18, True);
		time.sleep(3);
		#pause
		GPIO.output(17, False)
		GPIO.output(18, False)
		time.sleep(1)
	except(KeyboardInterrupt):
		#And final cleanup
		print "Finishing"
		GPIO.cleanup()
		quit()
