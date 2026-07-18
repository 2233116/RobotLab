from time import sleep_us
from machine import Pin
from machine import time_pulse_us
class Sonar:
    def __init__(self,trig_pin,echo_pin):
        self.trig = Pin(trig_pin,Pin.OUT)
        self.echo = Pin(echo_pin,Pin.IN) 
    def read(self):
        self.trig.value(0)
        sleep_us(2)
        self.trig.value(1)
        sleep_us(20)
        self.trig.value(0)
        duration = time_pulse_us(self.echo,1)
        if duration < 0:
            return None
        distance = duration / 58
        return distance