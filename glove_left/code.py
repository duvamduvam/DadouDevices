from buildinLed import BuildinLed
import busio
import board
import time
from glove_keys import GloveKeys
from vibrator import Vibrator
import supervisor
supervisor.runtime.autoreload = False

keyboard = GloveKeys((("c", "b", "a"), ("f", "e", "d"), ("i", "h", "g"), ("l", "k", "j")),
                     (board.GP10, board.GP11, board.GP12),
                     (board.GP6, board.GP7, board.GP8, board.GP9))

buildinLed = BuildinLed(pin=board.LED)
vibrator = Vibrator(board.GP14)

print("start glove")

while True:
    print("start glove")
    try:
        keys = keyboard.check()
        if len(keys) > 0:
            #if keys[0] == "a":
            #   bno055.process()
            #else:
            msg = "<"+keys[0]+">"
            print(msg)
            buildinLed.flash()
            vibrator.click()
            time.sleep(0.05)
        buildinLed.process()
        vibrator.process()
        #bno055.process()
    except Exception as e:
        print("error : {}".format(e))
