import analogio
import board
from buildinLed import BuildinLed
from digitalio import DigitalInOut, Direction, Pull
import time

#print(dir(board))
print("start josystick")

buildinLed = BuildinLed(pin=board.GP16, rgb=True)

x_axis_pin = analogio.AnalogIn(board.A0)
y_axis_pin = analogio.AnalogIn(board.A2)

btn = DigitalInOut(board.GP9)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

enabled = False
lastBtnTime = float(0)
btnTimeout = float(0.5)

def mapping(v, in_min: int, in_max: int, out_min: int, out_max: int):
    # Check that the value is at least in_min
    if v < in_min:
       v = in_min
    # Check that the value is at most in_max
    if v > in_max:
       v = in_max
    return (v - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:

    if not btn.value and time.monotonic() > (lastBtnTime + btnTimeout):
        enabled = not enabled
        print("button pressed joystick enabled {}".format(enabled))
        lastBtnTime = time.monotonic()

    if enabled:
        x_axis = x_axis_pin.value
        y_axis = y_axis_pin.value
        # print((x_axis,y_axis))
        x_value = mapping(x_axis, 0, 65535, -100, 100)
        y_value = mapping(y_axis, 0, 65535, -100, 100)
        print("{},{}".format(x_axis, y_axis))
        print("{},{}".format(x_value, y_value))
        buildinLed.flash()

    else:
        buildinLed.process()

    time.sleep(0.1)