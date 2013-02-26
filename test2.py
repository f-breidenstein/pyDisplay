#! /usr/bin/python2
import termios, sys, os
from displaylib import *
from actionlib import *
from time import sleep
from thread import start_new_thread, allocate_lock

# Initialize displaywires
disp = Display(25, 24, 23, 17, 21, 22, 20)

#longString = "This is a really long string to test the display"
longString = " A short one. "
longString2 = "This is another long string for testing purpose"
longString3 = "A big brown fox jumps over the fence in the garden"
longString4 = "BillX is the baddass operator from hell!! :D"

fb = []
fb=[""*20,""*20,""*20,""*20]

thread_started = False
lock = allocate_lock()

def updater():
    while True:
        disp.printStr(1,"c",fb[0])
        disp.printStr(2,"c",fb[1])
        disp.printStr(3,"c",fb[2])
        disp.printStr(4,"c",fb[3])
        time.sleep(0.5)

def lauftext(line,string):
    while True:
        longString = string*3
        for i in range(len(string)):
            lock.acquire()
            fb[line-1]=longString[i:i+20]
            lock.release()
            time.sleep(1)

start_new_thread(updater,())
start_new_thread(lauftext,(1,longString,))
#start_new_thread(lauftext,(2,longString2,))
#start_new_thread(lauftext,(3,longString3,))
#start_new_thread(lauftext,(4,longString4,))

while True:
    time.sleep(1)
