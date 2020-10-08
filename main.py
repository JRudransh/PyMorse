#!/usr/bin/python3

import numpy as np
import simpleaudio as sa # pip3 install simpleaudio
from time import sleep

spd = input('Set speed [1-20]: ')

if spd != '':
    try:
        spd = int(spd)
    except:
        spd = 6
else:
    spd = 6

unit = 1/6
A_freq = 230
sample_rate = 44100

def sound(T):
    n = int(sample_rate * T)
    t = np.linspace(0, T, n, endpoint=True)
    A_note = np.sin(A_freq * t * 2 * np.pi)
    audio = np.hstack(A_note)
    audio *= 32767 / np.max(np.abs(audio))
    audio = audio.astype(np.int16)
    play_obj = sa.play_buffer(audio, 2, 2, sample_rate)
    play_obj.wait_done()


def dot(unit):
    T = unit
    sound(T)
    

def dash(unit):
    T = unit * 3
    sound(T)
    

def gap(unit):
    T = unit * 3
    sleep(T)

def space(unit):
    T = unit * 7
    sleep(T)

code = {'A': [0, 1], 'B': [1, 0, 0, 0], 'C': [1, 0, 1, 0], 'D': [1, 0, 0], 'E': [0], 'F': [0, 0, 1, 0], 'G': [1, 1, 0], 'H': [0, 0, 0, 0], 'I': [0, 0], 'J': [0, 1, 1, 1], 'K': [1, 0, 1], 'L': [0, 1, 0, 0], 'M': [1, 1], 'N': [1, 0], 'O': [1, 1, 1], 'P': [0, 1, 1, 0], 'Q': [1, 1, 0, 1], 'R': [0, 1, 0], 'S': [0, 0, 0], 'T': [1], 'U': [0, 0, 1], 'V': [0, 0, 0, 1], 'W': [0, 1, 1], 'X': [1, 0, 0, 1], 'Y': [1, 0, 1, 1], 'Z': [1, 1, 0, 0]}


def play_char(data):
    cod = code[data]
    for i in cod:
        if i == 0:
            dot(unit)
        else:
            dash(unit)

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
            space(unit)
        else:
            gap(unit)
            print_char(i)
            play_char(i)
    print('\n\n')


try:
    start('abcdefghijklmnopqrstuvwxyz')
except KeyboardInterrupt:
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
