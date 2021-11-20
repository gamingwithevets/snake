import os
from random import randint
from decimal import *

# game logic

# score set when starting the game. do not change unless you like to cheat!
score = 0

# 0: score (default)
# 1: key and prev. key counter
# 2: same as 1, but translated into readable inputs
# 3: snake speed
counter = 0

# set to zero to make the snake able to run over itself
snakebump = 1

# set to 0 to disable turning around
turn_head = 0

# 0: lets the snake go through the border to the other side
# 1: the border kills the snake
dead_border = 1

# max score for Limited Apples mode; set to 0 or lower to switch to Classic mode
maxscore = 0

def maingame(score, counter, snakebump, turn_head, dead_border, maxscore):
	try:
		import curses
	except Exception:
		if os.path.exists(os.getenv('LOCALAPPDATA') + "\\Programs\\Python\\Python39") or os.path.exists(os.getenv('LOCALAPPDATA') + "\\Programs\\Python\\Python38") or os.path.exists(os.getenv('LOCALAPPDATA') + "\\Programs\\Python\\Python37") or os.path.exists(os.getenv('LOCALAPPDATA') + "\\Programs\\Python\\Python36") or os.path.exists(os.getenv('LOCALAPPDATA') + "\\Programs\\Python\\Python35"):
			print("Hey you! You need the Curses library! Just use pip to install the module and you're done!\nSimple as that! Now scram!!!!")
		else:
			print("Hey you! You need the Curses library! As of 2021, Python 3.10 doesn't have that yet.\nSo, you need Python 3.6-3.9. Now scram!!!!")
		return;
	curses.initscr()

	# init colors
	curses.start_color()
	curses.use_default_colors()
	curses.init_pair(1, 0, curses.COLOR_RED)
	curses.init_pair(2, 0, curses.COLOR_BLUE)
	curses.init_pair(3, 0, curses.COLOR_GREEN)
	curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLUE)

	# setup window
	width = 40
	height = 20
	win = curses.newwin(height,width,0,0) #y,x
	win.keypad(1)
	curses.noecho()
	curses.curs_set(0)
	win.bkgd(' ', curses.color_pair(2))
	win.border(0)
	win.nodelay(1) # -1

	# snake and food
	snake = [(4,10), (4,9), (4,8)]
              #head  #body #tail
	food = (randint(5,height-5), randint(5,width-5))

	win.addch(food[0], food[1], ' ')

	ESC = 27
	prev_key = curses.KEY_RIGHT
	key = prev_key

	# prevent immediate win in Limited Apples mode
	# and also starting scores beyond the max score
	if maxscore != 0 and score >= maxscore: score = maxscore - 1

	while key != ESC:
		# end the game prematurely when score hits max score
		if maxscore != 0 and score == maxscore: break

		# initialize board
		speed = 150 - (len(snake)) // 5 + len(snake)//100 % 120
		if counter == 0: win.addstr(0, 2, 'Score: ' + str(score) + ' ',  curses.color_pair(4))
		else:
			if counter == 2:
				prev_key_str = 'Right'
				key_str = prev_key_str
				if prev_key == 258: prev_key_str = 'Down '
				elif prev_key == 259: prev_key_str = 'Up   '
				elif prev_key == 260: prev_key_str = 'Left '
				else: prev_key_str = 'Right'
				if key == 258: key_str = 'Down '
				elif key == 259: key_str = 'Up   '
				elif key == 260: key_str = 'Left '
				elif key == 261: key_str = 'Right'
				elif key == -1: key_str = 'None '
				else: key_str = 'Other'
				win.addstr(0, 2, 'Key: ' + str(key_str) + '  ' + 'Prev. Key: ' + str(prev_key_str) + ' ',  curses.color_pair(4))
			elif counter == 3:
					getcontext().prec = 3
					speed_str = Decimal(speed) / Decimal(20)
					win.addstr(0, 2, 'Speed: ' + str(speed_str) + ' tile(s)/s ',  curses.color_pair(4))    
			else:
				win.addstr(0, 2, 'Key: ' + str(key) + '  ' + 'Prev. Key: ' + str(prev_key) + ' ',  curses.color_pair(4))    
		win.timeout(speed) #increase speed

		event = win.getch()
		key = event

		# calculate the next coordinates
		y = snake[0][0]
		x = snake[0][1]
		if turn_head == 0:
			if (key == curses.KEY_DOWN and prev_key != curses.KEY_UP or 
			key == curses.KEY_UP and prev_key != curses.KEY_DOWN or
			key == curses.KEY_RIGHT and prev_key != curses.KEY_LEFT or
			key == curses.KEY_LEFT and prev_key != curses.KEY_RIGHT):
				prev_key = key
		else:
			if key in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN]:
				prev_key = key

		if prev_key == curses.KEY_DOWN:
			y += 1
		if prev_key == curses.KEY_UP:
			y -= 1
		if prev_key == curses.KEY_RIGHT:
			x += 1
		if prev_key == curses.KEY_LEFT:
			x -= 1

		#if snake runs over itself
		if snakebump == 1:
			if snake[0] in snake[1:]: break

		# check if we hit the border
		if dead_border == 1:
			if y == 1: break
			if y == height -1: break
			if x == 1: break
			if x == width -1: break
		else:
			if y == 0: y = height - 2
			elif y == height -1: y = 1
			if x == 0: x = width - 2
			elif x == width -1: x = 1

		snake.insert(0, (y,x)) # snake head

		if snake[0] == food:
			# eat the food
			score += 1
			food = ()
			while food == ():
				food = (randint(1,height-2), randint(1,width-2))
				if food in snake:
					food = ()
			win.addch(food[0], food[1], ' ',  curses.color_pair(1))
		else:
			# move snake
			last = snake.pop()
			win.addch(last[0], last[1], ' ',  curses.color_pair(2))
		win.addch(snake[0][0], snake[0][1], ' ',  curses.color_pair(3))

		for c in snake:
			win.addch(c[0], c[1], ' ',  curses.color_pair(3))
		win.addch(food[0], food[1], ' ',  curses.color_pair(1))

	curses.endwin()
	if key == ESC:
		print(f"Game exited with ESCAPE/CTRL+[.")
		print(f"Score: {score}")
		return

	if maxscore > 0:
		if score != maxscore: print(f"You died!")
		else: print(f"You won!")
	else:  print(f"You died!")
	print(f"Score: {score}")
	return

if __name__ == "__main__":
	maingame(score, counter, snakebump, turn_head, dead_border, maxscore)