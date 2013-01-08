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

        self.LINE = [0x80, 0xC0, 0x94, 0xD4]

        self.E_PULSE = 0.00005
        self.E_DELAY = 0.00005

        self.CHR = True

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.E, GPIO.OUT)
        GPIO.setup(self.RS, GPIO.OUT)
        GPIO.setup(self.D4, GPIO.OUT)
        GPIO.setup(self.D5, GPIO.OUT)
        GPIO.setup(self.D6, GPIO.OUT)
        GPIO.setup(self.D7, GPIO.OUT)

        self.lcd_byte(0x33,False)
        self.lcd_byte(0x32,False)
        self.lcd_byte(0x28,False)
        self.lcd_byte(0x0C,False)  
        self.lcd_byte(0x06,False)
        self.lcd_byte(0x01,False)  

    def printStr(self,line,string):
        self.lcd_byte(self.LINE[line-1],False)
        self.lcd_string(string)

    def lcd_string(self, message):
        message = message.ljust(self.WIDTH," ")  

        for i in range(self.WIDTH):
            self.lcd_byte(ord(message[i]),self.CHR)

    def lcd_byte(self, bits, mode):

        GPIO.output(self.RS, mode) # RS

        # High bits
        GPIO.output(self.D4, False)
        GPIO.output(self.D5, False)
        GPIO.output(self.D6, False)
        GPIO.output(self.D7, False)
        if bits&0x10==0x10:
            GPIO.output(self.D4, True)
        if bits&0x20==0x20:
            GPIO.output(self.D5, True)
        if bits&0x40==0x40:
            GPIO.output(self.D6, True)
        if bits&0x80==0x80:
            GPIO.output(self.D7, True)

        # Toggle 'Enable' pin
        time.sleep(self.E_DELAY)    
        GPIO.output(self.E, True)  
        time.sleep(self.E_PULSE)
        GPIO.output(self.E, False)  
        time.sleep(self.E_DELAY)      

        # Low bits
        GPIO.output(self.D4, False)
        GPIO.output(self.D5, False)
        GPIO.output(self.D6, False)
        GPIO.output(self.D7, False)
        if bits&0x01==0x01:
            GPIO.output(self.D4, True)
        if bits&0x02==0x02:
            GPIO.output(self.D5, True)
        if bits&0x04==0x04:
            GPIO.output(self.D6, True)
        if bits&0x08==0x08:
            GPIO.output(self.D7, True)

        # Toggle 'Enable' pin
        time.sleep(self.E_DELAY)    
        GPIO.output(self.E, True)  
        time.sleep(self.E_PULSE)
        GPIO.output(self.E, False)  
        time.sleep(self.E_DELAY)   
