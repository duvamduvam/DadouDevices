import keypad
import board
import digitalio
import time


class GloveKeys:
    lastKeyTime = 0
    timeout = 0.25

    def __init__(self, cols, rows):

        #self.keys = (("c", "b", "a"), ("f", "e", "d"), ("i", "h", "g"), ("l ", "k", "j"))
        #cols = [digitalio.DigitalInOut(x) for x in (board.GP7, board.GP8, board.GP9)]
        #rows = [digitalio.DigitalInOut(x) for x in (board.GP10, board.GP11, board.GP12, board.GP13)]

        #self.keypad = adafruit_matrixkeypad.Matrix_Keypad(
        #    [digitalio.DigitalInOut(x) for x in rows],
        #    [digitalio.DigitalInOut(x) for x in cols], keys)

        self.keypad = keypad.KeyMatrix(
            row_pins=rows,
            column_pins=cols,
        )


    def check(self):
        event = self.keypad.events.get()

        if event and (time.monotonic() > (self.lastKeyTime + self.timeout)):
            self.lastKeyTime = time.monotonic()
            #print("Pressed: ", keys[0], "time ", time.monotonic(), "lastKeyTime ", self.lastKeyTime)
            #print("Pressed: ", keys[0])
            return event.key_number
        return None