alarmclock
==========

Talking alarm clock for Raspberry Pi. Uses light sensor with GPIO

OVERVIEW
--------

This is an alarm clock. Once the alarm is set the clock waits for the alarm to be triggered

Once the alarm is triggered, it will continuously start talking, speaking the output from the 
classic 'fortune' unix application until you turn on the light.

The light sensor will detect that the light is on, and the alarm clock will shut up.

PREREQS
-------

- espeak : the voice (apt-get install espeak)
- fortune: the words (apt-get install fortune)
- GPIO python libraries


USAGE
-------

sudo python bin/app.py <HH:MM>

- HH : hour (0-29)
- MM : minute (00-59)

example:
$sudo python alarmclock/bin/app.py 


Note: sudo is needed in order to access the GPIO inputs (light sensor)

light sensor is set to GPIO pin 25 (can modify in lightsensor.py)

More information can be found here:
http://roverpi.blogspot.com/2013/07/sidetracked-using-light-sensor-on.html
