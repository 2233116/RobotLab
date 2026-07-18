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