from time import sleep_ms
from machine import Pin
class Buzzer:
    def __init__(self,pin_num):
        self.buzzer = Pin(pin_num,Pin.OUT)
    def on(self):
        self.buzzer.value(1)
    def off(self):
        self.buzzer.value(0)   
    def beep(self):
        self.off()
        sleep_ms(1000)
        self.on()
        sleep_ms(1000)
        self.off()