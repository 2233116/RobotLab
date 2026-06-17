from machine import Pin
from time import ticks_ms
from time import sleep_ms     
class Button:
    def __init__(self,pin_num):
        self.pin = Pin(pin_num,Pin.IN,Pin.PULL_UP)
        self.old_state = self.pin.value()
        self.last_pressed_time = 0 
    def is_pressed(self):
        new = self.pin.value()
        now = ticks_ms()
        pressed = False
        if new == 0 and self.old_state == 1 and now - self.last_pressed_time > 50:
            self.last_pressed_time = now
            pressed = True
        self.old_state = new
        return pressed
    def __init__(self,pin_num):
        self.buzzer = Pin(pin_num,Pin.OUT)
    def on(self):
        self.buzzer.value(1)
    def off(self):
        self.buzzer.value(0)   
    def beep(self,duration=200): 
        self.on()
        sleep_ms(duration)
        self.off()   
    
class Controller:
    def __init__(self):
        self.button_a = Button(1)
        self.mode_a = 0
        self.buzzer = Buzzer(2)
    def update(self):
        if self.button_a.is_pressed():
            self.mode_a += 1
            if self.mode_a == 2:
                self.buzzer.beep()
        if self.mode_a > 2 :
            self.mode_a = 0
        if self.mode_a == 0:
            self.buzzer.off()
        if self.mode_a == 1:
            self.buzzer.on()

controll = Controller()                
while True:
    controll.update()
