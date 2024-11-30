from buildinLed import BuildinLed
import busio
import board
import time
from glove_keys import GloveKeys
from vibrator import Vibrator
import supervisor
supervisor.runtime.autoreload = False

keyboard = GloveKeys((board.GP10, board.GP11, board.GP12),
                     (board.GP6, board.GP7, board.GP8, board.GP9))

buildinLed = BuildinLed(pin=board.LED)
vibrator = Vibrator(board.GP14)

print("start glove")

while True:
    try:
        key = keyboard.check()
        if key:
            #if keys[0] == "a":
            #   bno055.process()
            #else:
            msg = "<{}>".format(key)
            print(msg)
            buildinLed.flash()
            vibrator.click()
            time.sleep(0.05)
        buildinLed.process()
        vibrator.process()

    except Exception as e:
        print("error : {}".format(e))

    time.sleep(0.01)