import zmq
import socket
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
while True:
    message = socket.recv()
    
