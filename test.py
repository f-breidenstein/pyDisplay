#! /usr/bin/python2
import termios, sys, os
from displaylib import *
from actionlib import *

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
menu_audio = ["Play / Pause",
              "Next Track",
              "Current Track"]
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

def drawMenu():
  disp.printMenu(names[cat],subnames[cat][subcat])

#########################
# START MAIN PROGRAMM   #
#########################
# Welcome Screen
disp.printStr(1, "c", "*** Welcome ***")
disp.printStr(2, "c", "Use w,a,s,d")
disp.clear(3)
disp.printStr(4, "c", "(c) by POETTERING") 

# loop to 
while True:
    key = getKey()
    if (key == "a"):
        subcat -= 1
        if (subcat < 0):
            subcat = len(subnames[cat])-1

    elif (key == "d"):
        subcat += 1
        if (subcat == len(subnames[cat])):
            subcat = 0

    elif (key == "w"):
        cat -= 1
        subcat = 0
        if (cat < 0):
            cat = len(subnames)-1

    elif (key == "s"):
        cat += 1
        subcat = 0
        if (cat == len(subnames)):
            cat = 0
    elif (key == "f"):
        disp.clear(2)
        disp.clear(3)
        disp.clear(4)
        disp.action(cat,subcat) 
        time.sleep(2)
    else:
        print (key) 
    
    # Update Screen with new Menupoint
    drawMenu()
