from machine import Pin
from time import ticks_ms
class Button:
    def __init__(self,pin_um):
        self.pin = Pin(pin_um,Pin.IN,Pin.PULL_UP)
        self.old_state = 1
    def is_pressed(self):
        if current_time - last_state_time > 50:
            
        new_state = self.pin.value()
        pressed = (new_state == 0 and self.old_state == 1)
        self.old_state = new_state

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
    def __init__(self):
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
class RobotController:#"说实话我不知道这个类里放什么东西，就比如led里放了关于他的定义函数，但是我感觉robobcontroller里没有函数可以用，而且感觉就一个robotcontroller不像led一样有blue.led或者black.led之类的，感觉它调用一下led和button的类一样"
     def __init__(self):
         self.button = Button
         self.led = Led
         self.motor = Motor
button_a = Button(4)
button_b = Button(3)
button_c = Button(5)
led = Led(2)
motor = Motor(1)#"也像button那样给一个引脚触发之类的"
mode_a = 0
mode_b = 0
mode_c = 0
robotcontroller = RobotController()
while True:
    if robotcontroller.button_a.is_pressed():
        mode_a += 1
        if  mode_a > 1:
             mode_a = 0
    if  mode_a == 0:
         if  robotcontroller.button_b.is_pressed():
            mode_b += 1
            if  mode_b > 2:
                mode_b = 0
            if mode_b == 0:    
                robotcontroller.led.off()
            elif  mode_b == 1:
                robotcontroller.led.on()
            elif  mode_b == 2:
                robotcontroller.led.blink()  
    elif  mode_a == 1:
            if  robotcontroller.button_c.is_pressed():
                mode_c += 1
                if  mode_c > 2:
                    mode_c = 0
            if mode_c == 0:    
                robotcontroller.motor.forward()
            elif  mode_c == 1:
                robotcontroller.motor.backward()
            elif  mode_c == 2:
                robotcontroller.motor.stop()
             
        
def state_0():
    led.value(0)
def state_1():
    led.value(1)
def state_2(now,last_time,led):
    if now - last_time >= 800:
            led.value(not led.value())
            last_time = now
    return  last_time
def state_3(now,last_time,led):
     if now - last_time >= 200:
            led.value(not led.value())
            last_time = now
     return  last_time      
# ===== 初始化 =====
led = Pin(2, Pin.OUT)
button_a = Button(4)
button_b = Pin(5, Pin.IN, Pin.PULL_UP)
# ===== 状态变量 =====
led_state = 0
old_a = 1
old_b = 1
last_time = 0
# ===== 主循环 =====
while True:
    now = ticks_ms()
    new_a = button_a.value()
    new_b = button_b.value()
    # 输入处理
    if new_b == 0 and old_b == 1:
        led_state = 0

    if button_a.is_pressed():
        led_state += 1
        if led_state > 3:
            led_state = 0
    # 状态执行
    if led_state == 0:
        state_0()
    elif led_state == 1:
        state_1()
    elif led_state == 2:
        last_time = state_2(now,last_time,led)
    elif led_state == 3:
        last_time = state_3(now,last_time,led)
    old_a = new_a
    old_b = new_b