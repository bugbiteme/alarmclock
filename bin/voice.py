from subprocess import call
import random
import string
from os import remove

DEBUG = False

class Voice(object):
	
	def __init__(self):
		self.sentence = "I have nothing to say right now"
		self.pitch = 20
		self.accent = 'en'
	
	def say(self, sentence=None):
		if sentence is None:
			sentence = self.sentence
		
		#random named file four characters long	
		sound_file = ''.join(random.choice(string.lowercase) for x in range(4))
		
		command = "espeak -v%s+m6 -k5 -s150 -g 2 -p %d \"%s\" > /dev/null -w %s 2>&1; sudo aplay %s > /dev/null 2>&1" % (self.accent, self.pitch, sentence, sound_file, sound_file)
		
		if DEBUG: print command
		call(command, shell=True)
		
		remove(sound_file)
		
	def say_cl(self, cl=None):
		if cl is None:
			cl = "echo \"%s\"" % self.sentence
		
		#random named file four characters long
		sound_file = ''.join(random.choice(string.lowercase) for x in range(4))
		
		command = "%s | espeak -v%s+m6 -k5 -s150 -g 2 -p %d -w %s > /dev/null 2>&1; sudo aplay %s > /dev/null 2>&1" % (cl, self.accent, self.pitch, sound_file, sound_file)
		
		if DEBUG: print command	
		call(command, shell=True)	
		
		remove(sound_file)
	
	# Changes pitch of voice (1-99) default = 20
	def change_pitch(self, pitch):
		self.pitch = pitch
		
	# type "espeak --voices" to get a list of all possible accents
	# 'en' is the default
	def change_accent(self, accent):
		self.accent = accent
		


		