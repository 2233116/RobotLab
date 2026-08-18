from time import ticks_ms
from machine import Pin
class Button:
    def __init__(self,pin_num):
        self.pin = Pin(pin_num,Pin.IN,Pin.PULL_UP)
        self.old_state = 0
        self.last_pressed_time = 0
    def is_pressed(self):
        new = self.pin.value()
        now = ticks_ms()
        if new == 0 and self.old_state == 1 and now - self.last_pressed_time > 50: 
            self.last_pressed_time = now
            return True
        self.old_state = new
        return False