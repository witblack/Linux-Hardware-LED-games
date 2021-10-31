#!/usr/bin/python

from os import system,name
from time import sleep

def leds(a,b,c):
	system('echo ' + str(a) + ' > /sys/class/leds/input23::numlock/brightness')
	system('echo ' + str(b) + ' > /sys/class/leds/input23::capslock/brightness')
	system('echo ' + str(c) + ' > /sys/class/leds/input23::scrolllock/brightness')
if name != 'posix':
	print("This program not for your OS. use Linux.")
else:
	leds(0,0,0)
	while True:
		leds(1,0,0)
		sleep(0.5)
		leds(0,1,0)
		sleep(0.5)
		leds(0,0,1)
		sleep(0.5)
