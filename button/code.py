import busio
import board
import time
from digitalio import DigitalInOut, Direction, Pull
from buildinLed import BuildinLed
#buildinLed = BuildinLed()
#print(dir(board))

btn = DigitalInOut(board.GP27)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

led = DigitalInOut(board.GP14)
led.direction = Direction.OUTPUT

buildinLed = BuildinLed(pin=board.GP16, rgb=True)

print("start button")

while True:

    if btn.value:
        led.value = False
    else:
        led.value = True
        print("<B>")
        buildinLed.flash()

    buildinLed.process()
    time.sleep(0.1)