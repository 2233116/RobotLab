from machine import Pin
from machine import time_pulse_us
from time import ticks_ms
from time import sleep_us
from time import sleep_ms
class Button:
    def __init__(self,pin_num):
        self.pin = Pin(pin_num,Pin.IN,Pin.PULL_UP)
        self.last_state = self.pin.value()
        self.last_pressed_time = 0
    def is_pressed(self):
        new = self.pin.value()
        now = ticks_ms()
        pressed = False
        if new == 0 and self.last_state == 1 and now - self.last_pressed_time > 50:
            self.last_pressed_time = now
            return not pressed
        self.last_state = new
        return pressed
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
sonar = Sonar(4,5)
buzzer = Buzzer(21)
while True:
    distance = sonar.read()
    if distance is None:
        continue
    if distance > 20:
        buzzer.off()
    else:
        buzzer.on()
    
