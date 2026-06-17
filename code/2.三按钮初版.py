from machine import Pin
from time import ticks_ms


class Button:
    def __init__(self, pin_num):
        self.pin = Pin(pin_num, Pin.IN, Pin.PULL_UP)
        self.old_state = 1
        self.last_pressed_time = 0

    def is_pressed(self):
        current_time = ticks_ms()
        new_state = self.pin.value()

        pressed = (
            new_state == 0
            and self.old_state == 1
            and current_time - self.last_pressed_time > 50
        )

        self.old_state = new_state

        if pressed:
            self.last_pressed_time = current_time

        return pressed


class Led:
    def __init__(self, pin_num):
        self.pin = Pin(pin_num, Pin.OUT)
        self.last_toggle_time = 0

    def on(self):
        self.pin.value(1)

    def off(self):
        self.pin.value(0)

    def blink(self):
        now = ticks_ms()

        if now - self.last_toggle_time >= 500:
            self.pin.value(not self.pin.value())
            self.last_toggle_time = now


class Motor:
    def __init__(self):
        self.state = "stop"
        self.speed = 0

    def forward(self):
        self.state = "forward"
        self.speed = 50

    def backward(self):
        self.state = "backward"
        self.speed = 50

    def stop(self):
        self.state = "stop"
        self.speed = 0


class RobotController:
    def __init__(self):

        self.button_a = Button(1)
        self.button_b = Button(2)
        self.button_c = Button(3)

        self.led = Led(4)
        self.motor = Motor()

        # 关机状态启动
        self.enabled = False

        self.led_mode = 0
        self.motor_mode = 0

    def update(self):

        # A = 总开关
        if self.button_a.is_pressed():
            self.enabled = not self.enabled

        # 关机处理
        if not self.enabled:
            self.led.off()
            self.motor.stop()
            return

        # B = LED模式切换
        if self.button_b.is_pressed():
            self.led_mode += 1

            if self.led_mode > 2:
                self.led_mode = 0

        # C = Motor模式切换
        if self.button_c.is_pressed():
            self.motor_mode += 1

            if self.motor_mode > 2:
                self.motor_mode = 0

        # LED状态执行
        if self.led_mode == 0:
            self.led.off()

        elif self.led_mode == 1:
            self.led.on()

        elif self.led_mode == 2:
            self.led.blink()

        # Motor状态执行
        if self.motor_mode == 0:
            self.motor.stop()

        elif self.motor_mode == 1:
            self.motor.forward()

        elif self.motor_mode == 2:
            self.motor.backward()


controller = RobotController()

while True:
    controller.update()