import RPi.GPIO as GPIO
import time
#Set to broadcom pin numbers
GPIO.setmode(GPIO.BCM)

#Motor 1 = Pins 17 and 18

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

button1 = 23 #connects to GPIO 23

GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP) #button1 input, activate Pull UP resistor

m1a = GPIO.PWM(17,100)
m1b = GPIO.PWM(18,100)

m1a.start(0)
m1b.stop()
speed=1		#set initial speed to 1


while (True):
	try:
		if GPIO.input(button1)==0: #look for button1 press
			print "Button 1 pressed"
			speed=speed*2	#double speed	
			m1a.ChangeDutyCycle(speed)
			time.sleep(0.5)
			print(motor)
		m1a.stop()
	except(KeyboardInterrupt):
		#And final cleanup
		print "Finishing"
		GPIO.cleanup()
		quit()
