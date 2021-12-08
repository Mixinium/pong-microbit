import serial, time

import tkinter as tk
import keyboard

from SI.pong.pong import haut1
port = "COM6"
baud = 115200
s = serial.Serial(port)
s.baudrate = baud

def demande_mouvement():
    s.write(b'mouvement')
    data = s.readline()  
    print(data)












port = "COM6"
baud = 115200
s = serial.Serial(port)
s.baudrate = baud


def demande_mouvement():
    s.write(b'mouvement')
    data = s.readline()  
    data = int(data[0:4])
    print(data)
    s.write(b'o')
    if data==1:
        print("haut")


while True:
    if keyboard.is_pressed("z") == True :
        demande_mouvement()
    



