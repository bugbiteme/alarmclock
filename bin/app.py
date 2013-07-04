import alarm_clock
from sys import argv

def print_usage(argv):
  print "Usage: %s HH:MM" % argv[0]
	print "\tHH:\t00-23"
	print "\tMM:\t00-59"
	
try:
	alarm_clock.AlarmClock().enable_alarm_st(argv[1])
	
except ValueError:
	print_usage(argv)
	exit(1)
	
except IndexError:
	print_usage(argv)
	exit(1)

except KeyboardInterrupt:
	print "Disabling alarm"
	exit()
