import time
import neopixel
from rainbowio import colorwheel
import board
import digitalio

FLASH = "flash"
BLINK = "blink"

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

class BuildinLed:

    flashNb = 6
    flashCount = 0
    mode = BLINK

    def __init__(self, pin=board.LED, rgb=False):
        if not rgb:
            self.led = digitalio.DigitalInOut(pin)
            self.led.direction = digitalio.Direction.OUTPUT
        else:
            self.led = neopixel.NeoPixel(pin, 1)
        self.rgb = rgb
        self.lastBlink = float(0)
        self.blinkRate = float(0.5)
        self.flashRate = float(0.05)
        self.currentRate = self.blinkRate

        self.rgb_count = 0

    # print("Start Blink!")

    def blink(self):
        self.mode = BLINK
        self.currentRate = self.blinkRate

    def flash(self):
        self.mode = FLASH
        self.flashCount = 0
        self.currentRate = self.flashRate

    def process(self):
        if time.monotonic() > (self.lastBlink + self.currentRate):
            if self.rgb:
                self.rgb_count = (self.rgb_count + 1) % 256  # run from 0 to 255
                if self.rgb_count == 0:
                    self.led.fill(YELLOW)
                elif self.rgb_count == 1:
                    self.led.fill(PURPLE)
                elif self.rgb_count == 2:
                    self.led.fill(BLUE)
                elif self.rgb_count == 3:
                    self.led.fill(CYAN)

                self.rgb_count = (self.rgb_count +1)%4

            else:
                self.led.value = not self.led.value
            self.lastBlink = time.monotonic()
            if self.mode == FLASH:
                if self.flashCount >= self.flashNb:
                    self.blink()
                else:
                    self.flashCount += 1
