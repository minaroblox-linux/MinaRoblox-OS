from colorama import Fore, Back, Style
import colorama
from scripts.apps import App

# import colorama
# start colorama

colorama.init(autoreset=True)

# functions for making easier

def printColor(colour, text):
	# Define a dictionary to map color names to Fore attributes
	colors = {

		"red": Fore.RED,
		"green": Fore.GREEN,
		"yellow": Fore.YELLOW,
		"blue": Fore.BLUE,
		"purple": Fore.MAGENTA,
		"cyan": Fore.CYAN,
		"white": Fore.WHITE
		
	}

	code = colors.get(colour.lower(), Fore.WHITE)

	print(f"{code}{text}")

# code start

import time
import random
import os

# some function

def clear():
	os.system("clear")

def load_animation():
	random_booting_time = random.randint(10, 20)
	time_repeated = 0
	running = True
	symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
	

	while running:
		for symbol in symbols:
			clear()
			print(symbol)
			time.sleep(0.1)

		time_repeated += 1

		if time_repeated == random_booting_time:
			running = False

# booting up

time.sleep(3)

clear()

printColor("cyan", """

		MINAROBLOX OS
		DESIGNED IN PYTHON
		COMPILED WITH PYINSTALLER

		VERSION 1.0.0


""")

time.sleep(random.randint(5, 7))

# loading animation

load_animation()

booted_up = True
printColor("cyan" ,f"""

		WELCOME TO MINAROBLOX OS
		TYPE HELP.SH FOR AVAILIBLE APPS
		VERSION 1.0.0

	""")

# main loop

debug_mode = False

while booted_up:

	# register user input

	command_input = input("./")

	# help command

	if command_input == "HELP.SH":
		printColor("green","""

			ALL APPS:
		
			CALCULATOR.SH
			PASSWORD_GENERATOR.SH
			HANGMAN.SH
			ROCK_PAPER_SCISSORS.SH
			COUNTDOWN.SH
			DOLLARS_TO_PESOS.SH 
		
			ALL COMMANDS:
		
			OPEN {app_name} / OPENS THE APP IN
			THE app_name PART
		
			TURN_OFF / TURNS OFF THE COMPUTER
		
			HELP / SHOWS THIS SCREEN
		
		""")

	# commads

	elif debug_mode and command_input == "PROGRESS":
		printColor("purple","""

			CALC = DONE
			PASS_GEN = DONE
			HANGMAN = DONE
			ROCK = DONE
			COUNT = DONE
			DOLL = DONE

			""")

	elif command_input == "CLEAR":
		clear()
	
	# calculator app

	elif command_input == "OPEN CALCULATOR.SH":
		App.calculator()
		clear()

	# password gen app

	elif command_input == "OPEN PASSWORD_GENERATOR.SH":
		App.password_generator()
		clear()

	# countdown app
	
	elif command_input == "OPEN COUNTDOWN.SH":
		App.countdown()
		clear()

	# dollars to pesos

	elif command_input == "OPEN DOLLARS_TO_PESOS.SH":
		App.dollars_to_pesos()
		clear()

	# hangman (hardest game to program)

	elif command_input == "OPEN HANGMAN.SH":
		App.hangman()
		clear()

	# rock paper scissors

	elif command_input == "OPEN ROCK_PAPER_SCISSORS.SH":
		App.rock_paper_scissors()
		clear()

	# command open empty

	elif command_input == "OPEN":
		print("""
		
		PLEASE ENTER {app_name}.SH

		""")


	# the thing didnt exist

	else:
		print(f"""

			FILE/COMMAND DOES NOT EXIST
			{command_input}

		""")
	