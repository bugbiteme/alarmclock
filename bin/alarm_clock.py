import time
from datetime import datetime
from os import system
import lightsensor
import voice

class AlarmClock(object):

	def __init__(self):
		self.light_sensor = lightsensor.LightSensor()

	def time_to_string(self, hour, minute):
		if minute < 10: 
			return "%d:0%d" % (hour, minute)
		else: 
			return "%d:%d" % (hour, minute)
			
	def is_time_to_turn_on_alarm(self, hour, minute):
		return getattr(datetime.now(), 'hour') == hour and getattr(datetime.now(), 'minute') == minute
		
	def wait_for_light_on(self):
		while self.light_sensor.light_is_on() != True:
			voice.Voice().say_cl('/usr/games/fortune')
			time.sleep(.5)
			
	def enable_alarm_st(self, time):
		hour_minute = time.split(':')
		self.enable_alarm_int(int(hour_minute[0]), int(hour_minute[1]))
		
	def enable_alarm_int(self, hour, minute):
		alarm_is_enabled = True
		
		while alarm_is_enabled:
			system('clear')
			print datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
			print "\nAlarm set for: %s" % self.time_to_string(hour, minute)
			time.sleep(1)
			
			if self.is_time_to_turn_on_alarm(hour, minute):
				self.wait_for_light_on()
				voice.Voice().say("ALARM DEACTIVATED.")
				alarm_is_enabled = False
			
				
