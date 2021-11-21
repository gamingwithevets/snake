# Basic info
Snake, made in 100% Python.<br>
It's a very simple script. ~~In fact, everyone can make one of these by themselves using tutorials and some Python knowledge.~~<br>
It uses the Curses library to display color.

# menu.py
*menu.py* is a launcher that lets you set flags/variables in the main game.<br>
It gives you every flag the game has to offer, and it doesn't lie.<br>
I can't spoil all the flags, so go check it out!

# snake.py
*snake.py* is the game itself. If you don't run it through the launcher, it'll start with the default settings, which the launcher also loads on startup.<br>
You can modify the startup variables manually in the code. But remember: this will ***permanently*** change settings in the game, so do it at your own risk!

# System requirements
For Windows:<br>
You need Python 3.6 - *3.9.9* and Windows 7+ (Windows 8+ for Python 3.9) with the *windows-curses* package installed.<br>
Now, you may be wondering, "Why not Python 3.10 instead? That's the newest version!"<br>
And you're right. But, as of 2021, __no Curses library has been made for 3.10__, and so, using pip to install *windows-curses*... is pretty much impossible. You can read more [here](https://stackoverflow.com/questions/69927587/python-curses-module-for-windows-cant-install).


For Mac:<br>
*Please note, I have never installed Python on a Mac before, so please correct anything wrong!*<br>
You need Mac OS X 10.6 Snow Leopard to 10.9 Mavericks and above, depending on what the description says, to install Python.<br>
Again, you need Python 3.6 - *3.9.9* as well.


For Linux:<br>
Ubuntu 20.04 happens to have Python 3.8 installed along with the Curses library.<br>
If you didn't uninstall the Curses library or Python, you're all good to go!

# Python requirements
- Python 3.6 - *3.9.9* (DO NOT USE 3.10)<br>
- The Curses library (either use *windows-curses* or some other Curses package)
