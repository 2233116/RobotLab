from machine import Pin
from time import ticks_ms
class Button:
    def __init__(self,pin_um):
        self.pin = Pin(pin_um,Pin.IN,Pin.PULL_UP)
        self.old_state = 1
    def is_pressed(self):
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
button = Button(4)
led = Led(2)
mode = 0
while True:
     if button.is_pressed():
         mode += 1
         if  mode > 2:
             mode = 0
     if  mode == 0:
         led.off()
     elif  mode == 1:
         led.on()
     elif  mode == 2:
         led.blink()
             
        
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