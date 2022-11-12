from microbit import *
import radio

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

while True:
    if button_a.was_pressed():
        radio.send("a")
    if button_b.was_pressed():
        radio.send("b")
