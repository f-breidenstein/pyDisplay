import RPi.GPIO as GPIO
import time
import socket
import os
from datetime import timedelta

class Display(object):

    def __init__(self,RS,E,D4,D5,D6,D7,WIDTH):
        self.RS = RS
        self.E = E
        self.D4 = D4
        self.D5 = D5
        self.D6 = D6
        self.D7 = D7
        self.WIDTH = WIDTH

        LINE = [0x80, 0xC0, 0x94, 0xD4]

        E_PULSE = 0.00005
        E_DELAY = 0.00005

        CHR = True
        CMD = False

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarningsF(False)
        GPIO.setup(E, GPIO.OUT)
        GPIO.setup(D4, GPIO.OUT)
        GPIO.setup(D5, GPIO.OUT)
        GPIO.setup(D6, GPIO.OUT)
        GPIO.setup(D7, GPIO.OUT)

    def printStr(self,line,string):
        lcd_byte(LINE[line+1],CMD)
        lcd_string(string)
