from buildinLed import BuildinLed
import busio
import board
#from anglometer import Anglometer
from glove_keys import GloveKeys
from vibrator import Vibrator
from bno055 import BNO055

#keyboard = GloveKeys((("l", "k", "j"), ("f", "e", "d"), ("c", "b", "a"), ("i", "h", "g")),
#                     (board.GP10, board.GP11, board.GP12),
#                     (board.GP6, board.GP7, board.GP8, board.GP9))

keyboard = GloveKeys((("c", "b", "a"), ("f", "e", "d"), ("i", "h", "g"), ("l", "k", "j")),
                     (board.GP10, board.GP11, board.GP12),
                     (board.GP6, board.GP7, board.GP8, board.GP9))

#keyboard = GloveKeys((("c", "b", "a"), ("f", "e", "d"), ("i", "h", "g"), ("l", "k", "j")),
#                     (board.GP7, board.GP8, board.GP9),
#                     (board.GP10, board.GP11, board.GP12, board.GP13))

#keyboard = GloveKeys((("y ", "w", "v"), ("r", "q", "p"), ("o", "n", "m"), ("u", "t", "s")),
#                     (board.GP17, board.GP10, board.GP11),
#                     (board.GP13, board.GP16, board.GP14, board.GP15))

buildinLed = BuildinLed()
#uart = busio.UART(board.GP0, board.GP1, baudrate=115200, timeout=10)
#anglometer = Anglometer()
vibrator = Vibrator(board.GP14)
bno055 = BNO055(board.GP2, board.GP3)

print("start glove")

while True:
    try:
        keys = keyboard.check()
        if len(keys) > 0:
            if keys[0] == "a":
               bno055.process()
            else:
                msg = "<"+keys[0]+">"
                print(msg)
            buildinLed.flash()
            vibrator.click()
        buildinLed.process()
        vibrator.process()
        #bno055.process()
    except Exception as e:
        print("error : {}".format(e))
