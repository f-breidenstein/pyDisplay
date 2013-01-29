#! /usr/bin/python2
import termios, sys, os
from displaylib import *

# Initialize displaywires
disp = Display(25, 24, 23, 17, 21, 22, 20)

string = "Baum"
TERMIOS = termios

cat = 0
subcat = 0

names = ["System",
         "Audio",
         "Info"]

menu_system = ["RAM",
               "CPU"]
menu_audio = ["Track 1",
              "Track 2",
              "Track 3"]
menu_info = ["Date",
             "Time"]

subnames = [menu_system,
            menu_audio,
            menu_info]

def getKey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c

def drawrMenu():
    printMenu(names[cat],subnames[cat][subcat])

#disp.printStr(1, "l", string) 
#disp.printStr(2, "r", string)

while True:
    key = getKey()
    if (key = "a"):
        subcat -= 1;
    elif (key = "d"):
        subcat += 1;
    elif (key = "w"):
        cat -= 1;
    elif [key = "s"):
        cat += 1:
    else
        echo key;
    drawMenu;

