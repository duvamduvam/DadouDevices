import board
import busio
import digitalio

import adafruit_rfm9x

class Lora:

    def __init__(self):
        RADIO_FREQ_MHZ = 510
        CS = digitalio.DigitalInOut(board.GP10)
        RESET = digitalio.DigitalInOut(board.GP9)
        spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
        self.rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

    def send_msg(self):
        self.rfm9x.send(bytes("Hello world!\r\n", "utf-8"))

    def get_msg(self):
        return self.rfm9x.receive()
        #return str(packet, "ascii")
