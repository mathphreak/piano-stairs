import pygame

import serial
import time

#onpi = True
onpi = False

numpins = 8

# switch between piano and guitar every 3 minutes
seconds = 3 * 60

previnputs = [False for a in range(0, numpins)]

if onpi:
    ser = serial.Serial('/dev/ttyACM0', 9600)

pygame.mixer.pre_init(channels=6, buffer=1024)
pygame.mixer.init()

letters = ["c1", "d", "e", "f", "g", "a", "b", "c"]
piano_notes = [pygame.mixer.Sound("piano-notes/"+letter+".wav") for letter in letters]

def piano(i):
    piano_notes[i].play()

count = 0

time.sleep(3)

while True:
    count += 1
    line = ""
    if onpi:
        line = ser.readline()
    else:
        line = raw_input()
    if len(line) < numpins:
        continue
    for i in range(0, numpins):
        curr = line[i] != '0'
        prev = previnputs[i]
        if curr and not prev:
            piano(i)
        previnputs[i] = curr

