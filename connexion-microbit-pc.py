import serial, time, zmq

import tkinter as tk
import keyboard



port = "COM7"
baud = 115200
s = serial.Serial(port)
s.baudrate = baud










while True:
    data = s.readline()  
    data = int(data[0:4])

    

    



