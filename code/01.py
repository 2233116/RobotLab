from machine import Pin
from time import ticks_ms
class Button:
    def __init__(self,pin_num):
        self.pin = Pin(pin_num,Pin.IN,Pin.PULL_UP)
        self.old_state = 0
        self.last_pressed_time = 0
    def is_pressed(self):
        new = self.pin.value()
        now = ticks_ms()
        if new == 0 and self.old_state == 1 and now - self.last_pressed_time > 50: 
            self.last_pressed_time = now#"我怎么感觉现在这个防抖有点问题，他现在怎么感觉这次按完距离下次按的时间很长导致他不会触发"
            return True#"如果把return放进if的缩进会怎么样？又有点忘了"
        self.old_state = new
        return False
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
class Motor:
    def __init__(self,pin_num):
        self.in1.pin = Pin(pin_num,Pin.OUT)
        self.in2.pin = Pin(pin_num,Pin.OUT)
        self.pwm = 
        self.speed = 
    def stop(self):
        self.in1.pin.value(0)
        self.in2.pin.value(0)
    def forward(self):
        self.in1.pin.value(1)
        self.in2.pin.value(0)
    def backward(self):
        self.in1.pin.value(0)
        self.in2.pin.value(1)
        
class Robotcontroller:
    def __init__(self):
        self.button_a = Button(1)
        self.button_b = Button(2)
        self.button_c = Button(3)
        self.enable = False
        self.mode_a = 0
        self.mode_b = 0
        self.led = Led(4)
        self.motor = Motor(5)
    def updata(self):
        if self.button_a.is_pressed():
            self.enable = not self.enable
        if  not self.enable:
                self.led.off()
                self.motor.stop()
                return
        if self.button_b.is_pressed():
            self.mode_a += 1
            if self.mode_a > 3 :
                self.mode_a = 0
        if self.button_c.is_pressed():
            self.mode_b += 1
            if self.mode_b > 2 :
                self.mode_b = 0        
        if self.mode_a == 0 :
            self.led.off()
        if  self.mode_a == 1 :
            self.led.on()
        if  self.mode_a == 2 :
            self.led.stoggle()
        if  self.mode_a == 3 :
            self.led.blink()
        if self.mode_b == 0 :
            self.motor.stop()
        if self.mode_b == 1 :
            self.motor.forward()
        if self.mode_b == 2 :
            self.motor.backward()        


            



