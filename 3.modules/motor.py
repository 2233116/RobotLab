from machine import Pin,PWM
from time import sleep
FORWARD  =  1
BACKWARD = 2
STOP = 3
class Motor:
    def __init__(self,pin_num_1,pin_num_2) :
        self.pwm1 = PWM(Pin(pin_num_1),freq = 1000)
        self.pwm2 = PWM(Pin(pin_num_2), freq = 1000) 
        self.speed = 0
        self.is_running = 0
        sleep(0.001)
    def stop(self):
        self.set_speed(0)
    def set_speed(self,speed):
        if speed  > 100:
            speed = 100
        elif speed < -100 :
            speed = -100
        if speed == self.speed :
            return
        speed_1 = abs(speed)
        if speed > 0 :
            self.pwm1.duty_u16(0)
            self.pwm2.duty_u16(0)
            self.pwm1.duty_u16(int(speed_1/100*65535))
            self.is_running = True
        elif speed < 0 :
            self.pwm1.duty_u16(0)
            self.pwm2.duty_u16(0)
            self.pwm2.duty_u16(int(speed_1/100*65535)) 
            self.is_running = True
        elif speed == 0 :
            self.pwm1.duty_u16(0)
            self.pwm2.duty_u16(0)
            self.is_running = False
        self.speed = speed
        
     