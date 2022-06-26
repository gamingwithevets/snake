# Basic info
Snake, made in 100% Python.<br>
These are very simple scripts. ~~In fact, everyone can make one of these by themselves using tutorials and some Python knowledge.~~<br>
It uses the Curses library to display color.<br><br>
Main game code from [this tutorial](https://youtu.be/M_npdRYD4K0) by [Python Engineer](https://www.youtube.com/channel/UCbXgNpp0jedKWcQiULLbDTA).<br>
Other code written by SJ Studio in cooperation with GamingWithEvets Inc.<br>
© 2021 GamingWithEvets Inc. & SJ Studio. All rights go to their respective owners.

# menu.py
*menu.py* is a launcher that lets you set flags/variables in the main game.<br>
It gives you every flag the game has to offer, and it doesn't lie.<br>
I can't spoil all the flags, so go check it out!

# snake.py
*snake.py* is the game itself. If you don't run it through the launcher, it'll start with the default settings, which the launcher also loads on startup.<br>
You can modify the startup variables manually in the code. But remember: this will ***permanently*** change settings in the game, so do it at your own risk!

# System requirements
For Windows:<br>
You need Python 3.6+ and Windows 7+ (Windows 8+ for Python 3.9+) with the Curses library installed.

For Mac:<br>
*Please note, I have never installed Python on a Mac before, so please correct anything wrong!*<br>
You need Mac OS X 10.6 Snow Leopard to 10.9 Mavericks and above, depending on what the description says, to install Python.<br>
Again, you need Python 3.6+ as well.


For WSL/Linux:<br>
Ubuntu 20.04 happens to have Python 3.8 installed along with the Curses library.<br>
If you didn't uninstall the Curses library or Python, you're all good to go!<br>
Also, you should definitely install *pip*.<br>
First, you should type `sudo apt-get update` to update *apt*. This is optional.<br>
Then, you type `apt install python3-pip`. And that's it!

# Python requirements
- Python 3.6+
- The Curses library (either use *windows-curses* for Windows or some other Curses package)
