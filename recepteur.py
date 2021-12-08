from microbit import *
import radio
uart.init(115200)
msg_bytes = uart.read()
baudrate = 115200
msg_str = str(msg_bytes)
microbit_uart_timeout_char = 13000 / baudrate + 1
radio.config(length=32, queue=3, channel=18, power=0, address=0x75626974, group=0, data_rate=radio.RATE_1MBIT)
radio.on()
test = 0

while True:
    msg_bytes = uart.read()
    msg_str = str(msg_bytes)
    incomming = radio.receive()
    if incomming == 'a':
        test+=1
        display.show(test)
        print(msg_str)
    if incomming == 'b':
        test-=1
        display.show(test)
        print(msg_str)




