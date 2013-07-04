
import RPi.GPIO as GPIO, time, os      
from subprocess import call

DEBUG = False
GPIO.setmode(GPIO.BCM)

LIGHT_SENSOR = 25

class LightSensor(object):
	
	def __init__(self):
		self.rc_pin = LIGHT_SENSOR
		
	def rc_time(self):
		reading = 0
		GPIO.setup(self.rc_pin, GPIO.OUT)
		GPIO.output(self.rc_pin, GPIO.LOW)
		time.sleep(0.1)
 
		GPIO.setup(self.rc_pin, GPIO.IN)
		# This takes about 1 millisecond per loop cycle
		while (GPIO.input(self.rc_pin) == GPIO.LOW):
			reading += 1
		
		return reading
		
	def light_is_on(self):
		reading = self.rc_time()
		if reading > 400:
			return False
		else:
			return True