import os
import traceback
import time

def clear():
	if os.name == 'nt':
		 _ = os.system('cls')
	else:
		_ = os.system('clear')

clear()
print("   _____ _   _          _  ________ \n  / ____| \\ | |   /\\   | |/ /  ____|")
time.sleep(0.5)
print(" | (___ |  \\| |  /  \\  | ' /| |__   \n  \\___ \\| . ` | / /\\ \\ |  < |  __|  ")
time.sleep(0.5)
print("  ____) | |\\  |/ ____ \\| . \\| |____ \n |_____/|_| \\_/_/    \\_\\_|\\_\\______|")
print("              in Python")
time.sleep(1)
print("\nChecking for Curses library...", end = "")
time.sleep(1)
try:
	import snake
except Exception:
	print("  ERROR\nWhere is snake.py? Did you forget to copy it into the same folder as this script, or did you rename or delete it?")
	input()
	clear()
	exit()
print("  OK\nSetting up variables...", end = "")
time.sleep(1.5)
score = 0
counter = 0
snakebump = 1
turn_head = 0
dead_border = 1
maxscore = 100
print("  OK\nDefining functions...", end = "")
time.sleep(1.5)

def set_default(mode):
	if mode == 0 or mode == 1 or mode == 3:
		return 0
	elif mode == 2 or mode == 4:
		return 1
	else:
		return 100

def set_score(lastscore):
	clear()
	scoretoset = 0
	print("PYTHON SNAKE GAME LAUNCHER")
	print("Okay, type in the score you wanna start with.\nIt must be at least 0, or your score won't be set.\nPlease note: this does not affect the snake's length!\n")
	scoretoset = input("Score: ")
	scoretoset = int(scoretoset)
	if scoretoset < 0:
		return lastscore
	else:
		return scoretoset	

def set_counter(lastmode):
	clear()
	modetoset = 0
	print("PYTHON SNAKE GAME LAUNCHER")
	print("Okay, choose a display mode. (Inputting invalid numbers will not change the display mode)\n")
	print("[1] Score Display\n[2] Key & Previous Key Display [DEBUG]\n[3] Key & Previous Key Display (Translated Inputs) [DEBUG]\n[4] Speed Display [DEBUG]\n")
	modetoset = input("Your choice: ")
	modetoset = int(modetoset)
	if modetoset > 4 or modetoset < 1:
		return lastmode
	else:
		if modetoset == 1: return 0
		elif modetoset == 2: return 1
		elif modetoset == 3: return 2
		elif modetoset == 4: return 3

def set_snakebump(lastvalue):
	clear()
	choice = 0
	print("PYTHON SNAKE GAME LAUNCHER")
	print("Do you want the snake to be able to run over itself?\n\n[1] Yes\n[2] No\n\nInputting invalid numbers won't change the flag!\n")
	choice = input("Your choice: ")
	choice = int(choice)
	if choice < 1 or choice > 2:
		return lastvalue
	else:
		if choice == 1: return 0
		elif choice == 2: return 1 	

def set_turnhead(lastvalue):
	clear()
	choice = 0
	print("PYTHON SNAKE GAME LAUNCHER")
	print("Do you want the snake to be able to turn around?\n\n[1] Yes\n[2] No\n\nInputting invalid numbers won't change the flag!\n")
	choice = input("Your choice: ")
	choice = int(choice)
	if choice < 1 or choice > 2:
		return lastvalue
	else:
		if choice == 1: return 1
		elif choice == 2: return 0 	

def set_barrier(lastvalue):
	clear()
	choice = 0
	print("PYTHON SNAKE GAME LAUNCHER")
	print("Do you want the snake to die when it touches the border?\n\n[1] Yes\n[2] No\n\nInputting invalid numbers won't change the flag!\n")
	choice = input("Your choice: ")
	choice = int(choice)
	if choice < 1 or choice > 2:
		return lastvalue
	else:
		if choice == 1: return 1
		elif choice == 2: return 0

def set_maxscore(lastscore):
	clear()
	scoretoset = 0
	print("PYTHON SNAKE GAME LAUNCHER")
	print("Okay, type in the score you have to get to win in the Limited Apples mode.\nIt must be at least 1, or your score won't be set.\n")
	scoretoset = input("Maximum Score: ")
	scoretoset = int(scoretoset)
	if scoretoset < 1:
		return lastscore
	else:
		return scoretoset

def launch_game(score, counter, snakebump, turn_head, dead_border, maxscore):
	while True:
		clear()
		choice = 0
		print("PYTHON SNAKE GAME LAUNCHER")
		print("Please select a game mode.\n\n[1] Classic\n[2] Limited Apples\n[3] Back\n")
		choice = input("Your choice: ")
		choice = int(choice)
		if choice == 3: break
		if choice == 1:
			while True:
				clear()
				choice2 = 0
				print("PYTHON SNAKE GAME LAUNCHER")
				print("Classic mode:\nPlay Snake forever!... until you die or hit ESCAPE.\n\n[1] Play  [2] Back\n")
				choice2 = input("Your choice: ")
				choice2 = int(choice2)
				if choice2 == 2: break
				else:
					clear()
					snake.maingame(score, counter, snakebump, turn_head, dead_border, 0)
				return
		if choice == 2:
			while True:
				clear()
				choice2 = 0
				print("PYTHON SNAKE GAME LAUNCHER")
				if score >= maxscore or maxscore - score == 1: print("Limited Apples mode:\nCollect an apple to win! Easy, right?\n")
				else: print("Limited Apples mode:\nCollect " + str(maxscore - score) + " apples to win!\n")
				print("[1] Play  [2] Back\n")
				choice2 = input("Your choice: ")
				choice2 = int(choice2)
				if choice2 == 2: break
				else:
					clear()
					if score >= maxscore:
						snake.maingame(score, counter, snakebump, turn_head, dead_border, score + 1)
					else: snake.maingame(score, counter, snakebump, turn_head, dead_border, maxscore)
				return
		else:
			pass
	return

print("  OK\nDone!")
time.sleep(1)

while True:
	clear()
	select = 0

	if counter == 1: counter_str = "Key & Previous Key Display"
	elif counter == 2: counter_str = "Key & Previous Key Display - Translated Inputs"
	elif counter == 3: counter_str = "Speed Display"
	else: counter_str = "Score Display"

	if snakebump == 1: snakebump_str = "Disabled"
	else: snakebump_str = "Enabled"

	if turn_head == 1: turn_head_str = "Enabled"
	else: turn_head_str = "Disabled"

	if dead_border == 1: dead_border_str = "Enabled"
	else: dead_border_str = "Disabled"

	print("PYTHON SNAKE GAME LAUNCHER")
	print("Welcome! Here, you can set some flags in the Snake game.\n")
	print("[1] Launch game\n[2] Set starting score                       (currently: " + str(score) + ")\n[3] Set display mode                         (currently: " + str(counter_str) + ")\n[4] Enable/disable snake running over itself (currently: " + str(snakebump_str) + ")\n[5] Toggle turning around                    (currently: " + str(turn_head_str) + ")\n[6] Toggle death border                      (currently: " + str(dead_border_str) + ")\n[7] Set Limited Apples mode maximum score    (currently: " + str(maxscore) + ")\n[8] Set to defaults\n[9] Exit launcher\n")
	try:
		select = input("Your choice: ")
		select = int(select)
		if select < 1 or select > 9:
			pass
		else:
			if select == 9:
				clear()
				exit()
			if select == 1: launch_game(score, counter, snakebump, turn_head, dead_border, maxscore)
			if select == 2: score = set_score(score)
			if select == 3: counter = set_counter(counter)
			if select == 4: snakebump = set_snakebump(snakebump)
			if select == 5: turn_head = set_turnhead(turn_head)
			if select == 6: dead_border = set_barrier(dead_border)
			if select == 7: maxscore = set_maxscore(maxscore)
			if select == 8:
				score = set_default(0)
				counter = set_default(1)
				snakebump = set_default(2)
				turn_head = set_default(3)
				dead_border = set_default(4)
				maxscore = set_default(5)
	except Exception:
		clear()
		print("My my! An error occured! Screw you!\n")
		print(traceback.format_exc())
		print("If this error isn't a ValueError, please contact the creator at thenewgwe@gmail.com")
		print("\nPress any key to return to the menu.")
		input()
		pass