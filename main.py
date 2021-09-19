#!/usr/bin/python3

import numpy as np
from time import sleep
import time
from pysinewave import SineWave

# level = input('Set Level [1-7]: ')
level = '1'

if level == '1':
    spd = 10
    g_u = 3
elif level == '2':
    spd = 20
    g_u = 3
elif level == '3':
    spd = 25
    g_u = 2
elif level == '4':
    spd = 40
    g_u = 2
elif level == '5':
    spd = 80
    g_u = 2
elif level == '6':
    spd = 80
    g_u = 1
elif level == '7':
    spd = 130
    g_u = 1







if spd != '':
    try:
        spd = int(spd)
    except:
        spd = 6
else:
    spd = 6

unit = 1/spd

def sound(T):
    sinewave = SineWave(pitch = 7, pitch_per_second = 200)
    # Turn the sine wave on.
    sinewave.play()

    # Sleep for 2 seconds, as the sinewave keeps playing.
    time.sleep(T)
    sinewave.stop()



def gap():
    T = unit
    sleep(T)


def dot():
    T = unit
    sound(T)
    gap()
    

def dash():
    T = unit * 3
    sound(T)
    gap()


def point():
    T = unit * 2 * g_u
    sleep(T)


def space():
    T = unit * 4 * g_u
    sleep(T)


code = {
    'A': [0, 1], 'B': [1, 0, 0, 0], 'C': [1, 0, 1, 0], 'D': [1, 0, 0], 
    'E': [0], 'F': [0, 0, 1, 0], 'G': [1, 1, 0], 'H': [0, 0, 0, 0], 
    'I': [0, 0], 'J': [0, 1, 1, 1], 'K': [1, 0, 1], 'L': [0, 1, 0, 0], 
    'M': [1, 1], 'N': [1, 0], 'O': [1, 1, 1], 'P': [0, 1, 1, 0], 
    'Q': [1, 1, 0, 1], 'R': [0, 1, 0], 'S': [0, 0, 0], 'T': [1], 
    'U': [0, 0, 1], 'V': [0, 0, 0, 1], 'W': [0, 1, 1], 'X': [1, 0, 0, 1], 
    'Y': [1, 0, 1, 1], 'Z': [1, 1, 0, 0], '.' : [0,1,0,1,0,1], 
    ',': [1, 1, 0, 0, 1, 1], '1': [0, 1, 1, 1, 1], '2': [0, 0, 1, 1, 1],
    '3': [0, 0, 0, 1, 1], '4': [0, 0, 0, 0, 1], '5': [0, 0, 0, 0, 0],
    '6': [1, 0, 0, 0, 0], '7': [1, 1, 0, 0, 0], '8': [1, 1, 1, 0, 0],
    '9': [1, 1, 1, 1, 0]
    }


def play_char(data):
    cod = code[data]
    for i in cod:
        if i == 0:
            dot()
        else:
            dash()

def print_char(data):
    print(data, end='  ')
    cod = code[data]
    for i in cod:
        if i == 0:
            print('.', end='')
        else:
            print('_', end='')
    print()

def start(string):
    print('\n\n')
    for i in string.upper():
        if i == ' ':
            print()
            space()
        else:
            print_char(i)
            play_char(i)
            point()
    print('\n\n')


def start2(string):
    print('\n\n')
    for word in string.split():
        print(word)
        for i in word.upper():
            play_char(i)
            point()
        space()
        
    print('\n\n')



try:
    start2('Hello Morse')
except:
    pass

while True:
    try:
        i = input('# ')
        if i.lower() == ':q':
            print('\n\n')
            break
        start(i)
    except KeyboardInterrupt:
        print('\n\nEnter :q to quit..\n\n')
