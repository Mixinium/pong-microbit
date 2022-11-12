from microbit import *
import radio, time

uart.init(baudrate=115200)
msg_bytes = uart.read()
baudrate = 115200
msg_str = str(msg_bytes)
microbit_uart_timeout_char = 13000 / baudrate + 1
radio.config(
    length=32,
    queue=3,
    channel=18,
    power=0,
    address=0x75626974,
    group=0,
    data_rate=radio.RATE_1MBIT,
)
radio.on()
test = 0
mouv = 0
display.scroll("Pret")


while True:
    msg_str = str(msg_bytes)
    incomming = radio.receive()
    choix = 0

    if incomming == "1":
        print("1")
        display.show("1")
    if incomming == "2":
        print("2")
        display.show("2")
    if incomming == "3":
        print("3")
        display.show("3")
    if incomming == "4":
        print("4")
        display.show("4")
