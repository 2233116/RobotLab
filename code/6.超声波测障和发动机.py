from machine import Pin,PWM
FORWARD  =  1
BACKWARD = 2
STOP = 3
class Motor:
    def __init__(self,pin_num_1,pin_num_2,pin_num_3) :
        self.AIN1 = Pin(pin_num_1,Pin.OUT)
        self.AIN2 = Pin(pin_num_2,Pin.OUT)
        self.PWMA = PWM(Pin(pin_num_3),freq = 1000, duty_u16 = 0) 
        self.speed = 0
        self.direction = 0
        self.is_running = 0
    def forward(self,speed):
        self.AIN1(1)
        self.AIN2(0)
        self.set_speed(speed)
        self.direction = FORWARD
        self.is_running = True
    def backward(self,speed):
        self.AIN1(0)
        self.AIN2(1) 
        self.set_speed(speed)
        self.direction = BACKWARD
        self.is_running = True
    def stop(self):
        self.AIN1(0)
        self.AIN2(0)
        self.set_speed(0)
        self.direction = STOP
        self.is_running = False
    def set_speed(self,speed):
        if speed  > 100:
            speed = 100
        elif speed < 0 :
            speed = 0
        if speed == self.speed :
            return
        self.speed = speed
        self.PWMA.duty_u16(int(speed/100*65535))
    