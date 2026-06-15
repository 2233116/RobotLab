from machine import Pin
from time import ticks_ms
class Button:
    def __init__(self,pin_um):
        self.pin = Pin(pin_um,Pin.IN,Pin.PULL_UP)
        self.old_state = 1
        self.last_pressed_time = 0
    def is_pressed(self):
        current_time = ticks_ms()
        new_state = self.pin.value()
        pressed = (new_state == 0 and self.old_state == 1 and current_time - self.last_pressed_time > 50)
        self.old_state = new_state
        if pressed :
           self.last_pressed_time = current_time
        return pressed
class Led:
    def __init__(self,pin_num):
        self.pin = Pin(pin_num,Pin.OUT)
        self.last_toggle_time = 0
    def  on(self):
        self.pin.value(1)
    def  off(self):
        self.pin.value(0)
    def  blink(self):
        now = ticks_ms()
        if now - self.last_toggle_time >= 500:
           self.pin.value(not self.pin.value())
           self.last_toggle_time = now
    def toggle(self):
         self.pin.value(not self.pin.value())
class Motor:
    def __init__(self,pin_num):
        self.state = 0
        self.speed = 0
    def forward(self):
        self.state = "forward"
        self.speed = 50
    def backward(self):
        self.state = "backward"
        self.speed = 0
    def stop(self):
        self.state = "stop"
        self.speed = 0
class RobotController:
     def __init__(self):
        self.self.button_a  = Button(1)     
        self.self.button_b = Button(2)
        self.self.button_c = Button(3)
        self.enable = 0
        self.self.led_mode = 0
        self.self.motor_mode = 0
        self.self.led = Led(4)
        self.self.motor = Motor(5)
     def updata(self):
        if self.button_a.is_pressed():
            self.enable += 1
            if  self.enable > 1:
             self.enable = 0
        if  self.enable == 0:
             if  self.button_b.is_pressed():
                self.led_mode += 1
                if  self.led_mode > 2:
                    self.led_mode = 0
             if self.led_mode == 0:    
                self.led.off()
             elif  self.led_mode == 1:
                self.led.on()
             elif  self.led_mode == 2:
                self.led.blink()  
        elif  self.enable == 1:
            if  self.button_c.is_pressed():
                self.motor_mode += 1
                if  self.motor_mode > 2:
                    self.motor_mode = 0
            if self.motor_mode == 0:    
                self.motor.forward()
            elif  self.motor_mode == 1:
                self.motor.backward()
            elif  self.motor_mode == 2:
                self.motor.stop()
contorll = RobotController()                
while True:
    contorll.updata()
    
             
        
def state_0():
    self.led.value(0)
def state_1():
    self.led.value(1)
def state_2(now,last_time,self.led):
    if now - last_time >= 800:
            self.led.value(not self.led.value())
            last_time = now
    return  last_time
def state_3(now,last_time,self.led):
     if now - last_time >= 200:
            self.led.value(not self.led.value())
            last_time = now
     return  last_time      
# ===== 初始化 =====
self.led = Pin(2, Pin.OUT)
self.button_a = Button(4)
self.button_b = Pin(5, Pin.IN, Pin.PULL_UP)
# ===== 状态变量 =====
self.led_state = 0
old_a = 1
old_b = 1
last_time = 0
# ===== 主循环 =====
while True:
    now = ticks_ms()
    new_a = self.button_a.value()
    new_b = self.button_b.value()
    # 输入处理
    if new_b == 0 and old_b == 1:
        self.led_state = 0

    if self.button_a.is_pressed():
        self.led_state += 1
        if self.led_state > 3:
            self.led_state = 0
    # 状态执行
    if self.led_state == 0:
        state_0()
    elif self.led_state == 1:
        state_1()
    elif self.led_state == 2:
        last_time = state_2(now,last_time,self.led)
    elif self.led_state == 3:
        last_time = state_3(now,last_time,self.led)
    old_a = new_a
    old_b = new_b