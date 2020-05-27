import os
import subprocess
from bs4 import BeautifulSoup
from get_answer import Fetcher

class Commander:
	def __init__(self):
		# Confirm or cancel
		self.confirm = ["yes", "sure", "affirmative", "do it", "yeah", "confirm", "yep", "please"]
		self.cancel = ["no", "negative", "cancel", "don't", "wait", "nope", "no thank you"]

	# Determine what was said and what action to perform
	def discover(self, text):
		# Get name
		if "what" in text and "your name" in text:
			if "my" in text and "name" in text:
				self.respond("You have not tole me your name yet")
			else:
				self.respond("My name is python commander. How are you?")
	
		# Open app from cmd prompt
		# elif "open" in text or "launch" or "start" in text: 
			# app = text.split(" ", 1)[-1]
			# self.respond("Opening " + app)
			# os.system("Start " + app + ".exe")

		# Get data from web to answer questions
		else:																
			f = Fetcher("https://www.google.com/search?q=" + text)
			answer = f.lookup()
			self.respond(answer)

	# TTS response output, call from windows, speak response
	def respond(self, response):
		print(response)
		subprocess.call("PowerShell -Command Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('"+ response +"')", shell=True)

