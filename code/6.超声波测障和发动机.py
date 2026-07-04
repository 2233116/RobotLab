from machine import Pin
FORWARD  =  1
BACKWARD = 2
STOP = 3
class Motor:
    def __init__(self,pin_num_1,pin_num_2,pin_num_3) :
        self.AIN1 = Pin(pin_num_1,Pin.OUT)#"这几个self.pin... 写的对不对"
        self.AIN2 = Pin(pin_num_2,Pin.OUT)
        self.PWMA = Pin(pin_num_3,Pin.OUT) 
        self.speed = 
        self.direction = 0
        self.is_running = 0
    def forward(self):
        self.AIN1(1)
        self.AIN2(0)
        self.direction = FORWARD
        self.is_running = True
    def backward(self):
        self.AIN1(0)
        self.AIN2(1)
        self.direction = BACKWARD
        self.is_running = True
    def stop(self):
        self.AIN1(0)
        self.AIN2(0)
        self.direction = STOP
        self.is_running = False
    def pwm(self):
        self.PWMA()
    