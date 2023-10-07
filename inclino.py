# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import busio
import adafruit_lis3dh


class Inclino:

    def __init__(self, i2c):
        self.lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x18)
        self.lis3dh.range = adafruit_lis3dh.RANGE_2_G

        self.last_value = 0
        self.time_step = 0.2

    def process(self):
        # Read accelerometer values (in m / s ^ 2).  Returns a 3-tuple of x, y,
        # z axis values.  Divide them by 9.806 to convert to Gs.
        if time.monotonic() > (self.last_value + self.time_step):
            x, y, z = [
                value / adafruit_lis3dh.STANDARD_GRAVITY for value in self.lis3dh.acceleration
            ]
            turn = self.translate(x, 1, -1, 100, -100)
            forward = self.translate(y, 1, -1, 100, -100)
            self.last_value = time.monotonic()
            print("x = {}, y = {}".format(turn, forward))

    def translate(value, leftMin, leftMax, rightMin, rightMax):
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return rightMin + (valueScaled * rightSpan)