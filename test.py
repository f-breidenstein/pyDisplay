#! /usr/bin/python2
from displaylib import *

disp = Display(25, 24, 23, 17, 21, 22, 20)

string = "Baum"

disp.printStr(1, "l", string) 
disp.printStr(2, "r", string)
#disp.printScrolling(3, "Das ist ein ziemlich langer Text!")
disp.printScrolling(4, "OMG, das ist auch ein langer Text!")
