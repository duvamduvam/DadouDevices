import time
import board
import digitalio
from analogio import AnalogIn

# Update this to match the number of NeoPixel LEDs connected to your board.
from buildinLed import BuildinLed
#import busio

#print(dir(board))

buildinLed = BuildinLed(pin=board.GP16, rgb=True)
#uart = busio.UART(board.GP0, board.GP1, baudrate=115200, timeout=10)

right = AnalogIn(board.A1)
left = AnalogIn(board.A0)

two_slide = digitalio.DigitalInOut(board.GP3)
two_slide.direction = digitalio.Direction.INPUT
two_slide.pull = digitalio.Pull.UP

one_slide = digitalio.DigitalInOut(board.GP5)
one_slide.direction = digitalio.Direction.INPUT
one_slide.pull = digitalio.Pull.UP



print("start slider")

def mapping(v, in_min, in_max, out_min, out_max):
    # Check that the value is at least in_min
    if v < in_min:
        v = in_min
    # Check that the value is at most in_max
    if v > in_max:
        v = in_max
    return (v - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


while True:
    right_value = mapping(65535 - right.value, 0, 65535,10, 99)
    left_value = mapping(left.value, 0, 65535, 10, 99)
    if not two_slide.value:
        print("<{}{}>".format(str(left_value), str(right_value)))
        buildinLed.flash()
    else:
        buildinLed.blink()


    if not one_slide.value:
        print("<{}>".format(str(left_value)))

    time.sleep(0.05)
    buildinLed.process()
