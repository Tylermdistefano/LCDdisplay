from RPLCD import *
from time import sleep
from RPLCD.i2c import CharLCD

def readUsers(input): #function to read in user txt file and return dict with ids and users.
# Open the file in read mode
    with open('users.txt', 'r') as file:
    # Read the contents of the file
        text = file.read()
 
    users = {}
    lines = text.split('\n')
# Parses text in file and puts into dict
    for line in lines:
        parts = line.split(',')
        name = parts[0].strip()
        number = parts[1].strip()
        users[number] = name
    return users

lcd = CharLCD('PCF8574', 0x27)

def Print_usrClockOut(user):
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string(user)
    lcd.curcor_pos = (1, 0)
    lcd.write_string('Is now clocked out')

def Print_usrClockIn(user):
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string(user)
    lcd.curcor_pos = (1, 0)
    lcd.write_string('Is now clocked in')

def waitingForSwipe():
    lcd.clear()
    lcd.curcor_pos = (1, 0)
    lcd.write_string('Waiting for swipe......')    