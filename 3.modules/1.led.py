from machine import Pin
from time import ticks_ms
class Led:
    def __init__(self,pin_num):
        self.pin = Pin(pin_num,Pin.OUT)
        self.last_time = 0
    def on(self):
        self.pin.value(1)
    def off(self):
        self.pin.value(0)
    def stoggle(self):
        self.pin.value(not self.pin.value)
    def blink(self):
        now = ticks_ms()
        if now - self.last_time > 500:
            self.pin.value(not self.pin.value)
            self.last_time = now