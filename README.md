alarmclock
==========

Talking alarm clock for raspberry pi. Uses light sensor with GPIO

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

